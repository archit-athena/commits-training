#!/usr/bin/env python3
"""
Check available vLLM endpoints
"""

import requests

base_url = "http://10.11.7.31:8000"

# Try common endpoints
endpoints = [
    "/v1/chat/completions",
    "/chat/completions",
    "/v1/completions",
    "/completions",
    "/generate",
    "/v1/generate",
    "/api/generate",
]

print("🔍 Checking vLLM endpoints...\n")

for endpoint in endpoints:
    url = base_url + endpoint
    print(f"Testing: {url}")

    try:
        # Try GET first
        response = requests.get(url, timeout=5)
        print(f"  GET: {response.status_code} - {response.text[:100]}")
    except Exception as e:
        print(f"  GET: Error - {e}")

    try:
        # Try POST with minimal payload
        payload = {"model": "zai-org/GLM-4.6-FP8", "messages": [{"role": "user", "content": "hi"}]}
        response = requests.post(url, json=payload, timeout=5)
        print(f"  POST: {response.status_code} - {response.text[:100]}")
    except Exception as e:
        print(f"  POST: Error - {e}")

    print()

# Also check for models endpoint
print("Checking models endpoint...")
try:
    response = requests.get(f"{base_url}/v1/models", timeout=5)
    print(f"GET /v1/models: {response.status_code}")
    if response.status_code == 200:
        print(response.text)
except Exception as e:
    print(f"Error: {e}")
