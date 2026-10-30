---
number: 1161
status: Active
formerly:
- THEORY-tmpbnint
title: 'In Friedkin''s simulations of reflected appraisal with Friedkin–Johnsen anchoring on initial positions, 99.0–100% of 100,000 random strongly connected networks of 5 to 25 members, complete or with random zero weights, evolve to a single leader and the rest to two'
version: 2
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed from the reading of Friedkin's 2011/2012 paper (NOTE-1374),
    set beside the record's reading of Jia, MirTabatabaei, Friedkin and
    Bullo (LIT-1146, NOTE-1135, THEORY-916). Both halves were re-run on
    2026-10-29 in a scratch script that was not kept in the record:
    Friedkin's update as printed on 300 random complete networks each of
    sizes 5, 10 and 20, and on 300 random strongly connected networks of
    size 10 and density 0.4; and, on 100 random complete networks each
    of sizes 5 and 10, Friedkin's update and the DeGroot–Friedkin update
    from the same start. Proposed because the concentration result is
    shown only by simulation, Friedkin's and this record's.
- version: 2
  date: '2026-10-30'
  note: >-
    Narrowed and promoted by the twenty-fourth status review, at the
    status review's ruling (the owner delegated these rulings; ADR-065).
    The title now reports Friedkin's simulations only (NOTE-1374, read
    in full; Table 2), with LIT-1404 its one source; nothing in the
    record contradicts them. The old "almost every random strongly
    connected group" stated a general law, beside re-runs that gave 93%
    and 96% single leaders on sparser networks of density 0.4. The
    comparison with the DeGroot–Friedkin step stays in THEORY-tmp771g4,
    Proposed, which extends this entry and keeps the old title and
    condition word for word (ADR-065 §3; ADR-047 kind 1), because it
    puts the record's own re-run beside two papers, and a THEORY is a
    reading of its source. The re-runs, including a second check on
    2026-10-30 with its script and controls, are in the note of
    2026-10-30. The old title: "Under reflected appraisal across issues,
    whether power concentrates in one member depends on the single-issue
    step: with Friedkin–Johnsen anchoring on initial positions almost
    every random strongly connected group evolves to a single leader,
    and with DeGroot consensus the same random complete networks keep
    power spread". The old promote_when: "An analysis of the
    Friedkin–Johnsen reflected-appraisal map (Eqs. 6, 9 and 10 of
    LIT-1404) that finds its fixed points and their stability for
    strongly connected relative weights, showing that the autocratic
    fixed points attract almost every start, or a published simulation
    by others that reproduces the contrast with the DeGroot–Friedkin map
    on the same networks. A larger simulation by this record would not
    settle it."
tags:
- network-science
- complex-systems
date: '2026-10-29'
source:
- LIT-1404
summary: >-
  Friedkin (2011/2012), LIT-1404, read in NOTE-1374. Under reflected
  appraisal, the next self-weight set to the member's share of control
  over the last issue, with each issue settled by Friedkin–Johnsen
  anchoring, his simulations give a single leader in 99.0–100% of 100,000
  random networks. Re-runs on sparser networks gave 93% and 96%. The
  contrast with the DeGroot step, and which step real groups follow, are
  not this reading's: the first is THEORY-tmp771g4.
---
<!-- inactive-ok-file: THEORY-tmp771g4 — Proposed; filed beside this reading by the twenty-fourth status review: the comparison of the two single-issue steps -->
<!-- inactive-ok-file: THEORY-916 — Proposed; the companion account, cited as open and not leaned on -->

# THEORY-1161: In Friedkin's simulations of reflected appraisal with Friedkin–Johnsen anchoring on initial positions, 99.0–100% of 100,000 random strongly connected networks of 5 to 25 members, complete or with random zero weights, evolve to a single leader and the rest to two

## Source

Friedkin, N. E. (2011). A formal theory of reflected appraisals in the
evolution of power. *Administrative Science Quarterly* 56(4), LIT-1404,
read in full in NOTE-1374 (Table 2 and Eqs. 6, 9 and 10).

## What was actually shown

Friedkin fixes the relative interpersonal weights C and, after each issue,
sets member i's self-weight to their share of the total control over that
issue's outcome. One issue is settled by the Friedkin–Johnsen model:
W = AC + I − A with A = diag(1 − w); y(t+1) = AWy(t) + (I − A)y(1), so each
member stays anchored on their initial position; control
V = (I − AW)⁻¹(I − A); the next self-weight is the column mean of V.

In his simulations, 10,000 random systems for each of two types and five
sizes from 5 to 25, the share that evolves to a single leader is
0.9996–1.0000 for complete networks (Type 1) and 0.9900–0.9987 for networks
with random densities and arrangements of zero weights (Type 2); the rest
end with two members holding all control.

What could have come out otherwise: the end states could have kept power
spread, or split it among several members. In Friedkin's samples they
almost never do.

## What this does not say

- **Not that real groups concentrate power.** It is a model. Friedkin's
  experiment tests one step of the rule over five issues, and it scores
  self-weights with the anchored model, so it cannot test the end state.
- **Not which feature of the anchored step does the work.** The self-weight
  enters twice, on W's diagonal and in the anchorage (I − A)y(1). Whether
  the anchorage alone gives autocracy, or only the double entry does, was
  not separated.
- **Not a proof, and not for every network.** These are simulations on
  random weights. Sparser networks give more two-member ends (the note
  below), and no class of C is excluded.
- **Not a comparison with the DeGroot step.** Friedkin's paper does not
  make one. The contrast with Jia et al.'s DeGroot–Friedkin model, and the
  general claim that the single-issue step decides whether power
  concentrates, are THEORY-tmp771g4, Proposed.

## Note of 2026-10-30: the re-runs

**What was re-run.** Friedkin's update as printed (above), and, from the
same networks and starting self-weights, the DeGroot–Friedkin update of
Jia, MirTabatabaei, Friedkin and Bullo (2015), LIT-1146, read in NOTE-1135
(THEORY-916): W = diag(x) + (I − diag(x))C, each issue goes to consensus,
and control, which becomes the next x, is W's dominant left eigenvector
normalised to sum 1.

**The first run, 2026-10-29** (NOTE-1374; its script was not kept). Every
one of 900 random complete networks (300 each of sizes 5, 10 and 20) ended
with one self-weight above 0.99 and the rest below 0.01. On 300 random
strongly connected networks of size 10 and density 0.4, 93% ended with a
single leader and the rest with two. On 100 random complete networks each
of sizes 5 and 10, Friedkin's update gave a median largest self-weight of
1.0 and the DeGroot–Friedkin update 0.29 and 0.13.

**The second check, 2026-10-30**, by the twenty-fourth status review, with
the script below (numpy only, seed 1, run with `python3 -I`). Off-diagonal
weights are uniform on (0, 1), rows normalised; sparse networks keep each
off-diagonal weight with probability 0.4 and are redrawn until strongly
connected; starting self-weights are uniform on (0.05, 0.95); each update
is iterated to a change below 10⁻¹² or 3,000 steps. A run is a single
leader when one self-weight exceeds 0.99 and the rest are below 0.01, and
bilateral when the two largest sum above 0.99.

- Friedkin's update, complete networks: 300/300 single leaders at each of
  sizes 5, 10 and 20.
- Friedkin's update, strongly connected networks of size 10 and density
  0.4: 289/300 (96%) single leaders, 11 bilateral. Friedkin's Type 2
  densities were random, so this is not his population.
- Same complete networks and starts, sizes 5 and 10: Friedkin's update gave
  a median largest self-weight of 1.000 at both sizes; the DeGroot–Friedkin
  update 0.267 and 0.128, with a largest value over all runs of 0.413 at
  size 5 and 0.172 at size 10. The first run's "never above 0.40" is not
  reproduced exactly.
- Controls: the DeGroot–Friedkin update goes autocratic on a star
  ([1, 0, 0, 0, 0]) and democratic on a uniform complete network (0.2
  each), as Jia et al.'s Lemmas 3.2 and 3.1 say; the classifier calls a
  uniform vector "other" and a unit vector "single".

```python
import numpy as np

def rand_C(n, rng, density=1.0):
    while True:
        M = rng.random((n, n)); np.fill_diagonal(M, 0)
        if density < 1:
            mask = rng.random((n, n)) < density; np.fill_diagonal(mask, False); M = M * mask
        if (M.sum(1) == 0).any():
            continue
        R = (M > 0).astype(int) + np.eye(n, dtype=int)
        if (np.linalg.matrix_power(R, n) > 0).all():      # strongly connected
            return M / M.sum(1, keepdims=True)

def friedkin_step(C, w):                                   # Eqs. (9), (6), (10)
    n = len(w); A = np.diag(1 - w)
    W = A @ C + np.eye(n) - A
    V = np.linalg.solve(np.eye(n) - A @ W, np.eye(n) - A)
    return V.mean(0)

def df_step(C, x):                                         # DeGroot-Friedkin
    n = len(x); W = np.diag(x) + (np.eye(n) - np.diag(x)) @ C
    vals, vecs = np.linalg.eig(W.T)
    v = np.abs(np.real(vecs[:, np.argmax(np.real(vals))]))
    return v / v.sum()

def run(step, C, w, iters=3000, eps=1e-12):
    for _ in range(iters):
        w = np.clip(w, 0, 1); w2 = step(C, w)
        if np.max(np.abs(w2 - w)) < eps:
            return w2
        w = w2
    return w

def classify(w):
    s = np.sort(w)[::-1]
    if s[0] > 0.99 and (s[1:] < 0.01).all(): return "single"
    if s[0] + s[1] > 0.99: return "bilateral"
    return "other"

rng = np.random.default_rng(1)
for n in (5, 10, 20):
    out = [classify(run(friedkin_step, rand_C(n, rng), rng.uniform(0.05, 0.95, n))) for _ in range(300)]
    print(n, out.count("single"), out.count("bilateral"), out.count("other"))
out = [classify(run(friedkin_step, rand_C(10, rng, 0.4), rng.uniform(0.05, 0.95, 10))) for _ in range(300)]
print("sparse", out.count("single"), out.count("bilateral"), out.count("other"))
for n in (5, 10):
    f, d = [], []
    for _ in range(100):
        C = rand_C(n, rng); w0 = rng.uniform(0.05, 0.95, n)
        f.append(run(friedkin_step, C, w0.copy()).max()); d.append(run(df_step, C, w0.copy()).max())
    print(n, np.median(f), np.median(d), np.max(d))
n = 5; C = np.zeros((n, n)); C[1:, 0] = 1; C[0, 1:] = 1 / (n - 1)
print("star", np.round(run(df_step, C, rng.uniform(0.05, 0.95, n)), 3))
C = (np.ones((n, n)) - np.eye(n)) / (n - 1)
print("uniform", np.round(run(df_step, C, rng.uniform(0.05, 0.95, n)), 3))
print(classify(np.ones(5) / 5), classify(np.eye(5)[0]))
```

The re-runs agree with Friedkin's Table 2 on complete networks, and on
complete networks they set the two updates far apart. That comparison puts
the record's own computation beside two papers, so it is not this
reading's: it is THEORY-tmp771g4.

## Connections

[CASE-092](../cases.d/CASE-092.md)'s note of 2026-10-23 asks that a coupled meaning–influence model
be compared with "DeGroot–Friedkin" reflected appraisal. On THEORY-tmp771g4
that is two baselines with opposite predictions, and the comparison
should name the single-issue step. [CLAIM-297](../claims.d/CLAIM-297.md)'s authority updated from
performance has the same shape as both rules.
