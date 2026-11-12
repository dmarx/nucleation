---
status: Proposed
title: "Under a deterministic, independently validated response guarantee, an absence of the guaranteed response to a delivered intervention entails that the guarantee was violated"
version: 1
form: formal-application
grounds:
- CASE-tmpaky45
concludes:
- CLAIM-tmpkr3ti
tags:
- epistemology
- logic
date: '2026-11-12'
line:
- record-as-apparatus
summary: >-
  The factive limiting case of [CLAIM-tmpkr3ti](../claims.d/CLAIM-tmpkr3ti.md), separated from the
  defeasible inference ([ARG-tmpwo5na](ARG-tmpwo5na.md)) at the review of [#483](https://github.com/dmarx/nucleation/issues/483) the owner
  relayed on 2026-11-12. If a guarantee states that whenever the
  intervention is delivered the response occurs within the interval,
  then a delivered intervention with no response falsifies the
  guarantee: modus tollens. The guarantee must be validated
  independently of the test, or the inference only restates the test.
  Proposed. The wording is the filer's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpaky45 CLAIM-tmpkr3ti ARG-tmpwo5na CASE-tmpl4kyp — filed from the same exchange, Proposed -->

# ARG-tmpkk8m0: Under a deterministic, independently validated response guarantee, an absence of the guaranteed response to a delivered intervention entails that the guarantee was violated

## The inference

1. A guarantee G: whenever intervention I is delivered to the mechanism
   in its specified condition, response R occurs within interval τ. G is
   deterministic, and it was validated independently of the present test
   (by construction, certification or earlier tests).
2. [CASE-tmpaky45](../cases.d/CASE-tmpaky45.md): I was delivered, and no R occurred within τ.
3. So G was violated on this occasion. By modus tollens, the mechanism
   (its test path included) was not in its specified condition.

This is natural meaning in Grice's factive sense: the absence means that
the guarantee failed, and that entails that it did.

## Critical questions

- **Does the rule apply?** Only if both premises hold. If I was not in
  fact delivered (the injector failed), premise 2 is false, and the
  absence entails nothing about the detector. That is why "the mechanism"
  includes the test path.
- **Is the guarantee really deterministic?** Real guarantees have error
  rates. Where they do, the inference becomes [ARG-tmpwo5na](ARG-tmpwo5na.md)'s: a shift of
  support, not an entailment. The factive reading is the limit as the
  healthy probability of no response goes to zero ([CLAIM-tmpkr3ti](../claims.d/CLAIM-tmpkr3ti.md)'s
  table).
- **Is the validation independent?** If G is known only from this test,
  "G was violated" restates the outcome. Independence is what makes the
  conclusion informative.

## What it does not show

That any real alarm carries such a guarantee, or which component failed.
In [CASE-tmpl4kyp](../cases.d/CASE-tmpl4kyp.md)'s chain, with readout errors, only the defeasible
reading applies.
