---
status: Active
status_note: 'read 2026-10-16 ([NOTE-tmpetxcq](../notes.d/NOTE-tmpetxcq.md)) in full; worth reading as the place where Bourgain''s O(log n) embedding of finite metrics into Euclidean space is restated, reproved by distances to random sets of every scale, and shown tight: constant-degree expanders need distortion Ω(log n) in ℓ_p, 1 ≤ p ≤ 2, of any dimension, because their gap between multicommodity flow and cut is Ω(log n). The same embeddings bound that gap by O(log k) for k commodities. Read it knowing that the O(log n) dimension comes from Johnson–Lindenstrauss, not from the construction, which uses O(log² n) coordinates; that the lower bound rests on Leighton and Rao''s gap, cited; that constants are unspecified; and that it says nothing about trees in ℓ₂, for which Sala et al. cite it. Filed as [THEORY-tmpbseab](../theory.d/THEORY-tmpbseab.md).'
title: 'The geometry of graphs and some of its algorithmic applications'
version: 2
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Filed at the owner's request as later work flagged by the reading of
    Johnson and Lindenstrauss (NOTE-tmpmv42v), whose Connections name it as
    unchecked. Citation checked against Crossref on 2026-10-16.
    Not held in the Anthology of the SOTA: a grep of its record/ (clone pulled 2026-10-16) for the authors' names and the identifiers found nothing. Crossref gives June 1995 and no day; a conference version appeared at FOCS 1994 (doi:10.1109/SFCS.1994.365733).
- version: 2
  date: '2026-10-16'
  note: >-
    Read in full (NOTE-tmpetxcq) from the authors' 26-page manuscript, "the
    final version of February 1995", hosted on a Michigan State University
    course page; it is not the journal's typeset text, which runs 31
    pages. Text extracted with pdftotext -layout and the mathematics read
    from page images. The takeaways from citing works are replaced with
    the reading, the summary is rewritten from it, the status moved from
    Deferred to Active, and Standing in the record names NOTE-tmpetxcq and
    THEORY-tmpbseab. One takeaway was imprecise: the O(log² n) dimension is
    that of the random construction (Theorem 3.2(5)); for ℓ₂ the paper
    states O(log n), by adding Johnson–Lindenstrauss. The expander bound
    covers ℓ_p for 1 ≤ p ≤ 2, not only ℓ₂. The keyword "sparsest cut"
    names the cut of Theorem 4.1, which minimizes capacity over demand;
    the paper does not use the phrase. The bibliographic data and tags
    were found correct.
tags:
- mathematics
- operations-research
date: '2026-10-16'
published: '1995-06-01'
doi: '10.1007/BF01200757'
first_author: 'Linial'
keywords:
- 'metric embeddings'
- 'distortion'
- 'graphs'
- 'expanders'
- 'multicommodity flow'
- 'sparsest cut'
extends:
- LIT-tmpwy0he
implementations: []
summary: >-
  Linial, London & Rabinovich (1995), *Combinatorica* 15(2): 215–245. Every
  n-point metric embeds in O(log n)-dimensional Euclidean space with
  distortion O(log n) (Bourgain's theorem as Theorem 3.2(1) states it).
  The paper reproves the distortion by a randomized map to distances from
  O(log² n) random sets, takes the dimension from Johnson–Lindenstrauss,
  and computes the least Euclidean distortion of any finite metric by
  semidefinite programming. Constant-degree expanders need distortion
  Ω(log n) in ℓ_p, 1 ≤ p ≤ 2, of any dimension (Proposition 4.2), so the
  bound is tight. The max-flow/min-cut gap for k commodities is O(log k),
  with a deterministic algorithm (Theorem 4.1).
---
<!-- inactive-ok-file: LIT-tmpwy0he — Unavailable; Bourgain's paper, which this one restates and extends -->

# LIT-tmp9g20z: The geometry of graphs and some of its algorithmic applications

Nathan Linial, Eran London and Yuri Rabinovich (1995), "The geometry of graphs and some of its algorithmic applications", *Combinatorica* 15(2): 215–245 — [doi:10.1007/BF01200757](https://doi.org/10.1007/BF01200757)

## Key takeaways

*From the reading, [NOTE-tmpetxcq](../notes.d/NOTE-tmpetxcq.md).*

- **Bourgain's theorem as stated (Theorem 3.2(1)).** "Every n-point
  metric space (X, d) can be embedded in an O(log n)-dimensional Euclidean
  space with an O(log n) distortion."
- **Reproved and made algorithmic (Claim 5).** Distances to O(log n)
  random sets of each size 2ˡ, O(log² n) coordinates in all, give
  distortion O(log n) in ℓ_p for any p ≥ 1, in random polynomial time.
  Johnson–Lindenstrauss (Theorem 3.1, quoted as t = O(log n/ε²)) brings
  ℓ₂ down to O(log n) dimensions.
- **Least distortion computable (Claim 2, Corollary 3.5).** c₂(X) is found
  to within any ε by semidefinite programming, with a dual
  characterization over positive semidefinite Q with Q·1⃗ = 0⃗.
- **Tight (Proposition 4.2).** Every embedding of a constant-degree
  expander into ℓ_p, 1 ≤ p ≤ 2, of any dimension, has distortion
  Ω(log n). Constant distortion in any norm needs Ω(log² n) dimensions.
  The proof uses Leighton and Rao's Ω(log n) flow–cut gap.
- **Multicommodity flow (Theorem 4.1).** The flow–cut gap is at most the
  ℓ₁ distortion of the LP-optimal metric, so O(log k) for k commodities,
  with a deterministic algorithm for the cut.
- **Isometric dimension (§5).** Trees O(log n), tight; dim(Kₙ) =
  ⌈log₂ n⌉; dim(C₂ₘ) = m; dim(m-cube) = m. Separators (Theorem 6.1) and
  low-diameter decompositions (Theorem 7.1) for low-dimensional graphs.
- **Scope.** Constants unspecified; the paper cites neither Johnson and
  Lindenstrauss's Problem 4 nor any Euclidean lower bound for trees.

## Standing in the record

Filed on 2026-10-16 as later work flagged by [NOTE-tmpmv42v](../notes.d/NOTE-tmpmv42v.md) and cited,
unread, by [NOTE-679](../notes.d/NOTE-679.md) and [NOTE-905](../notes.d/NOTE-905.md), and read the same day in
[NOTE-tmpetxcq](../notes.d/NOTE-tmpetxcq.md). It is how the record reads Bourgain's theorem
([LIT-tmpwy0he](LIT-tmpwy0he.md)) until a copy of that paper is supplied. Filed as
[THEORY-tmpbseab](../theory.d/THEORY-tmpbseab.md).

The reading confirms [NOTE-tmpmv42v](../notes.d/NOTE-tmpmv42v.md)'s unchecked remark as far as this
paper goes. It states Bourgain's O(log n), and it shows that expanders
need Ω(log n) in ℓ₂. The step to Johnson and Lindenstrauss's Problem 4,
answered in the negative, is the record's inference, since the paper does
not mention the problem. It also confirms [NOTE-905](../notes.d/NOTE-905.md)'s Fact 4, the
embedding of integer ℓ₁ into Hamming space (Corollary 3.8's proof).

It does not support [NOTE-679](../notes.d/NOTE-679.md)'s citation. Sala et al. cite it as
"Bourgain's theorem" for the claim that Euclidean space cannot embed
trees with low distortion in any dimension. The paper's Bourgain theorem
is an upper bound, its lower bound is for expanders, and its tree result
is an isometric embedding in ℓ∞.

`operations-research` is for the multicommodity flow and cut results. The
clustering remark in §3.2 is not an instruction for machine-learning
practice, and the paper is held here only.
