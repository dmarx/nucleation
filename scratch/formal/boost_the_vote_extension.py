# scratch/formal/boost_the_vote_extension.py
"""The three-axis extension of the BoostTheVote model proposed in the record's CASE on it.

Voters have fixed leans: voter i votes "1" with probability p_i ~ Beta(2, 2),
whatever the truth. The truth is 1 for the first E1 elections and 0 for the
next E2, so who is right changes at the switch. The collective decision is
the weighted majority. Weights update multiplicatively: x(1 + f) if a scored
voter's vote matched the standard, x(1 - f) if not.

Axes:
  rho     feedback: probability that an unheeded voter (one who voted against
          the decision) is scored at all; heeded voters are always scored.
          rho = 1 is full information, rho = 0 is bandit feedback.
  m       metric: probability that, in a given election, the standard voters
          are scored against is the collective's own decision rather than the
          truth. m = 0 is an independent metric, m = 1 a fully endogenous one.
  renewal None; or a fraction `churn` replaced each round at weight 1 with a
          fresh lean, chosen either by age ("age") or as the highest-weight
          voters ("top", a term limit).

  obs     observability: "always", the truth is observed every election; or
          "act", the outcome is observed only when the decision is 1 (acting);
          deciding 0 (avoiding) yields no observation and nobody is scored
          against the truth. With "act" the truth switches 0 -> 1, so that the
          old answer is avoidance; with "always" it switches 1 -> 0.

Reported per cell, as means over runs: accuracy of the decision before the
switch (phase 1) and after it (phase 2); the share of runs right at the last
election; and the mean delay, in elections, from the switch to the first of
five consecutive right decisions (E2 if never).
"""
import itertools

import numpy as np


def run(rng, rho, m, renewal, obs="always", N=1000, f=0.2, E1=30, E2=60, churn=0.05):
    p = rng.beta(2, 2, N)
    w = np.ones(N)
    age = np.zeros(N)
    right = []
    for t in range(E1 + E2):
        before = t < E1
        truth = (1 if before else 0) if obs == "always" else (0 if before else 1)
        votes = (rng.random(N) < p).astype(int)
        decision = int((w * votes).sum() / w.sum() > 0.5)
        right.append(decision == truth)
        observed = obs == "always" or decision == 1
        endogenous = rng.random() < m
        if not (endogenous or observed):
            continue_scoring = False
        else:
            continue_scoring = True
        standard = decision if endogenous else truth
        heeded = votes == decision
        scored = (heeded | (rng.random(N) < rho)) & continue_scoring
        good = votes == standard
        w = np.where(scored & good, w * (1 + f), np.where(scored & ~good, w * (1 - f), w))
        w /= w.mean()  # rescale to avoid overflow; relative weights unchanged
        age += 1
        if renewal is not None:
            k = int(N * churn)
            if renewal == "age":
                ix = rng.choice(N, k, replace=False, p=age / age.sum())
            else:  # "top": replace the k highest-weight voters
                ix = np.argsort(w)[-k:]
            p[ix] = rng.beta(2, 2, k)
            w[ix] = 1
            age[ix] = 0
    right = np.array(right)
    post = right[E1:]
    delay = next((i for i in range(len(post) - 4) if post[i:i + 5].all()), E2)
    return right[:E1].mean(), post.mean(), right[-1], delay


def table(rng, cells, runs):
    print(f"{'obs':>6} {'rho':>4} {'m':>4} {'renewal':>7} | phase1 phase2  last  delay")
    for obs, rho, m, ren in cells:
        res = np.array([run(rng, rho, m, ren, obs) for _ in range(runs)], dtype=float)
        a, b, c, d = res.mean(axis=0)
        print(f"{obs:>6} {rho:>4} {m:>4} {str(ren):>7} | {a:6.2f} {b:6.2f} {c:5.2f} {d:6.1f}")


def main(runs=100, seed=0):
    rng = np.random.default_rng(seed)
    table(rng, [("always",) + c for c in itertools.product((1.0, 0.0), (0.0, 0.25, 0.5, 1.0), (None, "age", "top"))], runs)
    print()
    table(rng, [("act",) + c for c in itertools.product((1.0, 0.0), (0.0,), (None, "age"))], runs)


if __name__ == "__main__":
    main()
