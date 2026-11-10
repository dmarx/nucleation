---
status: Proposed
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

# SYNTHESIS-tmptiwlg: What sets when a network acquires a structure, and whether acquisition is one kind of event or several, is open: the record holds partial answers each proved or measured in one setting, refinements asking whether each survives another start, optimizer, input law or architecture, a question whether training's order follows the posterior's order in sample size, and a question whether circuits forming over shared features predict held-out training interventions, which the line's frustration, concept and persona entries cite

*A part account of the learned-structure line (ADR-083); the line's account is built over it and its sibling parts. Every component is a question; the part holds no claim.*

## The account

- **The root.** QUESTION-039 (filed in the fourth synthesis pass, the
  record's; Open) asks what sets the order and moment at which a network
  acquires a structure, and whether acquisition is one kind of event or
  several. Its body lists partial answers, each with its limit: eigenspace
  order in the kernel regime (THEORY-086), depth and plateaus in deep
  linear networks (THEORY-187), invariances arriving with the
  training-set size (THEORY-200), a correlation horizon (THEORY-204),
  stepwise eigenvectors for Barlow Twins (THEORY-229), the optimizer
  setting sequential onset in a toy model (THEORY-253), sample-count
  thresholds (THEORY-283, THEORY-293). Its note of 2026-10-26 adds that
  in small attention-only transformers the moment is when a composition
  becomes available (THEORY-973), and that the refined-LLC study reports
  several kinds of event per component. Its note of 2026-11-04 adds Dong's
  answer for conjunction circuits, "Acquisition is one kind of
  rate-limiting event, a single joint step", single-author and
  unreplicated.
- **Whether each partial answer survives.** Six questions refine
  QUESTION-039, each holding the promotion condition of the reading it
  names: QUESTION-158 (THEORY-283, gradient descent without a spectral
  start or a second input law), QUESTION-166 (THEORY-187, starts off the
  decoupled set), QUESTION-175 (THEORY-229, generic small
  initialization), QUESTION-176 (THEORY-293, whether trained networks
  reach the capacity-optimal allocation), QUESTION-193 (THEORY-253, a
  derivation for sign descent and a trained-network test) and
  QUESTION-305 (THEORY-481, alignment not assumed). QUESTION-081 (the
  assistant's, from reading Dominé et al. and Ziyin et al., filed at the
  owner's request) refines QUESTION-039 too: whether the regime a layer
  scale sets under gradient flow survives SGD's drift toward balance.
- **Training's order against the posterior's.** QUESTION-363 (the
  owner's challenge at U4 of "Analyze nucleation concepts", which A4
  conceded in part; Open) refines QUESTION-039. Its partial datum
  (THEORY-1275, rechecked on 2026-11-06) is the toy model of
  superposition, where SGD at n = 1,000 ends short of the 6-gon the
  posterior favours. Its note of 2026-11-04 records Dong's finding that
  learning rate is "a clock, never a temperature" for transformers.
- **Circuits as regimes over shared features.** QUESTION-275 (the
  owner's question at T24 of "Experimental Infrastructure Review", with
  the reply's research question as its test; Open) refines QUESTION-039.
  Its "Acquisition" bullet calls its question whether a circuit emerges
  by acquiring or reorganizing features "QUESTION-039's second half". It
  names its test: a model fitted to early checkpoints must out-predict
  feature-only and circuit-only descriptions on held-out training
  interventions. QUESTION-193's note of 2026-10-26 takes a testbed from
  the works read for it (THEORY-981).
- **Instruments.** QUESTION-234 (the promotion condition of THEORY-243;
  Open) asks whether interchange interventions leave the mediating
  direction underdetermined in trained networks. Its note of 2026-10-26
  takes two works read for QUESTION-275, and its note of 2026-10-27
  names QUESTION-274 as the neighbouring question. QUESTION-274 (filed
  2026-10-27 from the circuits readings; Open) asks whether two
  dictionaries of equal fidelity give the same validated circuit; it is
  "THEORY-802's thesis moved from alignments to dictionaries".

Outside this part, QUESTION-275 is the line's most cited question. From the
frustration part (SYNTHESIS-tmp4xa7p) it cites CASE-113, CLAIM-367 and CLAIM-366 as
apparatus the record already held, CLAIM-263's quotient under "What would
not answer it", and CLAIM-555 and CASE-197 in its note of 2026-11-04;
CASE-193 calls itself a caution for it. CLAIM-555 and CASE-197 also cite QUESTION-363. In the concepts
part (SYNTHESIS-tmp3crnp), QUESTION-360 proposes QUESTION-275's setting for tracking
its criteria over training. Among the persona entries, CLAIM-543 bears
on QUESTION-275 and QUESTION-370 lists it under "Bears on".

## The components

- QUESTION-039, the record's (fourth synthesis pass, 2026-10-12), Open.
- QUESTION-081, the assistant's from two readings, filed at the owner's
  request, Open.
- QUESTION-158, QUESTION-166, QUESTION-175, QUESTION-176, QUESTION-193
  and QUESTION-305, each a promotion condition moved from the reading
  named above when that reading was narrowed and promoted (2026-10-19 to
  2026-10-29), Open.
- QUESTION-363, the owner's challenge, narrowed by A4, Open.
- QUESTION-275, the owner's question with the reply's test, Open.
- QUESTION-234, a promotion condition moved from THEORY-243, Open.
- QUESTION-274, filed from the circuits readings of 2026-10-26, Open.

## Links tested as claims

None. Every component is an open question, and the links among them are
`refines` and dated notes. No component offers an integration to test.

## Not stated on the record

- **QUESTION-039 and the coarse-to-fine questions (SYNTHESIS-tmpha4sq).**
  QUESTION-217's third relation, acquisition, is QUESTION-039's subject,
  and both list THEORY-086 and the deep linear readings. Neither refines
  or names the other.
- **QUESTION-081 and QUESTION-164 (SYNTHESIS-tmpexmgz).** Both turn on the law of
  balance (THEORY-211, LIT-1012). QUESTION-164's answer would bear on
  QUESTION-081's "fast drift" branch, and no entry says so.
- **QUESTION-274 and QUESTION-275's feature arm.** QUESTION-275's
  cautions for the feature arm cite the same dictionary-resolution
  readings as QUESTION-274 (THEORY-1016, THEORY-992). They are joined
  only through QUESTION-234's note.
- **The unlinked timing entries.** CLAIM-360's "B, inside the same case,
  at a time budget" uses THEORY-187 and THEORY-740; QUESTION-165 and
  QUESTION-233 ask whether sample-count thresholds have the reason their
  readings give. None is related to QUESTION-039 (the line's account).

## What it does not say

- That acquisition is one kind of event: QUESTION-039 holds evidence both
  ways (THEORY-967, THEORY-1353).
- That any partial answer holds outside its setting.
- That a transformer's circuits are organizational regimes, or
  perspectives: QUESTION-275 says "Nothing here says that a circuit is a
  perspective."
- Anything with standing of its own.
