---
number: 517
status: Active
formerly:
- CLAIM-tmpekkm7
title: 'A successor regulator keeps a viable set positively invariant if, at every boundary context, its response distribution is within γ/L in total variation of a regulator that certifies inward margin γ, the dynamics being L-Lipschitz in that distribution; an average distillation loss certifies this only through coverage of the boundary contexts, so fidelity measured in ordinary operation certifies nothing about viability'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the Pinsker and coverage steps, or a closed set and dynamics
  meeting the hypotheses (inward margin γ at every boundary point, dynamics
  Lipschitz in the state and L-Lipschitz in the regulator's response
  distribution in total variation, a boundary regular enough for Nagumo's
  theorem, margins uniform over the environment) from which a trajectory
  leaves. It is not defeated by a successor that keeps the set viable
  without meeting the bound: the condition is sufficient, not necessary.
tags:
- complex-systems
- mathematics
- information-theory
date: '2026-10-31'
line:
- distributed-agency
- formal-apparatus
grounds:
- THEORY-134
complements:
- CLAIM-503
- CLAIM-407
summary: >-
  From A16 §4 and §5 of the exchange "Analyze nucleation concepts"
  (2026-10-31), the owner having quoted its conclusion at U17:
  "preserving a regulator's response distribution sufficiently accurately
  can guarantee preservation of a physical organization's viability". The
  algebra was rechecked; the regularity conditions A16 left implicit are
  stated here. A16's application to its own construction (γ = 0.16) was
  notional, since that model has no regulator distribution and L is
  undefined there.
---

# CLAIM-517: A successor regulator keeps a viable set positively invariant if, at every boundary context, its response distribution is within γ/L in total variation of a regulator that certifies inward margin γ, the dynamics being L-Lipschitz in that distribution; an average distillation loss certifies this only through coverage of the boundary contexts, so fidelity measured in ordinary operation certifies nothing about viability

## The claim

Let a physical state x evolve as ẋ = F(x, p(· | s)), where p is a
regulator's response distribution in context s, F is Lipschitz in x and
L-Lipschitz in p under total variation. Let K be a closed set regular
enough for Nagumo's theorem, and suppose a reference regulator p* gives
n·F(x, p*) ≤ −γ < 0 at every boundary point x with outward normal n, in
every context the boundary meets. Then any successor p with
TV(p(· | s), p*(· | s)) < γ/L at those contexts gives
n·F(x, p) ≤ −γ + L·TV < 0, so K stays positively invariant ([THEORY-134](../theory.d/THEORY-134.md)).

A distillation loss is an average. If the successor was trained to
forward KL ε under a context distribution μ, Pinsker and Jensen give
E_μ TV ≤ √(ε/2), which bounds nothing at any one context. With finitely
many boundary contexts each sampled with probability at least μ_min,
TV ≤ √(ε/(2μ_min)) at each, so ε < 2μ_min(γ/L)² suffices. Under a
deployment distribution ν with dν/dμ ≤ M, E_ν TV ≤ √(Mε/2).

A16: "A distillation procedure cannot certify the preservation of
capacities under interventions that its transmission regime never
samples." The contexts at the boundary of viability are those that
ordinary operation rarely visits, so a successor faithful on ordinary
operation can be arbitrarily wrong exactly where viability is decided.
This is the coverage form of [CLAIM-407](CLAIM-407.md): closure under ordinary dynamics
does not fix responses to intervention.

## What it does not say

- That distillation preserves viability in practice. The condition is
  sufficient, and it asks for coverage that ordinary training does not
  supply.
- That fidelity is lineage. A successor meeting the bound is a faithful
  student; whether it continues the predecessor is [CLAIM-329](CLAIM-329.md)'s question.

## Note of 2026-11-04: Guigues, Kleywegt and Nascimento, "Policies for the Operation of an Ambulance Fleet", read

The authors say their local preparedness approximation "may be inaccurate if demand is large relative to supply" ([LIT-2066](../literature.d/LIT-2066.md)). The metric is least reliable in high-load contexts, which qualifies, by analogy, any reliance on fidelity under ordinary load. Nothing formal links the two. No status changes.

## Note of 2026-11-04: Rockafellar and Uryasev, "Optimization of conditional value-at-risk", read

Rockafellar and Uryasev (2000), [LIT-2052](../literature.d/LIT-2052.md), read in [NOTE-1623](../notes.d/NOTE-1623.md), give the standard formal way to make an objective depend on the tail of a loss distribution rather than its bulk: minimizing CVaR is a convex program, and on sampled scenarios a linear one. That qualifies this claim by analogy only, as the same stance as attending to boundary contexts rather than ordinary operation. It proves nothing about viability or positive invariance, and its own examples show that rare scenarios must be sampled heavily. Whether a tail-risk objective could certify the boundary coverage this claim asks for is left open. No status changes.
