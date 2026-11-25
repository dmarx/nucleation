---
number: 895
status: Proposed
formerly:
- CLAIM-tmpu482h
title: 'Under Contextuality-by-Default, pooling two noncontextual systems whose direct influences point opposite ways can give a contextual system, because pooling averages the correlations but cancels the signalling, so a test must analyse each counterbalancing cell as its own system'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  The construction fails: for the rank-4 cyclic systems it uses (each
  correlation 0.65 with an odd sign pattern, each content's marginal
  +0.075 in one of its contexts and -0.075 in the other, and the mirror
  system with the marginals reversed), either system is contextual, or
  their equal mixture is not, under the cyclic-system criterion of
  Contextuality-by-Default.
tags:
- contextuality
- mathematical-statistics
date: '2026-11-22'
line:
- pragmatic-transport
- formal-apparatus
grounds:
- LIT-777
- THEORY-177
complements:
- CLAIM-245
summary: >-
  Found while drafting [LEAD-182](../leads.d/LEAD-182.md)'s design, 2026-11-22. In a cyclic system
  the criterion is s_odd(E) − (n − 2) − Δ, with Δ the summed absolute
  marginal differences. Mixing averages E linearly but Δ only
  subadditively, and when two systems' influences are opposite, Δ of the
  mixture is zero while s_odd keeps its value: two systems at Δ_C = 0
  pool to Δ_C = 0.6 (scratch/studies/lead-182/test_cbd.py). Without
  signalling the opposite holds, since the contextual fraction is convex
  under mixing ([THEORY-165](../theory.d/THEORY-165.md)). So averaging over a counterbalanced factor,
  such as which character is named first, can manufacture contextuality,
  and [CASE-329](../cases.d/CASE-329.md) analyses each cell apart. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-329 — new; the design that applies this claim -->

# CLAIM-895: Under Contextuality-by-Default, pooling two noncontextual systems whose direct influences point opposite ways can give a contextual system, because pooling averages the correlations but cancels the signalling, so a test must analyse each counterbalancing cell as its own system

## The claim

Take a rank-4 cyclic system: contents q0 to q3, context k measuring q_k
and q_(k+1). Contextuality-by-Default calls it contextual exactly when

    Δ_C = s_odd(E) − 2 − Δ > 0,

where E_k is the mean product of the two ±1 answers in context k, s_odd
the largest signed sum of the E_k with an odd number of minus signs, and Δ
the sum over contents of the absolute difference between the content's
two marginal means ([LIT-777](../literature.d/LIT-777.md); [THEORY-177](../theory.d/THEORY-177.md) for what Δ measures).

**The construction.** System P1: every |E_k| = 0.65, signs (+, +, +, −),
so s_odd = 2.6; each content's marginal is +0.075 in one of its contexts
and −0.075 in the other, so Δ = 8 × 0.075 = 0.6 and Δ_C = 0. System P2:
the same correlations, every marginal reversed; again Δ_C = 0. Their equal
mixture has the same correlations, s_odd = 2.6, and every marginal 0, so
Δ = 0 and Δ_C = 0.6. Two systems on the noncontextual boundary pool to one
that is contextual by a wide margin. The check is
`test_pooling_label_orders_can_create_contextuality` in
scratch/studies/lead-182/test_cbd.py.

**Why.** E enters the criterion linearly, so mixing averages it. Δ enters
through absolute values, and |½(d1 + d2)| ≤ ½(|d1| + |d2|), with equality
only when the two differences agree in sign. Opposite influences cancel in
the mixture's Δ while the correlations they accompanied survive.

**Where it bites.** A counterbalanced design that pools its cells. If
which character is named first, or which answer is shown first, shifts
the marginals one way in one cell and the other way in the other, the
pooled system shows contextuality that neither cell has. Lo, Sadrzadeh
and Mansfield's design ([NOTE-2316](../notes.d/NOTE-2316.md)) avoids the question by never
eliciting marginals; a free-response design meets it. So the design for
[LEAD-182](../leads.d/LEAD-182.md) ([CASE-329](../cases.d/CASE-329.md)) fixes in advance that each counterbalancing cell
is analysed as its own system, and that pooling, if reported, is
reported only beside the per-cell results.

## What it does not say

- That pooled systems are generally contextual, or that any published
  result was produced this way. It says pooling can create the verdict,
  so a design must rule it out.
- Anything against the sheaf-theoretic measure for no-signalling models.
  There the contextual fraction is convex under mixing ([THEORY-165](../theory.d/THEORY-165.md)), so a
  mixture of noncontextual no-signalling models is noncontextual. The
  difference lies in how Contextuality-by-Default discounts signalling.
- Anything about recodings, which [CLAIM-245](CLAIM-245.md) treats. The two are
  companions: a recoding acts on each context's outcomes, and pooling on
  the population a context's statistics come from. Under either, the
  verdict depends on a choice that has to be fixed before the data.
