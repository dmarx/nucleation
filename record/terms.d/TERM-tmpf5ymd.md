---
status: Proposed
title: "bulk, in two senses that come apart: by count, the many members or directions that make up most of a population or spectrum, and by weight, the few that carry most of its mass, density or activity; in a skewed distribution or spectrum the two sit at opposite ends"
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    After the readings of LIT-2983 (NOTE-tmpdac0o) and LIT-2990
    (NOTE-tmpzethm): Dandi and colleagues' learned-feature spectrum added as
    a worked case in which the two senses split, and in which the bulk by
    count is itself what learning changes. Definition unchanged.
tags:
- probabilistic-modeling
- representation-learning
date: '2026-11-22'
line:
- formal-apparatus
- learned-structure
summary: >-
  At the owner's correction of 2026-11-22, on a relay of Song, Ahn and Yun
  that used "bulk" for the many low-curvature directions: 'you have my intended meaning of 'bulk' backwards, I meant that in the sense of the domain which carries the dominant density. in the context of e.g. the 80-20 rule, the *bulk* of the population does not contribute the *bulk* of the activity. Spectrally, the top eigenvalues definitionally are associated with the dominating 'bulk' of the operator's activity.'
  The record and its sources use the word in both senses. By count, the
  bulk is the many: Song et al.'s "bulk subspace", the complement of the
  top Hessian eigenvectors, and random-matrix theory's continuous bulk of a
  spectrum, from which outliers detach ([TERM-138](TERM-138.md), sense 3). By weight, the
  bulk is the few that carry most of the mass or activity: the owner's
  sense, the top eigenvalues of an operator. In a skewed population or
  spectrum the two sit at opposite ends, as the 80-20 rule says and as
  [CLAIM-832](../claims.d/CLAIM-832.md) holds for heavy tails (most events small by count, most of the
  total in the tail). The term's job is to make an entry say which it
  means. The distinction is the owner's; The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmpcij35 THEORY-tmpthmd7 THEORY-tmphbp5a CLAIM-799 — Proposed or new; the readings of 2026-11-22 that use the term, and the claim they qualify -->
<!-- inactive-ok-file: TERM-138 CLAIM-832 — Proposed or new; the senses this term separates and the claim that uses it -->

# TERM-tmpf5ymd: bulk, in two senses that come apart: by count, the many members or directions that make up most of a population or spectrum, and by weight, the few that carry most of its mass, density or activity; in a skewed distribution or spectrum the two sit at opposite ends

## Definition

- **Bulk by count.** The many members of a population, or the many directions of a spectrum, that make up most of it by number.
  - Song, Ahn and Yun's "bulk subspace": everything outside the top-k Hessian eigenvectors ([THEORY-tmpthmd7](../theory.d/THEORY-tmpthmd7.md)).
  - Random-matrix theory's bulk: the continuous part of a spectral density, from which an outlier separates ([TERM-138](TERM-138.md), sense 3).
- **Bulk by weight.** The few that carry most of the mass, density or activity. Spectrally, the top eigenvalues, which carry most of the operator's activity: the owner's sense.

## How they come apart

In any skewed population the two sit at opposite ends.
- **Heavy tails.** Most events are small by count, and most of the total lies in the rare large ones ([CLAIM-832](../claims.d/CLAIM-832.md)).
- **The 80-20 rule.** In the owner's words, "the *bulk* of the population does not contribute the *bulk* of the activity".
- **Spectra.** In a spectrum with a few large eigenvalues, the bulk by count is the many small directions and the bulk by weight is the few large ones.

- **A worked case: learned features after one large step** (added 2026-11-22, version 2). In Dandi and colleagues' feature covariance (THEORY-tmpcij35), the few outliers of order d, which come from the features' means and carry the largest eigenvalues, are the bulk by weight; the continuous part, which the paper calls "the 'bulk' of the feature covariance", is the bulk by count. And the bulk by count is itself what learning changes: it "is modified from the unspiked RF spectrum ..., displaying in particular a wider support and longer tails". So here the bulk by count is not unlearned noise.

## Use

An entry that says "bulk" says which sense it means. Song et al.'s finding, read in these terms, is that training progress runs through the bulk by count, the low-curvature majority, and not through the bulk by weight, the dominant directions. The relay that prompted this term had it the other way round, as its devlog note records.

The distinction is the owner's; The wording is the assistant's (Claude, in this session); adopting it is the owner's call.

## Note of 2026-11-22: Dandi and colleagues, and Park and colleagues, read

- **Dandi and colleagues** (LIT-2983, NOTE-tmpdac0o): a worked case where
  the senses split, added above. The paper uses "bulk" by count throughout
  ("a random bulk", Fig. 1's "Bulk spectrum"), in TERM-138's sense 3, and
  its finding that learning reshapes that bulk qualifies CLAIM-799.
- **Park and colleagues** (LIT-2990, NOTE-tmpzethm): an instance of the
  bulk by count, the "random spectral bulk" from which "isolated
  eigenvalues detach", with the informative content in one outlier. No new
  sense.
