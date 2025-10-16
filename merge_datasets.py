#!/usr/bin/env python3
"""
merge_datasets.py - Merge GitHub PRs/Issues with commit identifier data

Combines:
1. PRs/Issues from gather_pr_issues.py (problem statements + patches)
2. Commit identifiers from generate.py (detailed function/struct changes)
3. Enhanced transformation from enhanced_transformer.py (architectural patterns)

Creates the ultimate training dataset:
- Product-level problem statement
- Architectural layers affected
- Detailed identifier-level changes (functions, structs, enums)
"""

import argparse
import json
from pathlib import Path
from typing import Dict, List, Optional
from collections import defaultdict
from tqdm import tqdm
import sys

# Import our enhanced transformer
sys.path.append(str(Path(__file__).parent))
from enhanced_transformer import ProductCodeMapper


class DatasetMerger:
    """Merge PR/Issue data with commit identifier data"""

    def __init__(self, pr_issues_dir: str, commits_dir: str, output_dir: str = "merged_dataset"):
        self.pr_issues_dir = Path(pr_issues_dir)
        self.commits_dir = Path(commits_dir)
        self.output_dir = Path(output_dir)
        self.mapper = ProductCodeMapper()

        # Index: commit_sha -> commit_data
        self.commit_index = {}

    def load_commit_data(self):
        """Load all commit data from generate.py output (JSONL files)"""
        print(f"📦 Loading commit data from {self.commits_dir}...")

        commit_files = list(self.commits_dir.glob("*.jsonl"))
        print(f"Found {len(commit_files)} commit files")

        for commit_file in tqdm(commit_files, desc="Loading commits"):
            try:
                with open(commit_file, 'r') as f:
                    commit_data = json.loads(f.read())

                    # Extract commit SHA from filename
                    # Format: {index}_{short_hash}_{full_hash}.jsonl
                    # Example: 00042_2d580b3a_2d580b3afbca861028e010853dc33c75818c9288.jsonl
                    parts = commit_file.stem.split('_')

                    if len(parts) >= 3:
                        full_sha = parts[2]  # Get the full SHA (last part)
                        short_sha = parts[1]  # Get short SHA too

                        # Index by both full and short SHA for flexibility
                        commit_info = {
                            'prompt': commit_data.get('prompt', ''),
                            'response': commit_data.get('response', ''),
                            'file': str(commit_file),
                            'full_sha': full_sha,
                            'short_sha': short_sha
                        }

                        self.commit_index[full_sha] = commit_info
                        self.commit_index[short_sha] = commit_info  # Also index by short SHA
                    else:
                        # Fallback: try to extract from filename
                        sha = parts[-1] if parts else commit_file.stem
                        self.commit_index[sha] = {
                            'prompt': commit_data.get('prompt', ''),
                            'response': commit_data.get('response', ''),
                            'file': str(commit_file)
                        }

            except Exception as e:
                print(f"⚠️  Error loading {commit_file}: {e}")
                continue

        print(f"✅ Loaded {len(self.commit_index)} commits into index")

    def load_prs(self) -> List[Dict]:
        """Load PR data"""
        prs_file = self.pr_issues_dir / "prs.jsonl"

        if not prs_file.exists():
            print(f"❌ PRs file not found: {prs_file}")
            return []

        print(f"📦 Loading PRs from {prs_file}...")

        prs = []
        with open(prs_file, 'r') as f:
            for line in f:
                try:
                    prs.append(json.loads(line))
                except:
                    continue

        print(f"✅ Loaded {len(prs)} PRs")
        return prs

    def load_issues(self) -> List[Dict]:
        """Load issue data"""
        issues_file = self.pr_issues_dir / "issues.jsonl"

        if not issues_file.exists():
            print(f"⚠️  Issues file not found: {issues_file}")
            return []

        print(f"📦 Loading issues from {issues_file}...")

        issues = []
        with open(issues_file, 'r') as f:
            for line in f:
                try:
                    issues.append(json.loads(line))
                except:
                    continue

        print(f"✅ Loaded {len(issues)} issues")
        return issues

    def merge_pr_with_commits(self, pr: Dict) -> Optional[Dict]:
        """
        Merge a PR with its commit identifier data

        Returns enriched dataset entry with:
        - Problem statement (from PR body or linked issue)
        - Architectural layers (extracted from patch)
        - Detailed identifiers (from commit data)
        """
        try:
            # Extract problem statement
            problem_statement = pr.get('body', '') or pr.get('title', '')

            # Get patch
            patch = pr.get('patch', '')

            if not patch or not problem_statement:
                return None

            # Extract architectural patterns using enhanced_transformer
            hierarchy = self.mapper.extract_file_hierarchy(patch)
            change_types = self.mapper.extract_change_types(patch)
            intent = self.mapper.extract_product_intent(problem_statement, '')

            # Build the architectural response
            arch_response = self.mapper.create_enhanced_response_from_juspay({
                'problem_statement': problem_statement,
                'patch': patch,
                'hints_text': ''
            })

            # Try to get detailed identifier changes from commits
            pr_commits = pr.get('commits', [])
            detailed_identifiers = []

            for commit in pr_commits:
                sha = commit.get('sha', '')

                # Try matching with full SHA first
                commit_data = None
                if sha in self.commit_index:
                    commit_data = self.commit_index[sha]
                # Try short SHA (first 7-8 chars)
                elif sha[:8] in self.commit_index:
                    commit_data = self.commit_index[sha[:8]]
                elif sha[:7] in self.commit_index:
                    commit_data = self.commit_index[sha[:7]]

                if commit_data:
                    detailed_identifiers.append({
                        'sha': sha[:8],
                        'message': commit.get('message', ''),
                        'identifiers': commit_data.get('response', '')
                    })

            # Create enhanced prompt
            enhanced_prompt = self.mapper.create_enhanced_prompt_from_juspay({
                'problem_statement': problem_statement,
                'hints_text': ''
            })

            # Combine architectural + identifier information
            if detailed_identifiers:
                # We have detailed identifier data!
                response_parts = [arch_response, "\n**Detailed Identifier Changes:**\n"]

                for commit_info in detailed_identifiers[:3]:  # Show top 3 commits
                    response_parts.append(f"\nCommit {commit_info['sha']}:")
                    response_parts.append(commit_info['identifiers'])

                combined_response = '\n'.join(response_parts)
            else:
                # Only architectural info
                combined_response = arch_response

            return {
                'prompt': enhanced_prompt,
                'response': combined_response,
                'metadata': {
                    'pr_number': pr.get('number'),
                    'pr_title': pr.get('title'),
                    'merged_at': pr.get('merged_at'),
                    'intent': intent,
                    'hierarchy': hierarchy,
                    'change_types': change_types,
                    'has_identifier_data': len(detailed_identifiers) > 0,
                    'commits_included': len(detailed_identifiers)
                }
            }

        except Exception as e:
            print(f"⚠️  Error merging PR #{pr.get('number')}: {e}")
            return None

    def merge(self, max_samples: Optional[int] = None):
        """Main merge process"""
        print("=" * 80)
        print("🔀 Merging PR/Issue Data with Commit Identifiers")
        print("=" * 80)

        # Load all data
        self.load_commit_data()
        prs = self.load_prs()

        if not prs:
            print("❌ No PRs to merge!")
            return

        # Filter merged PRs only
        merged_prs = [pr for pr in prs if pr.get('merged_at')]
        print(f"📊 Found {len(merged_prs)} merged PRs")

        # Merge each PR
        print(f"\n🔄 Merging PRs with commit data...")
        merged_dataset = []

        for pr in tqdm(merged_prs[:max_samples] if max_samples else merged_prs,
                      desc="Merging"):
            merged_entry = self.merge_pr_with_commits(pr)

            if merged_entry:
                merged_dataset.append(merged_entry)

        # Save merged dataset
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Save as JSONL
        output_file = self.output_dir / "merged_dataset.jsonl"
        with open(output_file, 'w') as f:
            for entry in merged_dataset:
                f.write(json.dumps(entry, ensure_ascii=False) + '\n')

        print(f"\n✅ Merge complete!")
        print(f"📁 Output: {output_file}")
        print(f"📊 Total samples: {len(merged_dataset)}")
        print(f"📊 Samples with identifier data: {sum(1 for e in merged_dataset if e['metadata']['has_identifier_data'])}")

        # Save statistics
        stats = {
            'total_samples': len(merged_dataset),
            'with_identifier_data': sum(1 for e in merged_dataset if e['metadata']['has_identifier_data']),
            'feature_types': {},
            'avg_commits_per_pr': sum(e['metadata']['commits_included'] for e in merged_dataset) / len(merged_dataset) if merged_dataset else 0
        }

        # Count feature types
        for entry in merged_dataset:
            ft = entry['metadata']['intent']['feature_type']
            stats['feature_types'][ft] = stats['feature_types'].get(ft, 0) + 1

        stats_file = self.output_dir / "statistics.json"
        with open(stats_file, 'w') as f:
            json.dump(stats, f, indent=2)

        print(f"\n📈 Statistics:")
        print(f"   - Total samples: {stats['total_samples']}")
        print(f"   - With identifier data: {stats['with_identifier_data']}")
        print(f"   - Avg commits per PR: {stats['avg_commits_per_pr']:.1f}")
        print(f"\n📊 Feature types:")
        for ft, count in sorted(stats['feature_types'].items(), key=lambda x: -x[1])[:5]:
            print(f"   - {ft}: {count}")


def main():
    parser = argparse.ArgumentParser(
        description="Merge PR/Issue data with commit identifier data",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Merge github_data with commits_export
  %(prog)s github_data commits_export

  # Limit to 100 samples
  %(prog)s github_data commits_export --max-samples 100
        """
    )

    parser.add_argument("pr_issues_dir",
                       help="Directory with PRs/issues (output from gather_pr_issues.py)")
    parser.add_argument("commits_dir",
                       help="Directory with commit data (output from generate.py)")
    parser.add_argument("-o", "--output", default="merged_dataset",
                       help="Output directory (default: merged_dataset)")
    parser.add_argument("--max-samples", type=int,
                       help="Maximum samples to process")

    args = parser.parse_args()

    merger = DatasetMerger(
        pr_issues_dir=args.pr_issues_dir,
        commits_dir=args.commits_dir,
        output_dir=args.output
    )

    merger.merge(max_samples=args.max_samples)


if __name__ == "__main__":
    main()
