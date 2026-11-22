"""LEAD-173: the leave-one-out and pairwise tables for the five conditions.

Run:  cd scratch/studies/lead-173 && python3 -I run.py
Writes results.json and results.md here. Takes well under a minute.
"""
from __future__ import annotations

import itertools
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np

from fivecond import Model, config
from witnesses import var1_witnesses, var2_witnesses, leaky_witnesses, pad

CONDS = "PDMAC"
H, B, EPS_ALT = 2, 2, 0.01


def forbidden(cfg, var, eps):
    """The proved entailments. cfg is a dict of booleans over PDMAC.
    E1 (VAR(1), Sigma > 0 only): D => M            (CLAIM-389).
    E2 (any eps >= 0, any h, any stationary Gaussian process): P & D & M => A.
    E3 (eps = 0, horizon set containing k = 1): A => P."""
    if var == 1 and cfg["D"] and not cfg["M"]:
        return "E1"
    if cfg["P"] and cfg["D"] and cfg["M"] and not cfg["A"]:
        return "E2"
    if eps == 0 and cfg["A"] and not cfg["P"]:
        return "E3"
    return None


def all_configs():
    for bits in itertools.product([1, 0], repeat=5):
        yield dict(zip(CONDS, map(bool, bits)))


def allowed_configs(var, eps):
    return [c for c in all_configs() if forbidden(c, var, eps) is None]


def key(c):
    return "".join("1" if c[x] else "0" for x in CONDS)


def random_model(rng, p=1, n=None, m=None):
    """Sparse random VAR(p) with diagonal noise; Y the first m coordinates,
    Z a coordinate outside Y."""
    n = n or int(rng.integers(2, 5))
    m = m or int(rng.integers(1, min(2, n - 1) + 1))
    while True:
        A_list = []
        for lag in range(p):
            mask = rng.random((n, n)) < (0.5 if lag == 0 else 0.3)
            vals = rng.choice([-1, 1], (n, n)) * rng.uniform(0.2, 0.6, (n, n))
            A_list.append(mask * vals)
        Sigma = np.diag(rng.uniform(0.5, 1.5, n))
        L = np.eye(n)[:m]
        G = np.eye(n)[[int(rng.integers(m, n))]]
        try:
            return Model(A_list, Sigma, L, G)
        except ValueError:
            continue


def witness_table():
    rows = []
    groups = [("VAR(1)", 1, 0.0, var1_witnesses()),
              ("VAR(2)", 2, 0.0, var2_witnesses()),
              ("VAR(1)/VAR(2), eps = 0.01", None, EPS_ALT, leaky_witnesses())]
    for label, var, eps, W in groups:
        for k, mdl in W.items():
            for padded in (False, True):
                mm = pad(mdl, 3 - mdl.m) if padded else mdl
                d = mm.evaluate(h=H, eps=eps, b=B)
                rows.append(dict(group=label, class_p=mm.p, eps=eps, name=mm.name,
                                 config=config(d["holds"]),
                                 defects={c: float(d[c]) for c in "PDMA"}, m=mm.m))
    return rows


def realized(rows, var, eps):
    out = set()
    for r in rows:
        if r["class_p"] > var:
            continue
        # a witness built for eps = 0 is valid at eps > 0 iff its A defect
        # is 0 or above eps; re-evaluate the A bit at this eps
        bits = list(r["config"])
        a = r["defects"]["A"]
        bits[3] = "1" if a <= eps + 1e-9 else "0"
        if r["eps"] > 0 and eps == 0:
            continue  # leaky witnesses are built for eps > 0
        out.add("".join(bits))
    return out


def pairwise(allowed):
    """X => Y iff no allowed configuration has X true and Y false."""
    M = {}
    for x in CONDS:
        for y in CONDS:
            if x != y:
                M[x + y] = not any(c[x] and not c[y] for c in allowed)
    return M


def leave_one_out(allowed_keys):
    out = {}
    for i, x in enumerate(CONDS):
        k = "".join("0" if j == i else "1" for j in range(5))
        out[x] = k in allowed_keys
    return out


def falsify(rng, N, p):
    hits = {}
    border = 0
    for _ in range(N):
        mdl = random_model(rng, p=p)
        for eps in (0.0, EPS_ALT):
            d = mdl.evaluate(h=H, eps=eps, b=B)
            for c in "PDM":
                if 1e-9 < d[c] < 1e-6:
                    border += 1
            f = forbidden(d["holds"], p, eps)
            k = (eps, config(d["holds"]))
            hits[k] = hits.get(k, 0) + 1
            if f is not None:
                raise AssertionError(f"forbidden {f} realized: {k}")
    return hits, border


def main():
    rows = witness_table()
    res = dict(regime=dict(target="Z_{t+1} = G X_{t+1}, external to Y", projection="Mori, onto span(Y_t)",
                           metric="relative excess MSE over E[Z_{t+k} | full past]", horizon=H,
                           eps=[0.0, EPS_ALT], budget=f"dim Y <= {B}"),
               witnesses=rows, regimes={})
    for var in (1, 2):
        for eps in (0.0, EPS_ALT):
            allowed = allowed_configs(var, eps)
            ak = {key(c) for c in allowed}
            rz = realized(rows, var, eps)
            missing = sorted(ak - rz)
            extra = sorted(rz - ak)
            assert not extra, (var, eps, extra)
            res["regimes"][f"VAR({var}), eps={eps}"] = dict(
                allowed=sorted(ak), n_allowed=len(ak), unwitnessed=missing,
                pairwise=pairwise(allowed), leave_one_out=leave_one_out(ak))
    rng = np.random.default_rng(173)
    fal = {}
    for p in (1, 2):
        hits, border = falsify(rng, 3000, p)
        fal[f"VAR({p})"] = dict(N=3000, borderline=border,
                                configs={f"eps={e} {c}": n for (e, c), n in sorted(hits.items())})
    res["falsification"] = fal
    with open("results.json", "w") as f:
        json.dump(res, f, indent=1)
    write_md(res)
    print(json.dumps({k: dict(n_allowed=v["n_allowed"], unwitnessed=v["unwitnessed"],
                              loo=v["leave_one_out"]) for k, v in res["regimes"].items()}, indent=1))
    print(json.dumps({k: (v["borderline"], len(v["configs"])) for k, v in fal.items()}))


def write_md(res):
    L = ["# LEAD-173 results (generated by run.py)", ""]
    L.append("## Witnesses (exact covariances; h = 2, b = 2)")
    L.append("")
    L.append("| class | eps | config PDMAC | P | D (nats) | M | A | m | construction |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    for r in res["witnesses"]:
        d = r["defects"]
        L.append(f"| VAR({r['class_p']}) | {r['eps']} | {r['config']} | {d['P']:.4f} | {d['D']:.4f} | "
                 f"{d['M']:.4f} | {d['A']:.4f} | {r['m']} | {r['name']} |")
    for name, v in res["regimes"].items():
        L += ["", f"## {name}", "", f"Allowed configurations: {v['n_allowed']} of 32; "
              f"unwitnessed: {v['unwitnessed'] or 'none'}.", "",
              "Leave-one-out (other four hold, this one fails): " +
              ", ".join(f"{x} {'realizable' if ok else 'impossible'}" for x, ok in v["leave_one_out"].items()),
              "", "Pairwise implications X => Y (row X, column Y):", "",
              "| | " + " | ".join(CONDS) + " |", "|---" * 6 + "|"]
        for x in CONDS:
            L.append(f"| {x} | " + " | ".join("-" if x == y else ("yes" if v["pairwise"][x + y] else "no")
                                               for y in CONDS) + " |")
    L += ["", "## Falsification on random sparse models", ""]
    for k, v in res["falsification"].items():
        L.append(f"- {k}: {v['N']} models, no forbidden configuration; borderline defects "
                 f"(1e-9 to 1e-6): {v['borderline']}; configurations hit: {len(v['configs'])}")
    with open("results.md", "w") as f:
        f.write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
