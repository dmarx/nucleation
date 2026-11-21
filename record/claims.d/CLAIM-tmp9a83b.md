---
status: Proposed
title: 'Linear preferential attachment is itself balanced at a boundary, between the stretched-exponential tails of weaker attachment and the condensation of stronger, so rich-get-richer processes and criticality are not opposite routes to a power law: both reach one at a marginal point, and differ in what is balanced'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A growing-network or Yule-type model giving a power-law tail over an
  open range of attachment exponents α around 1, without a compensating
  ingredient tuned with it, so that linear attachment is not marginal; or
  an argument that the balance in criticality (offspring mean against
  extinction) and the balance in attachment (the kernel's exponent
  against linear) are not the same kind of thing, so that "both marginal"
  is a pun.
tags:
- complex-systems
- network-science
- probabilistic-modeling
date: '2026-11-21'
line:
- formal-apparatus
objects_to:
- CLAIM-tmp2k0r2
rests_on:
- CLAIM-tmpepx9m
- CLAIM-tmply70l
grounds:
- LIT-tmp959qu
- CASE-tmpi5vfh
summary: >-
  An objection to A's A8 §8 contrast ([CLAIM-tmp2k0r2](CLAIM-tmp2k0r2.md)), filling a gap the
  ledger of the exchange "Rich Get Richer Power Laws" names. A's own A1 §4
  table shows a power law only at α = 1, with a stretched exponential
  below and condensation above; the assistant's runs ([CLAIM-tmpepx9m](CLAIM-tmpepx9m.md))
  confirm both sides. So linear attachment is a marginal point, as
  R = 1 is for a cascade. What differs is what is balanced: a kernel's
  exponent against linearity, or reproduction against extinction. And in
  the attachment model the exponent is a ratio of two rates
  ([CLAIM-tmply70l](CLAIM-tmply70l.md)), which a balance sets. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
bears_on:
- QUESTION-tmp21jtb
---
<!-- inactive-ok-file: CLAIM-tmp2k0r2 CLAIM-tmpepx9m CLAIM-tmply70l CASE-tmpi5vfh — Proposed or new; the claim objected to and the claims and case this rests on, filed from the same exchange -->
<!-- inactive-ok-file: LIT-tmp959qu — Deferred; registered from this exchange and not read -->

# CLAIM-tmp9a83b: Linear preferential attachment is itself balanced at a boundary, between the stretched-exponential tails of weaker attachment and the condensation of stronger, so rich-get-richer processes and criticality are not opposite routes to a power law: both reach one at a marginal point, and differ in what is balanced

## The objection

A8 §8 ([CLAIM-tmp2k0r2](CLAIM-tmp2k0r2.md)) sets "advantage feeds on advantage" against
"dynamics … balanced at a boundary between qualitatively different
regimes". But A's own table at A1 §4 puts rich-get-richer at such a
boundary. With attachment ∝ k^α, α < 1 gives a stretched-exponential
tail, α > 1 condensation onto one unit, and only α = 1 a power law
(Krapivsky, Redner and Leyvraz, [LIT-tmp959qu](../literature.d/LIT-tmp959qu.md), unread). The assistant's
simulations ([CLAIM-tmpepx9m](CLAIM-tmpepx9m.md)) show both sides. At α = 0.5 the largest of
100,000 nodes has degree 42. At α = 1.5 one node holds 99,354 links and the
next 12. A power law appears only at the boundary, just as a cascade's
law s^(−3/2) appears only at R = 1 ([CASE-tmpi5vfh](../cases.d/CASE-tmpi5vfh.md)).

So the two are not opposites in the respect A names. Both are tuned to a
marginal point between a regime with a characteristic scale and a regime
with a macroscopic winner. That is a giant cluster, or a condensate. The
parallel runs further:

| | below the boundary | at it | above it |
|---|---|---|---|
| cascade, mean offspring R | cutoff s_c ≈ 2/(1 − R)^2 | s^(−3/2) | positive chance of no end |
| attachment, kernel k^α | stretched exponential | k^(−3) | one node takes almost all |

## What does differ

What is balanced. In the cascade, reproduction balances extinction. In
attachment, the kernel's growth with k is exactly proportional. That
proportionality makes each unit's growth exponential in logarithmic
time, and entry turns that into a Pareto tail. The exponent, 2 for the
survival function, is then the ratio of the entry rate to the growth
rate ([CLAIM-tmply70l](CLAIM-tmply70l.md)). So in both, a power law comes from a balance of
two rates. The difference A points to, a privileged unit against an
unprivileged event, is real. It is a difference in *what* becomes
extreme, which A3 §3 already draws (entities against events), and not a
difference in how the scale is removed.

## What it does not say

- Not that the power law in attachment is fragile in every respect. A
  shifted linear kernel k + a keeps a power law and moves its exponent
  (a standard result, not checked here), so the boundary is a line in a
  larger space of kernels, not a point.
  The claim is that the exponent of k must be one.
- Not that the two mechanisms share a universality class or exponent.
- Not an answer to what fixes the exponents ([QUESTION-tmp21jtb](../questions.d/QUESTION-tmp21jtb.md)), though it
  bears on it.
