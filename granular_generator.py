#!/usr/bin/env python3
"""
granular_generator.py - Break down large commits into granular pairs using vLLM
"""

import argparse
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import traceback
import re

try:
    from datasets import load_dataset
except ImportError:
    print("❌ datasets not installed. Installing...")
    import subprocess
    subprocess.check_call(["pip", "install", "datasets"])
    from datasets import load_dataset

try:
    import requests
except ImportError:
    print("❌ requests not installed. Installing...")
    import subprocess
    subprocess.check_call(["pip", "install", "requests"])
    import requests


class vLLMClient:
    """Client for interacting with vLLM server"""

    def __init__(self, base_url: str = "http://10.11.7.31:8000/v1", model: str = "zai-org/GLM-4.6-FP8", timeout: int = 300):
        self.base_url = base_url
        self.model = model
        self.timeout = timeout
        self.chat_endpoint = f"{base_url}/chat/completions"

    def chat_completion(self, messages: List[Dict[str, str]],
                       temperature: float = 0.7,
                       max_tokens: int = 2048) -> Optional[str]:
        """Send a chat completion request to vLLM server"""
        try:
            payload = {
                "model": self.model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens
            }

            response = requests.post(
                self.chat_endpoint,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=self.timeout
            )

            response.raise_for_status()
            result = response.json()

            if "choices" in result and len(result["choices"]) > 0:
                return result["choices"][0]["message"]["content"]
            return None

        except requests.exceptions.RequestException as e:
            print(f"❌ Error calling vLLM API: {e}")
            return None
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return None


class GranularDatasetGenerator:
    """Generate granular commit-patch pairs from large commits"""

    def __init__(self, dataset_name: str, output_dir: str = "granular_dataset",
                 vllm_url: str = "http://10.11.7.31:8000/v1",
                 model: str = "meta-llama/Llama-3.1-8B-Instruct",
                 min_files: int = 5,
                 max_workers: int = 4):
        self.dataset_name = dataset_name
        self.output_dir = Path(output_dir)
        self.vllm_client = vLLMClient(base_url=vllm_url, model=model)
        self.min_files = min_files  # Minimum files to consider a commit "large"
        self.max_workers = max_workers
        self.errors = []

    def count_files_in_response(self, response: str) -> int:
        """Count number of files mentioned in the response"""
        # Count lines that start with **filename.rs**
        files = re.findall(r'\*\*([^*]+\.rs)\*\*', response)
        return len(files)

    def is_large_commit(self, example: Dict[str, str]) -> bool:
        """Determine if a commit is large enough to break down"""
        file_count = self.count_files_in_response(example['response'])
        return file_count >= self.min_files

    def create_breakdown_prompt(self, prompt: str, response: str) -> List[Dict[str, str]]:
        """Create a prompt for the LLM to break down a large commit"""
        system_message = """You are an expert at analyzing Git commits. Break down large commits into 2-3 smaller, focused commits.

Return ONLY a JSON array like this:
[
  {"prompt": "feat: add auth", "response": "Files to modify:\\n\\n**auth.rs**\\n  Add:\\n    - function: pub::validate"},
  {"prompt": "feat: add token", "response": "Files to modify:\\n\\n**token.rs**\\n  Add:\\n    - function: pub::generate"}
]"""

        user_message = f"""Split this commit into 2-3 focused changes. Return ONLY JSON:

{prompt}

{response}"""

        return [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]

    def parse_llm_response(self, llm_output: str) -> Optional[List[Dict[str, str]]]:
        """Parse the LLM's JSON response"""
        try:
            # Try to extract JSON from the response
            # Sometimes the model adds extra text, so we find the JSON array
            json_match = re.search(r'\[\s*\{.*?\}\s*\]', llm_output, re.DOTALL)
            if json_match:
                json_str = json_match.group(0)
                parsed = json.loads(json_str)
                return parsed

            # If no match, try parsing the whole thing
            return json.loads(llm_output)
        except json.JSONDecodeError as e:
            print(f"❌ Failed to parse LLM response as JSON: {e}")
            print(f"Response was: {llm_output[:200]}...")
            return None

    def break_down_commit(self, example: Dict[str, str]) -> List[Dict[str, str]]:
        """Use LLM to break down a large commit into smaller ones"""
        messages = self.create_breakdown_prompt(example['prompt'], example['response'])

        llm_response = self.vllm_client.chat_completion(
            messages=messages,
            temperature=0.3,  # Lower temperature for more consistent formatting
            max_tokens=2048  # Reduced for faster generation
        )

        if not llm_response:
            return [example]  # Return original if LLM fails

        parsed_commits = self.parse_llm_response(llm_response)

        if not parsed_commits or len(parsed_commits) == 0:
            return [example]  # Return original if parsing fails

        return parsed_commits

    def process_example(self, example: Dict[str, str], idx: int) -> List[Dict[str, str]]:
        """Process a single example, breaking it down if needed"""
        try:
            if self.is_large_commit(example):
                # Break down large commit
                broken_down = self.break_down_commit(example)
                return broken_down
            else:
                # Keep small commits as-is
                return [example]
        except Exception as e:
            error_msg = f"Error processing example {idx}: {str(e)}"
            self.errors.append(error_msg)
            return [example]  # Return original on error

    def save_as_jsonl(self, examples: List[Dict[str, str]], filename: Path):
        """Save examples as JSONL format"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                for example in examples:
                    json.dump(example, f, ensure_ascii=False)
                    f.write('\n')
        except Exception as e:
            print(f"Error saving JSONL {filename}: {e}")

    def create_statistics_report(self, original_count: int, granular_count: int,
                                large_commits: int):
        """Create a statistics report"""
        try:
            report_file = self.output_dir / "statistics.md"
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write(f"# Granular Dataset Generation Report\n\n")
                f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write(f"## Summary Statistics\n\n")
                f.write(f"- **Original Dataset Size:** {original_count:,} examples\n")
                f.write(f"- **Granular Dataset Size:** {granular_count:,} examples\n")
                f.write(f"- **Large Commits Broken Down:** {large_commits:,}\n")
                f.write(f"- **Expansion Factor:** {granular_count / original_count:.2f}x\n\n")

                if self.errors:
                    f.write(f"## Errors\n\n")
                    f.write(f"- **Total Errors:** {len(self.errors)}\n\n")
                    for error in self.errors[:10]:  # Show first 10 errors
                        f.write(f"- {error}\n")
                    if len(self.errors) > 10:
                        f.write(f"\n... and {len(self.errors) - 10} more errors\n")

            print(f"📄 Created statistics report: {report_file.name}")
        except Exception as e:
            print(f"Error creating statistics report: {e}")

    def generate(self):
        """Main generation process"""
        try:
            # Setup
            self.output_dir.mkdir(parents=True, exist_ok=True)

            print(f"📦 Loading dataset: {self.dataset_name}")
            dataset = load_dataset(self.dataset_name)

            train_data = dataset['train']
            print(f"📊 Dataset loaded: {len(train_data)} examples\n")

            # Process examples
            print(f"⚡ Processing examples with {self.max_workers} workers...\n")

            all_granular_examples = []
            large_commit_count = 0

            # Sequential processing with progress bar
            with tqdm(total=len(train_data), desc="Processing", unit="commit") as pbar:
                for idx, example in enumerate(train_data):
                    is_large = self.is_large_commit(example)
                    if is_large:
                        large_commit_count += 1

                    granular_examples = self.process_example(example, idx)
                    all_granular_examples.extend(granular_examples)

                    pbar.update(1)
                    pbar.set_postfix({
                        'large': large_commit_count,
                        'total_out': len(all_granular_examples)
                    })

            # Save granular dataset
            print(f"\n💾 Saving granular dataset...")
            output_file = self.output_dir / "granular_dataset.jsonl"
            self.save_as_jsonl(all_granular_examples, output_file)

            # Create statistics report
            print(f"📝 Creating statistics report...")
            self.create_statistics_report(
                len(train_data),
                len(all_granular_examples),
                large_commit_count
            )

            print(f"\n✅ Generation complete!")
            print(f"📁 Output directory: {self.output_dir.absolute()}")
            print(f"📊 Original dataset: {len(train_data)} examples")
            print(f"📊 Granular dataset: {len(all_granular_examples)} examples")
            print(f"🔄 Expansion factor: {len(all_granular_examples) / len(train_data):.2f}x")
            print(f"📦 Large commits processed: {large_commit_count}")
            if self.errors:
                print(f"⚠️  Errors encountered: {len(self.errors)}")

        except Exception as e:
            print(f"\n❌ Fatal error: {e}")
            traceback.print_exc()


def main():
    parser = argparse.ArgumentParser(
        description="Break down large commits into granular pairs using vLLM",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate granular dataset from HuggingFace
  %(prog)s archit11/hyperswitch-rust-commits-final2

  # Custom settings
  %(prog)s archit11/hyperswitch-rust-commits-final2 -o output_dir -m 3 --vllm-url http://localhost:8000/v1
        """
    )

    parser.add_argument("dataset_name", help="HuggingFace dataset name (e.g., archit11/hyperswitch-rust-commits-final2)")
    parser.add_argument("-o", "--output", default="granular_dataset",
                       help="Output directory (default: granular_dataset)")
    parser.add_argument("-m", "--min-files", type=int, default=5,
                       help="Minimum files to consider commit 'large' (default: 5)")
    parser.add_argument("--vllm-url", default="http://10.11.7.31:8000/v1",
                       help="vLLM server URL (default: http://10.11.7.31:8000/v1)")
    parser.add_argument("--model", default="zai-org/GLM-4.6-FP8",
                       help="Model name (default: zai-org/GLM-4.6-FP8)")
    parser.add_argument("--max-workers", type=int, default=1,
                       help="Max parallel workers (default: 1)")

    args = parser.parse_args()

    print("=" * 80)
    print("🦀 Granular Rust Commit Dataset Generator")
    print("=" * 80)
    print(f"📍 Dataset: {args.dataset_name}")
    print(f"🤖 vLLM URL: {args.vllm_url}")
    print(f"📏 Min files threshold: {args.min_files}")
    print("=" * 80)

    generator = GranularDatasetGenerator(
        dataset_name=args.dataset_name,
        output_dir=args.output,
        vllm_url=args.vllm_url,
        model=args.model,
        min_files=args.min_files,
        max_workers=args.max_workers
    )

    generator.generate()


if __name__ == "__main__":
    main()
