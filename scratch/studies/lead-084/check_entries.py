"""Pre-commit checks the run-lead skill asks for: frontmatter parses, the
title has no code, and the H1 matches the title. Usage:
python3 -I check_entries.py FILE..."""
import re
import sys

import yaml

CODE = re.compile(r"\b[A-Z]+-(\d{3,}|tmp[a-z0-9]+)\b")
ok = True
for path in sys.argv[1:]:
    text = open(path, encoding="utf-8").read()
    _, fm, body = text.split("---\n", 2)
    meta = yaml.safe_load(fm)
    title = meta["title"]
    code = path.rsplit("/", 1)[-1][:-3]
    h1 = [l for l in body.splitlines() if l.startswith("# ")][0]
    probs = []
    if CODE.search(title):
        probs.append("code in title")
    if h1 != f"# {code}: {title}":
        probs.append("H1 does not match title")
    print(path, "OK" if not probs else probs)
    ok &= not probs
sys.exit(0 if ok else 1)
