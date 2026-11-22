"""Summarise the SGD sweep (results/sgd_*.jsonl): how often each initialisation
ends in, or ever reaches, the 6-gon, by n, batch size and learning rate.
Usage: python3 -I analyze_sgd.py results/sgd_*.jsonl"""
import json, sys
from collections import Counter, defaultdict

rows = []
for p in sys.argv[1:]:
    with open(p) as f:
        rows += [json.loads(l) for l in f]


def is6(lab):
    return lab.startswith("6")


def summary(rows, keys):
    g = defaultdict(list)
    for d in rows:
        g[tuple(d[k] for k in keys)].append(d)
    return g


print(f"{len(rows)} runs")
for ep in sorted({d['epochs'] for d in rows}):
    R = [d for d in rows if d["epochs"] == ep]
    print(f"\n=== epochs {ep}: final label counts by initialisation ===")
    for ini, ds in sorted(summary(R, ["init"]).items()):
        print(ini, dict(Counter(d["final"] for d in ds).most_common()))
    print(f"\n=== epochs {ep}: runs ending at a 6-gon (6, any +/-) / runs, non-6 initialisations ===")
    g = summary([d for d in R if d["init"] != "6gon"], ["n", "batch", "lr"])
    print("n     B    lr      4gon   5gon   prior  | ever-6 (any checkpoint)")
    for (n, B, lr), ds in sorted(g.items()):
        by = {i: [d for d in ds if d["init"] == i] for i in ("4gon", "5gon", "prior")}
        cell = "  ".join(f"{sum(is6(d['final']) for d in v)}/{len(v)}".rjust(5) for v in by.values())
        ever = sum(any(is6(l) for e, l in d["labels"].items() if e != "0") for d in ds)
        print(f"{n:<5} {B:<4} {lr:<7} {cell}  | {ever}/{len(ds)}")
    ctl = [d for d in R if d["init"] == "6gon"]
    if ctl:
        print(f"\n6-gon control: {sum(is6(d['final']) for d in ctl)}/{len(ctl)} end at a 6-gon;",
              dict(Counter(d["final"] for d in ctl)))
    # n either side of 600: totals
    print("\nby n (non-6 inits):")
    for n, ds in sorted(summary([d for d in R if d["init"] != "6gon"], ["n"]).items()):
        print(n, f"{sum(is6(d['final']) for d in ds)}/{len(ds)} end at 6;",
              dict(Counter(d['final'] for d in ds).most_common(6)))
    print("\nby init and lr, pooled over n and B (non-6 inits):")
    for k, ds in sorted(summary([d for d in R if d["init"] != "6gon"], ["init", "lr"]).items()):
        print(k, f"{sum(is6(d['final']) for d in ds)}/{len(ds)}")
    dv = [d for d in R if not d["alive"]]
    print("\ndiverged:", len(dv), dict(Counter((d["lr"], d["batch"]) for d in dv)))
