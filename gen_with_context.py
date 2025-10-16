#!/usr/bin/env python3
"""
Generate commits with MORE context lines using git show -U<N>

This gives you more surrounding code so you can see function names!
"""

import subprocess
import sys
from pathlib import Path

# Quick script - just modify generate.py to use git show directly
repo = sys.argv[1] if len(sys.argv) > 1 else "/tmp/hyperswitch"
context = int(sys.argv[2]) if len(sys.argv) > 2 else 10
min_lines = int(sys.argv[3]) if len(sys.argv) > 3 else 50

print(f"📦 Repo: {repo}")
print(f"📏 Context lines: {context}")
print(f"📏 Min lines: {min_lines}")
print("This uses git show -U{context} for more surrounding code!")
