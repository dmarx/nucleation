---
number: 516
status: Active
formerly:
- CLAIM-tmpczfpk
title: 'Where every constraint capacity turns over at a positive rate and is produced only by others, with no basal production and production vanishing as its producers do, capacities whose production graph is acyclic all decay to zero: a capacity that persists needs a productive cycle among its ancestors, and removing a feedback edge set extinguishes every capacity; a cycle is necessary and not sufficient, and a one-member cycle is not closure'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the induction, or a system meeting the stated hypotheses
  (continuous production that vanishes uniformly as its producers go to
  zero, no basal production, turnover rates bounded below by d₀ > 0) whose
  production graph is acyclic and in which some capacity does not tend to
  zero.
tags:
- philosophy-of-biology
- mathematics
- complex-systems
date: '2026-10-31'
line:
- distributed-agency
- formal-apparatus
uses:
- TERM-070
complements:
- CLAIM-395
grounds:
- 'CASE-189'
summary: >-
  From A10 §1 and §5A of the exchange "Analyze nucleation concepts"
  (2026-10-31), after the owner's "try to progress the theoretical
  program". The proof was rechecked by the reader of U7–U10. It is known in
  substance from autocatalytic-set theory, as A10 said. What it adds to the
  record is the boundary with closure: the necessary cycle may be a
  self-loop, and a self-loop is not closure in [TERM-070](../terms.d/TERM-070.md)'s sense or
  [CLAIM-395](CLAIM-395.md)'s, which need two or more constraints.
---

# CLAIM-516: Where every constraint capacity turns over at a positive rate and is produced only by others, with no basal production and production vanishing as its producers do, capacities whose production graph is acyclic all decay to zero: a capacity that persists needs a productive cycle among its ancestors, and removing a feedback edge set extinguishes every capacity; a cycle is necessary and not sufficient, and a one-member cycle is not closure

## The claim

Let constraint capacities cᵢ ≥ 0 evolve as ċᵢ = Pᵢ(c) − dᵢ(t)cᵢ, with
dᵢ(t) ≥ d₀ > 0, Pᵢ continuous, depending only on the capacities that
produce cᵢ (its parents in the production graph), and Pᵢ → 0 uniformly
as those parents go to zero. There is no basal production.

**Acyclic graphs go extinct.** Order the capacities topologically. A
capacity with no parents has ċᵢ ≤ −d₀cᵢ and decays exponentially. If all
of cᵢ's parents tend to zero, Pᵢ eventually falls below any ε, so
lim sup cᵢ ≤ ε/d₀ for every ε, and cᵢ → 0. By induction every capacity
tends to zero.

**Ancestry.** A capacity's ancestors form a forward-closed set, so the
same argument applied to them shows: if none of a capacity's ancestors
lies on a cycle, it tends to zero. A capacity that does not decay has a
productive cycle among its ancestors. Removing a feedback edge set, so
that the graph becomes acyclic, extinguishes every capacity, provided
the knockout leaves each Pᵢ vanishing as its remaining parents do.

## What it does not say

- **That a cycle suffices.** The two-constraint model of [CASE-189](../cases.d/CASE-189.md) has a
  cycle and goes extinct from small seeds and above a damage threshold.
- **That the cycle is closure.** A self-loop, a capacity producing itself,
  satisfies the necessary condition. Closure in [TERM-070](../terms.d/TERM-070.md)'s sense, and in
  [CLAIM-395](CLAIM-395.md)'s, needs at least two mutually dependent constraints, and
  [CASE-161](../cases.d/CASE-161.md) shows a self-dependent production rule does not regenerate a
  zeroed rule. The theorem's necessary condition is weaker than closure.
- **Anything about systems with basal production or an outside supply.**
  An exogenous source keeps an acyclic graph alive; that is the
  externally maintained case.
- **That real chemistry decays to zero.** The hypothesis of no basal
  production and decay to zero is the limit of infinite affinity, with
  irreversible decay. Under local detailed balance the decay c ⇌ W has a
  back reaction, and with any waste present the capacities of an acyclic
  graph relax to (d′/d)[W], not to zero. The proof and the warrant stand
  for the stated hypotheses.
- **That the production cycle is a stoichiometric cycle.** The graph is one
  of catalytic influence. Catalysts cancel out of the stoichiometric
  matrix, so a cycle of mutual catalytic production is not a cycle in the
  reaction network's kernel; steady currents run on fuel-to-waste cycles
  ([THEORY-1248](../theory.d/THEORY-1248.md)). Mossio, Montévil and Longo's closure likewise needs
  another member, and their hydrological cycle is a cycle of processes that
  is not closure ([LIT-1888](../literature.d/LIT-1888.md)).
