---
number: 207
status: Proposed
formerly:
- CASE-tmpez9ok
title: 'The square twist: a crease pattern with no rigid folding motion folds once facet bending is paid for, so which configurations are connected depends on the energy available'
version: 2
history:
- version: 2
  date: '2026-11-11'
  note: >-
    Bears on QUESTION-391, at the reading review of 2026-11-11 (by
    question, ADR-091), as an instance (ADR-092). The question's note of
    2026-11-05 "reads the square twist (CASE-207) as a case of this
    question"; its own text, "A constraint below one energy scale, facet
    planarity, is a degree of freedom above it." Already carries
    realizability, so no line changes. No other change.
standing: documented
kind: reported-study
tags:
- natural-sciences
- mathematics
- complex-systems
date: '2026-11-05'
line:
- realizability
illustrates:
- CLAIM-571
- CLAIM-478
reported_in:
- LIT-2100
- NOTE-1554
summary: >-
  Filed at the owner's request on 2026-11-05, to file "one or more CASEs
  for origami as a toy model of a resource bounded constraint
  configuration space". Silverberg et al. 2015 ([NOTE-1554](../notes.d/NOTE-1554.md)): the
  square twist's crease pattern is isostatic, and rigidly it has only two
  isolated states, unfolded and folded, yet it folds by bending its
  facets, a hidden degree of freedom with its own energy scale. The
  authors' thesis is that the number of degrees of freedom changes with
  the energy scale probed; their kinematic skeleton, with bending capped
  at 10°, has a critical plane angle near 23° separating a connected
  configuration space from a disconnected one. Read as a resource model,
  the configuration space is indexed by the budget rather than fixed, and
  widening the admissible moves is itself priced, which joins the vertex
  under a budget ([CASE-206](CASE-206.md)) to the curved vertex whose moves no
  budget widens ([CASE-204](CASE-204.md)). A mechanical study; its organizational
  reading is an analogy. Adopting it is the owner's call.
bears_on:
- QUESTION-391
---
<!-- inactive-ok-file: CLAIM-478 CASE-204 — Proposed; the entries filed beside it, cited as filed, nothing here rests on their being settled -->

# CASE-207: The square twist: a crease pattern with no rigid folding motion folds once facet bending is paid for, so which configurations are connected depends on the energy available

## The case

**The study.** Silverberg et al. (2015; [NOTE-1554](../notes.d/NOTE-1554.md)) fold the square
twist, a crease pattern whose geometric constraints make it isostatic:
counted with rigid facets it has zero degrees of freedom, and rigid
geometry allows only two isolated states, fully unfolded and folded. It
folds anyway, in paper and in a sub-millimetre self-folding gel, by
bending its facets, a deformation the crease pattern does not show. The
bending modes sit above the crease modes in energy.

**What is reported.**

- **The thesis.** A structure can be overconstrained with respect to
  low-energy loading and underconstrained once higher-energy modes are
  reached: "Thus, Nf should be thought of as a variable quantity that
  changes with the experimental energy scale."
- **A kinematic skeleton** (SI p. 2, skimmed). With facet bending allowed
  up to 10° at no cost, and none beyond, a purely kinematic model has a
  critical plane angle of (23 ± 2)°, separating a continuously connected
  configuration space (φ below it) from one with disconnected solutions
  (φ above it).
- **With energetics.** Below a critical plane angle of (25 ± 2.5)° the
  structure is monostable, above it bistable and snapping. The critical
  angle shifts with the ratio of bending to crease stiffness, k_b/k_c: in
  simulation every geometry was monostable for k_b/k_c ≤ 1 and bistable
  for k_b/k_c ≥ 10³. Added creases remove the gel's hysteresis.

**The resource reading (the filer's).** In [CASE-206](CASE-206.md) the
configuration space is fixed and a budget cuts it. Here the budget
decides what the configuration space is. Under rigid folding alone, the
unfolded and folded states are isolated points: no admissible path joins
them, and [CLAIM-571](../claims.d/CLAIM-571.md)'s bottleneck budget is infinite, as in
[CASE-204](CASE-204.md). Admit facet bending as a move and the points are joined,
at a cost. The skeleton makes this exact for one cap: with 10° of
bending, the two are connected for small plane angles and not for large
ones. So the declared class of admissible moves, which [CLAIM-567](../claims.d/CLAIM-567.md)
holds fixed when it separates feasible from reachable, is here itself a
function of the energy available. Where the curved vertex's widening, a
face through a face, cannot be bought at all, this one can.

## What it can show

- **A resource-indexed configuration space.** Which configurations count,
  and which are joined, change with the budget, not only which
  configurations a budget admits.
- **That an admissibility boundary can be a price.** A constraint below
  one energy scale, facet planarity, is a degree of freedom above it. The
  line between not allowed and too expensive is drawn by the scale the
  system is probed at.
- **[CLAIM-478](../claims.d/CLAIM-478.md), with an energetic rather than a temporal separation.**
  Below the bending scale facet planarity acts as a constraint; above it
  the constraint is a freedom, and the ratio of the two scales decides
  whether the structure is bistable. The claim speaks of time scales; the
  mapping holds where stiffer modes also relax faster, which the paper
  does not discuss.
- **A neighbour.** Jules et al. ([NOTE-1617](../notes.d/NOTE-1617.md)) trace their Kresling
  memory's defect states to hidden elastic degrees of freedom of the same
  kind, reached by twisting by hand.
- **An analogy, the filer's.** For an organization, what counts as an
  available rearrangement may itself depend on how much it can spend:
  rules that bind at a low budget may be renegotiable at a high one. The
  study shows that shape in a sheet; it does not show it in any
  organization.

## What it cannot show

- **Anything about organizations.** It is a mechanical study; the
  organizational reading is an analogy.
- **The threshold for a given sheet.** The 10° cap is the skeleton's
  stipulation, from SI pages the reading skimmed; it is not a measured
  budget, and the energetic model does not give a single number for
  B*.
- **That the bistable twist is connected at a finite budget in the
  skeleton's sense.** Above the critical angle the skeleton's solutions
  are disconnected at 10°. That the real sheet still snaps between them,
  so that more bending is spent on the way, is the filer's reading of the
  bistability, not a result the reading states.
- **More than one cell.** Tessellations and coupling between cells are
  proposed, not tested.
