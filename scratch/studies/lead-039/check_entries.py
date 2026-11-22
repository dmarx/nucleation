"""Pre-commit check for LEAD-039's record files: frontmatter parses, the
title carries no code, and the H1 matches the title.

  python3 -I scratch/studies/lead-039/check_entries.py FILE...
"""
import re
import sys

import yaml

CODE = re.compile(r"\b(LIT|NOTE|THEORY|ADR|DP|QUESTION|CLAIM|CASE|TERM|ARG|LEAD|SYNTHESIS)-(\d+|tmp\w+)\b")
bad = 0
for path in sys.argv[1:]:
    text = open(path, encoding="utf-8").read()
    _, fm, body = text.split("---\n", 2)
    meta = yaml.safe_load(fm)
    title = meta.get("title")
    if title is None:  # fragments without a title
        print("ok (no title)", path)
        continue
    stem = path.rsplit("/", 1)[-1][:-3]
    problems = []
    if CODE.search(title):
        problems.append("code in title")
    h1 = re.search(r"^# (.+)$", body, re.M)
    if not h1 or h1.group(1) != f"{stem}: {title}":
        problems.append("H1 does not match title")
    print(("FAIL " + "; ".join(problems)) if problems else "ok", path)
    bad += bool(problems)
sys.exit(1 if bad else 0)
