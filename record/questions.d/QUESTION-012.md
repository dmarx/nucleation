---
number: 12
status: Open
formerly:
- QUESTION-tmpcginb
title: 'When does reconstruction through an intermediate image preserve or degrade observational structure relative to direct text-to-text reconstruction?'
version: 1
tags:
- compositionality
- probabilistic-modeling
- philosophy-of-language
date: '2026-10-08'
line: pragmatic-transport
refines:
- QUESTION-002
summary: >-
  Proposal v6's Result 5 (A100), "especially interesting as a
  proposition that connects the formal theory to a novel empirical
  setting". Dropped from the manuscript, which keeps the
  text→image→caption chain as Case III but states no result about
  composition through a medium.
---
<!-- inactive-ok-file: CLAIM-076 CLAIM-098 CLAIM-178 THEORY-174 — listed as material that may bear on this question, not as settled -->
<!-- inactive-ok-file: CLAIM-087 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# QUESTION-012: When does reconstruction through an intermediate image preserve or degrade observational structure relative to direct text-to-text reconstruction?

## Why it is a question

A100, five target formal results; the first four "can be developed from
established mathematical machinery. The fifth is especially interesting":
"**Result 5 — Cross-modal transport composition.** Specify conditions under which
composition through an intermediate image representation preserves or degrades
observational structure relative to direct text-to-text reconstruction."

## What would count as an answer

A bound or counterexample for chains that pass through a medium with a
different cover ([CASE-009](../cases.d/CASE-009.md)). It would cover the case in which the image adds
distinctions as well as the one in which it loses them ([CLAIM-087](../claims.d/CLAIM-087.md)). The
manuscript's Case III would measure it ("alternate text→image→caption→image and
compare against text-only reconstruction chains"); its theory says nothing about
it beyond Propositions 1 and 2, which assume a fixed correspondence of contexts.

## Note of 2026-10-11: material in the record that may bear on this

A synthesis review of 2026-10-11 found these entries bearing on this
question without being linked to it. Each is listed for what its title
says; none has yet been assessed as an answer, and none is linked by
`answers`.

- [THEORY-174](../theory.d/THEORY-174.md): Classical simulations between empirical models on different
  scenarios never create contextuality, and a…
- [CLAIM-076](../claims.d/CLAIM-076.md): Cross-modal chains expose reconstruction because media differ
  in expressive affordances, and each…
- [CLAIM-098](../claims.d/CLAIM-098.md): Translation and cross-modal reconstruction need not be group
  actions: they form a category or semigroup of…
- [CLAIM-178](../claims.d/CLAIM-178.md): A manuscript should be a view over the argument and not its
  only copy: a draft written straight from an…

## Note of 2026-10-12: two listed titles were scoped on 2026-10-10

PR [#121](https://github.com/dmarx/nucleation/issues/121)'s round of 2026-10-10 scoped two of the entries listed above.
[CLAIM-tmpz7og0](../claims.d/CLAIM-tmpz7og0.md), granted, shows that [CLAIM-098](../claims.d/CLAIM-098.md)'s "category or semigroup"
holds for approximate transports only if the distortion obeys a triangle
inequality and later kernels are nonexpansive. [CLAIM-tmprwo1c](../claims.d/CLAIM-tmprwo1c.md), granted,
shows that under Contextuality-by-Default a deterministic recoding can
create or remove contextuality once the source signals. It notes that
[THEORY-174](../theory.d/THEORY-174.md), whose title says simulations "never create contextuality", is
about no-signalling models. Both bear on what a chain through an
intermediate image can do to observational structure.
