---
status: Active
title: 'In a two-alternative choice made by two competing leaky accumulators, the decision is optimal only when leak and mutual inhibition balance, so that the network integrates the difference of the evidence without loss; imbalance bounds accuracy at any fixed time and weights early or late evidence'
version: 1
tags:
- behavioral-integration
- cognition
- probabilistic-modeling
date: '2026-10-03'
source:
- LIT-tmp93b13
- LIT-tmp2p2lh
summary: >-
  Bogacz et al. ([LIT-tmp93b13](../literature.d/LIT-tmp93b13.md)) prove that the pure drift diffusion model is
  the continuum limit of the sequential probability ratio test, and so the
  optimal two-choice decider, and that the linearised Usher–McClelland
  network reduces to it exactly when leak equals inhibition (and, for free
  response, when both are also large). Usher and McClelland ([LIT-tmp2p2lh](../literature.d/LIT-tmp2p2lh.md))
  derived the difference of the two units as an Ornstein–Uhlenbeck process
  with net leak K = k − β: K ≠ 0 caps accuracy, leak-dominant weights late
  evidence and inhibition-dominant early. Active because the core is
  derivation, checkable on paper. What it does not say: that brains are
  balanced, that the result carries to more than two options or to
  non-stationary evidence, or that the primacy and recency seen in six
  participants are explained by it.
---
<!-- inactive-ok-file: THEORY-056 — Proposed; named as the record's account of competing motive states, with no relation claimed -->
<!-- inactive-ok-file: THEORY-tmp2002z THEORY-tmp1gn9c — Proposed; companion accounts in this batch, named for what they borrow from this one -->

# THEORY-tmpinmsm: In a two-alternative choice made by two competing leaky accumulators, the decision is optimal only when leak and mutual inhibition balance, so that the network integrates the difference of the evidence without loss; imbalance bounds accuracy at any fixed time and weights early or late evidence

## Source

- Bogacz, Brown, Moehlis, Holmes & Cohen (2006), [LIT-tmp93b13](../literature.d/LIT-tmp93b13.md), read in
  [NOTE-tmpo6f5g](../notes.d/NOTE-tmpo6f5g.md): the SPRT and the DDM (pp. 703–704), the reductions of the
  mutual inhibition model (Eqs. 18–26, Figs. 4–10) and Table 1. Appendix A,
  where the proofs are written out, was read only by its section titles.
- Usher & McClelland (2001), [LIT-tmp2p2lh](../literature.d/LIT-tmp2p2lh.md), read in [NOTE-tmp74uji](../notes.d/NOTE-tmp74uji.md): the
  reduction to an Ornstein–Uhlenbeck process (Eqs. 5–10), Figure 4, and
  Experiment 3.

## What was actually shown

**The standard of optimality.** Bogacz et al. ([LIT-tmp93b13](../literature.d/LIT-tmp93b13.md)) restate the
classical theorems. The sequential probability ratio test (Wald) is the
fastest test for a given error rate, and the Neyman–Pearson test is the most
accurate for a given time. Both accumulate the log likelihood ratio, and in
the continuum limit that is a drift diffusion process. So a two-choice
decider that integrates the *difference* of the evidence for the two options,
perfectly and from a fixed start, is doing the best that can be done.

**The network and its difference process.** Usher and McClelland
([LIT-tmp2p2lh](../literature.d/LIT-tmp2p2lh.md)) give each alternative a leaky accumulator and let each
inhibit the other. Linearised, the difference x₁ − x₂ obeys
dx = (v − Kx) dt/τ + noise, with K = k − β, leak minus inhibition (their
Eqs. 5–8). K = 0 is the classical diffusion model. For K ≠ 0 the
discriminability under unlimited time is finite, d_asy = (2v/σ)√(1/K)
(Eq. 10). Bogacz et al. derive the same decomposition in rotated
coordinates, writing λ = w − k (inhibition minus leak, the opposite sign).
The difference is an O-U process with rate λ, and the sum is a stable O-U
process with rate k + w. With k = w the difference is a pure diffusion. With
k and w both large, the sum settles fast onto a "decision line" and the
two-dimensional network behaves as the one-dimensional DDM.

**Which balance is optimal, and where.** Bogacz et al. find, for the linear
model, that:

- under interrogation (a decision forced at time T), error is minimised at
  λ = 0, whatever the magnitude of leak and inhibition;
- in free response, at fixed error, decision time is shortest at k = w and
  falls toward the DDM's as k = w grows;
- as T → ∞, error goes to zero only for λ = 0. For λ ≠ 0 it has a floor that
  depends on |λ| alone (Table 1).

**Which evidence is weighted.** In the linear O-U process an input arriving
at time s is carried to the decision at t with weight e^{−K(t−s)}. That is the
standard solution of the equation, written here by the record; the sources
state its consequence. When leak dominates,
old evidence decays and late evidence counts most (recency). When inhibition
dominates, an early lead is amplified and early evidence counts most
(primacy). Usher and McClelland show by simulation of the full nonlinear
model that the time–accuracy curve depends only on |K|, while the
trajectories differ (Fig. 4–5). So two networks with equal accuracy can
weight the stream oppositely.

The first three findings and the weighting are mathematics about a stated
model, which is why this account is Active. What could have come out
otherwise is the reduction: the race model never reduces to the DDM
([LIT-tmp93b13](../literature.d/LIT-tmp93b13.md)), and a network can be built that way.

**Empirical contact, not part of the claim.** Usher and McClelland's
Experiment 3 (6 participants) found 2 who favoured a late cluster of
evidence, 2 who favoured an early one and 2 who were neutral. Fitted leak and
inhibition accounted for each pattern, and the neutral participants were the
most accurate, as the account predicts. That is consistent with it, on six
people, and attentional explanations were not excluded ([NOTE-tmp74uji](../notes.d/NOTE-tmp74uji.md), C4).

## What this does not say

- **It does not say brains are balanced.** It says what balance buys. Whether
  a given circuit is balanced is an empirical question this account cannot
  answer, and Usher and McClelland's own evidence that leak matters (a
  likelihood ratio of about 62 over three participants) is modest and contested
  by drift-variance accounts ([LIT-tmpcmcw7](../literature.d/LIT-tmpcmcw7.md)).
- **Two alternatives, stationary evidence, linearised units.** The
  multi-alternative case (the MSPRT) is pointed to and not treated. The
  threshold-linear floor is dropped. The extended equivalences need the
  total input to be constant across trials, and Bogacz et al. note there is
  no cortical evidence for the anticorrelated starting points they also
  need.
- **Imbalance is not always worse in practice.** Bogacz et al. report by
  simulation that with variable starting points a leak-dominant network can
  do better, because it discounts a noisy start. And in free response, error
  can still be driven to zero for λ < 0, but only with decision times that
  diverge. "Bounds accuracy" in the title is about a fixed time.
- **Optimality here is statistical, not about what is at stake.** Setting
  the threshold for a utility (reward rate, Bayes risk) is a further step,
  which Bogacz et al. also take. The companion account [THEORY-tmp2002z](THEORY-tmp2002z.md) uses
  it.

## What would show it wrong

As mathematics, an error in the derivations. Appendix A of [LIT-tmp93b13](../literature.d/LIT-tmp93b13.md) has
not been read line by line here, so a first-hand check of the proofs of the
O-U error rates and of the free-response optimum would close that gap. The
claim would be shown not to apply, rather than wrong, by evidence that the
choice circuits it is used to describe do not compare alternatives by mutual
inhibition at all.

## Connections

- **The unity it is about.** This is `behavioral-integration` at the scale of
  one decision: how two candidate responses come down to one. It is not a
  claim about phenomenal unity or about any self ([ADR-024](../decisions.d/ADR-024.md)).
- **[THEORY-056](THEORY-056.md)** (regulation as one motive state checking another, with no
  regulator above them). Mutual inhibition between accumulators is a
  formal case of tendencies that suppress one another with no supervisory
  unit, and this account says when such suppression is lossless. Neither
  source is about emotion or motive, so no relation is declared.
- **[THEORY-tmp1gn9c](THEORY-tmp1gn9c.md)** (the readiness potential) uses the leak-dominant,
  single-accumulator regime of the same process.
