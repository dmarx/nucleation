---
number: 494
status: Open
formerly:
- QUESTION-tmprj00l
title: 'In a percept–action loop with feedback, does the memory that minimizes dissipation retain the interventional partition of histories (the causal information bottleneck), the predictive partition, or neither, once the costs of building, maintaining, operating and revising it are counted?'
version: 1
tags:
- thermodynamics
- information-theory
- learning-theory
date: '2026-11-19'
line:
- learned-structure
- formal-apparatus
refines:
- QUESTION-191
summary: >-
  A's, from A65 §4 and §9–10 of the exchange "Topological protection
  explained" (2026-11-19), after the owner asked to "connect this to
  information thermodynamics" (U29) and remarked "sounds like we're getting
  into active learning territory now" (U30). Still and colleagues relate
  dissipation to nonpredictive memory only for a system driven without
  feedback ([THEORY-026](../theory.d/THEORY-026.md)). The causal information bottleneck's optimum is
  the partition by response to intervention ([THEORY-1125](../theory.d/THEORY-1125.md), [THEORY-1146](../theory.d/THEORY-1146.md)),
  which A65 rebuilt as an "intervention-response signature". A proposed an
  "intervention-relative, physically costed information bottleneck" and
  called it a proposal, not a theorem. A learner that chooses its
  observations breaks the no-feedback condition, so the passive result does
  not reach it. The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-2011 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: THEORY-1646 THEORY-817 — Proposed; cited in this filing of 2026-11-19 -->

# QUESTION-494: In a percept–action loop with feedback, does the memory that minimizes dissipation retain the interventional partition of histories (the causal information bottleneck), the predictive partition, or neither, once the costs of building, maintaining, operating and revising it are counted?

## Why it is a question

A65 §4 of the exchange "Topological protection explained"
(https://chatgpt.com/share/6afe6dd0-9d78-83ea-9782-f55680665dcf): "The
appropriate target of learning is not always the future that will
occur." Without feedback, [THEORY-026](../theory.d/THEORY-026.md) makes nonpredictive memory the
wasteful part. With feedback, the record has one proved binary channel
([THEORY-026](../theory.d/THEORY-026.md)'s narrowed clause) and a broader Proposed account
([THEORY-817](../theory.d/THEORY-817.md)). Separately, the causal information bottleneck optimizes for
the partition by p(y | do(x)) ([THEORY-1125](../theory.d/THEORY-1125.md)), which can differ from the
predictive partition under confounding ([THEORY-1146](../theory.d/THEORY-1146.md)). Nothing joins the
two: which partition a physically costed memory should keep when the
agent acts.

## Scope

- An abstract many-to-one map is not physical erasure, and Landauer prices
  only logically irreversible steps ([THEORY-030](../theory.d/THEORY-030.md)).
- Variational free energy is not thermodynamic free energy (A69 §8).
- Thermodynamic viability is not legitimacy ([CLAIM-075](../claims.d/CLAIM-075.md)), and semantic
  information is relative to a viability function the analyst chooses
  ([THEORY-1646](../theory.d/THEORY-1646.md)).

## What would answer it

A65 §10's Experiment A: a finite-state stochastic memory coupled to an
environment with explicit energetic costs for acquiring, keeping, using
and resetting information. Compare memories that keep all recent history,
only predictive information, or only action-relevant information,
measuring mutual information, entropy production, success under
interventions and the cost of reconfiguring. First reproduce Still's
no-feedback result, then add feedback. A71 §10's Experiment III is the
same design. Still's 2020 derivation of a bottleneck from a dissipation
bound ([LIT-2832](../literature.d/LIT-2832.md)) is the nearest prior result, unread.

## Note of 2026-11-19: readings for the exchange "Topological protection explained"

Still ([THEORY-2011](../theory.d/THEORY-2011.md)), read from arXiv v3: leaves the question open and sharpens it. The dissipation-minimizing memory is the information bottleneck relative to Y, the variables the work-extraction device can manipulate, so "relevant" is already relative to action. But it is computed from the observational p(y|x), and the agent's action never changes the next cycle's data: the preparation is fixed and the marginals unchanged. It is the no-feedback first rung of Experiment A. The choice between the interventional and the predictive partition arises only once preparation depends on memory.

No status change.
