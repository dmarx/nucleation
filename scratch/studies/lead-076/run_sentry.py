"""Run CASE-153's sentry design (LEAD-076). Writes results/*.jsonl, one line
per condition as it finishes; reruns skip conditions already written.

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -I run_sentry.py
"""
from __future__ import annotations

import json
import os
import sys
from dataclasses import asdict, replace

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sentry import Params, Condition, draws, simulate, measures, summarize  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results")
N = 1000
SEED = 20261122


def done_keys(path):
    if not os.path.exists(path):
        return set()
    with open(path) as f:
        return {json.loads(line)["key"] for line in f if line.strip()}


def append(path, row):
    with open(path, "a") as f:
        f.write(json.dumps(row) + "\n")


def boot_ci(x, n_boot=2000, seed=0):
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(x), (n_boot, len(x)))
    m = x[idx].mean(axis=1)
    return float(x.mean()), float(np.quantile(m, 0.025)), float(np.quantile(m, 0.975))


def first_experiment(p, U):
    path = os.path.join(RES, "first_experiment.jsonl")
    have = done_keys(path)
    conds = {
        "bayesian": Condition(model="bayes"),
        "bayesian, inspection cost 0.3": Condition(model="bayes", c_override=0.3),
        "habit": Condition(model="habit"),
        "governance": Condition(),
        "independent audit": Condition(correction="audit"),
        "protected investigator": Condition(correction="protected"),
        "habit, protected investigator": Condition(model="habit", correction="protected"),
        "bayesian, inspection cost 0.3, protected investigator": Condition(model="bayes", c_override=0.3, correction="protected"),
    }
    for k, c in conds.items():
        if k in have:
            continue
        s = summarize(measures(p, simulate(p, c, U)))
        append(path, {"key": k, "condition": asdict(c), **s})


def factorial(p, U):
    path = os.path.join(RES, "factorial.jsonl")
    have = done_keys(path)
    per_seed = {}
    for fb in ("independent", "success", "fixed"):
        for rs in (False, True):
            for cr in ("ordinary", "audit", "protected"):
                key = f"{fb}|{'restricted' if rs else 'independent-evidence'}|{cr}"
                c = Condition(feedback=fb, restrict=rs, correction=cr)
                m = measures(p, simulate(p, c, U))
                per_seed[key] = m
                if key not in have:
                    append(path, {"key": key, "condition": asdict(c), **summarize(m)})
    for rs in (False, True):
        for cr in ("ordinary", "protected"):
            key = f"habit|{'restricted' if rs else 'independent-evidence'}|{cr}"
            c = Condition(model="habit", restrict=rs, correction=cr)
            m = measures(p, simulate(p, c, U))
            per_seed[key] = m
            if key not in have:
                append(path, {"key": key, "condition": asdict(c), **summarize(m)})
    # interaction contrasts on needless protection cost, paired over seeds
    ipath = os.path.join(RES, "interactions.jsonl")
    ihave = done_keys(ipath)
    for cr in ("ordinary", "audit", "protected"):
        for meas in ("needless_cost", "exit"):
            key = f"{meas}|{cr}"
            if key in ihave:
                continue
            def v(fb, rs):
                return per_seed[f"{fb}|{rs}|{cr}"][meas].astype(float)
            restr_eff_success = v("success", "restricted") - v("success", "independent-evidence")
            restr_eff_indep = v("independent", "restricted") - v("independent", "independent-evidence")
            inter = restr_eff_success - restr_eff_indep
            append(ipath, {"key": key,
                           "restriction_effect_under_success": boot_ci(restr_eff_success),
                           "restriction_effect_under_independent": boot_ci(restr_eff_indep),
                           "interaction": boot_ci(inter)})
    # does correction remove the persistence of success x restricted?
    for cr in ("audit", "protected"):
        key = f"correction_effect|{cr}"
        if key in ihave:
            continue
        a = per_seed["success|restricted|ordinary"]["needless_cost"].astype(float)
        b = per_seed[f"success|restricted|{cr}"]["needless_cost"].astype(float)
        append(ipath, {"key": key, "reduction_in_needless_cost": boot_ci(a - b)})


def interventions(p, U):
    path = os.path.join(RES, "interventions.jsonl")
    have = done_keys(path)
    t_int = p.T1 + 50
    models = {
        "governance": dict(model="governance"),
        "habit": dict(model="habit"),
        "bayesian": dict(model="bayes"),
        "bayesian, inspection cost 0.3": dict(model="bayes", c_override=0.3),
    }
    for mname, kw in models.items():
        for iv in (None, "belief", "authority", "evidence", "reinforcement"):
            if mname != "governance" and iv == "reinforcement":
                continue
            if mname.startswith("bayesian") and iv == "authority":
                continue
            key = f"{mname}|{iv or 'none'}"
            if key in have:
                continue
            c = Condition(intervention=iv, t_int=t_int, **kw)
            rec = simulate(p, c, U)
            m = measures(p, rec, t_from=t_int)
            s = summarize(m)
            # belief right after the intervention and 30 steps on
            s["b_after_30"] = float(rec["b"][:, t_int + 30].mean())
            s["pp_after_30"] = float(rec["pp"][:, t_int + 30].mean())
            append(path, {"key": key, "condition": asdict(c), **s})


def phase_diagram(p, U):
    path = os.path.join(RES, "phase_diagram.jsonl")
    have = done_keys(path)
    cells = {
        "success|restricted|ordinary": Condition(),
        "success|independent-evidence|ordinary": Condition(restrict=False),
        "success|restricted|protected": Condition(correction="protected"),
        "success|restricted|audit": Condition(correction="audit"),
        "independent|restricted|ordinary": Condition(feedback="independent"),
    }
    for cell, c in cells.items():
        for kappa in np.round(np.arange(0, 3.01, 0.25), 2):
            for eta in (0.005, 0.01, 0.02, 0.05, 0.1):
                key = f"{cell}|kappa={kappa}|eta={eta}"
                if key in have:
                    continue
                pk = replace(p, kappa=float(kappa), eta=float(eta))
                m = measures(pk, simulate(pk, c, U))
                s = summarize(m)
                append(path, {"key": key, "cell": cell, "kappa": float(kappa), "eta": eta, **s})


def main():
    os.makedirs(RES, exist_ok=True)
    p = Params()
    with open(os.path.join(RES, "params.json"), "w") as f:
        json.dump({"params": asdict(p), "N": N, "seed": SEED}, f, indent=1)
    U = draws(p, N, SEED)
    which = sys.argv[1:] or ["first", "factorial", "interventions", "phase"]
    if "first" in which:
        first_experiment(p, U)
    if "factorial" in which:
        factorial(p, U)
    if "interventions" in which:
        interventions(p, U)
    if "phase" in which:
        phase_diagram(p, U)


if __name__ == "__main__":
    main()
