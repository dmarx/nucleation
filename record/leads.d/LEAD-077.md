---
number: 77
status: Open
formerly:
- LEAD-tmpdesma
title: 'Run audited governance against a contextual router, given the same audit delay and cost, after expertise reverses and in the arms where a router could lose'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    A dated note added: LEAD-077's run of CASE-158's design. The entry
    is otherwise unchanged.
stage: specified
priority: high
method:
- empirical
tags:
- self-governance
- social-ontology
date: '2026-11-19'
line:
- distributed-agency
advances:
- CLAIM-467
- QUESTION-271
- QUESTION-264
- QUESTION-089
- CLAIM-277
- CLAIM-342
- CLAIM-286
operationalized_in:
- CASE-158
- CASE-144
summary: >-
  The in-force test of whether governance does anything a router does not;
  [ARG-036](../arguments.d/ARG-036.md) names it as the remedy for the line naming no outcome its model
  rules out. Named in [CLAIM-467](../claims.d/CLAIM-467.md), [CASE-158](../cases.d/CASE-158.md) and [ARG-036](../arguments.d/ARG-036.md). Filed by the
  backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: ARG-036 — Proposed; cited in the backlog audit of 2026-11-19 -->

# LEAD-077: Run audited governance against a contextual router, given the same audit delay and cost, after expertise reverses and in the arms where a router could lose

## What it would do

Run [CASE-158](../cases.d/CASE-158.md) with the router matched on audit delay and cost, adding one
arm per failure [QUESTION-271](../questions.d/QUESTION-271.md) lists: cycles, no common scale, capture,
bandit feedback, and continued training.

Where the record names it:

- [CLAIM-467](../claims.d/CLAIM-467.md): "A run of [CASE-158](../cases.d/CASE-158.md)'s design, with the router given the same
  audit delay and cost, in which audited governance has lower held-out error
  than the router under full-information, independent audits"
- [CASE-158](../cases.d/CASE-158.md): "What would make it informative is one arm per failure of
  [QUESTION-271](../questions.d/QUESTION-271.md)"
- [ARG-036](../arguments.d/ARG-036.md): "Does it tell the hypothesis apart from its rivals? Not yet.
  This is the question that fails."

## What would count

Audited governance with lower held-out error than the matched router in
some arm defeats [CLAIM-467](../claims.d/CLAIM-467.md) as stated and names a regime where governance
adds something. The router matching or beating it in every arm supports
[CLAIM-467](../claims.d/CLAIM-467.md) and answers [ARG-036](../arguments.d/ARG-036.md)'s failed question against the line.

## Note of 2026-11-22: run, and what remains

<!-- inactive-ok-file: CASE-tmpkghqb CLAIM-tmpdmn0v — new; the run filed for LEAD-077 and its claim, cited in the note of 2026-11-22 -->

Run on 2026-11-22 by a delegated worker ([CASE-tmpkghqb](../cases.d/CASE-tmpkghqb.md), [CLAIM-tmpdmn0v](../claims.d/CLAIM-tmpdmn0v.md);
scratch/studies/lead-077/). [CASE-158](../cases.d/CASE-158.md)'s design was built in numpy with
the router matched on audit records, delay and cost, and run with one arm
per failure of [QUESTION-271](../questions.d/QUESTION-271.md) and one with continued training: 8 arms,
3 gate temperatures, 12 paired seeds, 288 runs, about 20 minutes of CPU.

Against "What would count": governance had lower error than the
contextual router under full information at shared low temperatures, and
not at the temperature both do best at; a router seeing only the region
id beat it everywhere. In the failure arms the best router matched or beat
the best governance in each. Read by this lead's own wording, "lower
held-out error than the matched router in some arm", two comparisons
qualify: full information at shared low temperatures, and bandit feedback
with a 10% audit floor imposed on both (12 of 12), where the router
without the floor did as well as governance with it. Whether that defeats or supports [CLAIM-467](../claims.d/CLAIM-467.md)
is set out as two readings in [CLAIM-tmpdmn0v](../claims.d/CLAIM-tmpdmn0v.md), for the owner.

What remains: α-Rank or Nash averaging as governance's procedure under
cycles and duplication; unknown or zero audit propensities; an
entrenchment arm with the training rate and capacity swept; [CASE-158](../cases.d/CASE-158.md)'s
grant-reset counterfactual. The status and stage are the owner's.
