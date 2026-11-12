---
status: Proposed
title: 'The record computes no withdrawals: retiring an entry reports what rests on it and leaves whether each dependant falls to a judgment, and no rule reading only the support graph and the entries'' statuses could make that judgment correctly'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  The configured record does retract a dependant automatically when what it
  rests on is retired, so the first half is false of it; or a rule that
  reads only the support graph and the entries' statuses decides correctly,
  in both of CASE-089's worlds, whether the conclusion should be withdrawn,
  which would contradict CLAIM-293. Also defeated if it only restates
  CLAIM-293 and CLAIM-479 with nothing added: the addition is that the
  reporting design is what CLAIM-293 requires of any record whose relations
  carry no weights, not a shortfall against a truth-maintenance system.
  Not defeated by a reasoner that reads more than the graph, likelihoods or
  dependence models, deciding correctly; the claim is about the graph.
tags:
- epistemology
- logic
- design-rationale
date: '2026-11-12'
line:
- records-of-inquiry
- record-as-apparatus
rests_on:
- CLAIM-293
bears_on:
- QUESTION-tmps5iou
- QUESTION-108
summary: >-
  A's, stated four times in the exchange "luria experiment design"
  (2026-11-10): A20 §3, "Unlike a full truth-maintenance reasoner, Luria
  does not automatically calculate which beliefs should be withdrawn. It
  exposes structure and maintenance obligations to human judgment"; A27;
  A45 §9, citing CLAIM-293; and A50 §7, against Doyle's and de Kleer's
  truth maintenance and AGM revision (LIT-2291, LIT-2320, LIT-1050). A
  presents it as a boundary on what luria can claim. The derivation here
  makes it also a reason for the boundary: by CLAIM-293, a rule reading
  only the unweighted graph would retract wrongly in one of two worlds the
  graph cannot tell apart. The wording is A's; adopting it is the owner's
  call.
---
<!-- inactive-ok-file: LIT-2291 LIT-2320 — Deferred; registered from the same exchange, not read -->

# CLAIM-tmp8qsef: The record computes no withdrawals: retiring an entry reports what rests on it and leaves whether each dependant falls to a judgment, and no rule reading only the support graph and the entries' statuses could make that judgment correctly

## The claim

From the exchange "luria experiment design"
(https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda). A27:
"Luria is not a logical truth-maintenance engine. It can expose relevant
dependencies and status changes, but it cannot automatically decide that
every downstream conclusion is false." A45 §9: "Luria's typed relations and
validation mechanisms do not by themselves determine how rational belief
should change."

**What the record does.** The relation that carries dependence says what
retiring its target leaves and does nothing about it: `rests_on` is
"another of the record's own claims this one could not stand without …
Retired, it leaves this claim needing another route" (docs/record.md,
from luria.yaml). `corroborates` says the other claim "loses support, not
its footing" (ADR-044). The `argument` chain walks the dependants. No status changes
because another did. A truth
maintenance system (LIT-2291, LIT-2320) or an AGM revision operator
(LIT-1050) computes the new belief set instead.

**Why no graph-only rule could replace the judgment.** CLAIM-293, from
CASE-089: two records with the same edges, E₁ → H ← E₂, where discounting
E₁ leaves H at odds of 20:1 in one and 1.1:1 in the other. Take any rule
that decides, from the support graph and the entries' statuses alone,
whether H is withdrawn when E₁ is retired. The two records give it the
same input, so it gives the same verdict in both, and the verdict is wrong
in one of them under any standard that keeps H at 20:1 and withdraws it at
1.1:1. So a record
whose relations carry no weights cannot compute withdrawals correctly
from them, and reporting the dependants for a judgment that reads the
evidence is what such a record can soundly do.

## What it does not say

- Not that the record should weight its edges. CLAIM-293 leaves that as a
  design question, and the owner objected to turning to it.
- Not that the judgment is made well. CLAIM-479: a relation's rigidity is
  "not evidence that the dependency it records is sound". The record only
  says where a judgment is owed.
- Not that a reasoner over richer records could not compute withdrawals.
  A50's proposed test, a plain record, the record, a truth-maintenance
  system and the record with an external reasoner on formally specified
  tasks, would separate "what the record preserves from what the reasoning
  algorithm computes".
