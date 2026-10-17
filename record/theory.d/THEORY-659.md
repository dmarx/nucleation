---
number: 659
status: Active
formerly:
- THEORY-tmpwx87w
title: "In the EEAS's 2024 sample of 505 foreign information manipulation incidents, the overt state voice is a small core: of the 2,055 channels that recur across incidents, 20% are attributed to Russia, 3.5% to China and 76.5% are not attributed, after some 28,000 disposable inauthentic accounts are set aside; the sample is not representative, and the four-tier Exposure Matrix used to grade channels' ties to a state is unvalidated"
version: 1
tags:
- society-and-governance
- network-science
date: '2026-10-16'
source:
- LIT-084
summary: >-
  European External Action Service (2025), [LIT-084](../literature.d/LIT-084.md), the 3rd EEAS report on
  FIMI threats, read in [NOTE-060](../notes.d/NOTE-060.md). A description of what the EEAS monitored,
  which the report itself says is not a basis for general trends. The
  76.5% is a share of a filtered co-involvement graph, not of the 38,000
  channels, though the report's conclusions restate it as such. The
  Exposure Matrix grades attribution in four tiers by evidence and
  treats it as revisable; no inter-rater test or worked classification
  is given, and the strongest evidence is proprietary or classified.
---
<!-- inactive-ok-file: LIT-083 — Proposed; the DISINFOX preprint, named for its schema beside the Exposure Matrix, not leaned on -->

# THEORY-659: In the EEAS's 2024 sample of 505 foreign information manipulation incidents, the overt state voice is a small core: of the 2,055 channels that recur across incidents, 20% are attributed to Russia, 3.5% to China and 76.5% are not attributed, after some 28,000 disposable inauthentic accounts are set aside; the sample is not representative, and the four-tier Exposure Matrix used to grade channels' ties to a state is unvalidated

## Source

European External Action Service (2025), [LIT-084](../literature.d/LIT-084.md), *3rd EEAS Report on
Foreign Information Manipulation and Interference Threats: Exposing the
architecture of FIMI operations* (March 2025), read in [NOTE-060](../notes.d/NOTE-060.md). Page
numbers are the printed ones.

## What was actually shown

**The sample (pp. 6, 9–11).** 505 incidents detected and analysed by EEAS
strategic monitoring in 2024: about 38,000 unique channels on 25
platforms, more than 68,000 observables, 90 countries and 322
organisations targeted. Disposable bot and coordinated-inauthentic
accounts were 28,000 of the 38,000 channels (73%). The report says the
incidents reflect "known outlets related to overt FIMI or independently
attributed operations by selected actors and on priority issues", do not
cover all regions or languages, and "should not be used to draw
conclusions about general trends".

**The graph (p. 20).** Nodes are channels; an edge is shared involvement in
an incident. Only channels in more than one incident with at least two
connections are kept: 2,055 nodes and 8,056 edges. By attribution: Russia
20%, China 3.5%, non-attributed 76.5%.

**The Exposure Matrix (pp. 14–19).** Four categories by the strength and
kind of evidence tying a channel to a state: official state channels;
state-controlled outlets (RT, Sputnik, CGTN and mirrors sharing their
infrastructure); state-linked channels, covert but attributed on
high-confidence, mostly proprietary or classified indicators; and
state-aligned channels, not attributed but showing "strong, repetitive
patterns of alignment" on medium-confidence, mostly open indicators.
Narrative alignment alone is not enough, over-attribution is to be
avoided (p. 14), and classification is "not static". The final public
attribution is "often political" (p. 19).

**What could have come out otherwise.** Attributed channels could have
been the bulk of the recurring infrastructure. In this sample they were
not.

## What this does not say

- **That three-quarters of FIMI channels are unattributed.** The 76.5% is
  a share of the filtered graph, excluding the 28,000 inauthentic accounts
  and every single-incident channel. The conclusions (p. 38) restate it as
  "a sizeable majority (76.5%) of the channels investigated", which the
  body does not support ([NOTE-060](../notes.d/NOTE-060.md), corrections).
- **Anything about prevalence or trend.** Every count is a count of what
  the EEAS chose to monitor.
- **That the Matrix sorts channels reliably.** No inter-rater test and no
  worked example of weighing indicators for a channel. Category 3 rests
  partly on evidence not shown (C1, moderate as a proposal).
- **That China's network is centralised and Russia's decentralised.**
  Read off the picture, with no metric (C6, weak–moderate).
- **Anything about impact.** The report says "true reach and impact"
  remain unclear (p. 11). About 41 incidents involved AI, and AI's use
  "does not necessarily translate into a greater impact".
- **That its figures reconcile.** The per-platform channel counts add to
  about 63,000, against 38,000; X's 88% has no stated base; the foreword
  and body differ on countries and organisations targeted.

## Connections

- **[QUESTION-070](../questions.d/QUESTION-070.md)** asks whether an organized whole manipulates when no
  member intends to, and names this report's tiered network as one of its
  two cases. This account says what the network looks like in the EEAS's
  sample: most of its recurring channels are graded only as state-aligned.
  It does not answer the question, which turns on what manipulation is.
- **[THEORY-651](THEORY-651.md)** (DISINFOX, [LIT-083](../literature.d/LIT-083.md)) carries incidents in STIX with
  attribution as one ungraded edge; the Matrix is the graded layer that
  schema lacks.
- **[THEORY-488](THEORY-488.md)** and **[THEORY-551](THEORY-551.md)** give the Russian side.
  The report names "information confrontation" as central to Russian
  doctrine (p. 12) without citing a Russian text; Fridman ([LIT-088](../literature.d/LIT-088.md))
  cites Russian work on it. The foreword's FIMI used "to lay the way for
  kinetic action" (p. 2) parallels Clark's subordination of kinetic action
  to information.
