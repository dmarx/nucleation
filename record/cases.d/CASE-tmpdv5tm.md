---
status: Proposed
title: 'The imagined owner, built and run: a distributed-control plant whose self-model is either accurate about the division of labour or attributes control to one centralized owner; with the two self-models matched in parameters and reconstructing the aggregate outcome exactly, the centralized one still names the wrong component as the cause on about four errors in five, spreads blame toward the owner''s global command, and, driving governance, strips more legitimate gain from innocent components to cut the same errors'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-134. The code,
    tests and result files are committed beside it under
    scratch/studies/lead-134/.
standing: documented
kind: executed-study
tags:
- self
- agency
date: '2026-11-22'
line:
- evidence-for-experience
- organizational-affect
variant_of:
- CASE-114
illustrates:
- CLAIM-355
draws_on:
- THEORY-646
---
<!-- inactive-ok-file: CLAIM-355 THEORY-646 — Proposed; the claim this build tests and Drayson's objection its result is set against, both cited as open -->
<!-- inactive-ok-file: CLAIM-tmppxyo3 — the finding filed from this build (new, Proposed) -->

# CASE-tmpdv5tm: The imagined owner, built and run: a distributed-control plant whose self-model is either accurate about the division of labour or attributes control to one centralized owner; with the two self-models matched in parameters and reconstructing the aggregate outcome exactly, the centralized one still names the wrong component as the cause on about four errors in five, spreads blame toward the owner's global command, and, driving governance, strips more legitimate gain from innocent components to cut the same errors

## What was built

[CASE-114](CASE-114.md)'s Experiment C, in numpy ([LEAD-134](../leads.d/LEAD-134.md)). A plant has K
components, each emitting an independent drive deviation; the outcome is their
sum. Control is distributed: no component determines the outcome, and each
contributes a share that varies with its own drive. An error is a single
component's fault excursion; the simulator records which component faulted and
when, apart from any self-model, as the true cause.

Two self-models observe the same per-component signals and both reconstruct
the aggregate outcome. They differ only in the causal graph they assume:

- **accurate** — K parallel autonomous components, the true graph;
- **centralized** — one owner command that drives every effector uniformly, a
  star graph. It explains each outcome as the owner's command deviating, spread
  over the effectors.

Held fixed, per [CASE-114](CASE-114.md): the distributed control and the behaviour. In the
open-loop phase the self-model only narrates, so the two systems are the same
run and only the reports differ. The closed-loop phase lets the self-model's
blame drive governance (reduce the blamed component's gain); this is A27 §12's
loop, which [CASE-114](CASE-114.md) warns breaks the held-fixed equivalence, and it is where
A27's fourth measure — revising governance after an error — lives.

## How the main threat was met

[CASE-114](CASE-114.md)'s chief threat is that an accurate model simply carries more
information, so worse attribution would show only that a coarser model answers
component questions less well, which is true of any compression. The build
removes that reading three ways, all checked in the grid: the two self-models
take **identical inputs**, have the **same parameter count**, and **reconstruct
the aggregate outcome exactly** (reconstruction error 0 for the accurate model
and ~1e-15 for the centralized one across all 60 configurations). The
centralized model is therefore not a lossy summary of the outcome — it
reproduces the behaviour perfectly — and is not short of information about the
components it is asked about. It is simply wrong about the causal topology. Any
attribution divergence is wrong-about-control, not merely-coarser.

## What it shows

Across 60 configurations (K ∈ {3, 5, 8}, equal and graded gains, ten seeds):

- **Cause identification.** The accurate self-model names the recorded culprit
  on 94% of errors; the centralized one on 21%, at chance (1/K), because it
  spreads blame uniformly and credits the owner's global command. The
  misattribution is in a predictable direction.
- **Attribution mass.** The accurate model places 0.56 of the attributed
  magnitude on the true cause; the centralized model places 0.22, the uniform
  share.
- **Judgment of authorship.** The accurate model reports distributed control
  tracking the one culprit per event; the centralized model reports a single
  owner acting through all effectors (near-maximal entropy over components).
- **Governance after error.** Because the centralized model cannot localize the
  rogue component, to cut the same errors it suppresses the whole system: it
  strips more legitimate gain from the innocent components than the accurate
  model does (0.46 vs 0.34, on every one of the 60 configurations) and incurs
  more errors over the course of the revision (accurate lower on 54 of 60).

So a unified self-model, matched in capacity and reproducing behaviour exactly,
systematically misdescribes who controls what. The error is located in the
attribution and belongs to the system that holds the self-model, as
[CLAIM-355](../claims.d/CLAIM-355.md) says it must. Against Drayson's objection ([THEORY-646](../theory.d/THEORY-646.md)), the
represented single owner here has **no** truthmaker in the true, distributed
division of control: the centralized self-model's owner is a misdescription,
not a lossy but faithful compression. This is the case [CLAIM-355](../claims.d/CLAIM-355.md)'s note of
2026-11-06 says the record lacked, now run. The finding is filed as
[CLAIM-tmppxyo3](../claims.d/CLAIM-tmppxyo3.md).

## What it cannot show

- **That a distributed agent would come to represent a single owner.** The
  modeller writes both self-models, so the content is the modeller's
  ([CLAIM-288](../claims.d/CLAIM-288.md)). The build shows what the centralized content *does* once
  present, not that it would arise.
- **Anything about phenomenal properties.** It tests attribution of control, as
  [CASE-114](CASE-114.md) stipulates, not whether any state is felt.
- The construction is stipulated: the two causal graphs and the governance
  lever are the modeller's choices, defended in the study's README but not
  forced by the phenomena. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
