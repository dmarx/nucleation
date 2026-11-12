---
status: Proposed
title: 'An absence of response under an inserted intervention with an expected response profile is diagnostic evidence about the mechanism under test, carried with nothing emitted: under a probabilistic response model it shifts support toward fault by its likelihood ratio, and in the limiting case of a deterministic, independently validated response guarantee it entails that the guarantee was violated'
version: 2
history:
- version: 2
  date: '2026-11-12'
  note: >-
    Revised at the review of #483 the owner relayed on 2026-11-12. The
    review objected that version 1 read "means" in Grice's factive sense
    while its own worked model has a 2% error rate, so the likelihood
    ratio of 49 establishes strong evidence, not that the mechanism is
    broken, and restricting the claim to cases where it really is
    broken makes the account retrospective. The claim now separates two
    readings, each with its own criterion of correctness. The defeasible
    reading is the general one and the factive reading its limiting
    case. The defeater is rewritten to match. The owner's U3 wording
    stays quoted as the owner's; the narrowing is the review's. Old
    title: A failure to respond under an inserted intervention with an
    expected response profile means that the mechanism under test is
    broken: the meaning is carried by an absence, with nothing emitted.
role: thesis
warrant: interpretive
defeated_if: >-
  For the defeasible reading: a correctly delivered intervention with a
  stated expected response model under which the absence is no likelier
  with the mechanism out of profile than in it (likelihood ratio 1), and
  yet the absence is still taken as evidence of a fault; or an argument
  that shifting support among fault hypotheses is not meaning in any
  sense the record uses (TERM-089's operational sense, or Grice's natural
  meaning in its evidential use) but only an observer's inference. For
  the factive reading: a response guarantee that is deterministic and
  independently validated, the intervention delivered as the guarantee
  specifies, no response, and the guarantee not violated. Not defeated
  by a silence that fails to say which component failed: both readings
  are about the mechanism under test as a whole, its test path included
  (A5 §1). Not defeated by an absence the model gives a low but nonzero
  probability under health: that is what "defeasible" means here.
tags:
- philosophy-of-language
- epistemology
- causality
date: '2026-11-12'
line:
- record-as-apparatus
- pragmatic-transport
grounds:
- CASE-tmpaky45
bears_on:
- QUESTION-285
summary: >-
  The owner's, U3 of the exchange "Meaning Transmission Explained"
  (2026-11-07): "if the alarm doesn't trigger when presented with
  appropriate conditions (i.e. the debugger interrogates the system by
  inserting an intervention with a particular expected response profile)
  that *means* the alarm mechanism is broken." It was put forward as a
  case of meaning with no sentient emitter, on U1's question. Narrowed
  at the review of [#483](https://github.com/dmarx/nucleation/issues/483) the owner relayed on 2026-11-12 into two
  readings with their own criteria of correctness. Defeasible: under a
  probabilistic response model the absence shifts support toward fault
  hypotheses, as with the likelihood ratio of 49 in [CASE-tmpl4kyp](../cases.d/CASE-tmpl4kyp.md); it is
  correct when the shift matches the model, whether or not the
  mechanism turns out broken. Factive: under a deterministic,
  independently validated response guarantee, the absence entails that
  the guarantee was violated; it is correct only when it was. The first
  is the general reading, the second its limiting case. Proposed.
---
<!-- inactive-ok-file: CASE-tmpv6i22 CLAIM-tmpz1xb5 CASE-tmpl4kyp ARG-tmpwo5na ARG-tmpkk8m0 — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: THEORY-444 THEORY-220 — Proposed; readings cited with their standing -->

# CLAIM-tmpkr3ti: An absence of response under an inserted intervention with an expected response profile is diagnostic evidence about the mechanism under test, carried with nothing emitted: under a probabilistic response model it shifts support toward fault by its likelihood ratio, and in the limiting case of a deterministic, independently validated response guarantee it entails that the guarantee was violated

## The claim

The owner, at U3 of the exchange "Meaning Transmission Explained"
(https://chatgpt.com/share/6af517f7-cb48-83ea-8395-df7d52333dc7), on the
smoke detector of [CASE-tmpv6i22](../cases.d/CASE-tmpv6i22.md): "consider someone debugging a
malfunctioning system. if the alarm doesn't trigger when presented with
appropriate conditions (i.e. the debugger interrogates the system by
inserting an intervention with a particular expected response profile)
that *means* the alarm mechanism is broken."

U1 asked how meaning can be transmitted "independent of any sentient
emitter or receiver". The owner's case answers the emitter half in an
unexpected way. Nothing is emitted. The broken detector produces no
signal, and "Indeed, its failure might prevent it from generating any
output whatsoever" (A5 §2). What carries the meaning is an absence. It
carries it only because an intervention with an expected response was put
to the system.

## Two readings of "means"

The review of [#483](https://github.com/dmarx/nucleation/issues/483) the owner relayed on 2026-11-12 separated the two
readings below. Its summary: "meaningful diagnostic evidence need not be
infallible evidence."

| reading | model of the response | what the absence establishes | correct when |
|---|---|---|---|
| **defeasible** (general) | probabilistic: P(response \| healthy, do(I)) and P(response \| fault, do(I)) | a shift of support toward fault, by the likelihood ratio P(none \| fault, do(I)) / P(none \| healthy, do(I)) | the shift is the one the model licenses; it stays correct if the mechanism turns out healthy |
| **factive** (limiting) | deterministic: a response guarantee, validated independently of this test | that the guarantee was violated | the guarantee was in fact violated |

- **The defeasible reading is the general one.** In [CASE-tmpl4kyp](../cases.d/CASE-tmpl4kyp.md)'s chain,
  with a 2% readout error, the silent injector test has a likelihood
  ratio of 0.98/0.02 = 49, and silence in clean air has 1. That is A5 §1's
  contrast made exact (recomputed): "In ordinary operation, silence is
  compatible with normal functioning. Under controlled stimulation,
  silence can be evidence of a malfunction." It is evidence before
  anyone knows whether the mechanism is broken, which is what a diagnosis
  is for.
- **The factive reading is its limiting case.** As the healthy
  probability of no response goes to zero, the likelihood ratio grows
  without bound. Where a response guarantee holds with certainty and has
  been validated independently of the test, the absence entails a
  violation. This is natural meaning in Grice's sense, "x means that p
  entails p" ([NOTE-735](../notes.d/NOTE-735.md); [THEORY-444](../theory.d/THEORY-444.md)), and holds only under the guarantee.
- **The owner's "*means*"** is the second reading if the debugger's
  "appropriate conditions" carry such a guarantee, and the first if they
  carry only a reliable expectation. The claim takes the first as the
  general case.
- **Both readings are about the mechanism under test, its test path
  included.** A failed injector makes the absence count against the
  arrangement, not the detector (A5 §1; [CASE-152](../cases.d/CASE-152.md)).

## What the record already holds, and what this adds

- **The formal core is held and demonstrated.** [CLAIM-414](CLAIM-414.md) and [CLAIM-407](CLAIM-407.md):
  systems that agree under ordinary operation can differ in their response
  to an intervention, which only the intervention exposes.
- **That one silence does not localize the fault is held** ([CASE-152](../cases.d/CASE-152.md)).
- **Inquiry fixing what would count as an answer is held** ([CLAIM-470](CLAIM-470.md)).
- **New here** is the semantic reading. The record's line on meaning with
  no sentient party ([TERM-089](../terms.d/TERM-089.md), [CLAIM-525](CLAIM-525.md), [QUESTION-285](../questions.d/QUESTION-285.md)) locates meaning in
  what an organization does with a difference that reaches it. This claim
  locates it in a difference that does not arrive, read against a response
  the intervention made expected. On both readings the meaning lies in the
  relation among the intervention, the response model and the outcome,
  not in any signal (A5 §2: "The meaning is not encoded in the silence
  alone").

## What it does not say

- That the debugger must be sentient. A5 §3 replaces the person with an
  automated tester. What a tester needs to register a bounded
  non-response is [CLAIM-tmpz1xb5](CLAIM-tmpz1xb5.md).
- That the response model is the system's own. Here it is the designer's
  ([QUESTION-128](../questions.d/QUESTION-128.md); [THEORY-220](../theory.d/THEORY-220.md) for a system that holds its own).
- Which component failed, or how a real test's error rates are known.

The inference to the defeasible reading is [ARG-tmpwo5na](../arguments.d/ARG-tmpwo5na.md), and to the
factive reading under a guarantee, [ARG-tmpkk8m0](../arguments.d/ARG-tmpkk8m0.md).
