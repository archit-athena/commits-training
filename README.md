# Commits Training - Dataset Generation Pipeline

## Quick Start

### Generate Dataset
```bash
python3 generate.py https://github.com/juspay/hyperswitch \
  -f sft -m 100 -o hyperswitch_final -b main
```
(-m flag = minimum lines changed to include commit)

### Train Model
```bash
python3 train_sft.py \
  --dataset archit11/hyperswitch-rust-commits-final2 \
  --model Qwen/Qwen3-4B \
  --output_dir ./qwen-rust-full-ft \
  --batch_size 2 \
  --gradient_accumulation 2 \
  --learning_rate 5e-6 \
  --num_epochs 2 \
  --wandb_project rust-hyperswitch-fullft
```

---

## Key Differences Between Scripts

### Data Generation
- **`generate.py`**: Tree-sitter AST parsing, detailed identifiers (pub/private, async/unsafe)
- **`gen_ctx.py`**: Simple git show -U50, more context, no identifier parsing
- **`gen_full.py`**: **BEST** - Combines both (tree-sitter identifiers + full context)

### Data Collection
- **`gather_pr_issues.py`**: Scrapes GitHub PRs/Issues for product context

### Merging & Transformation
- **`merge_datasets.py`**: Merges PRs + commits by SHA matching
- **`smart_merge.py`**: **BETTER** - Matches by PR number (#1234) instead of SHA
- **`enhanced_transformer.py`**: Extracts architectural patterns (API/DB/domain layers)
- **`granular_generator.py`**: LLM-powered transform to product-focused queries
- **`transform_to_natural.py`**: LLM-powered natural language explanations

### Which to Use?
**For best results**: `gen_full.py` → `smart_merge.py` → `transform_to_natural.py` → `train_sft.py`

---

See [FILE_DOCUMENTATION.md](FILE_DOCUMENTATION.md) for complete details.
