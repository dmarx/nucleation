---
number: 52
status: Proposed
formerly:
- CLAIM-tmpevciu
title: 'Interpretive framing operations generally do not commute, and this can be investigated without committing to quantum probability'
version: 4
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Warrant corrected from interpretive to empirical, carrying out the
    promotion audit's decision (record/promotion-audit/decisions/CLAIM-052.yaml,
    batch 022, ADR-047). The title's main clause is a generalization about
    how the order of framing prompts changes later judgements, and its
    defeat condition is an observation, so its support would be
    observational (ADR-043). The second clause, that order effects can be
    studied without quantum probability, holds because classical
    sequential and context-dependent-marginal models describe them
    (LIT-264). The status stays Proposed: the claim is untested, and
    CASE-021, run, is what would move it.
- version: 3
  date: '2026-10-19'
  note: >-
    Warrant restored to interpretive at the owner's direction (ADR-043
    v2: `warrant` records how a claim is supported now). The record holds
    no observation of framing-order effects on pragmatic judgements;
    CASE-021 is a design not yet run. Version 2's relabelling read
    `warrant` as the kind of evidence that would settle the claim, which
    the owner rejected. Status unchanged.
- version: 4
  date: '2026-10-29'
  note: >-
    THEORY-166 added under corroborated_by (ADR-058) by the fourteenth
    status review (ADR-057), at the status review's ruling (the owner
    delegated these rulings): question order changed the answers in the
    Pew surveys, and a classical model with order events meets the same
    regularity, independent evidence for both clauses from another
    domain, which the claim does not rest on. The claim is unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  In controlled designs the order of framing prompts makes no
  difference, beyond noise, to the distribution of later pragmatic
  judgements.
tags:
- philosophy-of-language
- probabilistic-modeling
date: '2026-10-08'
line: pragmatic-transport
works:
- what-survives-translation
supersedes:
- CLAIM-073
uses:
- TERM-024
- TERM-026
corroborated_by:
- THEORY-166
summary: >-
  A30's H1, "pragmatic noncommutativity", what the owner's U13 claim
  became. Manuscript §9: order-dependent framing "is central to
  pragmatic reconstruction".
supports:
- CLAIM-117
---
<!-- ref::uses-file: TERM-024 — stated in "noncommutativity, of events and of operations"; the body names the term only inside quotations of its source, which are not altered (ADR-038) -->
<!-- inactive-ok-file: CLAIM-117 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-052: Interpretive framing operations generally do not commute, and this can be investigated without committing to quantum probability

## The claim

A30: "**H1 — Pragmatic noncommutativity.** Interpretive framing operations
generally do not commute: T_f T_g ≠ T_g T_f. This can be investigated without
committing to quantum probability." Manuscript §9: "Order-dependent framing is
central to pragmatic reconstruction. A prompt emphasizing camaraderie followed
by one emphasizing condemnation may lead to another response distribution than
the reverse order."

## What it does not say

Nothing about nonclassicality ([CLAIM-041](CLAIM-041.md)). It is untested; [CASE-021](../cases.d/CASE-021.md) and the
manuscript's Case II (alternating frames ([TERM-026](../terms.d/TERM-026.md)<!-- ref::uses: TERM-026 -->)) would test it. [CLAIM-117](CLAIM-117.md) rests on it.

## Note of 2026-10-29: what holds it back

The record holds no observation of framing-order effects on pragmatic
judgements: [CASE-021](../cases.d/CASE-021.md) and the manuscript's Case II, which would test the
defeat condition, have not been run. The nearest held result,
question-order effects in the Pew surveys ([THEORY-166](../theory.d/THEORY-166.md)), concerns the order
of survey questions, not of framing prompts, and does not show that
framing operations in general fail to commute.
