---
number: 649
status: Active
formerly:
- THEORY-tmpv2lo3
title: "When agents holding uniformly random consistent theories over two or three atomic sentences each average their theories once, bit by bit, with all peers within a Hamming bound of confidence, an individual agent ends up with the inconsistent theory at most 1.81% of the time, but the chance that some agent in the group does reaches 6.4% for two sentences and 16.9% for three"
version: 1
tags:
- epistemology
- network-science
- logic
date: '2026-10-16'
source:
- LIT-163
summary: >-
  Wenmackers (2011), [LIT-163](../literature.d/LIT-163.md), chapter 5, read in [NOTE-139](../notes.d/NOTE-139.md). An exact count,
  extended by sampling, of how often one round of bounded-confidence
  averaging over theories yields the inconsistent theory. The per-agent
  fraction F_AG peaks at 1.8112% (M = 2) and 0.3215% (M = 3); the
  per-profile fraction F_OP reaches 6.4298% and 16.867%. The thesis's
  headline, that the risk "can be made arbitrarily small" by adding
  sentences, rests on two values of M and is contradicted for F_OP.
---
<!-- inactive-ok-file: LIT-070 — Unavailable; a continuous-opinion model named for contrast -->
<!-- inactive-ok-file: THEORY-127 — Proposed; the discursive-dilemma account named in Connections -->

# THEORY-649: When agents holding uniformly random consistent theories over two or three atomic sentences each average their theories once, bit by bit, with all peers within a Hamming bound of confidence, an individual agent ends up with the inconsistent theory at most 1.81% of the time, but the chance that some agent in the group does reaches 6.4% for two sentences and 16.9% for three

## Source

Wenmackers (2011), [LIT-163](../literature.d/LIT-163.md), chapter 5 with its appendices A and B, read in
full in [NOTE-139](../notes.d/NOTE-139.md). [NOTE-139](../notes.d/NOTE-139.md) corrects the thesis's summary of this chapter,
and this document follows the correction.

## What was actually shown

**The model.** M atomic sentences give 2^M worlds; a theory is a set of
worlds, coded as a bit string, and the empty set is the inconsistent
theory. Each of N agents independently draws a uniformly random consistent
theory (an impartial culture). In one simultaneous update, each agent
averages each bit over the peers within Hamming distance D and rounds; a
tie keeps the old bit. A "zero-update" is an update to the inconsistent
theory. There is no truth, evidence, trust or network structure, and only
one step is analysed.

**The counts (eq. 5.1, Table 5.3).** F_AG is the fraction of agents that
zero-update; F_OP the fraction of opinion profiles in which at least one
does. Both were computed exactly for N ≤ 21 (M = 2) and N ≤ 4 (M = 3), and
by sampling 10^6 profiles per point up to N = 200 (M = 2) and N = 2500
(M = 3).

- No zero-update occurs for M = 1, D = 1 or N = 2. The minimal case,
  M = 2, N = 3, D = 2, gives F_OP = F_AG = 24/3375 = 0.711%, checked by
  hand.
- F_AG is at most 1.8112% for M = 2 (at D = 4, N = 5) and at most 0.3215%
  for M = 3.
- F_OP reaches 6.4298% for M = 2 and 16.867% for M = 3 (D = 6, N = 1780).
- Odd and even N alternate in an unexplained wobble.

**What could have come out otherwise.** Averaging could have produced
inconsistency often, or never. It produces it rarely per agent, and the
group-level risk rises from M = 2 to M = 3.

## What this does not say

- **That the risk falls with more sentences.** The abstract's "arbitrarily
  small" by raising M is extrapolated from two values, and Appendix B says
  the data are "insufficient to predict the shape of D-curves for higher
  values of M". For F_OP the trend from M = 2 to M = 3 runs the other way
  ([NOTE-139](../notes.d/NOTE-139.md), Corrections).
- **That the bound is proved.** It is computed for M = 2 and 3 only, after a
  single update, in an impartial culture.
- **That real groups should avoid even sizes.** The chapter's
  recommendation (§5.5) conflicts with its own finding that odd N gives the
  higher per-agent fraction; the even-favouring wobble is in F_OP. The
  Delphi recommendations are not validated.
- **Anything about truth-tracking.** Agents average attitudes, not
  evidence, and no theory is true.

## Connections

- It is a theory-valued counterpart to the continuous-opinion models in the
  record, such as [LIT-070](../literature.d/LIT-070.md), and sits beside the discursive dilemma (List
  2005, which the chapter cites), where proposition-wise aggregation of
  consistent judgements also yields inconsistency. The record's account of
  that impossibility is [THEORY-127](THEORY-127.md).
- The network-epistemology results of [THEORY-422](THEORY-422.md) concern pooling
  estimates and learning by trying; none of them asks whether the pooled
  state is logically consistent.
