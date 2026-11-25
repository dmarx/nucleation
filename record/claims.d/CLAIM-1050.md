---
number: 1050
status: Proposed
formerly:
- CLAIM-tmp8nzk0
title: 'Weak anchoring shows compliance before adequacy'
statement: >-
  In the anchored model of a response and its co-adapting standard, after a
  transient the gap between them is a fixed small fraction of the response's
  distance from the independent target, about the anchoring rate over the
  sum of the adaptation rates, and that distance closes only at about the
  response's rate times that fraction, so a weakly anchored standard shows
  near-perfect measured compliance long before the response is adequate
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation or the check: parameters with α, β, κ > 0 for
  which, once the fast mode has decayed, |a − q| / |d − a| differs from
  |λ_s|/α, or the slow eigenvalue λ_s is not
  (−(α + β + κ) + √((α + β + κ)² − 4ακ))/2.
tags:
- control-theory
- society-and-governance
- mathematics
date: '2026-11-23'
line:
- readiness
- formal-apparatus
rests_on:
- CLAIM-1087
complements:
- CLAIM-342
summary: >-
  A gap fill ([ADR-137](../decisions.d/ADR-137.md)) for A50 §§4–5 of the exchange "Explain First Contact
  RL" (2026-11-23). A50 shows that anchoring the standard to an independent
  target d makes a = q = d stable, and that the unanchored system has a
  neutral mode; it does not say how fast the anchored system gets there, or
  what measured compliance shows on the way, which is what its "excellent
  measured compliance" depends on. Derived and checked with python3 -I.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---

<!-- inactive-ok-file: CLAIM-1087 — Proposed; the model this extends, and the claim on a wrong anchor -->

# CLAIM-1050: Weak anchoring shows compliance before adequacy

## The gap it fills

A50 §4 adds an anchor, q̇ = β(a − q) + κ(d − q), and stops at stability
([CLAIM-1087](CLAIM-1087.md)). §5 says "the discrepancy disappears rapidly while their
common position persists" for the unanchored model, and §4 that "Eventually
the system exhibits excellent measured compliance. Yet neither process
necessarily keeps the arrangement connected to independently justified
public demands." Neither says what the anchor buys, or how long measured
compliance and adequacy part company when the anchor is weak.

## The derivation

In deviations x = a − d, y = q − d the Jacobian is [[−α, α], [β, −β − κ]],
with s = α + β + κ and eigenvalues λ = (−s ± √(s² − 4ακ))/2. The slow one,
λ_s, is ≈ −ακ/(α + β) when κ is small against α + β; the fast one is
≈ −(α + β + κ). The neutral mode of the unanchored model becomes a slow
mode, at a rate proportional to κ.

Once the fast mode has decayed (time of order 1/(α + β)), the state lies on
the slow eigenvector. From the first row, −αx + αy = λ_s x, so
y = x(α + λ_s)/α and the gap a − q = x − y = −xλ_s/α. Hence

|a − q| = (|λ_s|/α) · |d − a| ≈ (κ/(α + β)) · |d − a|,

and |d − a| itself decays at |λ_s| ≈ α · κ/(α + β).

## The check

`python3 -I`, numpy, on 2026-11-23. Eigenvalues against the closed form at
(α, β, κ) = (1, 1, 0.05), (1, 0.25, 0.05), (0.5, 2, 0.1), (2, 2, 0.01),
(1, 1, 1): slow eigenvalues −0.02469, −0.03967, −0.01938, −0.00499, −0.38197,
against −ακ/(α + β) = −0.025, −0.04, −0.02, −0.005, −0.5 (the approximation
fails at κ = 1, as it should). Euler runs from a = 0, q = 0.2, d = 1, read
after 15/(α + β): the observed ratio |a − q|/|d − a| was 0.02469, 0.03967,
0.03875 and 0.38197, equal to |λ_s|/α to five places in each case. At
α = β = 1, κ = 0.05, the response first came within 0.01 of d at t ≈ 183,
while the fast mode's time scale is 0.5.

## What it shows

Measured compliance, the gap between response and standard, understates
inadequacy by the factor |λ_s|/α ≈ κ/(α + β). A standard that adapts quickly
to the respondent (large β) and is weakly anchored (small κ) reports
near-perfect compliance at every moment while the response's distance from
d closes slowly. Compliance measures adequacy only when κ is comparable to
α + β, that is, when the standard answers to the independent target at
least as strongly as to the respondent. This is the quantitative form of
A50's "self-confirming coordination" for the anchored case, and of
[CLAIM-342](CLAIM-342.md)'s point that what anchors a loop is evidence that does not pass
through it: here, the share of the standard's movement that comes from d.

## What it does not say

It is a linear two-variable model. It says nothing about an anchor that is
itself wrong ([CLAIM-1185](CLAIM-1185.md) holds that case) or that the respondent can
influence.

## Standing

Proposed, the assistant's.
