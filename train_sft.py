#!/usr/bin/env python3
"""
SFT Training Script for Qwen 2.5 Coder on Rust Commit Dataset
"""

import json
import torch
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import BitsAndBytesConfig
import argparse
from pathlib import Path


def load_jsonl_dataset(dataset_path: str):
    """Load dataset from HuggingFace Hub or local JSONL file"""
    from datasets import load_dataset

    # Check if it's a local file
    if dataset_path.endswith('.jsonl') and Path(dataset_path).exists():
        data = []
        with open(dataset_path, 'r', encoding='utf-8') as f:
            for line in f:
                entry = json.loads(line.strip())
                data.append({
                    'prompt': entry['prompt'],
                    'response': entry['response']
                })
        return Dataset.from_list(data)
    else:
        # Load from HuggingFace Hub
        return load_dataset(dataset_path)


def format_prompt(prompt: str, response: str = None) -> str:
    """Format prompt-response pair for Qwen3"""
    if response:
        # Training format with response
        return f"""<|im_start|>system
You are a helpful Rust programming assistant that generates code patches based on commit messages.<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
{response}<|im_end|>"""
    else:
        # Inference format without response
        return f"""<|im_start|>system
You are a helpful Rust programming assistant that generates code patches based on commit messages.<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
"""


def tokenize_function(examples, tokenizer, max_length=2048):
    """Tokenize the dataset"""
    # Format all examples
    texts = [
        format_prompt(prompt, response)
        for prompt, response in zip(examples['prompt'], examples['response'])
    ]

    # Tokenize
    tokenized = tokenizer(
        texts,
        truncation=True,
        max_length=max_length,
        padding="max_length",  # Pad to max_length
        return_tensors=None
    )

    # Add labels (same as input_ids for causal LM)
    tokenized['labels'] = [
        [(label if label != tokenizer.pad_token_id else -100) for label in labels]
        for labels in tokenized['input_ids']
    ]

    return tokenized


def main():
    parser = argparse.ArgumentParser(description="Train Qwen3-4B on Rust commits")
    parser.add_argument("--dataset", type=str, required=True,
                       help="Path to consolidated JSONL dataset")
    parser.add_argument("--model", type=str, default="Qwen/Qwen3-4B",
                       help="Model name or path")
    parser.add_argument("--output_dir", type=str, default="./qwen-rust-sft",
                       help="Output directory for model")
    parser.add_argument("--max_length", type=int, default=4096,
                       help="Maximum sequence length")
    parser.add_argument("--batch_size", type=int, default=1,
                       help="Training batch size per device")
    parser.add_argument("--gradient_accumulation", type=int, default=4,
                       help="Gradient accumulation steps (smaller for more frequent updates)")
    parser.add_argument("--learning_rate", type=float, default=5e-6,
                       help="Learning rate (lower for full fine-tuning)")
    parser.add_argument("--num_epochs", type=int, default=3,
                       help="Number of training epochs")
    parser.add_argument("--use_4bit", action="store_true",
                       help="Use 4-bit quantization")
    parser.add_argument("--use_lora", action="store_true", default=False,
                       help="Use LoRA (default: False for full fine-tuning)")
    parser.add_argument("--lora_r", type=int, default=16,
                       help="LoRA rank")
    parser.add_argument("--lora_alpha", type=int, default=32,
                       help="LoRA alpha")
    parser.add_argument("--wandb_project", type=str, default="rust-sft",
                       help="Weights & Biases project name")
    parser.add_argument("--wandb_run_name", type=str, default=None,
                       help="Weights & Biases run name")

    args = parser.parse_args()

    print("=" * 80)
    print("🦀 Qwen3-4B Full Fine-Tuning on Rust Commits")
    print("=" * 80)
    print(f"Model: {args.model}")
    print(f"Dataset: {args.dataset}")
    print(f"Output: {args.output_dir}")
    print(f"Training Mode: {'LoRA' if args.use_lora else 'Full Fine-Tuning'}")
    print(f"Max length: {args.max_length}")
    print(f"Batch size per GPU: {args.batch_size}")
    print(f"Gradient accumulation: {args.gradient_accumulation}")
    print(f"Effective batch size: {args.batch_size * args.gradient_accumulation * 2} (2x H200)")
    print(f"Learning rate: {args.learning_rate}")
    print(f"Epochs: {args.num_epochs}")
    print(f"Use 4-bit: {args.use_4bit}")
    print("=" * 80)

    # Load dataset
    print("\n📦 Loading dataset...")
    dataset = load_jsonl_dataset(args.dataset)

    # Handle both DatasetDict and Dataset
    if hasattr(dataset, 'keys'):  # DatasetDict from HF Hub
        print(f"✓ Loaded dataset with splits: {list(dataset.keys())}")
        train_dataset = dataset['train']
        eval_dataset = dataset['test'] if 'test' in dataset else dataset['train'].train_test_split(test_size=0.05, seed=42)['test']
    else:  # Single Dataset
        print(f"✓ Loaded {len(dataset)} examples")
        split_dataset = dataset.train_test_split(test_size=0.05, seed=42)
        train_dataset = split_dataset['train']
        eval_dataset = split_dataset['test']

    print(f"✓ Train: {len(train_dataset)}, Eval: {len(eval_dataset)}")

    # Load tokenizer
    print("\n🔤 Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"
    print(f"✓ Tokenizer loaded (vocab size: {len(tokenizer)})")

    # Tokenize datasets
    print("\n⚙️  Tokenizing dataset...")
    train_dataset = train_dataset.map(
        lambda x: tokenize_function(x, tokenizer, args.max_length),
        batched=True,
        remove_columns=['prompt', 'response'],
        desc="Tokenizing train"
    )
    eval_dataset = eval_dataset.map(
        lambda x: tokenize_function(x, tokenizer, args.max_length),
        batched=True,
        remove_columns=['prompt', 'response'],
        desc="Tokenizing eval"
    )
    print("✓ Tokenization complete")

    # Load model
    print(f"\n🤖 Loading model: {args.model}")

    if args.use_4bit:
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_use_double_quant=True,
        )
        model = AutoModelForCausalLM.from_pretrained(
            args.model,
            quantization_config=bnb_config,
            device_map="auto",
            trust_remote_code=True,
            torch_dtype=torch.bfloat16,
        )
    else:
        model = AutoModelForCausalLM.from_pretrained(
            args.model,
            device_map="auto",
            trust_remote_code=True,
            torch_dtype=torch.bfloat16,
        )

    print(f"✓ Model loaded")

    # Apply LoRA
    if args.use_lora:
        print(f"\n🔧 Applying LoRA (r={args.lora_r}, alpha={args.lora_alpha})...")

        if args.use_4bit:
            model = prepare_model_for_kbit_training(model)

        lora_config = LoraConfig(
            r=args.lora_r,
            lora_alpha=args.lora_alpha,
            target_modules=[
                "q_proj", "k_proj", "v_proj", "o_proj",
                "gate_proj", "up_proj", "down_proj"
            ],
            lora_dropout=0.05,
            bias="none",
            task_type="CAUSAL_LM"
        )

        model = get_peft_model(model, lora_config)
        model.print_trainable_parameters()

    # Initialize wandb
    import os
    if args.wandb_project:
        print(f"\n📊 Initializing Weights & Biases...")
        print(f"   Project: {args.wandb_project}")
        if args.wandb_run_name:
            print(f"   Run name: {args.wandb_run_name}")
        os.environ["WANDB_PROJECT"] = args.wandb_project
        if args.wandb_run_name:
            os.environ["WANDB_RUN_NAME"] = args.wandb_run_name

    # Training arguments
    training_args = TrainingArguments(
        output_dir=args.output_dir,
        num_train_epochs=args.num_epochs,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.batch_size,
        gradient_accumulation_steps=args.gradient_accumulation,
        learning_rate=args.learning_rate,
        weight_decay=0.01,
        warmup_steps=50,
        lr_scheduler_type="cosine",
        logging_steps=1,
        save_strategy="steps",
        save_steps=300,
        eval_strategy="steps",
        eval_steps=80,
        save_total_limit=3,
        fp16=False,
        bf16=True,
        optim="adamw_torch",
        gradient_checkpointing=True,
        group_by_length=True,
        report_to="wandb" if args.wandb_project else "none",
        logging_dir=f"{args.output_dir}/logs",
        run_name=args.wandb_run_name,
    )

    # Data collator - use default padding
    from transformers import default_data_collator
    data_collator = default_data_collator

    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        data_collator=data_collator,
    )

    # Train
    print("\n🚀 Starting training...")
    print("=" * 80)
    trainer.train()

    # Save final model
    print("\n💾 Saving final model...")
    trainer.save_model(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)

    print("\n✅ Training complete!")
    print(f"📁 Model saved to: {args.output_dir}")
    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()

