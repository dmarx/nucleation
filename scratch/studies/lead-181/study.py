"""LEAD-181: run CASE-249's institution under five governance regimes and
four settings, and measure the inquiry an adaptive institution undertakes.

For each (setting, regime): the Monte Carlo value of every stationary
policy on the grid (common random numbers), the optimal policy and the set
of policies statistically tied with it, and 16 independent gradient-bandit
learners trained for 4000 episodes. Writes results.json and results.md.
Run: OPENBLAS_NUM_THREADS=1 python3 -I study.py   (about two minutes)
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as m  # noqa: E402

SETTINGS = {
    "S1 costly inquiry": dict(alpha=0.1),
    "S2 costless inquiry and remediation": dict(alpha=0.0),
    "S3 S1 + surfacing s=0.03": dict(alpha=0.1, s=0.03),
    "S4 S3 + cost of being found out sigma=3": dict(alpha=0.1, s=0.03, sigma=3.0),
}
REPS, SEED = 2000, 20261123
EPISODES, LEARNERS, LR = 4000, 16, 0.2
ARMS = m.arms()
A = np.array([x[0] for x in ARMS])


def per_rep(regime, kw):
    vals, stats = [], []
    for ai, bi in ARMS:
        rng = np.random.default_rng(SEED)
        r = m.simulate(np.full(REPS, ai), np.full(REPS, bi), regime, rng, **kw)
        vals.append(r["reward"])
        stats.append({k: float(v.mean()) for k, v in r.items()})
    return np.array(vals), stats


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out = {"params": m.DEFAULTS, "settings": SETTINGS, "arms": ARMS,
           "reps": REPS, "episodes": EPISODES, "learners": LEARNERS,
           "results": {}}
    lines = ["| setting | regime | optimal (a, b) | tied a range | "
             "learned mean a | learned hidden found | true viol (learned) | "
             "recognized viol (learned) |", "|" + "---|" * 8]
    for sname, kw in SETTINGS.items():
        for regime in m.REGIMES:
            vals, stats = per_rep(regime, kw)
            mean = vals.mean(1)
            best = int(mean.argmax())
            diff = vals - vals[best]
            se = diff.std(1, ddof=1) / np.sqrt(REPS)
            tied = [i for i in range(len(ARMS))
                    if i == best or mean[best] - mean[i] <= 2 * se[i]]
            rng = np.random.default_rng(SEED + 1)
            P = m.learn(regime, ARMS, EPISODES, LEARNERS, rng, lr=LR, **kw)
            la = float((P * A).sum(1).mean())
            la_sd = float((P * A).sum(1).std())
            w = P.mean(0)
            lf = float(sum(w[i] * stats[i]["hidden_recognized"]
                           for i in range(len(ARMS))))
            ltv = float(sum(w[i] * stats[i]["true_viol"]
                            for i in range(len(ARMS))))
            lrv = float(sum(w[i] * stats[i]["recog_viol"]
                            for i in range(len(ARMS))))
            res = dict(
                optimal=ARMS[best], optimal_value=float(mean[best]),
                optimal_stats=stats[best],
                tied_a=[int(A[i]) for i in tied],
                learned_mean_a=la, learned_sd_a=la_sd,
                learned_hidden_recognized=lf, learned_true_viol=ltv,
                learned_recog_viol=lrv,
            )
            out["results"][f"{sname} | {regime}"] = res
            lines.append(
                f"| {sname} | {regime} | {tuple(ARMS[best])} | "
                f"{min(res['tied_a'])}-{max(res['tied_a'])} | "
                f"{la:.2f} (sd {la_sd:.2f}) | {lf:.2f} | {ltv:.2f} | "
                f"{lrv:.2f} |")
            print(lines[-1], flush=True)
    with open(os.path.join(here, "results.json"), "w") as f:
        json.dump(out, f, indent=1)
    with open(os.path.join(here, "results.md"), "w") as f:
        f.write("# LEAD-181 results\n\n"
                "a: inquiry units per period (of B = 10); b: remediation "
                "cap. 'tied a range': inquiry levels of the policies within "
                "two paired standard errors of the best. Learned: 16 "
                "gradient-bandit learners, 4000 episodes each; hidden found "
                "is the fraction of the 20 hidden requirements recognized "
                "by the end; violations at the end of the episode, of 30 "
                "requirements (about 9 violated at the start).\n\n")
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
