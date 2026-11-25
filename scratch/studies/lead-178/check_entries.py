"""Check changed record files: frontmatter parses, title has no code,
H1 matches the title. Usage: python3 -I check_entries.py FILE..."""
import re
import sys

import yaml

CODE = re.compile(r"\b[A-Z]+-(?:\d+|tmp[a-z0-9]+)\b")
bad = 0
for path in sys.argv[1:]:
    text = open(path).read()
    parts = text.split("---\n", 2)
    fm = yaml.safe_load(parts[1])
    title = fm["title"]
    m = re.search(r"^# ([A-Z]+-(?:\d+|tmp[a-z0-9]+)): (.*)$", parts[2], re.M)
    ok = True
    if CODE.search(title):
        print(path, "title has a code"); ok = False
    if not m or m.group(2) != title:
        print(path, "H1 does not match title"); ok = False
    bad += not ok
    print(path, "ok" if ok else "FAIL")
sys.exit(bad)
