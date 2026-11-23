---
status: Proposed
title: 'Whether information a learning system stores is knowledge depends on whether the procedures the declared system may use, within a declared budget, bring it to bear as a premise, not on whether it can be decoded: knowing is relative to the declared system and budget, and decodability by an outside probe makes information stored, not known'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  An independently motivated criterion of knowledge for learning systems
  on which information that no procedure of the declared system uses, at
  any admissible budget, counts as known because it is decodable; or on
  which the verdict on a fact accessible under one admissible cue and not
  under the default does not change when the declared procedures or
  budget change. Not defeated by showing that some decodable information
  is also used, which the claim allows.
tags:
- epistemology
- learning-theory
- representation-learning
date: '2026-11-23'
line:
- learned-structure
bears_on:
- QUESTION-493
rests_on:
- CLAIM-296
- CLAIM-697
grounds:
- CASE-tmpk3qls
- CASE-tmpp2okq
summary: >-
  The verdict of two cases of LEAD-001's set on possession against
  accessibility. A fact a probe decodes and the model never uses is
  stored, not known; a fact the model's own procedures use under one
  admissible cue is known relative to a procedure class that includes
  that cue. CLAIM-296's has-against-deploys and CLAIM-697's
  resource-conditional disposition applied to knowing, as QUESTION-493's
  candidate (A73) began to. The wording is the assistant's (Claude, in
  this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-697 TERM-079 CASE-371 — Proposed; cited as the premise, the criterion applied and a related case -->
<!-- inactive-ok-file: CASE-tmpk3qls CASE-tmpp2okq CASE-tmppqt0f — Proposed; filed by the lead run of 2026-11-23 -->

# CLAIM-tmpgfunb: Whether information a learning system stores is knowledge depends on whether the procedures the declared system may use, within a declared budget, bring it to bear as a premise, not on whether it can be decoded: knowing is relative to the declared system and budget, and decodability by an outside probe makes information stored, not known

## The claim

QUESTION-493's candidate (A73) separates possession, accessibility and
manifestation, and says both that "a capacity costly to exercise is still
possessed" and that "a fact buried in a gigantic database and inaccessible
to every permitted retrieval procedure should not automatically count".
Two cases fix where the line falls.

- CASE-tmpk3qls: a linear probe reads the true country of a city from a
  model's activations; the model answers and reasons with a false one;
  ablating the probe's direction changes nothing. The information is
  stored and cheaply decodable. No procedure of the model uses it. Not
  known.
- CASE-tmpp2okq: the model answers a fact correctly, and reasons from it,
  under a French cue and not under its default English query; a
  one-sentence instruction restores it in English. Known, relative to a
  procedure class that includes the cue or the instruction; not
  accessible under the default alone.

What separates them is not cost of retrieval (the probe is cheap) but
whose procedure brings the information to bear as a premise in
TERM-079's sense. So:

1. Information is a candidate for knowledge of a declared system only if
   some procedure that system may use, within a declared budget, uses it
   as a premise.
2. "The model knows p" is incomplete until the procedures and the budget
   are named, as CLAIM-697 says of a disposition to succeed and
   CLAIM-296 of what a system can deploy given the cue.
3. Adding an outside probe to the declared system does not by that make
   the information known: the composite then answers with p while its
   further inferences run on not-p. A composite knows only where its
   procedures use what its part produces, which is the condition
   CASE-tmppqt0f's generator and verifier meet.

The record's executed study CASE-371, where facts fine-tuned away stay
recoverable by an untrained cue, a probe or the runner-up answer, is the
evidence that such states occur; which of its recoveries count as the
system's procedures is a declaration this claim says must be made.

## What it does not say

- Not which procedures should be declared. That is a choice about what
  the system is taken to be, and evaluations differ on it.
- Not that knowledge needs a cheap retrieval: a costly procedure that is
  admissible counts.
