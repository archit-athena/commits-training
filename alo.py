from datasets import load_dataset
import json
dataset = load_dataset("archit11/hyperswitch-rust-commits-final2")
sample_data = dataset["train"][:1]

# Print the sample data
print("Sample data:")
print(json.dumps(sample_data, indent=2))

# Clean all samples by removing "\n\n authored by" text
print("\n\nCleaning dataset...")
for split in dataset:
    for i, example in enumerate(dataset[split]):
        # Clean the prompt field if it exists
        if 'prompt' in example and example['prompt']:
            dataset[split][i]['prompt'] = example['prompt'].replace('\n\n authored by', '')
        # Clean other text fields that might contain this text
        for key in example:
            if isinstance(example[key], str):
                dataset[split][i][key] = example[key].replace('\n\n authored by', '')

print("Dataset cleaned!")
