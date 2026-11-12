---
status: Proposed
title: "From the debugger's test and a probabilistic response model to the defeasible reading: an absence under an intervention with an expected response shifts support toward fault by its likelihood ratio"
version: 2
history:
- version: 2
  date: '2026-11-12'
  note: >-
    Revised at the review of #483 the owner relayed on 2026-11-12. The
    review found that version 1 moved from "silence is more likely under
    malfunction" to "silence means malfunction", which is valid
    evidentially and not factively. The ARG now concludes only the
    defeasible reading of CLAIM-tmpkr3ti. The factive reading, under a
    deterministic and independently validated guarantee, has its own ARG,
    ARG-tmpkk8m0. Form changed from generalization to evidence. Old
    title: From the debugger's test to the claim that a failed response
    under an intervention means the mechanism is broken.
form: evidence
grounds:
- CASE-tmpaky45
- CASE-tmpl4kyp
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
  The inference from the owner's debugging case (CASE-tmpaky45, U3 of the
  exchange "Meaning Transmission Explained", 2026-11-07), under a
  probabilistic response model, to the defeasible reading of
  CLAIM-tmpkr3ti: the absence shifts support toward fault hypotheses by
  its likelihood ratio. CASE-tmpl4kyp gives the worked instance, 49
  against 1 for the same silence in clean air. CASE-152 confines the
  conclusion to the mechanism under test, its test path included. It
  concludes nothing factive; that is ARG-tmpkk8m0's, under a stated
  guarantee. Proposed. The inference is the filer's, as revised at the
  review of #483 the owner relayed on 2026-11-12; adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-tmpaky45 CLAIM-tmpkr3ti CASE-tmpl4kyp CLAIM-tmpz1xb5 ARG-tmpkk8m0 — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: CASE-202 — Proposed; the control cited for a test that breaks what it tests -->

# ARG-tmpwo5na: From the debugger's test and a probabilistic response model to the defeasible reading: an absence under an intervention with an expected response shifts support toward fault by its likelihood ratio

## The inference

1. CASE-tmpaky45: a debugger puts test smoke to a detector whose expected
   response is an alarm, and there is no alarm.
2. CLAIM-414 (demonstrated, Active): systems that agree under ordinary
   operation can differ under a specified intervention, which exposes
   what passive observation does not. A working and a broken detector
   are such a pair.
3. A probabilistic response model gives P(no alarm | fault, do(test)) and
   P(no alarm | healthy, do(test)). Where the first exceeds the second,
   the absence raises the odds of a fault by their ratio. In CASE-tmpl4kyp
   that ratio is 0.98/0.02 = 49, and for silence in clean air it is 1.
4. CASE-152: a missing response does not say what was missing. So the
   hypotheses the support moves among are faults of the mechanism under
   test, its test path included.
5. So the absence is diagnostic evidence about that mechanism, with its
   strength fixed by the model (CLAIM-tmpkr3ti, defeasible reading).

## Critical questions

- **Is the evidence relevant to the conclusion?** Yes, wherever the
  likelihood ratio differs from 1. Where it is 1, as for silence in
  ordinary operation, the absence is no evidence, and the claim's
  defeater says so.
- **Is the model reliable?** The strength of the shift is only as good
  as the response model. A model whose error rates are guessed gives a
  guessed ratio. The conclusion is relative to the model, and the claim
  says so.
- **Is there contrary evidence?** A test that breaks what it tests (A8
  §6; CASE-202's control) makes the fault real but caused by the test.
  The evidence then bears on the mechanism after the test, which is what
  the conclusion is about. A test path that failed is covered by step 4.
- **Does the conclusion say more than the evidence?** Not now. Version 1
  concluded that the mechanism "is broken". The conclusion is now the
  shift in support, which stays correct if the mechanism turns out
  healthy.

## What it does not show

That the mechanism is broken. That follows only under a deterministic,
independently validated guarantee (ARG-tmpkk8m0). Nor does it show that
the response model is the system's own (QUESTION-128).
