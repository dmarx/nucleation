# scratch/formal/decision-census/term_changes.py
"""Were vocabulary terms that changed their declaration, or were removed,
carried through the documents that use them? (Prediction P3 of the manuscript.)

For every authored commit up to REV that changes a vocabulary term's
declaration (label, blurb, alert, group) or removes the term, report:
the date, the commit, the pull request (unit of work) it came in, which keys
changed, whether an ADR was added or changed in the same unit, how many
documents carried the term just before the change, and how many of those
were touched in the same unit (a proxy for being re-read).

Usage: python -I term_changes.py REPO [REV]   (REV default: HEAD)
Writes JSON to stdout.
"""
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import schema_rates as sr  # noqa: E402  (git, show, load, units)

BOT = "github-actions[bot]"


def term_decls(config):
    """(vocabulary, term) -> declaration dict, from a parsed luria.yaml."""
    out = {}
    for name, v in (config.get("vocabularies") or {}).items():
        v = v or {}
        terms = v.get("terms") if "terms" in v else v
        for t, d in (terms if isinstance(terms, dict) else {}).items():
            out[(name, t)] = d if isinstance(d, dict) else {"value": d}
    return out


def diff_terms(before, after):
    """Changed and removed terms: list of (key, kind, changed_keys)."""
    events = []
    for k, d in before.items():
        if k not in after:
            events.append((k, "removed", []))
        elif after[k] != d:
            keys = sorted(x for x in set(d) | set(after[k]) if d.get(x) != after[k].get(x))
            events.append((k, "changed", keys))
    return events


# Vocabularies used by one scheme only: search that scheme's directory, so that
# a common word ("Rejected") is not counted in schemes that never use the vocabulary.
SCOPE = {"synthesis": "record/syntheses.d/", "lit-": "record/literature.d/",
         "case-": "record/cases.d/", "arg-": "record/arguments.d/",
         "lead-": "record/leads.d/", "claim-": "record/claims.d/"}


def scope(vocab):
    return next((d for p, d in SCOPE.items() if vocab.startswith(p)), "record/")


def carriers(repo, rev, term, where="record/"):
    """Files under `where` whose frontmatter lists or names the term at rev."""
    r = subprocess.run(["git", "-C", repo, "grep", "-l", "-E",
                        rf"^\s*-\s*'?{term}'?\s*$|^[a-z_]+:\s*'?{term}'?\s*$",
                        rev, "--", where], capture_output=True, text=True)
    return {line.split(":", 1)[1] for line in r.stdout.splitlines() if ":" in line}


def unit_files(repo, commits):
    files = set()
    for c in commits:
        files |= set(sr.git(repo, "show", "--name-only", "--format=", c).split())
    return files


def events(repo=".", rev="HEAD"):
    """The term-change events up to rev, as a list of dicts (what `main` writes)."""
    unit_of = sr.units(repo)
    by_unit = {}
    for c, u in unit_of.items():
        by_unit.setdefault(u, []).append(c)
    log = sr.git(repo, "log", "--reverse", "--format=%H\t%an\t%aI", rev, "--", "luria.yaml")
    out = []
    for line in log.splitlines():
        sha, author, date = line.split("\t")
        if author == BOT:
            continue
        before = sr.load(sr.show(repo, f"{sha}^", "luria.yaml"))
        after = sr.load(sr.show(repo, sha, "luria.yaml"))
        if before is None or after is None:
            continue
        for (vocab, term), kind, keys in diff_terms(term_decls(before), term_decls(after)):
            unit = unit_of.get(sha)
            commits = by_unit.get(unit, [sha]) if unit else [sha]
            touched = unit_files(repo, commits)
            carry = carriers(repo, f"{sha}^", term, scope(vocab))
            out.append({
                "date": date[:10], "commit": sha[:9], "pr": unit, "vocabulary": vocab,
                "term": term, "kind": kind, "keys": keys,
                "adr_in_unit": any(f.startswith("record/decisions.d/ADR-") for f in touched),
                "carriers": len(carry), "carriers_touched": len(carry & touched),
            })
    return out


def main(repo=".", rev="HEAD"):
    json.dump(events(repo, rev), sys.stdout, indent=1)


if __name__ == "__main__":
    main(*sys.argv[1:])
