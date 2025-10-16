# app.py
import os
import asyncio
import json
from typing import Optional
from urllib.parse import quote

import httpx
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

app = FastAPI(title="DeepWiki MCP Agent")

# DeepWiki configuration
DEEPWIKI_MCP_SSE_URL = os.getenv("DEEPWIKI_MCP_SSE_URL", "https://mcp.deepwiki.com/sse")
QUERY_TIMEOUT_S = int(os.getenv("QUERY_TIMEOUT_S", "30"))  # seconds
DEFAULT_USER_AGENT = "deepwiki-mcp-agent/1.0 (+https://example.com)"

# OpenAI-compatible API configuration
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "http://10.11.7.31:8000/v1")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "dummy")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "zai-org/GLM-4.6-FP8")

# Initialize OpenAI client
client = AsyncOpenAI(
    base_url=OPENAI_BASE_URL,
    api_key=OPENAI_API_KEY,
)

class Query(BaseModel):
    repo: str
    prompt: str
    timeout_s: Optional[int] = None

async def _stream_sse_and_aggregate(url: str, headers: dict, timeout_s: int) -> str:
    """
    Connect to an SSE endpoint using httpx and aggregate data: lines into text.
    This function is resilient to the common SSE format:
      - Lines beginning with 'data: ' are appended.
      - Also attempts to parse JSON 'data' and extract likely fields like 'content' or 'chunk'.
    Returns aggregated text (string).
    """
    aggregated_parts = []
    # Use a short overall timeout sentinel using asyncio.wait_for
    async def _inner():
        async with httpx.AsyncClient(timeout=None, headers=headers) as client:
            # Stream the response
            async with client.stream("GET", url) as resp:
                if resp.status_code >= 400:
                    # try to get small body
                    text = await resp.aread()
                    raise HTTPException(status_code=502, detail=f"Upstream SSE returned {resp.status_code}: {text[:200]!r}")
                # accumulate event data until end
                event_lines = []
                async for raw_chunk in resp.aiter_bytes():
                    # raw_chunk is bytes; decode
                    try:
                        chunk = raw_chunk.decode("utf-8")
                    except Exception:
                        # skip undecodable bytes
                        continue
                    # SSE sends text with newline separators, but chunk boundaries may split lines
                    # We'll split into lines and process
                    lines = chunk.splitlines(keepends=True)
                    for line in lines:
                        # common SSE event separators are '\n' or '\r\n'; handle them gracefully
                        stripped = line.strip("\r\n")
                        if stripped == "":
                            # blank line => event boundary; process event_lines
                            if event_lines:
                                # join event lines and extract data:
                                data_lines = [l[len("data:"):].lstrip() if l.startswith("data:") else l for l in event_lines if l.startswith("data:") or l.startswith("event:")]
                                # prefer 'data:' lines
                                if data_lines:
                                    # join and try parse JSON
                                    joined = "\n".join([l[len("data:"):].lstrip() if l.startswith("data:") else l for l in event_lines])
                                    joined = joined.strip()
                                    # Try JSON
                                    parsed = None
                                    try:
                                        parsed = json.loads(joined)
                                    except Exception:
                                        parsed = None

                                    if parsed:
                                        # heuristics: look for common fields
                                        if isinstance(parsed, dict):
                                            # possible keys: 'content','chunk','text','message','final'
                                            for key in ("content", "chunk", "text", "message", "final", "answer"):
                                                if key in parsed:
                                                    aggregated_parts.append(str(parsed[key]))
                                                    break
                                            else:
                                                # fallback: use whole JSON string
                                                aggregated_parts.append(json.dumps(parsed))
                                        else:
                                            # array or primitive -> append string
                                            aggregated_parts.append(str(parsed))
                                    else:
                                        # not json, append joined text
                                        aggregated_parts.append(joined)
                                # reset event_lines
                                event_lines = []
                            continue

                        # accumulate line for the event
                        event_lines.append(stripped)

                        # Some SSE servers send single-line data events frequently without an empty line.
                        # Detect obvious 'data: <something>' lines and append immediately.
                        if stripped.startswith("data:"):
                            payload = stripped[len("data:"):].lstrip()
                            # try quick parse
                            parsed = None
                            try:
                                parsed = json.loads(payload)
                            except Exception:
                                parsed = None

                            if parsed:
                                if isinstance(parsed, dict):
                                    # heuristics same as above
                                    appended = False
                                    for key in ("content", "chunk", "text", "message", "final", "answer"):
                                        if key in parsed:
                                            aggregated_parts.append(str(parsed[key]))
                                            appended = True
                                            break
                                    if not appended:
                                        aggregated_parts.append(json.dumps(parsed))
                                else:
                                    aggregated_parts.append(str(parsed))
                            else:
                                # not json; append raw payload string
                                aggregated_parts.append(payload)
                # end stream loop
    try:
        await asyncio.wait_for(_inner(), timeout=timeout_s)
    except asyncio.TimeoutError:
        # timeout: just return what we have so far
        pass
    except HTTPException:
        # re-raise HTTPException to outer scope
        raise
    except Exception:
        # any other network error, ignore but continue with whatever aggregated
        pass

    # join aggregated parts into final string
    final_text = "\n".join([p for p in aggregated_parts if p is not None]).strip()
    return final_text

@app.post("/query")
async def query_endpoint(q: Query, request: Request):
    """
    POST /query
    Body: { "repo": "owner/name", "prompt": "question", "timeout_s": optional }
    Response: { "prompt": "...", "response": "final answer" }
    """
    repo = q.repo.strip()
    prompt = q.prompt.strip()
    timeout_s = q.timeout_s if q.timeout_s is not None else QUERY_TIMEOUT_S

    if not repo or not prompt:
        raise HTTPException(status_code=400, detail="Please provide non-empty 'repo' and 'prompt' fields")

    # Build SSE URL for deepwiki; adjust tool and param names to match your DeepWiki MCP server.
    # Many MCP SSE endpoints accept query params like tool=ask_question, repo=..., question=...
    sse_url = f"{DEEPWIKI_MCP_SSE_URL}?tool=ask_question&repo={quote(repo)}&question={quote(prompt)}"

    headers = {
        "User-Agent": DEFAULT_USER_AGENT,
        "Accept": "text/event-stream",
    }

    # If the incoming request had an Authorization header (optional), forward it upstream
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]

    try:
        aggregated = await _stream_sse_and_aggregate(sse_url, headers=headers, timeout_s=timeout_s)
    except HTTPException as he:
        raise he
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Failed to talk to DeepWiki SSE: {exc}")

    # If nothing was produced, return helpful message
    if not aggregated:
        # return empty response but keep format
        return {"prompt": prompt, "response": ""}

    # Return final prompt-response pair
    return {"prompt": prompt, "response": aggregated}


@app.post("/generate")
async def generate_endpoint(q: Query):
    """
    POST /generate
    Body: { "repo": "owner/name", "prompt": "question", "timeout_s": optional }
    Response: { "prompt": "...", "response": "answer from GLM-4.6-FP8" }

    Uses the OpenAI-compatible GLM-4.6-FP8 model for generation.
    """
    repo = q.repo.strip()
    prompt = q.prompt.strip()

    if not repo or not prompt:
        raise HTTPException(status_code=400, detail="Please provide non-empty 'repo' and 'prompt' fields")

    try:
        # Create messages for the model
        messages = [
            {
                "role": "system",
                "content": f"You are an expert assistant answering questions about the {repo} repository. Provide accurate, helpful answers based on your knowledge."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

        # Call OpenAI-compatible API
        response = await client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=messages,
            temperature=0.7,
            max_tokens=2048,
        )

        answer = response.choices[0].message.content.strip()

        return {"prompt": prompt, "response": answer}

    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to generate response: {exc}")

