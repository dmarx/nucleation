---
number: 2
status: Proposed
formerly:
- THEORY-tmp4sf4k
promote_when: >-
  A proved stability result linking a distributional distance to a Bures
  distance between the centred kernels of the representations themselves,
  for a model family that includes contrastive or language-model
  objectives, or a measurement showing whether model pairs with high
  mutual-nearest-neighbour alignment also have high Bures alignment of their
  centred kernels. A result in CKA does not count by itself, since CKA and
  normalized Bures similarity bound each other only within a rank-dependent
  factor (LIT-250 eq. 24; THEORY-tmpip5os). Nielsen et al.'s Thm 4.7 (LIT-253) is a proved
  stability result of this kind for softmax models, and by an identity
  NOTE-tmp6dvmv derived and checked by script, but which the paper does not
  state, its d_SVD is 1 − NBS. What remains: that kernel is of the
  per-coordinate standardized log-odds coordinates Lᵀf(x), which depend on
  a pivot label and label set, not of the embedding f(x) itself; the record
  has not decided that a Bures-type quantity on those coordinates counts;
  and the identity is the reader's, not a proved statement of the source.
title: 'Convergence of representations, in the Platonic hypothesis''s sense, is convergence of kernels, which fixes representations only up to the symmetry group of what is observed; whether closeness in distribution implies closeness of representation depends on the distance used'
version: 4
history:
- version: 2
  date: '2026-10-05'
  note: >-
    `extends: THEORY-004` re-filed as `presupposes: THEORY-004` (ADR-029),
    and a Connections section added saying what is taken from it. The kernel
    result is a premise for a claim about what the Platonic hypothesis can
    mean.
- version: 3
  date: '2026-10-14'
  note: >-
    After the close readings NOTE-tmp6dvmv (LIT-253) and NOTE-tmpx7mtu
    (LIT-250). The title's last clause, "closeness in distribution does not
    imply closeness of representation", held only for KL divergence;
    LIT-253 proves the converse for its d_LLV distance (Thm 4.7) and
    concludes that the answer depends on the distance. Title and body now
    say so, Thm 4.7 is added to the Source section, and the KL
    counterexample is qualified: it needs the unembedding norm to grow
    without bound, the size of the dissimilarity is shown only numerically,
    and only the final embedding and unembedding are covered. Applying it
    to the Platonic hypothesis is marked as this record's inference. The
    promote_when no longer treats Bures and CKA as interchangeable
    (LIT-250 eq. 24), and records that Thm 4.7 meets it only in part, so
    the status stays Proposed. Stale Deferred comments for LIT-253 and
    LIT-250 removed.
- version: 4
  date: '2026-10-14'
  note: >-
    The promote_when's remark that a CKA result does not count by itself
    now cites THEORY-tmpip5os, the account of LIT-250 eq. 24 filed today.
tags:
- representation-learning
- philosophy-of-science
date: '2026-09-26'
source:
- LIT-253
- LIT-250
summary: >-
  An inference joining Huh et al.'s Platonic hypothesis ([ANTH-LIT-458](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-458.md)) to
  Nielsen et al. ([LIT-253](../literature.d/LIT-253.md)) and Harvey, Larsen & Williams ([LIT-250](../literature.d/LIT-250.md)).
  It does not refute the hypothesis; it says what the hypothesis can and
  cannot mean.
presupposes:
- THEORY-004
supports:
- CLAIM-193
- CLAIM-269
---
<!-- inactive-ok-file: THEORY-004 — Proposed; the kernel result this account presupposes, and this account is no firmer than it -->
<!-- inactive-ok-file: THEORY-tmpip5os — Proposed; cited in promote_when as the reason a CKA result does not count, not leaned on -->

# THEORY-002: Convergence of representations, in the Platonic hypothesis's sense, is convergence of kernels, which fixes representations only up to the symmetry group of what is observed; whether closeness in distribution implies closeness of representation depends on the distance used

## Source

Nielsen et al. (2025), [LIT-253](../literature.d/LIT-253.md), Thm 2.2, Thm 3.1, Cor. 3.2, Thm 4.7, as read in [NOTE-tmp6dvmv](../notes.d/NOTE-tmp6dvmv.md); Harvey, Larsen & Williams (2023), [LIT-250](../literature.d/LIT-250.md), Thm 1 and eq. 24, as read in [NOTE-tmpx7mtu](../notes.d/NOTE-tmpx7mtu.md). The hypothesis itself is Huh et al. (2024), [ANTH-LIT-458](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-458.md), §4.2 and App. A.

## What was actually shown

Huh et al. ([ANTH-LIT-458](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-458.md), §4.2) prove that, under bijective observations and an NCE objective, representations converge to the PMI kernel up to an offset — the log of the density ratio K⁺ that the contrastive losses target (see the first claim in this group). Their measurements, though, use mutual nearest neighbours (App. A), which is much weaker than kernel equality. Nielsen et al. show that for softmax models the output distribution fixes the embeddings only up to an invertible linear map, not an orthogonal one (Thm 2.2, cited from earlier work), and that ε-closeness in KL does not bound representational dissimilarity (Thm 3.1, Cor. 3.2). That counterexample needs the unembedding norm to grow without bound, so that both softmaxes saturate, and the theorem proves only that the embeddings are not related by an invertible linear map; how far apart they are is shown numerically (Table 1). Under a different distance the answer reverses: closeness in their log-likelihood variance distance bounds a representational dissimilarity, d_LLV ≤ ε ⇒ d_f,g ≤ 2Mε (Thm 4.7), and the paper's stated conclusion is that the answer "depends critically on the choice of distributional and representational distance". All of this concerns the final embedding and the unembedding only; the paper says earlier layers would need identifiability results that do not yet exist (§6). Harvey, Larsen & Williams supply the kernel-side metric under which kernel closeness is rotation-aligned closeness, for centred linear kernels.

Nielsen et al. cite the Platonic hypothesis only as evidence that learned representations are robust, and do not argue against it. Reading their KL result as a caution for the hypothesis is this record's inference, and it reaches the hypothesis's kernels, which are pooled hidden states, only by analogy.

Read together: the defensible formal content of "representations converge" is that kernels converge, and the representation is then fixed only up to the symmetry group of the observed quantity — orthogonal if the kernel is observed, general linear if only the distribution is.

## What this does not say

- That the Platonic hypothesis is false.
- That trained models do, or do not, converge in kernel.
- That any one metric (Bures, CKA, mutual nearest neighbours) is the right one.
- That closeness in distribution never bounds representational dissimilarity. It fails for KL in the saturation regime and holds for d_LLV ([LIT-253](../literature.d/LIT-253.md), Thm 4.7).

## Connections

- **Presupposes [THEORY-004](THEORY-004.md).** That account shows that a representation is
  fixed by its centred kernel up to a translation and an orthogonal
  transformation. This one takes
  that as the premise that lets convergence of kernels count as
  convergence of representations up to rotation, and asks what the
  Platonic hypothesis can then mean.
