#!/usr/bin/env python3
"""
Translate personal-mba small chunks sequentially using agy CLI.
Usage: python3 translate_chunks.py [start_chunk] [end_chunk]
"""
import os
import sys
import subprocess
import time

CHUNKS_DIR = "converted/personal-mba/chunks-small"
OUTPUT_DIR = "converted/personal-mba/personal-mba-ko/chunks-small"
MODEL = "Claude Sonnet 4.6 (Thinking)"

os.makedirs(OUTPUT_DIR, exist_ok=True)

start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
end = int(sys.argv[2]) if len(sys.argv) > 2 else 151

PROMPT_TEMPLATE = """다음 영어 마크다운을 한국어로 번역하세요. 번역된 마크다운만 출력하고 설명은 절대 하지 마세요. 코드블록으로 감싸지 마세요.

번역 규칙:
1. 마크다운 서식(#/##/###, >, */-/1., **굵게**, *이탤릭*, 표, 링크)을 그대로 유지하세요.
2. 비즈니스 교양서 어조의 자연스러운 한국어 서술체(~다, ~한다)를 사용하세요.
3. 인명/회사명/지명은 한국어 발음 표기 후 괄호 안에 원어를 표기하세요. 전문 용어도 처음 등장시 영어를 괄호 안에 표기하세요.
4. YAML 프론트매터가 있으면 title을 "퍼스널 MBA (The Personal MBA)"로 번역하고 나머지는 유지하세요.

{content}"""

for i in range(start, end + 1):
    chunk_file = os.path.join(CHUNKS_DIR, f"chunk-{i:03d}.md")
    output_file = os.path.join(OUTPUT_DIR, f"chunk-{i:03d}-ko.md")

    if os.path.exists(output_file) and os.path.getsize(output_file) > 200:
        print(f"[SKIP] Chunk {i:03d} already done ({os.path.getsize(output_file)} bytes).", flush=True)
        continue

    if not os.path.exists(chunk_file):
        print(f"[WARN] Chunk {i:03d} not found, skipping.", flush=True)
        continue

    with open(chunk_file, 'r', encoding='utf-8') as f:
        content = f.read()

    prompt = PROMPT_TEMPLATE.format(content=content)

    print(f"[{i:03d}/{end}] Translating chunk-{i:03d} ({len(content)} chars)...", flush=True)

    for attempt in range(3):
        try:
            result = subprocess.run(
                ["agy", "--dangerously-skip-permissions",
                 "--model", MODEL,
                 "--print-timeout", "4m",
                 "--print", prompt],
                capture_output=True, text=True, timeout=260,
                cwd="/home/fkt/Downloads/repo/machine-translation"
            )
            translated = result.stdout.strip()
            if len(translated) > 200:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(translated)
                print(f"  Done: {len(translated)} chars", flush=True)
                break
            else:
                print(f"  [WARN attempt {attempt+1}] short: '{translated[:80]}'", flush=True)
                if result.stderr:
                    print(f"  stderr: {result.stderr[:200]}", flush=True)
                time.sleep(10)
        except subprocess.TimeoutExpired:
            print(f"  [TIMEOUT attempt {attempt+1}]", flush=True)
            time.sleep(10)
        except Exception as e:
            print(f"  [ERROR attempt {attempt+1}] {e}", flush=True)
            time.sleep(10)

    time.sleep(2)

print("All done!", flush=True)
