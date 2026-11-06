---
number: 196
status: Proposed
formerly:
- CASE-tmpqzzui
title: 'Three species whose every pair coexists identically for every strength b of a three-way term that vanishes on pairs: above b = 0.96 a missing species cannot invade a resident pair, above b = 1.76 the triple cannot persist from any start, and between them it persists from some starts and not others, so whether the triangle of the compatibility complex is filled depends on whether compatibility is declared as robust permanence or as a stable positive equilibrium'
version: 1
standing: fictional
kind: construction
tags:
- ecology
- mathematics
- complex-systems
date: '2026-11-04'
line:
- distributed-agency
variant_of:
- CASE-119
- CASE-118
illustrates:
- CLAIM-347
- CLAIM-534
summary: >-
  A8's Proposal A, from the exchange "Organizational Nucleation and SLT"
  (2026-11-04), answering the owner's U8 request for CASEs the record
  lacks. [CASE-119](CASE-119.md) stipulates a complex with every edge and no triangle.
  This one derives it from ecological dynamics, with every pair's dynamics
  identical at every b. A stated two results. The reader confirmed both by
  simulation, derived the two thresholds, and found a bistable band A did
  not mention, 0.96 < b < 1.76. In that band the complex depends on which
  notion of compatibility is declared. The wording is A's, sharpened by the
  reader; adopting it is the owner's call.
---

# CASE-196: Three species whose every pair coexists identically for every strength b of a three-way term that vanishes on pairs: above b = 0.96 a missing species cannot invade a resident pair, above b = 1.76 the triple cannot persist from any start, and between them it persists from some starts and not others, so whether the triangle of the compatibility complex is filled depends on whether compatibility is declared as robust permanence or as a stable positive equilibrium

## The construction

The owner's U8: "try to construct some new CASE proposals which elucidate
some of our account's matured nuance that isn't already captured by the
CASEs already documented on the record."

A8, Proposal A. Three populations n_i ≥ 0 follow

  ṅ_i = n_i [1 − n_i − a Σ_{j≠i} n_j − b Π_{j≠i} n_j],

with a = 0.2. The parameter b ≥ 0 "measures an interaction that only
operates when all three populations are present".

- **Every pair is fixed.** On a pair the third population is 0, so the
  product term vanishes. Each pair coexists stably at n = 1/(1 + a) = 5/6
  for every b.
- **Invasion.** A rare third species entering a resident pair grows at
  s_inv = 1 − 2a/(1 + a) − b/(1 + a)². At b = 4 this is −19/9.
- **The complex.** A8: "Define a collection of species as compatible when
  that collection admits robust permanence under its corresponding
  ecological dynamics. Then the compatibility complex at b=4 contains
  every edge but lacks the filled triangle, whereas at b=0 the triangle is
  present."

The persistence of a species stands in for a demand here. That is a
modelling choice, as in [CASE-118](CASE-118.md).

## Results

The reader's checks used scipy's solve_ivp with rtol 10⁻⁹ and 200 random
starts in [0.01, 1.5]³ for each b. The scripts are scratch/formal/r2_three_species.py and
scratch/formal/r2_band_and_fourth_arm.py.

**Two thresholds.** The symmetric interior equilibrium x* solves
1 − (1 + 2a)x − bx² = 0. Its Jacobian is −xI − x(a + bx)(11ᵀ − I). The
transverse eigenvalue, of multiplicity 2, is x(a + bx − 1).

- **Invasion fails** when s_inv < 0, that is b > 1 − a² = 0.96.
- **The interior equilibrium loses stability** when a + bx* > 1, that is
  b > (1 − a)(2 + a) = 1.76.

A8's own code for these failed to run in the export. Its formulas match.

**Outcomes from random starts.**

| b | invasion rate | transverse eigenvalue | starts keeping all three |
|---|---|---|---|
| 0 | +0.667 | −0.571 | 200 / 200 |
| 0.5 | +0.319 | −0.298 | 200 / 200 |
| 1.0 | −0.028 | −0.145 | 193 / 200 |
| 1.2 | −0.167 | −0.100 | 123 / 200 |
| 1.5 | −0.375 | −0.042 | 40 / 200 |
| 1.7 | −0.514 | −0.009 | 0 / 200 |
| 4 | −2.111 | +0.220 | 0 / 200 |

- At b = 4 every start ends with exactly two species. So the triple cannot
  persist from typical starts at all. That is stronger than A8's "not
  robustly permanent".
- At b = 1.7 the interior equilibrium is still stable. A start displaced
  by 0.01 returns to it, and one displaced by 0.03 loses a species. The
  basin shrinks to nothing as b approaches 1.76, so 0 of 200 random starts
  is consistent with stability.

**The bistable band.** For 0.96 < b < 1.76 the pairs resist invasion, so
the triple is not robustly permanent. Yet the triple has a stable positive
equilibrium, reached from some starts. Which complex the system has
depends on the declared notion of compatibility:

- **robust permanence:** the triangle is missing for every b > 0.96;
- **a stable positive equilibrium exists:** the triangle is present up to
  b = 1.76.

## What it shows and does not

**It shows that a missing simplex can be derived, not only stipulated.**
[CASE-119](CASE-119.md)'s point, that pairwise compatibility does not fix joint
compatibility, here comes out of dynamics. Every pair is held exactly
fixed while b varies. A8: "a precise example of community-level
frustration that cannot be diagnosed from pairwise coexistence data."

**It shows that the face criterion is part of what is declared.** [CLAIM-347](../claims.d/CLAIM-347.md)
indexes the complex to an organization, a horizon and a budget. This case
adds a further index: what counts as joint persistence. In the band, robust
permanence and stable coexistence give different complexes. This is
[CLAIM-534](../claims.d/CLAIM-534.md)'s point that integration has to be "kept so under its own
dynamics", made sharper.

**It is the nonlinear case [THEORY-598](../theory.d/THEORY-598.md) marks.** [THEORY-598](../theory.d/THEORY-598.md) says group terms
that enter linearly reduce to pairwise dynamics, while bistability comes
from group terms that enter nonlinearly. The b term is a product, and the
band is its bistability. The organizational counterpart is the bistable
authority balance of [CLAIM-459](../claims.d/CLAIM-459.md) and [CASE-112](CASE-112.md).

**Its invasion structure is acyclic.** [THEORY-1168](../theory.d/THEORY-1168.md) shows that the invasion
graph of symmetric Lotka–Volterra has no cycles. This model is not
Lotka–Volterra, because of the product term. Its invasion structure, from
singletons to pairs with no edge into the triple, is acyclic in any case.
[NOTE-1379](../notes.d/NOTE-1379.md), a reading of Hofbauer and Schreiber ([LIT-1233](../literature.d/LIT-1233.md)), gives the
invasion-graph criterion for permanence.

**It does not show relief.** A8 suggested adding an adaptive variable
that lowers the effective three-way term. A8: "This would not establish
that differentiation is spontaneously learned. That additional mechanism
would have to be specified and tested." That is [QUESTION-133](../questions.d/QUESTION-133.md).
