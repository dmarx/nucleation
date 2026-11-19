---
status: Open
title: 'In a trained recurrent network with symmetry-related ordered phases, do domain walls, local causal-state coherent structures, concentrations of local transfer entropy and intervention-identified operative structures pick out the same features, and where do they come apart?'
version: 1
tags:
- representation-learning
- complex-systems
- individuation
date: '2026-11-19'
line:
- learned-structure
- distributed-agency
summary: >-
  A's, from A12 §3–4 and A15 §3 and §10 (Experiment B) of the exchange
  "Topological protection explained" (2026-11-18), after the owner offered
  Iqbal and Welling's defects in deep networks ([LIT-tmp01nqp](../literature.d/LIT-tmp01nqp.md)) as an
  example of informative features emerging in learning (U6). A's slogan:
  "Spatial defect ≠ Predictive coherent structure ≠ Causal computational
  mechanism". The record holds the separations in general: [CLAIM-474](../claims.d/CLAIM-474.md)'s
  achievements are partially ordered, [CLAIM-407](../claims.d/CLAIM-407.md) shows that closure need not
  preserve the response to intervention, and [CLAIM-152](../claims.d/CLAIM-152.md) makes sufficiency
  relative to a target. What it does not hold is the comparison on a
  learned feature. The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: LIT-tmp6x1cq LIT-tmpn17zh — Deferred; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CLAIM-694 SYNTHESIS-079 THEORY-1507 THEORY-tmpvtafk — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: NOTE-tmpdcvze — Skimmed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: LIT-tmp01nqp — Unfetched; cited in this filing of 2026-11-19 -->

# QUESTION-tmpcb0bf: In a trained recurrent network with symmetry-related ordered phases, do domain walls, local causal-state coherent structures, concentrations of local transfer entropy and intervention-identified operative structures pick out the same features, and where do they come apart?

## Why it is a question

A12 §4 of the exchange "Topological protection explained"
(https://chatgpt.com/share/6afe6dd0-9d78-83ea-9782-f55680665dcf) proposed
measuring three properties of a defect separately: that it is
topologically stable, that it carries task information, and that it is
causally used. A15 §3 added Rupe and Crutchfield's local causal states
([LIT-tmpn17zh](../literature.d/LIT-tmpn17zh.md)), which pick out coherent structures by their predictive
light cones, the spatiotemporal form of [TERM-062](../terms.d/TERM-062.md)'s causal state, and local
transfer entropy ([THEORY-702](../theory.d/THEORY-702.md), from [LIT-1175](../literature.d/LIT-1175.md)). A12's interventional test:
"intervene on a latent state to move a domain wall while approximately
preserving the surrounding ordered configurations", with causal
abstraction ([LIT-tmp6x1cq](../literature.d/LIT-tmp6x1cq.md)) as the criterion.

## What the record already says

- The criteria need not agree: [CLAIM-474](../claims.d/CLAIM-474.md), [CLAIM-401](../claims.d/CLAIM-401.md), [CLAIM-405](../claims.d/CLAIM-405.md).
- Prediction is not intervention: [CLAIM-407](../claims.d/CLAIM-407.md), [SYNTHESIS-079](../syntheses.d/SYNTHESIS-079.md).
- A topological charge fixes a sector, not a token ([CLAIM-694](../claims.d/CLAIM-694.md)), and a
  closed wall lies in the trivial sector ([THEORY-1507](../theory.d/THEORY-1507.md)). Whether walls
  between oscillator domains are protected depends on whether the vacua
  are disconnected; with isotropic coupling on a sphere they are not
  ([NOTE-tmpdcvze](../notes.d/NOTE-tmpdcvze.md)).
- Interchange interventions can succeed in frozen random networks
  ([THEORY-1002](../theory.d/THEORY-1002.md)), so an interventional criterion needs that control.

## What would answer it

A family of small recurrent networks with a Z2 symmetry, trained on a
task whose answer depends on boundaries in the input (A15 Experiment B).
Compute the four candidate partitions of the hidden field and compare
them; move walls by intervention; compare a closed wall, which can shrink,
with one anchored by boundary conditions (A12 §6, A15 §9). A15's
Experiment E adds the spectrum linearized around a wall, to see whether a
wall hosts its own modes ([CLAIM-164](../claims.d/CLAIM-164.md)).

## Bearing so far

The authors' continuous-symmetry paper ([THEORY-tmpvtafk](../theory.d/THEORY-tmpvtafk.md)) shows a
transition whose functional consequence depends on equivariance; its
vortices are individuated descriptively and dynamically, with no role
shown ([NOTE-tmpsdqio](../notes.d/NOTE-tmpsdqio.md)).

## Note of 2026-11-19: readings for the exchange "Topological protection explained"

Geiger and colleagues (THEORY-tmp1cus0), skimmed for definitions: supports the interventional arm by making its criterion precise. A wall is a computational feature if a high-level model with a wall variable abstracts the network under an alignment, tested by (distributed) interchange interventions and scored by interchange intervention accuracy (Definitions 44, 46, 48). Remark 47 restricts tests to values the network realizes on some input, so moving a wall must be an interchange from a source input with the wall elsewhere. It gives no random-network control, which THEORY-1002 requires.

Jacobs and colleagues (THEORY-tmpctik9), read: qualifies the design of Experiment B. They train locally connected recurrent networks on a task whose answer depends on boundaries in the input, and the learned dynamics make interfaces, soft boundaries from a jump in natural frequency, which reflect waves and bring shape information to each pixel. But the interfaces are set by the input encoder, not walls between symmetry-related phases, and the waves' role is shown by correlations and readout comparisons, not by intervention.

Keller and colleagues (THEORY-tmpuy990), read: leaves the question open. A recurrent network learns travelling waves on a ring that hold the recent past, a spatially organized carrier of task information, but with no ordered phases, walls or defects. Their test of whether the waves matter compares models (initialization, freezing, a wave-free control) and does not intervene inside a trained network. A wave field is a further candidate partition beside the question's four, one whose features are inputs in transit rather than localized structures.

Masumori and colleagues (THEORY-tmp3vfqj), read: bears on the question from outside its setting. In a trained neural cellular automaton, sites of high fluctuation coincide with concentrations of transfer entropy, while per-cell vulnerability to perturbation follows mean state magnitude (r = 0.639) more than fluctuation (r = 0.325). So two criteria pick partly different sites in one learned field. Their intervention blocks small updates outside a disc, not at the cores, so whether the cores are operative is left open. No symmetry-related phases are involved.

Rupe and Crutchfield (THEORY-tmpgs5bb), read: sharpens the predictive criterion. Domains are where the local causal-state field has a space–time shift symmetry group, and coherent structures are localized, persistent deviations from it. A defect counts only where a discrete domain symmetry is locally broken; a global change of symmetry gives a new domain instead. They show the criterion only on deterministic binary cellular automata, and stochastic domains need a hand-applied filter. A trained network's continuous hidden field would need an estimator and a tolerance the paper does not give.

Kaschube, Schnabel and Wolf (THEORY-tmpg9anb, read as a stand-in for LIT-tmpdedmw): leaves the question open. Pinwheels are topological point defects of a map formed by activity-dependent development, and the paper treats them only as countable markers whose density tests the developmental model, assigning them no function. That fits A15's reading of them as defects that need not be functional units, but it neither shows that they lack a function nor compares any two criteria.

No status change.
