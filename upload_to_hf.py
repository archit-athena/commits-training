#!/usr/bin/env python3
"""
Upload Rust Commit Dataset to Hugging Face Hub
"""

import json
import argparse
from pathlib import Path
from datasets import Dataset, DatasetDict
from huggingface_hub import HfApi, login


def load_jsonl_files(path: str):
    """Load from JSONL file or directory of JSONL files"""
    path_obj = Path(path)
    data = []

    # Check if it's a file or directory
    if path_obj.is_file():
        print(f"📂 Loading dataset from file: {path_obj}...")
        dataset_files = [path_obj]
    else:
        print(f"📂 Loading dataset files from directory: {path_obj}...")
        dataset_files = sorted(list(path_obj.glob("*.jsonl")) + list(path_obj.glob("*.rs")))

    print(f"Found {len(dataset_files)} dataset files")

    for dataset_file in dataset_files:
        with open(dataset_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    entry = json.loads(line.strip())
                    # Keep ALL fields - don't truncate anything
                    data_entry = {
                        'prompt': entry.get('prompt', ''),
                        'response': entry.get('response', '')
                    }
                    # Include metadata if present (as JSON string for HF compatibility)
                    if 'metadata' in entry:
                        data_entry['metadata'] = json.dumps(entry['metadata'])
                    data.append(data_entry)

    print(f"✓ Loaded {len(data)} examples")

    # Show sample response length stats
    if data:
        response_lengths = [len(d['response']) for d in data]
        print(f"📊 Response length stats:")
        print(f"   - Min: {min(response_lengths)} chars")
        print(f"   - Max: {max(response_lengths)} chars")
        print(f"   - Avg: {sum(response_lengths) // len(response_lengths)} chars")

    return data


def create_dataset(data):
    """Create Hugging Face Dataset with train/test split"""
    print("\n📊 Creating dataset...")

    # Create dataset
    dataset = Dataset.from_list(data)

    # Split into train/test (95/5)
    dataset_dict = dataset.train_test_split(test_size=0.05, seed=42)

    print(f"✓ Train: {len(dataset_dict['train'])} examples")
    print(f"✓ Test: {len(dataset_dict['test'])} examples")

    return dataset_dict


def upload_to_hub(dataset_dict, repo_id, token=None, private=False):
    """Upload dataset to Hugging Face Hub"""
    print(f"\n🚀 Uploading to Hugging Face Hub: {repo_id}")

    # Login if token provided
    if token:
        login(token=token)

    # Push to hub
    dataset_dict.push_to_hub(
        repo_id,
        private=private,
        commit_message="Upload Rust commit dataset from Hyperswitch"
    )

    print(f"✅ Dataset uploaded successfully!")
    print(f"🔗 View at: https://huggingface.co/datasets/{repo_id}")


def create_dataset_card(repo_id, num_examples, token=None):
    """Create a README.md for the dataset"""
    readme_content = f"""---
language:
- en
license: mit
task_categories:
- text-generation
tags:
- rust
- code
- commit-messages
- patches
- sft
size_categories:
- 1K<n<10K
---

# Rust Commit Dataset - Hyperswitch

## Dataset Description

This dataset contains Rust commit messages paired with their corresponding code patches from the [Hyperswitch](https://github.com/juspay/hyperswitch) repository.

### Dataset Summary

- **Total Examples**: {num_examples}
- **Language**: Rust
- **Source**: Hyperswitch GitHub repository
- **Format**: Prompt-response pairs for supervised fine-tuning (SFT)

### Data Fields

- `prompt`: The commit message describing the change
- `response`: The git patch/diff showing the actual code changes

### Example

```json
{{
  "prompt": "fix: update payment status handling",
  "response": "diff --git a/src/payment.rs b/src/payment.rs\\n..."
}}
```

### Usage

```python
from datasets import load_dataset

# Load dataset
dataset = load_dataset("{repo_id}")

# Access train/test splits
train_data = dataset['train']
test_data = dataset['test']

# Example
print(train_data[0]['prompt'])
print(train_data[0]['response'])
```

### Training

This dataset is designed for fine-tuning code generation models on Rust commit-to-patch generation tasks.

Example training command:
```bash
python train_sft.py \\
    --dataset {repo_id} \\
    --model Qwen/Qwen3-4B \\
    --output_dir ./qwen-rust-sft \\
    --use_4bit \\
    --use_lora
```

### Data Collection

The data was collected using PyDriller and tree-sitter for parsing Rust identifiers:
- Only commits with 20+ lines changed are included
- Rust-specific identifier tracking (functions, structs, enums, traits, impls, modules)

### Citation

If you use this dataset, please cite the Hyperswitch repository:
```
@misc{{hyperswitch2024,
  title={{Hyperswitch}},
  author={{Juspay}},
  year={{2024}},
  url={{https://github.com/juspay/hyperswitch}}
}}
```

### License

This dataset follows the same license as the Hyperswitch project.
"""

    print("\n📝 Creating dataset card...")

    api = HfApi(token=token)
    api.upload_file(
        path_or_fileobj=readme_content.encode(),
        path_in_repo="README.md",
        repo_id=repo_id,
        repo_type="dataset",
    )

    print("✓ Dataset card created")


def main():
    parser = argparse.ArgumentParser(
        description="Upload Rust commit dataset to Hugging Face Hub"
    )
    parser.add_argument(
        "--dataset_dir",
        type=str,
        default="hyperswitch_dataset",
        help="Directory containing JSONL files"
    )
    parser.add_argument(
        "--repo_id",
        type=str,
        required=True,
        help="Hugging Face repo ID (e.g., username/dataset-name)"
    )
    parser.add_argument(
        "--token",
        type=str,
        help="Hugging Face API token (or set HF_TOKEN env var)"
    )
    parser.add_argument(
        "--private",
        action="store_true",
        help="Make dataset private"
    )

    args = parser.parse_args()

    print("=" * 80)
    print("🤗 Hugging Face Dataset Uploader")
    print("=" * 80)
    print(f"📂 Dataset directory: {args.dataset_dir}")
    print(f"🎯 Target repo: {args.repo_id}")
    print(f"🔒 Private: {args.private}")
    print("=" * 80)

    # Load data
    data = load_jsonl_files(args.dataset_dir)

    # Create dataset
    dataset_dict = create_dataset(data)

    # Upload to hub
    upload_to_hub(dataset_dict, args.repo_id, args.token, args.private)

    # Create dataset card
    create_dataset_card(args.repo_id, len(data), args.token)

    print("\n" + "=" * 80)
    print("✅ All done!")
    print(f"📦 Dataset available at: https://huggingface.co/datasets/{args.repo_id}")
    print("\n💡 You can now load it anywhere with:")
    print(f'   from datasets import load_dataset')
    print(f'   dataset = load_dataset("{args.repo_id}")')
    print("=" * 80)


if __name__ == "__main__":
    main()
