"""Sensitivity sweep: rerun the ablation comparison at age 1000, full
visibility, under one-at-a-time changes of the parameters, appending one
JSON line per cell to sweep.jsonl (resumable).

Usage: OMP_NUM_THREADS=1 python3 -I sweep.py [N_RUNS]
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import resolve_model as m  # noqa: E402

AGE = 1000
OUT = os.path.join(HERE, "sweep.jsonl")
VARIANTS = {
    "base": {},
    "delta_0.3": {"DELTA": 0.3},
    "tau0_0.4": {"TAU0": 0.4},
    "sigma_1.5": {"SIGMA": 1.5},
    "kappa_3": {"KAPPA": 3.0},
    "eta_0.005": {"ETA": 0.005, "ETA_E": 0.005},
    "lam_imposed_0.8": {"LAM_IMPOSED": 0.8},
    "alpha_slow_0.002": {"ALPHA_SLOW": 0.002},
    "beta_4": {"BETA": 4.0, "BETA_I": 10.5},
}
DEFAULTS = {k: getattr(m, k) for v in VARIANTS.values() for k in v}


def main(n):
    done = set()
    if os.path.exists(OUT):
        with open(OUT) as f:
            done = {json.loads(line)["key"] for line in f}
    with open(OUT, "a") as f:
        for name, over in VARIANTS.items():
            for k, v in DEFAULTS.items():
                setattr(m, k, v)
            for k, v in over.items():
                setattr(m, k, v)
            yokes = {}
            for env in ("defeater", "irrelevant"):
                s = m.make_stream(env, AGE, "full", n, 159)
                for agent in m.AGENTS:
                    for cond in m.CONDITIONS:
                        key = f"{name}|{agent}|{cond}|{env}"
                        if key in done:
                            continue
                        yoke = None
                        if cond == "yoked":
                            if agent not in yokes:
                                ys = m.make_stream("neither", AGE, "full", n,
                                                   10159)
                                yokes[agent] = m.simulate(
                                    agent, "intact", ys, record_slow=True)
                            yoke = yokes[agent]
                        r = m.simulate(agent, cond, s, yoke=yoke,
                                       record_slow=True)
                        e = m.endpoints(r["choices"], r["c"], s)
                        e.update({"key": key, "variant": name,
                                  "agent": agent, "cond": cond, "env": env,
                                  "lam_onset": float(r["lam"][AGE].mean()),
                                  "a_onset": float(r["a"][AGE].mean())})
                        f.write(json.dumps(e) + "\n")
                        f.flush()


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 200)
