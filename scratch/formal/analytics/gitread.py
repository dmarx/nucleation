# scratch/formal/analytics/gitread.py
"""Read a luria record as it stood at one git revision.

Every figure the pipeline computes is read from a commit, never from the
working tree, so that the commit named in `computed_at` is the record state
the figure describes. Blob reads go through one `git cat-file --batch`
(record_rates.Blobs); frontmatter is split by record_rates.split.
"""
import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
for p in (HERE.parent, HERE.parent / "decision-census"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

import record_rates as rr  # noqa: E402  (Blobs, split)

LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


def git(repo: str | Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True,
                          text=True, check=True).stdout


def resolve(repo: str | Path, rev: str) -> str:
    """The full sha of rev."""
    return git(repo, "rev-parse", "--verify", f"{rev}^{{commit}}").strip()


def has_rev(repo: str | Path, rev: str) -> bool:
    r = subprocess.run(["git", "-C", str(repo), "rev-parse", "--verify", "-q", f"{rev}^{{commit}}"],
                       capture_output=True, text=True)
    return r.returncode == 0


def commit_info(repo: str | Path, rev: str) -> dict:
    """sha, committer date and subject of rev."""
    sha, date, subject = git(repo, "log", "-1", "--format=%H%x09%cI%x09%s", rev).rstrip("\n").split("\t", 2)
    return {"sha": sha, "short": sha[:9], "date": date, "subject": subject}


def last_first_parent_by(repo: str | Path, ref: str, day: str) -> str | None:
    """The last first-parent commit on ref by 23:59:59 UTC on day (YYYY-MM-DD)."""
    out = git(repo, "rev-list", "-1", "--first-parent", f"--before={day}T23:59:59Z", ref).strip()
    return out or None


def ls_files(repo: str | Path, rev: str) -> list[str]:
    """Every file path in the tree of rev."""
    return git(repo, "ls-tree", "-r", "--name-only", rev).splitlines()


def read_text(repo: str | Path, rev: str, path: str) -> str | None:
    r = subprocess.run(["git", "-C", str(repo), "show", f"{rev}:{path}"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def load_yaml(text: str | None) -> dict:
    if not text:
        return {}
    c = yaml.load(text, Loader=LOADER)
    return c if isinstance(c, dict) else {}


def is_entry(path: str, directory: str) -> bool:
    """A record entry: a .md file directly in the scheme's directory, not a template or README."""
    p = Path(path)
    return (str(p.parent) == directory.rstrip("/") and p.suffix == ".md"
            and not p.name.startswith("_") and p.name != "README.md")


def read_entries(repo: str | Path, rev: str, files: list[str], dirs: dict[str, str]) -> list[dict]:
    """[{code, scheme, path, fm}] for every entry of every scheme (dirs: scheme -> directory)."""
    by_dir = {d.rstrip("/"): s for s, d in dirs.items() if d}
    blobs = rr.Blobs(repo)
    out = []
    try:
        for path in files:
            scheme = by_dir.get(str(Path(path).parent))
            if scheme and is_entry(path, str(Path(path).parent)):
                fm, _ = rr.split(blobs.get(rev, path))
                out.append({"code": Path(path).stem, "scheme": scheme, "path": path, "fm": fm or {}})
    finally:
        blobs.p.stdin.close()
        blobs.p.wait()
    return out


def _flat(v) -> list[str]:
    if v is None:
        return []
    return [str(x) for x in v] if isinstance(v, list) else [str(v)]


def crosstab(entries: list[dict], row: str, col: str) -> dict[str, dict[str, int]]:
    """{row value: {col value: count}} over the entries' frontmatter (lists count each member)."""
    out: dict[str, Counter] = {}
    for e in entries:
        for r in _flat(e["fm"].get(row)) or ["None"]:
            for c in _flat(e["fm"].get(col)) or ["None"]:
                out.setdefault(r, Counter())[c] += 1
    return {r: dict(sorted(c.items())) for r, c in sorted(out.items())}


def vocabulary_terms(config: dict) -> dict[str, list[str]]:
    """vocabulary -> its terms; terms sit under `terms:` or are the vocabulary's own keys."""
    out = {}
    for name, v in (config.get("vocabularies") or {}).items():
        v = v or {}
        terms = v.get("terms") if "terms" in v else v
        out[name] = list(terms) if isinstance(terms, dict) else []
    return out


def grammar_counts(repo: str, sha: str) -> dict:
    """The §12.5 measures at one commit."""
    files = ls_files(repo, sha)
    text = read_text(repo, sha, "luria.yaml") or ""
    config = load_yaml(text)
    return {
        "commit": sha[:9],
        "date": commit_info(repo, sha)["date"],
        "repo_files": len(files),
        "record_files": sum(1 for f in files if f.startswith("record/")),
        "schemes": len(config.get("schemes") or {}),
        "vocabularies": len(config.get("vocabularies") or {}),
        "topic_terms": len(vocabulary_terms(config).get("topics", [])),
        "luria_yaml_lines": len(text.splitlines()),
    }
