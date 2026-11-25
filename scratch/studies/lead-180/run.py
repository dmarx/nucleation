"""LEAD-180 experiments. `python3 -I run.py [e1 e2 ...]`; writes results/<name>.json
and results/tables.md (rebuilt from whatever JSON exists)."""
from __future__ import annotations

import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import model as M  # noqa: E402

RES = os.path.join(HERE, "results")
SEEDS = range(30)
KEYS = ("MC_M", "MC_m", "AS", "dshare", "evals_per_round")


def summarize(outs, keys=KEYS):
    s = {}
    for k in keys:
        x = np.array([o[k] for o in outs], dtype=float)
        x = x[np.isfinite(x)]
        s[k] = [round(float(x.mean()), 4) if len(x) else None,
                round(float(1.96 * x.std(ddof=1) / np.sqrt(len(x))), 4) if len(x) > 1 else None]
    return s


def cell(arch, seeds=SEEDS, **kw):
    P = M.default_params(**kw)
    return [M.run(arch, P, s) for s in seeds]


def e1():
    """Four architectures (+ the oracle) x attack class x compromised evaluators."""
    rows = []
    for attack in ("none", "overt", "mimic"):
        for n_comp in (0, 2):
            for arch in M.ARCHS:
                rows.append(dict(arch=arch, attack=attack, n_comp=n_comp,
                                 **summarize(cell(arch, attack=attack, n_comp=n_comp))))
    return rows


def e2():
    """Role-limited audit: one central evaluator against a distributed pool,
    by number of compromised evaluators, panel size and quorum."""
    rows = []
    for attack in ("overt", "mimic"):
        for n_comp in (0, 1):
            rows.append(dict(arch="role", config="central", attack=attack, n_comp=n_comp,
                             k_p=1, q=1.0,
                             **summarize(cell("role", attack=attack, n_comp=n_comp, central=True))))
        for arch in ("role", "adaptive"):
            for k_p in (3, 7):
                for q in (0.5, 2 / 3):
                    for n_comp in (0, 1, 2, 3):
                        rows.append(dict(arch=arch, config="pool of 7", attack=attack,
                                         n_comp=n_comp, k_p=k_p, q=round(q, 3),
                                         **summarize(cell(arch, attack=attack, n_comp=n_comp,
                                                          k_p=k_p, q=q))))
    return rows


def e3():
    """Coverage of the minority block by independent evidence, under the mimic
    attack; and the relabelling check (dissenters' and mimics' targets swapped,
    b_A = 1, no farming): attack success in the two worlds sums to 1 when no
    one holds evidence on m."""
    rows = []
    archs = [a for a in M.ARCHS if a != "oracle"]
    for n_Em in (0, 1, 2, 3):
        for arch in archs:
            rows.append(dict(part="coverage", arch=arch, n_Em=n_Em,
                             **summarize(cell(arch, attack="mimic", n_Em=n_Em,
                                              monitor_covers_m=n_Em > 0))))
    for n_Em in (0, 2):
        for arch in archs:
            kw = dict(attack="mimic", b_A=1.0, t_farm=0, n_Em=n_Em, monitor_covers_m=n_Em > 0)
            a = cell(arch, **kw)
            b = cell(arch, swap_targets=True, **kw)
            sums = np.array([x["AS"] + y["AS"] for x, y in zip(a, b)])
            rows.append(dict(part="relabelling", arch=arch, n_Em=n_Em,
                             AS_world=summarize(a)["AS"], AS_relabelled=summarize(b)["AS"],
                             AS_sum=[round(float(sums.mean()), 4),
                                     round(float(1.96 * sums.std(ddof=1) / np.sqrt(len(sums))), 4)]))
    return rows


def onset_recovery(traj_AS, t0, thr=0.1, hold=20):
    """Rounds after t0 until AS stays below thr for `hold` rounds; None if never."""
    x = traj_AS[t0:]
    below = x < thr
    for i in range(len(x) - hold + 1):
        if below[i:i + hold].all():
            return i
    return None


def e4():
    """Repair after failure: adaptive against role-limited, honest or compromised
    monitor, with and without compromised evaluators in the pool."""
    rows = []
    for attack in ("overt", "mimic"):
        for n_comp in (0, 2):
            for arch, mon in (("role", False), ("adaptive", False), ("adaptive", True)):
                outs = cell(arch, attack=attack, n_comp=n_comp, monitor_comp=mon)
                P = M.default_params()
                rec = [onset_recovery(o["traj"]["AS"], P["t_farm"]) for o in outs]
                peak = [float(o["traj"]["AS"][P["t_farm"]:].max()) for o in outs]
                susp = np.zeros((len(outs), 3))
                for j, o in enumerate(outs):
                    seen = set()
                    for _, i, ty in o["susp"]:
                        if i not in seen:
                            seen.add(i)
                            susp[j, ty] += 1
                n = np.array([P["n_C"], P["n_D"], P["n_A"]])
                rows.append(dict(arch=arch, monitor_compromised=mon, attack=attack,
                                 n_comp=n_comp, **summarize(outs),
                                 peak_AS=round(float(np.mean(peak)), 4),
                                 recovered_share=round(float(np.mean([r is not None for r in rec])), 4),
                                 median_rounds_to_recover=(float(np.median([r for r in rec if r is not None]))
                                                           if any(r is not None for r in rec) else None),
                                 ever_suspended_share=dict(zip(("C", "D", "A"),
                                                               [round(float(v), 4) for v in susp.mean(0) / n]))))
    return rows


def e5():
    """Farming: adversaries that act cooperatively for 100 rounds before
    attacking, against ones that attack from the start (overt attack)."""
    rows = []
    for arch in ("unrestricted", "rel-agree", "rel-val", "role", "adaptive"):
        for t_farm in (0, 100):
            rows.append(dict(arch=arch, t_farm=t_farm,
                             **summarize(cell(arch, attack="overt", t_farm=t_farm))))
    return rows


EXPS = dict(e1=e1, e2=e2, e3=e3, e4=e4, e5=e5)


def fmt(v):
    if isinstance(v, list) and len(v) == 2:
        return "—" if v[0] is None else f"{v[0]:.3f} ± {v[1]:.3f}" if v[1] is not None else f"{v[0]:.3f}"
    if isinstance(v, float):
        return f"{v:.3f}"
    if isinstance(v, dict):
        return ", ".join(f"{k} {x:.2f}" for k, x in v.items())
    return "—" if v is None else str(v)


def tables():
    out = ["# LEAD-180 results", "",
           "Means over 30 seeds ± 95% half-width (1.96 s / sqrt n). MC_M, MC_m:"
           " main and minority capability (1 = learned, 0 = initial). AS: attack"
           " success (share of the attacker's displacement achieved). dshare:"
           " dissenters' influence on the m block over their head-count share"
           " (1 parity, 0 suppressed). Generated by run.py.", ""]
    for name in EXPS:
        f = os.path.join(RES, f"{name}.json")
        if not os.path.exists(f):
            continue
        rows = json.load(open(f))
        out += [f"## {name}: {EXPS[name].__doc__.split(chr(10))[0]}", ""]
        cols = list(rows[0].keys())
        for r in rows:
            for c in r:
                if c not in cols:
                    cols.append(c)
        out.append("| " + " | ".join(cols) + " |")
        out.append("|" + "---|" * len(cols))
        for r in rows:
            out.append("| " + " | ".join(fmt(r.get(c)) for c in cols) + " |")
        out.append("")
    open(os.path.join(RES, "tables.md"), "w").write("\n".join(out))


if __name__ == "__main__":
    os.makedirs(RES, exist_ok=True)
    names = sys.argv[1:] or list(EXPS)
    for n in names:
        t = time.time()
        rows = EXPS[n]()
        json.dump(rows, open(os.path.join(RES, f"{n}.json"), "w"), indent=1)
        print(n, f"{time.time() - t:.0f}s", flush=True)
    tables()
