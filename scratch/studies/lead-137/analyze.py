"""Summarize results.jsonl for LEAD-137. python3 -I analyze.py"""
import json
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
rows = [json.loads(l) for l in open(os.path.join(HERE, "results.jsonl")) if l.strip()]


def agg(subset, field="overlap"):
    v = np.array([r[field] for r in subset])
    return v.mean(), v.std(), v.min(), v.max(), len(v)


def show(name, subset):
    m, s, lo, hi, n = agg(subset)
    cc = np.mean([r["coarse_corr"] for r in subset])
    ndr = np.median([r["near_decomp_ratio"] for r in subset])
    print(f"{name:42s} overlap mean={m:.3f} sd={s:.3f} "
          f"[{lo:.3f},{hi:.3f}] coarse_corr={cc:.3f} ndr~{ndr:.1f} n={n}")


print(f"total items: {len(rows)}")
print("\n== by border homogeneity (lattice-like vs generic) ==")
for hb in (True, False):
    show(f"homogeneous_border={hb}", [r for r in rows if r["homogeneous_border"] == hb])

print("\n== generic (non-lattice) border only, by mode ==")
gen = [r for r in rows if not r["homogeneous_border"]]
for mode in ("symmetric", "asymmetric"):
    show(f"mode={mode}", [r for r in gen if r["mode"] == mode])

print("\n== generic border, by rho ==")
for rho in (0.5, 0.8, 0.95):
    show(f"rho={rho}", [r for r in gen if r["rho"] == rho])

print("\n== generic border, by modularity (w_cross) ==")
for wc in (0.1, 0.5):
    tag = "strong-modular" if wc == 0.1 else "weak-modular"
    show(f"w_cross={wc} ({tag})", [r for r in gen if r["w_cross"] == wc])

print("\n== generic border, by buffer width ==")
for bw in (1, 2):
    show(f"buffer_width={bw}", [r for r in gen if r["buffer_width"] == bw])

print("\n== homogeneous (lattice-like) border, by mode ==")
hom = [r for r in rows if r["homogeneous_border"]]
for mode in ("symmetric", "asymmetric"):
    show(f"mode={mode}", [r for r in hom if r["mode"] == mode])

print("\n== 2-D subspace overlap (robustness), generic vs homogeneous ==")
for hb in (True, False):
    v = np.array([r["subspace2"] for r in rows if r["homogeneous_border"] == hb])
    print(f"homogeneous_border={hb}: subspace2 mean={v.mean():.3f} sd={v.std():.3f}")

# fraction of items that "coincide" at thresholds
print("\n== fraction with overlap above threshold ==")
for hb in (True, False):
    sub = [r for r in rows if r["homogeneous_border"] == hb]
    for th in (0.9, 0.7, 0.5):
        frac = np.mean([r["overlap"] > th for r in sub])
        print(f"  homogeneous_border={hb} overlap>{th}: {frac:.2f}")

# confirm R is a genuine gap-isolated block in the strongly-modular case
print("\n== near-decomposability of R (should be >1 to be a block) ==")
for wc in (0.1, 0.5):
    v = np.array([r["near_decomp_ratio"] for r in rows if r["w_cross"] == wc
                  and not r["homogeneous_border"]])
    print(f"  w_cross={wc}: ndr median={np.median(v):.2f} min={v.min():.2f}")
