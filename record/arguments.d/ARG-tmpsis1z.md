---
status: Proposed
title: 'The corroborates decision, as an existence case, shows a grammar revision making a distinction consequential'
statement: >-
  The graph that asserted an unmade inference, and the decision that
  answered it with `corroborates`, show by existence that a revision of the
  record's rules can make a distinction produce findings it did not produce
  before; the case shows a distinction made expressible, and the stronger
  clause, an expressible but inert distinction made consequential, needs a
  second instance, which the lint check on Read notes of unreached works
  supplies
version: 1
history:
- version: 1
  date: '2026-11-26'
  note: >-
    Filed 2026-11-26 by the assistant, with the claim it argues, from the
    exchange "Alignment consequences brainstorm" (ChatGPT, 2026-11-26).
form: existence
grounds:
- CASE-131
concludes:
- CLAIM-tmpxl7dc
tags:
- design-rationale
- software-engineering
date: '2026-11-26'
line:
- record-as-apparatus
summary: >-
  A25 §3 of the exchange "Alignment consequences brainstorm" cites the
  `corroborates` decision (ADR-044, CASE-131) as the record "developing a
  new distinction in how changes to evidence ought to become consequential".
  As an existence case for CLAIM-tmpxl7dc it holds for the weaker reading:
  before ADR-044 the difference between corroborating and depending could
  not be written, so a perturbation that drew it was not in M's domain,
  not one with Δ_M = 0. ADR-069 is the instance of the stronger reading:
  a NOTE marked Read on a LIT marked Unavailable was writable and produced
  no finding before 2026-11-01, and fails lint after it. With both, the
  claim's existence clause stands. The wording is the assistant's (Claude,
  in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpxl7dc — Proposed; the claim this argues, filed 2026-11-26 -->

# ARG-tmpsis1z: The corroborates decision, as an existence case, shows a grammar revision making a distinction consequential

## The inference

Premise (CASE-131): a claim was filed with `supports` on another; the
link fixer wrote the converse `rests_on`, asserting that the second could
not stand without the first; ADR-044 added `corroborates`, which retiring
does not walk. Conclusion (CLAIM-tmpxl7dc): a revision M → M′ can give a
perturbation δ with Δ_M(R, δ) = 0 and Δ_M′(R, δ) > 0.

## Critical questions

1. **Is the case coherent?** Yes; it is documented (CASE-131, Active) and
   the decision is Active.
2. **Does it separate the very things the conclusion says come apart?**
   Only in part. Under the old grammar the distinction between
   corroborating and depending could not be written at all: `supports`
   and `rests_on` were one relation read from two ends. So there was no δ
   expressible under M that drew it, and Δ_M(R, δ) was undefined, not
   zero. What the case shows is M′ enlarging the set of expressible
   perturbations, which is CLAIM-419's ground: a move the grammar could not
   hold, answered by amending the grammar.

   The stronger reading needs δ expressible under both rules. ADR-069
   (2026-11-01) is one: a NOTE with status Read whose `paper:` is a LIT
   marked Unavailable, Unfetched or Deferred was writable before the
   decision and produced no finding; after it, `lint.fail_on` fails on it.
   The decision says "The record has no match today", so R itself was
   unchanged and only the perturbation separates the two rule sets, which
   is the claim's shape exactly.

Verdict: the existence clause of CLAIM-tmpxl7dc stands, on ADR-069 for
"inert made consequential" and on CASE-131 for "inexpressible made
expressible". The two are different interventions on the grammar, and a
measure of Δ should report them apart: one changes F_M on a fixed domain,
the other changes the domain.
