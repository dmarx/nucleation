---
status: Proposed
title: "From the debugger's test to the claim that a failed response under an intervention means the mechanism is broken"
version: 1
form: generalization
grounds:
- CASE-tmpaky45
- CASE-152
rests_on:
- CLAIM-414
concludes:
- CLAIM-tmpkr3ti
tags:
- epistemology
- philosophy-of-language
date: '2026-11-12'
line:
- record-as-apparatus
summary: >-
  The inference from the owner's debugging case (CASE-tmpaky45, U3 of
  the exchange "Meaning Transmission Explained", 2026-11-07) to the
  owner's claim (CLAIM-tmpkr3ti) that an absence under an intervention
  with an expected profile means the mechanism under test is broken.
  Proposed. It holds for the claim as narrowed, the test's own path
  counted in the mechanism, because CASE-152 shows one silence does not
  say which part failed; and it holds only where the silence is likelier
  under a fault than without one, which CLAIM-414 supplies for
  mechanisms matched in ordinary operation. The inference is the
  filer's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpaky45 CLAIM-tmpkr3ti CASE-tmpl4kyp CLAIM-tmpz1xb5 — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: CASE-202 — Proposed; the control cited for a test that breaks what it tests -->

# ARG-tmpwo5na: From the debugger's test to the claim that a failed response under an intervention means the mechanism is broken

## The inference

1. CASE-tmpaky45: a debugger puts test smoke to a detector whose expected
   response is an alarm, and there is no alarm.
2. CLAIM-414 (demonstrated, Active): systems that agree under ordinary
   operation can differ under a specified intervention, which exposes
   what passive observation does not. A working and a broken detector
   are such a pair: both are silent in clean air, and only the working
   one sounds under the test.
3. So the silence under the test is evidence that the tested arrangement
   is the broken member of the pair, and in clean air it is not.
4. CASE-152: a missing response does not say whether nothing was
   attempted or nothing was taken up. So "the mechanism" in the
   conclusion must include the test's path (the injector, the smoke
   reaching the sensor), not only the detector.
5. Generalized: under any intervention with an expected response profile,
   where the absence is likelier with the mechanism out of profile than
   in it, the absence means, in the evidential sense, that the mechanism
   under test is broken (CLAIM-tmpkr3ti).

## Critical questions

- **Is the case typical of the class the conclusion covers?** For
  deterministic, single-fault mechanisms with a reliable test, yes: that
  is the textbook case of a functional test. The conclusion's condition,
  that the absence is likelier under a fault, is what makes it typical.
  Where the test is unreliable, the absence still bears on the mechanism,
  by its likelihood ratio (49 at A's 2% error rate, CASE-tmpl4kyp), but
  "means" in the factive sense holds only of the cases in which the
  mechanism is in fact out of profile.
- **Are there counterexamples?** One kind is excluded by step 4: the
  test's own failure (the injector, in CASE-tmpl4kyp's chain) makes the
  silence true of the arrangement and not of the detector. Another is a
  test that breaks what it tests (A8 §6; CASE-202's control). There the
  mechanism is broken after the test, and the silence means what the
  claim says; how it came to be broken is a different question. The
  third is an absence no apparatus registers. Then there is no
  distinction for the meaning to be carried by, which CLAIM-tmpz1xb5
  states as a condition.
- **Is the sample large enough?** One stipulated case carries the
  semantic reading. The formal part rests on CLAIM-414, which is
  demonstrated, and needs no sample.
- **Is "means" used in one sense throughout?** It has to be. In the
  evidential sense the conclusion follows. If "means" is read as a
  message from the detector, it does not, and that is the owner's point:
  nothing is emitted.

## What it does not show

That the expected profile could be the system's own (QUESTION-128), or
that the evidential sense of "mean" is all U1's question asked for.
Grice's non-natural meaning needs an utterer's intention, which a
debugging test does not supply.
