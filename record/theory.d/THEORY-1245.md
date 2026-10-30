---
number: 1245
status: Proposed
formerly:
- THEORY-tmpvevpl
title: 'Evaluating expected free energy recursively over the beliefs an agent would hold after each plausible outcome makes active inference a pruned tree search over belief states, formally analogous to Bellman recursion, which lets the agent plan through short-term costs that one-step agents cannot; that the pruning keeps deep search tractable beyond toy problems is argued, not shown'
version: 1
tags:
- probabilistic-modeling
- information-theory
date: '2026-10-30'
source:
- LIT-577
extends:
- THEORY-426
promote_when: >-
  A comparison on shared tasks larger than toy mazes, with variance over
  runs, between sophisticated active inference and a Bayes-adaptive
  planner (for example Monte Carlo tree search over belief states), that
  reports both what each solves and the number of belief states each
  evaluates as the horizon and the number of plausible outcomes grow.
  Promote if the pruned recursion solves problems one-step expected free
  energy cannot, at a cost that stays far below the full tree where many
  outcomes remain plausible. More single deterministic runs on toy
  problems cannot settle it, and neither can a further derivation of
  which objectives are special cases.
summary: >-
  The general form of Friston, Da Costa, Hafner, Hesp and Parr (2020),
  [LIT-577](../literature.d/LIT-577.md), under [THEORY-426](THEORY-426.md)'s old title. It was kept here when the
  twenty-fourth status review narrowed [THEORY-426](THEORY-426.md) to the paper's runs and
  promoted it ([ADR-065](../decisions.d/ADR-065.md) §3; [ADR-047](../decisions.d/ADR-047.md), kind 1). The paper shows the planning
  claim only in single deterministic runs on a T-maze and an 8 × 8 maze
  ([NOTE-454](../notes.d/NOTE-454.md), C2). It argues tractability from pruning and sparsity and
  counts evaluations for one maze (C3). It tries no problem where many
  outcomes stay plausible, and runs no Bayes-adaptive planner beside it.
---

# THEORY-1245: Evaluating expected free energy recursively over the beliefs an agent would hold after each plausible outcome makes active inference a pruned tree search over belief states, formally analogous to Bellman recursion, which lets the agent plan through short-term costs that one-step agents cannot; that the pruning keeps deep search tractable beyond toy problems is argued, not shown

## Source

Friston et al. (2020), "Sophisticated Inference", [LIT-577](../literature.d/LIT-577.md), read in full as
prose in [NOTE-454](../notes.d/NOTE-454.md). What the paper's runs showed is [THEORY-426](THEORY-426.md), which this
entry extends.

## Why it is Proposed

The title states the planning claim generally, where the paper shows it on
toy problems, "rather trivial problems" by the authors' own account. The
cost figure, "usually several hundred" of about 10¹⁰ or 10¹⁵ paths, is
for one maze. A 1/16 pruning threshold cuts little where many outcomes stay
plausible, and no such problem is tried ([NOTE-454](../notes.d/NOTE-454.md), Open questions). The
paper says the scheme recovers Bayes-adaptive RL at zero temperature, but
no Bayes-adaptive or Monte Carlo planner is run on the same tasks.
