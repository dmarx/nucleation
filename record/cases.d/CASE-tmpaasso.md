---
status: Proposed
title: 'Two patient arrangements: under a right of refusal, Arrangement A treats on consent and refrains on refusal, Arrangement B treats either way; on every occasion the patient consents their histories are identical, and only A respects the right'
version: 1
standing: stipulated
kind: construction
tags:
- ethics
- game-theory
date: '2026-11-17'
line:
- organizational-normativity
- will-organization
bears_on:
- QUESTION-454
summary: >-
  A's construction, from the exchange "Assess Depp Heard Abuse"
  (2026-11-17): A97 III's patient arrangements, stated "assuming a
  competent patient, an applicable right of refusal, and no justified
  exception", restated as Policy A and Policy B with π_A(c) = c and
  π_B(c) = 1 in A102 §4, and generalized as the conditional rights-respect
  test in A106 §15. Checked on filing. It grounds CLAIM-tmpol7nz's second
  separation, between realized history and policy. Proposed because the
  construction is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpol7nz — filed from the same exchange, Proposed -->

# CASE-tmpaasso: Two patient arrangements: under a right of refusal, Arrangement A treats on consent and refrains on refusal, Arrangement B treats either way; on every occasion the patient consents their histories are identical, and only A respects the right

## The case

A97 III of the exchange "Assess Depp Heard Abuse"
(https://chatgpt.com/share/6afcb46d-83a8-83e9-9c85-4a0c3604405b): "Suppose
the patient voluntarily accepts treatment. The treatment occurs. That
history may be entirely legitimate. Now suppose a different institution
always administers the treatment regardless of consent. The patient
happens to want treatment on the particular occasion observed. The
outcome is identical. Yet the second institution may not respect the
patient's right to refuse."

Stipulated: a competent patient, a right of refusal that applies, no
justified exception. With c = 1 consent, c = 0 refusal, a = 1 treat,
a = 0 refrain (A102 §4):

| Protected choice | Policy A | Policy B |
|---|---|---|
| Consent, c = 1 | Intervene | Intervene |
| Refusal, c = 0 | Refrain | Intervene |

π_A(c) = c and π_B(c) = 1. The right's required responses are
Resp_N(r, 1) = {intervene, refrain} and Resp_N(r, 0) = {refrain}.

## Checked

- On c = 1, both produce the history (c, a) = (1, 1). Any evaluation that
  is a function of the realized history gives the same verdict to both.
- A meets Resp_N at c = 1 (intervene is permitted) and at c = 0 (refrain).
  B meets it at c = 1 and fails at c = 0.
- So respect for the right differs while the history on the consenting
  occasion does not. If the patient always consents, no observed history
  ever separates them.

## What it can show

It is the construction CLAIM-tmpol7nz rests on: a right that protects a
choice is a property of a policy over the protected choices. A97 III's
other examples have the same form: an easement unused in a period, an
appeal right never invoked, "A right of refusal can matter when a person
freely agrees" (A102 §4).

What it cannot show: which rights protect choices rather than outcomes,
or that any actual institution behaves like B. An observed refusal
overridden would show B's policy; consent observed, however often,
cannot show A's.

It bears on QUESTION-454, on authority to decide about another's body: the
question already presupposes a right of this kind, and the case says what
respecting it consists in.
