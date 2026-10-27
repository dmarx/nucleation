# scratch/formal/record_rates.py
"""Measure how fast each layer of this record changes, from its git history.

For CLAIM-tmpmx2ql, CLAIM-tmpl228b and CLAIM-tmpoe0v5: do the record's layers
(the prose of entries, their standing, the relations between them, and the
grammar that declares the relation types) change on separated time scales?

Every non-merge commit reachable from HEAD is read. For each document of a
declared scheme, and for luria.yaml, the old and new versions are compared and
the change is classed:

- body: the prose below the frontmatter changed;
- status: the `status:` field changed;
- edge: an authored relation field gained or lost a target (fields the link
  fixer writes, the converses, are excluded; `complements` is symmetric and
  kept as authored);
- grammar: in luria.yaml, a scheme, a reference (relation type) of a scheme,
  or a field of a scheme was added, removed or redeclared; vocabulary terms are
  counted apart;
- pin: the luria version pinned in the workflows changed.

Commits by github-actions[bot] are machine commits (link repair,
concretization, views); their body changes are counted apart as `body-bot`.
A document keeps its identity through renames and through concretization:
a file added with `formerly: [X]` continues X.

Rate of a layer: its changes after filing, divided by the days each object has
existed (object-days); tau is the inverse. Changes in the first day after filing
are drafting, so a settled tau is also given, over the time after that day.
A tau longer than the 50-day history rests on few events and is an
extrapolation. Frontmatter outside `status:` and the relation fields (title,
summary, version, history) is in none of the layers. For luria.yaml, a piece's
rate counts redeclarations only; additions are its filings.

Usage: python -I scratch/formal/record_rates.py [REPO]   (default: cwd)
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
FM = re.compile(r"\A---\n(.*?)\n---\n?(.*)\Z", re.S)


def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True,
                          text=True, check=True).stdout


class Blobs:
    """Read file contents at a commit through one `git cat-file --batch`."""

    def __init__(self, repo):
        self.p = subprocess.Popen(["git", "-C", str(repo), "cat-file", "--batch"],
                                  stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def get(self, rev, path):
        self.p.stdin.write(f"{rev}:{path}\n".encode())
        self.p.stdin.flush()
        header = self.p.stdout.readline().decode()
        if header.endswith("missing\n"):
            return None
        size = int(header.split()[2])
        data = self.p.stdout.read(size)
        self.p.stdout.read(1)
        return data.decode("utf-8", "replace")


def split(text):
    """(frontmatter dict, body) of a record document; ({}, text) if none."""
    if text is None:
        return None, None
    m = FM.match(text)
    if not m:
        return {}, text
    try:
        fm = yaml.load(m.group(1), Loader=LOADER) or {}
    except yaml.YAMLError:
        fm = {}
    return (fm if isinstance(fm, dict) else {}), m.group(2)


def as_set(v):
    if v is None:
        return set()
    if isinstance(v, list):
        return {str(x) for x in v}
    return {str(v)}


def schemes(config):
    """dir -> (scheme, authored relation fields) from a parsed luria.yaml."""
    out = {}
    for name, s in (config.get("schemes") or {}).items():
        refs = s.get("references") or {}
        authored = [k for k, r in refs.items()
                    if not re.search(r"written by|converse of", str((r or {}).get("blurb", "")))]
        out[s.get("dir")] = (name, authored)
    return out


def grammar(config):
    """The declared grammar as comparable pieces: scheme set, relation types, fields."""
    pieces = {}
    for name, s in (config.get("schemes") or {}).items():
        pieces[("scheme", name)] = s.get("dir")
        for k, r in (s.get("references") or {}).items():
            r = r or {}
            pieces[("relation", name, k)] = json.dumps(
                {"scheme": r.get("scheme"), "converse": r.get("converse"),
                 "many": r.get("many"), "required": r.get("required")}, sort_keys=True)
        for k, f in (s.get("fields") or {}).items():
            pieces[("field", name, k)] = json.dumps(f, sort_keys=True, default=str)
    vocab = {}
    for name, v in (config.get("vocabularies") or {}).items():
        vocab[name] = set((v or {}).get("terms") or {})
    return pieces, vocab


def main(repo="."):
    repo = Path(repo)
    blobs = Blobs(repo)
    log = git(repo, "log", "--no-merges", "--reverse", "--format=%H%x09%an%x09%ct", "HEAD")
    commits = [l.split("\t") for l in log.splitlines()]
    events = defaultdict(list)      # (layer, object) -> [time]
    filed = {}                      # object -> time
    alias = {}                      # path or code -> object id
    edge_born = {}                  # (object, field, target) -> time
    edge_life = []                  # completed edge lifetimes (days)
    edge_births = 0
    piece_born = {}                 # grammar piece -> first appearance
    counts = defaultdict(int)
    vocab_events = []
    pin_events = []
    grammar_now, vocab_now = {}, {}
    sch = {}
    last_pin = None
    # a tmp code and the number it was concretized to are one target
    formerly = {}
    for path in git(repo, "ls-files", "record").splitlines():
        if path.endswith(".md"):
            fm, _ = split(blobs.get("HEAD", path))
            for x in as_set((fm or {}).get("formerly")):
                formerly[x] = Path(path).stem

    def norm(code):
        return formerly.get(code, code)

    t0 = int(commits[0][2])

    for sha, author, ts in commits:
        t = int(ts)
        bot = author == BOT
        parent = git(repo, "rev-parse", f"{sha}^").strip() if sha != commits[0][0] else None
        diff = git(repo, "diff-tree", "--no-commit-id", "-r", "-M", "--name-status",
                   *( [parent, sha] if parent else ["--root", sha]))
        for line in diff.splitlines():
            parts = line.split("\t")
            st = parts[0]
            old_path = parts[1]
            new_path = parts[-1]
            if new_path == "luria.yaml" or old_path == "luria.yaml":
                cfg = yaml.load(blobs.get(sha, "luria.yaml") or "", Loader=LOADER) or {}
                pieces, vocab = grammar(cfg)
                for key in pieces:
                    piece_born.setdefault(key, t)
                for key in set(pieces) | set(grammar_now):
                    if pieces.get(key) != grammar_now.get(key) and grammar_now and key in grammar_now:
                        events[("grammar", key[0])].append(t)
                        events[("grammar-piece", key)].append(t)
                for name in set(vocab) | set(vocab_now):
                    if vocab.get(name, set()) != vocab_now.get(name, set()) and vocab_now:
                        vocab_events.append((t, name))
                grammar_now, vocab_now = pieces, vocab
                sch = schemes(cfg)
                continue
            if new_path.startswith(".github/workflows/"):
                text = blobs.get(sha, new_path) or ""
                pin = tuple(sorted(set(re.findall(r"luria==([\d.]+)", text))))
                if pin and pin != last_pin:
                    if last_pin is not None:
                        pin_events.append((t, pin))
                    last_pin = pin
                continue
            d = str(Path(new_path).parent)
            if d not in sch or not new_path.endswith(".md") or Path(new_path).name.startswith("_"):
                continue
            scheme, authored = sch[d]
            new_fm, new_body = split(blobs.get(sha, new_path) if st[0] != "D" else None)
            old_fm, old_body = split(blobs.get(parent, old_path) if parent and st[0] != "A" else None)
            # identity
            if st[0] == "R":
                obj = alias.get(old_path, old_path)
            elif st[0] == "A":
                prior = [alias.get(str(Path(d) / f"{x}.md")) for x in as_set((new_fm or {}).get("formerly"))]
                prior = [p for p in prior if p]
                obj = prior[0] if prior else new_path
            else:
                obj = alias.get(old_path, old_path)
            alias[new_path] = obj
            obj = (scheme, obj)
            if new_fm is None:            # deleted (retired by deletion is rare)
                continue
            if obj not in filed:
                filed[obj] = t
                for layer in ("body", "status", "edge"):
                    events[(layer, obj)].append(t)
                for f in authored:
                    for x in as_set(new_fm.get(f)):
                        edge_born[(obj, f, norm(x))] = t
                        edge_births += 1
                counts["filed", scheme] += 1
                continue
            if old_fm is None:
                continue
            if (old_body or "").strip() != (new_body or "").strip():
                events[("body-bot" if bot else "body", obj)].append(t)
                counts["body-bot" if bot else "body", scheme] += 1
            if str(old_fm.get("status")) != str(new_fm.get("status")):
                events[("status", obj)].append(t)
                counts["status", scheme] += 1
            changed_edge = False
            for f in authored:
                if bot:                   # link completion and concretization are mechanical
                    continue
                a = {norm(x) for x in as_set(old_fm.get(f))}
                b = {norm(x) for x in as_set(new_fm.get(f))}
                for x in b - a:
                    edge_born[(obj, f, x)] = t
                    edge_births += 1
                    changed_edge = True
                for x in a - b:
                    born = edge_born.pop((obj, f, x), None)
                    if born is not None:
                        edge_life.append((t - born) / 86400)
                    changed_edge = True
            if changed_edge:
                events[("edge", obj)].append(t)
                counts["edge", scheme] += 1

    now = int(commits[-1][2])
    days = (now - t0) / 86400

    def exposure_rate(births, changes):
        """Changes per object per day over the time each object has existed, and its inverse."""
        exp = sum((now - b) / 86400 for b in births.values())
        n = sum(len(set(changes.get(k, []))) for k in births)
        return n, exp, (n / exp if exp else float("nan"))

    def row(label, births, changes, early=None):
        n, exp, rate = exposure_rate(births, changes)
        changed = sum(1 for k in births if changes.get(k))
        tau = 1 / rate if rate else float("inf")
        extra = ""
        if early is not None:
            # The first day after filing is drafting; the rate after it is the settled rate.
            e = sum(1 for k in births for c in set(changes.get(k, [])) if c - births[k] <= 86400)
            late_exp = sum(max(now - b - 86400, 0) / 86400 for b in births.values())
            late_tau = late_exp / (n - e) if n - e else float("inf")
            extra = f"; within a day of filing {e / max(n, 1):.0%}; settled tau={late_tau:7.1f} d"
        print(f"  {label:34s} objects={len(births):5d} changed={changed / max(len(births), 1):4.0%} "
              f"changes={n:5d} object-days={exp:9.0f} rate={rate:.4f}/day tau={tau:8.1f} d{extra}")

    print(f"history: {len(commits)} non-merge commits over {days:.1f} days "
          f"({datetime.fromtimestamp(t0, timezone.utc):%Y-%m-%d} to "
          f"{datetime.fromtimestamp(now, timezone.utc):%Y-%m-%d}); "
          f"authored {sum(1 for c in commits if c[1] != BOT)}, bot {sum(1 for c in commits if c[1] == BOT)}")

    def layer(name, scheme=None):
        births = {o: b for o, b in filed.items() if scheme is None or o[0] == scheme}
        changes = {}
        for (lay, o), ts in events.items():
            if lay == name and o in births:
                changes[o] = [x for x in ts if x > births[o]]
        return births, changes

    print("\nDocuments (rate of change per document-day; tau = 1/rate):")
    for scheme in ("CLAIM", "THEORY", "LIT", "QUESTION", "TERM", "CASE", None):
        for name in ("body", "status", "edge"):
            b, c = layer(name, scheme)
            row(f"{scheme or 'ALL'} {name} (authored)", b, c, early=True)
        b, c = layer("body-bot", scheme)
        row(f"{scheme or 'ALL'} body (bot repair)", b, c)

    print("\nAuthored relation instances (edges):")
    print(f"  declared={edge_births} removed={len(edge_life)} standing={len(edge_born)}")
    exp = sum((now - t) / 86400 for t in edge_born.values()) + sum(edge_life)
    print(f"  removals per edge-day={len(edge_life) / exp:.5f} tau={exp / max(len(edge_life), 1):.0f} d; "
          f"removed edges lived: median={statistics.median(edge_life):.2f} d" if edge_life else "  none removed")

    print("\nGrammar (luria.yaml), per declared piece:")
    for kind in ("scheme", "relation", "field"):
        births = {k: b for k, b in piece_born.items() if k[0] == kind}
        changes = {k: [x for x in ts if x > births[k]] for (lay, k), ts in events.items()
                   if lay == "grammar-piece" and k in births}
        row(f"{kind} declarations", births, changes)
    gc = sorted({t for (lay, k), ts in events.items() if lay == "grammar" for t in ts})
    print(f"  commits changing any scheme, relation type or field: {len(gc)} ({len(gc) / days:.2f}/day)")
    vt = sorted({t for t, _ in vocab_events})
    print(f"  commits changing a vocabulary: {len(vt)} ({len(vt) / days:.2f}/day): " +
          ", ".join(f"{n} {sum(1 for _, m in vocab_events if m == n)}" for n in sorted({n for _, n in vocab_events})))
    print(f"  luria version pin changes: {len(pin_events)}")
    for kind in ("scheme", "relation", "field"):
        ds = sorted(round((b - t0) / 86400) for k, b in piece_born.items() if k[0] == kind)
        print(f"  {kind} filed on days: {ds}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
