---
status: Proposed
title: 'A Contextuality-by-Default test of pragmatic judgements: two-pronoun Winograd and two-turn indirect-request items with named characters, two free binary answers from each respondent in one of four contexts, every counterbalancing cell analysed apart, and the statistic, sign pattern, coding and verdicts fixed before the data'
version: 1
standing: stipulated
kind: proposed-study
tags:
- contextuality
- pragmatics
- psychometrics
date: '2026-11-22'
line: pragmatic-transport
draws_on:
- THEORY-tmpdcw35
- THEORY-177
- THEORY-168
- THEORY-722
- THEORY-623
bears_on:
- QUESTION-001
summary: >-
  Drafted for LEAD-182 on 2026-11-22, after a literature check found no
  powered CbD test on human pragmatic judgements (scratch/studies/lead-182/search.md).
  It revises Lo, Sadrzadeh and Mansfield's generalised Winograd design
  (THEORY-tmpdcw35): free per-question answers, so signalling is observed
  and discounted rather than designed away; named characters; a second
  family of indirect-request items; each counterbalancing cell its own
  system (CLAIM-tmpu482h); a fixed sign pattern from a pilot; detection by
  the plug-in statistic and absence by a conservative bound
  (CLAIM-tmpalxab). The simulation (CASE-tmpjp6vg) puts the cost at 1,600
  to over 4,000 valid respondents a context an item, set by the pilot's
  signalling. Every number is a lean; fixing them is the owner's. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: LEAD-182 — Open; the lead this design would carry out -->
<!-- inactive-ok-file: THEORY-tmpdcw35 CLAIM-tmpu482h CLAIM-tmpalxab CASE-tmpjp6vg — new; the reading, findings and simulation this design rests on -->
<!-- inactive-ok-file: CLAIM-009 CLAIM-105 — Proposed; the claims this study would test, open -->

# CASE-tmpl2va4: A Contextuality-by-Default test of pragmatic judgements: two-pronoun Winograd and two-turn indirect-request items with named characters, two free binary answers from each respondent in one of four contexts, every counterbalancing cell analysed apart, and the statistic, sign pattern, coding and verdicts fixed before the data

## What it would test

LEAD-182 asks for "an adequately powered Contextuality-by-Default test on
human pragmatic judgements, with signalling accounted for and outcome
coding fixed in advance". CASE-053's four conditions are its brief: (a)
elicited judgements; (b) contextuality after a CbD correction; (c) enough
observations a context; (d) pragmatic content. A robust positive would
support CLAIM-009 and meet CLAIM-325's defeat condition; a robust absence
on items able to show contextuality would count the other way (LEAD-182,
"What would count"). Nothing has been run. The materials are stipulated
(ADR-042).

## Materials

Each item is a rank-4 cyclic system: two binary questions, Q1 and Q2,
each asked under one of two versions of a word, so four contents
(Q1 under w1 or w1′, Q2 under w2 or w2′) and four contexts, the pairings
(w1, w2), (w1, w2′), (w1′, w2), (w1′, w2′). Two families, four items each,
eight in all (the lean).

- **Family A, two-pronoun Winograd** (Lo et al., THEORY-tmpdcw35), with
  named characters of the same gender in place of A and B, so the items
  read as English and their asymmetries are free to show. Stipulated
  example: "Maria lent Ana her notes because she was [ill / organised].
  The next week one of them was [grateful / annoyed]." Q1: who was ill
  (or organised)? Q2: who was grateful (or annoyed)?
- **Family B, two-turn indirect requests.** A remark and a reply, the
  first word deciding whether the remark reads as a request, the second
  how the reply takes it. Stipulated example: X: "It's [freezing /
  stuffy] in here, isn't it?" Y: "[I'll grab you a jumper / Funny, I was
  just thinking it's fine]." Q1: was X asking Y to do something? Q2: did
  Y take it as a request? This is pragmatic in the narrow sense, an act
  and its uptake, which Family A is only in the broad one.

Both families need items that readers find ambiguous: deterministic
judgements cannot be contextual (Lo et al., §4.2).

## Procedure

- **Pilot**, on a sample not used again: 100 valid respondents a context
  an item. It keeps an item only if every content's marginal lies
  between 0.2 and 0.8 and some odd sign pattern gives σ·Ê above 1.6. It
  fixes each kept item's sign pattern σ, the pattern that maximises
  σ·Ê in the pilot. Its estimate of each item's signalling sets that
  item's sample size (below).
- **Main study**, between subjects within an item: each respondent sees
  each item once, in one context drawn at random, and answers Q1 then Q2,
  each a free forced choice between two options. No "pick two of four".
  Items appear in random order.
- **One presentation an item.** Which character is named first, and the
  order of the questions, are fixed for each item and identical across
  its four contexts. Counterbalancing is done across items, not within
  one. If it must be done within an item, each cell is analysed as a
  system of its own, and the pooled result is reported only beside them,
  because pooling can create contextuality that no cell has
  (CLAIM-tmpu482h).

## Outcome coding, fixed in advance

- Each answer is coded +1 for the option listed first in the item file,
  which is frozen with σ before the main study.
- Answers are binary by construction, so no dichotomization is chosen
  after the data (THEORY-168, THEORY-722).
- Exclusions, fixed: failing an attention item, or finishing faster
  than a time fixed from the pilot. Never by the pattern of answers.
  The exclusion rate by context is reported, and an item whose rates
  differ by context beyond a fixed tolerance is flagged.

## Analysis, fixed in advance

- **Statistic**: for each item, Δ_C = σ·Ê − 2 − Δ̂, with σ from the
  pilot and Δ̂ the plug-in signalling, Σ over contents of |d̂_q|
  (THEORY-177). The criterion is the cyclic-system one, for which CbD 1.0
  and 2.0 agree (THEORY-722).
- **Detection**: contextual if the 5% percentile-bootstrap lower bound
  of Δ_C is above 0, at 0.05/8 for the family. Resampling is by
  respondent, and when respondents answer several items, by respondent
  across items (a cluster bootstrap). The plug-in Δ̂ is biased upward,
  so this errs toward missing contextuality, never toward finding it
  (CLAIM-tmpalxab).
- **Absence**: noncontextual only if the conservative bound
  (cbd.absence_upper_bound: an upper bound on σ·E at α/2, less a lower
  bound on each content's signalling at α/8) is below 0. The plug-in
  upper bound must not be used: it declares absence for contextual
  systems (CASE-tmpjp6vg).
- **Otherwise inconclusive.** Both rules are reported for every item,
  with Ê, each d̂_q and their intervals.
- **Replication**: an item found contextual is rerun on a fresh sample of
  the same size, with σ and coding unchanged. A robust positive is two
  detections.
- **Robustness, reported not decisive**: the same analysis within strata
  fixed in advance (first language, age band), since a population is
  itself a pool of respondents whose direct influences may differ
  (below).

## Sample size

From CASE-tmpjp6vg. At a true violation of 0.19 (Lo et al.'s size), the
plug-in test at 0.05 has power about 0.80 at 1,600 valid respondents a
context when the item's signalling is 0.3 or more, 0.83 at 2,500 when it
is 0.1, and 0.65 at 4,000 when it is near 0. At 0.05/8, with signalling
0.3, power is 0.76 at 2,500 and 0.95 at 4,000. The lean: n a context set per item from the pilot's
signalling, 2,500 where the pilot's Δ̂ is at least 0.2, 4,000 where it
is lower, and an item dropped rather than run if 4,000 is beyond the
budget. Eight items at 2,500 are 80,000 item responses; if every
respondent answers all eight, 10,000 respondents before exclusions. A
pilot with less signalling than this costs more.

## The main threat to inference

**Pooling.** A between-subjects system is the population's, not a
person's. If respondents differ in which way the second word pushes the
first answer, the population's signalling cancels while their
correlations add, and the population can be contextual when no
respondent is (CLAIM-tmpu482h's mechanism, applied to people instead of
cells). The design can rule out the pooling it controls, its cells, and
check the strata it fixes in advance; it cannot rule out pooling over
differences it does not measure. So a positive result shows that the
population's judgement system is contextual under CbD, which is what
CLAIM-009 says of "context-relative distributions", and not that any
individual's interpreting is. The second threat is content: a positive
in Family A only is coreference by world knowledge, as Lo et al.'s was;
only Family B bears on acts and uptake.

## What each outcome would show

- **Robust positive in Family B**: the first documented contextual
  pragmatic data set; CLAIM-325's defeat condition met; CLAIM-009
  supported for the population; the fixed-scenario form of CLAIM-105's
  headline, which needs a contextual model on one side (CLAIM-219),
  given a case that is not constructed.
- **Robust positive in Family A only**: contextuality in coreference
  judgements; CLAIM-325 met as to "meaning judgements", not pragmatic
  ones.
- **Absence shown on most kept items**: evidence of absence where until
  now there was absence of evidence (CASE-053), for these items.
  Because the absence bound works only where signalling is small, this
  verdict is reachable mainly for near-symmetric items.
- **Inconclusive on most items**: the expected outcome if true effects
  are under 0.1, and itself informative: a family in which the test that
  LEAD-182 asks for cannot be powered at this budget.

## What the owner decides

Every number above is a lean: the number of items, the pilot's
thresholds, α and the correction, the n rule, the replication rule, the
strata, and whether Family A is run at all. So is the choice of panel and
language. The draft fixes none of them.
