---
number: 2240
status: Proposed
formerly:
- THEORY-tmpqveji
promote_when: >-
  The same association, between a rising word's topic frequency change and
  how near to it in semantic space the frequency losses that offset its
  rise fall, found again in a corpus or with a semantic model other than
  this paper's LSA, or by these authors' method under a causal design; or
  the five-corpus result confirmed by rerunning the published code on the
  same corpora. A study measuring the neighbours' range of use rather
  than frequency would test a different claim and does not meet this.
title: 'In five diachronic corpora, a sharply rising word''s frequency gain is offset by losses among its nearest distributional neighbours more often when the frequency of its topic is stable than when it is rising, a significant association in each corpus explaining up to 11% of the variance beyond lexical controls'
version: 1
tags:
- linguistics
- social-science
date: '2026-11-22'
source:
- LIT-3105
summary: >-
  Karjus, Blythe, Kirby and Smith (2020), [LIT-3105](../literature.d/LIT-3105.md), read in full in
  [NOTE-2328](../notes.d/NOTE-2328.md). The equalization range (how far out in LSA space the
  neighbours' frequency losses sum to a rising word's gain) correlates
  with topical advection (the mean log frequency change of the word's top
  context words) in COHA, DTA, Estonian, Czech and Scottish Twitter
  corpora, p < 0.05 in each. airplane took its rise from aeroplane while
  aviation's topic was stable; famed and famous rose together with
  interwar celebrity. The measure is frequency, not range of use.
---
<!-- inactive-ok-file: THEORY-159 — Proposed; the account whose test LEAD-056 looks for -->

# THEORY-2240: In five diachronic corpora, a sharply rising word's frequency gain is offset by losses among its nearest distributional neighbours more often when the frequency of its topic is stable than when it is rising, a significant association in each corpus explaining up to 11% of the variance beyond lexical controls

## Source

Andres Karjus, Richard A. Blythe, Simon Kirby and Kenny Smith (2020),
[LIT-3105](../literature.d/LIT-3105.md) (arXiv:2006.09277), read in full in [NOTE-2328](../notes.d/NOTE-2328.md).

## What was actually shown

About 270 target words per corpus whose frequency rose at least e²-fold
between two adjacent spans. For each, all other words were ordered by
normalised cosine distance in an LSA space (minus the target's topic
words), and the equalization range is the distance at which their
cumulated frequency losses match the target's gain. Advection is the
weighted mean log frequency change of the target's top 75 PPMI context
words. A linear regression of range on advection, with controls (target
frequency change, peak, onset time, word length, edit distance and cosine
distance to the nearest neighbour, the largest percentage fall among the
nearest neighbours, leftover frequency mass, and for Twitter the
user-to-frequency ratio), finds advection significant (p < 0.05) in all
five corpora, adding up to 11% of variance. The result could have come out
otherwise: rising words could have taken their frequency from near
neighbours, or from far ones, regardless of their topic. Falling words in
COHA show a smaller association of the same sign.

## What this does not say

- **Not that neighbours' meanings shift.** The response is frequency.
  Whether a neighbour that loses frequency also narrows its range of use
  is not measured, and the authors name it as uncontrolled.
- **Not causal.** "Our essentially correlational results could be improved
  with causal analysis."
- **Not that words compete to extinction.** Complete disappearance of a
  neighbour within a generation is "almost non-existent".
- **Not a test of a structuralist account.** The neighbourhood is
  distributional, collapsing synonyms, antonyms, hyponyms and associates;
  it is not a lexical field, and [THEORY-159](THEORY-159.md)'s promote_when, which asks
  for the neighbours' use and interpretation against terms outside the
  field, is not met by it.
- **Not that topic frequency is communicative need.** That identification
  is the paper's premise, resting on an earlier, unread paper.
