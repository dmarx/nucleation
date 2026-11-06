---
number: 1517
status: Active
formerly:
- THEORY-tmpymvl9
title: 'Knack finds, across 80 aid-receiving countries from 1982 to 1995, that higher mean aid relative to GNP or to government spending goes with smaller gains in the ICRG governance index, controlling for initial governance, income growth and population growth; the effect roughly doubles when aid is instrumented with recipient need and donor interest, holds within sub-Saharan Africa for aid relative to GNP, is several times larger for technical assistance, does not depend on initial governance, and shrinks as aid becomes less predictable'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the status review's ruling (the owner delegated these
    rulings), under ADR-065 and ADR-047's one-study rule: the title
    reports what one study read in NOTE-1707 found, with its hedges
    kept, and nothing in the record contradicts it. The standard error
    printed as 0.037 and 0.045 for one estimate leaves it significant
    under either, so no clause of the title turns on it. The replication
    and refutation clauses move word for word to QUESTION-424. The
    old condition: A replication, with these instruments or
    better-justified ones and with first stages reported, on the
    published 2001 data or an extended ICRG panel, again finds a
    negative, significant coefficient of mean aid on the change in
    governance, a larger coefficient for technical assistance than for
    aid overall, a null interaction of aid with initial governance, and
    a positive interaction of aid with its variability. A replication in
    which the aid coefficient becomes insignificant once country panels
    with fixed effects are used would refute it as a causal reading.
    Evidence on tax effort or on what follows the withdrawal of aid does
    not bear on it.
tags:
- society-and-governance
- social-science
date: '2026-11-05'
source:
- LIT-2219
bears_on:
- QUESTION-424
summary: >-
  Knack (2000), [LIT-2219](../literature.d/LIT-2219.md), read in [NOTE-1707](../notes.d/NOTE-1707.md) in its World Bank
  working-paper version; the 2001 journal version was not read. Held as what the study finds, with its hedges:
  one change score per country, instruments whose exclusion is defended
  only by overidentification tests, no first stage reported, and a
  standard error printed differently in two tables. It measures governance,
  not tax effort or revenue, and has no withdrawal episodes. It stands in
  only in part for Bräutigam & Knack (2004), [LIT-2221](../literature.d/LIT-2221.md).
---
<!-- inactive-ok-file: LIT-2221 — Unavailable; the article this reading partly stands in for -->

# THEORY-1517: Knack finds, across 80 aid-receiving countries from 1982 to 1995, that higher mean aid relative to GNP or to government spending goes with smaller gains in the ICRG governance index, controlling for initial governance, income growth and population growth; the effect roughly doubles when aid is instrumented with recipient need and donor interest, holds within sub-Saharan Africa for aid relative to GNP, is several times larger for technical assistance, does not depend on initial governance, and shrinks as aid becomes less predictable

## Source

Knack (2000), World Bank Policy Research Working Paper 2396, [LIT-2219](../literature.d/LIT-2219.md); read in [NOTE-1707](../notes.d/NOTE-1707.md).

## What was actually shown

- **Design** (p. 10): the 1995 ICRG index (corruption, bureaucratic
  quality, rule of law; 0–18) minus its 1982 or 1984 value, regressed on
  mean aid over 1982–95, with initial ICRG, population change and income
  growth controlled; 80 countries for aid/GNP, 68 for aid/government
  spending.
- **OLS** (Table 2): aid/GNP −0.067 (0.021), aid/government −0.027
  (0.010); robust, median and ordered-logit estimates agree (p. 13).
- **2SLS** (Table 2): −0.154 (0.037) and −0.054 (0.014), with infant
  mortality, initial income, initial population and Franc-zone and
  Central-America dummies as instruments; overidentification p = .52 and
  .81; no first stage reported. The same Basic 2SLS coefficient is printed
  with s.e. 0.045 in Table 4.
- **Africa only** (Table 4, row 8): aid/GNP −0.074 (0.030) OLS, −0.126
  (0.057) 2SLS on 31 countries; aid/government spending not significant on
  24.
- **Technical assistance** (Table 4, row 9): −0.346 (0.089) OLS, −0.699
  (0.159) 2SLS; with the rest of aid entered beside it, "only the former is
  significant" (n. 18), the two correlated at .87.
- **Initial conditions** (Table 5, eqs. 3–4): interactions −0.002 (0.008)
  and 0.003 (0.003); "Results provide no support for the hypothesis that
  initial conditions matter".
- **Variability** (Table 5, eqs. 1–2): coefficient of variation +2.569
  (0.593), interaction +0.145 (0.070); "the negative effects of aid levels
  disappear when the CV is about .78". Trends in aid do not matter.

Each of these could have come out the other way: the aid coefficient
could have vanished under instruments or in Africa, and the initial-
conditions interaction could have been negative.

## What this does not say

- That governance declined with aid: it improved on average, and aid goes
  with less improvement.
- That aid lowers tax effort or revenue: no tax or revenue variable is in
  the paper, and the fiscal-contract mechanism is argued, not tested.
- Anything about what happens when aid stops or tapers: there are no
  withdrawal episodes; the cited cases (the Dominican Republic; Korea and
  Taiwan) point both ways.
- That the effect is causal beyond the instruments' exclusion, which is
  untested.
- That aid relative to government spending harms governance within
  Africa: that coefficient is not significant there.
- That the 2001 journal version reports the same estimates.
- Anything about Bräutigam & Knack's (2004) own Africa estimates.
