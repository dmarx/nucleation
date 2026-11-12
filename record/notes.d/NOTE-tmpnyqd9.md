---
status: Read
paper: LIT-tmp8v1tl
title: 'Chen, Kuo, Liu, Poon, Towey, Tse and Zhou — Metamorphic testing: a review of challenges and opportunities'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from the authors' manuscript ("Manuscript submitted
    to ACM", 26 pages with a cover sheet saying the final version is ACM
    Computing Surveys 51(1), 4:1–4:27), on the University of Wollongong's
    Research Online repository hosted on Figshare
    (https://ndownloader.figshare.com/files/50531136), lawful under
    ADR-074. Read in full: abstract and §§1–8 (Definitions 1–4, Concepts
    1–4, Challenges 1–7, Opportunities 1–7). Skipped: the reference list.
    Page numbers are the manuscript's. A delegated reader drafted the
    reading; every quotation below was rechecked against the downloaded
    text by script.
date: '2026-11-12'
summary: >-
  A review by metamorphic testing's originators. It defines metamorphic
  relations as necessary properties over two or more inputs and their
  outputs, says the method alleviates but cannot solve the oracle problem,
  and supplies three limits for using such relations as a scorer: they are
  necessary not sufficient, their choice dominates what is found, and their
  source decides whether passing them verifies or validates.
---
<!-- unresolved-ok-file: CASE-tmppm4do QUESTION-tmps5iou — entries proposed in pull request #484, not on this branch; cited in prose only -->
<!-- inactive-ok-file: ADR-tmppzz2h — Proposed; the topic decision this work first applies -->

# NOTE-tmpnyqd9: Chen, Kuo, Liu, Poon, Towey, Tse and Zhou — Metamorphic testing: a review of challenges and opportunities

## Contribution

A formal statement of metamorphic testing (MT) and its parts, by the group
that proposed it in 1998, with four common misreadings corrected, a review
of MT as an oracle substitute and as a way of generating tests, its
extension to proving relations, to validation and to quality assessment,
and its integration with debugging, fault localization, fault tolerance and
repair; then seven challenges and seven opportunities. The authors call it
"different from traditional surveys": it covers the most influential
studies, not all of them (p. 3).

## Key results

- **Relations, not outputs** (§2.2, p. 4): "Even if we cannot determine the
  correctness of the actual output for an individual input, it may still be
  possible to use relations among the expected outputs of multiple related
  inputs (and the inputs themselves) to help."
- **What a relation is** (abstract; Definition 1, p. 4): metamorphic
  relations are "necessary properties of the target function or algorithm
  in relation to multiple inputs and their expected outputs", over "a
  sequence of two or more inputs". A source test case is transformed into
  follow-up cases; together they form a metamorphic group.
- **Not an oracle** (§4.1, p. 8): MT alleviates the oracle problem but "one
  can never completely solve it"; even a complete set of relations "might
  still not be equivalent to a test oracle due to the necessary (but not
  sufficient) nature of the properties."
- **A few diverse relations go far, reportedly** (§4.1, p. 8, reporting Liu
  et al.): "MT only required an average of three to six diverse MRs to
  reveal at least 90% of the faults that could be detected by an oracle."
  A report of another study, unread here; Opportunity 1 adds that "the
  concept of diversity was not formally defined".
- **Not only equalities** (Concept 3, p. 7): "Not all MRs are equality
  relations." Removing a disjunct from a query's condition must return a
  subset of the original result (Example 2).
- **Choice dominates** (§4.2, p. 11): the compiler studies' contrast
  "emphasizes the significant impact MR choice has on the fault-detection
  effectiveness of MT."
- **Self-derived relations are suspect** (Challenge 2, p. 9): "MRs based on
  program executions may be erroneous if the implementation is faulty."
- **Tested, not proven** (§5.1, p. 12): "In MT, MRs are tested and not
  proven".
- **Source decides purpose** (§5.2, p. 13): relations violated by kNN and
  Naive Bayes implementations turned out to be users' expectations, not
  properties of the algorithms, so MT serves validation "if the MRs are
  identified based on actual user expectations rather than on the target
  algorithm"; "in verification, they are derived from the specifications;
  in validation, they are derived from the user expectations".
- **Localization is coarse** (Challenge 7, p. 16): "with an MR violation, it
  is only possible to say that at least one test case in the MR-violating MG
  is related to the fault, unless we do have a test oracle."
- **Relations change with requirements** (Opportunity 7, p. 21): in agile
  development "the MRs would also require regular updating and
  fine-tuning", "the adoption of new MRs and the removal of obsolete ones".

## Assumptions

- The target algorithm, or its users' expectations, has necessary
  properties statable as relations across inputs; MT is only as good as the
  relations chosen.
- The effectiveness evidence is mostly mutation analysis against random
  testing, on small or medium programs in single domains (Challenge 1).
- Identifying relations is largely manual and ad hoc (Challenge 2).

## Concepts

Oracle problem; metamorphic relation (MR); source and follow-up test case;
metamorphic group; MR diversity; semi-proving; metamorphic slicing;
verification against validation (Boehm's "building the product right" and
"building the right product"); differential testing and N-version
programming, which use one input and so are not MT; assertion checking, a
one-input property and so not an MR.

## Bearing on the record

A cited it in the exchange "luria experiment design" (2026-11-10), A50 §11,
for metamorphic relations as the hidden oracle of an evaluation of changes
to a record's schema, so that an agent is not scored on reproducing one
canonical patch. The characterization is accurate as far as it goes; the
use for schemas is A's transfer, not anything the survey discusses.

- **The proposed schema-change study** ([CASE-tmppm4do](../cases.d/CASE-tmppm4do.md), proposed in pull
  request [#484](https://github.com/dmarx/nucleation/issues/484) and not on this branch, seeded with [CASE-131](../cases.d/CASE-131.md)). Its specified
  outcomes, that B may raise support for A, that A does not depend on B,
  that A survives B's retirement, that renaming a scheme without changing
  its semantics leaves query results equivalent, are metamorphic relations
  in the survey's sense: a source state, a follow-up operation and a
  relation between outcomes, some of them non-equalities as Concept 3
  allows. The reading supports the design with three limits. Passing them
  shows no known violation, not a correct change (§4.1). Which relations
  are chosen dominates what is found (§4.2), and the hope that a handful of
  diverse ones approaches an oracle rests on one reported study with
  diversity undefined. And by §5.2 they are validation relations, drawn
  from what the record's users expect, not verification relations from a
  specification. [CASE-131](../cases.d/CASE-131.md) itself is a historical case the survey does not
  bear on.
- **[CLAIM-266](../claims.d/CLAIM-266.md)** (probes that supply an optimized system's training signal
  cannot certify what it preserves). Consistent with it by analogy only:
  Challenge 2's relations mined from the program's own runs cannot certify
  that program, and §5.2's point that a relation's source decides what
  passing it shows. The survey says nothing about optimization against
  probes, so no relation is written. Applied to the study, it suggests the
  hidden relations must not be visible to or derivable from the agents'
  own patches.
- **[QUESTION-tmps5iou](../questions.d/QUESTION-tmps5iou.md)** (proposed in [#484](https://github.com/dmarx/nucleation/issues/484): whether coupling schema change to
  governance does work that performance-gated evolution does not). The
  survey supplies a measuring tool for its "semantic correction without
  regressions" outcome and leaves the question open.
- **[ADR-tmppzz2h](../decisions.d/ADR-tmppzz2h.md).** The work fits the word's first item, "testing and test
  oracles, metamorphic testing among them".

## Limitations

- Read from the submitted manuscript, not the ACM version; wording and pages
  may differ slightly.
- A review: its figures (three to six relations, about 90% of
  oracle-detectable faults) report other studies, unread here.
- Nothing in it concerns records of knowledge, agents or optimization
  against tests; every bearing above is by transfer.
