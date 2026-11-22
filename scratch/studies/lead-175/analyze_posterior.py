"""Posterior across n for LEAD-175: occupancy from the parallel-tempering run,
and region free energies from the restricted runs by thermodynamic integration,
anchored at the prior (n = 0). Writes results/posterior_summary.json and prints
a report.

Units. n here is the multiplier of the population loss L = E||x - f||^2 in the
exponent, p_n ∝ exp(-n L) N(0, I): the n of Chen et al.'s formula
f_α(n) = n L_α + λ_α log n + c_α (their App. F.1). Their likelihood (Eq. 3) has a
factor 1/2, so their NUTS posterior on n samples is p_{n/2} in these units.

Usage: python3 -I analyze_posterior.py
"""
import glob, json, os, sys
from math import log
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import tms
import ti

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results")
LCRIT = {k: float(tms.pop_loss(*v)) for k, v in tms.CRIT.items()}
# Chen et al.: Table 1 (theory) and Table K.1 (estimates), Table C.2 constants,
# as in scratch/formal/tms_critical_sizes_check.py
LAM_TH = {"5": 7.0, "5+": 8.5, "6": 8.5}
LAM_HAT = {"4++-": 4.097, "4+": 5.761, "4": 5.297, "5": 7.705, "5+": 9.906, "6": 9.027}
CC = {"6": 6.37767, "5": 3.62417, "5+": 3.62764, "4": 2.0, "4+": 2.00347, "4++-": 1.50694}
PAIRS = [("4++-", "4+"), ("4+", "5"), ("5", "5+"), ("5", "6"), ("5+", "6"), ("4+", "4++")]


def formula_ncr(a, b, lam):
    return ti.formula_ncr(LCRIT[b] - LCRIT[a], lam[b] - lam[a], CC[b] - CC[a])


crossing = ti.crossing


def load(p):
    with open(p) as f:
        return [json.loads(l) for l in f]


out = {}
# ------------------------------------------------------------ unrestricted PT
pt = [b for b in load(os.path.join(RES, "posterior_pt.jsonl")) if not b["burn"]]
lad = np.array(pt[0]["ladder"])
labels = sorted({k for b in pt for c in b["counts"] for k in c})
cnt = np.zeros((len(pt), len(lad), len(labels)))
for bi, b in enumerate(pt):
    for r, c in enumerate(b["counts"]):
        for k, v in c.items():
            cnt[bi, r, labels.index(k)] = v
tot = cnt.sum((0, 2))
frac = cnt.sum(0) / tot[:, None]
blockfrac = cnt / cnt.sum(2, keepdims=True)
se = blockfrac.std(0, ddof=1) / np.sqrt(len(pt))   # blocks as batch means
print(f"PT: {len(pt)} post-burn blocks x {pt[0]['iters']} iters x {pt[0]['chains']} chains; "
      f"swap acceptance min {min(min(b['swap']) for b in pt):.2f}")
main = [l for l in labels if frac[:, labels.index(l)].max() > 0.02]
print("n       " + "".join(f"{l:>8}" for l in main))
for r in range(0, len(lad), 2):
    print(f"{lad[r]:<8.0f}" + "".join(f"{frac[r, labels.index(l)]:8.3f}" for l in main))
out["pt"] = {"ladder": lad.tolist(), "labels": labels, "frac": frac.round(5).tolist(),
             "se": se.round(5).tolist(), "samples_per_rung": tot.tolist()}
pt_cross = {}
for a, b in PAIRS:
    if a in labels and b in labels:
        ca, cb = cnt.sum(0)[:, labels.index(a)], cnt.sum(0)[:, labels.index(b)]
        ok = (ca >= 20) & (cb >= 20)
        y = np.where(ok, np.log(np.maximum(cb, 1) / np.maximum(ca, 1)), np.nan)
        pt_cross[f"{a}->{b}"] = crossing(lad, y)
print("PT occupancy crossings (both regions >= 20 samples):", pt_cross)
out["pt_crossings"] = pt_cross

# ------------------------------------------------------------ prior anchor
pr = load(os.path.join(RES, "prior_regions.jsonl"))
N0 = sum(r["size"] for r in pr)
P0, EL0 = {}, {}
for r in pr:
    for k, v in r["count"].items():
        P0[k] = P0.get(k, 0) + v; EL0[k] = EL0.get(k, 0.0) + r["sumL"][k]
EL0 = {k: EL0[k] / P0[k] for k in P0}
P0 = {k: P0[k] / N0 for k in P0}

# ------------------------------------------------------------ restricted TI
logZ, lam_loc, ladR = {}, {}, None
for p in sorted(glob.glob(os.path.join(RES, "restricted_*.jsonl"))):
    B = [b for b in load(p) if not b["burn"]]
    if not B:
        continue
    reg = B[0]["region"]
    ladR = np.array(B[0]["ladder"])
    EL = np.mean([b["meanL"] for b in B], 0)
    ELse = np.std([b["meanL"] for b in B], 0, ddof=1) / np.sqrt(len(B)) if len(B) > 1 else np.zeros_like(EL)
    logZ[reg] = ti.ti_logZ(ladR, EL, EL0[reg], P0[reg])
    lam_loc[reg] = (ladR * (EL - LCRIT[reg])).tolist()
    out.setdefault("restricted", {})[reg] = {"blocks": len(B), "meanL": EL.tolist(), "meanL_se": ELse.tolist(),
                                            "logZ": logZ[reg].tolist(), "prior_mass": P0[reg],
                                            "acc_min": min(min(b["acc"]) for b in B)}
if logZ:
    out["restricted_ladder"] = ladR.tolist()
    print("\nRestricted runs: regions", sorted(logZ))
    print("local learning coefficient n(E[L]-L_crit) at n = 1000, 3000, 10000:")
    for reg in sorted(logZ):
        vals = [np.interp(np.log(x), np.log(ladR), lam_loc[reg]) for x in (1000, 3000, 10000)]
        print(f"  {reg:5} " + "  ".join(f"{v:6.2f}" for v in vals),
              f"(Chen: theory {LAM_TH.get(reg, '-')}, estimate {LAM_HAT.get(reg, '-')})")
    ti_cross = {}
    for a, b in PAIRS:
        if a in logZ and b in logZ:
            ti_cross[f"{a}->{b}"] = crossing(ladR, logZ[b] - logZ[a])
    out["ti_crossings"] = ti_cross
    # validation: TI log odds against PT log odds where both measured
    val = []
    for a, b in PAIRS:
        if a in logZ and b in logZ and a in labels and b in labels:
            ca, cb = cnt.sum(0)[:, labels.index(a)], cnt.sum(0)[:, labels.index(b)]
            for r in range(len(lad)):
                if ca[r] >= 50 and cb[r] >= 50:
                    tiv = np.interp(np.log(lad[r]), np.log(ladR), logZ[b] - logZ[a])
                    val.append((f"{a}->{b}", round(float(lad[r]), 1), round(float(np.log(cb[r] / ca[r])), 3), round(float(tiv), 3)))
    out["ti_vs_pt"] = val
    if val:
        d = np.array([v[2] - v[3] for v in val])
        print(f"\nTI vs PT log-odds, {len(val)} (pair, n) points: mean diff {d.mean():+.3f}, rms {np.sqrt((d**2).mean()):.3f}")
    print("\nCritical n (units of the formula, p ∝ exp(-nL)):")
    print(f"{'pair':10}{'formula λ̂':>14}{'formula theory λ':>18}{'PT':>9}{'TI':>9}")
    for a, b in PAIRS:
        k = f"{a}->{b}"
        lamth = dict(LAM_HAT); lamth.update(LAM_TH)
        fh = formula_ncr(a, b, LAM_HAT) if a in LAM_HAT and b in LAM_HAT else None
        ft = formula_ncr(a, b, lamth) if a in lamth and b in lamth and a in CC and b in CC else None
        print(f"{k:10}{str(fh):>14}{str(ft):>18}{str(round(pt_cross[k]) if pt_cross.get(k) else None):>9}"
              f"{str(round(ti_cross[k]) if ti_cross.get(k) else None):>9}")
        out.setdefault("table", {})[k] = {"formula_lam_hat": fh, "formula_lam_theory": ft,
                                          "pt": pt_cross.get(k), "ti": ti_cross.get(k)}
    # which region dominates the posterior among those integrated, by n
    regs = sorted(logZ)
    M = np.array([logZ[r] for r in regs])
    dom = [regs[i] for i in M.argmax(0)]
    seq = [(round(float(ladR[0]), 1), dom[0])]
    for i in range(1, len(dom)):
        if dom[i] != dom[i - 1]:
            seq.append((round(float(ladR[i]), 1), dom[i]))
    print("\nDominant region among those integrated, from n =", seq)
    out["ti_dominant_sequence"] = seq
with open(os.path.join(RES, "posterior_summary.json"), "w") as f:
    json.dump(out, f, indent=1)
