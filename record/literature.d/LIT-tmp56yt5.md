---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmp3w3nx](../notes.d/NOTE-tmp3w3nx.md)); worth reading as the large-scale test of the QQ equality: across 66 Pew surveys chosen without regard to their results, question order changes the answers significantly (p = 0.0004 for the distribution of order-effect χ² values), while the probability of answering the two questions alike stays the same (p = 0.4625 for the q values). Read with the caveats that the supporting information, which holds the proof, the per-study table and the χ² tests, was not reachable and was not read, and that the paper''s title claims more than its evidence: the equality is a symmetry constraint that the authors concede a classical model could be built to satisfy, and [LIT-264](LIT-264.md) shows that data satisfying it are noncontextual.'
title: 'Context effects produced by question orders reveal quantum nature of human judgments'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed and read on 2026-10-09 (NOTE-tmp3w3nx), from the PubMed Central
    full text (PMC4084470), main text, Table 1, figure captions and
    references. The supporting information (pnas.201407756SI.pdf) was not
    read: PMC's copy returned a proof-of-work challenge page, PNAS's copy
    HTTP 403, and Europe PMC reports the article as not open access for
    supplementary files. Details checked against Crossref (PNAS
    111(26):9431–9436; Zheng Wang, Tyler Solloway, Richard M. Shiffrin,
    Jerome R. Busemeyer). `published:` is the Crossref published-online
    date, 16 June 2014; the issue is dated 1 July 2014. Not held in the
    Anthology of the SOTA: a grep of its record/ (clone of 2026-10-09,
    commit d8b5ba5) for the authors, the DOI and the title found nothing.
tags:
- cognition
- social-science
- probabilistic-modeling
- quantum-foundations
date: '2026-10-09'
published: '2014-06-16'
doi: '10.1073/pnas.1407756111'
first_author: 'Wang'
keywords:
- 'question order effects'
- 'context effects'
- 'quantum probability'
- 'QQ equality'
- 'law of reciprocity'
- 'survey research'
implementations: []
summary: >-
  Wang, Solloway, Shiffrin & Busemeyer (2014), PNAS 111(26):9431–9436.
  Tests the QQ equality of [LIT-tmptn5dr](LIT-tmptn5dr.md), that the probability of giving
  the same answer to two questions does not depend on their order, on 70
  national surveys and two laboratory experiments. Across all 66 Pew
  surveys from 2001–2011 that varied the order of two questions, order
  effects are significant (p = 0.0004) and the q values are not
  (p = 0.4625); paired context effects across 72 studies correlate at
  r = −0.82 along the predicted line of slope −1.
---

<!-- inactive-ok-file: LIT-316 — Deferred; the book is unread here and is named only as the paper's own reference for the proof -->
<!-- inactive-ok-file: THEORY-tmp9wyar — Proposed; this reading is its primary source -->

# LIT-tmp56yt5: Context effects produced by question orders reveal quantum nature of human judgments

Zheng Wang, Tyler Solloway, Richard M. Shiffrin, Jerome R. Busemeyer
(2014), *Proceedings of the National Academy of Sciences* 111(26):9431–9436
— DOI-10.1073/pnas.1407756111

## Key takeaways

- **The regularity.** In a table of context effects (the cell-by-cell
  difference between the two orders' answer proportions), the two cells
  of each diagonal sum to approximately zero: q =
  [p(AyBy) + p(AnBn)] − [p(ByAy) + p(BnAn)] ≈ 0. The number of people
  who switch from yes–yes to no–no in one order is offset by those who
  switch the other way. Nothing in probability forces it: the set of
  possible context-effect tables is a three-dimensional pyramid, and the
  QQ equality picks out a triangular plane inside it.
- **The data.** There are 72 studies: 66 Pew Research Center surveys
  from 2001–2011, which are all the Pew surveys of that decade that
  varied the order of two questions; three Gallup polls from Moore
  (2002); Schuman, Presser and Ludwig's 1981 abortion study; and two
  laboratory experiments. The Rose–Jackson poll is excluded because the
  model predicts it should fail. Paired context effects fall along the a
  priori line of slope −1 (r = −0.82; −0.73 without two extremes), and
  the ratio of q to the size of the order effect falls towards zero as
  order effects grow (17 studies with order effect > 0.10).
- **The test that carries the weight** is on the 66 Pew surveys alone,
  chosen without regard to their outcome: the distribution of χ² values
  for order effects departs from the null (p = 0.0004), and the
  distribution for q does not (p = 0.4625).
- **The model and its condition.** The prediction is the Lüders double
  projection of [LIT-tmptn5dr](LIT-tmptn5dr.md), and it holds for mixed states, so it
  survives individual differences. It requires that the questions be
  asked back to back. New information between them applies different
  transformations, P_A U″ P_B versus P_B U′ P_A, and the equality is no
  longer expected, which is the Rose–Jackson case (q = 0.1514,
  χ²(1) = 28.57).
- **What the authors concede.** "It is possible to construct a model that
  is narrowly constrained to satisfy the QQ equality, but these
  constraints could also prevent the model from accounting for order
  effects", with two examples in the supporting information, which was
  not read here. They ask for alternative accounts. They say the brain
  need not be quantum: quantum probability may describe reasoning even
  if neural processes are classical.

## Standing in the record

Filed on 2026-10-09 at the owner's request, from the bibliography of the
owner's manuscript (work `what-survives-translation`) as it stood on
2026-10-08: a work the bibliography considered and the final reference
list dropped. See the curation entry of that day.

Read on 2026-10-09 ([NOTE-tmp3w3nx](../notes.d/NOTE-tmp3w3nx.md)). It is the primary source of
[THEORY-tmp9wyar](../theory.d/THEORY-tmp9wyar.md). The model it tests is [LIT-tmptn5dr](LIT-tmptn5dr.md). Its data set,
supplied by the authors, is re-analysed under Contextuality-by-Default in
[LIT-264](LIT-264.md), which finds the equality implies noncontextuality. The paper
cites [LIT-316](LIT-316.md) for proofs; that book is unread here.
