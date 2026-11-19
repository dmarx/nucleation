---
status: Proposed
title: 'Marx (2017) maps Reddit''s subreddits by shared active users with each directed edge weighted by the share of the target subreddit''s active users also active in the source, so that a small community nested in a large one appears as an edge into it, read as a specialization forked from the larger community; the monthly graphs are flattened by their maximum weight, which keeps relationships and discards the order in which they formed'
version: 1
source:
- LIT-tmpuv25r
tags:
- social-science
- network-science
date: '2026-11-19'
promote_when: >-
  The weighting and its reading are confirmed by a second reader of the
  post, or by recomputing a few edges from the public comment data with
  the stated thresholds.
summary: >-
  From the reading of [LIT-tmpuv25r](../literature.d/LIT-tmpuv25r.md) in [NOTE-tmpbivmm](../notes.d/NOTE-tmpbivmm.md). The owner's own
  method, named at U37 as a place to see communities forming
  subcommunities. Proposed until its promote_when is met.
---

# THEORY-tmp5zxkk: Marx (2017) maps Reddit's subreddits by shared active users with each directed edge weighted by the share of the target subreddit's active users also active in the source, so that a small community nested in a large one appears as an edge into it, read as a specialization forked from the larger community; the monthly graphs are flattened by their maximum weight, which keeps relationships and discards the order in which they formed

## The account

Project the user–subreddit network onto subreddits, counting users
active in both in a month, and divide by the active users of the target.
Each edge then estimates the probability that a random active member of
the target is active in the source, so a 2,000-member subreddit inside a
million-member one gets a strong edge into it and a weak edge out. The
post reads such an edge as a specialization forked from the larger
community. Monthly graphs are combined by taking each edge's maximum, and
edges below a ratio of 0.1 dropped.

## Evidence

A method and a map, not a test: the specialization reading is the
author's interpretation of the edge direction, and the flattening means
the map cannot show which community came first.

## Note of 2026-11-19: Hessel, Tan and Lee, read
<!-- inactive-ok-file: THEORY-tmpj5upc THEORY-tmps2gur — Proposed; cited from the readings of 2026-11-19 -->

Hessel, Tan and Lee ([THEORY-tmps2gur](THEORY-tmps2gur.md); [NOTE-tmpwmsxg](../notes.d/NOTE-tmpwmsxg.md)), on the same platform, qualify the reading of a nested edge as a specialization forked from the larger community: in 14% of name-linked pairs the specific community is the older ("ukpolitics" before "politics"), and about half of related pairs share few early participants. Overlap or nesting is not descent, which this account's flattening of the months already leaves undetermined. Krohn and Weninger ([THEORY-tmpj5upc](THEORY-tmpj5upc.md)) build a different graph, from explicit links, monthly; it grows sparser and more tree-like over time, a different measure, not a confirmation.
