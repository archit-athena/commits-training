# Commits Training - File Documentation

Comprehensive documentation explaining what each file does, how it generates datasets, and key differences.

---

## Table of Contents

1. [Key Implementation Differences](#key-implementation-differences)
2. [Data Generation Scripts](#1-data-generation-scripts)
3. [Data Collection Scripts](#2-data-collection-scripts)
4. [Data Merging & Transformation](#3-data-merging--transformation)
5. [Training Scripts](#4-training-scripts)
6. [Upload Utilities](#5-upload-utilities)
7. [Testing & Exploration](#6-testing--exploration)
8. [Services & APIs](#7-services--apis)
9. [Comparison Matrix](#8-comparison-matrix)

---

## Key Implementation Differences

### Data Generation Scripts

**`generate.py`** (Tree-sitter + PyDriller):
- Parsing: Tree-sitter AST for accurate identifier extraction
- Extracts: functions, structs, enums, traits, impl blocks, mods
- Tracks: visibility (pub/private), modifiers (async, unsafe, const)
- Min lines filter: 10 (default)
- Output: SFT/JSON/Patch formats
- Pros: Accurate, detailed identifiers

**`gen_ctx.py`** (Git show with context):
- Uses: `git show -U<N>` directly via subprocess
- Context: Configurable (default: 50 lines before/after)
- Parsing: None - just extracts file-level changes
- Min lines filter: 50 (default)
- Output: JSONL + full context patch
- Pros: More surrounding code, simpler, no dependencies

**`gen_full.py`** (Best of Both):
- Uses: Tree-sitter for parsing + git show for context
- Gets default diff for parsing, full context diff for patches
- Detailed identifiers: Functions/structs with visibility
- Full context: 50 lines before/after
- Dual patch generation
- Pros: Comprehensive - both identifiers AND context

### Data Collection Scripts

**`gather_pr_issues.py`** (GitHub API Scraper):
- Fetches: PRs with full patches + Issues
- Extracts: Commit SHAs, linked issues, file changes
- Features:
  - Multi-token support (5000 req/hour per token)
  - Auto token rotation on rate limit
  - PR ↔ Issue linking via regex
  - Full patch diffs
- Output: prs.jsonl, issues.jsonl, summary.json

### Data Merging & Transformation

**`merge_datasets.py`** (SHA-based matching):
- Matching: By commit SHA (full and short)
- Uses: `enhanced_transformer.py` for patterns
- Extracts: Architectural hierarchy, change types, intent
- Combines: PR problem statement + arch patterns + identifiers
- Limitation: SHA matching fails with squash/rebase

**`smart_merge.py`** (PR number matching):
- Matching: By PR number from commit message `(#1234)`
- Uses regex: `\(#(\d+)\)` to extract PR number
- Preserves: Full PR title + body in prompt
- Same pattern extraction as merge_datasets.py
- Advantage: More reliable than SHA (survives squash/rebase)

**`enhanced_transformer.py`** (Pattern Extractor):
- Extracts 3 key dimensions:
  1. **File Hierarchy**: Groups files by layer (API/DB/domain/core/connectors)
  2. **Change Types**: Counts structs/functions/fields/queries added
  3. **Product Intent**: Detects feature type (search/payment/auth) + action (add/fix/enhance)
- Transforms: Technical commits → product-focused queries
- Creates: Digestible architectural explanations
- No LLM required - rule-based extraction

**`granular_generator.py`** (LLM-powered):
- Two modes:
  1. **Breakdown**: Splits large commits (5+ files) into smaller ones
  2. **Transform**: Converts to product-focused format
- Uses: vLLM API for LLM generation
- Model: GLM-4.6-FP8 (default)
- JSON parsing from LLM responses
- Temperature: 0.3 (breakdown), 0.5 (transform)

**`transform_to_natural.py`** (Natural Language):
- Converts: Mechanical file lists → explanatory prose
- LLM-powered with specific system prompt
- Explains WHAT and WHY, not just HOW
- Groups by architectural layer
- Temperature: 0.3 for consistency

### Which to Use?

**For Maximum Identifier Detail + Context**:
→ `gen_full.py` (tree-sitter parsing + 50-line context)

**For Simple Context Only**:
→ `gen_ctx.py` (fast, no dependencies, large context)

**For Product-Level Training Data**:
→ `gather_pr_issues.py` → `smart_merge.py` → `transform_to_natural.py`

**For Quick Identifier Extraction**:
→ `generate.py` (standard choice)

**For LLM-Enhanced Datasets**:
→ `granular_generator.py` (requires vLLM server)

---

## 1. Data Generation Scripts

### `generate.py`
**Purpose**: Extract Rust identifier changes from git commits using tree-sitter AST parsing.

**How it works**:
- Uses PyDriller to traverse git commit history
- Tree-sitter AST parsing for accurate Rust identifier extraction
- Extracts: functions, structs, enums, traits, impl blocks, modules
- Tracks visibility (pub/private) and modifiers (async, unsafe, const)
- Filters commits by minimum lines changed (default: 10 lines)

**Output formats**:
1. **SFT** (default): Prompt-response pairs for supervised fine-tuning
2. **JSON**: Detailed commit metadata with identifiers
3. **Patch**: Traditional git patch format

**Output structure** (SFT):
```json
{
  "prompt": "feat(connector): Add PlaceToPay cards",
  "response": "Files to modify:\n\n**placetopay.rs**\n  Add:\n    - function: pub::validate_capture_method\n    - struct: pub::PlacetopayPayment"
}
```

**Usage**:
```bash
python generate.py https://github.com/juspay/hyperswitch -f sft -m 20 -o commits_export
```

**Key difference**: Uses tree-sitter for accurate AST parsing vs regex patterns.

---

### `gen_ctx.py`
**Purpose**: Generate commits with custom context lines using `git show -U<N>`.

**How it works**:
- Uses git directly via subprocess
- Configurable context lines (default: 50 lines before/after changes)
- Provides more surrounding code for better understanding
- Filters by minimum lines changed and Rust files only

**Key features**:
- Larger code context window
- Simpler implementation (no tree-sitter dependency)
- Basic identifier extraction (file-level only)

**Output**:
- `.jsonl` files with prompt-response pairs
- `.patch` files with full 50-line context

**Usage**:
```bash
python gen_ctx.py /path/to/repo -U 50 -m 50 -o commits_ctx50
```

**Key difference**: Focuses on context window size rather than detailed identifier parsing.

---

### `gen_full.py`
**Purpose**: Combines BOTH detailed identifier extraction AND full context patches.

**How it works**:
- Uses tree-sitter for identifier parsing (from `generate.py`)
- Uses `git show -U50` for full context patches (from `gen_ctx.py`)
- Best of both worlds approach

**Key features**:
1. Detailed identifiers: Functions, structs, enums with visibility
2. Full context: 50 lines before/after each change
3. Dual patch generation (default for parsing, full for context)

**Output structure**:
```json
{
  "prompt": "feat: add validation",
  "response": "Files to modify:\n\n**auth.rs**\n  Add:\n    - function: pub::validate_token\n    - struct: private::TokenValidator"
}
```

Plus separate `.patch` file with full context.

**Usage**:
```bash
python gen_full.py /path/to/repo -U 50 -m 50 -o commits_full
```

**Key difference**: Comprehensive extraction with both identifiers AND context.

---

### `gen_with_context.py`
**Purpose**: Simple wrapper script demonstrating context line usage.

**What it does**:
- Minimal script showing how to use `git show -U<N>`
- Example/template for custom extractors

---

## 2. Data Collection Scripts

### `gather_pr_issues.py`
**Purpose**: Scrape GitHub PRs and Issues with full context using GitHub API.

**What it fetches**:
1. **Issues**: Problem statements, descriptions
2. **PRs**:
   - Full patches (git diff)
   - Commit SHAs
   - PR ↔ Issue links
   - Files changed with line counts
   - Labels, merge status

**Key features**:
- Multi-token support for rate limiting (5000 req/hour per token)
- Automatic token rotation when rate limited
- Extracts linked issues from PR descriptions
- Supports filtering by state, labels, max count

**Output**:
```
github_data/
├── prs.jsonl          # All PRs with patches and commits
├── issues.jsonl       # All issues
└── summary.json       # Statistics
```

**Output structure** (PR):
```json
{
  "number": 1234,
  "title": "Add search feature",
  "body": "Problem statement...",
  "patch": "diff --git a/...",
  "commits": [{"sha": "abc123", "message": "..."}],
  "files_changed": [{"filename": "src/core.rs", "additions": 50}],
  "linked_issues": [9642]
}
```

**Usage**:
```bash
export GITHUB_TOKEN="ghp_your_token"
python gather_pr_issues.py juspay hyperswitch --max-prs 500 -o github_data
```

**Key difference**: Provides product-level context (problem statements) vs raw commits.

---

## 3. Data Merging & Transformation

### `merge_datasets.py`
**Purpose**: Merge GitHub PRs/Issues with commit identifier data to create ultimate training dataset.

**How it works**:
1. Loads PR/Issue data from `gather_pr_issues.py`
2. Loads commit identifier data from `generate.py`
3. Indexes commits by SHA (full and short)
4. Matches PR commits with identifier data
5. Uses `enhanced_transformer.py` for architectural pattern extraction

**Key features**:
- Product-level problem statements (from PRs/Issues)
- Architectural layer extraction (API, DB, domain, core)
- Detailed identifier changes (functions, structs, enums)
- Change type analysis (structs added, queries modified, etc.)

**Output structure**:
```json
{
  "prompt": "Add search functionality to Customer API so merchants can find customers by ID...",
  "response": "To implement this search_filter feature:\n\n1. API Request/Response Models\n   - crates/api_models/src/customers.rs\n\n2. Database Layer\n   - crates/diesel_models/src/query/customers.rs\n\n**Detailed Identifier Changes:**\n\nCommit abc12345:\n**customers.rs**\n  Add:\n    - function: pub::list_by_merchant_id",
  "metadata": {
    "pr_number": 9642,
    "intent": {"feature_type": "search_filter", "action": "add_feature"},
    "hierarchy": {"api_models": [...], "database": [...]},
    "has_identifier_data": true
  }
}
```

**Usage**:
```bash
python merge_datasets.py github_data commits_export -o final_dataset
```

**Key difference**: Combines product intent + architecture + identifiers = ultimate training data.

---

### `smart_merge.py`
**Purpose**: Intelligently match PRs with commits using PR number extraction.

**Matching strategies**:
1. **PR number in commit message** (most reliable): Extract #1234 from "feat: xyz (#1234)"

**How it works**:
- Indexes all commits by PR number found in message
- Direct lookup when processing PRs
- More reliable than SHA matching (which fails with squash/rebase)

**Key features**:
- Uses PR number regex: `\(#(\d+)\)`
- Preserves full PR title + body in prompt
- Architectural pattern extraction via `enhanced_transformer.py`
- Detailed identifier merging

**Output**: Same format as `merge_datasets.py` but with better matching accuracy.

**Usage**:
```bash
python smart_merge.py github_data commits_export -o smart_merged
```

**Key difference**: More reliable PR-commit matching via PR numbers vs SHA matching.

---

### `enhanced_transformer.py`
**Purpose**: Transform technical patches into product abstraction → code pattern mappings.

**What it extracts**:

**1. File Hierarchy** (Architectural layers):
```python
{
  'api_models': ['customers.rs'],
  'database': ['query/customers.rs'],
  'domain': ['customer.rs'],
  'core_business': ['core/payments.rs'],
  'connectors': ['connector/stripe.rs'],
  'types': ['payment_types.rs']
}
```

**2. Change Types**:
```python
{
  'structs_added': 5,
  'functions_added': 12,
  'fields_added': 8,
  'database_queries': 7
}
```

**3. Product Intent**:
```python
{
  'feature_type': 'search_filter',  # or payment, auth, refund, etc.
  'action': 'add_feature',          # or fix_bug, enhance, refactor
  'entities': ['customer', 'payment']
}
```

**Key features**:
- Converts technical commits → product-focused queries
- Digestible architectural explanations
- Pattern-aware responses

**Example transformation**:
```
FROM: "feat(api): add customer search"
TO:   "How do I add search functionality to the Customer API?"

FROM: "**customers.rs**\n  Add:\n    - function: pub::search"
TO:   "To implement search, modify customers.rs by adding search() to handle queries..."
```

**Usage**: Typically imported and used by merge scripts.

**Key difference**: Adds product abstraction layer to technical code changes.

---

### `granular_generator.py`
**Purpose**: Break down large commits OR transform to product-focused format using vLLM.

**Two modes**:

**1. Breakdown mode**: Split large commits (5+ files) into smaller focused commits
```json
[
  {"prompt": "feat: add auth", "response": "Files to modify:\n**auth.rs**..."},
  {"prompt": "feat: add token", "response": "Files to modify:\n**token.rs**..."}
]
```

**2. Transform mode** (default): Convert technical commits to product queries
```json
{
  "prompt": "How do I add payment card support for PlaceToPay?",
  "response": "To implement card payments:\n\n1. Update placetopay.rs:\n   - Add validation\n   - Create request builders\n\n2. Update transformers.rs:\n   - Define payment structures"
}
```

**Key features**:
- Uses vLLM for LLM-powered transformation
- Configurable model (default: GLM-4.6-FP8)
- Automatic JSON parsing from LLM responses
- Progress tracking with statistics

**Usage**:
```bash
# Transform to product-focused
python granular_generator.py archit11/hyperswitch-rust-commits-final2 --mode transform

# Break down large commits
python granular_generator.py archit11/hyperswitch-rust-commits-final2 --mode breakdown -m 5
```

**Key difference**: LLM-powered transformation vs rule-based extraction.

---

### `transform_to_natural.py`
**Purpose**: Transform mechanical file/function lists into natural, developer-friendly explanations.

**Transformation example**:
```
FROM (Mechanical):
Files to modify:

**placetopay.rs**
  Add:
    - function: pub::validate_capture_method
    - function: pub::get_headers

TO (Natural):
To implement card payments for PlaceToPay:

**API Layer** (placetopay.rs):
- Add validate_capture_method() - validates payment capture methods before processing
- Add get_headers() - builds authentication headers for API requests
```

**Key features**:
- LLM-powered natural language generation
- Explanatory style (WHAT and WHY, not just HOW)
- Groups by architectural layer
- Preserves file paths for reference

**Usage**:
```bash
python transform_to_natural.py input.jsonl -o natural_dataset.jsonl --model zai-org/GLM-4.6-FP8
```

**Key difference**: Converts mechanical lists to explanatory prose.

---

## 4. Training Scripts

### `train_sft.py`
**Purpose**: Supervised Fine-Tuning (SFT) for Qwen models on Rust commit datasets.

**Configuration**:
- **Model**: Qwen/Qwen3-4B (default)
- **Dataset**: archit11/hyperswitch-rust-commits-final2 or local JSONL
- **Max sequence length**: Configurable (default: 4096)
- **Training**: LoRA + 4-bit quantization support
- **Format**: Chat format with system/user/assistant messages

**Prompt templates**:
1. **Basic**: Simple instruction
2. **Detailed**: Extended instruction with requirements
3. **Contextual**: Expert persona
4. **Structured**: Structured task format

**Key features**:
- Multiple prompt template choices
- 4-bit quantization (BitsAndBytes)
- LoRA fine-tuning for efficiency
- Flash Attention 2 support
- Wandb integration for tracking
- Auto train/test split (95/5)

**Training arguments**:
- BF16 precision
- Gradient checkpointing
- Cosine learning rate schedule
- Gradient accumulation

**Usage**:
```bash
python train_sft.py \
  --dataset archit11/hyperswitch-rust-commits-final2 \
  --model Qwen/Qwen3-4B \
  --output_dir ./qwen-rust-sft \
  --batch_size 2 \
  --gradient_accumulation 2 \
  --learning_rate 5e-6 \
  --num_epochs 2 \
  --use_4bit \
  --use_lora \
  --wandb_project rust-hyperswitch-sft
```

**Key difference**: Full training pipeline with efficient LoRA + 4-bit quantization.

---

## 5. Upload Utilities

### `upload_to_hf.py`
**Purpose**: Upload Rust commit datasets to Hugging Face Hub.

**What it does**:
1. Loads JSONL files from directory or single file
2. Creates train/test split (95/5)
3. Uploads to HuggingFace Hub
4. Auto-generates dataset card (README.md)

**Key features**:
- Preserves all fields including metadata
- Response length statistics
- Auto dataset card with usage examples
- Public or private upload

**Dataset card includes**:
- Dataset description
- Data fields
- Usage examples
- Training commands
- Citation info

**Output**:
- HuggingFace dataset at `username/dataset-name`
- Accessible via `load_dataset("username/dataset-name")`

**Usage**:
```bash
python upload_to_hf.py \
  --dataset_dir commits_export \
  --repo_id archit11/hyperswitch-rust-commits \
  --token $HF_TOKEN
```

**Key difference**: Complete dataset packaging + auto documentation.

---

## 6. Testing & Exploration

### `test_transform.py`
**Purpose**: Test LLM transformation on a single example.

**What it does**:
- Loads sample commit data
- Calls `granular_generator.py` in transform mode
- Shows before/after comparison
- Useful for debugging transformation prompts

**Usage**: `python test_transform.py`

---

### `test_vllm.py`
**Purpose**: Test vLLM server connection.

**What it does**:
- Sends test request to vLLM server
- Validates response format
- Checks model availability
- Timeout handling (120s)

**Usage**: `python test_vllm.py`

---

### `check_endpoints.py`
**Purpose**: Check available vLLM API endpoints.

**What it does**:
- Tests multiple endpoint paths
- Tries both GET and POST
- Checks `/v1/models` for model list
- Helps debug vLLM server setup

**Endpoints tested**:
- `/v1/chat/completions`
- `/chat/completions`
- `/v1/completions`
- `/generate`
- `/v1/models`

**Usage**: `python check_endpoints.py`

---

### `explore_juspay_dataset.py`
**Purpose**: Explore the juspay/hyperswitch dataset structure.

**What it does**:
- Loads juspay/hyperswitch dataset
- Shows available keys and types
- Displays first sample structure
- Saves sample to `juspay_sample.json`

**Usage**: `python explore_juspay_dataset.py`

---

### `find_rust_samples.py`
**Purpose**: Find samples with significant Rust code changes in juspay dataset.

**What it does**:
- Filters for samples with `.rs` file changes
- Counts Rust files per sample
- Shows top samples by file count
- Saves good examples to `rust_example_full.json`

**Usage**: `python find_rust_samples.py`

---

### `alo.py`
**Purpose**: Sample data cleaning utility.

**What it does**:
- Loads archit11/hyperswitch-rust-commits-final2
- Cleans unwanted text patterns (e.g., "\n\n authored by")
- Shows sample data structure

**Usage**: `python alo.py`

---

## 7. Services & APIs

### `gen_dw.py`
**Purpose**: DeepWiki MCP agent - FastAPI server for querying DeepWiki and LLM generation.

**Endpoints**:

**1. POST /query** - Query DeepWiki via SSE
```json
{
  "repo": "juspay/hyperswitch",
  "prompt": "How does payment processing work?",
  "timeout_s": 30
}
```
Response: Aggregated content from DeepWiki SSE stream

**2. POST /generate** - Generate using GLM-4.6-FP8
```json
{
  "repo": "juspay/hyperswitch",
  "prompt": "Explain the connector pattern"
}
```
Response: Generated answer from LLM

**Key features**:
- SSE stream aggregation with JSON parsing
- OpenAI-compatible API client
- Configurable timeout
- Error handling and retry logic

**Configuration** (env vars):
- `DEEPWIKI_MCP_SSE_URL`: DeepWiki SSE endpoint
- `OPENAI_BASE_URL`: vLLM server URL
- `OPENAI_MODEL`: Model name

**Usage**:
```bash
uvicorn gen_dw:app --host 0.0.0.0 --port 8080
```

**Key difference**: Full API service vs one-off scripts.

---

## 8. Comparison Matrix

### Data Generation Scripts

| Script | Parsing Method | Context | Identifiers | Output | Min Lines |
|--------|---------------|---------|-------------|--------|-----------|
| `generate.py` | Tree-sitter AST | Default git | ✅ Detailed (visibility, modifiers) | SFT/JSON/Patch | 10 |
| `gen_ctx.py` | None | Custom (-U50) | ❌ File-level only | JSONL + Patch | 50 |
| `gen_full.py` | Tree-sitter AST | Custom (-U50) | ✅ Detailed | JSONL + Patch | 50 |
| `gen_with_context.py` | None | Custom | ❌ | N/A | N/A |

### Data Merging Scripts

| Script | Matching Method | PR Context | Identifiers | Architectural Patterns |
|--------|----------------|------------|-------------|----------------------|
| `merge_datasets.py` | SHA matching | ✅ PR body | ✅ From commits | ✅ via enhanced_transformer |
| `smart_merge.py` | PR number regex | ✅ Full PR title+body | ✅ From commits | ✅ via enhanced_transformer |
| `enhanced_transformer.py` | N/A | N/A | ❌ | ✅ Core transformation logic |

### Transformation Scripts

| Script | Purpose | LLM Required | Input | Output |
|--------|---------|-------------|-------|--------|
| `granular_generator.py` | Breakdown OR Transform | ✅ vLLM | Dataset | Product-focused or split commits |
| `transform_to_natural.py` | Natural language | ✅ vLLM | JSONL | Explanatory responses |
| `enhanced_transformer.py` | Architectural extraction | ❌ | Patches | Hierarchical patterns |

---

## Key Differentiators

### Evolution of Data Generation:
1. **Basic extraction** (`gen_ctx.py`): Simple git show with context
2. **Detailed identifiers** (`generate.py`): Tree-sitter AST parsing
3. **Comprehensive** (`gen_full.py`): Both identifiers AND context

### Evolution of Merging:
1. **Basic merge** (`merge_datasets.py`): SHA-based matching
2. **Smart merge** (`smart_merge.py`): PR number regex matching (more reliable)
3. **Enhanced transformation** (`enhanced_transformer.py`): Product abstraction layer

### Evolution of Output Quality:
1. **Mechanical** (default): File lists with identifiers
2. **Product-focused** (`granular_generator.py` transform mode): Business queries
3. **Natural explanations** (`transform_to_natural.py`): Developer-friendly prose

---

## Recommended Usage

### For Training Code Generation Models:
**Option 1**: Product-focused SFT
```bash
# 1. Scrape GitHub
python gather_pr_issues.py juspay hyperswitch --max-prs 500 -o github_data

# 2. Extract commits
python generate.py /tmp/hyperswitch -f sft -m 20 -o commits_export

# 3. Smart merge
python smart_merge.py github_data commits_export -o merged_data

# 4. Train
python train_sft.py --dataset merged_data/merged_dataset.jsonl --model Qwen/Qwen3-4B
```

**Option 2**: Transform existing dataset
```bash
# Transform to product-focused
python granular_generator.py archit11/hyperswitch-rust-commits-final2 --mode transform -o transformed

# Train on transformed
python train_sft.py --dataset transformed/transformed_dataset.jsonl --model Qwen/Qwen3-4B
```

### For Dataset Creation:
**Comprehensive dataset**:
```bash
# Generate with full context + identifiers
python gen_full.py /tmp/hyperswitch -U 50 -m 50 -o hyperswitch_full

# Upload to HF
python upload_to_hf.py --dataset_dir hyperswitch_full --repo_id username/dataset-name
```

---

## Complete Workflow Example

### Step 1: Scrape GitHub Data
```bash
export GITHUB_TOKEN="your_token"
python gather_pr_issues.py juspay hyperswitch --max-prs 500 -o github_data
```

### Step 2: Extract Commits with Full Context
```bash
git clone https://github.com/juspay/hyperswitch /tmp/hyperswitch
python gen_full.py /tmp/hyperswitch -U 50 -m 20 -o commits_full
```

### Step 3: Smart Merge
```bash
python smart_merge.py github_data commits_full -o final_dataset
```

### Step 4: Optional - Transform to Natural Language
```bash
python transform_to_natural.py final_dataset/merged_dataset.jsonl -o natural_dataset.jsonl
```

### Step 5: Upload to HuggingFace
```bash
python upload_to_hf.py --dataset_dir . --repo_id username/hyperswitch-commits --token $HF_TOKEN
```

### Step 6: Train
```bash
python train_sft.py \
  --dataset username/hyperswitch-commits \
  --model Qwen/Qwen3-4B \
  --output_dir ./qwen-rust-ft \
  --use_4bit \
  --use_lora \
  --num_epochs 2
```

---

## Summary

This project provides a **comprehensive pipeline** for creating high-quality code generation training datasets by:

1. **Combining multiple data sources**: Git commits + GitHub PRs/Issues
2. **Multiple granularities**: File-level → Identifier-level → Product-level
3. **Flexible transformations**: Mechanical → Architectural → Natural language
4. **Production-ready training**: SFT with LoRA + 4-bit quantization

The key innovation is **Product Abstraction → Code Pattern** mapping that teaches models:
- "When implementing X product feature, you modify Y architectural layers"
- "Search features typically need API + DB + domain layers"
- Exact functions/structs to modify with explanations

Choose the appropriate scripts based on your needs:
- **Simple identifier extraction**: `generate.py`
- **Maximum context**: `gen_full.py`
- **Product-level understanding**: `smart_merge.py` + `enhanced_transformer.py`
- **Natural explanations**: `transform_to_natural.py`
- **Training**: `train_sft.py`
