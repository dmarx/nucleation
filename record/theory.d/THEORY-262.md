---
number: 262
status: Proposed
formerly:
- THEORY-tmpficjv
promote_when: >-
  Two results, one per clause. For the two-extremes clause: a proof, or a
  check across more than one family of covariance matrices, that C_N
  vanishes at independence and falls toward its floor as all
  correlations approach one, at fixed n. A second worked example from the
  same Toeplitz family does not count. For the connectivity clause: the
  ordering patchy > uniform at equal number and strength of connections,
  reproduced in an independent simulation or in recorded activity, with
  C_N normalised for n and I and with more than one realisation per
  connectivity pattern. It is refuted by a matched comparison in which
  uniform intergroup wiring gives C_N at least as high as patchy wiring.
  High C_N in recorded brains with no matched connectivity contrast
  cannot settle the connectivity clause.
title: "Neural complexity is low when a system's parts are independent or uniformly dependent and high when small subsets are nearly independent while large ones are integrated; in simulated cortex, patchy grouped connectivity raises it above random connectivity of equal density"
version: 1
tags:
- neuroscience
- information-theory
- complex-systems
date: '2026-10-14'
source:
- LIT-998
summary: >-
  Tononi, Sporns & Edelman (1994), [LIT-998](../literature.d/LIT-998.md), read in [NOTE-767](../notes.d/NOTE-767.md).
  C_N, the summed shortfall of average subset integration below a linear
  rise with subset size, is shown low at both extremes for one family of
  Gaussian matrices, and higher for patchy than for uniform wiring in one
  simulated visual area and in small linear systems. All of it is
  simulation. It is a whole-system number over fixed components: it does
  not find units or boundaries.
---
<!-- inactive-ok-file: CLAIM-157 THEORY-097 THEORY-063 — Proposed; the block criterion and the block-duration finding this measure is compared with, and the dynamic-core account named for lineage -->

# THEORY-262: Neural complexity is low when a system's parts are independent or uniformly dependent and high when small subsets are nearly independent while large ones are integrated; in simulated cortex, patchy grouped connectivity raises it above random connectivity of equal density

## Source

Tononi, Sporns & Edelman (1994), *PNAS* 91:5033–5037, [LIT-998](../literature.d/LIT-998.md), read in
full in [NOTE-767](../notes.d/NOTE-767.md): Theory (Eqs. 1–6), Results (Figs. 1–3) and
Discussion.

## What was actually shown

**The measure.** For a system X of n components with stationary activity,
integration is I(X) = Σᵢ H(xᵢ) − H(X). Its average ⟨I(X_j^k)⟩ over all
subsets of size k rises monotonically from 0 at k = 1 to I(X) at k = n
(from Eq. 3). Neural complexity is

C_N(X) = Σ_{k=1}^{n} [(k/n) I(X) − ⟨I(X_j^k)⟩] = Σ_{k=1}^{n/2} ⟨MI(X_j^k; X − X_j^k)⟩,

the shortfall below the linear rise, equivalently the average mutual
information between a subset and the rest, summed over sizes (Eqs. 4, 6).
C_N ≥ 0. For Gaussian activity, I(X) = −ln|CORR(X)|/2.

**The two extremes (Fig. 1).** Toeplitz covariance matrices, n = 64, with
correlation length varied from near-independence to all coefficients near
one. C_N is very low at both ends and maximal when the coefficients span
the whole range from 0 to 1, though I keeps rising. This could have come
out otherwise: C_N could have tracked I.

**Connectivity (Fig. 2).** In a simulated primary visual area (512
neuronal groups, intrinsic Gaussian noise, no input), the patchy pattern
modelled on cortex gave C_N = 2244.7. The same number and strength of
intergroup connections spread uniformly gave a higher I(X), a globally
synchronised state, and C_N = 1240.2. Halving the density of the patchy
pattern gave C_N = 542.35. In small linear systems (n = 8, fixed total
weight), concentrating connections on fewer partners raised C_N/I
(Fig. 3A, 1,000 networks per point). At constant I, more reciprocal pairs
tended to go with higher C_N (Fig. 3B, 10,000 networks).

## What this does not say

- **It does not say the brain has high C_N.** Nothing was recorded. The
  authors' claim that neuroimaging covariance shows high C_N rests on
  unpublished data, and the prediction about waking and slow-wave sleep is
  a prediction.
- **It does not prove the two-extremes property.** It is shown for one
  family of matrices. At independence C_N is zero by definition; "low"
  at full dependence is shown, not derived.
- **It does not find units.** C_N is one number for a system whose
  components are fixed in advance. It names no boundary, block or scale,
  and it has no threshold or penalty for estimating structure from
  finite data. So it does not compete with a gap-and-Occam block test
  ([CLAIM-154](../claims.d/CLAIM-154.md), [CLAIM-157](../claims.d/CLAIM-157.md)) as a way to pick out a unit. It only says that
  grouped, patchy structure raises the score.
- **It does not say high complexity is consciousness.** The Discussion
  links C_N to "conscious perception and behavior" only as a hypothesis
  for later work, and conditionally on extending the measure to
  nonstationary activity.
- **The connectivity results are single realisations** (Fig. 2) or
  tendencies (Fig. 3B), and two effects (grouping, reciprocity at lower w)
  are "data not shown".

## Connections

- **[QUESTION-042](../questions.d/QUESTION-042.md)** asks whether blocks that clear an Occam-priced test
  fall at anatomical boundaries in a recorded brain. This account does not
  answer it, and no `answers:` is declared. It supplies the comparison the
  question was given [LIT-998](../literature.d/LIT-998.md) for. The paper treats a system as one only
  if "no bipartition yields two statistically independent subsets", which
  is a oneness test with a zero threshold. [CLAIM-157](../claims.d/CLAIM-157.md)'s gap-beats-Occam
  criterion is the priced version of the same idea.
- **[THEORY-097](THEORY-097.md)** puts long-range blocks at about 70 ms. A stationary
  measure like C_N cannot see a block that short.
- **[THEORY-063](THEORY-063.md)** cites Tononi and Edelman's later dynamic core ("maximal
  causal density", "distinct functional borders"). That is the descendant
  that adds a border. Nothing there rests on this paper.
