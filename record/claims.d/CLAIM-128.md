---
number: 128
status: Proposed
formerly:
- CLAIM-tmp0d575
title: 'No single ranking of translations holds across tasks: where distortion profiles trade off, only a task''s priorities rank them, and the theory of fidelity fixes no weighting'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Split under ADR-043 at the owner's direction, from the owner's
    promotion audit of 2026-10-19. The claim was filed demonstrated, but
    only its order-theoretic part is proved: trade-off is incomparability
    under the componentwise order, and positive weights can rank a
    trade-off either way. That part is now CLAIM-371, Active, and this
    claim rests on it. What stays is the thesis that fidelity is ranked
    only relative to a task and that the theory fixes no weighting. It is
    argued from the manuscript, and whether trade-offs occur for the tasks
    studied has no observation under it, so by ADR-043's rule it is
    interpretive. The title is restated to lead with the thesis; the
    defeat condition, which was already about the thesis, is unchanged.
    The status stays Proposed.
role: thesis
warrant: interpretive
defeated_if: >-
  For the tasks studied, the components of the fidelity profile D(T)
  order all compared transports the same way, so that no trade-offs
  occur; or the theory forces a single weighting of the components
  instead of leaving it to be chosen per task.
tags:
- model-comparison
- philosophy-of-language
date: '2026-10-10'
line: pragmatic-transport
rests_on:
- CLAIM-106
- CLAIM-371
complements:
- CLAIM-033
- CLAIM-240
- CLAIM-347
- CLAIM-354
uses:
- TERM-043
summary: >-
  A129 §3, after the owner's U41 "agreed." to unifying the fidelity
  lineages, and restated at A151 §5, A178 Ch9.7 and A203 §22. A
  translation that keeps social footing and loses rhyme is not ranked
  above or below one that does the opposite until a task says which
  matters. It does not say how the components are measured, nor that
  they are independent.
---
<!-- inactive-ok-file: CLAIM-033 — Proposed; open, and cited as open: the claim is under test, not settled -->

# CLAIM-128: No single ranking of translations holds across tasks: where distortion profiles trade off, only a task's priorities rank them, and the theory of fidelity fixes no weighting

## The claim

Fidelity is a profile of directed distortions, compared component by
component ([TERM-043](../terms.d/TERM-043.md)). One transport is at least as faithful as another
when it distorts no component more. When one transport is better on one
component and worse on another, neither is at least as faithful as the
other. A129 §3: "When the profiles trade off, the transports are
incomparable without selecting additional priorities." Its example: "A
translation that preserves social footing but discards rhyme need not be
ranked unconditionally above or below one that does the opposite."

A ranking appears only when a task fixes weights, D_w = Σ_j w_j D_j, and a
different task fixes different weights. So no ranking of translations
holds across tasks. A129 §3: "**Fidelity is a family of directed
comparisons whose meaning depends on which structures the communicative
task requires.**" It connects the vector form to "our earlier rejection of a
universal equivalence relation", which is [CLAIM-106](CLAIM-106.md): fidelity is graded
and directed, and equivalence is its zero-distortion limit. This claim
rests on that one, because a profile of graded distortions is what makes
trade-offs possible.

The claim recurs. A151 §5: "two translations can preserve different
structures without being forced into a universal ranking." A178 Ch9.7:
"Partial orders on fidelity profiles". A203 §22: "no universal weighting is
assumed". It complements [CLAIM-033](CLAIM-033.md), which found at A75 that a translation can
broaden the readings along one dimension while narrowing them along
another: that is one trade-off, in the region picture.

## What it does not say

It does not say how the components are measured. Only D_obs has a formula,
and D_causal needs a correspondence on interventions that nothing yet
fixes ([QUESTION-005](../questions.d/QUESTION-005.md)). It does not say the components are independent.
Whether they move together under iteration is [QUESTION-013](../questions.d/QUESTION-013.md). If they do
for every task the manuscript studies, trade-offs never arise there and the
claim is defeated for those tasks.

It does not say a scalar is illegitimate. A task-relative weighting is
what the claim allows. It denies only that one weighting is fixed by the
theory of fidelity itself.

## Note of 2026-10-19: split under [ADR-043](../decisions.d/ADR-043.md)

The order-theoretic part of this claim is now [CLAIM-371](CLAIM-371.md), with its
proof: under the componentwise order, two profiles are incomparable exactly
when they trade off, positive weights can then rank them either way, and no
positive weighting reverses a dominance. That part is demonstrated and
Active. This claim keeps the thesis built on it, that a ranking of
translations exists only relative to a task and that the theory of
fidelity fixes no weighting, and is interpretive. Its defeat condition was
already about the thesis and is unchanged.

## Note of 2026-10-30: what holds it back

No fidelity profile has been measured for any compared pair of
transports on any task. Only D_obs has a formula (QUESTION-005), and
whether components move together is QUESTION-013, so whether trade-offs
occur at all, the first branch of the defeat condition, has no
observation. The order-theoretic part is CLAIM-371 and is Active.
