from datasets import load_dataset
import json
dataset = load_dataset("archit11/hyperswitch-rust-commits-final2")
sample_data = dataset["train"][:10]
