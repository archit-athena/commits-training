#!/usr/bin/env python3
"""
Transform mechanical commit-style responses into natural, explanatory responses

Uses LLM to convert:
FROM: "Files to modify:\n**file.rs**\n  Add:\n    - function: pub::foo"
TO: "To implement this, modify file.rs by adding the foo() function which handles..."
"""

import json
import argparse
from pathlib import Path
from tqdm import tqdm
from typing import Dict, Optional
import sys

sys.path.append(str(Path(__file__).parent))
from test_vllm import vLLMClient


class NaturalTransformer:
    """Transform mechanical responses to natural explanations"""

    def __init__(self, vllm_url: str = "http://10.11.7.31:8000/v1",
                 model: str = "zai-org/GLM-4.6-FP8"):
        self.vllm_client = vLLMClient(base_url=vllm_url, model=model)

    def create_transformation_prompt(self, prompt: str, response: str) -> list:
        """Create prompt to transform mechanical response to natural explanation"""

        system_message = """You are an expert at explaining code changes in natural, developer-friendly language.

Your task: Transform technical file/function lists into clear, actionable explanations.

INPUT STYLE (Mechanical):
```
Files to modify:

**crates/api_models/src/payments.rs**
  Add:
    - function: pub::get_payment_methods
    - struct: pub::PaymentMethodRequest
  Remove:
    - function: private::old_helper

**crates/router/src/core/payments.rs**
  Add:
    - function: pub::filter_by_status
```

OUTPUT STYLE (Natural & Explanatory):
```
To implement this feature, you'll need to make changes across the payment handling layers:

**API Layer** (`crates/api_models/src/payments.rs`):
- Add `get_payment_methods()` - fetches and returns available payment methods for the merchant
- Create `PaymentMethodRequest` struct - defines the request schema with validation
- Remove the deprecated `old_helper()` function - replaced by new payment flow

**Core Business Logic** (`crates/router/src/core/payments.rs`):
- Add `filter_by_status()` - enables filtering payments by their current status (pending, completed, etc.)
- This integrates with the existing payment processing pipeline
```

RULES:
1. Use natural language, not lists
2. Explain WHAT each change does (briefly)
3. Group by architectural layer with clear headers
4. Be concise but informative
5. Focus on developer understanding, not mechanical precision
6. Keep file paths for reference but explain the purpose

Return ONLY the transformed response text, no JSON wrapper."""

        user_message = f"""Transform this mechanical response into a natural, explanatory format:

TASK/QUERY:
{prompt}

MECHANICAL RESPONSE TO TRANSFORM:
{response}

Transform this into natural, developer-friendly explanation:"""

        return [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]

    def transform_response(self, prompt: str, response: str) -> str:
        """Transform a single response using LLM"""
        messages = self.create_transformation_prompt(prompt, response)

        llm_response = self.vllm_client.chat_completion(
            messages=messages,
            temperature=0.3,
            max_tokens=2048
        )

        if llm_response:
            return llm_response.strip()
        else:
            return response  # Fallback to original

    def transform_dataset(self, input_file: Path, output_file: Path, max_samples: Optional[int] = None):
        """Transform entire dataset"""
        print(f"📖 Reading dataset from {input_file}...")

        samples = []
        with open(input_file, 'r') as f:
            for line in f:
                if line.strip():
                    samples.append(json.loads(line))

        if max_samples:
            samples = samples[:max_samples]

        print(f"✅ Loaded {len(samples)} samples")
        print(f"\n🔄 Transforming responses...")

        transformed = []
        errors = 0

        for sample in tqdm(samples, desc="Transforming"):
            try:
                original_prompt = sample['prompt']
                original_response = sample['response']

                # Transform the response
                natural_response = self.transform_response(original_prompt, original_response)

                transformed.append({
                    'prompt': original_prompt,
                    'response': natural_response,
                    'metadata': sample.get('metadata', {})
                })

            except Exception as e:
                print(f"\n❌ Error transforming sample: {e}")
                # Keep original on error
                transformed.append(sample)
                errors += 1

        # Save transformed dataset
        print(f"\n💾 Saving transformed dataset to {output_file}...")
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'w') as f:
            for sample in transformed:
                f.write(json.dumps(sample, ensure_ascii=False) + '\n')

        print(f"\n✅ Transformation complete!")
        print(f"📊 Transformed: {len(transformed)} samples")
        print(f"⚠️  Errors: {errors}")


def main():
    parser = argparse.ArgumentParser(
        description="Transform mechanical responses to natural explanations using LLM"
    )
    parser.add_argument("input_file", help="Input JSONL file")
    parser.add_argument("-o", "--output", default="transformed_dataset.jsonl",
                       help="Output file (default: transformed_dataset.jsonl)")
    parser.add_argument("--vllm-url", default="http://10.11.7.31:8000/v1",
                       help="vLLM server URL")
    parser.add_argument("--model", default="zai-org/GLM-4.6-FP8",
                       help="Model name")
    parser.add_argument("--max-samples", type=int,
                       help="Max samples to transform (for testing)")

    args = parser.parse_args()

    print("=" * 80)
    print("✨ Natural Language Transformer")
    print("=" * 80)
    print(f"📁 Input: {args.input_file}")
    print(f"📁 Output: {args.output}")
    print(f"🤖 Model: {args.model}")
    print("=" * 80)

    transformer = NaturalTransformer(
        vllm_url=args.vllm_url,
        model=args.model
    )

    transformer.transform_dataset(
        input_file=Path(args.input_file),
        output_file=Path(args.output),
        max_samples=args.max_samples
    )


if __name__ == "__main__":
    main()
