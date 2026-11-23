"""Check the record files this lead changed, without running luria lint.

For each file: the frontmatter parses (yaml.safe_load), the title carries no
code, and the H1 is `# <CODE>: <title>` with the title's apostrophes single.
Then a narrow luria.ref_status scan of these files only: unexcused citations
of entries not in force, and excuses that excuse nothing.

Run from the worktree root:  python3 scratch/studies/lead-188/check_files.py FILE...
Exits non-zero on any finding.
"""
import re
import sys
from pathlib import Path

import yaml

CODE = re.compile(r"\b[A-Z]+-(?:\d{3,}|tmp[a-z0-9]{5})\b")


def check_shape(path: Path) -> list[str]:
    text = path.read_text()
    out = []
    if "changelog.d" in str(path):
        return out  # fragments carry no frontmatter
    if not text.startswith("---\n"):
        return [f"{path}: no frontmatter"]
    fm_text, body = text[4:].split("\n---\n", 1)
    try:
        fm = yaml.safe_load(fm_text)
    except yaml.YAMLError as e:
        return [f"{path}: frontmatter does not parse: {e}"]
    if "changelog.d" in str(path) or "curation.d" in str(path):
        return out
    title = fm.get("title", "")
    if CODE.search(title):
        out.append(f"{path}: title carries a code")
    code = path.stem
    h1 = next((ln for ln in body.splitlines() if ln.startswith("# ")), None)
    if h1 != f"# {code}: {title}":
        out.append(f"{path}: H1 does not match title\n  {h1}\n  # {code}: {title}")
    if fm.get("version", 1) > 1 and not fm.get("history"):
        out.append(f"{path}: version above 1 without history")
    return out


def check_refs(paths: list[Path]) -> list[str]:
    import luria.ref_status as r

    docs = r.load_docs()
    res = r.scan(files=paths, docs=docs)
    out = []
    for doc, loud, _ in r.flagged(res, docs):
        for c in loud:
            out.append(f"{c.path}:{c.line}: {c.code} not in force, unexcused")
    for code, sites, _ in r.dangling(res, docs):
        for c in sites:
            out.append(f"{c.path}:{c.line}: {code} names no document")
    out += r.stale_annotations(res, docs)
    return out


def main(argv: list[str]) -> int:
    paths = [Path(a).resolve() for a in argv]
    problems = []
    for p in paths:
        problems += check_shape(p)
    # ref_status scans neither changelog.d nor curation.d (scanned_files()).
    problems += check_refs([p for p in paths if p.suffix == ".md"
                            and "changelog.d" not in str(p)
                            and "curation.d" not in str(p)])
    for line in problems:
        print(line)
    print(f"{len(problems)} finding(s) in {len(paths)} file(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
