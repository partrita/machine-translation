#!/usr/bin/env python3
"""
Merge all translated small chunks into final index.qmd
"""
import os
import glob

TRANSLATED_DIR = "converted/personal-mba/personal-mba-ko/chunks-small"
OUTPUT_FILE = "mybook/personal-mba/index.qmd"

files = sorted(glob.glob(os.path.join(TRANSLATED_DIR, "chunk-*-ko.md")))

print(f"Found {len(files)} translated chunk files")

parts = []
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        parts.append(fh.read().strip())

merged = "\n\n".join(parts)

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(merged)

print(f"Written to {OUTPUT_FILE}: {len(merged)} chars, {len(merged.splitlines())} lines")
