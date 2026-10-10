---
status: Active
title: 'On observed responses, a rendering that keeps the response distribution of each order of two framings within ε of the source''s, under an outcome correspondence, keeps the observed order effect within 2ε, a bound identified from data, while the intertwining identity bounds it only through defects of an unidentified state model'
version: 1
role: thesis
defeated_if: >-
  A pair of order-contexts on which the inequality fails, which would show
  the derivation wrong; or the order effects the line studies are shown
  not to be differences between the response distributions of the two
  orders.
tags:
- mathematics
- probabilistic-modeling
date: '2026-10-10'
line: pragmatic-transport
complements:
- CLAIM-063
- CLAIM-117
uses:
- TERM-043
summary: >-
  The record's repair, on 2026-10-10, after [CLAIM-tmpvmzx9](CLAIM-tmpvmzx9.md). The commutator
  identity of the manuscript's §9 holds, and its defects are not
  identified from data, by the objection's hidden-bit construction. What
  can be estimated is the response distribution under each order, so the
  bound is restated on those: a special case of observational distortion
  with contexts indexed by framing order. Active, because it is
  elementary and checkable. It does not say the state-model account is
  wrong, and it does not identify the defects.
illustrated_by:
- CASE-tmpkhubu
---
<!-- inactive-ok-file: CLAIM-063 CLAIM-117 — Proposed; the commutator thesis and the dynamics thesis this restates on observations, cited as open -->
<!-- inactive-ok-file: CLAIM-tmpeqvy4 — Proposed; the procedure-level measure that fixes the kernel across items, cited as open -->

# CLAIM-tmpfzcik: On observed responses, a rendering that keeps the response distribution of each order of two framings within ε of the source's, under an outcome correspondence, keeps the observed order effect within 2ε, a bound identified from data, while the intertwining identity bounds it only through defects of an unidentified state model

## What it answers

This is the record's reply of 2026-10-10 to [CLAIM-tmpvmzx9](CLAIM-tmpvmzx9.md), which the record
concedes. The objection is right on both counts. The intertwining defects
E_A = ΦA − A′Φ and E_B = ΦB − B′Φ act on interpretive states, and its
hidden-bit construction gives two models with the same observations and
defects 0 and 1, so the defects are not a function of the data. And the
identity reaches observed order effects only through a readout
correspondence it does not name. The reply restates the bound on what is
observed. It is decisive and checkable: the derivation below is a few
lines of the triangle inequality.

## The claim

**Setting.** Two framings A and B are given in either order, and a later
question is asked. The observed responses are two distributions on the
source's outcome set: p_AB after one order and p_BA after the other. In the
state model of manuscript §9 they would be O A B μ and O B A μ, but nothing
below uses the model. The observed order effect is the signed difference

Δ^o = p_AB − p_BA.

For the rendering, the same design gives q_AB and q_BA on the target's
outcome set, and Δ^t = q_AB − q_BA. Let K be a Markov kernel from source
outcomes to target outcomes, the outcome correspondence [CLAIM-tmpvmzx9](CLAIM-tmpvmzx9.md)
names, the same for both orders. Write TV(p, q) = ½‖p − q‖₁.

**Hypothesis.** TV(q_AB, K p_AB) ≤ ε and TV(q_BA, K p_BA) ≤ ε. These are the
observational distortions of the two order-contexts, so the hypothesis is
that the rendering has observational distortion at most ε in each.

**Bound.** K acts linearly on signed measures, so K Δ^o = K p_AB − K p_BA.
Then

Δ^t − K Δ^o = (q_AB − K p_AB) − (q_BA − K p_BA),

and by the triangle inequality for the norm ½‖·‖₁,

½‖Δ^t − K Δ^o‖₁ ≤ ½‖q_AB − K p_AB‖₁ + ½‖q_BA − K p_BA‖₁
= TV(q_AB, K p_AB) + TV(q_BA, K p_BA) ≤ 2ε.

So the target's order effect differs from the transported source order
effect by at most 2ε. No state space, no Φ and no readout defect enters.
Every quantity is a response distribution or a kernel between response
sets, so the bound is stated in quantities the data identify.

**A worked check.** Let both outcome sets be {yes, no}, K the identity,
p_AB = (0.7, 0.3), p_BA = (0.4, 0.6), so Δ^o = (0.3, −0.3). Let
q_AB = (0.6, 0.4) and q_BA = (0.45, 0.55). Then TV(q_AB, p_AB) = 0.1 and
TV(q_BA, p_BA) = 0.05, so ε = 0.1 serves. Δ^t = (0.15, −0.15), and
Δ^t − Δ^o = (−0.15, 0.15), with ½‖·‖₁ = 0.15 ≤ 0.2 = 2ε, and indeed
≤ 0.1 + 0.05.

**It is observational distortion.** The bound is a special case of D_obs
([TERM-043](../terms.d/TERM-043.md)), with the contexts indexed by framing order. It inherits
[CLAIM-tmp6xxbf](CLAIM-tmp6xxbf.md)'s caveat: if K is chosen freely for one pair it can be
constant, and a constant K sends every Δ^o to zero, so the bound then says
nothing about the source. K is to be fixed across items, as
[CLAIM-tmpeqvy4](CLAIM-tmpeqvy4.md) requires.

**The identity stays as an explanation.** Under a state model the
commutator identity of [CLAIM-117](CLAIM-117.md) explains why a transport that intertwines
each framing would keep the order effect, and [ARG-006](../arguments.d/ARG-006.md)'s algebra stands.
But its defects are identified only given a result the record does not
have, such as a minimal-realization theorem under which observationally
equivalent models leave the defect norms fixed ([CLAIM-tmpvmzx9](CLAIM-tmpvmzx9.md)'s second
answer).

## What it does not say

- It does not say the state-model account is wrong, or identify its
  defects.
- It does not say order effects are the whole of the dynamics. Longer
  sequences of framings are further contexts, and the same bound holds
  term by term.
- It does not choose ε or K. Those are fixed by design and estimated, and
  their estimation error is not in the bound.

## Note of 2026-10-10: a documented case

[CASE-tmpkhubu](../cases.d/CASE-tmpkhubu.md), found by a search the owner asked for, gives this bound a
documented illustration and a practical resolution. Haberstroh et al.
(2002) gave two satisfaction questions, in German and in a back-translated
Chinese version, in both orders; the part–whole correlation's order effect
is about +.25 in the German administration and about −.14 in the Chinese,
with the life-first order nearly kept (.53 against .50) and the
academic-first order not (.78 against .36). That is the bound's
contrapositive in kind, with the distortion localised to one order-context.
It does not supply an ε: only correlations are reported, so the inequality
cannot be checked on it, and language and readership change together.

The resolution comes from Moore's Clinton–Gore poll, read through [LIT-834](../literature.d/LIT-834.md).
Its order effect is about 0.095 in total variation, and sampling alone puts
about 0.03 to 0.04 into each order's estimated ε at n ≈ 450, so 2ε is about
0.05 to 0.08 before any distortion: as large as the effect it would
certify. At poll sizes the bound cannot certify that a rendering keeps an
order effect of that size; roughly ten times the respondents per order and
version would be needed. This is a fact about estimation, which "What it
does not say" already sets outside the bound, and it does not touch the
derivation.
