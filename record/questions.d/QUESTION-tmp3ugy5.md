---
status: Answered
title: 'Are the conditions an effective description is asked to meet (predictive sufficiency, dynamical independence, memory closure, approximation fidelity, tractability) of one logical kind, or are some of them parameters of the regime under which the others are assessed rather than conditions in their own right?'
version: 1
tags:
- complex-systems
- philosophy-of-science
date: '2026-10-29'
line: formal-apparatus
refines:
- QUESTION-252
answered_by:
- CLAIM-401
summary: >-
  The last clause of QUESTION-252, split off by the thirteenth status
  review under ADR-049 because CLAIM-401 (Active) settles it: they are not
  of one kind. Predictive sufficiency and approximation fidelity are
  adequacy relative to a declared target, metric and horizon; tractability
  restricts the operations under which adequacy is assessed; dynamical
  independence and memory closure are relations of the representation to
  the system, memory relative to a chosen projection. Which conditions can
  fail while the others hold, and which configurations are impossible in
  which model classes, stays QUESTION-252's.
---

# QUESTION-tmp3ugy5: Are the conditions an effective description is asked to meet (predictive sufficiency, dynamical independence, memory closure, approximation fidelity, tractability) of one logical kind, or are some of them parameters of the regime under which the others are assessed rather than conditions in their own right?

## Why it was a question

QUESTION-252 asked it together with the leave-one-out design: which of the
five conditions can fail while all the others hold, and which such
configurations are impossible in which model classes. Working through that
design, A4 and A5 of the exchange of 2026-10-20 found that the five were
not coordinates of one kind. This part has an answer the record holds; the
leave-one-out part does not, so they are filed apart (ADR-049).

## The answer

Not of one kind (CLAIM-401):

- **Adequacy for a target.** Predictive sufficiency and approximation
  fidelity hold only relative to a declared target, metric and horizon
  (CLAIM-152, CLAIM-348).
- **A restriction on operations.** Tractability restricts the operations
  under which adequacy is assessed, and the same representation passes or
  fails with the budget (CLAIM-304).
- **Relations of the representation to the system.** Dynamical
  independence and memory closure, the latter relative to a chosen
  projection (CLAIM-397, THEORY-752).

So a matrix over the five as independent binary axes conflates kinds. The
answer does not say the five reduce to three, and it leaves the
leave-one-out cells, once the regime (TERM-065) is fixed, to QUESTION-252.
