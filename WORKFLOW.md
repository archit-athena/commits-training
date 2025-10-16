# Complete Dataset Generation Workflow

This workflow creates a **Product Abstraction → Code Pattern** training dataset that teaches models:
1. **Product-level understanding** (from issues/PRs)
2. **Architectural patterns** (which layers to modify)
3. **Detailed identifier changes** (specific functions, structs, enums)

## 📊 Data Sources

1. **GitHub PRs/Issues** - Product context, problem statements, full patches
2. **Commit History** - Detailed identifier-level changes (functions, structs, enums)
3. **Enhanced Transformation** - Architectural pattern extraction

## 🔧 Tools

### 1. `gather_pr_issues.py` - Scrape GitHub PRs & Issues

Fetches:
- Problem statements from issues
- Full PR patches
- Commit SHAs from PRs
- PR ↔ Issue links

**Usage:**
```bash
# Set your GitHub token
export GITHUB_TOKEN="ghp_your_token_here"

# Scrape hyperswitch repo
python3 gather_pr_issues.py juspay hyperswitch -o github_data

# Or with recent 200 PRs only
python3 gather_pr_issues.py juspay hyperswitch --max-prs 200
```

**Output:**
```
github_data/
├── prs.jsonl          # All PRs with patches and commit SHAs
├── issues.jsonl       # All issues
└── summary.json       # Statistics
```

### 2. `generate.py` - Extract Detailed Commit Identifiers

Extracts from git history:
- Functions added/removed (with pub/private visibility)
- Structs added/removed
- Enums, traits, impls
- Tree-sitter parsing for accurate identifier extraction

**Usage:**
```bash
# Extract from local repo
python3 generate.py /path/to/hyperswitch -f sft -o commits_export

# Or from remote
python3 generate.py https://github.com/juspay/hyperswitch -f sft -o commits_export
```

**Output:**
```
commits_export/
├── 00001_abc12345_full_sha.jsonl
├── 00002_def67890_full_sha.jsonl
...
└── index.csv
```

Each JSONL contains:
```json
{
  "prompt": "feat(connector): Add PlaceToPay cards",
  "response": "Files to modify:\n\n**placetopay.rs**\n  Add:\n    - function: pub::validate_capture_method\n    - struct: pub::PlacetopayPayment"
}
```

### 3. `merge_datasets.py` - Combine Everything

Merges PR/Issue data with commit identifiers using `enhanced_transformer.py` to create ultimate training data.

**Usage:**
```bash
python3 merge_datasets.py github_data commits_export -o final_dataset
```

**Output:**
```
final_dataset/
├── merged_dataset.jsonl    # Combined training data
└── statistics.json         # Dataset statistics
```

Each entry in `merged_dataset.jsonl`:
```json
{
  "prompt": "Add search functionality to Customer API so merchants can find customers by ID...",
  "response": "To implement this search_filter feature:\n\n1. API Request/Response Models\n   - crates/api_models/src/customers.rs\n\n2. Database Layer\n   - crates/diesel_models/src/query/customers.rs\n...\n\nDetailed Identifier Changes:\n\nCommit abc12345:\n**customers.rs**\n  Add:\n    - function: pub::list_by_merchant_id\n    - struct: pub::CustomerListConstraints",
  "metadata": {
    "pr_number": 9642,
    "intent": {
      "feature_type": "search_filter",
      "action": "add_feature"
    },
    "hierarchy": {
      "api_models": [...],
      "database": [...]
    },
    "has_identifier_data": true
  }
}
```

## 🎯 What The Model Learns

### Before (Generic):
```
Q: "Add search to customer API"
A: "Modify customer files"
```

### After (Specific with Patterns):
```
Q: "Add search functionality to Customer API so merchants can find customers by ID"
A: "To implement this search_filter feature:

1. API Request/Response Models (api_models/src/customers.rs)
   - Add customer_id field to CustomerListRequest struct

2. Database Layer (diesel_models/src/query/customers.rs)
   - Modify list_by_merchant_id function
   - Add conditional filtering with .eq() predicate

3. Domain Models (hyperswitch_domain_models/src/customer.rs)
   - Add customer_id field to CustomerListConstraints

Code Patterns:
- Extend types with new fields (9 changes)
- Add conditional logic for filtering (2 changes)
- Modify database queries (7 changes)

Detailed Changes:
Commit abc12345:
**customers.rs**
  Add:
    - function: pub::list_by_merchant_id
```

## 🚀 Complete Workflow

### Step 1: Scrape GitHub Data
```bash
export GITHUB_TOKEN="your_token"
python3 gather_pr_issues.py juspay hyperswitch --max-prs 500 -o github_data
```

### Step 2: Extract Commit Identifiers
```bash
# Clone repo if needed
git clone https://github.com/juspay/hyperswitch /tmp/hyperswitch

# Extract commits
python3 generate.py /tmp/hyperswitch -f sft -o commits_export -m 20
```

### Step 3: Merge Everything
```bash
python3 merge_datasets.py github_data commits_export -o final_dataset
```

### Step 4: Use for Training
```bash
# The merged_dataset.jsonl is ready for SFT training!
# Use with any training framework (Axolotl, TRL, etc.)
```

## 📈 Expected Dataset Quality

**Input Sources:**
- **500 PRs** with problem statements and patches
- **2000+ commits** with detailed identifiers
- **~300-400 matched** (PRs with commit identifier data)

**Output:**
- **300-400 high-quality samples** with:
  - Product-level problem statement ✅
  - Architectural pattern guidance ✅
  - Detailed identifier changes ✅

## 🔑 Key Features

1. **Product Abstraction Knowledge**
   - Model learns to map "add search feature" → specific architectural layers

2. **Architectural Patterns**
   - Model learns: "search features typically need API layer + DB layer + domain layer"

3. **Detailed Identifiers**
   - Model learns exact functions/structs to modify

4. **Cross-Referenced**
   - PR problem statements linked to actual code changes

## 💡 Tips

1. **GitHub Token**: Get yours at https://github.com/settings/tokens
   - Need scopes: `repo` (for private repos) or none for public

2. **Rate Limits**:
   - Without token: 60 requests/hour
   - With token: 5000 requests/hour

3. **Disk Space**:
   - 500 PRs: ~50MB
   - 2000 commits: ~100MB
   - Final dataset: ~150MB

4. **Processing Time**:
   - Step 1 (scrape): ~10 minutes (500 PRs)
   - Step 2 (extract): ~30 minutes (2000 commits)
   - Step 3 (merge): ~5 minutes

## 🎓 Training Recommendations

- **Context Length**: 4096+ tokens (some samples are large)
- **Format**: Standard instruction format
- **Validation Split**: 10-15%
- **Epochs**: 2-3 (avoid overfitting on patterns)

## 🐛 Troubleshooting

**Q: "Rate limit exceeded"**
- A: Set GITHUB_TOKEN or wait 1 hour

**Q: "No identifier data for most PRs"**
- A: Ensure commit SHAs in PRs match those in commits_export
- A: Check that generate.py was run on the same repo

**Q: "Patches are too large"**
- A: Filter PRs by size in merge_datasets.py
- A: Use `--max-samples` to limit

## 📝 Notes

- This workflow is designed for **Rust** repositories specifically
- For other languages, modify tree-sitter parser in `generate.py`
- The enhanced_transformer.py can be extended with more architectural patterns
