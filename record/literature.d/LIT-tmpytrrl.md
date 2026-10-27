---
status: Active
status_note: >-
  read in full 2026-10-27 ([NOTE-tmp2eky0](../notes.d/NOTE-tmp2eky0.md)), from arXiv v2; worth reading as
  the quantitative restatement of relational quantum mechanics, with
  relative facts defined by relative information and held by commutative
  subalgebras rather than by quantum systems. The definitions are clean.
  The resolutions it claims (combination problem, Frauchiger–Renner,
  intersubjectivity) are paragraphs or citations, and every consistency
  check is computed relative to one outside system.
title: 'Relative Information, Relative Facts'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read. Checked against the arXiv API on 2026-10-27: Andrea
    Di Biagio and Carlo Rovelli, arXiv 2510.11349, v1 submitted 13
    October 2025, which is `published:` per ADR-002; v2 is current. A19
    said it was revised in March 2026; that was not checked.
- version: 2
  date: '2026-10-27'
  note: >-
    Read in full from arXiv 2510.11349v2, 12 pp., §§I–X and Appendices
    A–E, with the references; the first NOTE on the work (NOTE-tmp2eky0).
    v1 was not read. Status set from the reading: Active. `published:`
    stays 2025-10-13, the v1 date, per ADR-002. A19's "revised March 2026"
    is wrong: the v2 PDF is stamped "9 Feb 2026" and "Dated: February 10,
    2026", which agrees with the arXiv API's updated date of 2026-02-09.
    The summary is replaced by one from the text. The exchange's
    description was right on each of its four points, all taken from the
    abstract: a quantitative treatment of information and relative facts,
    no fundamentally special role for observers, perspectives tied to
    commuting observables, and measurement as a continuous process. It
    softened one, saying "rather than necessarily with whole systems",
    where the paper holds that a quantum system with non-commuting
    variables has no perspective at all (p. 4). It left out the
    definitions themselves (I_{A|B} = I_A + I_{A:B}, a relative fact as
    maximal relative information), "Every fact is a relative fact", the
    graded threshold for facthood, and that the continuity of measurement
    is called "a side result" that "has actually little to do with quantum
    theory". Three THEORYs are filed from it (THEORY-tmpyoeip,
    THEORY-tmper2kf, THEORY-tmphcxoi).
tags:
- quantum-foundations
- information-theory
date: '2026-10-27'
published: '2025-10-13'
arxiv: '2510.11349'
first_author: 'Di Biagio'
keywords:
- 'relational quantum mechanics'
- 'relative information'
- 'perspectives'
- 'measurement'
implementations: []
summary: >-
  Di Biagio & Rovelli (2025). Relational quantum mechanics restated in
  Shannon terms. The information about A relative to B is the expected
  conditional information, I_{A|B} = I_A + I_{A:B}, and A is a fact
  relative to B when it is maximal. Only commuting variables have a joint
  distribution, so perspectives belong to commutative subalgebras
  ("classical subsystems"), not to quantum systems, and a qubit has none.
  "Every fact is a relative fact", and in practice a fact is information
  "high enough" for the resolution needed. As a side result, a von
  Neumann measurement is continuous growth of the pointer's information,
  sin²(ωt)H_A in the model. Merging perspectives, Wigner's friend, EPR and
  the extended Wigner's friend scenario are treated by worked examples.
---
<!-- inactive-ok-file: QUESTION-tmpubsi9 THEORY-tmphcxoi — Open or Proposed; the question it was filed for and a THEORY filed from it, cited as open -->

# LIT-tmpytrrl: Relative Information, Relative Facts

Di Biagio, A., & Rovelli, C. (2025). Relative information, relative facts. arXiv:2510.11349.

Read in full on 2026-10-27 ([NOTE-tmp2eky0](../notes.d/NOTE-tmp2eky0.md)).

## Why this is here

A19 §3 called it "high-priority new prior art" for a generic notion of
measurement. It bears on [QUESTION-tmpubsi9](../questions.d/QUESTION-tmpubsi9.md). The reading found it exact
for the question's lowest rungs, correlation and complete correlation
between commuting variables, and silent on records, use and revision
([NOTE-tmp2eky0](../notes.d/NOTE-tmp2eky0.md)).
