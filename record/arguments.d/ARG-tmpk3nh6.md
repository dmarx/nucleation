---
status: Proposed
title: "Mitzenmacher's survey supports the lognormal of pure multiplicative growth and a floor's power law in the form of a reflecting minimum, but states neither Kesten's additive term, nor the exponent equation, nor the conditions, so it corroborates the claim and does not ground it"
version: 1
form: source
grounds:
- THEORY-tmp23821
concludes:
- CLAIM-tmpiervv
tags:
- probabilistic-modeling
- complex-systems
date: '2026-11-21'
line:
- formal-apparatus
summary: >-
  CLAIM-tmpiervv grounded itself in Kesten (LIT-tmpx9axf), Mitzenmacher
  (LIT-tmpwdtfj) and THEORY-696. Read, Mitzenmacher gives the claim's
  lognormal half (§5) and a floor turning it into a power law (§5.1), but
  the floor is a reflecting minimum, not the additive term B of
  W' = AW + B, and the paper states neither E[A^κ] = 1 nor any condition.
  Its one worked example does satisfy the equation, at κ = 1. So it is
  independent evidence for the claim's shape, and moves from grounds to
  corroborates; the Kesten half still rests on Kesten, unread. The wording
  is the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-tmpiervv THEORY-tmp23821 — Proposed; the claim and the reading this argument joins -->
<!-- inactive-ok-file: LIT-tmpx9axf — Deferred; Kesten, registered and unread -->

# ARG-tmpk3nh6: Mitzenmacher's survey supports the lognormal of pure multiplicative growth and a floor's power law in the form of a reflecting minimum, but states neither Kesten's additive term, nor the exponent equation, nor the conditions, so it corroborates the claim and does not ground it

## The inference

CLAIM-tmpiervv: i.i.d. multiplicative growth gives a lognormal; the same
growth "with an additive floor" gives a stationary Pareto tail with κ
solving E[A^κ] = 1, even when E[log A] < 0. Read as a source,
THEORY-tmp23821 would carry both halves.

## Critical questions (source)

**Does the work say this, read in context?** The first half, yes: "if the
ln Fk are independent and identically distributed variables with finite
mean and variance, then asymptotically Xj will approach a lognormal
distribution" (§5, p. 236). The second half, in another form: "As long as
there is a bounded minimum that acts as a lower reflective barrier to the
multiplicative model, it will yield a power law instead of a lognormal
distribution. The theory of this phenomenon is more fully developed in
[Gabaix 99, Kesten 73]" (§5.1, p. 238). A reflecting minimum is not an
additive B: one stops X from falling below m, the other adds a positive
amount each step.

**Is it said within the scope the claim needs?** Not for the exponent. The
paper gives no equation for κ and no conditions. Its Champernowne example
(F = 1/2 with probability 2/3, 2 with probability 1/3) satisfies the
claim's equation: (2/3)·2^(−κ) + (1/3)·2^κ = 1 at κ = 1, which is its
Pr[X ≥ x] = m/x, and E[ln F] = −0.231 < 0, so it contracts in log terms
as the claim allows. The filer checked both by hand and by simulating the
chain with its floor (python3 -I). That is an instance the paper gives,
not a statement it makes.

**Does the claim lean on the reading for more than it holds?** By listing
it as a ground, yes: the claim's exponent and conditions come from Kesten,
whom the paper only cites. The paper corroborates the claim's three-way
account (entry, floor, both): its §8 names two of the routes, "once the
observation time is random or a lower boundary is put into effect".

## Verdict

LIT-tmpwdtfj moves from the claim's grounds to `corroborates` on
THEORY-tmp23821. The claim's "additive floor" is one kind of floor; a
reflecting barrier is another, and a dated note on CLAIM-tmpiervv says so.
