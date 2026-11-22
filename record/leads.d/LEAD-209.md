---
number: 209
status: Open
formerly:
- LEAD-tmpng7or
title: 'Write and try a protocol that reads which mechanism maintains an observed power law from how its cutoff, its rescaled distributions, its dynamics and its response to a symmetry-breaking field behave'
version: 3
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Edited in place on 2026-11-22 after Beck and Cohen (LIT-2962) was
    read: a row for the third-order term of the small-variance expansion,
    the mixture column's cutoff cell restated by CLAIM-tmpf9qt9, and a
    paragraph saying that the turbulence and mixture columns are not
    exclusive. The plan and status are unchanged.
- version: 3
  date: '2026-11-22'
  note: >-
    Edited in place on 2026-11-22 after Takeuchi and Sano (LIT-2982),
    Kardar, Parisi and Zhang (LIT-2978) and Toner and Tu (LIT-2970) were
    read, and Kosterlitz and Thouless (LIT-2969) through neighbours: the
    KPZ column's skewness cell corrected from increments to the height; a
    row for the parameter-free skewness and kurtosis of the height (GUE
    against GOE against Gaussian); a row for a finite interaction range
    (a penetration depth λ) beside the symmetry-breaking field; the
    flock's observables named. The plan and status are unchanged.
stage: idea
method:
- formal
- empirical
tags:
- complex-systems
- natural-sciences
- mathematical-statistics
date: '2026-11-21'
line:
- formal-apparatus
advances:
- CLAIM-841
- CLAIM-829
- QUESTION-508
summary: >-
  The exchange "Rich Get Richer Power Laws" offers several tests to tell
  what keeps a power law in place: finite-size scaling and data collapse
  (A8 §6, A12 §8), the behaviour of the cutoff by mechanism (A24 §9), the
  dynamic exponent (A24 §6), probability currents and the time asymmetry
  of trajectories (A24 §1, §10), and the gap a symmetry-breaking field
  opens (A27 §6). It never puts them together, and the one it leans on,
  the cutoff, is a static feature, which the ledgers flag. The lead is to
  write them as one protocol and try it on simulated systems whose
  mechanism is known. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmpw4qgu THEORY-tmpczldx CLAIM-tmpf9qt9 — Proposed; the readings of 2026-11-22 cited in the notes and the table, and the assistant's condition on the spread -->
<!-- inactive-ok-file: CLAIM-841 CLAIM-829 CLAIM-803 CLAIM-846 CLAIM-850 — filed from the same exchange on 2026-11-21, Proposed or Open -->
<!-- inactive-ok-file: THEORY-tmpmoyol THEORY-tmpo3w5v THEORY-tmpdfeto THEORY-tmpwdka8 NOTE-tmpcjw5n CLAIM-tmpvq33w LIT-2969 — Proposed, Skimmed, Unfetched or new; the readings of 2026-11-22 and the claim filed from them -->

# LEAD-209: Write and try a protocol that reads which mechanism maintains an observed power law from how its cutoff, its rescaled distributions, its dynamics and its response to a symmetry-breaking field behave

## Sketch

**Why.** [CLAIM-841](../claims.d/CLAIM-841.md) holds that a power law does not show criticality,
and A24 §1 that a stationary histogram cannot name its mechanism. The
exchange offers discriminating observations one at a time; A24 §9's
summary of them ("What is the tail actually measuring?") still reads the
mechanism from a static cutoff. A protocol that uses dynamics and
response as well would make [CLAIM-841](../claims.d/CLAIM-841.md) usable, and test
A10 §8's reading, which [CLAIM-829](../claims.d/CLAIM-829.md) states as the separation-of-scales
reading of the owner's U5, that the extremes near a continuous transition
follow the same law as the bulk: "The extreme events aren't governed by
fundamentally different rules", with A's hedge that this "is not
universally true for all heavy-tailed phenomena". An event above the
extrapolated law, a dragon king, is exactly an extreme with different
rules, and the data collapse is the check that tells the two apart.
[CLAIM-803](../claims.d/CLAIM-803.md) makes the general point that a distribution does not
identify its mechanism; [LEAD-211](LEAD-211.md) is the cutoff row of this lead's
protocol taken alone, as an early-warning sign; this lead subsumes its
cutoff test, and it stays a lead of its own for its comparison with the
variance warning.

**Observations, and what each mechanism predicts.**

| Observation | Tuned criticality | Symmetry (Goldstone, XY) | Flux (turbulence) | Growth (KPZ) | Mixture or heterogeneity |
|---|---|---|---|---|---|
| cutoff as the control parameter moves | grows on approach | none in the phase | set by injection and dissipation scales | none needed | fixed by the spread's lowest rate; none if the spread has power-law weight at zero rate ([CLAIM-tmpf9qt9](../claims.d/CLAIM-tmpf9qt9.md)) |
| cutoff with system size L | ∝ L^D, with collapse s^(−τ) f(s/L^D) | ∝ L | fixed by viscous scale | W ∝ L^α | independent of L |
| dynamic exponent z, from C(r, t) = r^(−2Δ) F(t/r^z) | model's z | 1 or 2 by mode | from flux scaling | 3/2 in 1D | none |
| net probability currents, path-space KL(forward ‖ reversed) | zero for an equilibrium point (Ising), nonzero for an absorbing-state one (directed percolation) | zero at equilibrium | nonzero | nonzero | either |
| a small symmetry-breaking field μ | shifts the point | opens a gap, ξ ∼ √ρ_s/μ; for a flock, a "compass" gives a "mass" (Toner and Tu, p. 63) | no effect expected | depends | no effect |
| a finite interaction range (a cutoff length λ on the coupling, e.g. a penetration depth) | depends | ends the 2D XY phase: beyond λ vortices are free at any T > 0 (Kosterlitz's lecture, p. 98) | not worked out | not worked out | no effect |
| odd-order statistics of increments | zero in a Z₂-symmetric equilibrium model | zero (Gaussian) | nonzero (4/5 law) | not measured in the KPZ readings; the nonzero skewness they report is of the height, next row | either |
| skewness and kurtosis of the rescaled height, which need no fitted parameter | not worked out | zero (Gaussian) | not worked out | GUE Tracy-Widom, about 0.2241 and 0.09345, for a curved front; GOE for a flat one; Gaussian excluded (Takeuchi and Sano, p. 3) | not worked out |
| third-order term g(q) of the small-variance expansion of the log distribution (Beck and Cohen, eqs. 26–30) | not worked out | not worked out | the spread's, where the flux is read as superstatistics | not worked out | tells the spread apart: 0 uniform, −⅓(q − 1)² gamma, −⅙(q³ − 3q + 2) lognormal |

**The columns are not exclusive.** Beck and Cohen's own application of
superstatistics is turbulence: the heavy tails of velocity differences
are modelled as an average over the fluctuating energy dissipation rate
("In the turbulence applications ... the fluctuating intensive quantity
is related to the energy dissipation rate of the flow", [LIT-2962](../literature.d/LIT-2962.md), p. 9;
[THEORY-tmpczldx](../theory.d/THEORY-tmpczldx.md)). So one system can be read under the flux column and the
mixture column at once, and the protocol should score that as a joint
answer, not a miss. Their third-order term is the row added above: at
small variance every superstatistics has the same first correction, and
only g(q) tells the spread apart.

The table is a first draft from A's turns and the assistant's checks in
[CLAIM-846](../claims.d/CLAIM-846.md) and [CLAIM-850](../claims.d/CLAIM-850.md); writing the protocol includes
checking each cell.

The KPZ column's dynamic exponent and cutoff cells are what Kardar,
Parisi and Zhang and Takeuchi and Sano give (z = 3/2, W ∝ L^α, α = ½), for
d = 1; above two dimensions a weak nonlinearity flows to the smooth phase
(z = 2), so the column is for d ≤ 2. The flock's observables, for the
symmetry column, are the density structure factor Cρ(q), diverging as
q → 0, the widths and heights of the peaks of Cρ(q, ω), and a tagged
bird's hyperdiffusive w²(t) ∝ t^(4/3) in d = 2 (Toner and Tu, §VII).

**Trial.** Simulate one system per column where the answer is known:
critical branching at several R and sizes; the Gaussian spin-wave field
with and without μ; the linear shell cascade of [CLAIM-850](../claims.d/CLAIM-850.md) and, if
affordable, a shell model of turbulence; a 1D KPZ discretization, scored against the exponents and the
GUE/GOE skewness and kurtosis; an
exponential mixture over a gamma spread of rates. Apply the protocol blind
to each and score how often it names the mechanism. Then add a
dragon-king case (one mechanism for the bulk, another for the top
events) and see whether the collapse check catches it ([CLAIM-829](../claims.d/CLAIM-829.md)).

**What would count.** The protocol names the mechanism in each simulated
case from observations a field study could make. If two columns cannot be
told apart by any row, that pair goes into [CLAIM-841](../claims.d/CLAIM-841.md) as a limit.

**Cost.** A few days of simulation and writing; no outside data. The
trajectory-level rows answer A24 §10's proposal of a "universality of
histories" for these cases only.

## Note of 2026-11-22: Clauset, Shalizi and Newman, read

**Method** ([LIT-2987](../literature.d/LIT-2987.md), [NOTE-tmphbwdu](../notes.d/NOTE-tmphbwdu.md), [THEORY-tmpw4qgu](../theory.d/THEORY-tmpw4qgu.md)). The protocol's
first step can use their nested likelihood-ratio test of a pure power law
against one with an exponential cutoff (§5.2, Tables 6.2–6.3), which
detects a cutoff in one sample; the cutoff form is "clearly favored" for
fires, flares, earthquakes and web hits (p. 26). The paper has nothing on
how a cutoff scales with system size, which is the protocol's own
step.

## Change of 2026-11-22: Beck and Cohen, read

Beck and Cohen ([LIT-2962](../literature.d/LIT-2962.md), read in [NOTE-tmpj8ro5](../notes.d/NOTE-tmpj8ro5.md); [THEORY-tmpczldx](../theory.d/THEORY-tmpczldx.md))
**qualify the table**: a row for the third-order term g(q), a discriminating
observable the table lacked; the mixture column's cutoff cell restated
(a spread with power-law weight at zero rate has no cutoff; one bounded
away from zero has an exponential cutoff at its lowest rate,
[CLAIM-tmpf9qt9](../claims.d/CLAIM-tmpf9qt9.md)); and the paragraph above on the flux and mixture columns.
The trial's "exponential mixture over a gamma spread of rates" is their
eq. 13, (1 + bE)^(−c). Version 2.

## Change of 2026-11-22: the KPZ and symmetry columns, after reading

- **Skewness of the height, not of increments.** The KPZ cell "nonzero
  skewness" in the increments row was near the mark but misplaced: what
  Takeuchi and Sano measure (LIT-2982, NOTE-tmpbmox1; THEORY-tmpmoyol) is
  the skewness of the height itself, the local radius, about 0.2241, with
  kurtosis about 0.09345, quantities "which do not depend on the
  parameter estimates" (p. 3). The cell now says so, and a row of its
  own carries them: they tell GUE (curved fronts) from GOE (flat) and
  from Gaussian, so they read the geometry as well as the class.
- **A finite interaction range**, beside the symmetry-breaking field: a
  second kind of scale-introducing perturbation. In a charged
  superconducting film a finite penetration depth "limits the range of
  the logarithmic interaction between vortices", so "the vortices are
  always free at any T > 0" (Kosterlitz's lecture, LIT-tmp3k6np, p. 98;
  THEORY-tmpwdka8). It ends the untuned XY phase without breaking the
  symmetry. CLAIM-tmpvq33w states the shape the two rows share.
- **The flock's field response.** Toner and Tu (LIT-2970, NOTE-tmpcjw5n;
  THEORY-tmpdfeto) support the field row for flocks: a compass
  "will introduce a "mass" that makes any fluctuation away from the
  pre-picked direction of flock motion decay rapidly" (p. 63).

Version 3.

## Note of 2026-11-22: Kardar, Parisi and Zhang, read

KPZ (LIT-2978, NOTE-tmpf6isj; THEORY-tmpo3w5v) **supports the KPZ
column's z and W cells** for d = 1, exact there, and scopes the column to
d ≤ 2. It has nothing on skewness, currents or a cutoff. A trial on a 1D
discretization should recover z = 3/2 and the growth exponent ⅓.

