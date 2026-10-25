# scratch/formal/boost_the_vote.py
"""Python port of dmarx/BoostTheVote (boost_the_vote.R, 2014), for the record's CASE on it.

Voters have fixed accuracies drawn from Beta(a, b); the election result is the
weight-averaged vote; after each election every voter's weight is multiplied by
1 + f if their own vote was right and 1 - f if not (full-information feedback);
a fraction `churn` of voters is replaced each round, chosen with probability
proportional to age, entering at weight 1.

One deliberate difference from the R original: a replaced voter's age is reset
to 0 here; the R code never resets it, so newcomers inherit their predecessor's
death risk.
"""
import numpy as np


def boost_the_vote(rng, N=1000, a=2, b=2, f=0.2, elections=30, churn=0.1):
    v = rng.beta(a, b, N)
    w = np.ones(N)
    age = np.zeros(N)
    nc = int(N * churn)
    result = np.zeros(elections)
    for i in range(elections):
        o = rng.random(N) < v
        result[i] = (w * o).sum() / w.sum()
        w = np.where(o, w * (1 + f), w * (1 - f))
        age += 1
        if nc:
            ix = rng.choice(N, nc, replace=False, p=age / age.sum())
            v[ix] = rng.beta(a, b, nc)
            w[ix] = 1
            age[ix] = 0
    return result


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    for f in (0, 0.2, 0.5, 0.8):
        row = []
        for c in (0, 0.1, 0.3):
            last = [boost_the_vote(rng, f=f, churn=c)[-1] for _ in range(50)]
            row.append(f"{np.median(last):.2f}")
        print(f, *row)
