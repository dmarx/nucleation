---
number: 325
status: Active
formerly:
- CLAIM-tmpxrlyo
title: 'Behavioural data read show no contextuality'
statement: >-
  The behavioural data the record has read show no contextuality proper:
  none of the five kinds of data Dzhafarov, Zhang and Kujala re-analyse is
  contextual, Wang et al. test none of their 90 language systems for it, and
  no documented test of pragmatic or meaning judgements finds it at adequate
  power
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    A dated note records LEAD-182's search of 2026-11-22 (nothing meets the
    defeat condition) and what "at adequate power, with its signalling
    accounted for" costs (CASE-328). The claim is unchanged.
role: thesis
warrant: empirical
defeated_if: >-
  A documented data set of pragmatic or meaning judgements that is
  contextual in the Contextuality-by-Default sense at adequate power, with its
  signalling accounted for and its outcome coding fixed in advance. A
  contextual result on content that is not pragmatic, such as instructed
  attribute matching, does not meet this condition.
tags:
- contextuality
- cognition
date: '2026-10-15'
line: pragmatic-transport
grounds:
- LIT-264
- LIT-851
- CASE-053
summary: >-
  Split from [CLAIM-219](CLAIM-219.md) under [ADR-043](../decisions.d/ADR-043.md): the empirical premise of that
  objection's dilemma, which [CLAIM-201](CLAIM-201.md) conceded. Dzhafarov, Zhang and
  Kujala ([LIT-264](../literature.d/LIT-264.md), read in [NOTE-235](../notes.d/NOTE-235.md)) find none of five kinds of behavioural
  data contextual, two of them previously published as contextual; Wang,
  Sadrzadeh, Abramsky and Cervantes ([LIT-851](../literature.d/LIT-851.md)) report signalling in 69 of 90
  language systems and test none for contextuality; [CASE-053](../cases.d/CASE-053.md) collects the
  documented tests on elicited judgements and finds no contextual pragmatic
  data. It is scoped: [CASE-053](../cases.d/CASE-053.md) records a reliable positive result on
  instructed matching, so "none in behavioural data" is too broad, and the
  absence is [LIT-264](../literature.d/LIT-264.md)'s working hypothesis, not a proof that such data
  cannot exist.
---
<!-- inactive-ok-file: CASE-328 CASE-329 LIT-3100 THEORY-2226 CLAIM-896 CLAIM-895 — new; filed by LEAD-182 on 2026-11-22 -->
<!-- inactive-ok-file: CLAIM-105 CLAIM-201 — Proposed; the headline and its narrowing this premise bears on, open -->

# CLAIM-325: Behavioural data read show no contextuality

## The claim

This is the observation [CLAIM-219](CLAIM-219.md)'s dilemma starts from, stated on its own
so that its warrant can be.

Dzhafarov, Zhang and Kujala ([LIT-264](../literature.d/LIT-264.md), read in [NOTE-235](../notes.d/NOTE-235.md)) apply the
Contextuality-by-Default criterion to five kinds of behavioural data, two
of them previously published as contextual. "None is contextual." [NOTE-235](../notes.d/NOTE-235.md)
separates a response distribution that depends on context, inconsistent
connectedness, "a trivial sense of contextuality", from contextuality
proper: "Behavioural data have plenty of the first and, so far, none of the
second."

[CLAIM-125](CLAIM-125.md), from Wang, Sadrzadeh, Abramsky and Cervantes ([LIT-851](../literature.d/LIT-851.md)): "69 of
the 90 systems signal" and "34 signal enough that they cannot be contextual
at all". The paper tests none of the 90 for contextuality ([LIT-851](../literature.d/LIT-851.md)'s status
note).

[CASE-053](../cases.d/CASE-053.md) collects the documented tests of contextuality proper on elicited
human judgements. No study of pragmatic or meaning judgements finds it at an
adequate sample size: [LIT-264](../literature.d/LIT-264.md) and Wang's thesis (2024) find none, and Lo,
Sadrzadeh and Mansfield's Winograd schemas, the one test with pragmatic
content, find a violation of about one standard deviation, with
no-signalling forced by the response format.

## What it does not say

- That a contextual pragmatic data set cannot exist. [LIT-264](../literature.d/LIT-264.md) offers the
  absence of contextuality as a working hypothesis, and [CASE-053](../cases.d/CASE-053.md) documents
  that the adequate test has not been run.
- That no behavioural data anywhere are contextual. [CASE-053](../cases.d/CASE-053.md) records
  Cervantes and Dzhafarov's "Snow Queen" as contextual with high
  reliability; its content is instructed attribute matching, not
  pragmatics, and the result is disputed.
- Anything about [CLAIM-105](CLAIM-105.md)'s headline. What follows for it is [CLAIM-219](CLAIM-219.md)'s
  dilemma and [CLAIM-201](CLAIM-201.md)'s narrowing, which rest on this claim.
- That a contextual result would settle the matter by itself. How much
  contextuality a data set shows depends on how its outcomes are coded
  ([CLAIM-245](CLAIM-245.md)), so the coding has to be fixed in advance.

## Note of 2026-11-22: the search updated, and what adequate power takes

[LEAD-182](../leads.d/LEAD-182.md) searched Europe PMC and arXiv for tests since [CASE-053](../cases.d/CASE-053.md) and found
none on pragmatic or meaning judgements. The one new CbD test on
elicited judgements, Bruza, Lee and Hoyte (2025, [LIT-3100](../literature.d/LIT-3100.md)), is on
face perception, unread, and would not meet this claim's condition,
which excludes content that is not pragmatic. The reading of Lo,
Sadrzadeh and Mansfield ([THEORY-2226](../theory.d/THEORY-2226.md)) is evidence for the claim as
it stands: their violation is about one standard deviation, and their
format never elicits the marginals a CbD correction discounts.

The defeat condition's "adequate power, with its signalling accounted
for" now has numbers ([CASE-328](../cases.d/CASE-328.md), [CLAIM-896](CLAIM-896.md)): power has to be
computed with the signalling estimated, and a violation of 0.19 then
needs 1,600 to over 4,000 respondents a context. A design that could
meet the condition is [CASE-329](../cases.d/CASE-329.md). Two cautions for reading a future
result against it: pooled counterbalancing cells can produce
contextuality no cell has ([CLAIM-895](CLAIM-895.md)), and a "noncontextual"
verdict from a plug-in estimate at a modest sample size is not evidence
of absence.
