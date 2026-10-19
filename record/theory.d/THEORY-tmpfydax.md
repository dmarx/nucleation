---
status: Active
title: 'In the hyperbolic plane, a root carrying deg_max ≥ 15 chains of length m, embedded with worst-case distortion 1 + ε for ε ≤ 1, forces some node to hyperbolic distance at least (ℓ/(4ε))·ln(deg_max/(π√2)) from the origin, so fixed-point Poincaré coordinates need Ω((ℓ/ε) log deg_max) bits'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-196 and filed Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-196.yaml, batch 012, ADR-047).
    THEORY-196's promote_when asked first for "a complete proof of the
    lower bound, without the small-angle substitution taken as an
    equality". LIT-874's Lemma D.1, followed in NOTE-679, uses that
    substitution. The proof below is the record's own, by exact hyperbolic
    trigonometry, with explicit constants, and it was checked numerically.
    Under ADR-047 v2 (the owner's rule of 2026-10-19), a step-by-step
    re-derivation meets the condition. THEORY-196 keeps the matching upper
    bound, which rests on Sarkar's construction, and extends this one.
tags:
- representation-learning
- mathematics
date: '2026-10-19'
source:
- LIT-874
summary: >-
  Sala, De Sa, Gu and Ré (2018), [LIT-874](../literature.d/LIT-874.md), Lemma D.1, read in [NOTE-679](../notes.d/NOTE-679.md), with
  the proof redone here without the paper's small-angle approximation.
  Only the root's children are used to fix the embedding's scale c, and
  then the chains turn the scale into depth. Plane only, one family of
  trees, fixed-point coordinates in the Poincaré disk, deg_max ≥ 15 and
  ε ≤ 1. It says nothing about H^r for r > 2, or about whether any tree
  needs fewer bits under another number system.
extended_by:
- THEORY-196
---
<!-- inactive-ok-file: THEORY-196 — Proposed; the account this was split from and that extends it, cited as open -->

# THEORY-tmpfydax: In the hyperbolic plane, a root carrying deg_max ≥ 15 chains of length m, embedded with worst-case distortion 1 + ε for ε ≤ 1, forces some node to hyperbolic distance at least (ℓ/(4ε))·ln(deg_max/(π√2)) from the origin, so fixed-point Poincaré coordinates need Ω((ℓ/ε) log deg_max) bits

## Source

Sala, De Sa, Gu and Ré (2018), [LIT-874](../literature.d/LIT-874.md), read in [NOTE-679](../notes.d/NOTE-679.md): §3.2 (bits per
distance) and Lemma D.1 (the lower bound for the chain graph G_m). The
statement is the paper's, up to constants. The proof below is the
record's: the paper's proof replaces √(2(1 − cos θ)) by θ as an equality
and passes over "some algebra".

## What was actually shown

Let G_m be a root with k = deg_max chains of length m, so the longest path
is ℓ = 2m. Let f embed G_m in H² with worst-case distortion at most 1 + ε,
ε ≤ 1. Write c for the minimum contraction, so that
c·d_T(u, v) ≤ d_H(f(u), f(v)) ≤ (1 + ε)c·d_T(u, v).

1. The root's children a_i satisfy r_i = d_H(f(root), f(a_i)) ∈ [c, (1 + ε)c],
   and d_H(f(a_i), f(a_j)) ≥ 2c.
2. Let θ be the angle at f(root) between a_i and a_j. The hyperbolic law of
   cosines can be rewritten exactly as
   cosh d = cosh(r_i + r_j)·sin²(θ/2) + cosh(r_i − r_j)·cos²(θ/2),
   using cosh(a ± b) = cosh a cosh b ± sinh a sinh b. So
   sin²(θ/2) = (cosh d − cosh(r_i − r_j))/(2 sinh r_i sinh r_j).
3. Since |r_i − r_j| ≤ εc ≤ c and r_i, r_j ≤ (1 + ε)c,
   sin²(θ/2) ≥ (cosh 2c − cosh c)/(2 sinh²((1 + ε)c)).
4. Order the k children by angle around f(root). The gaps sum to 2π, so some
   pair has θ ≤ 2π/k, and then sin(θ/2) ≤ π/k.
5. If c ≤ ln 4, the bound in step 3 is at least the minimum of
   (cosh 2c − cosh c)/(2 sinh² 2c) on (0, ln 4], which is 0.0465 (at c = ln 4).
   So sin(θ/2) ≥ 0.2156 for every pair, against step 4 once k ≥ 15. Hence
   c > ln 4.
6. For c > ln 4, cosh 2c − cosh c ≥ e^(2c)/4 and 2 sinh²x ≤ e^(2x)/2, so
   sin²(θ/2) ≥ e^(−2εc)/2. With step 4, εc ≥ ln(k/(π√2)).
7. The leaf of any chain is at tree distance m from the root, so
   d_H(f(root), f(leaf)) ≥ cm ≥ (ℓ/(2ε))·ln(k/(π√2)). One of the two points
   is therefore at distance D ≥ (ℓ/(4ε))·ln(k/(π√2)) from the origin.
8. In the Poincaré disk ‖x‖ = tanh(D/2), so 1 − ‖x‖ = 2/(e^D + 1) exactly.
   Writing x in fixed point so that 1 − ‖x‖ does not round to zero takes
   log₂((e^D + 1)/2) ≥ D/ln 2 − 1 bits, which is at least
   (ℓ/(4ε ln 2))·ln(k/(π√2)) − 1.

**Checked numerically.** Over 2×10⁵ random configurations satisfying
step 1, sin²(θ/2) never fell below the bound in step 3. The step-5
minimum and the step-6 inequality were checked on grids.

What could have failed: the scale c could have been free, as it is for a
path, which embeds isometrically at any scale. It is not, because k
children must fit around the root at mutual distance 2c, and that is what
the log deg_max term records.

## What this does not say

- **Not the upper bound.** That a distortion-(1 + ε) embedding exists with
  O((ℓ/ε) log deg_max) bits is Sarkar's construction, which neither
  record holds. It stays with [THEORY-196](THEORY-196.md).
- **Not beyond the plane.** In H^r, r > 2, more children fit around a node
  at a given angle, so step 4 changes. No lower bound there is held.
- **Not for trees of small degree.** For k ≤ 4, ln(k/(π√2)) ≤ 0 and the
  bound says nothing. For 5 ≤ k ≤ 14 the proof's case split does not
  close. The constant 15 is an artefact of step 5, not a threshold in the
  geometry.
- **Not about information.** The cost is that of fixed-point coordinates
  in the Poincaré disk. A tree is a list of edges in O(n log n) bits.
- **Not for every tree.** It is one family, chosen to need many bits.
  That is all a lower bound for "trees" needs.
