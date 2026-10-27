---
status: Active
title: 'In the infinite hidden Markov model, drawing at each time step a slice variable uniformly below the probability of the transition taken leaves the posterior unchanged and leaves only finitely many state trajectories with positive probability, so a whole trajectory can be resampled exactly by forward filtering and backward sampling, with no truncation of the state space'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Active from NOTE-tmp2597d. It is the paper's construction, §4
    and footnote 2 of Van Gael, Saatci, Teh and Ghahramani (2008). The
    finiteness follows because each transition row sums to one and the
    slice is positive almost surely. The invariance was checked
    numerically on a finite HMM (3 states, 4 steps, binary emissions):
    150,000 iterations of slice-then-trajectory sampling reached the exact
    posterior over the 81 trajectories to a total-variation distance of
    0.008 (record script, 2026-10-27).
tags:
- probabilistic-modeling
- mathematical-statistics
date: '2026-10-27'
source:
- LIT-tmp0oa8w
summary: >-
  Van Gael, Saatci, Teh and Ghahramani (2008), LIT-tmp0oa8w, read in
  NOTE-tmp2597d. u_t ~ Uniform(0, π_{s_{t−1}s_t}) is an auxiliary
  variable, so sampling u given s and then s given u leaves p(s | y)
  invariant; given u, the forward recursion sums only over transitions
  with π > u_t, of which there are finitely many per row. It says the
  sampler is exact, not how fast it mixes (THEORY-tmptl00j).
---
<!-- inactive-ok-file: THEORY-tmptl00j — Proposed; the mixing claim this account leaves out, cited as open -->

# THEORY-tmp7bmmi: In the infinite hidden Markov model, drawing at each time step a slice variable uniformly below the probability of the transition taken leaves the posterior unchanged and leaves only finitely many state trajectories with positive probability, so a whole trajectory can be resampled exactly by forward filtering and backward sampling, with no truncation of the state space

## Source

Van Gael, Saatci, Teh and Ghahramani (2008), *Beam sampling for the
infinite hidden Markov model*, LIT-tmp0oa8w, read in full in
NOTE-tmp2597d: §4, eq. (4), and footnote 2.

## What was actually shown

**Invariance.** The joint p(s, u, y | π, φ) = p(s, y | π, φ) ∏_t
I(0 < u_t < π_{s_{t−1}s_t})/π_{s_{t−1}s_t} has p(s, y | π, φ) as its
marginal, so Gibbs steps on u and on s given u leave the posterior over s
invariant. Given u, the factor 1/π cancels the transition probability and
leaves the indicator: p(s | u, y, π, φ) ∝ ∏_t p(y_t | s_t)
I(u_t < π_{s_{t−1}s_t}).

**Finiteness (footnote 2).** Each π_{kk′} > 0 almost surely, so u_t > 0;
the row π_{s_{t−1}·} sums to one, so finitely many of its entries exceed
u_t. By induction over t, finitely many trajectories s_{1:t} satisfy every
indicator, and the forward recursion (4) and backward sampling run over
them.

**The check.** On a finite HMM with 3 states and 4 steps, the chain
alternating u | s and s | u (forward filtering with the indicators,
backward sampling) visited the 81 trajectories with frequencies within a
total-variation distance of 0.008 of the exact posterior after 150,000
iterations (record script, 2026-10-27). The finite case tests the
invariance; the finiteness is the part specific to the infinite model.

## What this does not say

- **Not that it mixes faster than Gibbs.** That is the paper's empirical
  claim, filed separately as Proposed (THEORY-tmptl00j).
- **Not its cost.** The worst case is O(TK²) per iteration over the K
  represented states; the near-O(TK) behaviour is an observation on one
  synthetic set.
- **Not the hyperparameter updates.** β, α and γ are sampled as for the
  HDP; their correctness is the HDP paper's.

## Connections

- **LIT-1577 and NOTE-1199.** The infinite factorial HMM applies the same
  construction to each binary chain of the Markov IBP, with a slice over
  its sticks (THEORY-tmphvhg6's construction, LIT-tmpfhqac).
- **THEORY-tmphvhg6.** The IBP's slice sampler uses the same device on
  feature sticks.
