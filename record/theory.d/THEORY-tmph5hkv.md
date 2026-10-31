---
status: Active
title: 'At stationarity a driven reaction network is confined to a thermodynamic space: each reaction''s affinity lies between zero and the largest cycle affinity per use of that reaction among the elementary flux modes containing it, and each product of concentrations lies between the effective equilibrium constants of the extremal pathways; with no driving the space collapses to the equilibrium point, so multistability, symmetry breaking and amplification above equilibrium need driving and are bounded by it'
version: 1
tags:
- thermodynamics
date: '2026-10-31'
source:
- LIT-tmpfq9vf
summary: >-
  Liang, De Los Rios and Busiello (2024; PRX 2026), [LIT-tmpfq9vf](../literature.d/LIT-tmpfq9vf.md), read in
  [NOTE-tmp3di1n](../notes.d/NOTE-tmp3di1n.md): eqs. 20, 24 and 29, proved for arbitrary stoichiometry
  from local detailed balance and the conformal decomposition of steady
  fluxes into elementary flux modes. Checked on the paper's Schlögl
  parameters and on a reversible rewriting of [CASE-tmpwxags](../cases.d/CASE-tmpwxags.md). Active. It
  bounds where a stationary state can be, for every choice of kinetics;
  it does not say which state is reached, whether it is stable, or how
  long the driving lasts.
---
<!-- inactive-ok-file: THEORY-671 — Proposed; a candidate selection principle named for contrast -->

# THEORY-tmph5hkv: At stationarity a driven reaction network is confined to a thermodynamic space: each reaction's affinity lies between zero and the largest cycle affinity per use of that reaction among the elementary flux modes containing it, and each product of concentrations lies between the effective equilibrium constants of the extremal pathways; with no driving the space collapses to the equilibrium point, so multistability, symmetry breaking and amplification above equilibrium need driving and are bounded by it

## Source

Liang, De Los Rios and Busiello (2024; PRX 16, 041026, 2026), [LIT-tmpfq9vf](../literature.d/LIT-tmpfq9vf.md),
§IV, eqs. 15–29, and §V, pp. 7–17 of arXiv 2407.11498v4; read in
[NOTE-tmp3di1n](../notes.d/NOTE-tmp3di1n.md).

## What was actually shown

**Affinities.** A steady flux decomposes without cancellation into
elementary flux modes (EFMs), minimal sets of reactions that leave the
internal species unchanged. Along an EFM e conformal to the flux, every
reaction pushes forward, and the affinities sum to the cycle affinity A^Y_e
the chemostats supply (eq. 14). So no reaction's affinity exceeds A^Y_e per
use, and maximising over EFMs that contain the reaction gives a bound with
no kinetic input (eq. 20). A virtual, infinitely slow "probe" reaction
extends it to any interconversion the conservation laws allow (eq. 24).

**Concentrations.** Writing affinities through chemical potentials turns
the bound into K^min_π ≤ Π_i x_i^{S_iρ} ≤ K^max_π, where K_π is the
equilibrium constant along a pathway π including the free energy its
chemostats supply (eq. 29). At equilibrium every pathway has the same K, and
the space is a point.

**Checks (mine).** The Schlögl model with the paper's k₁± = 8, k₂± = 1,
b = 0.02 and a = 0.8 has fixed points 0.0234, 0.1787 and 0.5979, all in the
bound [0.02, 0.8] of eq. 36. At a = 0.5 and 0.3 there is one fixed point,
inside; at a = b the bound and the fixed point are both 0.02. In a
reversible rewriting of [CASE-tmpwxags](../cases.d/CASE-tmpwxags.md)'s first construction, every fixed
point lies in [(d′/d)[W], (k/k′)[S]] for each [W] tried.

**What could have failed.** A stationary state could have lain outside the
bounds for some kinetics, as a state above the slope-1 ceiling of the
network without 2B ⇌ C would (Fig. 4). The paper's random-kinetics
simulations and my two checks find none.

## What this does not say

- **Which state is occupied.** The bounds are attained only when one
  pathway dominates kinetically, a time-scale-separation limit; otherwise the
  state is interior and set by kinetics. This is [THEORY-692](THEORY-692.md)'s "thermodynamics
  supplies ... not a principle selecting which structure appears", made
  quantitative. It neither supports nor refutes maximum entropy production
  ([THEORY-671](THEORY-671.md)).
- **How much driving multistability needs.** The space has positive width
  for any positive driving; a particular network may need much more. The
  rewriting of [CASE-tmpwxags](../cases.d/CASE-tmpwxags.md) is monostable below 3.52 RT ([THEORY-tmplh6oa](THEORY-tmplh6oa.md)).
- **Anything about oscillations or transients.** The authors exclude
  persistent oscillations.
- **That an organization's lifetime is bounded by its driving.** The
  chemostats are fixed. A13 of the exchange "Analyze nucleation concepts"
  cited this paper for that point; it belongs to [LIT-tmpgm18n](../literature.d/LIT-tmpgm18n.md)
  ([THEORY-tmp1nk6k](THEORY-tmp1nk6k.md)).
