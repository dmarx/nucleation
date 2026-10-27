---
number: 103
status: Open
formerly:
- QUESTION-tmpadry4
title: Is computational indistinguishability the bounded-observer form of signal
  detection's chance ROC, and is ideal-observer efficiency its empirical measure,
  so that the record's formal results on bounded observers can be tested on real
  ones?
version: 1
tags:
- probabilistic-modeling
- information-theory
- cognition
date: '2026-10-15'
line: formal-apparatus
summary: >-
  The owner asked whether material downstream of computational indistinguishability,
  or the signal detection literature, would help. A test's distinguishing advantage
  is its hit rate minus its false-alarm rate, a point on its ROC; the best over
  all tests is total variation, reached by the likelihood-ratio detector ([THEORY-031](../theory.d/THEORY-031.md)).
  Computational indistinguishability says every efficient observer's ROC stays near
  the chance diagonal. Ideal-observer analysis measures how far real observers fall
  short of the ideal. This asks whether the two are one framework.
answered_by:
- THEORY-336
bearing:
- THEORY-357
- THEORY-349
---
<!-- inactive-ok-file: CLAIM-298 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# QUESTION-103: Is computational indistinguishability the bounded-observer form of signal detection's chance ROC, and is ideal-observer efficiency its empirical measure, so that the record's formal results on bounded observers can be tested on real ones?

## Why it is a question

The owner, 2026-10-15: "I'm wondering if maybe material downstream of the
computational indistinguishability work might be helpful as well. or maybe
we can connect that angle to the signal detection literature?"

**The formal link.** For a test f between two hypotheses, the distinguishing
advantage |Pr[f = 1 | x] − Pr[f = 1 | x′]| is hit rate minus false-alarm
rate, one point on f's ROC. Over all tests its maximum is the total variation
distance, attained by thresholding the likelihood ratio. The record holds
that half: [THEORY-031](../theory.d/THEORY-031.md) (from Peterson and Birdsall, [LIT-364](../literature.d/LIT-364.md)) says the
likelihood-ratio detector is optimal and performance is an ROC. [CLAIM-302](../claims.d/CLAIM-302.md)
says that for a restricted class of observers the best ROC can sit near
the chance diagonal while the ideal one is near perfect. So the record's
formal results on bounded observers are statements about the gap between
the ideal ROC and the best ROC in a class.

**The empirical side.** Vision science measures that gap: efficiency, the
squared ratio of human to ideal d′ (Burgess et al. 1981; Pelli and Farell
1999, neither held), says how much of the information a real observer uses;
Geisler 2011 ([LIT-1055](../literature.d/LIT-1055.md)) reviews the ideal-observer method without giving
the formula. If the link holds, the bounded-
observer questions ([QUESTION-111](QUESTION-111.md), [QUESTION-104](QUESTION-104.md)) have a measure
that can be taken on people and models, not only constructed.

**Downstream of indistinguishability.**

- Pseudoentropy (Håstad, Impagliazzo, Levin and Luby 1999, [LIT-1051](../literature.d/LIT-1051.md)):
  information content as efficient observers can tell, a candidate for the
  quantity [QUESTION-110](QUESTION-110.md) asks for.
- Outcome indistinguishability and multicalibration (Dwork et al. 2021,
  [LIT-1068](../literature.d/LIT-1068.md); Hébert-Johnson et al. 2018, [LIT-1052](../literature.d/LIT-1052.md)): a predictor is
  adequate relative to a class of distinguishers if none of them can tell
  its outcomes from nature's. That is individuation by sufficiency
  ([CLAIM-152](../claims.d/CLAIM-152.md)) with the observer's resources explicit.

**What would answer it.** A statement of the correspondence precise enough
to fail: which SDT quantity corresponds to advantage, whether a criterion
shift has a counterpart (indistinguishability is criterion-free, as d′ is
only in the equal-variance case, [THEORY-031](../theory.d/THEORY-031.md)), and whether efficiency is
well defined for a class of observers rather than one. A second part
would test it: a case where the record's formal gap is measured as an
efficiency. A possible use for [CLAIM-298](../claims.d/CLAIM-298.md), speculative: SDT separates
a change in the evidence (d′) from a change in criterion (bias), which
may be the split that claim needs between what is retrieved and how it
is weighed.

## Note of 2026-10-15: what the four readings found

All four were read the same day. The bridge is narrower than first stated.

- **Ideal-observer analysis bounds a different observer.** Geisler
  ([LIT-1055](../literature.d/LIT-1055.md), [NOTE-870](../notes.d/NOTE-870.md)) constrains the ideal observer by degrading
  its input, a garbling that loses information. [CLAIM-302](../claims.d/CLAIM-302.md) keeps the
  input and restricts the class of tests. These are the two receivers
  [CLAIM-199](../claims.d/CLAIM-199.md) already separates, Blackwell's ceiling and a rule class. So
  efficiency measures the first gap, and computational indistinguishability
  describes the second; a measure of the second on real observers is still
  wanting. The review also gives no formula for efficiency: the squared
  ratio of d′ above is from Burgess et al. 1981 and Pelli and Farell 1999,
  neither held.
- **Pseudoentropy** ([LIT-1051](../literature.d/LIT-1051.md), [NOTE-880](../notes.d/NOTE-880.md)). Håstad et al. define
  computational entropy with Shannon entropy and call indistinguishability
  "the computationally restricted adversary definition of statistical
  distance". The claims' G(Uₙ) is, in their terms, a false entropy
  generator. Their time–success ratio is a worked recovery-cost measure
  for [QUESTION-110](QUESTION-110.md).
- **Outcome indistinguishability** ([LIT-1068](../literature.d/LIT-1068.md), [NOTE-885](../notes.d/NOTE-885.md)) is the
  paper that frames adequacy as indistinguishability to a class, not
  multicalibration ([LIT-1052](../literature.d/LIT-1052.md), [NOTE-879](../notes.d/NOTE-879.md)), as first attributed above.
  Its finding for [QUESTION-104](QUESTION-104.md): the observer's access matters as much
  as its budget, and with oracle or code access a cheap observer can force
  a model as complex as nature.
- None of the four mentions signal detection. The link to ROC and d′ is
  the record's, and the criterion question is open.
