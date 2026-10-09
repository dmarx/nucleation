---
status: Active
status_note: 'read 2026-10-09 (NOTE-tmpwfgbe); worth reading as the step that makes Contextuality-by-Default representation-dependent. Every variable is replaced by binary splits (dichotomizations) and connections are coupled multimaximally, so a verdict belongs to a chosen set of splits, not to the measurements alone. Its one worked result is striking: if every split of two content-sharing k-valued variables is kept, that pair alone is noncontextual exactly when one variable "nominally dominates" the other, i.e. its probabilities fall below the other''s for at most one value (Theorem 4.6). For continuous variables the analogue makes any difference in distribution count as contextuality. The authors present this as opening behavioural contextuality, not as a reductio. Proofs are in the supplement and contain small slips that do not affect the results.'
title: 'Contextuality in Canonical Systems of Random Variables'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full on 2026-10-09 (NOTE-tmpwfgbe) from arXiv 1703.01252v4
    (19 Jul 2017, 12 pages of main text and 8 of supplement with proofs,
    "version 4 is a minor revision"), text extracted with pdftotext.
    Details checked against arXiv (v1 submitted 3 March 2017; journal ref
    Phil. Trans. R. Soc. A 375: 20160389) and Crossref (DOI
    10.1098/rsta.2016.0389, Philosophical Transactions of the Royal
    Society A 375(2106), article 20160389, published online 2 October
    2017, issue 13 November 2017). `published:` is the arXiv v1 date. Not
    held in the Anthology of the SOTA: a grep of its record/ (clone of
    2026-10-09, commit d8b5ba5) for the authors, the identifiers and the
    title found nothing.
tags:
- contextuality
- mathematics
- cognition
date: '2026-10-09'
published: '2017-03-03'
arxiv: '1703.01252'
doi: '10.1098/rsta.2016.0389'
first_author: 'Dzhafarov'
keywords:
- 'canonical systems'
- 'contextuality'
- 'dichotomization'
- 'direct influences'
- 'measurements'
implementations: []
summary: >-
  Dzhafarov, Cervantes & Kujala (2017), Phil. Trans. R. Soc. A
  375:20160389. Proposes that contextuality be judged only on a system's
  canonical representation: every variable, and every joining or
  coarsening of interest, replaced by its binary splits, with
  connections coupled multimaximally (pairwise maximally). For two
  content-sharing k-valued variables with all splits kept, the canonical
  system is noncontextual if and only if one variable nominally dominates
  the other (Pr below the other's for at most one value; Theorem 4.6).
  For continuous densities with all splits, any difference in
  distribution is contextual.
extends:
- LIT-tmpsa1qj
---

<!-- inactive-ok-file: THEORY-013 THEORY-tmpjdnxt — Proposed; named for the scope this reading bears on and the theory it sources -->

# LIT-tmp1kfuc: Contextuality in Canonical Systems of Random Variables

Ehtibar N. Dzhafarov, Víctor H. Cervantes and Janne V. Kujala (2017),
*Philosophical Transactions of the Royal Society A* 375(2106), 20160389 —
ARXIV-1703.01252

## Key takeaways

- **Canonical representation** (Section 3). Contextuality is decided on
  a system in which (A) every variable is binary and, after
  multimaximality, (B) connections are handled pairwise. A k-valued
  variable is replaced by its k one-value "detector" splits, plus the
  splits of any coarsening one cares about. Joint variables are formed
  by joining when within-context dependencies must count (Example 3.1).
  Which transformations to include "reflects what aspects of the
  empirical situation one is interested in". The canonical system is
  unique given that choice.
- **General CbD** (Section 2). Noncontextuality is relative to a chosen
  set T of connection couplings (Definition 2.1). The degree of
  contextuality is min‖X‖ − 1 over quasi-couplings agreeing with T
  (Theorems 2.4–2.5, from LIT-777).
- **One pair, all splits** (Section 4). For R_1^1, R_1^2 with values
  1…k and masses p_i, q_i, keep all 2^{k−1} − 1 splits. Then only the 1-
  and 2-splits matter (Theorems 4.1, 4.3). A maximally connected coupling
  of the 1-2 system is unique if it exists, and is supported on the
  diagonal plus one row or one column (Theorem 4.4). It exists if and
  only if p_i > q_i for at most one i, or p_i < q_i for at most one i
  (Corollary 4.5). The whole system is noncontextual exactly then
  (Theorem 4.6: *nominal dominance*).
- **Consequences the authors draw** (Section 5). Nominal dominance is "a
  stringent necessary condition for noncontextuality, likely to be
  violated in many empirical systems". Until then, almost all
  dichotomous behavioural systems examined had been noncontextual.
  Canonical representations of multiple-choice responses "offer new
  possibilities". For continuous densities, all splits make the pair
  contextual unless f = g. Restricting splits to intervals or cuts of an
  ordered scale is left as future work.

## Standing in the record

Filed on 2026-10-09 from the manuscript bibliography of 2026-10-09 (work
`what-survives-translation`) at the owner's request: a work the manuscript
considered and dropped from its final reference list. See the curation entry
of that day.

Read on 2026-10-09 (NOTE-tmpwfgbe). It is the source of THEORY-tmpjdnxt,
which states that CbD's verdict depends on the chosen representation. It
bears on THEORY-013's scope: that theory's data are binary, and this
paper's verdict for multi-valued responses can differ sharply.
