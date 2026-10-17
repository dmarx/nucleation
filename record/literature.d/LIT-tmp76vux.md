---
status: Active
status_note: 'read 2026-10-16 (NOTE-tmpicuma), the formal sections in full and the numerical and application sections at lower resolution; worth reading as the source of the k-nearest-neighbour (KSG) mutual-information estimators that the record''s readings use off the shelf (NOTE-788, NOTE-320, NOTE-828). Read it knowing that the estimators rest on a locally-constant-density approximation with no bias bound, that their exactness for independent variables is a numerical conjecture the paper''s own Weinman example strains, and that it estimates mutual information and multi-information only: conditional mutual information, and so transfer entropy, is not treated. Filed as THEORY-tmpj670e.'
title: 'Estimating Mutual Information'
version: 1
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Filed at the owner's request as the estimator behind the record's
    transfer-entropy and mutual-information readings, which cite it or use
    an implementation of it without holding it. Citation checked against
    the arXiv API on 2026-10-16 (Phys. Rev. E 69, 066138, 2004). Not held
    in the Anthology of the SOTA: a grep of its record/ (clone of
    2026-10-12, d1573d2) found the estimator used as a tool in its reading
    of the information-bottleneck rebuttal (ANTH-LIT-509, its NOTE-253)
    but no entry for the paper, and its topic vocabulary has no word an
    estimation paper in statistical physics could take. Read the same day
    from arXiv cond-mat/0305641v1 (NOTE-tmpicuma); the PRE version was not
    compared.
tags:
- information-theory
- mathematical-statistics
date: '2026-10-16'
published: '2003-05-28'
arxiv: 'cond-mat/0305641'
doi: '10.1103/PhysRevE.69.066138'
first_author: 'Kraskov'
keywords:
- 'mutual information'
- 'estimation'
- 'nearest neighbours'
- 'Kozachenko-Leonenko estimator'
- 'independent component analysis'
implementations: []
summary: >-
  Kraskov, Stögbauer & Grassberger (2004), *Physical Review E* 69, 066138, [ARXIV-cond-mat/0305641](https://arxiv.org/abs/cond-mat/0305641). Two estimators of I(X,Y) from N i.i.d. samples, built from Kozachenko–Leonenko k-nearest-neighbour entropy estimates with the joint space in the maximum norm: I⁽¹⁾ = ψ(k) − ⟨ψ(n_x+1) + ψ(n_y+1)⟩ + ψ(N), and I⁽²⁾ = ψ(k) − 1/k − ⟨ψ(n_x) + ψ(n_y)⟩ + ψ(N), where n_x, n_y count marginal neighbours within the joint k-th-neighbour distance. Using one distance scale across joint and marginal spaces makes the biases largely cancel. Numerically they are exact for independent variables (conjectured, not proved) and have systematic errors that scale with k/N.
---

# LIT-tmp76vux: Estimating Mutual Information

Alexander Kraskov, Harald Stögbauer and Peter Grassberger (2004), "Estimating Mutual Information", *Physical Review E* 69: 066138 — [ARXIV-cond-mat/0305641](https://arxiv.org/abs/cond-mat/0305641)

## Key takeaways

*From the reading, [NOTE-tmpicuma](../notes.d/NOTE-tmpicuma.md).*

- **Two estimators (Eqs. 8, 9).** I⁽¹⁾ counts marginal points strictly
  inside the joint k-th-neighbour cube; I⁽²⁾ uses the hyper-rectangle of
  the k-th neighbour's marginal extents. They behave almost identically;
  I⁽²⁾ is preferred in very high dimension.
- **The trick.** Estimating H(X), H(Y) and H(X,Y) separately with a fixed
  k uses different length scales, so the biases do not cancel. Taking the
  marginal neighbour counts at the joint distance makes them nearly
  cancel (§II B).
- **The only approximation** is a constant density inside each
  neighbourhood (Eq. 18). The bias is set by nonuniformity at the smallest
  resolved scale and scales, numerically, as k/N or (k − ½)/N (Eq. 32).
- **Exact for independence, by numerics.** The estimate vanishes up to
  fluctuations whenever µ(x, y) = µ(x)µ(y), for every marginal tried. Stated
  as a conjecture with "no proof for this very surprising result" (p. 3).
- **Practice inside the paper.** Use k = 2 to 4 for estimation and large k
  for testing independence; break ties from discretized data with noise of
  order 10⁻¹⁰; transform heavily skewed variables first.

## Standing in the record

Filed on 2026-10-16 as the estimator behind the record's information-flow
readings, and read the same day. [NOTE-788](../notes.d/NOTE-788.md) estimates mutual information with
scikit-learn's kNN estimator and [NOTE-320](../notes.d/NOTE-320.md) and [NOTE-828](../notes.d/NOTE-828.md) compare against
"Kraskov"; the record now holds what that estimator assumes. It does not
estimate transfer entropy: the conditional extension is later work, not
held. Filed as [THEORY-tmpj670e](../theory.d/THEORY-tmpj670e.md). `mathematical-statistics` is for its
subject, estimation; it carries no instruction for machine-learning
practice, its applications being gene-expression data and ICA of a fetal
ECG.
