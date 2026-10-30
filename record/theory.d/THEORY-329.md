---
number: 329
status: Active
formerly:
- THEORY-tmpzojtc
title: "In 32,479 Weibo posts of 2011–2016 scored with an emotion lexicon, posts tagged fake by the platform's fact-checkers carry more anger and less joy than true posts from verified accounts, and a post's share of anger words goes with more retweets after controls; whether the gap is due to falsity, and whether anger causes the spread, is not shown"
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Narrowed and promoted by the twenty-second status review, at the
    status review's ruling (the owner delegated these rulings;
    ADR-065; ADR-047 kinds 1 and 3): NOTE-852 read the paper in full,
    and the title now says what was measured: 32,479 lexicon-scored
    posts, the fake set tagged by Weibo's fact-checkers after it had
    spread and the true set from verified accounts, so that the
    fake-against-true gap may be selection's as well as falsity's, as
    the body already said. The paper's thesis, that anger makes fake
    news viral and that fake news on Weibo is angrier, moves to
    THEORY-1221, Proposed, which extends this entry and keeps the
    old condition word for word, its matched-comparison refutation
    clause included (ADR-047 kind 1). The old title: "On Weibo, fake
    news carries more anger and less joy than true news, and a post's
    share of anger words goes with more retweets after controls; that
    anger causes the spread is not shown" The old promote_when: "A
    randomized or quasi-experimental study in which the anger
    expressed in a post is varied while its claim, source and topic
    are held fixed, and sharing is measured as behaviour, on any
    platform. It promotes the account if anger raises sharing and
    lowers it for joy; it refutes the causal half if the effect
    vanishes. A second observational corpus with more controls, or
    another lexicon on the same Weibo data, cannot settle it: those
    only re-establish the association, which is already held. The
    first half (fake news carries more anger than true news) is
    refuted on Weibo if fake and true posts matched for author, topic
    and date show no anger gap."
tags:
- social-science
- emotion-and-affect
- society-and-governance
date: '2026-10-14'
source:
- LIT-379
summary: >-
  Chuai & Zhao (2020), [LIT-379](../literature.d/LIT-379.md), read in [NOTE-852](../notes.d/NOTE-852.md). In 32,479 Weibo
  posts from 2011–2016, lexicon-scored anger share is higher and joy
  share lower in fake than in true news, and in highly than in lowly
  retweeted news, under three scoring methods. With content, author and
  topic controls, anger share predicts more retweets within 48 hours and
  joy share fewer (R² 0.08–0.13). The paper calls this causal; the design
  is observational, and the fake set is selected for having spread.
  Active as a report of the association (ADR-065); the paper's causal
  thesis is THEORY-1221, Proposed.
---
<!-- inactive-ok-file: LIT-083 THEORY-055 THEORY-057 — Proposed; named in Connections to mark what this account is not about, not leaned on -->

<!-- inactive-ok-file: THEORY-1221 — Proposed; the paper's thesis split from this entry, cited as open -->

# THEORY-329: In 32,479 Weibo posts of 2011–2016 scored with an emotion lexicon, posts tagged fake by the platform's fact-checkers carry more anger and less joy than true posts from verified accounts, and a post's share of anger words goes with more retweets after controls; whether the gap is due to falsity, and whether anger causes the spread, is not shown

## Source

Chuai & Zhao (2020), [LIT-379](../literature.d/LIT-379.md) (arXiv 2004.10399v3), read in
[NOTE-852](../notes.d/NOTE-852.md): Fig. 1 and Tables S2–S14 (distributions), Table 1 and
Table S17 (regressions), S10 and Table S18 (English data), S13 and Table
S26 (survey), S14 and Table S27 (the 20% threshold).

## What was actually shown

**The anger and joy gaps.** On 22,479 fake posts (tagged by Weibo's
fact-checking committee) and 10,000 true posts (from verified accounts),
scored with a hand-labelled lexicon of 6,155 terms, mean anger share is
0.165 in fake and 0.112 in true news, and joy 0.443 against 0.609 (Table
S4). The gaps are larger between highly retweeted fake posts by authors
with few followers (LHF) and lowly retweeted true posts by authors with
many (HLT): anger 0.267 against 0.111, joy 0.329 against 0.611 (Table S2).
Highly retweeted (≥ 10 retweets) posts carry more anger than lowly
retweeted ones regardless of label (Table S5). Two classifiers and a rank
measure over six more give the same direction for anger and joy (S7);
disgust, sadness and fear do not behave consistently.

**The association with retweets.** In linear models of retweets within 48
hours, with follower, friend, mention, hashtag, location, date, URL,
length, one emergency event and seven topics as controls, anger share has
coefficient 23.96 and joy share −29.56 among fake posts (Table 1 (3),
N = 20,323, R² = 0.084), and 22.28 and −35.98 among all posts (Table 1
(4), R² = 0.134). The emotion shares sum to 1, so these are relative to
the omitted disgust, sadness and fear. Moving 0.1 of a post's emotional
vocabulary from joy to anger goes with about 5.4 more retweets among fake
posts and 5.8 among all posts; the paper reports 5.8 for fake news, which
is the all-news figure.

**What could have come out the other way.** The gaps could have vanished
under other scoring methods (they did for the other three emotions), and
the anger coefficient could have lost sign or significance once author
reach and topic were controlled. Neither happened. On unlabelled English
tweets anger also predicts reaching 10 retweets (logit 0.215, s.e. 0.062,
Table S18).

## What this does not say

- **That anger causes fake news to spread.** The paper says it does,
  "causally", throughout. The evidence is regression on observational
  data with no experiment, instrument or natural experiment, and the
  models leave nearly 90% of the variance unexplained. Content that
  carries anger words may carry other features (alarm, a call to repost,
  a rumour type) that do the work.
- **That fake news is angrier because it is false.** Fake posts were
  labelled because they had spread widely, and true posts come from
  verified authors, so the fake-against-true comparison mixes falsity
  with selection on spread and on source.
- **That the mechanism is platform-independent.** The English evidence
  has no fake/true labels in the main test, a gap of 0.123 against 0.110
  in a second set, and 478 tweets in a third.
- **That anger works through anxiety management.** The survey result
  rests on two anger-dominated posts, with unadjusted K-S tests at
  p ≈ 0.02–0.04, and measures stated motives, not reposting.
- **That flagging angry posts would work.** The 20% threshold is chosen
  in-sample, and its effect (46% of popular fake news caught, 22% of
  popular true news) assumes that no flagged post is ever retweeted.

## Connections

- The emotion accounts in the record ([THEORY-055](THEORY-055.md), [THEORY-057](THEORY-057.md)) concern
  what emotions are; this one concerns a word-level proxy for emotion in
  text, and depends on none of them.
- [THEORY-123](THEORY-123.md) holds that displayed mood spreads within small groups, shown
  experimentally. This account is about content features predicting
  sharing at scale, not about one person's emotion passing to another.
- [LIT-083](../literature.d/LIT-083.md) covers the response side of disinformation, this the spread.

## Note of 2026-10-30: narrowed and promoted

Promoted as a report of what the corpus measured ([ADR-065](../decisions.d/ADR-065.md)). The paper's
thesis, that anger makes fake news viral, is [THEORY-1221](THEORY-1221.md), Proposed,
which extends this entry and keeps its old condition.
