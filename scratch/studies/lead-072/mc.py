"""Monte Carlo on whole rank-2 systems: bias of Delta, coverage of the two
Delta intervals, size and power of the no-signalling test.

A rank-2 system: contents A (e.g. the verb) and B (the noun); context 1
and context 2 each record (A, B) jointly, from n1 and n2 occurrences.
Each context's joint is set by its two marginals and a correlation rho.
One JSON line per cell in mc.jsonl; cells already written are skipped.
Rerun: python3 -I mc.py
"""
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sig  # noqa: E402

OUT = os.path.join(HERE, "mc.jsonl")
REPS = 4000
NS = [2, 3, 5, 10, 30, 100]
# (a1, b1, a2, b2, rho): P(A=+1), P(B=+1) in contexts 1 and 2
MODELS = {
    "null_half": (0.5, 0.5, 0.5, 0.5, 0.6),
    "null_skew": (0.15, 0.8, 0.15, 0.8, 0.1),
    "sig_0.4": (0.4, 0.5, 0.6, 0.5, 0.5),
    "sig_1.0": (0.3, 0.4, 0.55, 0.65, 0.4),
    "sig_2.0": (0.2, 0.3, 0.7, 0.8, 0.3),
    "sig_3.0": (0.1, 0.2, 0.85, 0.95, 0.2),
}


def joint(a, b, rho):
    c = rho * math.sqrt(a * (1 - a) * b * (1 - b))
    p11 = a * b + c
    p10 = a - p11
    p01 = b - p11
    p00 = 1 - p11 - p10 - p01
    pr = np.array([p11, p10, p01, p00])
    assert (pr >= -1e-12).all()
    return np.clip(pr, 0, 1) / np.clip(pr, 0, 1).sum()


def counts(rng, pr, n):
    c = rng.multinomial(n, pr)
    return c[0] + c[1], c[0] + c[2]  # #(A=+1), #(B=+1)


def main():
    done = set()
    if os.path.exists(OUT):
        with open(OUT) as f:
            done = {(json.loads(l)["model"], json.loads(l)["n"]) for l in f}
    with open(OUT, "a") as f:
        for name, (a1, b1, a2, b2, rho) in MODELS.items():
            p1, p2 = joint(a1, b1, rho), joint(a2, b2, rho)
            true = 2 * abs(a1 - a2) + 2 * abs(b1 - b2)
            for n in NS:
                if (name, n) in done:
                    continue
                rng = np.random.default_rng(7200 + 31 * n + sum(map(ord, name)))
                plug, root, cbox, cnew, rej, lo2 = [], [], 0, 0, 0, 0
                for _ in range(REPS):
                    xa, xb = counts(rng, p1, n)
                    ya, yb = counts(rng, p2, n)
                    cs = [(xa, n, ya, n), (xb, n, yb, n)]
                    plug.append(sum(sig.plug(*c) for c in cs))
                    root.append(sum(sig.root_u2(*c) for c in cs))
                    l, h = sig.box_interval(cs)
                    cbox += (l - 1e-12 <= true <= h + 1e-12)
                    lo2 += (l >= 2)
                    l, h = sig.newcombe_delta(cs)
                    cnew += (l - 1e-12 <= true <= h + 1e-12)
                    rej += sig.nosig_test(cs)[0]
                r = {"model": name, "n": n, "true": true, "reps": REPS,
                     "plug_mean": float(np.mean(plug)), "root_mean": float(np.mean(root)),
                     "plug_rmse": float(np.sqrt(np.mean((np.array(plug) - true) ** 2))),
                     "root_rmse": float(np.sqrt(np.mean((np.array(root) - true) ** 2))),
                     "cov_box": cbox / REPS, "cov_newcombe": cnew / REPS,
                     "reject_nosig": rej / REPS, "box_lower_ge_2": lo2 / REPS}
                f.write(json.dumps(r) + "\n")
                f.flush()
                print(name, n, flush=True)


if __name__ == "__main__":
    main()
