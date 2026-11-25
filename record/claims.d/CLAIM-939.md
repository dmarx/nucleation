---
number: 939
status: Proposed
formerly:
- CLAIM-tmp8xj7x
title: 'Two-valued p(Y|x) gives nested IB optima'
statement: >-
  Information-bottleneck optima are nested at every pair of budgets whenever
  p(Y|x) takes at most two distinct values, for any finite Y: the region
  where F_β exceeds its convex envelope is a single interval, because r(1 −
  r) Σ_y Δ_y²/s_y(r) is concave, and that interval only widens as β grows
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: a finite joint distribution whose
  conditional p(Y|x) takes exactly two distinct values, and a pair of
  budgets λ₁ < λ₂, at which no information-bottleneck optimum at λ₁ is a
  garbling of an optimum at λ₂; or two rows a, b of a channel for which
  φ(r) = r(1 − r) Σ_y (b_y − a_y)²/((1 − r)a_y + r b_y) fails to be
  concave on (0, 1).
tags:
- information-theory
- mathematics
- learning-theory
date: '2026-11-22'
line:
- learned-structure
- formal-apparatus
answers:
- QUESTION-220
grounds:
- THEORY-757
- THEORY-753
- THEORY-743
complements:
- CLAIM-940
summary: >-
  Derived for [LEAD-039](../leads.d/LEAD-039.md) and checked numerically (scratch/studies/lead-039/;
  the study is [CASE-360](../cases.d/CASE-360.md)). It widens the binary case of [THEORY-757](../theory.d/THEORY-757.md)
  from X and Y both binary to any source whose causal partition has two
  cells, with Y of any finite size: the one step of that proof that used
  binary Y, that F_β is non-convex on a single interval, holds because a
  sum of harmonic-mean terms is concave. It is a structural condition on
  P(X, Y) of the kind [QUESTION-220](../questions.d/QUESTION-220.md) asks for, and [CLAIM-387](CLAIM-387.md)'s source shows
  it is sharp in the number of distinct rows: three rows with binary Y can
  fail. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-940 CASE-360 — new; filed with this claim from LEAD-039 -->

# CLAIM-939: Two-valued p(Y|x) gives nested IB optima

## The claim

**Setting.** X and Y finite, p(x) > 0. Bottlenecks, decoder points and
(λ₁, λ₂)-refinability are as in [THEORY-753](../theory.d/THEORY-753.md). Suppose the rows p(·|x) take
exactly two distinct values a ≠ b in Δ_Y. (One value means I(X; Y) = 0 and
every bottleneck is trivial.) Y may have any finite number of values.

**Theorem.** The problem is (λ₁, λ₂)-refinable for every 0 ≤ λ₁ ≤ λ₂: for
every pair of budgets there are bottlenecks T₁ at λ₁ and T₂ at λ₂ with
X → T₂ → T₁.

## Proof

**0. Reduce to binary X.** Let C ∈ {0, 1} be the cell of x (C = 1 where
p(·|x) = b), with P(C = 1) = p ∈ (0, 1). Averaging an encoder's rows within
each cell leaves the law of (T, Y) unchanged and does not raise I(X; T)
([THEORY-743](../theory.d/THEORY-743.md), step 1). So the information curve of (X, Y) is that of (C, Y),
and an encoder of C, composed with x ↦ C(x), is an encoder of X with the
same two informations. A chain C → T₂ → T₁ for (C, Y) composes to
X → T₂ → T₁. It is enough to prove the theorem for (C, Y).

**1. The curvature of F_β.** As in [THEORY-757](../theory.d/THEORY-757.md), write r = P(C = 1) for a
point of Δ_C = [0, 1], s(r) = (1 − r)a + rb ∈ Δ_Y, Δ = b − a, and
F_β(r) = H(s(r)) − h(r)/β in nats. Let Y⁺ = {y : Δ_y ≠ 0}; for y ∈ Y⁺,
s_y(r) > 0 on (0, 1). Then on (0, 1)

  F_β″(r) = (1 − βφ(r)) / (β r(1 − r)),  φ(r) = Σ_{y∈Y⁺} Δ_y² ψ_y(r),
  ψ_y(r) = r(1 − r)/s_y(r) = 1 / (a_y/r + b_y/(1 − r)).

If a_y, b_y > 0, ψ_y(r) = M(r/a_y, (1 − r)/b_y) with M(u, v) = uv/(u + v),
half the harmonic mean, which is concave on the positive quadrant; composed
with an affine map it is concave. If a_y = 0, ψ_y = (1 − r)/b_y, and if
b_y = 0, ψ_y = r/a_y, both affine. So **φ is concave on (0, 1)**. It is
also a rational function of r.

**2. The affine case is an erasure.** A term with a_y, b_y > 0 and
Δ_y ≠ 0 vanishes at both ends and is positive inside, so it is not affine.
If there is none, every y has a_y = b_y, a_y = 0 or b_y = 0, and with
m = Σ_{a_y = b_y} a_y the mass the rows share, φ ≡ 1 − m. Then F_{β} with
1/β = 1 − m is affine, so for every encoder
H(Y|T) − (1 − m)H(C|T) = H(Y) − (1 − m)H(C), that is,
I(Y; T) = (1 − m) I(C; T): Y is C erased with probability m. Every encoder
of C at budget λ ≤ H(C) with I(C; T) = λ is a bottleneck, and the erasures
of C ([THEORY-757](../theory.d/THEORY-757.md), case 1) nest at every pair of budgets.

**3. Otherwise the non-convex region is one interval.** If φ is not affine
it is not constant, so for each β the set {φ = 1/β} is finite and
J_β = {φ > 1/β}, the set where F_β″ < 0, is an open interval, possibly
empty, as a strict upper level set of a concave function. F_β″ ≥ 0 off J_β
with finitely many zeros, so F_β is strictly convex on each interval
disjoint from J_β. These are exactly the facts that [THEORY-757](../theory.d/THEORY-757.md)'s steps c
and d draw from its quadratic g. Its steps c to f then go through
unchanged:
- the set P(β) where F_β exceeds its lower convex envelope is a single open
  interval (u_β, v_β) containing J_β;
- if p ∈ P(β), the Lagrangian optimum is unique, with the two decoder
  points u_β and v_β; otherwise it is the trivial encoder, also unique;
- P(β₁) ⊆ P(β₂) for β₁ ≤ β₂ (the paper's Lemma A2, which holds for any
  channel: F_{β₁} = F_{β₂} − c h with c ≥ 0, and −c h is convex).

**4. Budgets.** For 0 < λ < H(C) the information curve has a supporting
line of slope 1/β at λ, any bottleneck at λ minimizes the Lagrangian at β,
and λ₁ < λ₂ gives β₁ ≤ β₂ ([THEORY-757](../theory.d/THEORY-757.md), step a). By step 3 the minimizer at
β is unique, so the bottleneck at λ is the canonical optimum at β, and
[u_{β₁}, v_{β₁}] ⊆ [u_{β₂}, v_{β₂}]. The fine decoder points are two distinct
points, hence affinely independent, so [THEORY-753](../theory.d/THEORY-753.md) step 4 gives the chain.
If λ₁ = 0, the trivial encoder is a garbling of anything. If λ₂ ≥ H(C),
take T₂ = C, which attains I(C; Y), and any bottleneck T₁ of (C, Y) at λ₁:
it is an encoder of C, hence a garbling of T₂. ∎

## What it adds, and what it does not say

- **Beyond [THEORY-757](../theory.d/THEORY-757.md).** That entry's case 2 needs X and Y both binary.
  Here Y is any finite alphabet, and X any finite alphabet whose rows of
  p(Y|x) take two values. The binary case is the instance |Y| = 2, where
  φ's concavity is [THEORY-757](../theory.d/THEORY-757.md)'s quadratic g. Whether Charvin, Catenacci
  Volpi and Polani or later work already state this extension was not
  checked: the record's reading of the paper ([NOTE-981](../notes.d/NOTE-981.md)) gives only the
  binary case.
- **Sharp in the number of rows.** [CLAIM-392](CLAIM-392.md)'s source has three distinct
  rows and binary Y, and its optima at β = 8 and 12 do not nest. So no
  condition on the size of Y alone, and no bound above two on the number
  of rows, suffices. [CASE-360](../cases.d/CASE-360.md) finds failures common among random
  three-row sources (uncertified).
- **Why two rows is special.** With two cells the decoder points live on a
  line through p(C), and the hull of an optimum is an interval around p(C)
  that can only grow. With three cells the decoder points live in a plane,
  and the non-convex region growing (step 3's last point, which holds in
  any dimension) does not stop the segment or triangle through p(X) from
  rotating, which is how [CASE-360](../cases.d/CASE-360.md)'s failures look.
- **Not more than two stages.** As in [THEORY-757](../theory.d/THEORY-757.md), the chain is proved for
  pairs; composing the garblings along an increasing sequence of budgets
  gives any number of stages, since each fine optimum here is the unique
  canonical one.
- **Products.** [CLAIM-940](CLAIM-940.md) shows refinability at every pair of budgets
  survives independent products, so sources built from independent
  two-row and function pairs nest too, with any number of distinct rows.
