#!/usr/bin/env python3
"""
Explore the juspay/hyperswitch dataset structure
"""

from datasets import load_dataset
import json

print("📦 Loading juspay/hyperswitch dataset...")
dataset = load_dataset("juspay/hyperswitch")

print(f"\n📊 Dataset splits: {list(dataset.keys())}")
print(f"📊 Train size: {len(dataset['train'])}")

# Get first sample
sample = dataset['train'][0]

print("\n" + "=" * 80)
print("🔍 FIRST SAMPLE STRUCTURE")
print("=" * 80)

print(f"\nKeys available: {list(sample.keys())}")

for key in sample.keys():
    value = sample[key]
    print(f"\n{'='*60}")
    print(f"KEY: {key}")
    print(f"TYPE: {type(value)}")
    print(f"{'='*60}")

    if isinstance(value, str):
        if len(value) > 500:
            print(f"{value[:500]}...\n[truncated, total length: {len(value)}]")
        else:
            print(value)
    elif isinstance(value, list):
        print(f"List with {len(value)} items")
        if len(value) > 0:
            print(f"First item: {value[0][:200] if isinstance(value[0], str) else value[0]}")
    else:
        print(value)

print("\n" + "=" * 80)
print("💾 Saving first sample to file...")
with open('juspay_sample.json', 'w') as f:
    json.dump(sample, f, indent=2)
print("Saved to: juspay_sample.json")
