---
number: 34
status: Proposed
formerly:
- SYNTHESIS-tmptiwlg
title: 'What sets when a network acquires a structure, and whether acquisition is one kind of event or several, is open: the record holds partial answers each proved or measured in one setting, refinements asking whether each survives another start, optimizer, input law or architecture, a question whether training''s order follows the posterior''s order in sample size, and a question whether circuits forming over shared features predict held-out training interventions, which the line''s frustration, concept and persona entries cite'
version: 1
defeated_if: >-
  A component misstated or misattributed here; an in-force component of
  this part of the learned-structure line (the order and moment of
  acquisition in training, and the instruments for observing it) left out
  without a reason given; or a link this account states that no component
  states. Its standing is its components'.
tags:
- learning-theory
- representation-learning
date: '2026-11-10'
line:
- learned-structure
integrates:
- QUESTION-039
- QUESTION-081
- QUESTION-158
- QUESTION-166
- QUESTION-175
- QUESTION-176
- QUESTION-193
- QUESTION-305
- QUESTION-363
- QUESTION-275
- QUESTION-234
- QUESTION-274
bears_on:
- QUESTION-039
---
<!-- inactive-ok-file: ADR-083 CASE-193 CLAIM-263 CLAIM-367 CLAIM-555 THEORY-200 THEORY-802 THEORY-967 THEORY-1016 THEORY-1353 — Proposed; components, citations and the decisions this account follows, with their standing -->

# SYNTHESIS-034: What sets when a network acquires a structure, and whether acquisition is one kind of event or several, is open: the record holds partial answers each proved or measured in one setting, refinements asking whether each survives another start, optimizer, input law or architecture, a question whether training's order follows the posterior's order in sample size, and a question whether circuits forming over shared features predict held-out training interventions, which the line's frustration, concept and persona entries cite

*A part account of the learned-structure line ([ADR-083](../decisions.d/ADR-083.md)); the line's account is built over it and its sibling parts. Every component is a question; the part holds no claim.*

## The account

- **The root.** [QUESTION-039](../questions.d/QUESTION-039.md) (filed in the fourth synthesis pass, the
  record's; Open) asks what sets the order and moment at which a network
  acquires a structure, and whether acquisition is one kind of event or
  several. Its body lists partial answers, each with its limit: eigenspace
  order in the kernel regime ([THEORY-086](../theory.d/THEORY-086.md)), depth and plateaus in deep
  linear networks ([THEORY-187](../theory.d/THEORY-187.md)), invariances arriving with the
  training-set size ([THEORY-200](../theory.d/THEORY-200.md)), a correlation horizon ([THEORY-204](../theory.d/THEORY-204.md)),
  stepwise eigenvectors for Barlow Twins ([THEORY-229](../theory.d/THEORY-229.md)), the optimizer
  setting sequential onset in a toy model ([THEORY-253](../theory.d/THEORY-253.md)), sample-count
  thresholds ([THEORY-283](../theory.d/THEORY-283.md), [THEORY-293](../theory.d/THEORY-293.md)). Its note of 2026-10-26 adds that
  in small attention-only transformers the moment is when a composition
  becomes available ([THEORY-973](../theory.d/THEORY-973.md)), and that the refined-LLC study reports
  several kinds of event per component. Its note of 2026-11-04 adds Dong's
  answer for conjunction circuits, "Acquisition is one kind of
  rate-limiting event, a single joint step", single-author and
  unreplicated.
- **Whether each partial answer survives.** Six questions refine
  [QUESTION-039](../questions.d/QUESTION-039.md), each holding the promotion condition of the reading it
  names: [QUESTION-158](../questions.d/QUESTION-158.md) ([THEORY-283](../theory.d/THEORY-283.md), gradient descent without a spectral
  start or a second input law), [QUESTION-166](../questions.d/QUESTION-166.md) ([THEORY-187](../theory.d/THEORY-187.md), starts off the
  decoupled set), [QUESTION-175](../questions.d/QUESTION-175.md) ([THEORY-229](../theory.d/THEORY-229.md), generic small
  initialization), [QUESTION-176](../questions.d/QUESTION-176.md) ([THEORY-293](../theory.d/THEORY-293.md), whether trained networks
  reach the capacity-optimal allocation), [QUESTION-193](../questions.d/QUESTION-193.md) ([THEORY-253](../theory.d/THEORY-253.md), a
  derivation for sign descent and a trained-network test) and
  [QUESTION-305](../questions.d/QUESTION-305.md) ([THEORY-481](../theory.d/THEORY-481.md), alignment not assumed). [QUESTION-081](../questions.d/QUESTION-081.md) (the
  assistant's, from reading Dominé et al. and Ziyin et al., filed at the
  owner's request) refines [QUESTION-039](../questions.d/QUESTION-039.md) too: whether the regime a layer
  scale sets under gradient flow survives SGD's drift toward balance.
- **Training's order against the posterior's.** [QUESTION-363](../questions.d/QUESTION-363.md) (the
  owner's challenge at U4 of "Analyze nucleation concepts", which A4
  conceded in part; Open) refines [QUESTION-039](../questions.d/QUESTION-039.md). Its partial datum
  ([THEORY-1275](../theory.d/THEORY-1275.md), rechecked on 2026-11-06) is the toy model of
  superposition, where SGD at n = 1,000 ends short of the 6-gon the
  posterior favours. Its note of 2026-11-04 records Dong's finding that
  learning rate is "a clock, never a temperature" for transformers.
- **Circuits as regimes over shared features.** [QUESTION-275](../questions.d/QUESTION-275.md) (the
  owner's question at T24 of "Experimental Infrastructure Review", with
  the reply's research question as its test; Open) refines [QUESTION-039](../questions.d/QUESTION-039.md).
  Its "Acquisition" bullet calls its question whether a circuit emerges
  by acquiring or reorganizing features "[QUESTION-039](../questions.d/QUESTION-039.md)'s second half". It
  names its test: a model fitted to early checkpoints must out-predict
  feature-only and circuit-only descriptions on held-out training
  interventions. [QUESTION-193](../questions.d/QUESTION-193.md)'s note of 2026-10-26 takes a testbed from
  the works read for it ([THEORY-981](../theory.d/THEORY-981.md)).
- **Instruments.** [QUESTION-234](../questions.d/QUESTION-234.md) (the promotion condition of [THEORY-243](../theory.d/THEORY-243.md);
  Open) asks whether interchange interventions leave the mediating
  direction underdetermined in trained networks. Its note of 2026-10-26
  takes two works read for [QUESTION-275](../questions.d/QUESTION-275.md), and its note of 2026-10-27
  names [QUESTION-274](../questions.d/QUESTION-274.md) as the neighbouring question. [QUESTION-274](../questions.d/QUESTION-274.md) (filed
  2026-10-27 from the circuits readings; Open) asks whether two
  dictionaries of equal fidelity give the same validated circuit; it is
  "[THEORY-802](../theory.d/THEORY-802.md)'s thesis moved from alignments to dictionaries".

Outside this part, [QUESTION-275](../questions.d/QUESTION-275.md) is the line's most cited question. From the
frustration part ([SYNTHESIS-026](SYNTHESIS-026.md)) it cites [CASE-113](../cases.d/CASE-113.md), [CLAIM-367](../claims.d/CLAIM-367.md) and [CLAIM-366](../claims.d/CLAIM-366.md) as
apparatus the record already held, [CLAIM-263](../claims.d/CLAIM-263.md)'s quotient under "What would
not answer it", and [CLAIM-555](../claims.d/CLAIM-555.md) and [CASE-197](../cases.d/CASE-197.md) in its note of 2026-11-04;
[CASE-193](../cases.d/CASE-193.md) calls itself a caution for it. [CLAIM-555](../claims.d/CLAIM-555.md) and [CASE-197](../cases.d/CASE-197.md) also cite [QUESTION-363](../questions.d/QUESTION-363.md). In the concepts
part ([SYNTHESIS-025](SYNTHESIS-025.md)), [QUESTION-360](../questions.d/QUESTION-360.md) proposes [QUESTION-275](../questions.d/QUESTION-275.md)'s setting for tracking
its criteria over training. Among the persona entries, [CLAIM-543](../claims.d/CLAIM-543.md) bears
on [QUESTION-275](../questions.d/QUESTION-275.md) and [QUESTION-370](../questions.d/QUESTION-370.md) lists it under "Bears on".

## The components

- [QUESTION-039](../questions.d/QUESTION-039.md), the record's (fourth synthesis pass, 2026-10-12), Open.
- [QUESTION-081](../questions.d/QUESTION-081.md), the assistant's from two readings, filed at the owner's
  request, Open.
- [QUESTION-158](../questions.d/QUESTION-158.md), [QUESTION-166](../questions.d/QUESTION-166.md), [QUESTION-175](../questions.d/QUESTION-175.md), [QUESTION-176](../questions.d/QUESTION-176.md), [QUESTION-193](../questions.d/QUESTION-193.md)
  and [QUESTION-305](../questions.d/QUESTION-305.md), each a promotion condition moved from the reading
  named above when that reading was narrowed and promoted (2026-10-19 to
  2026-10-29), Open.
- [QUESTION-363](../questions.d/QUESTION-363.md), the owner's challenge, narrowed by A4, Open.
- [QUESTION-275](../questions.d/QUESTION-275.md), the owner's question with the reply's test, Open.
- [QUESTION-234](../questions.d/QUESTION-234.md), a promotion condition moved from [THEORY-243](../theory.d/THEORY-243.md), Open.
- [QUESTION-274](../questions.d/QUESTION-274.md), filed from the circuits readings of 2026-10-26, Open.

## Links tested as claims

None. Every component is an open question, and the links among them are
`refines` and dated notes. No component offers an integration to test.

## Not stated on the record

- **[QUESTION-039](../questions.d/QUESTION-039.md) and the coarse-to-fine questions ([SYNTHESIS-029](SYNTHESIS-029.md)).**
  [QUESTION-217](../questions.d/QUESTION-217.md)'s third relation, acquisition, is [QUESTION-039](../questions.d/QUESTION-039.md)'s subject,
  and both list [THEORY-086](../theory.d/THEORY-086.md) and the deep linear readings. Neither refines
  or names the other.
- **[QUESTION-081](../questions.d/QUESTION-081.md) and [QUESTION-164](../questions.d/QUESTION-164.md) ([SYNTHESIS-028](SYNTHESIS-028.md)).** Both turn on the law of
  balance ([THEORY-211](../theory.d/THEORY-211.md), [LIT-1012](../literature.d/LIT-1012.md)). [QUESTION-164](../questions.d/QUESTION-164.md)'s answer would bear on
  [QUESTION-081](../questions.d/QUESTION-081.md)'s "fast drift" branch, and no entry says so.
- **[QUESTION-274](../questions.d/QUESTION-274.md) and [QUESTION-275](../questions.d/QUESTION-275.md)'s feature arm.** [QUESTION-275](../questions.d/QUESTION-275.md)'s
  cautions for the feature arm cite the same dictionary-resolution
  readings as [QUESTION-274](../questions.d/QUESTION-274.md) ([THEORY-1016](../theory.d/THEORY-1016.md), [THEORY-992](../theory.d/THEORY-992.md)). They are joined
  only through [QUESTION-234](../questions.d/QUESTION-234.md)'s note.
- **The unlinked timing entries.** [CLAIM-360](../claims.d/CLAIM-360.md)'s "B, inside the same case,
  at a time budget" uses [THEORY-187](../theory.d/THEORY-187.md) and [THEORY-740](../theory.d/THEORY-740.md); [QUESTION-165](../questions.d/QUESTION-165.md) and
  [QUESTION-233](../questions.d/QUESTION-233.md) ask whether sample-count thresholds have the reason their
  readings give. None is related to [QUESTION-039](../questions.d/QUESTION-039.md) (the line's account).

## What it does not say

- That acquisition is one kind of event: [QUESTION-039](../questions.d/QUESTION-039.md) holds evidence both
  ways ([THEORY-967](../theory.d/THEORY-967.md), [THEORY-1353](../theory.d/THEORY-1353.md)).
- That any partial answer holds outside its setting.
- That a transformer's circuits are organizational regimes, or
  perspectives: [QUESTION-275](../questions.d/QUESTION-275.md) says "Nothing here says that a circuit is a
  perspective."
- Anything with standing of its own.
