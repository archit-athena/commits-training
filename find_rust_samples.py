#!/usr/bin/env python3
"""
Find samples with significant Rust code changes and product context
"""

from datasets import load_dataset
import json
import re

print("📦 Loading juspay/hyperswitch dataset...")
dataset = load_dataset("juspay/hyperswitch")

print("\n🔍 Finding samples with Rust code changes...")

rust_samples = []
for i, sample in enumerate(dataset['train']):
    patch = sample.get('patch', '')
    problem = sample.get('problem_statement', '')

    # Check if it has Rust file changes
    if '.rs' in patch and len(patch) > 500:
        # Count files modified
        files = re.findall(r'diff --git a/(.+?) b/', patch)
        rust_files = [f for f in files if f.endswith('.rs')]

        if rust_files:
            rust_samples.append({
                'index': i,
                'instance_id': sample['instance_id'],
                'problem_length': len(problem),
                'patch_length': len(patch),
                'rust_files': rust_files,
                'num_files': len(rust_files)
            })

print(f"\n✅ Found {len(rust_samples)} samples with Rust changes")

# Show first 10
print("\n📊 Top 10 samples with most Rust files changed:")
rust_samples_sorted = sorted(rust_samples, key=lambda x: x['num_files'], reverse=True)

for i, s in enumerate(rust_samples_sorted[:10]):
    print(f"\n{i+1}. Index {s['index']} - {s['instance_id']}")
    print(f"   Files: {s['num_files']} Rust files")
    print(f"   Problem: {s['problem_length']} chars")
    print(f"   Patch: {s['patch_length']} chars")

# Get a good example - mid-size with multiple files
good_examples = [s for s in rust_samples_sorted if 2 <= s['num_files'] <= 5 and s['problem_length'] > 100]

if good_examples:
    print("\n" + "="*80)
    print("📌 GOOD EXAMPLE FOR ANALYSIS")
    print("="*80)

    example_idx = good_examples[0]['index']
    example = dataset['train'][example_idx]

    print(f"\nInstance ID: {example['instance_id']}")
    print(f"\n{'='*60}")
    print("PROBLEM STATEMENT:")
    print(f"{'='*60}")
    print(example['problem_statement'])

    print(f"\n{'='*60}")
    print("HINTS/PR DESCRIPTION:")
    print(f"{'='*60}")
    print(example['hints_text'][:800] if len(example['hints_text']) > 800 else example['hints_text'])

    print(f"\n{'='*60}")
    print("PATCH (first 1500 chars):")
    print(f"{'='*60}")
    print(example['patch'][:1500])

    # Save full example
    with open('rust_example_full.json', 'w') as f:
        json.dump(example, f, indent=2)
    print(f"\n💾 Saved full example to: rust_example_full.json")
