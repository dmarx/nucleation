---
number: 1266
status: Active
formerly:
- THEORY-tmplh6oa
title: 'In an open reaction network of reversible elementary mass-action reactions, sustained currents need an emergent cycle with nonzero affinity: each chemostatted species either breaks a conservation law or opens an emergent cycle, so one chemostat never suffices; with every emergent affinity zero the network relaxes to a unique equilibrium fixed by its unbroken conserved quantities; and a nonequilibrium steady state dissipates exactly the sum over emergent cycles of current times affinity'
version: 1
tags:
- thermodynamics
- complex-systems
date: '2026-10-31'
source:
- LIT-1889
- LIT-1897
summary: >-
  Rao and Esposito (2016), [LIT-1889](../literature.d/LIT-1889.md), read in [NOTE-1464](../notes.d/NOTE-1464.md), with the
  one-chemostat proof of Dal Cengio, Lecomte and Polettini (2023),
  [LIT-1897](../literature.d/LIT-1897.md) ([NOTE-1476](../notes.d/NOTE-1476.md)). Active: rank–nullity, Wegscheider's
  condition and two lines of algebra, checked numerically on a
  reversible rewriting of [CASE-189](../cases.d/CASE-189.md)'s first construction, which has
  a single equilibrium at zero affinity and is bistable only above
  3.52 RT. It does not say that a driven network is far from
  equilibrium, multistable or organized; only that without an emergent
  affinity it cannot be, and what it costs when it is.
---

# THEORY-1266: In an open reaction network of reversible elementary mass-action reactions, sustained currents need an emergent cycle with nonzero affinity: each chemostatted species either breaks a conservation law or opens an emergent cycle, so one chemostat never suffices; with every emergent affinity zero the network relaxes to a unique equilibrium fixed by its unbroken conserved quantities; and a nonequilibrium steady state dissipates exactly the sum over emergent cycles of current times affinity

## Source

Rao and Esposito (2016), [LIT-1889](../literature.d/LIT-1889.md), §§II C–E and III D, eqs. 20, 28, 50,
55 and 59–61, Example 6, pp. 4–10 of arXiv 1602.07257v3; read in
[NOTE-1464](../notes.d/NOTE-1464.md). The proof that a single chemostat leaves the affinity
conservative is Dal Cengio, Lecomte and Polettini (2023), [LIT-1897](../literature.d/LIT-1897.md), eq. 47
([NOTE-1476](../notes.d/NOTE-1476.md)).

## What was actually shown

**Bookkeeping.** Close a network and it has conservation laws ℓ (left null
vectors of the stoichiometric matrix ∇) and cycles (right null vectors).
Fix the concentrations of a set S_y of species and the internal matrix ∇_X
loses rows. By rank–nullity, |S_y| = |λ_b| + |ε|: each chemostatted species
either breaks a conservation law or creates an emergent cycle, a set of
reactions that leaves the internal species unchanged and moves chemicals
from one chemostat to another (pp. 4–5). The first chemostat always breaks
total mass, so one chemostat creates no emergent cycle and the network is
"unconditionally detailed-balanced" (Example 6).

**Equilibrium.** Local detailed balance, k⁺/k⁻ = exp(−Δ_r G°/RT), makes every
cycle affinity of the closed network zero. An emergent cycle's affinity
A_ε depends only on the chemostatted concentrations (eq. 28). The network is
detailed-balanced iff every A_ε = 0, and then relaxes to an equilibrium that
is globally stable and unique for given unbroken conserved quantities
(pp. 5–6).

**Cost.** Entropy production is RT Σ_ρ (J⁺ − J⁻) ln(J⁺/J⁻) ≥ 0 (eq. 55); at a
nonequilibrium steady state it equals Σ_ε J_ε A_ε (eq. 61).

**A worked check (mine).** [CASE-189](../cases.d/CASE-189.md)'s first construction, two
capacities producing each other with saturating production and turnover,
is written with irreversible Hill terms. Rewritten as elementary reversible
chemistry, with fuel S and waste W chemostatted, S + 2c₂ ⇌ c₁ + 2c₂,
S + 2c₁ ⇌ c₂ + 2c₁, c_i ⇌ W, all rate constants 1 and [S] = 3, the network
has two chemostats, one broken law, one emergent cycle (S → W) and
deficiency 2. Its emergent affinity is RT ln(3/[W]). At [W] = 3, zero
affinity, there is one fixed point, c = (3, 3), with no current. The
extinct state and the threshold appear only for [W] < 0.0887, above
3.52 RT. As [W] → 0 the symmetric equilibria tend to the case's own,
(3 ∓ √5)/2. At [W] = 0.01 the maintained state dissipates 29.77 (RT times
the rate unit), and the reaction-by-reaction sum and J_ε A_ε agree.

**What could have failed.** The steady dissipation could have depended on
internal concentrations in a way not captured by the emergent cycles. Or a
single reservoir could have sustained a current. Neither happens, and both
are exact.

## What this does not say

- **That a driven network is organized, multistable or far from
  equilibrium.** A nonzero affinity is necessary. What the network does with
  it is kinetics. Complex-balanced networks, including every deficiency-zero
  network, have a unique globally attracting steady state however hard they
  are driven ([LIT-1889](../literature.d/LIT-1889.md), §IV), so they form no dissipative structure.
- **That a positive production rate in a phenomenological model is a
  mechanism.** Hill and Michaelis–Menten terms, and irreversible decay, are
  effective rate laws outside the theory until resolved into elementary
  steps. The infinite-affinity limit in which they are recovered is where a
  model's "no basal production" assumption lives ([NOTE-1464](../notes.d/NOTE-1464.md), on
  [CLAIM-516](../claims.d/CLAIM-516.md)).
- **Anything about catalytic organization.** Catalysts cancel from the
  stoichiometric matrix, so who produces whom does not enter the
  thermodynamic budget ([THEORY-1248](THEORY-1248.md)).
- **That the chemostats are external.** They are a regime of a larger closed
  system, valid for a window ([THEORY-1250](THEORY-1250.md)).
- **Anything beyond ideal dilute, well-mixed, deterministic chemistry.**
