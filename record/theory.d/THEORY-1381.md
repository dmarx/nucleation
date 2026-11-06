---
number: 1381
status: Active
formerly:
- THEORY-tmp960op
title: 'Foschi, Hull and Ku give closed-form equations in the tangents of half the folding angles, one for opposite and one for adjacent folding angles, that describe the full configuration space of any degree-4 rigid origami vertex, Euclidean or non-Euclidean, as two folding modes, the two branches of a square root, which meet at the flat state of a developable vertex and cannot meet there when the sector angles do not sum to 2π; the arXiv copy prints the opposite-angle equation with two signs wrong'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Narrowed and promoted at the thirtieth status review (ADR-065, ADR-047),
    at the coordinator's ruling under the owner's delegation. The title was:
    "Foschi, Hull and Ku give closed-form equations in the tangents of half
    the folding angles that describe the full configuration space of any
    degree-4 rigid origami vertex, Euclidean or non-Euclidean, as two
    folding modes, which meet at the flat state of a developable vertex and
    are disconnected when the sector angles do not sum to 2π".

    The last clause is the source's generalization from one example (§V B).
    It holds only when no crease may pass ±π, and it moves to THEORY-tmp0i15x,
    which extends this entry and keeps the old condition (kind 1). The title
    now also records the misprint in Eq. 4, which the old title had asserted
    as describing the configuration space (kind 3, dated note).

    The promote_when was: "The derivation in Appendix A checked, or the
    equations verified numerically against the closure condition for random
    degree-4 vertices of all three types, together with a check that the two
    folding modes meet only at the flat state of a developable vertex and
    are disjoint when the sector angles do not sum to 2π." For the narrowed
    title it is met. The source was read in full (NOTE-1606, Read), and the
    equations were checked by scratch/formal/foschi_deg4_check.py,
    foschi_eq4_search.py and foschi_closure_check.py, second-checked by the
    coordinator on 2026-11-06.
tags:
- mathematics
date: '2026-11-05'
source:
- LIT-2055
summary: >-
  Foschi, Hull and Ku (2022), [LIT-2055](../literature.d/LIT-2055.md), read in full in [NOTE-1606](../notes.d/NOTE-1606.md) from the
  arXiv source of v2, with the equations checked numerically against an
  independent construction. Active as a report of what the paper derives,
  with its three misprints corrected below. Degree 4 only. The wider claim,
  that the modes are disconnected whenever the sector angles do not sum to
  2π, is held Proposed in [THEORY-tmp0i15x](THEORY-tmp0i15x.md), which extends this one.
---
<!-- inactive-ok-file: THEORY-tmp0i15x — Proposed; the wider clause this narrowing set aside -->

# THEORY-1381: Foschi, Hull and Ku give closed-form equations in the tangents of half the folding angles, one for opposite and one for adjacent folding angles, that describe the full configuration space of any degree-4 rigid origami vertex, Euclidean or non-Euclidean, as two folding modes, the two branches of a square root, which meet at the flat state of a developable vertex and cannot meet there when the sector angles do not sum to 2π; the arXiv copy prints the opposite-angle equation with two signs wrong

## Source

Foschi, Hull and Ku (2022), [LIT-2055](../literature.d/LIT-2055.md); read in full in [NOTE-1606](../notes.d/NOTE-1606.md).

## What was actually shown

- **The equations** (§§II–III). Theorem 2 gives one relation for opposite and one for adjacent folding angles, in tan(ρ/2), for any degree-4 vertex. They are proved in Appendix A, which was read and checked. The printed opposite-angle relation (Eq. 4) has two signs wrong; see the note below.
- **Two modes** (Corollary 1). Solving Eq. 5 for one angle gives two roots, the two branches of the square root in Eq. 6; the paper says the configuration space "consists of two curves in R4".
- **Meeting at the flat state.** In a developable vertex the modes cross at the flat state. A vertex whose sector angles do not sum to 2π cannot have every folding angle zero, so its modes cannot meet there (§III, Example 1). Example 1's elliptic and hyperbolic perturbations separate their modes when the folding angles stay inside (−π, π).
- **Discrete case** (§V A). The square-twist pouch's rigid configuration space is discrete, with three states.

## The misprints, as the paper prints them

The arXiv v2 copy prints three relations wrongly. Its other results use the correct forms.

- **Eq. 4.** Printed: tan²(ρ_i/2) = −[(1+T)cos(α_{i−1}+α_i) + T cos(α_{i+1}−α_{i+2}) + cos(α_{i+1}+α_{i+2})] / [(1+T)cos(α_{i−1}−α_i) − T cos(α_{i+1}−α_{i+2}) − cos(α_{i+1}+α_{i+2})], with T = tan²(ρ_{i+2}/2). The relation that holds has −T cos(α_{i+1}−α_{i+2}) − cos(α_{i+1}+α_{i+2}) in the numerator, and the denominator is unchanged.
- **(A3).** Printed: cos ρ2 = cot α1 cot α2 + (sin α2 sin α4 cos t − cos α3 cos α4)/(sin α1 sin α2). It holds with sin α3 sin α4 in place of sin α2 sin α4.
- **(A6).** It holds with its x² and y² coefficients exchanged, that is with x = tan(ρ1/2) and y = tan(ρ4/2); it is then Eq. 5 at i = 4.

## What this does not say

- Anything about vertices of degree other than 4.
- Which parts of each curve avoid self-intersection; the paper draws those parts, it does not exclude them.
- That the modes are disconnected for every non-Euclidean vertex. With passes through ±π allowed, the elliptic example is one connected loop; that wider claim is [THEORY-tmp0i15x](THEORY-tmp0i15x.md).

## Note of 2026-11-06: reader J, the misprints

As printed in arXiv v2, Theorem 2's Eq. 4 gives the numerator terms T cos(α_{i+1}−α_{i+2}) and cos(α_{i+1}+α_{i+2}) the wrong sign.

The check measured folding angles on independently built vertices of all three types. The printed form misses by about 2; with those two terms negated it holds to rounding. That check is scratch/formal/foschi_eq4_search.py, second-checked by the coordinator on 2026-11-06.

Appendix B's first display, Eq. 10 and Theorem 3 all agree with the corrected form, so the slip is in the typesetting of the theorem, not in the work. (A3) and (A6) carry two further slips, given above.
