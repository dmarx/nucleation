---
status: Proposed
title: 'Making a difference matter costs a separating budget'
statement: >-
  A23's consequentiality threshold κ_ε(x, x′), the least cost of a
  realizable witness under which the difference between x and x′ produces
  an outcome difference of at least ε, is the least budget at which A23's
  budgeted consequential difference D_B(x, x′) reaches ε, when the witness
  family at budget B is the witnesses costing at most B; so it is the
  record's separating budget (CLAIM-570, CLAIM-968) for outcome
  distinctions, and it is not a distance: it is infinite for identical or
  never-separated configurations, fails the triangle inequality, and
  satisfies only the reverse bound min(κ_{ε/2}(x, y), κ_{ε/2}(y, z)) ≤
  κ_ε(x, z)
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: with W_B the witnesses costing at most B and
  D_B the supremum of the outcome distance over W_B, a pair for which the
  least cost of an ε-separating witness differs from the least B with
  D_B ≥ ε when both are attained; or a triple violating the reverse bound.
  Witness families that are not indexed by a cost, or whose supremum is
  not attained, are outside it.
tags:
- mathematics
- individuation
- information-theory
date: '2026-11-26'
line:
- realizability
- formal-apparatus
rests_on:
- CLAIM-570
- CLAIM-574
complements:
- CLAIM-968
uses:
- TERM-tmp8nuak
summary: >-
  A gap fill (ADR-137) for A23 §4 of the exchange "Alignment consequences
  brainstorm" (ChatGPT, 2026-11-26), which defines κ_ε(x, x′) =
  inf_w {c(w) : Δ_w(x, x′) ≥ ε} and says "This gives us a geometry quite
  different from conventional transition distance", asking "How much
  capacity is required to establish circumstances in which the difference
  between x and x' matters?" It is different from a transition distance;
  it is also not a new geometry beside A23's own D_{B,T}: it is that
  quantity's level-set inverse, and the record holds it for observing
  budgets as the least budget that separates two states. It ranks pairs
  the other way round from a distance. Checked with python3 -I. The
  wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-968 SYNTHESIS-040 TERM-tmp8nuak — Proposed; filed, registered or cited in the filing of 2026-11-26 from the exchange "Alignment consequences brainstorm" -->

# CLAIM-tmpik3z0: Making a difference matter costs a separating budget

## The gap

A23 §3 defines, for a probe p in context g, Δ_{g,p}(x, x′) =
d_Y(F_g^p(x), F_g^p(x′)), and over "a family of admissible witness
contexts and probes attainable from the current organization within
budget B and time T", D_{B,T}^g(x, x′) = sup Δ_{h,p}(x, x′), noting that
"For fixed common witness families and a metric on comparable outcomes,
this construction gives a pseudometric". That is right: a supremum of
pseudometrics is one, and A23 rightly ties it to CLAIM-574's
resource-bounded profiles. A23 §4 then defines κ_ε as a separate
"consequentiality threshold" and contrasts it with "Nucleation's existing
transition threshold". It does not relate κ_ε to D, and does not say
what kind of quantity κ_ε is.

## The derivation

Let each witness w have a cost c(w) and an outcome difference Δ_w(x, x′),
let W_B = {w : c(w) ≤ B} and D_B = sup_{w∈W_B} Δ_w.

1. **κ is D's inverse.** If some w with c(w) ≤ B has Δ_w ≥ ε, then
   D_B ≥ ε; conversely, if D_B ≥ ε and the supremum is attained, some
   w ∈ W_B has Δ_w ≥ ε. So κ_ε(x, x′) = min{B : D_B(x, x′) ≥ ε}: the
   budget at which the pair first separates by ε. D_B is nondecreasing in
   B, so this is a threshold in the sense of CLAIM-968, and for an
   observing budget it is CLAIM-570's "least observing budget that
   separates two mutually reachable states".
2. **Not a distance.** κ_ε(x, x) = ∞, since no witness separates a
   configuration from itself, and κ_ε is large for pairs that are hard to
   tell apart and small for pairs that are easy: it orders pairs as a
   similarity does. It fails the triangle inequality: three
   configurations x, y, z with y cheaply separated from both and x, z
   never separated give κ(x, z) = ∞ > κ(x, y) + κ(y, z).
3. **What it satisfies instead.** Since D_B is a pseudometric, D_B(x, z) ≥
   ε forces D_B(x, y) ≥ ε/2 or D_B(y, z) ≥ ε/2. So
   min(κ_{ε/2}(x, y), κ_{ε/2}(y, z)) ≤ κ_ε(x, z): if a difference can be
   made to matter at some cost, one of its two halves can be made to
   matter half as much at no greater cost.

**Check (python3 -I).** 2,000 random families of eight witnesses with
costs uniform on [0, 10] and integer outcome maps on four
configurations: κ_ε equalled the least budget with D_B ≥ ε in all 48,000
ordered pairs (ε = 1, 2); the triangle inequality failed for κ in 15,126
ordered triples; the reverse bound failed in none; D_B satisfied the
triangle inequality in every triple at B = 3 and 7.

## What follows

- A23's two constructions are one object read two ways: D fixes a budget
  and asks how far apart, κ fixes a margin and asks at what budget. The
  "geometry" is the filtration of equivalences x ∼_B x′ (D_B = 0) that
  refine as B grows, which CLAIM-574 holds for probes and SYNTHESIS-040
  for observing against acting budgets.
- What A23 adds to the record is the witness family: probes "that become
  available through attainable organizational development", not only
  probes now affordable. That changes what B buys, not the mathematics.
  TERM-tmp8nuak keeps the condition this needs: the witness must be
  common to x and x′, which holds when the developing party is the one
  to whom the difference matters, not the system whose configurations x
  and x′ are.

## What it does not say

- That separating outcomes shows the difference causes them. A23 §3
  says so itself: "Establishing that the focal difference *causes* the
  outcome difference requires appropriately controlled interventions".
