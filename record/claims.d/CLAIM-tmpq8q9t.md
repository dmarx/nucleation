---
status: Proposed
title: 'At the critical point of a lattice model the Fisher information about a relevant coupling of renormalization-group eigenvalue y grows with linear size L as L^(2y) when 2y exceeds the dimension d and only as L^d ln L when 2y = d; in the two-dimensional Ising model the field''s grows per spin as L^(7/4) and the coupling''s only as ln L, so critical sensitivity lies along the field and is not shared by every control parameter'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An exact computation of Var(M) and Var(E) at h = 0, K = K_c on
  periodic L × L Ising lattices, for L up to 10 or beyond, in which
  Var(M)/L² does not grow as L^(7/4) or Var(E)/L² does not grow as a
  multiple of ln L near (8/π) ln L; or an error in the finite-size
  scaling step that the singular part of ln Z is a function of g L^y, so
  that its second derivative in g grows as L^(2y). A model whose
  renormalized couplings do not scale linearly near the fixed point, or a
  first-order transition, is outside the claim.
tags:
- information-geometry
- natural-sciences
- complex-systems
date: '2026-11-21'
line:
- formal-apparatus
grounds:
- THEORY-777
- THEORY-742
- LIT-1299
uses:
- TERM-tmpt3vht
summary: >-
  Fills two gaps in the exchange "Rich Get Richer Power Laws". At A13 §6 A
  shows that Fisher information about an Ising field is Var(M) and says
  that at criticality "nearby external fields can become exceptionally
  distinguishable", without the finite-size scaling; at A19 §6 A says a
  critical system can "forget most of its microscopic details while
  remaining acutely sensitive to a small number of control parameters",
  reading the sensitivity from dξ/dt, which is not a Fisher quantity.
  Computed exactly by transfer matrix: per spin, the information about
  the field grows as L^(7/4) and about the coupling only as ln L, so the
  acute sensitivity is the field's. In general it is set by 2y against
  d. The wording is the assistant's (Claude, in this session); adopting
  it is the owner's call.
---
<!-- inactive-ok-file: THEORY-777 — Proposed reading, the decimated spectrum this complements -->
<!-- inactive-ok-file: TERM-tmpt3vht — filed by another drafter from the same exchange, Proposed -->
<!-- inactive-ok-file: CLAIM-tmp99m8g LEAD-tmpl5wxz — filed with this claim from the same exchange, Proposed or Open -->

# CLAIM-tmpq8q9t: At the critical point of a lattice model the Fisher information about a relevant coupling of renormalization-group eigenvalue y grows with linear size L as L^(2y) when 2y exceeds the dimension d and only as L^d ln L when 2y = d; in the two-dimensional Ising model the field's grows per spin as L^(7/4) and the coupling's only as ln L, so critical sensitivity lies along the field and is not shared by every control parameter

## The gaps it fills

A13 §6 derives, for P_h(x) ∝ exp(hM(x) − H₀(x)), that the Fisher
information about h is Var_h(M), exactly, since the family is
exponential in h. Then: "Near a conventional continuous critical point,
magnetization fluctuations become extremely large … nearby external
fields can become exceptionally distinguishable." How large, and against
what, it does not say.

A19 §6 differentiates ξ ∝ |t|^(−ν) to get dξ/dt ∝ |t|^(−ν−1) and
concludes: "**The system can forget most of its microscopic details while
remaining acutely sensitive to a small number of control parameters**",
so "a critical system's response to perturbations is highly
anisotropic". The derivative of the correlation length is not the
Fisher information about t, which is the variance of the energy, and the
two need not behave alike.

## The claim

Near a fixed point, the singular part of ln Z for a system of linear size
L is, to leading order, a function of the scaling variables g_i L^(y_i).
Its second derivative in a coupling g of eigenvalue y therefore grows as
L^(2y). The Fisher information about g is that second derivative plus an
analytic part of order L^d. So the total information about g grows as
L^(2y) when 2y > d, as L^d ln L when 2y = d, and only extensively, as
L^d, when 2y < d. Per site the excess is L^(2y−d), the same exponent the
record holds for the Fisher eigenvalues under decimation, b^(2y−d) per
step (THEORY-777).

In the 2D Ising model y_h = 15/8 and y_t = 1, so 2y_h − d = 7/4 = γ/ν and
2y_t − d = 0 = α/ν. Per spin, the information about the field grows as
L^(7/4); about the coupling K, Var(E)/N grows only as ln L, with the
exact amplitude (8/π) ln L ≈ 2.55 ln L from the logarithmic specific
heat. Both relevant directions stand out from the irrelevant ones, as
THEORY-777 and the note on LIT-1299 report, but by very different
amounts, and the ratio grows as L^(7/4)/ln L. "Acutely sensitive" is true
of the field, mildly of the temperature.

## Check

The assistant computed ln Z(K, h) exactly on periodic L × L lattices
with the row transfer matrix (2^L states), at K_c = ½ ln(1 + √2), and took
second differences with step 10⁻³ (a numpy script of this session, not
kept; the method is as stated). Per spin:

| L | Var(M)/N | Var(E)/N |
|---:|---:|---:|
| 4 | 12.18 | 4.03 |
| 6 | 24.96 | 5.13 |
| 8 | 41.39 | 5.90 |
| 10 | 61.20 | 6.49 |

A log–log fit of Var(M)/N over L = 6 to 10 gives slope 1.756 against
7/4. A fit of Var(E)/N against ln L over the same range gives slope 2.66
against the exact 8/π = 2.55, the difference within the finite-size
corrections expected at L ≤ 10. The ratio of the two rises from 3.0 at
L = 4 to 9.4 at L = 10.

## What it does not say

- Not that the coupling direction is insensitive: its information still
  exceeds the extensive background by a factor growing as ln L.
- Not that every critical point concentrates sensitivity in one
  direction: where both relevant eigenvalues exceed d/2 both grow as
  powers. The anisotropy is ordered by y.
- Not that this measures distinguishability from coarse data. It is the
  information in the full configuration; under decimation THEORY-777
  finds the two relevant directions kept and the rest lost, which is a
  different contraction (THEORY-742).
