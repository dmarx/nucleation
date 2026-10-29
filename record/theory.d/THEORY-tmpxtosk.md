---
status: Proposed
promote_when: >-
  A rating study of naturally occurring requests in several languages, with
  annotators not screened for agreement with any model, in which the same
  bilingual judges rate items in their first and second languages under one
  instrument, reporting inter-judge agreement in each and test–retest
  agreement for each judge, and finding first-language agreement reliably
  higher across the languages. Agreement figures from model-screened
  annotators, or from different judges per language, do not settle it.
title: 'Native-speaker crowd judges agree only modestly on the graded politeness of written requests in their own language, mean pairwise Spearman about 0.46 across nine languages, and the same bilinguals agree less on English requests, about 0.36'
version: 1
tags:
- pragmatics
- psychometrics
date: '2026-10-29'
source:
- LIT-tmp2g5v4
summary: >-
  Srinivasan and Choi (2022), [LIT-tmp2g5v4](../literature.d/LIT-tmp2g5v4.md), read in [NOTE-tmpmy2mv](../notes.d/NOTE-tmpmy2mv.md) from the
  Findings of EMNLP 2022 PDF. Three Prolific annotators per item rated
  Wikipedia requests −3 to +3; mean pairwise Spearman within 20-item tasks
  was 0.46 on the 15 target-language items and 0.36 on the 5 English items
  (Table 2). The paper says own-language agreement is higher "across all
  nine languages"; Tamil (0.33 against 0.38) is the exception. The
  annotators had been screened for agreeing with an XLM-R classifier.
---

# THEORY-tmpxtosk: Native-speaker crowd judges agree only modestly on the graded politeness of written requests in their own language, mean pairwise Spearman about 0.46 across nine languages, and the same bilinguals agree less on English requests, about 0.36

## Source

Srinivasan and Choi (2022), [LIT-tmp2g5v4](../literature.d/LIT-tmp2g5v4.md), §2.1–2.3, Table 2, Table 9 and
Appendix C, pp. 5724–5726 and 5734 of the Findings of EMNLP 2022; read in
[NOTE-tmpmy2mv](../notes.d/NOTE-tmpmy2mv.md).

## What was actually shown

In each of nine languages, 7–11 bilingual crowdworkers who passed a
translation check and a qualification against a classifier rated requests
from that language's Wikipedia user talk pages, and five English requests in
each 20-item task (p. 5725). Agreement is the mean pairwise Spearman
correlation within tasks. Target-language means run from 0.33 (Tamil) to
0.60 (Korean), average 0.46 (SD 0.17); English means from 0.28 to 0.45,
average 0.36 (SD 0.31) (Table 2). Shuffled ratings give about zero (Fig. 2).
Own-language agreement is higher in eight of nine languages; Tamil is the
exception (Table 2; my count). The TyDiP annotators' English ratings
correlate 0.21–0.29 with the original English panel's raw labels (Table 9).

What could have come out otherwise: the English and target figures could
have been equal, which would have made the language of judgement
irrelevant to reliability. They differ by 0.1 on average, not in every
language.

## What this does not say

- **That politeness perception is this reliable in general.** The judges were
  kept only if their ratings did not stray far from a classifier's confident
  predictions (p. 5725). An unscreened panel could agree less.
- **That a judge is consistent with herself.** No repeated ratings.
- **That first-language agreement is higher in every language.** Tamil
  reverses it, and two more languages differ by 0.03 or less.
- **Why English agreement is lower.** English figures are over 5 items per
  task against 15, so they are noisier as well as being in a second
  language.
- **That the scores measure one construct across languages.** Each language
  had different judges and items, which the paper itself notes (p. 5727).
