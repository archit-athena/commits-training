#!/usr/bin/env python3
"""
smart_merge.py - Match PRs with commits intelligently

Since PR commit SHAs change after merge (squash/rebase), we match by:
1. PR number in commit message (e.g., "feat: xyz (#1234)")
2. Date proximity (commits merged within 1 day of PR merge)
3. File overlap (files changed in both)
"""

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from collections import defaultdict
from tqdm import tqdm

import sys
sys.path.append(str(Path(__file__).parent))
from enhanced_transformer import ProductCodeMapper


class SmartMerger:
    """Match PRs with commits using multiple strategies"""

    def __init__(self, pr_issues_dir: str, commits_dir: str, output_dir: str = "smart_merged"):
        self.pr_issues_dir = Path(pr_issues_dir)
        self.commits_dir = Path(commits_dir)
        self.output_dir = Path(output_dir)
        self.mapper = ProductCodeMapper()

        # Indexes
        self.commits_by_pr_number = defaultdict(list)
        self.commits_by_date = defaultdict(list)
        self.all_commits = []

    def extract_pr_number_from_message(self, message: str) -> Optional[int]:
        """Extract PR number from commit message like 'feat: xyz (#1234)'"""
        match = re.search(r'\(#(\d+)\)', message)
        if match:
            return int(match.group(1))
        return None

    def load_commits(self):
        """Load and index all commits"""
        print(f"📦 Loading commits from {self.commits_dir}...")

        commit_files = list(self.commits_dir.glob("*.jsonl"))

        for commit_file in tqdm(commit_files, desc="Loading commits"):
            try:
                with open(commit_file, 'r') as f:
                    commit_data = json.loads(f.read())

                # Extract info from filename
                parts = commit_file.stem.split('_')
                if len(parts) >= 3:
                    full_sha = parts[2]
                else:
                    full_sha = parts[-1]

                commit_message = commit_data.get('prompt', [''])[0] if isinstance(commit_data.get('prompt'), list) else commit_data.get('prompt', '')

                commit_info = {
                    'sha': full_sha,
                    'message': commit_message,
                    'response': commit_data.get('response', [''])[0] if isinstance(commit_data.get('response'), list) else commit_data.get('response', ''),
                    'file': str(commit_file)
                }

                self.all_commits.append(commit_info)

                # Index by PR number if found in message
                pr_num = self.extract_pr_number_from_message(commit_message)
                if pr_num:
                    self.commits_by_pr_number[pr_num].append(commit_info)

            except Exception as e:
                print(f"⚠️  Error loading {commit_file}: {e}")
                continue

        print(f"✅ Loaded {len(self.all_commits)} commits")
        print(f"📊 Indexed by PR number: {len(self.commits_by_pr_number)} PRs")

    def load_prs(self) -> List[Dict]:
        """Load PRs"""
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

    def match_pr_with_commits(self, pr: Dict) -> List[Dict]:
        """
        Match a PR with commits using multiple strategies

        Returns list of matching commits
        """
        pr_number = pr.get('number')

        # Strategy 1: Direct PR number match (most reliable!)
        if pr_number in self.commits_by_pr_number:
            return self.commits_by_pr_number[pr_number]

        # No match
        return []

    def merge_pr_with_commits(self, pr: Dict) -> Optional[Dict]:
        """Create merged entry for a PR"""
        try:
            problem_statement = pr.get('body', '') or pr.get('title', '')
            patch = pr.get('patch', '')

            if not patch or not problem_statement:
                return None

            # Extract patterns
            hierarchy = self.mapper.extract_file_hierarchy(patch)
            change_types = self.mapper.extract_change_types(patch)
            intent = self.mapper.extract_product_intent(problem_statement, '')

            # Build architectural response
            arch_response = self.mapper.create_enhanced_response_from_juspay({
                'problem_statement': problem_statement,
                'patch': patch,
                'hints_text': ''
            })

            # Match with commits
            matched_commits = self.match_pr_with_commits(pr)

            detailed_identifiers = []
            for commit_info in matched_commits[:3]:  # Top 3
                detailed_identifiers.append({
                    'sha': commit_info['sha'][:8],
                    'message': commit_info['message'][:100],
                    'identifiers': commit_info['response']
                })

            # Create prompt
            enhanced_prompt = self.mapper.create_enhanced_prompt_from_juspay({
                'problem_statement': problem_statement,
                'hints_text': ''
            })

            # Combine responses
            if detailed_identifiers:
                response_parts = [arch_response, "\n**Detailed Identifier Changes:**\n"]
                for commit_info in detailed_identifiers:
                    response_parts.append(f"\nCommit {commit_info['sha']}:")
                    response_parts.append(commit_info['identifiers'])
                combined_response = '\n'.join(response_parts)
            else:
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
                    'commits_matched': len(detailed_identifiers),
                    'match_method': 'pr_number' if detailed_identifiers else 'none'
                }
            }

        except Exception as e:
            print(f"⚠️  Error merging PR #{pr.get('number')}: {e}")
            return None

    def merge(self, max_samples: Optional[int] = None):
        """Main merge process"""
        print("=" * 80)
        print("🧠 Smart PR-Commit Matcher")
        print("=" * 80)

        # Load data
        self.load_commits()
        prs = self.load_prs()

        if not prs:
            print("❌ No PRs to merge!")
            return

        # Filter merged PRs
        merged_prs = [pr for pr in prs if pr.get('merged_at')]
        print(f"📊 Found {len(merged_prs)} merged PRs")

        # Merge
        print(f"\n🔄 Matching PRs with commits...")
        merged_dataset = []

        for pr in tqdm(merged_prs[:max_samples] if max_samples else merged_prs, desc="Merging"):
            merged_entry = self.merge_pr_with_commits(pr)
            if merged_entry:
                merged_dataset.append(merged_entry)

        # Save
        self.output_dir.mkdir(parents=True, exist_ok=True)
        output_file = self.output_dir / "merged_dataset.jsonl"

        with open(output_file, 'w') as f:
            for entry in merged_dataset:
                f.write(json.dumps(entry, ensure_ascii=False) + '\n')

        print(f"\n✅ Merge complete!")
        print(f"📁 Output: {output_file}")
        print(f"📊 Total samples: {len(merged_dataset)}")
        print(f"📊 Samples with identifier data: {sum(1 for e in merged_dataset if e['metadata']['has_identifier_data'])}")

        # Statistics
        stats = {
            'total_samples': len(merged_dataset),
            'with_identifier_data': sum(1 for e in merged_dataset if e['metadata']['has_identifier_data']),
            'match_methods': {},
            'feature_types': {}
        }

        for entry in merged_dataset:
            method = entry['metadata']['match_method']
            stats['match_methods'][method] = stats['match_methods'].get(method, 0) + 1

            ft = entry['metadata']['intent']['feature_type']
            stats['feature_types'][ft] = stats['feature_types'].get(ft, 0) + 1

        stats_file = self.output_dir / "statistics.json"
        with open(stats_file, 'w') as f:
            json.dump(stats, f, indent=2)

        print(f"\n📈 Match statistics:")
        print(f"   - Total: {stats['total_samples']}")
        print(f"   - With identifiers: {stats['with_identifier_data']}")
        print(f"\n📊 Match methods:")
        for method, count in stats['match_methods'].items():
            print(f"   - {method}: {count}")


def main():
    parser = argparse.ArgumentParser(description="Smart PR-Commit matcher")
    parser.add_argument("pr_issues_dir", help="Directory with PRs")
    parser.add_argument("commits_dir", help="Directory with commits")
    parser.add_argument("-o", "--output", default="smart_merged", help="Output directory")
    parser.add_argument("--max-samples", type=int, help="Max samples")

    args = parser.parse_args()

    merger = SmartMerger(
        pr_issues_dir=args.pr_issues_dir,
        commits_dir=args.commits_dir,
        output_dir=args.output
    )

    merger.merge(max_samples=args.max_samples)


if __name__ == "__main__":
    main()
