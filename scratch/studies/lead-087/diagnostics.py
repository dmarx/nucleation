"""Post hoc, run AFTER the pre-registered verdict (summary.txt) and not
part of it: why is spillover small, and does the ordering of sigma across
arms survive other settings? Each variant reruns study.one_seed with
changed constants and appends to diagnostics.jsonl, tagged by variant.

    OMP_NUM_THREADS=1 python3 -I diagnostics.py [n_seeds]
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import model as M  # noqa: E402
import study  # noqa: E402

OUT = os.path.join(HERE, "diagnostics.jsonl")
BASE = dict(F_S=M.F_S, Q_BASE=M.Q_BASE, LR_SOC=M.LR_SOC, WINDOW=M.WINDOW)
VARIANTS = {
    "S40": dict(F_S=0.4),               # twice as many perturbed members
    "lowfb": dict(Q_BASE=0.01),         # weaker anchoring by the world
    "soc3x": dict(LR_SOC=0.15),         # stronger social updates
    "win100": dict(WINDOW=100),         # shorter window after the perturbation
}


def main(n):
    done = set()
    if os.path.exists(OUT):
        done = {(r["variant"], r["seed"]) for r in map(json.loads, open(OUT))}
    for name, ch in VARIANTS.items():
        for k, v in {**BASE, **ch}.items():
            setattr(M, k, v)
        for seed in range(n):
            if (name, seed) in done:
                continue
            tmp = os.path.join(HERE, ".diag_tmp.jsonl")
            if os.path.exists(tmp):
                os.remove(tmp)
            study.OUT = tmp
            study.one_seed(seed, set())
            with open(tmp) as f, open(OUT, "a") as g:
                for line in f:
                    r = json.loads(line)
                    r["variant"] = name
                    g.write(json.dumps(r) + "\n")
            os.remove(tmp)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 20)
