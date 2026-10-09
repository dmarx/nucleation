---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmpytz8j](../notes.d/NOTE-tmpytz8j.md)); worth reading as an early mechanistic account of when grokking networks generalise, in a toy model that sums two learned embeddings and decodes the sum. An unseen pair is predicted correctly when its embedding sum coincides with a trained pair''s (a "parallelogram"), and the critical training fraction is where the training set''s parallelogram equations first fix the embedding up to translation and scale. The account is exact for the toy (1D embeddings, addition hard-coded in the architecture, an effective loss posited and derived only for a linear decoder); the transformer and MNIST evidence is qualitative (PCA pictures and phase diagrams), and the four "phases" are defined by accuracy thresholds, not by any order parameter.'
title: 'Towards Understanding Grokking: An Effective Theory of Representation Learning'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed and read on 2026-10-09 at the owner's request (NOTE-tmpytz8j).
    Read in full from the arXiv PDF of v2 (14 Oct 2022, the NeurIPS 2022
    camera-ready, 29 pp.), text extracted with pdftotext: §§1–6, the
    checklist and Appendices A–L; figures read from captions, axis labels
    and the text. The v1 PDF (20 May 2022, 20 pp.) was compared section by
    section: v2 adds §4.3 and Appendices A, I, J, K and L (the phase
    table, the effective theory for image classification, MNIST grokking,
    the lottery-ticket projection and the derivation of the effective
    loss); the rest is the same apart from renumbering. Bibliography
    checked against the arXiv abstract page (six authors, v1 submitted
    20 May 2022, comment "Accepted by NeurIPS 2022"), Crossref (DOI
    10.52202/068431-2511, Advances in Neural Information Processing
    Systems 35, pp. 34651–34663, year only) and the NeurIPS proceedings
    page (Main Conference Track). `published:` is the arXiv v1 date,
    20 May 2022, the earliest date any source gives. Not held in
    nucleation before this filing: a grep of record/ for the title, the
    authors and the identifier found only a mention in NOTE-283 and a
    citation in NOTE-317. Not held in the Anthology of the SOTA as far
    as its clone shows: a grep of its record/ (clone of commit d8b5ba5,
    9 Oct 2026, possibly stale) for the arXiv id, the title and Kitouni
    found nothing. The anthology holds the follow-up, Omnigrok
    (ANTH-LIT-540), and the grokking line around it.
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-10-09'
published: '2022-05-20'
arxiv: '2205.10343'
first_author: 'Liu'
keywords:
- 'grokking'
- 'effective theory'
- 'representation learning'
- 'phase diagram'
- 'delayed generalization'
- 'representation quality index'
- 'Goldilocks zone'
implementations:
- 'https://github.com/ejmichaud/grokking-squared'
summary: >-
  Liu, Kitouni, Nolte, Michaud, Tegmark and Williams (2022), NeurIPS 2022.
  In a toy model that decodes the sum of two learned embeddings, grokking
  is representation learning: an unseen pair is answered correctly when its
  embedding sum equals a trained pair's, and the critical training fraction
  (about 0.4 for addition with p = 10) is where the training set's
  "parallelogram" equations first fix the embedding up to translation and
  scale. A posited effective loss on the normalised embeddings predicts
  that threshold and, through its third Hessian eigenvalue, the time to
  structure. Phase diagrams over decoder learning rate and weight decay
  place grokking between comprehension and memorization in the toy, a
  transformer and MNIST.
---

<!-- inactive-ok-file: THEORY-tmps9ng8 — Proposed; the THEORY this reading produced -->
<!-- inactive-ok-file: THEORY-022 — Proposed; named as the record's account of the modular-addition circuit that this paper's circle pictures precede -->

# LIT-tmptf5mc: Towards Understanding Grokking: An Effective Theory of Representation Learning

Ziming Liu, Ouail Kitouni, Niklas Nolte, Eric J. Michaud, Max Tegmark and
Mike Williams (2022), *Advances in Neural Information Processing Systems 35*
(NeurIPS 2022), pp. 34651–34663 — [ARXIV-2205.10343](https://arxiv.org/abs/2205.10343); DOI-10.52202/068431-2511

## Key takeaways

- **Generalisation from parallelograms.** The toy model is
  (a, b) ↦ Dec(E_a + E_b). If training loss is zero and the decoder is
  injective, every pair of training samples with the same answer forces
  E_i + E_j = E_m + E_n (Proposition 2), and any such coincidence must
  respect the arithmetic (Proposition 1). An unseen pair is then answered
  correctly when its sum coincides with a trained pair's. The fraction of
  permissible parallelograms realised, the representation quality index
  (RQI), predicts accuracy closely for 1D embeddings (Fig. 3).
- **The critical training fraction is linear algebra on the dataset.** The
  parallelogram equations a training set implies have a null space of
  dimension at least 2 (translation and scale). When it is exactly 2, the
  representation is forced to E_k = a + kb. For addition with p = 10 the
  probability of that jumps near a training fraction of 0.4, matching the
  empirical steps-to-RQI > 0.95 (Fig. 4) and Power et al.'s critical
  fraction ([LIT-341](LIT-341.md)). For S₃ with matrix embeddings it is near 0.5.
- **An effective loss.** The normalised embeddings are modelled as
  gradient flow on ℓ_eff = ℓ₀/Z₀, the mean squared parallelogram defect
  over the training set divided by Σ|E_k|². It conserves Σ E_k and Z₀
  (proved, App. F), so it cannot collapse. Its dynamics are linear, and
  1/λ₃, the third Hessian eigenvalue, sets the time to structure: zero
  below the critical fraction, growing with data above it (Fig. 5). It is
  posited, and derived (App. L) only for a linear decoder in the limit of a
  frozen decoder.
- **Four phases.** Comprehension, grokking, memorization and confusion are
  defined by thresholds: 90% train and validation accuracy within 10⁵
  steps, and a gap of under 10³ steps between them. Over decoder learning
  rate and weight decay, grokking sits between comprehension and
  memorization in three toy tasks, a transformer on addition mod 53 and an
  MLP on a 1,000-sample subset of MNIST. Generalisation needs the
  representation to learn faster than the decoder, but not much faster.
- **Beyond the toy, pictures.** In the transformer, generalisation
  coincides with a circle in the first two principal components of the
  embeddings (Fig. 1) and with a fall in the entropy of the PCA spectrum.
  Decoder weight decay and dropout shorten or remove the delay. MNIST
  grokking needs a reduced training set and an enlarged initialisation
  (v2 only; it appears after the authors' Omnigrok, [ANTH-LIT-540](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-540.md)).

## Standing in the record

Filed on 2026-10-09 at the owner's request. It came in a batch with arXiv
2509.24914, 2502.09863, 2504.12916 and 2410.17770, with no stated context,
and it is read here on its own merits.

Read on 2026-10-09 ([NOTE-tmpytz8j](../notes.d/NOTE-tmpytz8j.md)). The reading is the source of
[THEORY-tmps9ng8](../theory.d/THEORY-tmps9ng8.md), the record's statement of when a training set fixes the
generalising representation in this toy. It is the earliest grokking paper
in the record to find the circle in modular-addition embeddings, which
[THEORY-022](../theory.d/THEORY-022.md) states from Nanda et al. ([LIT-345](LIT-345.md)). The founding experiment is
Power et al. ([LIT-341](LIT-341.md)).

It carries `anthology-candidate`: its subject is the training dynamics of
neural networks, and its phase diagrams are about which hyperparameters
remove the delay, which is ML practice. The anthology holds the follow-up,
Omnigrok ([ANTH-LIT-540](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-540.md)), and the grokking line around [ANTH-THEORY-069](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-069.md), but
not this paper as far as its clone of commit d8b5ba5 shows; that clone may
be stale.
