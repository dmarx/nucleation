---
status: Read
paper: 'LIT-tmpml2pq'
title: 'Chaves et al. — Bridging domains through subspace-aware model merging'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 from arXiv:2603.05768v2 (9 March 2026), from
    https://arxiv.org/pdf/2603.05768v2, 27 pp., text by pdftotext:
    §§1–5.2 in part, with the motivation (SAR, Fig. 2), SCORE (Alg. 1,
    Fig. 3), Table 1 and the first analyses. Skipped: the rest of §5.2
    (ablations), the conclusion and Appendices A2.x. The CVF open-access
    copy was located and not read. The filer rechecked every quotation
    below against the text, matching across column breaks, and rechecked
    the Table 1 and Fig. 2 figures.
date: '2026-11-15'
summary: >-
  Domain generalization by merging CLIP encoders fine-tuned on single
  source domains, leave-one-domain-out over eight benchmarks. Domain
  experts' task matrices overlap more in their singular subspaces than
  multi-task experts', which the paper calls stronger conflict. SCORE, a
  data-free shared-basis projection with trimmed off-diagonal couplings,
  edges TIES and TSV on average by under a point; task arithmetic at
  λ = 1 collapses below zero-shot.
---
<!-- inactive-ok-file: THEORY-107 CLAIM-498 — Proposed; held entries this reading bears on -->

# NOTE-tmpzye7e: Chaves et al. — Bridging domains through subspace-aware model merging

## Contribution

A leave-one-domain-out benchmark for model merging, the observation that
task matrices of domain experts share more singular subspace than those of
multi-task experts, and SCORE, a data-free merge that removes outlying
cross-couplings in a shared basis.

## Key insight

Models fine-tuned on different domains of the same task learn updates
along nearly the same singular directions. On the paper's reading, it is
that overlap, not difference, that makes their merge conflict, so the
merge should work in a basis they share and suppress the couplings that
stand out from it.

## Assumptions

- Every model starts from one pretrained CLIP encoder (ViT-B/32, B/16,
  L/14), each fine-tuned on one source domain; the label space is shared.
- No target-domain data, so λ = 1 for every method.
- High subspace overlap means conflict. This is argued and illustrated
  (Fig. 3), not isolated by an experiment in the sections read.

## Key results

- **Abstract.** "merging models trained under different distribution
  shifts induces stronger conflicts between their subspaces compared to
  traditional multi-task settings".
- **Motivation** (§3.2, Fig. 2). "Because these models solve similar
  classification problems, their delta weights tend to align along
  similar singular directions. This strong subspace overlap contrasts
  sharply with the diversity of multi-task learning." "This overlap leads
  to interference among singular directions during merging". Pairwise
  mean SAR is 0.61–0.71 among DomainNet domains and 0.41–0.69 among eight
  vision tasks, highest between related tasks such as MNIST and SVHN.
- **Method** (§4, Alg. 1). Concatenate the domains' top singular vectors,
  orthogonalize them into shared bases U⊥ and V⊥ as in TSV, project each
  task matrix, keep the diagonal and the off-diagonal entries beyond
  mean ± 1.96 SD, and sum.
- **Table 1** (eight benchmarks). ViT-B-32 average 65.69 for SCORE, 64.95
  for TSV, 64.84 for TIES, 61.31 for Iso-C, 55.63 zero-shot; ViT-L-14
  73.04 against 72.46 for TIES and 72.14 for TSV. Task arithmetic at λ = 1
  collapses below zero-shot: DomainNet 5.40 and ImageNet-R 4.65 on
  ViT-B-32, average 42.47.
- **Against ensembles** (§5.2). SCORE beats a logit ensemble of the same
  experts by 1.12 to 1.90 points on average.

## Concepts

Domain generalization by merging; leave-one-domain-out; subspace
alignment ratio (SAR); task matrix; shared orthogonal basis; diagonal
agreement and off-diagonal conflict; trimming at z = 1.96.

## Bearing on the record

- **[THEORY-107](../theory.d/THEORY-107.md) (interference in parameter coordinates)**: bears on its
  open point that "conflict frequency does not track cost". TIES finds
  sign conflicts as frequent within a task as across tasks; this paper
  finds the most subspace overlap among same-task experts, calls it
  conflict, and still merges them above zero-shot and above an ensemble.
  Sign disagreement per coordinate and overlap of singular subspaces are
  different measurements, and neither paper shows its measure causes the
  loss. Separately, task arithmetic at a fixed λ = 1 over three to five
  summed deltas collapses, while trimmed and normalized merges do not,
  which fits [THEORY-107](../theory.d/THEORY-107.md)'s finding that rescaling matters most; the paper
  does not test it.
- **[QUESTION-318](../questions.d/QUESTION-318.md), [CLAIM-498](../claims.d/CLAIM-498.md)**: indirect at most. These are many-model
  merges from one start, but no feature is measured.
- **[THEORY-112](../theory.d/THEORY-112.md), [CLAIM-407](../claims.d/CLAIM-407.md)**: no bearing.

## Connections

- **Zhang & Zhou (2025), [LIT-tmpwnkv8](../literature.d/LIT-tmpwnkv8.md) ([NOTE-tmpf8m60](NOTE-tmpf8m60.md))**, which the exchange
  joins to this paper, is about how one task's update acts on another
  task's inputs, in distribution. This paper is data-free and about the
  geometry of the updates alone. The exchange's sentence on parameters
  and data distributions is theirs, not this paper's.

## Limitations

- SCORE's lead over the next method is under a point on average, with no
  seeds or intervals in Table 1.
- λ = 1 for all methods penalizes task arithmetic, which is usually tuned.
- SAR is a proxy, and its link to accuracy is not tested causally.
- Image classification only.
- The ablations and appendices were not read.
