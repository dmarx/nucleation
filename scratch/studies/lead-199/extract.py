"""Walk origin/staging's non-merge history of record/ and emit
  - revisions.json: one row per (commit, claim file) change, classified
  - edges.json: inbound rests_on/grounds edge add/remove events
  - population.json: current claims (canonical code, aliases)
Usage: python3 -I extract.py REPO OUTDIR
"""
import json, os, re, subprocess, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from classify import classify, edges, CODE

REPO, OUT = sys.argv[1], sys.argv[2]
REF = "origin/staging"


def git(*a, inp=None):
    return subprocess.run(["git", "-C", REPO, *a], input=inp, capture_output=True,
                          check=True).stdout


# --- alias map from formerly: fields of every entry in the current tree
alias = {}
names = git("ls-tree", "-r", "--name-only", REF, "record/").decode().split("\n")
entry_paths = [p for p in names if re.match(r"record/[a-z]+\.d/[A-Z]+-[A-Za-z0-9]+\.md$", p)]


class Cat:
    def __init__(self):
        self.p = subprocess.Popen(["git", "-C", REPO, "cat-file", "--batch"],
                                  stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def get(self, spec):
        self.p.stdin.write((spec + "\n").encode()); self.p.stdin.flush()
        hdr = self.p.stdout.readline().decode().split()
        if len(hdr) < 3 or hdr[1] == "missing":
            return None
        n = int(hdr[2]); data = self.p.stdout.read(n); self.p.stdout.read(1)
        return data.decode("utf-8", "replace")


cat = Cat()
population = {}
for p in entry_paths:
    code = os.path.basename(p)[:-3]
    t = cat.get(f"{REF}:{p}")
    m = re.search(r"^formerly:\s*\n((?:- .*\n)+)", t or "", re.M)
    if m:
        for c in CODE.findall(m.group(1)):
            alias[c] = code
    if p.startswith("record/claims.d/"):
        st = re.search(r"^status:\s*(\S+)", t or "", re.M)
        population[code] = {"status": st.group(1) if st else None}

# renames seen in history (bot concretization) as a second source
log = git("log", REF, "--no-merges", "--format=format:X", "--name-status", "-M",
          "--diff-filter=R", "--", "record/").decode()
for line in log.splitlines():
    if line.startswith("R"):
        _, a, b = line.split("\t")
        ca, cb = os.path.basename(a)[:-3], os.path.basename(b)[:-3]
        alias.setdefault(ca, cb)


def canon(c):
    seen = 0
    while c in alias and alias[c] != c and seen < 10:
        c = alias[c]; seen += 1
    return c


for code in population:
    population[code]["aliases"] = sorted(a for a in alias if canon(a) == code)

# --- walk history
raw = git("log", REF, "--no-merges", "--reverse", "--no-abbrev", "--raw", "-M",
          "--format=C%x09%H%x09%at%x09%an%x09%s", "--", "record/").decode("utf-8", "replace")
commits, cur = [], None
for line in raw.splitlines():
    if line.startswith("C\t"):
        _, h, at, an, s = (line.split("\t", 4) + [""])[:5]
        cur = {"h": h, "t": int(at), "a": an, "s": s, "files": []}
        commits.append(cur)
    elif line.startswith(":"):
        meta, *paths = line.split("\t")
        f = meta.split()
        cur["files"].append((f[2], f[3], f[4], paths))

Z = "0" * 40
edge_cache = {}


def blob_edges(sha):
    if sha == Z:
        return set()
    if sha not in edge_cache:
        edge_cache[sha] = {canon(c) for c in edges(cat.get(sha)) if c.startswith("CLAIM-")}
    return edge_cache[sha]


revs, edge_ev = [], []
for i, c in enumerate(commits):
    nclaims = sum(1 for _, _, _, ps in c["files"] if ps[-1].startswith("record/claims.d/"))
    for old, new, st, paths in c["files"]:
        po, pn = paths[0], paths[-1]
        if not re.match(r"record/[a-z]+\.d/[A-Z]+-[A-Za-z0-9]+\.md$", pn):
            continue
        src = canon(os.path.basename(pn)[:-3])
        # edges
        eo, en = blob_edges(old), blob_edges(new)
        for tgt in en - eo:
            if tgt != src:
                edge_ev.append({"t": c["t"], "h": c["h"], "src": src, "tgt": tgt, "op": 1, "a": c["a"]})
        for tgt in eo - en:
            if tgt != src:
                edge_ev.append({"t": c["t"], "h": c["h"], "src": src, "tgt": tgt, "op": -1, "a": c["a"]})
        if pn.startswith("record/claims.d/"):
            to = None if old == Z else cat.get(old)
            tn = None if new == Z else cat.get(new)
            r = classify(to, tn, author=c["a"], message=c["s"], alias=canon)
            revs.append({"t": c["t"], "h": c["h"], "a": c["a"], "s": c["s"][:120],
                         "claim": src, "n_claims_in_commit": nclaims, **r})
    if i % 300 == 0:
        print(i, len(commits), file=sys.stderr)

json.dump(revs, open(os.path.join(OUT, "revisions.json"), "w"))
json.dump(edge_ev, open(os.path.join(OUT, "edges.json"), "w"))
json.dump(population, open(os.path.join(OUT, "population.json"), "w"))
print(len(commits), "commits;", len(revs), "claim-file changes;", len(edge_ev), "edge events")
