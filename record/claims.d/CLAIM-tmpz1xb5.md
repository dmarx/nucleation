---
status: Proposed
title: 'To register that an expected event failed to occur within a specified interval, an apparatus must physically distinguish the tested interval from its alternatives and retain enough state to classify the outcome; such an apparatus need not be sentient'
version: 2
history:
- version: 2
  date: '2026-11-12'
  note: >-
    Narrowed at the review of #483 the owner relayed on 2026-11-12. The
    review found the unrestricted version too strong. A deadline "may be
    sufficient but not necessary" for a meaningful absence: a fail-safe
    relay that must stay energized to hold a valve closed opens it when
    the current stops, an absence with an immediate consequence and no
    separately initiated test, stored expectation or timeout
    (CASE-tmp4gw3m). The claim is now about registering a bounded
    non-response, in the review's sentence. The fail-safe relay marks the
    claim's scope; it is not a counterexample to the narrowed claim. The
    review also called this claim's point "a central result of the
    inquiry". Old title: An absence of response is a distinction only
    for an apparatus that opens an interval, keeps the expected response
    through it and registers its non-occurrence at a deadline; such an
    apparatus need not be sentient, but without one nothing is there to
    carry the meaning.
role: thesis
warrant: interpretive
defeated_if: >-
  A system that classifies a trial as "expected event did not occur
  within the interval" correctly and reliably, while no part of it, or of
  anything coupled to it, physically marks which interval was the tested
  one or keeps a state that tells the tested interval's outcome from its
  alternatives at classification time. Also defeated, as a claim with
  content of its own, if it only restates TERM-089's differentiation and
  retention applied to non-events; then it belongs in a note on the term.
  Not defeated by a consequential absence that is not registered as the
  failure of an expected event, such as the fail-safe relay
  (CASE-tmp4gw3m): that is outside the claim's scope. Not defeated by an
  apparatus that is a person: the claim says sentience is not required,
  not that it is excluded.
tags:
- epistemology
- philosophy-of-language
date: '2026-11-12'
line:
- record-as-apparatus
uses:
- TERM-089
grounds:
- CASE-tmpaky45
bears_on:
- QUESTION-285
summary: >-
  From A10 §6 of the exchange "Meaning Transmission Explained"
  (2026-11-07), with A5 §3's automated debugger, on the owner's debugging
  case ([CASE-tmpaky45](../cases.d/CASE-tmpaky45.md)) and claim ([CLAIM-tmpkr3ti](CLAIM-tmpkr3ti.md)). A10: "**Silence is not
  literally an object transmitted from the broken detector to the
  debugger.**" Narrowed at the review of [#483](https://github.com/dmarx/nucleation/issues/483) the owner relayed on
  2026-11-12 to diagnosis by bounded non-response, in the review's
  sentence: "To register that an expected event failed to occur within a
  specified interval, an apparatus must physically distinguish the tested
  interval from its alternatives and retain enough state to classify the
  outcome." The fail-safe relay ([CASE-tmp4gw3m](../cases.d/CASE-tmp4gw3m.md)) shows that an absence can
  matter without any of this, and marks the claim's scope. [CLAIM-312](CLAIM-312.md)'s
  deadline-bound search is the record's nearest held case. The wording is
  A's and the review's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpaky45 CLAIM-tmpkr3ti CASE-tmp4gw3m — filed from the same exchange, Proposed -->

# CLAIM-tmpz1xb5: To register that an expected event failed to occur within a specified interval, an apparatus must physically distinguish the tested interval from its alternatives and retain enough state to classify the outcome; such an apparatus need not be sentient

## The claim

The sentence is the review's (the review of [#483](https://github.com/dmarx/nucleation/issues/483) the owner relayed on
2026-11-12):

> To register that an expected event failed to occur within a specified
> interval, an apparatus must physically distinguish the tested interval
> from its alternatives and retain enough state to classify the outcome.

It narrows A10 §6 of the exchange "Meaning Transmission Explained"
(https://chatgpt.com/share/6af517f7-cb48-83ea-8395-df7d52333dc7):

> **Silence is not literally an object transmitted from the broken
> detector to the debugger.** For an automated system to register the
> absence of a response, something physical must establish an
> observation interval, maintain the expectation, and record the failure
> to respond before a deadline.

A10's start, stored expectation and timeout are one way to meet the
review's condition, not the condition itself.

## The argument

[TERM-089](../terms.d/TERM-089.md)'s apparatus "makes some physical differences produce distinct
outcomes" (differentiation) and may keep them (retention). To classify a
trial as "the expected event did not occur in [t₀, τ]", the apparatus's
state at classification has to differ according to that outcome. It has
to differ from the case where the event occurred in the interval, and
from the case where no trial was run. A non-occurrence drives nothing at
any moment. So the difference has to be carried by a state that marks
the tested interval and persists until the outcome is classified. That
is the review's "physically distinguish the tested interval from its
alternatives and retain enough state". Without it, the detector's silence
under test and its silence in clean air leave the same trace. There is
then nothing for the owner's absence to be evidence of
([CLAIM-tmpkr3ti](CLAIM-tmpkr3ti.md)).

Nothing in this needs a sentient party. A5 §3's automated tester holds
the stored profile, a timer and a switch to the backup detector: "No
sentient entity participates in that particular diagnostic event."

## Scope

- **Registering, not mattering.** An absence can have consequences
  without being registered as the failure of an expected event. In the
  fail-safe relay ([CASE-tmp4gw3m](../cases.d/CASE-tmp4gw3m.md)) a valve opens because current stops,
  with no test, stored expectation or timeout. The review: "physical
  organization (relay state, spring, coupling) is still required, but
  that is a more general condition." The relay marks the edge of this
  claim's scope, and the claim does not cover it.
- **[CLAIM-312](CLAIM-312.md) is the held case nearest it.** A search that fails by the
  deadline "establishes unavailability outright"; absence needs a
  further certificate. A bounded test establishes a failure to respond
  within the interval, not that a response could never come.
- **[QUESTION-285](../questions.d/QUESTION-285.md)'s rungs.** The marked interval and the retained state are
  a record that something uses, so diagnosis by bounded non-response sits
  at the rung of use, with no conscious investigator.

## What it does not say

- That every consequential absence needs a test or a deadline. The
  version before the review said this, and the fail-safe relay shows it
  too strong.
- That the interval and the expectation must be designed. In A's tester
  they are. Whether a system could set its own is [QUESTION-128](../questions.d/QUESTION-128.md)'s
  question.

## Admission

Filed as a claim of A's with content of its own ([ADR-072](../decisions.d/ADR-072.md)), narrowed by the
review. The derivation above is short. The defeater names the objection
that it only restates [TERM-089](../terms.d/TERM-089.md).
