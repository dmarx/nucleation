---
number: 574
status: Active
formerly:
- THEORY-tmpljwz3
title: "The structural width of Xin Li's learning programme is a covering number of the margin-safe region by local pieces: its lower bounds come from metric confinement through a wedge point, not from topology, labels enter only through the margin, and the error floor below width binds only learners assembled from local experts, so it does not entail routing, nor training routing apart from the task loss"
version: 1
tags:
- learning-theory
- mathematics
date: '2026-10-16'
source:
- LIT-376
- LIT-375
- LIT-374
summary: >-
  Li (2026), [LIT-376](../literature.d/LIT-376.md) (Local Urysohn Width, v1), [LIT-375](../literature.d/LIT-375.md) (Structural
  Learning Theory) and [LIT-374](../literature.d/LIT-374.md) (Structural Decoupling), read jointly in
  [NOTE-323](../notes.d/NOTE-323.md), [NOTE-324](../notes.d/NOTE-324.md) and [NOTE-322](../notes.d/NOTE-322.md). In repaired form the formal core holds:
  width is incomparable with the per-cell VC dimension, fewer cells than
  width give an error floor (under an assumption that states it), and
  discovering all basins costs Ω(w log w) samples. But local correctness is
  automatic on any connected patch, the bouquet lower bound is metric (the
  paper's Remark 8.11 concedes it), a global classifier has width 1 (Remark
  3.4), and the additive Rademacher bound said to call for decoupled
  training holds for joint training too.
---
<!-- inactive-ok-file: LIT-374 LIT-375 LIT-376 — Proposed; the programme this account reads, cited for what its proofs show, which is the account, and for what they do not -->
<!-- inactive-ok-file: LIT-373 — Rejected; the programme's informal origin, named, not leaned on -->
<!-- inactive-ok-file: THEORY-019 THEORY-039 — Proposed; neighbouring accounts named in Connections, not leaned on -->

# THEORY-574: The structural width of Xin Li's learning programme is a covering number of the margin-safe region by local pieces: its lower bounds come from metric confinement through a wedge point, not from topology, labels enter only through the margin, and the error floor below width binds only learners assembled from local experts, so it does not entail routing, nor training routing apart from the task loss

## Source

Three papers by Xin Li (2026), read together on 2026-10-01 as one
programme, at the owner's request and charitably:

- *Local Urysohn Width* (arXiv 2603.15412 v1), [LIT-376](../literature.d/LIT-376.md), read in [NOTE-323](../notes.d/NOTE-323.md):
  the first definition of width and its cleanest proofs.
- *Structural Learning Theory* (arXiv 2602.07974 v2), [LIT-375](../literature.d/LIT-375.md), read in
  [NOTE-324](../notes.d/NOTE-324.md): width for contractive cells with a risk bound, the error floor,
  the spectral estimator.
- *Structural Decoupling* (arXiv 2506.20699 v2), [LIT-374](../literature.d/LIT-374.md), read in [NOTE-322](../notes.d/NOTE-322.md)
  with a joint re-reading: the additive bound and the decoupling
  prescription.

## What was actually shown

**Width as defined first ([LIT-376](../literature.d/LIT-376.md)).** For a margin-γ problem, the safe
region is the union of the γ/2-neighbourhoods of the class sets. Local
Urysohn width is the least number of connected sets of diameter ≤ D₀, each
carrying a continuous classifier correct on the safe region it meets,
needed to cover the safe region (Defs 3.2–3.3). On a bouquet of w circles
with safe balls at the antipodes, width is exactly w when
3γ/2 ≤ D₀ < L/2 − 3γ/4 (Thm 4.1); with m balls per loop it is at least wm,
so Ω(w·L/D₀) (Cor 5.1). Width and VC dimension do not determine each other
(Thm 6.1). Ω(w log w) samples are needed (Thm 7.1, coupon collector). The
proofs are correct ([NOTE-323](../notes.d/NOTE-323.md)).

**Why it is a covering number.** Class safe regions are closed and more
than γ apart, so on any connected patch Urysohn's lemma supplies a
correct continuous classifier. Local correctness is automatic, and width
is the least number of connected D₀-diameter sets covering the safe region:
labels enter only through γ ([NOTE-323](../notes.d/NOTE-323.md), C6). The bouquet lower bound uses
only geodesic distance through the wedge point; Remark 8.11 says the
obstruction "is metric (diameter bound) rather than cohomological". The
same argument gives width w on a star-shaped tree with w arms, where β₁ = 0.
The bouquet's safe region is disjoint arcs, so it does not meet the
homological condition of the Betti bound (Thm 8.5), and the general Betti
bound is a conjecture (Conj 8.9).

**The contractive-cell version ([LIT-375](../literature.d/LIT-375.md), [LIT-374](../literature.d/LIT-374.md)).** Width is redefined
as the least open cover by cells on each of which some predictor is
γ-contractive with risk ≤ δ. Below width there is an n-independent error
floor η(w, K) under Assumption 2.3, which states that any K-cell cover
mixing two basins has excess risk ≥ η (Thm 2.4). That is close to
definitional. The spectral estimator converges to a count relative to a
given predictor, not to width (Thm 3.5). The bound
R̂ ≤ √(2 log Δ_str(n)/n) + LK·R̂_n(G) for routed predictors holds, with a
fixable gap in its proof ([LIT-374](../literature.d/LIT-374.md), Thm 4.5).

**What could have come out otherwise.** The bouquet bound could have used
the loops' homology. It uses distance only.

## What this does not say

- **That topology forces classifier complexity.** The abstract and §10 of
  [LIT-376](../literature.d/LIT-376.md) say so; the proof is metric confinement, as the paper concedes.
- **That a monolithic model needs w experts.** Remark 3.4 of [LIT-376](../literature.d/LIT-376.md):
  a single global Urysohn function makes every margin problem width 1.
  "Any system that maintains fewer than uw experts cannot correctly
  classify" (§9) restates the definition's locality constraint. The
  question whether a capacity-matched monolithic network shows the floor
  is open ([NOTE-324](../notes.d/NOTE-324.md)).
- **That routing should be trained apart from the task loss.** [LIT-374](../literature.d/LIT-374.md)
  reads the additivity of an upper bound as a rule that its two terms be
  reduced by separate mechanisms on separate signals (Prop 4.7, §4.2).
  The bound holds for joint training too, and an upper bound's form does
  not fix the error's.
- **That width is estimated.** The contractive-similarity Laplacian counts
  prediction discontinuities of a fixed predictor, w_G(P), and no result
  ties that to width ([NOTE-324](../notes.d/NOTE-324.md), C6).
- **That the alignment section follows.** [LIT-374](../literature.d/LIT-374.md)'s recasting of
  alignment as scaffold alignment is asserted, with internal
  contradictions.

## Connections

- **[LIT-373](../literature.d/LIT-373.md)** ("The two dragons of cognition", Rejected) is the
  programme's informal origin. [LIT-376](../literature.d/LIT-376.md) concedes the global-Urysohn
  triviality that [LIT-373](../literature.d/LIT-373.md)'s linear-readout claim missed; none of the three
  papers repairs [LIT-373](../literature.d/LIT-373.md)'s other grounds ([NOTE-322](../notes.d/NOTE-322.md)).
- **[THEORY-028](THEORY-028.md).** Every guarantee here is class-level or assumes correct
  routing. A claim about which gradients should update which parameters
  would need algorithm-dependent analysis of that account's kind, and the
  programme has none.
- **[THEORY-019](THEORY-019.md).** The spectral estimator reads structure from eigenvalue
  multiplicity at zero, which counts components, not a group; consistent
  with that account's point that multiplicities carry dimension counts.
- **[THEORY-039](THEORY-039.md).** [LIT-374](../literature.d/LIT-374.md) identifies grokking with a width transition by
  shape only, which that account warns against.
