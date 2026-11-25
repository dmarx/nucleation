---
number: 109
status: Proposed
formerly:
- SYNTHESIS-tmp230me
title: 'Seeing splits categories, acting merges them'
statement: >-
  Growth in observing resource splits what can be told apart, growth in
  acting resource merges what can be turned into one another, and optimal
  categories at a larger budget can re-carve rather than refine: what the
  record holds on how categories change as resources grow
version: 1
defeated_if: >-
  A component misstated or misattributed here, with its scope conditions;
  an in-force entry of the record that states part of this theme left out
  without a reason given; or a link this account states that no component
  states. Its standing is its components': a component retired takes its
  clause with it.
tags:
- individuation
- information-theory
- learning-theory
date: '2026-11-20'
line:
- learning-and-inquiry
- realizability
- formal-apparatus
- learned-structure
integrates:
- CLAIM-557
- CLAIM-574
- CLAIM-581
- CLAIM-592
- CLAIM-387
- CLAIM-392
- CLAIM-409
- CLAIM-455
---
<!-- inactive-ok-file: CLAIM-799 CLAIM-827 CLAIM-837 CASE-301 CLAIM-826 TERM-138 — Proposed or new; filed 2026-11-21 from the exchange "Rich Get Richer Power Laws" -->

<!-- inactive-ok-file: CLAIM-770 CLAIM-780 CLAIM-781 — Proposed or Open; filed on 2026-11-21 and cited in this note -->
<!-- inactive-ok-file: CLAIM-823 CLAIM-802 CLAIM-834 ARG-132 CLAIM-839 CLAIM-849 CLAIM-809 ARG-148 CLAIM-814 — Proposed; filed 2026-11-21 from the exchange "Rich Get Richer Power Laws" and cited in the second note of that date -->

# SYNTHESIS-109: Seeing splits categories, acting merges them

*A thematic account, across lines, of principle P2 of the owner's manuscript (scratch/manuscripts/from-obstruction-to-reorganization/, §7.1, on its own branch). Filed at the owner's direction on 2026-11-20 after an independent reader's audit found the principle to be a conjunction of entries the record holds rather than a claim with content of its own ([ADR-075](../decisions.d/ADR-075.md), step 5; workbench entry of this date). It adds nothing; its standing is its components'. Its scope is a theme, not a line or a part of one, which [ADR-083](../decisions.d/ADR-083.md)'s one account per scope does not anticipate.*

## The account

**Two budgets pull in opposite directions.** [CLAIM-557](../claims.d/CLAIM-557.md) (Active, demonstrated, thesis): "More resource for observing splits what can be told apart, and more resource for acting merges what can be turned into one another". A system's budgeted individuation is therefore "indexed by a pair of budgets, not one".

**What can be told apart.** Along nested probe families compared on every probe, distinctions only grow, and objects told apart at a lower budget stay apart at every higher one ([CLAIM-574](../claims.d/CLAIM-574.md), Active, demonstrated). The guarantee needs both conditions: nested families, and comparison on every probe rather than an averaged distortion.

**What can be turned into one another.** Under peak-capacity costs on reversible moves, the configurations reachable within a budget form an equivalence at every budget, and these nest into one tree as the budget grows ([CLAIM-581](../claims.d/CLAIM-581.md), Active, demonstrated). Under additive costs they need not.

**Where the two meet.** The observer's partition and the system's partition agree exactly at partitions common to the observer's refinement chain and the system's merge tree. Which levels appear depends on the order of the probe costs ([CLAIM-592](../claims.d/CLAIM-592.md), Active, demonstrated).

**Optimal categories are a different object.** [CLAIM-387](../claims.d/CLAIM-387.md) and [CLAIM-392](../claims.d/CLAIM-392.md) (both Active, demonstrated) concern the *optimal* information-bottleneck partition at a budget, not what can be told apart. Optimal partitions at two budgets need not nest, with deterministic encoders ([CLAIM-387](../claims.d/CLAIM-387.md)) and with stochastic ones ([CLAIM-392](../claims.d/CLAIM-392.md)). Raising the budget can therefore reorganize the optimum rather than split it.

**Two further limits on the idea that more resource means finer categories.**

- **Closure.** A deficiency of sufficiency for a fixed target cannot increase under refinement, but informational closure is monotone in neither direction ([CLAIM-409](../claims.d/CLAIM-409.md), Active, demonstrated).
- **Bounded observers.** For one bounded observer, a transformation of a representation can make one task's distinction legible and another's illegible at once ([CLAIM-455](../claims.d/CLAIM-455.md), Active, demonstrated).

## Not stated on the record

- **Only an ideal observer with nested probes is guaranteed only to split.** The manuscript's P2 stated this, and it is false as stated. [NOTE-676](../notes.d/NOTE-676.md) (Read) records a nesting result for the information bottleneck with side information, in which "penalising irrelevant information can only prune the IB tree". So some rate-limited learners are guaranteed nested optima. [CLAIM-387](../claims.d/CLAIM-387.md)'s own limits allow that annealed category systems may nest. Growth in the acting budget, under [CLAIM-581](../claims.d/CLAIM-581.md)'s conditions, only merges.
- **That what can be told apart and what is optimal to keep are one ordering.** The record keeps them apart ([CLAIM-574](../claims.d/CLAIM-574.md) against [CLAIM-387](../claims.d/CLAIM-387.md)). The manuscript's P2 merged them.

## What it does not say

- That any particular learner re-carves.
- That splitting is the normal case. Which case holds depends on the conditions each component states.

## Note of 2026-11-21: where a level of the tree comes and goes

Filed since, and candidates for this account's components at its next synthesis review:

- **[CLAIM-770](../claims.d/CLAIM-770.md)** (Proposed, demonstrated): the tree of classes reachable within a budget keeps its shape while barriers move, and changes only where two barriers cross. A distinction between levels comes into being or passes away at such a crossing. This is a case, in one model, of the re-carving this account's optimal-partition clause describes.
- **[CLAIM-780](../claims.d/CLAIM-780.md)** and **[CLAIM-781](../claims.d/CLAIM-781.md)** (Proposed): how a hierarchy's levels show in a chain's time geometry, and what rate separation between levels does.
- **[QUESTION-500](../questions.d/QUESTION-500.md)** and **[QUESTION-501](../questions.d/QUESTION-501.md)** (Open): what rate ratio is enough for a level to show, and whether well-separated levels require separated rates.

## Note of 2026-11-21: the exchange "Rich Get Richer Power Laws"

This account's "what can be told apart" is the second of the three senses of separation that [TERM-138](../terms.d/TERM-138.md) (filed the same day) keeps apart: separation of classes. The exchange adds two things that bear on it, for its next version to weigh.

- **Spectral detectability as a budgeted telling-apart.** The threshold above which sample PCA finds a planted direction, β > √(D/N) ([CLAIM-799](../claims.d/CLAIM-799.md), [CLAIM-827](../claims.d/CLAIM-827.md)), falls as the number of samples N grows. That is the account's first clause in a concrete case: more observing resource splits what can be told apart. The distinction an unsupervised observer can draw appears at a budget that the threshold fixes. [CLAIM-837](../claims.d/CLAIM-837.md) gives the lag between a feature's onset and its detection, which scales as √(D/N).
- **The observer's kind matters as much as its budget.** At the same budget, a trained linear readout tells the classes apart (74% accurate) where PCA tells nothing ([CASE-301](../cases.d/CASE-301.md), β = 0.4 against a threshold of 0.5). So "what can be told apart" is relative to the observer's probe family as well as its resource, as [CLAIM-455](../claims.d/CLAIM-455.md) already says for bounded observers. The exchange's case separates a supervised from an unsupervised observer at equal N.
- **Telling apart without levels.** Near a critical point the class is easy to tell while no level separates ([CLAIM-826](../claims.d/CLAIM-826.md)). Separation of classes and separation of levels are independent.

No component, status or link of this account is changed. The note is the assistant's (Claude, in this session).

## Note of 2026-11-21: re-carving and orders in a learner

The note above concerns this account's first clause, what can be told apart. The same exchange also bears on its optimal-partition clause and on its claim that refinement is one case among several. For the next version to weigh:

- **A learner's transition as a re-carving, on one reading only.** The owner suggested that singularity theory's account of "phase transitions in learning as resolutions of singularities" might be useful ([CLAIM-834](../claims.d/CLAIM-834.md), U23). The record files two readings as alternatives, and the owner has not chosen between them.
  - Reading (b), [CLAIM-823](../claims.d/CLAIM-823.md) (A's): a transition is a change in which singular region dominates as the sample grows, between regions that fit differently. If adopted, it is a case of this account's re-carving with the sample as the budget: the best model at a larger sample need not refine the best at a smaller one. No entry states that tie to [CLAIM-387](../claims.d/CLAIM-387.md); it is the assistant's reading.
  - Reading (a), [CLAIM-802](../claims.d/CLAIM-802.md): training carries out a resolution. It gives no such case, and [ARG-132](../arguments.d/ARG-132.md) argues from [CLAIM-305](../claims.d/CLAIM-305.md) that it fails.
- **Orders that need not be chains.** [CLAIM-839](../claims.d/CLAIM-839.md) (A's): semantic entailment among a representation's regions, and Blackwell refinement among its checkpoints, are partial orders, "neither of which need be a chain". This agrees with the account's "What it does not say": splitting is not the normal case.
- **Resolved directions grow with data.** [CLAIM-849](../claims.d/CLAIM-849.md) (the assistant's, demonstrated): when past and future share a parameter, predictive information grows as (d/2) ln T with d resolved directions, and faster under a power-law Fisher spectrum. The number of directions a learner can tell apart is then itself a function of the observing budget.
- **A fixed capacity, redistributed.** [CLAIM-809](../claims.d/CLAIM-809.md) (A's), with [ARG-148](../arguments.d/ARG-148.md) and [CLAIM-814](../claims.d/CLAIM-814.md) (the assistant's): nearness to a dynamical transition redistributes a capacity bounded by the number of independent state variables, rather than raising it. This is a budget for distinctions held fixed while its allocation moves, which is neither of this account's two directions.

The readings of the works behind these are being filed: Bialek, Nemenman and Tishby, Dambre and colleagues, and the BBP papers. No component, status or link of this account is changed. The note is the assistant's (Claude, in this session).
