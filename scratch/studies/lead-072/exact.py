"""Exact (enumerated) bias, RMSE, interval coverage and test size per content.

Writes one JSON line per grid cell to exact.jsonl, skipping cells already
written. Rerun: python3 -I exact.py
"""
import json
import os
import sys

import numpy as np
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sig  # noqa: E402

OUT = os.path.join(HERE, "exact.jsonl")
NS = [1, 2, 3, 5, 10, 30, 100]
# (p, p') pairs: base 0.5 and 0.15, per-content signalling 2|p-p'| of 0, 0.2, 0.5, 1.0
PAIRS = [(0.5, 0.5), (0.5, 0.6), (0.5, 0.75), (0.25, 0.75),
         (0.15, 0.15), (0.15, 0.25), (0.15, 0.4), (0.05, 0.55)]


def done_keys():
    keys = set()
    if os.path.exists(OUT):
        with open(OUT) as f:
            for line in f:
                r = json.loads(line)
                keys.add((r["n"], r["p"], r["q"]))
    return keys


def fisher_size(n, m, p, alpha=0.05):
    xs, ys = np.arange(n + 1), np.arange(m + 1)
    w = np.outer(stats.binom.pmf(xs, n, p), stats.binom.pmf(ys, m, p))
    rej = np.array([[sig.content_pvalue(x, n, y, m) <= alpha for y in ys] for x in xs])
    return float((w * rej).sum())


def fisher_power(n, m, p, q, alpha):
    xs, ys = np.arange(n + 1), np.arange(m + 1)
    w = np.outer(stats.binom.pmf(xs, n, p), stats.binom.pmf(ys, m, q))
    rej = np.array([[sig.content_pvalue(x, n, y, m) <= alpha for y in ys] for x in xs])
    return float((w * rej).sum())


def main():
    keys = done_keys()
    with open(OUT, "a") as f:
        for n in NS:
            for p, q in PAIRS:
                if (n, p, q) in keys:
                    continue
                r = {"n": n, "m": n, "p": p, "q": q, "true": round(2 * abs(p - q), 10)}
                r["plug_mean"], r["plug_rmse"] = sig.exact_moments(sig.plug, n, n, p, q)
                if n >= 2:
                    r["root_mean"], r["root_rmse"] = sig.exact_moments(sig.root_u2, n, n, p, q)
                # per-content interval coverage at the level used for a rank-2 Delta (k = 2)
                r["cov_cp_k2"] = sig.exact_content_coverage(n, n, p, q, 0.05, "cp", k=2)
                r["cov_newc_k2"] = sig.exact_content_coverage(n, n, p, q, 0.05, "newcombe", k=2)
                # per-content Fisher test at alpha/2 (Bonferroni for k = 2)
                r["fisher_rej_k2"] = fisher_power(n, n, p, q, 0.025)
                f.write(json.dumps(r) + "\n")
                f.flush()
                print(n, p, q, flush=True)


if __name__ == "__main__":
    main()
