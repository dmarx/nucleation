# scratch/formal/schema_rates.py
"""Measure how fast a luria record's grammar grows, level by level, from git.

The owner's hierarchy (2026-10-27): documents are filed faster than
vocabularies grow, vocabularies faster than schemes gain or change fields,
fields faster than new schemes are declared, and schemes faster than new
projects are begun. For each level this counts declarations (and changes and
removals) in luria.yaml over the history, as events per day and as distinct
days with an event, with the gaps between those days and their burstiness.

It also asks how each refinement happened, by the unit of work it came in (the
pull request when the commit can be tied to one, else the commit):

- on demand: the same unit files documents, and for a vocabulary term, a
  document changed in the unit carries the term in its frontmatter;
- by decision: the same unit adds or changes an ADR.

Levels:
- doc: a document added to a scheme's directory by an authored commit;
- term: a vocabulary term; vocabulary: a vocabulary;
- member: a field or a relation (reference) of a scheme;
- scheme: a scheme;
- remote: an entry under `remotes:`, a project this record can cite.

Commits by github-actions[bot] are not counted as declarations of documents
(concretization renames, views). luria.yaml before its first appearance is
not read: a project whose grammar lived elsewhere first shows only what came
after.

Usage: python -I scratch/formal/schema_rates.py [REPO]   (default: cwd)
"""
import json
import re
import statistics
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml

LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
BOT = "github-actions[bot]"
FM = re.compile(r"\A---\n(.*?)\n---", re.S)
LEVELS = ("doc", "term", "vocabulary", "member", "scheme", "remote")


def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True,
                          text=True, check=True).stdout


def show(repo, rev, path):
    r = subprocess.run(["git", "-C", str(repo), "show", f"{rev}:{path}"],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def load(text):
    try:
        c = yaml.load(text, Loader=LOADER) if text else {}
    except yaml.YAMLError:
        return None
    return c if isinstance(c, dict) else {}


def pieces(config):
    """level -> {key: comparable declaration} for one parsed luria.yaml."""
    out = {lv: {} for lv in LEVELS if lv != "doc"}
    for name, s in (config.get("schemes") or {}).items():
        s = s or {}
        out["scheme"][name] = s.get("dir")
        for k, r in (s.get("references") or {}).items():
            out["member"][(name, "ref", k)] = json.dumps(r, sort_keys=True, default=str)
        for k, f in (s.get("fields") or {}).items():
            out["member"][(name, "field", k)] = json.dumps(f, sort_keys=True, default=str)
    for name, v in (config.get("vocabularies") or {}).items():
        out["vocabulary"][name] = True
        v = v or {}
        # Terms sit under `terms:`, or are the vocabulary's own keys in older layouts.
        terms = v.get("terms") if "terms" in v else v
        for t, d in (terms if isinstance(terms, dict) else {}).items():
            # A term's label and blurb are its declaration; rewording them is a change.
            out["term"][(name, t)] = json.dumps(d, sort_keys=True, default=str)
    for name, r in (config.get("remotes") or {}).items():
        out["remote"][name] = json.dumps(r, sort_keys=True, default=str)
    return out


def units(repo):
    """commit -> pull request number, for commits brought in by a merge or a squash."""
    out = {}
    for line in git(repo, "log", "--first-parent", "--format=%H %P\t%s").splitlines():
        head, subject = line.split("\t", 1)
        sha, *parents = head.split()
        m = re.search(r"#(\d+)", subject)
        if not m:
            continue
        if len(parents) == 2:
            for c in git(repo, "rev-list", f"{parents[0]}..{parents[1]}").split():
                out.setdefault(c, int(m.group(1)))
        out.setdefault(sha, int(m.group(1)))
    return out


def frontmatter_words(text):
    m = FM.match(text or "")
    if not m:
        return set()
    try:
        fm = yaml.load(m.group(1), Loader=LOADER) or {}
    except yaml.YAMLError:
        return set()
    words = set()
    for v in (fm.values() if isinstance(fm, dict) else []):
        for x in (v if isinstance(v, list) else [v]):
            if isinstance(x, (str, int)):
                words.add(str(x))
    return words


def gaps_report(label, times, t_start, t_end):
    days = (t_end - t_start) / 86400
    dates = sorted({datetime.fromtimestamp(t, timezone.utc).date() for t in times})
    gaps = [(b - a).days for a, b in zip(dates, dates[1:])]
    cv = (statistics.pstdev(gaps) / statistics.mean(gaps)) if len(gaps) > 1 and statistics.mean(gaps) else float("nan")
    half = t_start + (t_end - t_start) / 2
    first = sum(1 for t in times if t < half)
    print(f"  {label:22s} events={len(times):5d} per day={len(times) / days:7.2f} "
          f"days with one={len(dates):3d} of {days:4.0f} "
          f"median gap={statistics.median(gaps) if gaps else float('nan'):4.1f} d "
          f"gap CV={cv:4.2f} first half/second half={first}/{len(times) - first}")


def main(repo="."):
    repo = Path(repo)
    pr = units(repo)
    log = git(repo, "log", "--no-merges", "--reverse", "--format=%H\t%at\t%an", "--", "luria.yaml")
    config_commits = [l.split("\t") for l in log.splitlines()]
    if not config_commits:
        print("no luria.yaml in history")
        return
    t_start = int(config_commits[0][1])
    t_end = int(git(repo, "log", "-1", "--format=%at").strip())

    events = defaultdict(list)          # (level, kind) -> [(t, unit)]
    for sha, t, author in config_commits:
        new = load(show(repo, sha, "luria.yaml"))
        old = load(show(repo, f"{sha}^", "luria.yaml"))
        if new is None or old is None:
            continue
        a, b = pieces(old), pieces(new)
        unit = pr.get(sha, sha)
        for lv in b:
            for k in b[lv].keys() - a[lv].keys():
                events[(lv, "added", k)].append((int(t), unit))
            for k in a[lv].keys() - b[lv].keys():
                events[(lv, "removed", k)].append((int(t), unit))
            for k in a[lv].keys() & b[lv].keys():
                if a[lv][k] != b[lv][k]:
                    events[(lv, "changed", k)].append((int(t), unit))

    # Documents filed, and what each unit of work touched.
    final = pieces(load(show(repo, "HEAD", "luria.yaml")) or {})
    dirs = {load(show(repo, "HEAD", "luria.yaml"))["schemes"][s].get("dir") for s in final["scheme"]}
    dirs |= {"record/decisions.d", "docs/decisions"}
    touched = defaultdict(lambda: {"docs": 0, "adr": 0, "adr_new": 0, "words": set()})
    out = git(repo, "log", "--no-merges", "--format=@%H\t%at\t%an", "--name-status", "--no-renames",
              "--", *[d for d in dirs if d])
    sha = t = author = None
    for line in out.splitlines():
        if line.startswith("@"):
            sha, t, author = line[1:].split("\t")
            continue
        if not line.strip() or author == BOT:
            continue
        status, path = line.split("\t")[0], line.split("\t")[-1]
        if not path.endswith(".md") or "/_" in path or path.endswith(("README.md", "README.stub")):
            continue
        unit = touched[pr.get(sha, sha)]
        if "decisions" in path and re.search(r"ADR-", path):
            unit["adr"] += 1
            unit["adr_new"] += status == "A"
        if status == "A":
            unit["docs"] += 1
            events[("doc", "added", path)].append((int(t), pr.get(sha, sha)))
        if status in "AM":
            unit["words"] |= frontmatter_words(show(repo, sha, path))

    span = (t_end - t_start) / 86400
    print(f"{repo.resolve().name}: luria.yaml from "
          f"{datetime.fromtimestamp(t_start, timezone.utc):%Y-%m-%d} to "
          f"{datetime.fromtimestamp(t_end, timezone.utc):%Y-%m-%d} ({span:.1f} days); "
          f"declared now: " + ", ".join(f"{lv} {len(final[lv])}" for lv in final))
    scaffold = int(config_commits[0][1])
    for title, after in (("all events since luria.yaml was first written", t_start - 1),
                         ("the first luria.yaml commit left out", scaffold)):
        print(f"\nRates, by level ({title}):")
        for lv in LEVELS:
            for kind in ("added", "changed", "removed"):
                times = [t for (l, k, _), ev in events.items() if l == lv and k == kind
                         for t, _ in ev if t > after]
                if times:
                    gaps_report(f"{lv} {kind}", times, t_start, t_end)

    def shares(us):
        n = max(len(us), 1)
        return (f"units={len(us):3d} filing documents={sum(1 for u in us if touched[u]['docs']) / n:4.0%} "
                f"touching an ADR={sum(1 for u in us if touched[u]['adr']) / n:4.0%} "
                f"adding an ADR={sum(1 for u in us if touched[u]['adr_new']) / n:4.0%}")

    print("\nHow each declaration came in (share of the units of work that declared one):")
    print(f"  {'baseline':10s} {shares({u for u in touched if isinstance(u, int)})}  (every pull request touching the record)")
    for lv in LEVELS[1:]:
        us = {u for (l, k, _), ev in events.items() if l == lv and k == "added" for _, u in ev}
        if not us:
            continue
        with_lower = {}
        for lower in LEVELS[1:LEVELS.index(lv)]:
            lus = {u for (l, k, _), ev in events.items() if l == lower and k == "added" for _, u in ev}
            with_lower[lower] = sum(1 for u in us if u in lus)
        print(f"  {lv:10s} {shares(us)} "
              + " ".join(f"also adding a {k}={v / len(us):4.0%}" for k, v in with_lower.items()))
    terms = [(k, u) for (l, kind, k), ev in events.items() if l == "term" and kind == "added"
             for t, u in ev[:1] if t > t_start + 3600]
    used = sum(1 for (vocab, term), u in terms if str(term) in touched[u]["words"])
    if terms:
        print(f"  terms added after the first hour: {len(terms)}; used in the frontmatter of a "
              f"document the same unit changed: {used / len(terms):.0%}")


if __name__ == "__main__":
    main(*sys.argv[1:])
