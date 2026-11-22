"""LEAD-017 study driver. Writes results/results.jsonl, one line per item
as it finishes; reruns skip items already written. Then summarize.py.

Rerun: OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I study.py
"""
import json
import sys
from dataclasses import asdict, replace
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from measures import (DEVAL_START, _ftest, authority_interventional,  # noqa: E402
                      behaviour_features, lda_cv_accuracy,
                      registration_interventional, registration_passive)
from orgmodel import DEVAL_END, World, calibrate_b, simulate  # noqa: E402

OUT = HERE / "results" / "results.jsonl"
N = 200
TARGET = 0.6

MAIN = {
    "denied": (World("denied", auth="none"), True),
    "unregistered": (World("unregistered", g_range=(0, 0), auth="tolerance"), False),
    "accommodation": (World("accommodation", auth="tolerance", tol_mode="compensation"), True),
}
HELD_OUT = {
    "decoy_interoceptive": (World("decoy_interoceptive", g_range=(0, 0), auth="tolerance",
                                  decoy_intero=True), False),
    "direct_authority": (World("direct_authority", g_range=(0, 0), auth="direct"), False),
    "weak_registration": (World("weak_registration", g_range=(0.1, 0.25), auth="none"), True),
    "habit_persistence": (World("habit_persistence", auth="none", drive=0.0, habit_w=3.0), True),
}


def done_items():
    if not OUT.exists():
        return {}
    return {json.loads(line)["item"]: json.loads(line) for line in OUT.read_text().splitlines()}


def write(rec):
    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("a") as f:
        f.write(json.dumps(rec) + "\n")


def naive_registration(obs):
    """Decoding the assay from the record with no covariates: what a measure
    that ignores other routes into the record would say."""
    n = obs.pursued.shape[0]
    out = np.empty(n)
    for i in range(n):
        sl = slice(DEVAL_START, None)
        m = obs.delta[i, sl] == 0
        y = obs.assay[i, sl][m]
        out[i] = _ftest(y, np.ones((len(y), 1)), obs.record[i, sl][m])
    return out


def score_world(name, world, registered, seed, split):
    obs, lat = simulate(world, N, seed)
    return {
        "item": f"{split}:{name}", "world": name, "split": split, "seed": seed,
        "registered_truth": registered, "b": world.b,
        "pursuit_post": float(obs.pursued[:, DEVAL_END:].mean()),
        "pursuit_during": float(obs.pursued[:, DEVAL_START:DEVAL_END].mean()),
        "reg_int": registration_interventional(obs).tolist(),
        "reg_pas": registration_passive(obs).tolist(),
        "reg_int_report": registration_interventional(obs, "report").tolist(),
        "reg_naive": naive_registration(obs).tolist(),
        "auth": authority_interventional(obs).tolist(),
        "g": lat.g.tolist(),
    }


def main():
    done = done_items()
    worlds = {}
    for name, (w, reg) in {**MAIN, **HELD_OUT}.items():
        key = f"calib_b:{name}"
        if key in done:
            b = done[key]["b"]
        else:
            b = calibrate_b(w, TARGET, n=400, iters=18)
            write({"item": key, "b": b, "world": asdict(replace(w, b=b))})
        worlds[name] = (replace(w, b=b), reg)
        print(name, "b =", round(b, 3), flush=True)

    for split, seed, names in [("calibration", 10, MAIN), ("test", 20, MAIN),
                               ("held_out", 30, HELD_OUT)]:
        for name in names:
            key = f"{split}:{name}"
            if key in done:
                continue
            w, reg = worlds[name]
            write(score_world(name, w, reg, seed, split))
            print("scored", key, flush=True)

    # behaviour: can pursuit (and its coupling to the assay) tell the three
    # main organizations apart, without the record or the probes?
    key = "behaviour:main"
    if key not in done:
        rec = {"item": key}
        for probes in (False, True):
            X, Xa, y, rates = [], [], [], {}
            for k, name in enumerate(MAIN):
                obs, _ = simulate(worlds[name][0], N, 40, with_probes=probes)
                X.append(behaviour_features(obs, with_assay=False))
                Xa.append(behaviour_features(obs, with_assay=True))
                y.append(np.full(N, k))
                rates[name] = [float(obs.pursued[:, DEVAL_START:DEVAL_END].mean()),
                               float(obs.pursued[:, DEVAL_END:].mean())]
            X, Xa, y = np.vstack(X), np.vstack(Xa), np.concatenate(y)
            tag = "probes" if probes else "no_probes"
            rec[tag] = {"rates_during_post": rates,
                        "lda3_behaviour": lda_cv_accuracy(X, y),
                        "lda3_behaviour_assay": lda_cv_accuracy(Xa, y)}
        write(rec)
        print("scored", key, flush=True)


if __name__ == "__main__":
    main()
