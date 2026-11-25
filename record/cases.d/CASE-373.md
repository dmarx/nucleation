---
number: 373
status: Proposed
formerly:
- CASE-tmpxkvpz
title: 'An executed study: two compatibility-equivalent three-bit mechanisms probed at rising move budgets in numpy, with the distinguish-or-not verdict recorded at each budget, a reset-versus-acted-on control, and a constructed family whose distinguishing budget is any chosen length'
version: 1
standing: documented
kind: executed-study
tags:
- complex-systems
- mathematics
- individuation
date: '2026-11-22'
variant_of:
- CASE-202
illustrates:
- CLAIM-583
bears_on:
- QUESTION-382
line:
- realizability
- formal-apparatus
---
<!-- inactive-ok-file: CASE-202 CLAIM-968 — CASE-202 is the Proposed design this executes; CLAIM-968 is the finding filed beside it in this batch, grounded in this study -->

# CASE-373: An executed study: two compatibility-equivalent three-bit mechanisms probed at rising move budgets in numpy, with the distinguish-or-not verdict recorded at each budget, a reset-versus-acted-on control, and a constructed family whose distinguishing budget is any chosen length

## The case

This runs the individuation-by-probing component [CASE-202](CASE-202.md) proposes, on the
seed pair [CLAIM-583](../claims.d/CLAIM-583.md) constructs, holding the pair of mechanisms fixed and
varying what the observer may do to them (the respect in which [CASE-202](CASE-202.md)
varies [CASE-179](CASE-179.md)).

**The model.** A resource-bounded constraint system ([TERM-114](../terms.d/TERM-114.md)) is written as a
finite transition system: a set of admissible n-bit configurations; a fixed
local move rule, a single bit flip that stays inside the admissible set
(Gopalan et al.'s solution graph, as [CLAIM-583](../claims.d/CLAIM-583.md) uses); named demands, each
asking that a configuration equal a target; and a probe budget b, the number
of moves a probe may attempt. The probe readout at budget b is the
reachability-between-demands relation: from a configuration meeting demand
Dᵢ, which demands become reachable within b admissible moves. At b = 0 this
is the static family [CASE-202](CASE-202.md) names, which "asks of a configuration only
which demands it meets". The verdict on the pair at budget b is whether the
two mechanisms' readouts differ. Probing runs at b = 0, 1, 2, …, and records
the least budget at which the verdict reaches its final value and stays there.

**The probe family is fixed before the pair is seen** ([CLAIM-322](../claims.d/CLAIM-322.md)): the
reachability-between-demands readout is defined for any finite mechanism,
not selected to separate this pair, and the same family is applied to every
pair below, including ones it does not separate.

**The seed pair ([CLAIM-583](../claims.d/CLAIM-583.md)).** A = {000, 111} with D₁ = {000}, D₂ = {111};
B = {000, 001} with D₁ = {000}, D₂ = {001}. Both have the compatibility
complex {∅, {D₁}, {D₂}} ([CLAIM-347](../claims.d/CLAIM-347.md)), the same single-flip move rule and the
same (zero) costs. Result:

- at budget 0 the two readouts are **equal** — indistinguishable under the
  static family;
- at budget 1 they **part**: in B the D₁-configuration reaches a
  D₂-configuration in one admissible move (000 ↔ 001), in A it does not (000
  and 111 are three flips apart and no intermediate is admissible);
- the verdict **stabilizes at budget 1** and the pair stays distinguishable
  at every higher budget, as it must along nested families ([CLAIM-574](../claims.d/CLAIM-574.md)).

**The control** ([CASE-202](CASE-202.md): separate "discovering a difference" from
"creating" one). Every probe is run on a reset copy and on a copy earlier
probes have acted on. The prober only queries reachability and never mutates
the admissible set or the move rule, so the two readouts coincide at every
budget: the difference found is discovered in the mechanism, not made by the
probing. An identical-mechanism pair (B against B) is never distinguished at
any budget, a second control against artefacts of the procedure.

**That the parting budget is a measurement, not a design choice.** A
constructed family realizes any finite distinguishing budget L: both
mechanisms take D₁ = 0ⁿ and D₂ = 1ⁿ, B admits a Hamming path of length L
between them and A admits only the two endpoints, so the complexes, move
rules and costs agree and the readouts agree at every budget below L, and
the pair parts exactly at budget L. Run for L = 2…5, the stabilization
budget equals L in each case. The seed pair is the sharpest case of the same
phenomenon, its distinguishing move costing one.

**How it was run.** Pure numpy, CPU, single BLAS thread, well under a second;
no network. Fourteen pytest tests check the static-family agreement, the
budget-1 parting, the per-budget monotonicity, the two controls, the
tunable-threshold family and the complex equality. Script, results and tests
are in `scratch/studies/lead-135/` (see its README to rerun). The finding is
filed as [CLAIM-968](../claims.d/CLAIM-968.md).

## What it can show

Being an executed study of a construction, its facts are its definitions and
its re-runnable computations. It shows that [CASE-202](CASE-202.md)'s probing procedure, as
built here, recovers [CLAIM-583](../claims.d/CLAIM-583.md)'s separation of reachability from compatibility
by a method independent of the hand enumeration [CLAIM-583](../claims.d/CLAIM-583.md) used, and that the
budget at which a reachability distinction first appears between
compatibility-equivalent systems is a finite threshold that a construction
can set to any chosen length. For [QUESTION-382](../questions.d/QUESTION-382.md) it gives the maintenance-free
form of an interface equivalence (agreement under the static family) that
fails once the process layer is counted, with the failure budget measured.

## What it cannot show

- **That the distinction is of individuals.** A readout that separates two
  mechanisms is descriptive individuation in [TERM-088](../terms.d/TERM-088.md)'s sense; the dynamical,
  constitutive and autonomy senses need more.
- **The maintenance and architecture-change readouts of [CASE-202](CASE-202.md).** This
  study runs the reachability readout and the discovering-versus-creating
  control only; regeneration after turnover ([CLAIM-566](../claims.d/CLAIM-566.md)) and survival of the
  distinction across a declared change of architecture are not modelled here.
- **Anything about organizations**, the mechanisms being abstract.

The wording is the assistant's (Claude, in this session); adopting it is the
owner's call.
