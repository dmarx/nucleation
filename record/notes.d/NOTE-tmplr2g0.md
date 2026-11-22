---
status: Read
paper: LIT-tmpgkx6w
title: 'Generalised Winograd Schema and its Contextuality'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read in full for LEAD-182 on 2026-11-22, from the arXiv PDF
    2308.16498v1 (16 pages, text layer extracted), every section and the
    references. The quotes below were checked against that text by the
    filer. The violation and its standard deviation were recomputed from
    Table 1 (scratch/studies/lead-182/test_cbd.py): the printed rows sum
    to 0.998, and renormalised they give 0.196; at 87 responses a context
    the analytic standard deviation is 0.175.
date: '2026-11-22'
summary: >-
  Joining two Winograd schemas in one story makes a Bell-CHSH scenario
  over (pronoun, word) observables. One such story, judged by 348 valid
  Mechanical Turk respondents, violates the inequality by 0.192 with a
  standard deviation of 0.176. No-signalling holds because the response
  format enforces A/B symmetry, so the test cannot see the direct
  influences that free answers would show.
---
<!-- inactive-ok-file: CASE-tmpl2va4 CASE-tmpjp6vg — new and Proposed; the design and simulation this reading feeds -->
<!-- inactive-ok-file: CLAIM-009 — Proposed; open, the claim this reading bears on -->

# NOTE-tmplr2g0: Generalised Winograd Schema and its Contextuality

## Contribution

It shows that the Winograd schema, a pronoun resolved by world knowledge
under one of two words, cannot host contextuality as it stands, and
builds the smallest extension that can: two pronouns and two word pairs in
one discourse, isomorphic to Bell-CHSH. It then collects human judgements
on one instance and reports a positive violation.

## Key results

- §4.1: a schema's two sentences are two contexts with no shared
  observable, so "One can always construct a compatible global
  distribution by taking the product of the local distributions."
- §4.2, Definition 2: observables (p1, s1), (p1, a1), (p2, s2), (p2, a2);
  contexts the four (word1, word2) pairings; outcomes {A, B}. "The
  generalised WS scenario is isomorphic, i.e. identical upon relabelling,
  to the Bell-CHSH scenario."
- §4.2: near-deterministic judgements cannot be contextual, so "only a
  system with a moderate level of intelligence, in between that of humans
  and that of complete randomness, would have the possibility of being
  contextual." Items must be genuinely ambiguous to readers.
- §4.3, the instance: "A and B belong to the same [cannibalistic /
  herbivorous]1 species of animal. ... After a while, one of them2 is no
  longer [hungry / alive]2." Footnote 3: the original "contains several
  incorrect uses of English"; §4.4: "we did not notice these until a
  reviewer pointed them out, after data collection."
- §4.3, on symmetry: "all symmetric models are non-signalling ... By
  considering only symmetric models, we thereby avoid the complications
  of dealing with non-signalling models." Respondents "pick two out of the
  four combinations", which "allows the detection of invalid answers".
- §4.4: 410 responses (110 in one context, 100 in each other), 348 valid,
  USD 1.00 each. "The model violates the Bell-CHSH inequality by 0.192
  with a standard deviation of 0.176." Bootstrap: "87% of them exhibited a
  positive violation".
- §2.2, eq. 3: the CbD cyclic criterion, CNT1 = s_odd(⟨R R⟩) − Δ − n + 2,
  with Δ the summed marginal differences, which reduces to the CHSH
  violation when Δ = 0.

## Assumptions

- Each respondent answers in one context only (between subjects); a
  context is a version of the questionnaire.
- The two answers are elicited jointly as a choice among the four
  readings, and only answers in a symmetric pair are kept. So each valid
  response carries one bit, whether the two referents are the same, and
  the marginal of each pronoun is ½ by construction.
- The sign pattern of the violation is chosen after the data (the
  maximum over patterns), and no correction for that choice is reported.

## Concepts

- Generalised Winograd schema: two schemas in one discourse, giving two
  binary observables per party.
- Signalling in the sheaf sense, a marginal that differs between contexts;
  the paper separates it from contextuality (§2.1) but designs it away
  rather than measuring it.

## Bearing on the record

- [CASE-053](../cases.d/CASE-053.md) holds this study as "the right content, underpowered", and
  the reading confirms its figures and its point that the symmetry is
  forced. It adds one thing [CASE-053](../cases.d/CASE-053.md) does not say: the format does not
  merely discard asymmetric answers, it never elicits the per-pronoun
  answers, so the marginals that CbD discounts are not observed at all.
- For [LEAD-182](../leads.d/LEAD-182.md), it is the design to revise: free per-pronoun answers,
  named characters, and a CbD analysis with the signalling estimated
  ([CASE-tmpl2va4](../cases.d/CASE-tmpl2va4.md)). The power simulation ([CASE-tmpjp6vg](../cases.d/CASE-tmpjp6vg.md)) takes its Table 1
  as one of its true models.
- [CLAIM-325](../claims.d/CLAIM-325.md) and [CLAIM-009](../claims.d/CLAIM-009.md): it is the only pragmatic-content data set the
  record has with a positive violation, and the violation is about one
  standard deviation, so it neither meets [CLAIM-325](../claims.d/CLAIM-325.md)'s defeat condition nor
  gives [CLAIM-009](../claims.d/CLAIM-009.md) its test.

## Limitations

- One story, one run, faulty English, about 87 valid responses a
  context on average.
- Coreference from world knowledge is pragmatic only in the broad sense:
  no speaker, act or uptake is in play.
- The paper's "significance level of 87%" is the share of bootstrap
  resamples above zero, not a test at a stated level.
