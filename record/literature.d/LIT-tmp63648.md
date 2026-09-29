---
status: Active
status_note: 'read in full 2026-09-29 ([NOTE-tmpaxdi8](../notes.d/NOTE-tmpaxdi8.md)); Worth reading as the origin of the mutual-information bias and generalisation bound that [LIT-347](LIT-347.md) (Xu & Raginsky) extends, and as the first place its adaptive-composition chain rule and its per-query "information budget" with Gaussian noise (½·log(1+SNR) per query) appear. Read it knowing that it is stated for a finite set of m candidate statistics, and that "the bound is tight" is shown only for Gaussian argmax and threshold selections, as squared-error (not bias) bounds except in the exponential case.'
title: 'How much does your data exploration overfit? Controlling bias via information usage'
version: 2
history:
- version: 2
  date: '2026-09-29'
  note: >-
    Read in full (I read the full text of arXiv 1511.05219 v3 (8 Oct 2019),
    the accepted IEEE Transactions on Information Theory version
    ("Manuscript received January 30, 2017; revised May 30, 2018; accepted
    September 12, 2019"; "Part of this work was presented at AISTATS 2016"),
    23 pp., from the arXiv PDF. The text was extracted with PyMuPDF, and p.
    4 was rendered to check Corollary 1. I read all of it: the abstract,
    §§I–VII, Appendices A–I with every proof, the acknowledgement, all 37
    references and the author biographies. I checked the proofs of
    Propositions 1, 2, 5, 8, 9 and 10, Lemmas 1–3 and Proposition 13 line by
    line. For the Proposition 3 lower bound and the threshold Theorems 1–2
    (App. C), I followed the steps but did not re-derive the constants. I
    also compared v3 structurally against v1 (16 Nov 2015, titled
    "Controlling Bias in Adaptive Data Analysis Using Information Theory",
    23 pp.), reading its §§1–2 and the section list; I did not read v1 line
    by line, and I did not read v2 (6 Oct 2016) or the AISTATS 2016
    proceedings version. Page and section numbers are v3's. `published:` is
    the arXiv v1 date. No anthology entry exists for this paper (I grepped
    the arXiv id and both titles in record/literature.d).); the first NOTE
    on it, since it was seeded from the abstract alone. Status set from the
    reading: Active.
tags:
- learning-theory
- information-theory
- probabilistic-modeling
- anthology-candidate
date: '2026-09-29'
published: '2015-11-16'
doi: '10.1109/TIT.2019.2945779'
arxiv: '1511.05219'
first_author: 'Russo'
keywords:
- 'prior-art novelty map'
implementations: []
summary: >-
  Russo & Zou (2015), arXiv:1511.05219. Suppose an analyst reports
  statistic φ_T, chosen by any data-dependent rule T from m candidates
  each σ-sub-Gaussian. Then the selection bias obeys |E[φ_T − µ_T]| ≤
  σ√(2·I(T;φ)) (Prop. 1), where "information usage" I(T;φ) ≤ H(T) ≤ log m.
  For argmax selection over φ ~ N(µ,I) the squared error is Θ(1 + H(T))
  (Prop. 3). Adaptive analyses compose additively, with I(T_{k+1};φ) ≤ Σ_i
  I(Y_{T_i};φ_{T_i} | H_{i−1},T_i) (Lemma 1). Answering each query with
  Gaussian noise of variance σ²√j/n therefore keeps the k-th answer's
  error at O(σk^{1/4}/√n) (Prop. 7).
---

# LIT-tmp63648: How much does your data exploration overfit? Controlling bias via information usage

Russo & Zou (2015), *IEEE Transactions on Information Theory 66(1):302–323, January 2020 (Crossref-verified). An earlier version, "Controlling Bias in Adaptive Data Analysis Using Information Theory", appeared at AISTATS 2016 (PMLR 51; the proceedings version was not read) and is arXiv v1 (16 Nov 2015).* — arXiv:1511.05219

## Standing in the record

Filed on 2026-09-29 as a supplemental reading. The close readings of the owner's prior-art novelty map's
references found the map's citation for this point wrong, or its source unreachable, and this work is the
candidate replacement. `published:` is the first appearance ([ADR-002](../decisions.d/ADR-002.md)).

It was filed `Deferred`, unread. [NOTE-tmpaxdi8](../notes.d/NOTE-tmpaxdi8.md) is the close reading of 2026-09-29, and it placed the work: **Active** — Worth reading as the origin of the mutual-information bias and generalisation bound that [LIT-347](LIT-347.md) (Xu & Raginsky) extends, and as the first place its adaptive-composition chain rule and its per-query "information budget" with Gaussian noise (½·log(1+SNR) per query) appear. Read it knowing that it is stated for a finite set of m candidate statistics, and that "the bound is tight" is shown only for Gaussian argmax and threshold selections, as squared-error (not bias) bounds except in the exponential case.
