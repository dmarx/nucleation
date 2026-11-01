---
number: 189
status: Active
formerly:
- CASE-tmpwxags
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
- 'CLAIM-516'
- 'CLAIM-522'
- 'CLAIM-521'
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

# CASE-189: Two constructions of a maintained organization: two constraints producing each other with saturating production and turnover hold a three-unit coupling, with a box invariant under damage up to 0.4, a saddle-node at damage 0.5 and extinction above it; and a transient encounter that forms a connector enabling that reciprocal production, after which the connector is maintained by what it enables, every single-pathway knockout ends it, and the regime ends in a saddle-node at damage ≈ 0.691 where the coupling's gap is still ≈ 0.989

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
  and with them the coupling, as [CLAIM-516](../claims.d/CLAIM-516.md) requires.
- **Provenance.** An outside controller supplying the same production as
  state feedback gives identical trajectories under every perturbation
  of state ([CLAIM-522](../claims.d/CLAIM-522.md)).

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
  the fold is {0, q*c*, 3q*c*}, so λ₂ ≈ 0.9894 ([CLAIM-521](../claims.d/CLAIM-521.md)).

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
cycle with nonzero affinity ([LIT-1889](../literature.d/LIT-1889.md), [THEORY-1266](../theory.d/THEORY-1266.md)). A12's "viability kernel" over
every disturbance is Aubin's invariance kernel, not the viability kernel
[THEORY-134](../theory.d/THEORY-134.md) defines.

## Note of 2026-10-31: Construction 1 as reversible chemistry

The reading of the reaction-network works rewrote Construction 1 as
reversible mass-action chemistry, with fuel S and waste W chemostatted, all
rate constants 1 and [S] = 3. The results:

- **At zero affinity** there is a single equilibrium, c = (3, 3), with no
  current and no extinct state.
- **Bistability appears** only above about 3.52 RT of driving, that is
  [W] < 0.0887. This threshold belongs to this one reversible network
  with these parameters. It is not a general threshold for chemical
  bistability or for organizational maintenance.
- **The case's equilibria**, (3 ∓ √5)/2, return only in the limit
  [W] → 0, the limit of infinite affinity.
- **The maintained state costs** dissipation equal to current times
  affinity, J_ε A_ε: 29.77 at [W] = 0.01.

- **There is no extinct state at finite affinity.** With [W] > 0 the
  reverse of decay is a positive basal production, so the lower stable
  equilibrium is a low-activity branch with positive capacity, not zero.
  It approaches extinction only in the singular limit [W] → 0.

So the case's maintained branch, and the collapse to a low-activity
branch, are features of strong driving, not of the production graph
alone. "Extinction" in the case is the infinite-affinity idealization. And maintenance that is "endogenous"
relative to the organization lasts only while the reservoirs do. A
chemostat is itself a finite-lived structure of a larger closed network,
open for a time of order its abundance ratio ([THEORY-1250](../theory.d/THEORY-1250.md)).

## Note of 2026-10-31: the folds are statements about infinite size

Read with the stochastic-thermodynamics works, both constructions are
deterministic, so they hold in the limit of infinite size. At finite size
a maintained regime is metastable.
- **Lifetime.** It lasts a time exponential in size, set by a barrier in a
  quasi-potential computed from the dynamics, not by a free energy
  ([THEORY-1273](../theory.d/THEORY-1273.md), [THEORY-1264](../theory.d/THEORY-1264.md)).
- **Near the fold.** The barrier closes as the 3/2 power of the distance
  to the fold, so the hazard of escape rises steeply as the fold nears.
  Whether an observed transition comes before the fold is not fixed by
  that alone. It depends on system size, noise scale, how long the system
  is observed and how fast the parameter is changed.
- **Dissipation.** The production and decay terms here are irreversible,
  so they have no defined entropy production. To be paid for in
  stochastic-thermodynamic terms, every step needs a reverse step obeying
  local detailed balance ([LIT-1892](../literature.d/LIT-1892.md), [THEORY-1265](../theory.d/THEORY-1265.md)).

Vellela and Qian's Schlögl model ([LIT-1890](../literature.d/LIT-1890.md)) is the chemical,
stochastic counterpart of this case, as [CASE-111](CASE-111.md) is its deterministic
predecessor.

Three claims are to be kept apart:
1. a deterministic saddle-node exists in the limiting model;
2. a finite stochastic system can escape its metastable regime before
   that saddle-node;
3. where the transition is observed depends on the finite-time protocol.

The constructions establish the first. The stochastic readings establish
the second. The third is a matter of the experiment's design.

## Note of 2026-11-01: how-possibly models, and what the knockouts show

<!-- inactive-ok-file: CLAIM-tmpg57ci — Proposed; the claim filed from this reading, cited as open -->

- **How-possibly.** In Bechtel and Abrahamsen's terms (LIT-tmppbuqq,
  THEORY-tmpakm3a) both constructions are de novo dynamical models. Their
  variables are posited, not properties of parts found by experiment. So
  they show how a maintained organization could behave (contributions C1
  and C2), not that any system is organized this way.
- **The knockouts.** Removing a production pathway and finding that
  maintenance ends is their C3, a clamp in a model (THEORY-tmp7jall). It
  shows the pathway is a component of the mechanism responsible for
  maintenance. It does not show the pathway is the organization's own,
  since "Which terms are internal is stipulated".
- **Provenance.** The outside controller of CLAIM-522 meets mutual
  manipulability's manipulability conditions as the internal pathway
  does. So which one is a constituent of the organization is settled by
  the declared boundary (CLAIM-tmpg57ci).

No status, title or warrant changes.
