---
number: 217
status: Active
formerly:
- CASE-tmpj3cmd
title: 'A four-state branching model of assembly, unassembled, productive nucleus, trap and folded, in which three designs with the same target yield 59.3, 76.2 and 29.6 %, and scaling every supply by the same factor leaves the yield unchanged only while the competing exits from each state have the same molecularity'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the status review's ruling (the owner delegated these
    rulings; ADR-057): a construction (ADR-042) whose three designs,
    uniform-scaling table and escapable-trap yields were re-run by a
    second checker with python3 -I. Standing fictional is kept.
standing: fictional
kind: construction
tags:
- complex-systems
- mathematics
- natural-sciences
date: '2026-11-05'
line:
- realizability
illustrates:
- CLAIM-567
summary: >-
  A's model, from A's second synthesis on DNA origami, pasted by the owner
  on 2026-11-05, §2, with the assistant's extension. From U the system
  enters a productive nucleus N at rate α or a trap K at rate β; from N it
  completes to F at γ or falls into K at δ. With K and F absorbing,
  P_F = α/(α+β) · γ/(γ+δ). A's three designs (baseline, guided nucleation,
  competing early binding) share the target and yield 59.3, 76.2 and
  29.6 %, checked with python3 -I. A notes that scaling α and β together
  leaves the first branch unchanged. The assistant adds that this holds
  only when both exits have the same molecularity. If entering the trap
  from N binds a further molecule and completing does not, a uniform
  increase of supply by λ gives P_F = α/(α+β) · γ/(γ+λδ), which falls from
  59.3 % at λ = 1 to 19.0 % at λ = 20. The rates are A's invented
  illustrative parameters, not measurements. The model is A's; the
  extension is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---

# CASE-217: A four-state branching model of assembly, unassembled, productive nucleus, trap and folded, in which three designs with the same target yield 59.3, 76.2 and 29.6 %, and scaling every supply by the same factor leaves the yield unchanged only while the competing exits from each state have the same molecularity

## The case

A's network: U → N at α, U → K at β, N → F at γ, N → K at δ. "Suppose the
trap is effectively irreversible over the observation horizon, and the
completed structure is likewise retained during that horizon." Then

  P_F = α/(α+β) · γ/(γ+δ).

A's three designs, recomputed with python3 -I:

| Design | α | β | γ | δ | P_F |
|---|---|---|---|---|---|
| Baseline | 1 | 0.5 | 2 | 0.25 | 59.3 % |
| Guided nucleation | 3 | 0.5 | 2 | 0.25 | 76.2 % |
| Competing early binding | 1 | 2 | 2 | 0.25 | 29.6 % |

**Uniform scaling of supply.** The assistant's extension. Raise every
component's concentration by λ. A step that binds a further molecule
(bimolecular) speeds up by λ, while a step within one molecule
(intramolecular) does not. At the baseline:

| λ | α, β bimolecular only | and N → K bimolecular | and N → F bimolecular too |
|---|---|---|---|
| 0.5 | 0.593 | 0.627 | 0.593 |
| 1 | 0.593 | 0.593 | 0.593 |
| 2 | 0.593 | 0.533 | 0.593 |
| 5 | 0.593 | 0.410 | 0.593 |
| 10 | 0.593 | 0.296 | 0.593 |
| 20 | 0.593 | 0.190 | 0.593 |

**A trap that can be escaped.** A's caveat: "A long-lived trap is not
necessarily an absorbing state". With K → U at 0.01, the yield at times 10,
100 and 1000 is 0.612, 0.772 and 0.999. So finite-horizon yield and
eventual yield part.

## What it can show

- **One target, different chances of forming it** ([CLAIM-567](../claims.d/CLAIM-567.md)): A's boxed point that
  an identical target does not imply an identical probability of formation.
- **Abundance can help, be neutral or hurt.** Whether more of everything
  changes yield depends, at each branch point, on whether the competing
  steps bind further molecules. This is the assistant's [CLAIM-598](../claims.d/CLAIM-598.md).
- **It matches one reading.** Majikes et al. 2021 find for a single fold
  that the folded share is j/(j + S₀), with j the fold's effective
  concentration and S₀ the staple concentration. That has the same form as
  γ/(γ + λδ): intramolecular closure against bimolecular blocking.

Being fictional, with invented rates, it shows the logic and not the size
of any effect in DNA origami.
