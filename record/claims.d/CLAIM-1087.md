---
number: 1087
status: Proposed
formerly:
- CLAIM-tmpep410
title: 'Co-adapting standard converges to no target'
statement: >-
  When a response adapts toward its evaluative standard and the standard
  adapts toward the response, their gap closes at the sum of the two rates
  while a weighted mean of the two is conserved, so both converge to a point
  fixed by their initial conditions and not by any independent target; a
  pull of the standard toward an independently grounded target makes that
  target the stable equilibrium
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: a choice of positive rates for which the gap
  does not decay at α + β, the weighted mean (βa + αq)/(α + β) moves, or,
  with κ > 0, a = q = d is not the unique asymptotically stable equilibrium.
  A showing that real standards and responses do not adapt this way bears on
  its use (CLAIM-1053), not on it.
tags:
- control-theory
- society-and-governance
- mathematics
date: '2026-11-23'
line:
- readiness
- formal-apparatus
complements:
- CLAIM-342
- CLAIM-297
summary: >-
  A50 §§4 and 5 of the exchange "Explain First Contact RL" (ChatGPT,
  2026-11-23), its "surprisingly revealing toy model": ȧ = α(q − a),
  q̇ = β(a − q), and the anchored variant q̇ = β(a − q) + κ(d − q). A50
  derives the gap's decay, the conserved mean and the anchored equilibrium;
  the assistant rechecked each with python3 -I. A50 reads it as
  "self-confirming coordination" ([CLAIM-1053](CLAIM-1053.md)). The wording is A's
  (ChatGPT, at A50 of the exchange "Explain First Contact RL"); adopting it
  is the owner's call.
---

<!-- inactive-ok-file: CLAIM-1053 CLAIM-1050 — Proposed; A50's reading of this model and the assistant's rates for its anchored form, filed with it -->

# CLAIM-1087: Co-adapting standard converges to no target

## The model

A50 §4: let a(t) be an organization's current response and q(t) "the
standard against which that response is evaluated", with

- ȧ = α(q − a), the response adapting toward the standard;
- q̇ = β(a − q), the standard adapting "toward what the organization
  currently produces".

## The results

1. The gap e = a − q obeys ė = −(α + β)e, so it decays exponentially.
2. c = (βa + αq)/(α + β) has ċ = 0, so a and q "converge to the initial value
   of c". "The common outcome is determined by their initial conditions, not
   by any independent measure of what the organization ought to accomplish."
3. The Jacobian has eigenvalues 0 and −(α + β) (A50 §5): a neutral mode, the
   shared value, and a fast mode, the disagreement.
4. With an independently grounded target d, q̇ = β(a − q) + κ(d − q): "For
   positive α and κ, the fixed-d equilibrium is a = q = d, and it is
   asymptotically stable in this linear model."

## The check

Rechecked by the assistant on 2026-11-23 with `python3 -I` and numpy:

- (1) and (2) as identities at 1,000 random parameter and state draws, the
  largest residual 7 × 10⁻¹⁵;
- (3) at α = 1.3, β = 0.4, eigenvalues 0 and −1.7, and an Euler run from
  a = 0, q = 0.6 ending at 0.45882, against c(0) = 0.45882;
- (4) the anchored Jacobian [[−α, α], [β, −β − κ]] has trace −(α + β + κ) < 0
  and determinant ακ > 0, so both eigenvalues have negative real part
  whenever α, κ > 0 (confirmed at 1,000 random draws); setting ȧ = 0 gives
  a = q, and then q̇ = 0 gives q = d.

The derivation is A50's and correct. β plays no part in the stability
condition, and α must be positive: a response that does not adapt is not
moved by an anchor placed on the standard. How fast the anchored system
reaches d, and what measured compliance shows meanwhile, is [CLAIM-1050](CLAIM-1050.md).

## Where the record stands

[CLAIM-342](CLAIM-342.md) says what keeps a judgement–observation loop from confirming
itself is evidence that does not pass through the interpretation it tests;
this is a two-variable instance with the anchor as that evidence. [CLAIM-297](CLAIM-297.md)
shows an interpretive advantage amplified with no gain in fidelity in the
meaning–influence model; here nothing is amplified, and the fidelity lost
is to d, never consulted.

## Standing

Proposed, in A's voice; demonstrated, as checked.
