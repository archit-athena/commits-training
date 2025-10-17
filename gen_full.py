#!/usr/bin/env python3
"""
Generate commits with BOTH:
1. Detailed identifier extraction (from generate.py)
2. Full context patches with -U50 (from gen_ctx.py)
"""

import subprocess
import json
import argparse
from pathlib import Path
from tqdm import tqdm
import sys
import re

# Import the identifier parser from generate.py
sys.path.append(str(Path(__file__).parent))
from generate import RustIdentifierParser


def get_commits_list(repo_path: str, branch: str = None) -> list:
    """Get all commit SHAs"""
    cmd = ['git', '-C', repo_path, 'log', '--all', '--format=%H']
    if branch:
        cmd = ['git', '-C', repo_path, 'log', branch, '--format=%H']

    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip().split('\n')


def get_commit_with_full_context(repo_path: str, sha: str, context_lines: int = 50):
    """Get commit info with detailed identifiers AND full context patch"""

    # Get message
    msg_result = subprocess.run(
        ['git', '-C', repo_path, 'log', '-1', '--format=%s%n%b', sha],
        capture_output=True, text=True
    )
    message = msg_result.stdout.strip()

    # Get diff with FULL CONTEXT (50 lines)
    full_patch_result = subprocess.run(
        ['git', '-C', repo_path, 'show', f'-U{context_lines}', '--format=', sha],
        capture_output=True, text=True
    )
    full_patch = full_patch_result.stdout

    # Get diff with DEFAULT context for parsing (easier to parse)
    default_patch_result = subprocess.run(
        ['git', '-C', repo_path, 'show', '--format=', sha],
        capture_output=True, text=True
    )
    default_patch = default_patch_result.stdout

    # Count lines
    insertions = len([l for l in default_patch.split('\n') if l.startswith('+') and not l.startswith('+++')])
    deletions = len([l for l in default_patch.split('\n') if l.startswith('-') and not l.startswith('---')])
    total_lines = insertions + deletions

    # Extract files
    files = re.findall(r'diff --git a/(.+?) b/', default_patch)
    rust_files = [f for f in files if f.endswith('.rs')]

    # Parse identifiers from the default patch (easier to parse)
    parser = RustIdentifierParser()
    rust_files_info = []

    for rust_file in rust_files:
        # Extract the diff section for this file
        file_diff_match = re.search(
            rf'diff --git a/{re.escape(rust_file)} b/{re.escape(rust_file)}.*?(?=diff --git|$)',
            default_patch,
            re.DOTALL
        )

        if file_diff_match:
            file_diff = file_diff_match.group(0)

            # Get added and removed lines
            added_lines = []
            removed_lines = []

            for line in file_diff.split('\n'):
                if line.startswith('+') and not line.startswith('+++'):
                    added_lines.append(line[1:])
                elif line.startswith('-') and not line.startswith('---'):
                    removed_lines.append(line[1:])

            # Parse identifiers
            added_code = '\n'.join(added_lines)
            removed_code = '\n'.join(removed_lines)

            identifiers_added = parser.extract_identifiers(added_code)
            identifiers_removed = parser.extract_identifiers(removed_code)

            rust_files_info.append({
                'filename': rust_file,
                'added': identifiers_added,
                'removed': identifiers_removed
            })

    return {
        'sha': sha,
        'short_sha': sha[:8],
        'message': message,
        'patch': full_patch,  # Full 50-line context patch
        'files': files,
        'rust_files': rust_files,
        'rust_files_info': rust_files_info,  # Detailed identifiers
        'lines_changed': total_lines,
        'context_lines': context_lines
    }


def format_sft_response(rust_files_info):
    """Format detailed identifiers into SFT response"""
    response_parts = ["Files to modify:\n"]

    for file_info in rust_files_info:
        filename = file_info['filename']
        added = file_info['added']
        removed = file_info['removed']

        response_parts.append(f"\n**{filename}**")

        changes = []

        # Removals
        if any(removed.values()):
            removed_items = []
            for key, items in removed.items():
                if items:
                    removed_items.extend([f"{key[:-1]}: {item}" for item in items])
            if removed_items:
                changes.append(f"  Remove:\n    - " + "\n    - ".join(removed_items))

        # Additions
        if any(added.values()):
            added_items = []
            for key, items in added.items():
                if items:
                    added_items.extend([f"{key[:-1]}: {item}" for item in items])
            if added_items:
                changes.append(f"  Add:\n    - " + "\n    - ".join(added_items))

        if changes:
            response_parts.append("\n".join(changes))
        else:
            response_parts.append("  Modify existing code")

    return "\n".join(response_parts)


def save_commit_sft(commit_data: dict, output_dir: Path, index: int):
    """Save commit in SFT format with detailed identifiers"""

    prompt = commit_data['message']
    response = format_sft_response(commit_data['rust_files_info'])

    sft_entry = {
        'prompt': prompt,
        'response': response
    }

    # Save JSONL
    filename = f"{index:05d}_{commit_data['short_sha']}_{commit_data['sha']}.jsonl"
    with open(output_dir / filename, 'w') as f:
        json.dump(sft_entry, f, ensure_ascii=False)
        f.write('\n')

    # Save full context patch separately
    patch_filename = f"{index:05d}_{commit_data['short_sha']}_{commit_data['sha']}.patch"
    with open(output_dir / patch_filename, 'w') as f:
        f.write(commit_data['patch'])


def main():
    parser = argparse.ArgumentParser(
        description="Generate commits with detailed identifiers AND full context"
    )
    parser.add_argument("repo_path", help="Path to git repository")
    parser.add_argument("-U", "--context", type=int, default=50,
                       help="Context lines in patch (default: 50)")
    parser.add_argument("-m", "--min-lines", type=int, default=50,
                       help="Min lines changed (default: 50)")
    parser.add_argument("-o", "--output", default="commits_full",
                       help="Output directory")
    parser.add_argument("-b", "--branch", help="Specific branch")

    args = parser.parse_args()

    print("=" * 80)
    print("🦀 Full Commit Extractor (Identifiers + Context)")
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
            commit_data = get_commit_with_full_context(args.repo_path, sha, args.context)

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
