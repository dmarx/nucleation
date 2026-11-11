---
status: Proposed
title: 'Under one outcome kernel for both orders of two framings, a rendering''s observed order effect on an item exceeds the source''s by at most the sum of its two order-context distortions, so growth in the order effect bounds that distortion from below whatever kernel is used, while kernels fitted to the two orders separately bound nothing'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: distributions p_AB, p_BA on the source's
  outcomes, q_AB, q_BA on the target's and one Markov kernel K with
  TV(q_AB, q_BA) greater than TV(p_AB, p_BA) + TV(q_AB, K p_AB) +
  TV(q_BA, K p_BA); or the order effects the line studies shown not to
  be differences between the response distributions of the two orders,
  which is a premise it takes from its first premise.
tags:
- probabilistic-modeling
- mathematics
- translation
date: '2026-11-11'
line:
- pragmatic-transport
rests_on:
- CLAIM-231
- CLAIM-245
summary: >-
  [CLAIM-231](CLAIM-231.md) bounds the change in an observed order effect by the
  distortions of the two order-contexts under one outcome kernel, and
  [CLAIM-245](CLAIM-245.md)'s data-processing step says one kernel cannot raise the
  discrepancy between two contexts. Together, per item, the rendering's
  order effect in total variation is at most the source's plus the two
  distortions. So a rendering can lose an order effect while staying
  close in both orders, but cannot create or enlarge one by more than the
  distortion, and the growth is a lower bound on the distortion that needs
  no choice of kernel. The bound needs the same kernel for both orders: two
  kernels fitted order by order can each fit exactly while the rendering
  creates an order effect the source lacks. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-063 CLAIM-117 CLAIM-228 ADR-075 — Proposed; the theses this bears on, the measure it cites and the decision whose test it passes, open -->

# CLAIM-tmptimdb: Under one outcome kernel for both orders of two framings, a rendering's observed order effect on an item exceeds the source's by at most the sum of its two order-context distortions, so growth in the order effect bounds that distortion from below whatever kernel is used, while kernels fitted to the two orders separately bound nothing

## The claim

**Setting** ([CLAIM-231](CLAIM-231.md)'s). For one item, p_AB and p_BA are the source
responses after the two orders, q_AB and q_BA the rendering's, K one
Markov kernel from source to target outcomes, and ε_AB = TV(q_AB, K p_AB),
ε_BA = TV(q_BA, K p_BA). The order effect's size is TV(p_AB, p_BA) in the
source and TV(q_AB, q_BA) in the rendering.

**Derivation.** By the triangle inequality,
TV(q_AB, q_BA) ≤ ε_AB + TV(K p_AB, K p_BA) + ε_BA. By data processing, the
step [CLAIM-245](CLAIM-245.md) uses for one kernel applied in two contexts,
TV(K p_AB, K p_BA) ≤ TV(p_AB, p_BA). So

TV(q_AB, q_BA) ≤ TV(p_AB, p_BA) + ε_AB + ε_BA.

**Consequences.**

- A rendering within ε in both orders under one kernel cannot enlarge an
  item's order effect by more than 2ε. It can shrink it to nothing: a
  lossy K carries any order effect towards zero, which is [CLAIM-011](CLAIM-011.md)'s
  lossy limit at the level of outcomes.
- For every single kernel, max(ε_AB, ε_BA) ≥ [TV(q_AB, q_BA) −
  TV(p_AB, p_BA)] / 2. Growth in the observed order effect is a lower
  bound on the distortion that needs no choice of K. [CASE-065](../cases.d/CASE-065.md) says "the
  kernel K is assumed, not tested"; this bound, in the growth direction,
  needs none, though [CASE-065](../cases.d/CASE-065.md)'s correlations still give no total
  variation to apply it to.
- **One kernel is needed.** Let the source have no order effect,
  p_AB = p_BA = p = (.7, .2, .1), and let the rendering give q_AB = p and
  q_BA = σp, with σ the permutation exchanging the first and third
  outcomes. The kernels K_AB = identity and K_BA = σ fit both orders
  exactly, for every item if the same holds item by item, yet the
  rendering's order effect is 0.6 where the source's is 0. A kernel
  family fitted context by context, as the restated D_obs allows when the
  two orders are two contexts ([CLAIM-228](CLAIM-228.md)), carries no bound on order
  effects unless the two orders' kernels are tied.

Checked numerically (scratch script, numpy only): 20,000 random triples of
distributions and kernels with up to five outcomes gave no violation of
the inequality, and the permutation example gives order effects 0 and 0.6
with both per-order fits 0.

## What it bears on

[CLAIM-063](CLAIM-063.md) and [CLAIM-117](CLAIM-117.md) (Proposed) hold that how far framings interfere
can be part of what a rendering keeps. On observed responses and under
one kernel, keeping the interference within the distortion is only half
assured: the rendering cannot gain interference beyond it and can lose all
of it. [CLAIM-235](CLAIM-235.md) says order effects "are signalling in the CbD sense";
read so, the inequality is [CLAIM-245](CLAIM-245.md)'s "joint overlap discrepancy" not
rising under one kernel, made approximate.

## What it does not say

- That a rendering keeps an order effect: only that it cannot enlarge one
  by more than its distortion under one kernel.
- Anything about the sign of an effect measured as a correlation, which
  is not a total variation ([CASE-065](../cases.d/CASE-065.md)).
- Anything about sampling error, which, as [CLAIM-231](CLAIM-231.md) says, is outside the
  bound.

## Admission

Route: derivation ([ADR-075](../decisions.d/ADR-075.md), step 5). The steps are [CLAIM-231](CLAIM-231.md)'s triangle
inequality and [CLAIM-245](CLAIM-245.md)'s data-processing bound, applied to the two
order-contexts of one item. No entry states that a rendering's order
effect can grow by at most its distortion, that the growth bounds the
distortion for every kernel, or that per-order kernels void [CLAIM-231](CLAIM-231.md)'s
hypothesis; [CLAIM-231](CLAIM-231.md) assumes one K "the same for both orders" without
saying what is lost when it is not. Whether a short composition is
nontrivial is the owner's call. It passes no separating-case route, being
a derivation, and no realistic case can show it false short of an
arithmetic error.
