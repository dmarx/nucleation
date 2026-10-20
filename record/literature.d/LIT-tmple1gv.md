---
status: Active
title: 'Clustering and the hyperbolic geometry of complex networks'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed and skimmed on 2026-10-20 (NOTE-tmprov8v) in the promotion audit
    (batch 057), as the second half of THEORY-188's reading task: the
    clustering of the hyperbolic random graph at positive temperature.
    From the arXiv PDF of v3 (28 June 2015, 51 pp.), text extracted with
    pdftotext. Checked against the arXiv abstract page (arXiv:1309.0459,
    math.PR, v1 submitted 2 September 2013) and Crossref (DOI
    10.1080/15427951.2015.1067848, Internet Mathematics, published online
    25 July 2015; an extended abstract appeared at WAW 2014, DOI
    10.1007/978-3-319-13123-8_1; authors Elisabetta Candellero, Nikolaos
    Fountoulakis). `published:` is the arXiv v1 date (ADR-002). Not held
    in nucleation before this filing: a grep of record/ for the authors
    and the identifier found nothing. It is probability on random graphs,
    so no anthology topic holds it.
tags:
- network-science
- mathematics
- complex-systems
date: '2026-10-20'
published: '2013-09-02'
arxiv: '1309.0459'
doi: '10.1080/15427951.2015.1067848'
first_author: 'Candellero'
keywords:
- 'random hyperbolic graphs'
- 'global clustering coefficient'
- 'binomial model'
- 'temperature'
- 'complex networks'
implementations: []
summary: >-
  Candellero and Fountoulakis (2015), Internet Mathematics. For Krioukov et
  al.'s hyperbolic random graph with curvature −ζ², density exponent α and
  0 < ζ/α < 2, in the soft model with connection probability
  1/(exp(β(ζ/2)(d − R)) + 1): when β > 1 (temperature below 1) the global
  clustering coefficient (three times triangles over paths of length two)
  converges in probability to an explicit positive constant if ζ/α < 1
  and to zero if 1 ≤ ζ/α < 2; when β ≤ 1 it converges to zero. Restricted
  to vertices of bounded type it stays positive for every ζ/α < 2 when
  β > 1.
---
<!-- inactive-ok-file: THEORY-188 — Proposed; the account this reading was filed for, which it does not yet promote -->

# LIT-tmple1gv: Clustering and the hyperbolic geometry of complex networks

Elisabetta Candellero and Nikolaos Fountoulakis (2015), *Internet
Mathematics* — [ARXIV-1309.0459](https://arxiv.org/abs/1309.0459), DOI-10.1080/15427951.2015.1067848

## Key takeaways

- **Two models.** The disc model joins vertices at distance at most R;
  the binomial model joins them with probability
  1/(exp(β(ζ/2)(d(u, v) − R)) + 1), β the inverse temperature, and has the
  disc model as its β → ∞ limit. N = ν e^(ζR/2) vertices.
- **Global clustering (Theorem 1.2).** For β > 1, C2 → L∞(β, ζ, α) > 0
  in probability when 0 < ζ/α < 1, and C2 → 0 when 1 ≤ ζ/α < 2. For
  β ≤ 1, C2 → 0. The limit does not depend on ν, so clustering and
  average degree can be tuned separately.
- **Why it vanishes for heavy tails.** When ζ/α ≥ 1 (degree exponent at
  most 3), vertices of type above R/2 appear; their degrees add many paths
  of length two and few triangles. Removing them, the clustering of the
  subgraph of vertices of type at most t stays positive for every
  ζ/α < 2 when β > 1 (Theorem 1.3).
- **Not the local average.** The result is for C2. The average of local
  coefficients, the quantity Krioukov et al. simulated and Gugelmann et
  al. bounded, is said to need "significant modification" of the analysis.

## Standing in the record

Filed on 2026-10-20 by the promotion audit (batch 057) for [THEORY-188](../theory.d/THEORY-188.md)'s
clustering clause. It confirms clustering is tuned by the temperature with
a transition at T = 1, but only for the global coefficient, and only when
the degree exponent exceeds 3; below that the global coefficient vanishes
at every temperature. Its reading is [NOTE-tmprov8v](../notes.d/NOTE-tmprov8v.md), skimmed: §1 read in
full, the theorems and the heuristic of §1.3 followed, the proofs of
§§2–8 not read.
