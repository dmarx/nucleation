"""Check changed record files: frontmatter parses, title has no code, H1 matches.

Usage: python3 -I check.py FILE...   (exits non-zero on any failure)
"""
import re
import sys

import yaml

CODE = re.compile(r"\b[A-Z]+-(?:\d+|tmp[a-z0-9]+)\b")
bad = 0
for path in sys.argv[1:]:
    text = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        print(path, "no frontmatter"); bad += 1; continue
    try:
        fm = yaml.safe_load(m.group(1))
    except Exception as e:  # noqa: BLE001
        print(path, "yaml:", e); bad += 1; continue
    title = fm.get("title", "")
    if CODE.search(title):
        print(path, "code in title"); bad += 1
    stem = path.rsplit("/", 1)[-1][:-3]
    h1 = re.search(r"^# (.+)$", text[m.end():], re.M)
    want = f"{stem}: {title}"
    if not h1 or h1.group(1).strip() != want:
        print(path, "H1 mismatch:", h1.group(1) if h1 else None); bad += 1
    if fm.get("version", 1) > 1 and not fm.get("history"):
        print(path, "version > 1 without history"); bad += 1
print("checked", len(sys.argv) - 1, "files,", bad, "problems")
sys.exit(1 if bad else 0)
