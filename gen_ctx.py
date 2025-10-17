#!/usr/bin/env python3
"""
Generate commits with custom context lines using git show -U<N>
"""

import subprocess
import json
import argparse
from pathlib import Path
from tqdm import tqdm
import re


def get_commits_list(repo_path: str, branch: str = None) -> list:
    """Get all commit SHAs"""
    cmd = ['git', '-C', repo_path, 'log', '--all', '--format=%H']
    if branch:
        cmd = ['git', '-C', repo_path, 'log', branch, '--format=%H']

    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip().split('\n')


def get_commit_with_context(repo_path: str, sha: str, context_lines: int = 50):
    """Get commit info with custom context lines"""

    # Get message
    msg_result = subprocess.run(
        ['git', '-C', repo_path, 'log', '-1', '--format=%s%n%b', sha],
        capture_output=True, text=True
    )
    message = msg_result.stdout.strip()

    # Get diff with context
    diff_result = subprocess.run(
        ['git', '-C', repo_path, 'show', f'-U{context_lines}', '--format=', sha],
        capture_output=True, text=True
    )
    patch = diff_result.stdout

    # Count lines
    insertions = len([l for l in patch.split('\n') if l.startswith('+') and not l.startswith('+++')])
    deletions = len([l for l in patch.split('\n') if l.startswith('-') and not l.startswith('---')])
    total_lines = insertions + deletions

    # Extract files
    files = re.findall(r'diff --git a/(.+?) b/', patch)
    rust_files = [f for f in files if f.endswith('.rs')]

    return {
        'sha': sha,
        'short_sha': sha[:8],
        'message': message,
        'patch': patch,
        'files': files,
        'rust_files': rust_files,
        'lines_changed': total_lines,
        'context_lines': context_lines
    }


def save_commit_sft(commit_data: dict, output_dir: Path, index: int):
    """Save commit in SFT format"""

    # Build SFT format
    prompt = commit_data['message']

    response_parts = ["Files to modify:\n"]
    for rust_file in commit_data['rust_files']:
        response_parts.append(f"\n**{rust_file}**")
        response_parts.append("  Modify existing code")

    sft_entry = {
        'prompt': prompt,
        'response': '\n'.join(response_parts)
    }

    # Save JSONL
    filename = f"{index:05d}_{commit_data['short_sha']}_{commit_data['sha']}.jsonl"
    with open(output_dir / filename, 'w') as f:
        json.dump(sft_entry, f, ensure_ascii=False)
        f.write('\n')

    # Save patch with full context
    patch_filename = f"{index:05d}_{commit_data['short_sha']}_{commit_data['sha']}.patch"
    with open(output_dir / patch_filename, 'w') as f:
        f.write(commit_data['patch'])


def main():
    parser = argparse.ArgumentParser(
        description="Generate commits with custom diff context lines"
    )
    parser.add_argument("repo_path", help="Path to git repository")
    parser.add_argument("-U", "--context", type=int, default=50,
                       help="Context lines (default: 50)")
    parser.add_argument("-m", "--min-lines", type=int, default=50,
                       help="Min lines changed (default: 50)")
    parser.add_argument("-o", "--output", default="commits_ctx50",
                       help="Output directory")
    parser.add_argument("-b", "--branch", help="Specific branch")

    args = parser.parse_args()

    print("=" * 80)
    print("🦀 Git Commit Extractor with Custom Context")
    print("=" * 80)
    print(f"📍 Repository: {args.repo_path}")
    print(f"📏 Context lines: {args.context}")
    print(f"📏 Min lines: {args.min_lines}")
    print("=" * 80)

    # Create output dir
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Get commits
    print("\n🔍 Getting commit list...")
    commit_shas = get_commits_list(args.repo_path, args.branch)
    print(f"📊 Found {len(commit_shas)} commits")

    # Process
    print("\n⚡ Processing commits...")
    processed = 0
    skipped = 0

    for idx, sha in enumerate(tqdm(commit_shas, desc="Extracting"), 1):
        try:
            commit_data = get_commit_with_context(args.repo_path, sha, args.context)

            # Filter by min lines
            if commit_data['lines_changed'] < args.min_lines:
                skipped += 1
                continue

            # Filter by rust files
            if not commit_data['rust_files']:
                skipped += 1
                continue

            # Save
            save_commit_sft(commit_data, output_dir, processed + 1)
            processed += 1

        except Exception as e:
            print(f"\n❌ Error with {sha[:8]}: {e}")
            continue

    print(f"\n✅ Extraction complete!")
    print(f"📁 Output: {output_dir.absolute()}")
    print(f"📝 Processed: {processed} commits")
    print(f"⏭️  Skipped: {skipped} commits")
    print(f"💾 Total size: {sum(f.stat().st_size for f in output_dir.glob('*')) / 1024 / 1024:.2f} MB")


if __name__ == "__main__":
    main()
