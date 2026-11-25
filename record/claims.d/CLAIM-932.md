---
number: 932
status: Proposed
formerly:
- CLAIM-tmpwx1cm
title: 'In small trained Z2-symmetric recurrent lattices, domain walls, local causal-state coherent structures and intervention-identified operative sites pick out the same features while the field runs free, but local transfer entropy misses walls that are pinned, and the interventional criterion comes apart from the others while the input that set the walls is still on'
version: 1
role: thesis
warrant: empirical
tags:
- representation-learning
- complex-systems
- causality
date: '2026-11-22'
bears_on:
- QUESTION-491
grounds:
- CASE-354
line:
- learned-structure
- distributed-agency
defeated_if: >-
  A rerun of the study in scratch/studies/lead-040, or a variant within the
  same scope (one-dimensional Z2-equivariant recurrent lattices trained to
  a wall-dependent answer, with static walls), in which, after the input
  is removed, fewer than about four fifths of wall sites are operative or
  interchange accuracy against the wall model falls below about 0.8; or in
  which local transfer entropy concentrates at pinned walls; or in which
  the same walls are operative while the input is still on. A change of
  partition thresholds that reverses one of these findings defeats it
  for that finding. Results on networks whose walls move or oscillate do
  not, since the claim is limited to pinned walls.
summary: >-
  From [CASE-354](../cases.d/CASE-354.md), a partial answer to [QUESTION-491](../questions.d/QUESTION-491.md) on a learned
  feature. In five of six trained networks with static ordered phases, and
  after the input was removed, every wall site lay in a coherent structure,
  95 to 100% of wall sites were operative, and moving a wall by interchange
  gave the answer the wall model predicts (IIA 0.92 to 0.96, against 0.10
  to 0.21 for frozen random controls). Local transfer entropy was near zero
  at the pinned walls: a stored feature through which nothing flows is
  invisible to a flow criterion. While the input was on, the same walls
  were present and predictive but not operative (interchange accuracy 0.03
  to 0.32), because the input, not the wall, then carried the answer. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-354 THEORY-2028 THEORY-2048 — Proposed or new; cited in this filing of 2026-11-22 -->

# CLAIM-932: In small trained Z2-symmetric recurrent lattices, domain walls, local causal-state coherent structures and intervention-identified operative sites pick out the same features while the field runs free, but local transfer entropy misses walls that are pinned, and the interventional criterion comes apart from the others while the input that set the walls is still on

## The claim

[QUESTION-491](../questions.d/QUESTION-491.md) asks whether four criteria pick out the same features of a trained recurrent network with symmetry-related ordered phases, and where they come apart. On the networks of [CASE-354](../cases.d/CASE-354.md) the answer has three parts.

1. **Agreement while the field is free.** Once the input is removed, the walls (neighbouring states on opposite sides), the coherent structures of the local causal-state field ([THEORY-2028](../theory.d/THEORY-2028.md)) and the operative sites pick out the same features, up to the structures' wider reach. Moving a wall moves the answer as a model with the wall as a variable predicts.
2. **Transfer entropy comes apart on stored features.** A pinned wall holds task information without anything passing through it, so local transfer entropy ([THEORY-702](../theory.d/THEORY-702.md)) does not find it. Flow criteria find features in transit, not features in storage. This agrees with [THEORY-2048](../theory.d/THEORY-2048.md)'s waves as "inputs in transit", taken there as a further candidate partition.
3. **Intervention comes apart in time.** The same walls are present and predictive while the input is on, but not operative: an intervention on them is undone by the input. Whether a feature is operative depends on what else carries the answer at that moment, as [CLAIM-407](../claims.d/CLAIM-407.md) leads one to expect.

## Scope

- One dimension, 32 sites, six trained networks. The agreements hold for pinned walls.
- One network learned an oscillating phase instead, and the claim is silent on it.
- The partitions rest on thresholds that were not swept. The agreement between walls and coherent structures is partly built into the domain criterion.
- Closed walls that shrink by themselves, and boundary conditions as hard constraints, were not reached. The boundary result in the case is reported there and not claimed here.
