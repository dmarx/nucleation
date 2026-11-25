---
number: 1109
status: Proposed
formerly:
- CLAIM-tmphm1g8
title: 'Knowledge can belong to generator-verifier pair'
statement: >-
  Where a learning system samples and checks, knowledge can belong to the
  declared composite of generator and verifier under a sampling budget and
  to neither part: the generator's rare success is reach, the verifier's
  check is no capacity to answer, and the composite's delivered success is
  reliable and grounded by the check
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  An independently motivated argument that knowledge in a learning system
  needs a single bearer that both produces an answer and holds it, which
  a generator filtered by an exact verifier lacks, and which the argument
  does not equally deny to a single model that drafts and checks its own
  answers internally; or a case of such a composite that meets truth,
  reliability under its budget and grounding by an exact check and
  plainly does not know.
tags:
- epistemology
- learning-theory
- agency
date: '2026-11-23'
line:
- learned-structure
- distributed-agency
bears_on:
- QUESTION-493
rests_on:
- CLAIM-697
grounds:
- CASE-414
- CASE-400
- THEORY-1894
summary: >-
  The verdict of [LEAD-001](../leads.d/LEAD-001.md)'s generator-and-verifier case on where knowing
  sits, the second half of [QUESTION-493](../questions.d/QUESTION-493.md). A generator right one time in a
  hundred, filtered by an exact checker that cannot propose answers, is
  right 99% of the time at 460 samples. The composite knows under that
  budget; neither part does. [QUESTION-493](../questions.d/QUESTION-493.md)'s candidate (A73) said
  knowledge "may belong to the composite"; this says when. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-697 TERM-079 — Proposed; the premise this claim applies and a criterion it cites -->
<!-- inactive-ok-file: CASE-414 CASE-400 CLAIM-1100 CLAIM-1028 — Proposed; filed by the lead run of 2026-11-23 -->

# CLAIM-1109: Knowledge can belong to generator-verifier pair

## The claim

[CASE-400](../cases.d/CASE-400.md)'s model is right one time in two hundred: generative reach,
not knowledge, as [QUESTION-493](../questions.d/QUESTION-493.md)'s candidate (A73) says and [CLAIM-697](CLAIM-697.md)'s
coverage against delivery formalizes. [CASE-414](../cases.d/CASE-414.md) pairs such a
generator with an exact checker that cannot propose answers. Under a
budget N the composite succeeds with probability 1 − (1 − p)^N, which at
p = 0.01 passes 99% at N = 459, and its answers are right whenever it
gives one.

On A73's three criteria:

- **Truth**: yes, whenever it answers.
- **Reliability over the declared family**: yes under the budget, no
  below a few dozen samples. So the knowledge is the composite's *under
  a declared budget*, as [CLAIM-697](CLAIM-697.md) says of any disposition to succeed.
- **Grounding**: the check depends on what makes the answer true (the
  product of the factors) and on nothing else, so the composite's answer
  is grounded by the check. Neither part meets all three: the generator
  fails reliability, and the verifier gives no answer.

So knowledge can sit in a declared composite and in neither part. The
condition is that the composite's procedures use what its parts produce:
the accepted answer is the composite's answer. That is the condition
[CLAIM-1100](CLAIM-1100.md) sets for stored information, and it is what the
model-plus-probe composite of that claim fails. [THEORY-1894](../theory.d/THEORY-1894.md) shows the
verifier is the hinge: with automatic verification coverage turns into
solved problems as samples grow, and without one selection plateaus far
below coverage.

## What it does not say

- Not that every pairing of a model and a tool knows: a checker that
  depends on something other than the truthmaker (a reward model's
  preference, say) grounds nothing, and the composite inherits its
  failures.
- Not that the composite believes. It draws no further inferences from
  the accepted answer here, so [TERM-079](../terms.d/TERM-079.md)'s probes have nothing to test;
  whether knowledge without belief is coherent is the question the record
  left open when it set belief and knowledge apart.
- Not which route counts as the composite's own: on [CLAIM-1028](CLAIM-1028.md)'s
  reading of grounding that is a further question.
