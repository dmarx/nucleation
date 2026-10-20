---
number: 757
status: Active
formerly:
- THEORY-tmpkusod
title: 'The information bottleneck is successively refinable between every pair of budgets when Y is a function of X, by nested erasures of Y, and when X and Y are both binary, where the optimum at each nonzero budget is unique up to merging and relabelling and its two decoder points are the ends of an interval of the source simplex that only widens as the budget grows'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-981. The function case is the paper's Proposition 3 (Appendix B.4) and the binary case its Proposition 5 (Appendix B.7). The paper proves the binary case by citing Witsenhausen and Wyner for the shape of the region where F_β exceeds its convex envelope (its Lemma A3). The re-derivation below replaces that citation with a direct argument, that the curvature of F_β changes sign only through a quadratic with positive leading coefficient. With the paper's Lemma A2, re-derived here, every step is re-derived, which meets the condition for Active under ADR-047 v2. The paper's third case, jointly Gaussian variables (Proposition 2), rests on Kline and Palmer's semigroup result and is not claimed.
tags:
- information-theory
- mathematics
date: '2026-10-20'
source:
- LIT-1258
answers:
- QUESTION-220
summary: >-
  Charvin, Catenacci Volpi and Polani (2023), [LIT-1258](../literature.d/LIT-1258.md), read in [NOTE-981](../notes.d/NOTE-981.md). These are the two finite cases in which nested information-bottleneck optima are guaranteed at every pair of budgets. Neither reaches the record's four-state source, whose Y is not a function of X and whose X has three effective states. [NOTE-981](../notes.d/NOTE-981.md) finds that source not refinable. So binary Y alone does not guarantee nesting. The function case is the degenerate one, where the bottleneck is just a noisy copy of Y.
---
<!-- inactive-ok-file: THEORY-751 — Proposed; the rate–distortion analogue named for comparison, nothing here rests on it -->
# THEORY-757: The information bottleneck is successively refinable between every pair of budgets when Y is a function of X, by nested erasures of Y, and when X and Y are both binary, where the optimum at each nonzero budget is unique up to merging and relabelling and its two decoder points are the ends of an interval of the source simplex that only widens as the budget grows

## Source

Charvin, Catenacci Volpi and Polani (2023), *Entropy* 25(9):1355,
[LIT-1258](../literature.d/LIT-1258.md), read in full in [NOTE-981](../notes.d/NOTE-981.md): Propositions 3 and 5 with
Appendices B.4 and B.7. The criterion used is [THEORY-753](THEORY-753.md).

## What was actually shown

Bottlenecks, refinability and decoder points are as in [THEORY-753](THEORY-753.md).
X and Y are finite and p(x) > 0.

**1. Y = f(X) (Proposition 3, re-derived).**
- *Bound.* By data processing on T → X → Y, I(Y; T) ≤ I(X; T) ≤ λ, and
  I(Y; T) ≤ H(Y).
- *Erasures attain it.* Let T_α equal Y with probability α and an erasure
  symbol e otherwise, the coin independent of X. T_α depends on X only
  through Y, so I(X; T_α) = I(Y; T_α) = H(T_α) − H(T_α | Y) = αH(Y). For
  λ ≤ H(Y), T_{λ/H(Y)} meets the bound. For λ ≥ H(Y), T = Y does.
- *They nest.* For α₁ < α₂, the channel η that keeps a symbol y with
  probability α₁/α₂, erases it otherwise, and keeps e, maps q(T_{α₂}|X) to
  q(T_{α₁}|X). By [THEORY-753](THEORY-753.md), steps 2 and 1, the problem is refinable
  at every pair of budgets. Composing the η in order gives any number of
  stages.

**2. X and Y binary (Proposition 5, re-derived).** Write r = P(X = 1) for a
point of Δ_X = [0, 1], s(r) = s₀ + Δr with sᵢ = P(Y = 1 | X = i) and
Δ = s₁ − s₀, and h for binary entropy in nats. If Δ = 0, I(X; Y) = 0 and
every bottleneck is trivial. If s₀, s₁ ∈ {0, 1}, Y is a function of X and
case 1 applies. Otherwise s(r) ∈ (0, 1) for r ∈ (0, 1).
- *a. Budgets correspond to slopes.* The information curve λ ↦ I_Y(λ) is
  concave, by time-sharing. At a budget λ > 0 below its maximum it has a
  supporting line of slope 1/β. Any bottleneck at λ then minimizes
  I(X; T) − β I(Y; T), since for every T,
  I(Y; T) ≤ I_Y(I(X; T)) ≤ I_Y(λ) + (I(X; T) − λ)/β. Supporting slopes of a
  concave function do not increase, so λ₁ < λ₂ gives β₁ ≤ β₂. Also β > 1,
  because I(Y; T) < I(X; T) for every nontrivial T here. Equality would need
  T → Y → X as well as T → X → Y, and since the graph joining x and y with
  p(x, y) > 0 is connected, that makes T independent of X.
- *b. The curvature of F_β.* By [THEORY-753](THEORY-753.md) step 5, the Lagrangian
  optima are the decompositions of p(X) that reach the lower convex envelope
  K of F_β(r) = h(s(r)) − h(r)/β. On (0, 1),
  F_β″(r) = g(r) / (s(1 − s) r(1 − r)), with
  g(r) = s(r)(1 − s(r))/β − Δ² r(1 − r).
  g is a quadratic in r with leading coefficient Δ²(1 − 1/β) > 0. So
  {g < 0} is an open interval, possibly empty, and F_β is strictly convex on
  each interval where g ≥ 0, since g vanishes there at isolated points at most.
- *c. F_β exceeds its envelope on one interval.* Let P(β) = {K < F_β}, which
  is open. On each component (u, v), K is the chord from (u, F(u)) to
  (v, F(v)) and F lies strictly above it, so F is not convex on [u, v], and
  (u, v) meets {g < 0}. Conversely, a point w with g(w) < 0 is in P(β): if
  K(w) = F(w), a supporting line of K at w lies below F and touches it at w,
  which forces F″(w) ≥ 0. So the interval {g < 0} lies inside P(β), and every
  component of P(β) meets it. Since it is connected, P(β) is a single
  interval (u_β, v_β).
- *d. The optimum is unique.* If p(X) ∈ P(β), K(p) is reached only by
  decompositions supported where F touches the chord's line. Inside (u, v),
  F is above it. Outside, F is strictly convex and meets the line at u or v,
  so it is above it there too. So the decoder points are exactly u_β and
  v_β, with weights fixed by p(X): one canonical optimum, with two distinct,
  hence affinely independent, decoder points. If p(X) ∉ P(β), the trivial
  encoder is optimal and λ = 0.
- *e. P(β) grows with β (the paper's Lemma A2).* Let β₁ ≤ β₂ and
  c = 1/β₁ − 1/β₂ ≥ 0, so F_{β₁} = F_{β₂} − c h. Since −c h is convex,
  K_{β₁} ≥ K_{β₂} − c h. If r ∉ P(β₂), then
  K_{β₁}(r) ≥ F_{β₂}(r) − c h(r) = F_{β₁}(r), so r ∉ P(β₁).
- *f. Conclusion.* For λ₁ < λ₂, steps a, d and e give
  hull{q(X|t₁)} = [u_{β₁}, v_{β₁}] ⊆ [u_{β₂}, v_{β₂}] = hull{q(X|t₂)}. The
  fine decoder points are affinely independent, so by [THEORY-753](THEORY-753.md) step 4
  the problem is (λ₁, λ₂)-refinable.

What could have failed: the region where F_β exceeds its envelope could have
had two components, so that the decoder points jumped as β grew rather than
spreading. Step c rules this out for binary X, because g is a single convex
quadratic. That is also what does not survive a third source letter: the
curvature condition becomes a matrix condition on a two-dimensional simplex.
In [NOTE-981](../notes.d/NOTE-981.md)'s four-state example, which has three effective states and
binary Y, a decoder point moves out of the next optimum's hull.

## What this does not say

- **Not that binary Y suffices.** Proposition 5 needs X binary too. The
  four-state source of [CLAIM-387](../claims.d/CLAIM-387.md), with binary Y, is not refinable
  between β = 8 and β = 12 ([NOTE-981](../notes.d/NOTE-981.md)).
- **Not the Gaussian case.** The paper's Proposition 2, refinability of
  jointly Gaussian vectors for the Lagrangian problem, follows from Kline and
  Palmer's semigroup property of Gaussian bottlenecks, which was not read and
  is not re-derived.
- **Not that every pair of optima nests in the function case.** Refinability
  asks for some pair. The erasures are one family of optima, and the paper
  notes that it is "not very interesting: it is nothing more than an
  increasingly noisy version of Y". Other optima, such as deterministic
  partitions of Y's values, need not nest. In this case the Lagrangian path
  has only two points ([THEORY-743](THEORY-743.md), step 4), so the statement is about
  the primal problem.
- **Not more than two stages in the binary case.** The paper proves two
  stages. Composing the garblings would give more, but that is not claimed.
- **Not anything about block codes**, except through the paper's appeal to
  the operational equivalence ([THEORY-753](THEORY-753.md), Connections).

## Connections

- **[QUESTION-220](../questions.d/QUESTION-220.md): answers in part.** These are the structural
  conditions the question asked for, in the two finite cases where they are
  known. Both are narrow: X binary, or a bottleneck that only copies Y.
- **[THEORY-751](THEORY-751.md).** Equitz and Cover's Hamming case is the rate–distortion
  counterpart: refinable for every source. The log-loss analogue
  ([NOTE-980](../notes.d/NOTE-980.md)) is direct log-loss, which is case 1 with Y = X.
- **[THEORY-743](THEORY-743.md).** By its step 1, a source whose causal partition has
  two cells and binary Y reduces to case 2.
