---
status: Active
title: 'Two constructions of a maintained organization: two constraints producing each other with saturating production and turnover hold a three-unit coupling, with a box invariant under damage up to 0.4, a saddle-node at damage 0.5 and extinction above it; and a transient encounter that forms a connector enabling that reciprocal production, after which the connector is maintained by what it enables, every single-pathway knockout ends it, and the regime ends in a saddle-node at damage ≈ 0.691 where the coupling''s gap is still ≈ 0.989'
version: 1
standing: fictional
kind: construction
tags:
- complex-systems
- individuation
date: '2026-10-31'
line: distributed-agency
variant_of:
- CASE-111
supports:
- 'CLAIM-tmpczfpk'
- 'CLAIM-tmpr8p2x'
- 'CLAIM-tmppht9k'
illustrates:
- CLAIM-463
- CLAIM-456
summary: >-
  From A9 §4, A10 §2–5, A11 §2–5 and A12 §2–6 of the exchange "Analyze
  nucleation concepts" (2026-10-31), after the owner's "try to progress
  the theoretical program" and A10's own "theorem target" pasted back at
  U11. Every number below was recomputed by the turns' readers, with an
  independent integration, and the folds again by the filer. Fictional by
  construction, with illustrative parameters. A10's chart had three wrong
  points, which A10 corrected itself. A12 called its fold "the first
  mathematical account of organizational birth, commitment, and death
  within Nucleation's framework"; [CASE-111](CASE-111.md) is the earlier one, and this is
  its variant with a coupling attached.
---

# CASE-tmpwxags: Two constructions of a maintained organization: two constraints producing each other with saturating production and turnover hold a three-unit coupling, with a box invariant under damage up to 0.4, a saddle-node at damage 0.5 and extinction above it; and a transient encounter that forms a connector enabling that reciprocal production, after which the connector is maintained by what it enables, every single-pathway knockout ends it, and the regime ends in a saddle-node at damage ≈ 0.691 where the coupling's gap is still ≈ 0.989

## Construction 1: reciprocal production holding a coupling (A9, A10)

ċ₁ = 3c₂²/(1 + c₂²) − (1 + d₁(t))c₁, ċ₂ = 3c₁²/(1 + c₁²) − (1 + d₂(t))c₂.

- **Equilibria at d = 0.** Symmetric equilibria solve c = 3c²/(1 + c²):
  0, (3 − √5)/2 ≈ 0.382 (a saddle) and (3 + √5)/2 ≈ 2.618 (stable,
  eigenvalues −0.7454 and −1.2546). Since production is increasing there
  are no asymmetric equilibria. Resetting c₁ to 0 with c₂ at 2.618
  recovers to (2.618, 2.618).
- **Invariance.** For 0 ≤ dᵢ(t) ≤ 0.4 the box [1, 4]² is positively
  invariant: at c = 1 the inflow is at least 3/2 − 1.4 = 0.1, and at c = 4
  the outflow is at least 4 − 48/17. A constant d = 0.4 settles at 1.456.
- **Fold.** With constant d, positive equilibria exist iff
  9 − 4(1 + d)² ≥ 0, that is d ≤ 0.5, and they merge at c = 1. Above it,
  3M²/(1 + M²) ≤ 1.5M gives extinction from every start. A seed of 0.2
  collapses and one of 0.5 grows. A10's chart had three wrong points,
  which A10 corrected: (0.437, 2.291) at d = 0.1, (0.578, 1.729) at 0.3,
  (0.770, 1.299) at 0.45.
- **Coupling.** Three units x with ẋ = −L(c)x, L = Bᵀ diag(a₁, a₂) B,
  aᵢ = max{cᵢ − ½, 0}. While c stays in [1, 4]², λ₂(L) ≥ 0.5, so the units
  synchronize at rate at least ½. A pulse ε on the first unit gives
  ẋ₃(0) = 0 and ẍ₃(0) = a₁a₂ε: the third unit responds at second order,
  through the second.
- **Knockout.** Removing the c₂ → c₁ production collapses both capacities
  and with them the coupling, as [CLAIM-tmpczfpk](../claims.d/CLAIM-tmpczfpk.md) requires.
- **Provenance.** An outside controller supplying the same production as
  state feedback gives identical trajectories under every perturbation
  of state ([CLAIM-tmpr8p2x](../claims.d/CLAIM-tmpr8p2x.md)).

## Construction 2: a transient encounter forms a maintained connector (A11, A12)

Encounter variables zᵢ decay (żᵢ = −zᵢ from 1), with intensity
h = χ(z₁)χ(z₂), χ(z) = min{1, max{0, 10z − 5}}, which is zero after t = ln 2.

q̇ = (20h + 12q c₁c₂/(1 + c₁c₂))(1 − q) − q,
ċ₁ = 4q c₂²/(1 + c₂²) − (1 + d₁)c₁, ċ₂ = 4q c₁²/(1 + c₁²) − (1 + d₂)c₂,
from q = 0, c₁ = c₂ = 3.

- **Capture.** The box [0.8, 1] × [1, 4]² is entered by t = ¼
  (q(¼) ≈ 0.967) and is positively invariant for damage up to 0.4 after
  the encounter ends: inflow 0.2 at c = 1, 0.16 at q = 0.8. In the long run
  at d = 0.4, (q, c) ≈ (0.897, 2.085). Without the encounter, q = 0 is
  invariant and the capacities decay.
- **Knockouts.** Removing any single production pathway sends all three
  to zero.
- **Fold.** Symmetric positive equilibria: q = 11/12 − 1/(12c²),
  d(c) = (11c² − 1)/(3c(1 + c²)) − 1, maximal at c*² = (7 + 2√15)/11:
  c* ≈ 1.1578, q* ≈ 0.8545, d* ≈ 0.6908. The slowest maintenance eigenvalue
  goes to zero there.
- **Coupling at the fold.** With L = q Bᵀ diag(c₁, c₂) B the spectrum at
  the fold is {0, q*c*, 3q*c*}, so λ₂ ≈ 0.9894 ([CLAIM-tmppht9k](../claims.d/CLAIM-tmppht9k.md)).

## What it shows and does not

It shows a capacity to maintain, not only a state, being formed by a
transient event, kept by what it enables, and lost past a threshold, with
the coupling it supports unchanged up to that threshold. As A11 said, it
"demonstrates emergence of an operative relation, not creation of a new
fundamental law". The capacities exist from the start in Construction 2;
the encounter supplies only the connector, so this is a bistable system
pushed across a separatrix. Which terms are internal is stipulated, the
substrates are assumed available, and the production terms are not yet
paid for thermodynamically. A13 said that a positive production rate is
not yet a realizable mechanism, and Rao and Esposito make it exact: in an
open, reversible mass-action network, sustained currents need an emergent
cycle with nonzero affinity ([LIT-tmpj1wfs](../literature.d/LIT-tmpj1wfs.md), [THEORY-tmplh6oa](../theory.d/THEORY-tmplh6oa.md)). A12's "viability kernel" over
every disturbance is Aubin's invariance kernel, not the viability kernel
[THEORY-134](../theory.d/THEORY-134.md) defines.

## Note of 2026-10-31: Construction 1 as reversible chemistry

The reading of the reaction-network works rewrote Construction 1 as
reversible mass-action chemistry, with fuel S and waste W chemostatted, all
rate constants 1 and [S] = 3. The results:

- **At zero affinity** there is a single equilibrium, c = (3, 3), with no
  current and no extinct state.
- **Bistability appears** only above about 3.52 RT of driving, that is
  [W] < 0.0887.
- **The case's equilibria**, (3 ∓ √5)/2, return only in the limit
  [W] → 0, the limit of infinite affinity.
- **The maintained state costs** dissipation equal to current times
  affinity, J_ε A_ε: 29.77 at [W] = 0.01.

So the case's maintenance and extinction are features of strong driving,
not of the production graph alone. And maintenance that is "endogenous"
relative to the organization lasts only while the reservoirs do. A
chemostat is itself a finite-lived structure of a larger closed network,
open for a time of order its abundance ratio ([THEORY-tmp1nk6k](../theory.d/THEORY-tmp1nk6k.md)).

## Note of 2026-10-31: the folds are statements about infinite size

Read with the stochastic-thermodynamics works, both constructions are
deterministic, so they hold in the limit of infinite size. At finite size
a maintained regime is metastable.
- **Lifetime.** It lasts a time exponential in size, set by a barrier in a
  quasi-potential computed from the dynamics, not by a free energy
  ([THEORY-tmpwystk](../theory.d/THEORY-tmpwystk.md), [THEORY-tmpjzj2n](../theory.d/THEORY-tmpjzj2n.md)).
- **Before the fold.** The barrier closes as the 3/2 power of the distance
  to the fold, so the lifetime collapses before the fold is reached.
- **Dissipation.** The production and decay terms here are irreversible,
  so they have no defined entropy production. To be paid for in
  stochastic-thermodynamic terms, every step needs a reverse step obeying
  local detailed balance ([LIT-tmpm46ks](../literature.d/LIT-tmpm46ks.md), [THEORY-tmpkze5s](../theory.d/THEORY-tmpkze5s.md)).

Vellela and Qian's Schlögl model ([LIT-tmpkp8vh](../literature.d/LIT-tmpkp8vh.md)) is the chemical,
stochastic counterpart of this case, as [CASE-111](CASE-111.md) is its deterministic
predecessor.
