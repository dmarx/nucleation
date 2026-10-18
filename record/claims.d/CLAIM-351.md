---
number: 351
status: Active
formerly:
- CLAIM-tmpf67p3
title: 'A zero aggregate gradient does not show that the demands it aggregates are reconciled: with positive weights it holds both when every demand''s own gradient vanishes and when nonzero gradients cancel, and in the second case no update improves them all to first order; even the first is only joint first-order stationarity, which a demand''s maximum or saddle also has'
version: 2
history:
- version: 2
  date: '2026-10-18'
  note: >-
    uses moves to TERM-tmp9p3s9, which supersedes TERM-060 after the owner's third review; the claim is unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction: that at θ = 0 the losses (θ − 1)² and
  (θ + 1)² have a direction that lowers both to first order, or that the
  equal-weight aggregate gradient there is not zero; or an error in the
  general step, a positive combination of gradients that vanishes while
  some update lowers every loss. Not defeated by aggregates that do
  separate the cases, such as a vector of per-demand losses, which are
  not the scalar the claim is about.
tags:
- loss-landscapes
- operations-research
- agency
date: '2026-10-18'
line:
- distributed-agency
- formal-apparatus
complements:
- CLAIM-060
- CLAIM-276
uses:
- TERM-tmp9p3s9
summary: >-
  A33 §5 of the exchange of 2026-10-17: "Zero aggregate gradient does
  not imply absence of frustrated demands." With L₁ = (θ − 1)² and
  L₂ = (θ + 1)² at θ = 0 ([CASE-115](../cases.d/CASE-115.md)), the equal-weight gradient is
  zero and the aggregate is at its global minimum, while each loss is 1
  and wants the opposite move. In general a vanishing positive
  combination of gradients is either every gradient zero or a
  certificate that no update improves them all, and the scalar cannot
  tell which. The sharp edge: it is a fact about a weighted sum, not
  about what a monitor reading it represents. A29's "the unity of the
  distress signal need not arise from the unity of the underlying
  causes" is the interpretive reading, kept apart in the body.
grounds:
- CASE-115
---
<!-- inactive-ok-file: TERM-060 — Superseded; named in the version 2 history as the term this claim moved from -->

# CLAIM-351: A zero aggregate gradient does not show that the demands it aggregates are reconciled: with positive weights it holds both when every demand's own gradient vanishes and when nonzero gradients cancel, and in the second case no update improves them all to first order; even the first is only joint first-order stationarity, which a demand's maximum or saddle also has

## The claim

A33 §5: "Zero aggregate gradient does not imply absence of frustrated
demands." Say demands i = 1, …, n with losses L_i are **jointly
stationary** at θ when every g_i = ∇L_i(θ) is zero: no demand has a
first-order improving direction. Say common first-order descent is
**infeasible** there when some g_i ≠ 0 and no direction lowers every L_i
([TERM-tmp9p3s9](../terms.d/TERM-tmp9p3s9.md), local form).

Three things are kept apart, and only the first two are about
derivatives:

- **Stationarity** describes derivatives: whether the g_i vanish.
- **Compatibility** describes the joint existence of acceptable
  outcomes: whether ⋂ A_i ≠ ∅ for the declared acceptance conditions
  ([CLAIM-347](CLAIM-347.md)). Common first-order descent is its local, linearized
  diagnostic for demands of the form "improve".
- **Satisfaction** describes whether the selected outcome meets the
  requirements.

Stationarity is neither necessary nor sufficient for satisfaction. Not
sufficient: a point where every g_i vanishes can be a maximum or a
saddle of some L_i. Not necessary: a demand stated as a threshold,
L(θ) = θ² ≤ 1, is satisfied at θ = 0.5, where L = 0.25 and ∇L = 1 ≠ 0.
Vanishing gradients are necessary only for unconstrained interior optima
of differentiable losses, which is a narrower proposition. (The first
filing called stationarity necessary for reconciliation; the owner's
second review corrected it.) The claim is therefore about what the
aggregate gradient can show, not about when demands are satisfied, and
the ordinal account ([CLAIM-347](CLAIM-347.md)) decides the latter.

**The construction** ([CASE-115](../cases.d/CASE-115.md)). L₁(θ) = (θ − 1)², L₂(θ) = (θ + 1)²,
θ ∈ ℝ. At θ = 0, g₁ = −2 and g₂ = 2. With weights ½, ½ the aggregate
gradient is ½(−2) + ½(2) = 0. The aggregate L = ½L₁ + ½L₂ = θ² + 1 is not
only stationary at θ = 0 but globally minimized there. Yet L₁ = L₂ = 1,
each is minimized elsewhere (at +1 and −1), and any d ≠ 0 lowers one to
first order and raises the other: g₁d = −2d and g₂d = 2d have opposite
signs. The demands are frustrated, not reconciled.

**The general step.** Let w_i > 0 and Σ w_i g_i = 0. Then either every
g_i = 0, or the nonzero g_i satisfy Σ λ_i g_i = 0 with λ_i = w_i / Σ_j w_j
over them, so 0 ∈ conv{g_i}. In the second case no d has g_iᵀd < 0 for
all i, since Σ λ_i g_iᵀd = 0. So a vanishing positive aggregate is
compatible with joint stationarity and with infeasible common descent, and nothing in the
aggregate gradient or the aggregate loss separates them. With a zero
weight it says less: if w₂ = 0, stationarity of the aggregate constrains
g₁ only, and demand 2 can be anything.

The converse case in A33 §5 is the same fact from the other side: if
endorsement weights task 1 heavily, the aggregate improves while task 2 is
sacrificed. "So aggregate optimization performance may conceal the
distribution of frustration among constituent objectives."

## The interpretive reading, not part of the claim

A29, before frustration replaced distress ([CLAIM-368](CLAIM-368.md)): "the unity of
the distress signal need not arise from the unity of the underlying
causes. Many independently generated problems can be summarized by one
regulatory alarm or evaluation channel." A33 §5 drew the same moral for a
monitor: "A scalar training metric could therefore function as an
illusory unifier of evaluative success", where the illusion "would belong
to an interpreter or self-model that treats aggregate stability as
evidence that all relevant demands have been reconciled". These say what
a reader of the scalar might wrongly infer. The demonstration says only
that the inference is invalid. Whether any organization's monitor makes
it is not shown. It is the learning-system case of [CLAIM-060](CLAIM-060.md) (an
encompassing success does not establish its constituents') and of
[CLAIM-276](CLAIM-276.md) (stability is no evidence of fidelity).

## What it does not say

- **That the learning objectives have interests.** A33: "the analogy must
  not be taken as a claim that learning objectives have interests or
  rights."
- **That a zero aggregate gradient indicates frustration.** It is
  compatible with both cases; per-demand gradients are needed to decide.
- **Anything beyond first order.** At a point where every g_i = 0 the
  demands may still be frustrated at second order or globally. In the
  construction the frustration is also global: L₁ + L₂ = 2θ² + 2 ≥ 2, so
  no θ makes both losses less than 1.
