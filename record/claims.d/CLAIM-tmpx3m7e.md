---
status: Proposed
title: 'Observational distortion should be summed over the contexts both covers can host, with the target''s new questions asked of the source too, and the questions only one side can decide reported as a separate change of cover, so that a rendering that adds a relation pays for it'
version: 1
role: thesis
defeated_if: >-
  Renderings that agree on the source's contexts and differ only on added
  ones are judged alike by the named receivers on the stated tasks, so
  that the added term predicts nothing.
tags:
- mathematics
- philosophy-of-language
date: '2026-10-10'
line: pragmatic-transport
rests_on:
- CLAIM-076
complements:
- CLAIM-005
- CLAIM-tmp1rlu5
uses:
- TERM-021
- TERM-043
summary: >-
  The record's repair, on 2026-10-10, after [CLAIM-tmpwvljf](CLAIM-tmpwvljf.md). D_obs sums
  over source contexts only, so a target context outside the image of τ
  is free. Asking the target's new question of the source, where its
  readers can answer it, puts it in both covers, and an addition then
  costs. Questions only one side can decide are a change of cover, which
  [CLAIM-tmp1rlu5](CLAIM-tmp1rlu5.md) makes the line's headline; they are reported, not summed.
  A proposal: the restatement is a definition, and whether its added term
  predicts anything is the defeat condition. It does not say additions
  are distortions.
---
<!-- inactive-ok-file: CLAIM-005 CLAIM-076 CLAIM-087 CLAIM-034 CLAIM-106 — Proposed; the measure restated, the claim that interpreters add relations, the improvement and adaptation claims, and the directed-fidelity thesis, cited as open -->
<!-- inactive-ok-file: CLAIM-tmp1rlu5 — Proposed; the cover-change form of the headline, cited as open -->

# CLAIM-tmpx3m7e: Observational distortion should be summed over the contexts both covers can host, with the target's new questions asked of the source too, and the questions only one side can decide reported as a separate change of cover, so that a rendering that adds a relation pays for it

## What it answers

This is the record's reply of 2026-10-10 to [CLAIM-tmpwvljf](CLAIM-tmpwvljf.md) (granted, and
right): L_obs and D_obs sum over source contexts C, so a target context
that is not τ(C) for any C appears in no term, a rendering that adds a
relation pays nothing, and a change of cover registers only as loss. The
reply restates the measure. The restatement is a definition, so it is
checkable by reading; that the added term matters to receivers is a
proposal, which the defeat condition tests.

## The claim

**Ask the new question of the source too.** A target context C′ outside
the image of τ is a question the target's readers are asked and the
source's are not. Often the source's readers can be asked it: "Is the
speaker mocking a third party?" can be put to readers of the source as
well as of the rendering. Then C′ is a context of both covers, and the
two response distributions can be compared directly.

**The restated measure.** Let 𝒞_s be the source's contexts and 𝒞_t the
target's. Sum over the source's contexts as before, and add the target's
new contexts that source readers can decide:

D⁺_obs = Σ_(C ∈ 𝒞_s) w_C d_C((K_C)# e^o_C, e^t_τ(C))
+ Σ_(C′ ∈ 𝒞_t ∖ τ(𝒞_s), decidable for source readers) w′_C′ d_C′((K_C′)# e^o_C′, e^t_C′),

with K_C′ the outcome correspondence for the new context, the identity
when both readers answer the same question in the same categories.
Report separately two counts that are not summed: the target contexts that
source readers cannot decide, and the source contexts that target readers
cannot decide. Those are the change of cover itself.

**The worked case.** [CLAIM-tmpwvljf](CLAIM-tmpwvljf.md)'s source cover has one context C, the
speaker's stance; the target's has τ(C) and a new C′, whether the speaker is
mocking a third party. Ask C′ of the source's readers. If they answer that
the speaker is not mocking anyone, with distribution e^o_C′ concentrated
on "no", and the rendering's readers answer "yes" with probability 0.6,
the second term is w′_C′ times d_C′ of those two distributions, 0.6 in
total variation. Two renderings that agree on τ(C) and differ on C′ now
have different D⁺_obs.

**Directed.** Losses (source contexts with poor images) and additions (new
contexts where the target departs from the source) are separate terms, and
the two uncountable sides are separate counts. They can be weighted
differently or reported separately, as [CLAIM-106](CLAIM-106.md)'s asymmetry asks.

**Why the undecidable ones are not summed.** A question that only one
side's readers can decide has no distribution on the other side to
compare with. Summing it would need a value for "no answer", which is a
choice, not a measurement. Such questions are a change of cover, which
[CLAIM-tmp1rlu5](CLAIM-tmp1rlu5.md) makes the line's headline, and they are counted and
described there.

## What it does not say

- It does not say additions are distortions. [CLAIM-087](CLAIM-087.md)'s improved access
  and [CLAIM-034](CLAIM-034.md)'s deliberate adaptation may be wanted. The term measures
  the departure; whether it is a fault depends on the task.
- It does not say which new questions to ask. The new contexts are fixed
  by the design, before the renderings are scored.
- It does not settle the correspondence between new contexts on the two
  sides ([QUESTION-005](../questions.d/QUESTION-005.md)).
