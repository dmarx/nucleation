---
number: 395
status: Open
formerly:
- QUESTION-tmpw46vw
title: 'Beyond what records kept of each capacity bound, what observations, interventions, or models can distinguish a warranted reserve of specialized capability from wasteful redundancy when ordinary operation seldom exercises it, and how is that evidence weighed against the capability''s cost?'
version: 2
history:
- version: 2
  date: '2026-11-20'
  note: >-
    Split under ADR-049 at the status review's ruling (the owner delegated
    these rulings), when CLAIM-632 went Active. The answered part, whether
    records kept of each capacity identify readiness or only bound it and
    which verdicts they settle, is QUESTION-tmp1j2mq, answered by
    CLAIM-632. This question narrows to the remainder: the other evidence
    "What would answer it" lists, and the weighing against cost. The old
    title was "What observations, interventions, or models can distinguish
    a warranted reserve of specialized capability from wasteful redundancy
    when ordinary operation seldom exercises it?"
tags:
- operations-research
- causality
- society-and-governance
date: '2026-11-04'
line:
- readiness
summary: >-
  A's proposal, from the exchange on emergency readiness (2026-11-04; its
  share link could not be fetched, and its text was pasted by the owner),
  section 9 of A's "Proposed additions to Nucleation PR [#401](https://github.com/dmarx/nucleation/issues/401)". Since
  routine output cannot tell a reserve from redundancy ([CASE-210](../cases.d/CASE-210.md),
  [ARG-053](../arguments.d/ARG-053.md)), what evaluation regime can? An answer specifies the
  observations, interventions or models under which the two explanations
  come apart. The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-210 ARG-053 — Proposed, Rejected or new; A's proposals of 2026-11-04 and the readings they cite, as open -->

# QUESTION-395: Beyond what records kept of each capacity bound, what observations, interventions, or models can distinguish a warranted reserve of specialized capability from wasteful redundancy when ordinary operation seldom exercises it, and how is that evidence weighed against the capability's cost?

## Why it is a question

The inference from low exercise to waste fails ([ARG-053](../arguments.d/ARG-053.md)): a reserve
and a redundancy both cost money and both go unused. [CLAIM-561](../claims.d/CLAIM-561.md) adds
that cancellation counts do not separate them either. So the question is
an identification problem. In A's form: can two departments have the same
completed specialist interventions, the same dispatch and cancellation
counts, similar ordinary performance, and different probabilities of
timely qualified response to a specified rare incident? [CASE-210](../cases.d/CASE-210.md) says
yes, by construction. If so, which observations distinguish them?

Two held claims bound it. [CLAIM-414](../claims.d/CLAIM-414.md) shows, in finite constructions, that
matched ordinary trajectories can conceal differences that a specified
intervention exposes. [CLAIM-517](../claims.d/CLAIM-517.md) shows that fidelity measured in ordinary
operation certifies nothing about behaviour at the boundary contexts that
matter. Both say passive observation of ordinary operation is not enough;
neither says what is.

## What would answer it

An evaluation regime in which evidence can distinguish the explanations,
drawn from A's list: incident histories, response-time distributions,
availability records, training assessments, coverage simulations and
counterfactual stress tests. A full answer says which of these, alone or
together, identify the readiness ([TERM-115](../terms.d/TERM-115.md)) for a specified rare
contingency, and which only bound it, and weighs that against the
capability's cost and its alternatives.

## What would not answer it

Counts of use, dispatch or cancellation, alone. They are the same for the
two departments of [CASE-210](../cases.d/CASE-210.md).

## Note of 2026-11-20: the part split off

Records kept of each capacity are settled by [QUESTION-tmp1j2mq](QUESTION-tmp1j2mq.md): they fix the marginals, which bound readiness and identify it only when the capacities' dependence is known ([CLAIM-632](../claims.d/CLAIM-632.md)). What stays open here is which of the other kinds of evidence listed above, alone or together, identify readiness for a specified rare contingency, and how that is weighed against the capability's cost and its alternatives.
