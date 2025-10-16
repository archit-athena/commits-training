#!/usr/bin/env python3
"""
gather_pr_issues.py - Scrape PRs and Issues from GitHub with full context

This gathers:
1. Issues (problem statements)
2. PRs (code changes with full patches)
3. Links PRs to Issues
4. Extracts commits from PRs (to cross-reference with generate.py output)

Requires: GitHub PAT (Personal Access Token)
"""

import argparse
import json
import os
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional
import requests
from tqdm import tqdm
import time


class GitHubScraper:
    """Scrape PRs and Issues from GitHub API"""

    def __init__(self, repo_owner: str, repo_name: str,
                 github_token: Optional[str] = None,
                 output_dir: str = "github_data"):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.github_token = github_token or os.environ.get('GITHUB_TOKEN')
        self.output_dir = Path(output_dir)
        self.base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"

        if not self.github_token:
            print("⚠️  Warning: No GitHub token provided. Rate limits will be strict (60/hour)")
            print("   Set GITHUB_TOKEN env var or pass --token for 5000/hour")

        self.session = requests.Session()
        if self.github_token:
            self.session.headers.update({
                'Authorization': f'token {self.github_token}',
                'Accept': 'application/vnd.github.v3+json'
            })

    def check_rate_limit(self):
        """Check GitHub API rate limit"""
        try:
            response = self.session.get('https://api.github.com/rate_limit')
            data = response.json()
            core = data['resources']['core']
            print(f"📊 Rate Limit: {core['remaining']}/{core['limit']} remaining")
            if core['remaining'] < 100:
                print("⚠️  Warning: Low rate limit! Consider using a GitHub token")
            return core
        except Exception as e:
            print(f"❌ Error checking rate limit: {e}")
            return None

    def get_issues(self, state: str = "all", labels: Optional[List[str]] = None,
                   max_issues: Optional[int] = None) -> List[Dict]:
        """
        Get issues from repository

        Args:
            state: 'open', 'closed', or 'all'
            labels: Filter by labels (e.g., ['bug', 'enhancement'])
            max_issues: Maximum number of issues to fetch
        """
        print(f"\n📋 Fetching issues (state={state})...")

        issues = []
        page = 1
        per_page = 100

        params = {
            'state': state,
            'per_page': per_page,
            'page': page,
            'sort': 'created',
            'direction': 'desc'
        }

        if labels:
            params['labels'] = ','.join(labels)

        with tqdm(desc="Issues", unit="issue") as pbar:
            while True:
                try:
                    response = self.session.get(
                        f"{self.base_url}/issues",
                        params=params,
                        timeout=30
                    )

                    if response.status_code == 403:
                        print("\n⚠️  Rate limit exceeded. Waiting...")
                        time.sleep(60)
                        continue

                    response.raise_for_status()
                    page_issues = response.json()

                    if not page_issues:
                        break

                    # Filter out PRs (issues endpoint includes PRs)
                    page_issues = [i for i in page_issues if 'pull_request' not in i]

                    issues.extend(page_issues)
                    pbar.update(len(page_issues))

                    if max_issues and len(issues) >= max_issues:
                        issues = issues[:max_issues]
                        break

                    # Check if there's a next page
                    if 'Link' not in response.headers or 'rel="next"' not in response.headers['Link']:
                        break

                    params['page'] += 1
                    time.sleep(0.5)  # Be nice to API

                except Exception as e:
                    print(f"\n❌ Error fetching issues page {page}: {e}")
                    break

        print(f"✅ Fetched {len(issues)} issues")
        return issues

    def get_pull_requests(self, state: str = "all", max_prs: Optional[int] = None) -> List[Dict]:
        """
        Get pull requests from repository

        Args:
            state: 'open', 'closed', or 'all'
            max_prs: Maximum number of PRs to fetch
        """
        print(f"\n🔀 Fetching pull requests (state={state})...")

        prs = []
        page = 1
        per_page = 100

        params = {
            'state': state,
            'per_page': per_page,
            'page': page,
            'sort': 'created',
            'direction': 'desc'
        }

        with tqdm(desc="PRs", unit="pr") as pbar:
            while True:
                try:
                    response = self.session.get(
                        f"{self.base_url}/pulls",
                        params=params,
                        timeout=30
                    )

                    if response.status_code == 403:
                        print("\n⚠️  Rate limit exceeded. Waiting...")
                        time.sleep(60)
                        continue

                    response.raise_for_status()
                    page_prs = response.json()

                    if not page_prs:
                        break

                    prs.extend(page_prs)
                    pbar.update(len(page_prs))

                    if max_prs and len(prs) >= max_prs:
                        prs = prs[:max_prs]
                        break

                    if 'Link' not in response.headers or 'rel="next"' not in response.headers['Link']:
                        break

                    params['page'] += 1
                    time.sleep(0.5)

                except Exception as e:
                    print(f"\n❌ Error fetching PRs page {page}: {e}")
                    break

        print(f"✅ Fetched {len(prs)} pull requests")
        return prs

    def get_pr_details(self, pr_number: int) -> Optional[Dict]:
        """Get detailed PR information including patch, files, commits"""
        try:
            # Get PR data
            pr_response = self.session.get(
                f"{self.base_url}/pulls/{pr_number}",
                headers={'Accept': 'application/vnd.github.v3.diff'},
                timeout=30
            )

            if pr_response.status_code != 200:
                return None

            patch = pr_response.text

            # Get PR metadata
            pr_meta = self.session.get(
                f"{self.base_url}/pulls/{pr_number}",
                timeout=30
            ).json()

            # Get PR commits
            commits_response = self.session.get(
                f"{self.base_url}/pulls/{pr_number}/commits",
                timeout=30
            )
            commits = commits_response.json() if commits_response.status_code == 200 else []

            # Get files changed
            files_response = self.session.get(
                f"{self.base_url}/pulls/{pr_number}/files",
                timeout=30
            )
            files = files_response.json() if files_response.status_code == 200 else []

            return {
                'number': pr_number,
                'title': pr_meta.get('title'),
                'body': pr_meta.get('body'),
                'state': pr_meta.get('state'),
                'created_at': pr_meta.get('created_at'),
                'merged_at': pr_meta.get('merged_at'),
                'base_ref': pr_meta.get('base', {}).get('ref'),
                'head_ref': pr_meta.get('head', {}).get('ref'),
                'user': pr_meta.get('user', {}).get('login'),
                'labels': [l['name'] for l in pr_meta.get('labels', [])],
                'patch': patch,
                'commits': [{'sha': c['sha'], 'message': c['commit']['message']} for c in commits],
                'files_changed': [{'filename': f['filename'], 'status': f['status'],
                                  'additions': f['additions'], 'deletions': f['deletions']}
                                 for f in files],
                'linked_issues': self.extract_linked_issues(pr_meta.get('body', ''))
            }

        except Exception as e:
            print(f"❌ Error fetching PR #{pr_number} details: {e}")
            return None

    def extract_linked_issues(self, text: str) -> List[int]:
        """Extract issue numbers from text (e.g., 'fixes #123', 'closes #456')"""
        import re
        if not text:
            return []

        patterns = [
            r'(?:fix|fixes|fixed|close|closes|closed|resolve|resolves|resolved)\s+#(\d+)',
            r'#(\d+)'
        ]

        issue_numbers = []
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            issue_numbers.extend([int(m) for m in matches])

        return list(set(issue_numbers))

    def save_data(self, issues: List[Dict], prs: List[Dict]):
        """Save scraped data to files"""
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Save issues
        issues_file = self.output_dir / "issues.jsonl"
        with open(issues_file, 'w') as f:
            for issue in issues:
                f.write(json.dumps(issue, ensure_ascii=False) + '\n')
        print(f"💾 Saved {len(issues)} issues to {issues_file}")

        # Save PRs
        prs_file = self.output_dir / "prs.jsonl"
        with open(prs_file, 'w') as f:
            for pr in prs:
                f.write(json.dumps(pr, ensure_ascii=False) + '\n')
        print(f"💾 Saved {len(prs)} PRs to {prs_file}")

        # Create summary
        summary = {
            'repository': f"{self.repo_owner}/{self.repo_name}",
            'scraped_at': datetime.now().isoformat(),
            'total_issues': len(issues),
            'total_prs': len(prs),
            'prs_merged': sum(1 for pr in prs if pr.get('merged_at')),
        }

        summary_file = self.output_dir / "summary.json"
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2)
        print(f"📊 Saved summary to {summary_file}")

    def scrape(self, max_issues: Optional[int] = None,
               max_prs: Optional[int] = None,
               fetch_pr_details: bool = True,
               skip_issues: bool = False):
        """Main scraping workflow"""
        print("=" * 80)
        print(f"🕷️  Scraping GitHub Repository: {self.repo_owner}/{self.repo_name}")
        print("=" * 80)

        self.check_rate_limit()

        # Fetch issues
        if not skip_issues:
            issues = self.get_issues(state='all', max_issues=max_issues)
        else:
            print("\n⏭️  Skipping issues")
            issues = []

        # Fetch PRs
        prs = self.get_pull_requests(state='closed', max_prs=max_prs)  # Focus on merged PRs

        # Fetch detailed PR information
        if fetch_pr_details and prs:
            print(f"\n🔍 Fetching detailed PR information...")
            detailed_prs = []

            for pr in tqdm(prs, desc="PR Details"):
                pr_number = pr['number']
                details = self.get_pr_details(pr_number)

                if details:
                    detailed_prs.append(details)

                time.sleep(0.5)  # Rate limiting

            prs = detailed_prs

        # Save data
        print(f"\n💾 Saving data...")
        self.save_data(issues, prs)

        print(f"\n✅ Scraping complete!")
        print(f"📁 Output directory: {self.output_dir.absolute()}")
        self.check_rate_limit()


def main():
    parser = argparse.ArgumentParser(
        description="Scrape GitHub PRs and Issues with full context",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Scrape all PRs and issues from hyperswitch
  %(prog)s juspay hyperswitch --token YOUR_GITHUB_TOKEN

  # Scrape recent 100 PRs only
  %(prog)s juspay hyperswitch --max-prs 100

  # Set token via environment
  export GITHUB_TOKEN=your_token_here
  %(prog)s juspay hyperswitch
        """
    )

    parser.add_argument("owner", help="Repository owner (e.g., 'juspay')")
    parser.add_argument("repo", help="Repository name (e.g., 'hyperswitch')")
    parser.add_argument("-o", "--output", default="github_data",
                       help="Output directory (default: github_data)")
    parser.add_argument("--token", help="GitHub Personal Access Token (or set GITHUB_TOKEN env)")
    parser.add_argument("--max-issues", type=int, help="Maximum issues to fetch")
    parser.add_argument("--max-prs", type=int, help="Maximum PRs to fetch")
    parser.add_argument("--no-pr-details", action="store_true",
                       help="Skip fetching detailed PR information (faster)")
    parser.add_argument("--skip-issues", action="store_true",
                       help="Skip fetching issues (only fetch PRs)")

    args = parser.parse_args()

    scraper = GitHubScraper(
        repo_owner=args.owner,
        repo_name=args.repo,
        github_token=args.token,
        output_dir=args.output
    )

    scraper.scrape(
        max_issues=args.max_issues,
        max_prs=args.max_prs,
        fetch_pr_details=not args.no_pr_details,
        skip_issues=args.skip_issues
    )


if __name__ == "__main__":
    main()
