---
status: Active
status_note: >-
  read in full 2026-10-15 from the first author's manuscript of the journal paper,
  linked from Gupta's publication list (www3.cs.stonybrook.edu/~hgupta/ps/sel-views-tkde.pdf,
  41 single-column pages, read by OCR; not compared with IEEE's typeset pp. 24–43).
  Worth reading as the consolidated, proved account of Gupta's 1997 space-budget
  results ([LIT-tmpn0tsb](LIT-tmpn0tsb.md)) and Gupta and Mumick's 1999 maintenance-budget results
  ([LIT-tmpppd6p](LIT-tmpppd6p.md)): it is the journal version of both papers, not of the 1999 paper
  alone, and it adds proofs, not new problems or guarantees. The inverted-tree greedy's
  1 − 1/e guarantee for OR view graphs under a maintenance budget (now Theorem 8,
  still bicriteria at up to 2S and still assuming no tree-piece of the optimum exceeds
  S) and the exactness of A* on AND-OR graphs (Theorem 10) are now proved; the assumption-free
  half-density bound (Theorem 9) is referred to Gupta's thesis; the guarantee is
  still for OR graphs only and the greedy still exponential in the worst case, data
  cubes included. For [QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md) it changes nothing: the article holds two
  separate models, upkeep in the objective under a space budget (guaranteed only
  for AND view graphs in which every view is queried more often than updated, a
  lemma it now says fails for OR graphs) and upkeep as a budget with query cost
  alone in the objective, never both constraints together, and no build cost or
  staleness. [LIT-tmpu5ktj](LIT-tmpu5ktj.md) remains the closest to a joint model.
title: Selection of Views to Materialize in a Data Warehouse
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked against Crossref on 2026-10-15: IEEE TKDE
    17(1), pp. 24–43, January 2005; Crossref gives the month only. Not held in the
    Anthology of the SOTA: a grep of its record/ (clone of 2026-10-15, commit d1573d2)
    for the title and DOI found nothing. Read the same day (NOTE-tmpuaboe).
tags:
- databases
- operations-research
date: '2026-10-15'
published: '2005-01-01'
doi: 10.1109/TKDE.2005.16
first_author: Gupta
keywords: []
implementations: []
summary: >-
  Gupta and Mumick (2005), IEEE TKDE. The journal paper merges Gupta's 1997 space-budget
  results and the 1999 maintenance-budget results into one article; it adds proofs,
  not new problems or new guarantees. Theorem 8 (the conference Theorem 1: inverted-tree
  greedy on OR view graphs, at most 2S of maintenance, at least 1 − 1/e of an optimum
  with the same maintenance, assuming no inverted-tree piece of the optimum exceeds
  S) and Theorem 10 (A* is exact on AND-OR graphs) are now proved, while Theorem
  9 (the assumption-free half-density bound) is referred to Gupta's thesis. The
  maintenance-budget guarantee stays confined to OR view graphs, the greedy stays
  exponential in the worst case, and the two constraints are never combined. The
  only place upkeep is traded against query cost is the 1997 formulation carried
  over, query cost plus maintenance cost minimized under a space budget, with a
  guarantee only for AND view graphs in which every view is queried more often than
  it is updated; build cost and staleness are not modelled anywhere.
---

# LIT-tmp28bff: Selection of Views to Materialize in a Data Warehouse

Gupta, H. and Mumick, I. S. (2005). Selection of views to materialize in a data warehouse. *IEEE Transactions on Knowledge and Data Engineering* 17(1), 24–43. DOI 10.1109/TKDE.2005.16

## Key takeaways

Read in full ([NOTE-tmpuaboe](../notes.d/NOTE-tmpuaboe.md)), from the first author's manuscript of the journal paper, by OCR. It is the journal version of both ICDT papers, Gupta 1997 ([LIT-tmpn0tsb](LIT-tmpn0tsb.md)) and Gupta and Mumick 1999 ([LIT-tmpppd6p](LIT-tmpppd6p.md)), and it adds proofs, not new problems or guarantees. The maintenance-budget greedy for OR view graphs (now Theorem 8, still at up to twice the budget and still assuming no piece of the optimum exceeds it) and the exactness of A* (Theorem 10) are now proved; the assumption-free bound (Theorem 9) is referred to Gupta's thesis. The guarantees still cover OR graphs only, the greedy is still exponential in the worst case, the space and maintenance constraints are never combined, and build cost and staleness are not modelled.

## Why this is here

[QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md): the conference version ([LIT-tmpppd6p](LIT-tmpppd6p.md)) stated its guarantees without proof and covered OR view graphs only. This is the journal version.
