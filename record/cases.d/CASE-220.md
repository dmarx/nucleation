---
number: 220
status: Proposed
formerly:
- CASE-tmpvdu02
title: 'A proposed factorial assembly study: two scaffold routings of one target crossed with uniform or targeted early stabilization, at fixed geometry and component stock, measured by the committor of partial structures, so that a productive nucleus is one whose formation raises the chance of completion before failure and a trap one that lowers it'
version: 2
history:
- version: 2
  date: '2026-11-12'
  note: >-
    Draws on THEORY-1398 ("is the simulated instance"). First application
    of draws_on (ADR-095). No other change.
standing: stipulated
kind: proposed-study
tags:
- natural-sciences
- complex-systems
- mathematics
date: '2026-11-05'
line:
- realizability
variant_of:
- CASE-219
illustrates:
- CLAIM-567
- CLAIM-185
summary: >-
  A's design, from A's second synthesis on DNA origami, pasted by the owner
  on 2026-11-05, §§3 and 7. It varies A's earlier proposed study
  ([CASE-219](CASE-219.md)) in two respects: routing architecture becomes a factor,
  crossed with early stabilization, and the main measurement becomes the
  committor q(s) = Pr_s(τ_F < τ_K) of a partial structure s, the chance of
  reaching the target F before a designated failure set K. A productive
  nucleus is then one whose specified formation raises q, Δq_N > 0, and a
  trap one that lowers it, rather than any early or stable structure. Dunn
  et al. and DeLuca et al. ran the routing half in experiment and
  simulation. The wording is A's; adopting it is the owner's call.
draws_on:
- THEORY-1398
---
<!-- inactive-ok-file: ADR-095 — Proposed; the decision this entry's draws_on first applies, cited in its history -->
<!-- inactive-ok-file: CASE-219 CLAIM-185 CLAIM-184 — Proposed; the study it varies and the entries it would test -->

# CASE-220: A proposed factorial assembly study: two scaffold routings of one target crossed with uniform or targeted early stabilization, at fixed geometry and component stock, measured by the committor of partial structures, so that a productive nucleus is one whose formation raises the chance of completion before failure and a trap one that lowers it

## The case

A: "Hold fixed the required final geometry and the total quantity of
assembly components, to the extent that the physical design permits. Then
compare different routing architectures and controlled initial assembly
conditions."

| | Uniform initial conditions | Targeted early stabilization |
|---|---|---|
| Routing A | A1 | A2 |
| Routing B | B1 | B2 |

A notes: "The four conditions are proposed experiments, not observed
outcomes. The target fold must be verified as comparable across designs."
A's measurements:

- nucleation times and locations;
- the completion probability given particular early intermediates;
- the yield at a fixed horizon;
- the time spent in long-lived traps;
- the persistence of the completed structure under a later perturbation.

The key quantity is the committor, q(s) = Pr_s(τ_F < τ_K), and the effect
of forming a specified substructure N, Δq_N = q(s | do(N)) − q(s),
"provided the intervention is explicitly specified and physically
meaningful". In A's words: "A partial structure that appears quickly but
decreases that probability would be a kinetic trap, not a productive
nucleus."

## What it can show

- **A test for [CLAIM-185](../claims.d/CLAIM-185.md).** It asks when a persistent anchor helps, and
  separates productive nuclei from early structures that entrench
  ([CLAIM-184](../claims.d/CLAIM-184.md)).
- **Progress is not completion.** Partial structures with equal completion
  counts but different committors. DeLuca et al.'s run that was best folded
  at 1 s and second worst at 3.6 s ([THEORY-1398](../theory.d/THEORY-1398.md)) is the simulated instance.
- **Done in part already.** Dunn et al. vary seam routing and measure final
  shape distributions; Schneider, Möritz and Dietz delete early segments
  and find the intermediate abolished and folding slowed by hours. These are
  the routing column and an intervention on N, though neither measures a
  committor.

Being stipulated, it shows nothing until run. The committor needs a failure
set K declared in advance, so what counts as a trap is part of the design,
not a finding.

## Note of 2026-11-05: A's synthesis on the productive nucleus

From the third synthesis on DNA origami by another assistant (A), "The productive nucleus", pasted by the owner on 2026-11-05.

A's third synthesis refines the design into four interventions: a baseline, establishing the candidate nucleus, disrupting it, and establishing an alternative nucleus, in A's table: "Test whether productivity is specific to the arrangement rather than simply added stabilization". A adds the outcome to look for: stabilizing a nucleus that raises an intermediate's chance but lowers final yield. That "wouldn't refute the framework" but "would establish why productivity must be specified relative to a target and horizon". The alternative-nucleus arm also tests [CLAIM-599](../claims.d/CLAIM-599.md), whether productive relations combine.

No status changes.

## Note of 2026-11-05: A's predictions on productive nucleation

From the fourth synthesis on DNA origami by another assistant (A), "Predicting which organizations will successfully nucleate", pasted by the owner on 2026-11-05.

A's fourth synthesis enlarges the design. It has three or four candidate nucleating relations and two competing finished forms, with the inventory and resources fixed. It varies which relations come first, their strengths and how long support lasts, and records trajectories. A pairs each test with the rival it excludes: placement against more resources, structure against progress count, a stabilization sweep against degradation, complementarity against additivity, timing against total exposure, withdrawal against early completion, and competing targets against a silently privileged one. A notes the gap such a model would test: Aksel et al.'s design score ([NOTE-1642](../notes.d/NOTE-1642.md)) omits kinetics and inter-staple cooperativity.

No status changes.
