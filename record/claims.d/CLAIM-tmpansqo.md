---
status: Proposed
title: 'Observing a context, conditioning on one and intervening on the interpreter are different operations on an empirical model, so a framing intervention should index the model, e_C^do(a) = P(Y_C | do(a)), not enter its cover as one more context'
version: 1
role: thesis
defeated_if: >-
  Every framing intervention the manuscript's experiments use can be
  written as a measurement context in the cover, or as conditioning on
  an observed context variable, without changing any compatibility,
  contextuality or signalling verdict on the data; so that the do-index
  separates nothing the cover does not already separate.
tags:
- causality
- contextuality
date: '2026-10-09'
line: pragmatic-transport
uses:
- TERM-018
- TERM-030
complements:
- CLAIM-125
summary: >-
  Proposed in a review of the record that the owner relayed on
  2026-10-09, as the third of three structural changes to the
  manuscript. The record had made the distinction in words ([TERM-018](../terms.d/TERM-018.md)
  against [TERM-030](../terms.d/TERM-030.md)); the review puts it in the formalism. The link to
  signalling below is the record's own extrapolation.
---
<!-- inactive-ok-file: CLAIM-125 — Proposed; cited as the open problem this claim bears on, not as settled -->

# CLAIM-tmpansqo: Observing a context, conditioning on one and intervening on the interpreter are different operations on an empirical model, so a framing intervention should index the model, e_C^do(a) = P(Y_C | do(a)), not enter its cover as one more context

## The claim

The review: "make causal interventions and observational contexts separate
indexed structures from the outset: e_C^{do(a)} = P(Y_C | do(a)). That would
connect our recent Pearl-inspired refinement to the sheaf structure without
treating observation, conditioning, and intervention as the same operation."

The record already draws the distinction in words. A frame is a property of
the communicative situation ([TERM-030](../terms.d/TERM-030.md)); a framing intervention is "an action
that changes the conditions under which an utterance is interpreted"
([TERM-018](../terms.d/TERM-018.md)). Telling a reader that the speaker is a friend is not the same as
the speaker's being one. What the record lacks is a place for the
distinction in the formalism. In the sheaf-theoretic setting a context is a
set of jointly measured observables, and the empirical model assigns each a
distribution. Nothing there says whether an elicitation only reads the
interpreter's state or changes it. Under this claim each intervention a
gives its own empirical model e^do(a), with its own cover and compatibility.
Transport is then compared across a family of models indexed by
intervention, and no intervention is a context inside one of them.

## Why it matters for the open problems

This part is the record's extrapolation, not the review's. [CLAIM-125](CLAIM-125.md)'s second
open problem is that language data signal. In the corpus data Wang et al.'s
journal follow-up measured, 69 of 90 noun–verb systems signal. The
manuscript's experiments elicit judgements instead, and A35 §6 had already
warned that "forcing a participant to make an explicit judgment is itself an
intervention." If an elicitation is an intervention, then reading one
observable can change the interpreter's state. That change can show up as a
dependence of another observable's marginal on context, which is signalling.
The do-index gives this hypothesis a form that can be tested: models elicited
under different interventions are compared separately, not pooled into one
cover, and the elicited data can be checked for signalling beyond the
corpus baseline.

## What it does not say

It does not say the signalling in corpus data comes from elicitation. Corpus
estimates involve no elicitation at all. It does not say interventions
violate the no-signalling condition. It does not say Pearl's calculus applies
as it stands: a do-operator needs a causal model of the interpreter, and the
record has none. Nor does it settle where the "Pearl-inspired refinement" the
review mentions came from. No entry in the record carries one, and the
claim stands on [TERM-018](../terms.d/TERM-018.md) and [TERM-030](../terms.d/TERM-030.md), not on that refinement.
