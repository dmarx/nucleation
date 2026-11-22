"""Pre-commit checks for changed record files (run with python3 -I).

For each path: frontmatter parses with yaml.safe_load; title carries no
code (no LIT-/NOTE-/THEORY-/CLAIM-/... token); H1 matches the title.
"""
import sys, re, yaml

CODE = re.compile(r"\b(LIT|NOTE|THEORY|ADR|DP|QUESTION|CLAIM|CASE|TERM|ARG|LEAD|"
                  r"POSTMORTEM|RETRO|SYNTHESIS)-[A-Za-z0-9]+\b")
ok = True
for p in sys.argv[1:]:
    txt = open(p, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", txt, re.S)
    if not m:
        print("FAIL no frontmatter:", p); ok = False; continue
    try:
        fm = yaml.safe_load(m.group(1))
    except Exception as e:
        print("FAIL yaml:", p, e); ok = False; continue
    title = fm.get("title", "")
    if CODE.search(title):
        print("FAIL code-in-title:", p, title); ok = False
    body = m.group(2)
    h1 = re.search(r"^#\s+(.*)$", body, re.M)
    if not h1:
        print("FAIL no H1:", p); ok = False; continue
    h1txt = h1.group(1)
    # H1 form: "<CODE>: <title>"
    after = h1txt.split(":", 1)
    if len(after) == 2:
        h1title = after[1].strip()
    else:
        h1title = h1txt.strip()
    if h1title != title.strip():
        print("FAIL h1!=title:", p); print("  title:", repr(title.strip()))
        print("  h1   :", repr(h1title)); ok = False
if ok:
    print("OK", len(sys.argv) - 1, "files")
sys.exit(0 if ok else 1)
