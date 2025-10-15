#!/usr/bin/env python3
"""
SFT Training Script for Qwen 2.5 Coder on Rust Commit Dataset
"""

import json
import os
import torch
from datasets import Dataset, load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    BitsAndBytesConfig,
    default_data_collator
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
import argparse
from pathlib import Path


def load_jsonl_dataset(dataset_path: str):
    if dataset_path.endswith('.jsonl') and Path(dataset_path).exists():
        data = []
        with open(dataset_path, 'r', encoding='utf-8') as f:
            for line in f:
                entry = json.loads(line.strip())
                data.append({'prompt': entry['prompt'], 'response': entry['response']})
        return Dataset.from_list(data)
    else:
        return load_dataset(dataset_path)


def generate_prompt_basic(commit_message: str) -> str:
    return f"Generate the Rust identifiers (functions, structs, enums, traits, impls, mods) that need to be changed based on the following commit message:\n\n{commit_message}"


def generate_prompt_detailed(commit_message: str) -> str:
    return f"""Given the following commit message, identify which Rust identifiers need to be modified:

Commit Message: {commit_message}

Please list the identifiers (functions, structs, enums, traits, impl blocks, modules) that should be added, removed, or modified."""


def generate_prompt_contextual(commit_message: str) -> str:
    return f"""You are a Rust expert. Based on the commit message below, determine which identifiers need to be changed:

Commit Message:
{commit_message}

Provide the list of identifiers (functions, structs, enums, traits, impls, mods) that need to be added or removed."""


def generate_prompt_structured(commit_message: str) -> str:
    return f"""Task: Identify Rust identifiers to change based on commit message

Commit Message:
{commit_message}

Requirements:
- List all identifiers that need to be added or removed
- Include functions, structs, enums, traits, impl blocks, and modules
- Specify whether each identifier should be added or removed

Identifiers:"""


PROMPT_TEMPLATES = {
    'basic': generate_prompt_basic,
    'detailed': generate_prompt_detailed,
    'contextual': generate_prompt_contextual,
    'structured': generate_prompt_structured,
}


def format_prompt(prompt: str, response: str = None, identifier: str = 'basic') -> str:
    if identifier in PROMPT_TEMPLATES and not prompt.startswith('Generate'):
        prompt = PROMPT_TEMPLATES[identifier](prompt)

    if response:
        return f"""<|im_start|>system
You are a helpful Rust programming assistant that identifies which identifiers (functions, structs, enums, traits, impl blocks, modules) need to be changed based on commit messages.<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
{response}<|im_end|>"""
    else:
        return f"""<|im_start|>system
You are a helpful Rust programming assistant that identifies which identifiers (functions, structs, enums, traits, impl blocks, modules) need to be changed based on commit messages.<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
"""


def tokenize_function(examples, tokenizer, max_length=2048, prompt_identifier='basic'):
    texts = [
        format_prompt(prompt, response, identifier=prompt_identifier)
        for prompt, response in zip(examples['prompt'], examples['response'])
    ]

    tokenized = tokenizer(
        texts,
        truncation=True,
        max_length=max_length,
        padding="max_length",
        return_tensors=None
    )

    tokenized['labels'] = [
        [(label if label != tokenizer.pad_token_id else -100) for label in labels]
        for labels in tokenized['input_ids']
    ]

    return tokenized


def main():
    parser = argparse.ArgumentParser(description="Train Qwen3-4B on Rust commits")
    parser.add_argument("--dataset", type=str, required=True)
    parser.add_argument("--model", type=str, default="Qwen/Qwen3-4B")
    parser.add_argument("--output_dir", type=str, default="./qwen-rust-sft")
    parser.add_argument("--max_length", type=int, default=4096)
    parser.add_argument("--bsz", type=int, default=1)
    parser.add_argument("--gradient_accumulation", type=int, default=4)
    parser.add_argument("--prompt_template", type=str, default="basic",
                       choices=['basic', 'detailed', 'contextual', 'structured'])
    parser.add_argument("--learning_rate", type=float, default=5e-6)
    parser.add_argument("--num_epochs", type=int, default=3)
    parser.add_argument("--use_4bit", action="store_true")
    parser.add_argument("--use_lora", action="store_true", default=False)
    parser.add_argument("--lora_r", type=int, default=16)
    parser.add_argument("--lora_alpha", type=int, default=32)
    parser.add_argument("--wandb_project", type=str, default="rust-sft")
    parser.add_argument("--wandb_run_name", type=str, default=None)

    args = parser.parse_args()

    dataset = load_jsonl_dataset(args.dataset)

    if hasattr(dataset, 'keys'):
        train_dataset = dataset['train']
        eval_dataset = dataset['test'] if 'test' in dataset else dataset['train'].train_test_split(test_size=0.05, seed=42)['test']
    else:
        split_dataset = dataset.train_test_split(test_size=0.05, seed=42)
        train_dataset = split_dataset['train']
        eval_dataset = split_dataset['test']

    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    train_dataset = train_dataset.map(
        lambda x: tokenize_function(x, tokenizer, args.max_length, args.prompt_template),
        batched=True,
        remove_columns=['prompt', 'response'],
        desc="Tokenizing train"
    )
    eval_dataset = eval_dataset.map(
        lambda x: tokenize_function(x, tokenizer, args.max_length, args.prompt_template),
        batched=True,
        remove_columns=['prompt', 'response'],
        desc="Tokenizing eval"
    )

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
            attn_implementation="flash_attention_2",
        )
    else:
        model = AutoModelForCausalLM.from_pretrained(
            args.model,
            device_map="auto",
            trust_remote_code=True,
            torch_dtype=torch.bfloat16,
            attn_implementation="flash_attention_2",
        )

    if args.use_lora:
        if args.use_4bit:
            model = prepare_model_for_kbit_training(model)

        lora_config = LoraConfig(
            r=args.lora_r,
            lora_alpha=args.lora_alpha,
            target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
            lora_dropout=0.05,
            bias="none",
            task_type="CAUSAL_LM"
        )
        model = get_peft_model(model, lora_config)
        model.print_trainable_parameters()

    if args.wandb_project:
        os.environ["WANDB_PROJECT"] = args.wandb_project
        if args.wandb_run_name:
            os.environ["WANDB_RUN_NAME"] = args.wandb_run_name

    training_args = TrainingArguments(
        output_dir=args.output_dir,
        num_train_epochs=args.num_epochs,
        per_device_train_batch_size=args.bsz,
        per_device_eval_batch_size=args.bsz,
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

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        data_collator=default_data_collator,
    )

    trainer.train()
    trainer.save_model(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)


if __name__ == "__main__":
    main()
