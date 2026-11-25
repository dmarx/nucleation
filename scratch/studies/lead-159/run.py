"""Run every cell of LEAD-159's design and append one JSON line per cell to
results.jsonl, skipping cells already written (resumable).

Usage: OMP_NUM_THREADS=1 python3 -I run.py [N_RUNS]
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import resolve_model as m  # noqa: E402

AGES = (250, 1000, 4000)
SEED = 159          # observation streams of the cells
YOKE_SEED = 10159   # independent streams whose slow trajectories are yoked
OUT = os.path.join(HERE, "results.jsonl")


def cells():
    # the ablation comparisons, at full visibility, where the observation
    # stream is identical for intact and ablated runs
    for age in AGES:
        for env in m.ENVS:
            for agent in m.AGENTS:
                for cond in m.CONDITIONS:
                    yield (agent, cond, env, age, "full")
    # the visibility factor, intact agents only
    for age in AGES:
        for env in m.ENVS:
            for agent in m.AGENTS:
                for vis in ("partial", "routed"):
                    yield (agent, "intact", env, age, vis)


def key(c):
    return "|".join(map(str, c))


def main(n):
    done = set()
    if os.path.exists(OUT):
        with open(OUT) as f:
            for line in f:
                done.add(json.loads(line)["key"])
    streams, yokes = {}, {}
    with open(OUT, "a") as f:
        for c in cells():
            k = key(c)
            if k in done:
                continue
            agent, cond, env, age, vis = c
            sk = (env, age, vis)
            if sk not in streams:
                streams.clear()
                streams[sk] = m.make_stream(env, age, vis, n, SEED)
            s = streams[sk]
            yoke = None
            if cond == "yoked":
                yk = (agent, age, vis)
                if yk not in yokes:
                    ys = m.make_stream("neither", age, vis, n, YOKE_SEED)
                    yokes[yk] = m.simulate(agent, "intact", ys,
                                           record_slow=True)
                yoke = yokes[yk]
            r = m.simulate(agent, cond, s, yoke=yoke, record_slow=True)
            e = m.endpoints(r["choices"], r["c"], s)
            e.update({
                "key": k, "agent": agent, "cond": cond, "env": env,
                "age": age, "vis": vis,
                "lam_onset": float(r["lam"][age].mean()),
                "lam_end": float(r["lam"][-1].mean()),
                "a_onset": float(r["a"][age].mean()),
                "a_end": float(r["a"][-1].mean()),
            })
            f.write(json.dumps(e) + "\n")
            f.flush()


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 400)
