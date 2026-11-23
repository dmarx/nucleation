"""Run the crossed grid and append each probe's result to results/probes.jsonl.

python3 -I run_all.py           # calibrate (if needed), then the grid; resumes
Set OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 on a shared machine.
"""
import copy as _copy
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import crossed as c  # noqa: E402

RES = os.path.join(HERE, "results")
CAL = os.path.join(RES, "calibration.json")
OUT = os.path.join(RES, "probes.jsonl")

TRAINERS = ["heavy", "adam"]
PROBES = ["sgd", "heavy", "adam", "sign"]
SEEDS = list(range(12))
CAL_SEEDS = [100, 101, 102, 103]
TRAIN_STEPS = 3000
HEAL_STEPS = 1000
TARGET_TB = 40


def trained(seed, trainer):
    a, b, b2 = c.make_tasks(seed)
    X, ids = c.make_data(seed)
    y = c.targets(X, ids, a, b)
    yn = c.targets(X, ids, a, b2)
    p = c.init_params(seed)
    opt = c.Optimizer(trainer, c.TRAIN_LR[trainer])
    c.train(p, X, y, opt, TRAIN_STEPS)
    return p, opt, X, ids, y, yn


def calibrate():
    """Per (trainer, probe optimizer): the learning rate at which the intact
    network relearns B to 0.9 in TARGET_TB steps (median over CAL_SEEDS),
    by bisection in log learning rate. Pace is matched; path is not."""
    nets = {tr: [trained(s, tr) for s in CAL_SEEDS] for tr in TRAINERS}
    cal = {}
    for tr in TRAINERS:
        for po in PROBES:
            lo, hi = np.log(c.PROBE_LR[po] / 30), np.log(c.PROBE_LR[po] * 3)
            for _ in range(14):
                mid = 0.5 * (lo + hi)
                tbs = []
                for p, _, X, ids, _, yn in nets[tr]:
                    r = c.probe(p, X, ids, yn, c.Optimizer(po, float(np.exp(mid))))
                    tbs.append(r["tB"] if r["tB"] >= 0 else 10 ** 6)
                if np.median(tbs) > TARGET_TB:
                    lo = mid
                else:
                    hi = mid
            cal[f"{tr}/{po}"] = float(np.exp(0.5 * (lo + hi)))
    return cal


def states(seed, trainer):
    p, opt, X, ids, y, yn = trained(seed, trainer)
    rng = np.random.default_rng(1000 + seed)
    out = {"intact": p}
    out["permuted"] = c.permute_units(p, rng)[0]
    out["rescaled"] = c.rescale_units(p, rng)[0]
    sel = c.selectivity(p, X, ids)
    k = c.WIDTH // 4
    for name, units in [("ablate_selective", np.argsort(-sel)[:k]),
                        ("ablate_random", rng.choice(c.WIDTH, k, replace=False))]:
        q = c.ablate_units(p, units, rng)
        c.train(q, X, y, c.Optimizer(trainer, c.TRAIN_LR[trainer]), HEAL_STEPS)
        out[name] = q
    q = c.copy(p)
    c.train(q, X, y, c.Optimizer(trainer, c.TRAIN_LR[trainer], _copy.deepcopy(opt.state)),
            HEAL_STEPS)
    out["continued"] = q
    return out, opt, X, ids, y, yn


def done_keys():
    if not os.path.exists(OUT):
        return set()
    keys = set()
    with open(OUT) as f:
        for line in f:
            r = json.loads(line)
            keys.add((r["trainer"], r["seed"]))
    return keys


def main():
    os.makedirs(RES, exist_ok=True)
    if os.path.exists(CAL):
        cal = json.load(open(CAL))
    else:
        cal = calibrate()
        json.dump(cal, open(CAL, "w"), indent=1)
    print("calibration", cal, flush=True)
    done = done_keys()
    for tr in TRAINERS:
        for seed in SEEDS:
            if (tr, seed) in done:
                continue
            sts, opt, X, ids, y, yn = states(seed, tr)
            rows = []
            for sname, q in sts.items():
                lv = c.task_levels(q, X, ids, y)
                base = {"trainer": tr, "seed": seed, "state": sname,
                        "sA_train": float(lv[0]), "sB_train": float(lv[1]),
                        "seg": c.segregation(q, X, ids)}
                probes = [(po, c.Optimizer(po, cal[f"{tr}/{po}"])) for po in PROBES]
                if sname == "intact":
                    probes.append((tr + "_carried",
                                   c.Optimizer(tr, cal[f"{tr}/{tr}"], _copy.deepcopy(opt.state))))
                for pname, o in probes:
                    r = dict(base, probe=pname, lr=o.lr)
                    r.update(c.probe(q, X, ids, yn, o))
                    rows.append(r)
            with open(OUT, "a") as f:  # one (trainer, seed) block at a time
                for r in rows:
                    f.write(json.dumps(r) + "\n")
            print(tr, seed, "done", flush=True)


if __name__ == "__main__":
    main()
