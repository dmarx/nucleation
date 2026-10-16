---
number: 742
status: Read
formerly:
- NOTE-tmpftody
paper: LIT-245
title: 'Sefidgaran, Zaidi & Krasnowski — MDL and Generalization Guarantees for Representation Learning'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read from the arXiv v1 PDF (arxiv.org/pdf/2402.03254, 38 pp., the
    NeurIPS 2023 paper with its supplement), text extracted with
    pdftotext. Read in full: §§1–5 and Appendices A (tail bounds,
    Theorems 5–7), B (Blum–Langford; the critique of Kawaguchi et al.),
    C (the compressibility framework, h_D, geometric compression, future
    work) and D (the experiments). Of the proofs (App. E), E.1 (general
    technique) and E.5 (Theorem 4, the main result) were read. The proofs
    of Theorems 1–3 and 5–7 and Lemmas 1–3 (E.2–E.4, E.6–E.9) were not
    checked line by line. The skim note filed with the paper is NOTE-207.
date: '2026-10-14'
summary: >-
  The expected generalisation error of an encoder–decoder classifier is
  bounded by 2√((2·MDL + K + 2)/n) + ε, where MDL is a KL divergence
  between the encoder's joint law of train-and-ghost latents and a prior
  symmetric under label-preserving permutations. The bound holds for any
  decoder, stays finite for deterministic continuous encoders under lossy
  compression, and is never evaluated numerically. A VIB variant with
  label-dependent learned priors gains about 2.5 points on CIFAR-10.
---
<!-- inactive-ok-file: THEORY-035 — Rejected; the account whose Connections names this paper -->
<!-- inactive-ok-file: LIT-240 — Unavailable; Vera et al., whose bound this paper calls vacuous -->

# NOTE-742: Sefidgaran, Zaidi & Krasnowski — MDL and Generalization Guarantees for Representation Learning

## Contribution

The paper adapts Blum and Langford's PAC-MDL argument to block coding
and lossy compression. With it, it bounds the generalisation error of a
two-step (encoder, then decoder) learner by a complexity of the encoder's
latents alone. That complexity is a "multi-letter" KL divergence between
the law of the latents of a training set and a ghost set and a symmetric
prior, not I(X;U). It also shows that the label-prediction version of the
framework contains the f-CMI bound and recovers the VC bound. On that
basis it proposes data-dependent priors as a replacement for VIB's
standard Gaussian.

## Key insight

What controls generalisation is how few codewords suffice to cover the
joint sequence of latents of train and test samples. Covering is
measured against a prior that cannot tell train from test. Sample-wise
mutual information is that measure for a product prior and ignores the
encoder's structure. A prior that is symmetric only within each label
lets the measure see clustering by class, and it is finite for
deterministic encoders once small distortions are allowed.

## Assumptions

- **K-class classification with the 0–1 loss** (extended "trivially" to
  bounded losses). The ghost set S′ is drawn i.i.d. from the same
  distribution as S, with |S| = |S′| = n.
- **The prior's symmetry.**
  - *Type I:* invariant to swapping i and i + n.
  - *Type II:* invariant to any permutation of the 2n positions.
  - *Type III:* invariant to permutations that preserve labels,
    y_π(i) = y_i.
  Theorem 4 needs type III. The prior may depend on (X^{2n}, Y^{2n}) and
  on the compressed encoder, and so on the unseen ghost data.
- **Lossy version.** The infimum runs over Markov kernels P_{Ŵe|S} with
  E[gen(S,W) − gen(S,Ŵ)] ≤ ε.
- **Theorem 3 needs n ≥ 10.** The proof of Theorem 4 uses Lemma 3, stated
  for λ/n < 0.68, but applies it "conditioned that λ/n < 1.36". This
  looks like an internal inconsistency in the constants.

## Key results

- **Theorem 1 (type I, predicted labels).** E[gen(S,W)] ≤ √(2R/n) with
  R ≤ inf_{Q∈Q_i} E D_KL(E P^{⊗2n}(Ŷ,Ŷ′|X,X′,W) ‖ Q) = I(J; Ŷ^{2n} | Y^{2n}).
  Part ii is a tail bound with
  √((4/(2n−1))(D_KL(·‖Q) + log(√(2n)/δ))). The paper reads part i as an
  f-CMI bound that conditions on Y^{2n} only.
- **Relation to mutual information (Eqs. 3–4).** With the product prior
  Q^{⊗2n}, the right-hand side becomes n times a sample-wise KL. With Q
  the marginal of Ŷ, the first term is nÎ(X;Ŷ), "the empirical mutual
  information".
  - Threshold classifiers on [0,1] have VC dimension 1, so the bound is
    O(√(log n / n)).
  - Yet "the ratio between RHS of (4) and n converges … to a value which
    is at least H(Y)".
- **VC recovery.** By Sauer–Shelah, a uniform prior over the possible
  labellings bounds the KL term by d log(2en/d).
- **Theorem 2 (lossy).** The same bound, with an infimum over compressed
  algorithms Ŵ, plus ε.
- **Theorem 3 (type II).** For n ≥ 10,
  n·h_D(E L(W), E L̂(S,W)) ≤ I(T; Ŷ^{2n} | Y^{2n}) + log n, where
  h_D(x,x′) = 2h_b((x+x′)/2) − h_b(x) − h_b(x′). This is twice the binary
  Jensen–Shannon divergence. In the realisable case it gives O(1/n).
- **Theorem 4 (main result: latent variables).**
  E[gen(S,W)] ≤ inf 2√((2E D_KL(P^{⊗2n}_{U|X,Ŵe}(U,U′|X,X′,Ŵe) ‖ Q) + K + 2)/n) + ε,
  for any type-III prior Q. "This bound is valid for any choice decoder".
  Footnote 2 concedes it "may be loose", for instance when the decoder
  ignores U.
- **Theorem 7 (tail, latent variables).** With probability 1 − δ,
  gen(S,W) ≤ (D_KL(·‖Q) + (K+2)/2 + log(2/δ))/λ + 2λ/n + √(log(2/δ)/n).
- **Geometric compression (App. C.3).** Take U = −1 + X/5 if X < 0.5 and
  1 + X/5 if X > 0.5. Then I(U;X) = ∞, but a lossy Û with distortion
  below 0.05 has I(Û;X) = 1.
- **Kawaguchi et al. (App. B.2).** The authors say they "could not
  conclude the reported order-wise behavior". By its own constant
  definitions, the bound is in H(U|Y) + H(We), not
  I(X;U|Y) + I(We;S), and its G₃ term may grow as Õ(2^{H(U|Y)}).
- **Experiment (§4, App. D).** CIFAR-10, a small CNN encoder with a 64-d
  latent, a linear decoder, 200 epochs and 5 runs.
  - The lossy CDVIB prior reaches 65% best test accuracy (β = 0.01).
  - Lossless CDVIB reaches 64% (β = 1e−5).
  - Standard VIB reaches 62.5% (β = 0.005).
  - The priors are K × M Gaussians (M = 5 per label), updated by moving
    average. Footnote 8: for M = 1 this satisfies type-III symmetry, and
    for M > 1 it "is an approximation".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Generalisation of a representation learner is bounded by the KL of the latents' train-and-ghost law to a label-symmetric prior, for any decoder | strong | Theorem 4, proof App. E.5 (read) |
| C2 | The predicted-label bound contains the f-CMI bound and the VC bound as cases | strong | Theorem 1 with Eqs. 3–4 and Sauer–Shelah; proof E.2 not checked |
| C3 | Sample-wise mutual information can stay of order H(Y) where the true generalisation error vanishes | moderate | the threshold-classifier example in §2.2, argued in prose |
| C4 | Lossy compressibility accounts for geometric compression | weak | one constructed example, App. C.3 |
| C5 | Earlier IB generalisation bounds (Shamir et al., Vera et al., Kawaguchi et al.) are vacuous in realistic settings | moderate | cited for Vera et al.; argued from constant definitions for Kawaguchi et al., App. B.2 |
| C6 | Label-dependent learned priors regularise better than VIB's N(0, I) | weak | one dataset, one architecture, about 2.5 points, Figs. 2–3 |

## Method

The Lossless CDVIB regulariser replaces VIB's KL(N(μ_x, σ_x²) ‖ N(0,I))
with a KL to the nearest of M label-specific Gaussian priors. The prior
means and variances are updated by a moving average with coefficient α,
which is meant to stand in for the ghost data (Eq. 14). Lossy CDVIB
regularises a perturbed latent Û = μ_X + Z₂ + σ_X Z₁ through an upper
bound that splits it into two KLs (Eqs. 15–18). The decoder still
receives the unperturbed U.

## Concepts

- **Ghost (test) dataset S′.** An independent copy of S, used only in the
  analysis.
- **MDL of the latents.** The KL term of Theorem 4, read as the rate
  (nats per dataset) of a block codebook that covers the rearranged
  latent sequence. It is not the MDL of the model parameters.
- **Symmetric prior.** A conditional prior over the 2n predictions or
  latents, invariant under the permutation class of its type.
- **Lossy compressibility.** Covering up to average distortion ε in the
  generalisation gap, not exactly.
- **Geometric compression.** Latents concentrated around a few cluster
  centres, after Geiger & Koch (2019).

## Connections

The paper builds on Blum and Langford's PAC-MDL bound (2003), on the
authors' own fixed-size and variable-size compressibility frameworks
(Sefidgaran et al. 2022; Sefidgaran & Zaidi 2023) and on the CMI and
f-CMI frameworks of Steinke and Zakynthinou and of Harutyunyan et al. It
positions itself against the IB generalisation bounds of Shamir et al.
(2010), Vera et al. ([LIT-240](../literature.d/LIT-240.md)) and Kawaguchi et al. (2023), and draws on
the critiques of Amjad & Geiger, Geiger & Koch, Kolchinsky et al. and
Dubois et al. It notes that label-dependent priors connect to Fischer's
conditional IB ([LIT-226](../literature.d/LIT-226.md)).

## Bearing on the record

- **[THEORY-035](../theory.d/THEORY-035.md) (Rejected)** names the paper in Connections, as taking up
  "the IB term controls generalisation" formally. That is fair, but it
  takes the claim up to replace it. The paper does not prove that
  I(X;U) cannot bound generalisation. It argues that existing I(X;U)
  bounds are vacuous or infinite, and it exhibits a better quantity. It
  also gives [THEORY-035](../theory.d/THEORY-035.md) a further item for its "What this does not say"
  list. The information quantity that bounds generalisation here is a
  divergence of the latents to a prior shared by train and ghost data.
  That sits beside I(S;W) ([LIT-347](../literature.d/LIT-347.md)), not I(X;T). The argument against
  I(X;T) for deterministic continuous encoders, that it is infinite,
  agrees with Saxe et al. ([LIT-372](../literature.d/LIT-372.md), App. C).
- **The `corrects: LIT-240` relation on the LIT is stronger than the
  paper.** The paper does not show Vera et al.'s bound to be wrong. It
  says the bound holds only for finite alphabets and that its constant
  C_δ, which grows with the latent alphabet size |U|, "dominates and
  their bound becomes vacuous".
  For this it cites Rodriguez Galvez (2019) and Lyu et al. (2023)
  without its own computation. A weaker relation such as
  `compared_against` might fit better. That is for whoever reads
  [LIT-240](../literature.d/LIT-240.md).
- **On the heading** *relating K-complexity to minimum sufficient
  statistics*: the paper's "MDL" is a Shannon-style coding rate under a
  prior, not Kolmogorov complexity, and the paper says nothing about
  sufficient statistics. It answers the IB-against-MDL question directly.
  The IB's I(X;U) is replaced, as a complexity for generalisation, by a
  coding rate that depends on the encoder's structure.
- **Practice.** Regularising toward label-dependent learned priors
  (CDVIB) is a training instruction. It belongs in the anthology, so the
  `anthology-candidate` flag stands.

## Limitations

- **The bound is never computed.** No experiment evaluates the right-hand
  side of Theorem 4 or 7. Computing it "analytically in simple setups" is
  listed as future work (App. C.4).
- **The prior is not available from training data.** The type-III prior
  may depend on the ghost set, which is unavailable. The experiment
  approximates it by moving averages, and the priors for M > 1 are only
  approximately symmetric (footnote 8).
- **A floor of 2√((K+2)/n).** The K + 2 term remains however compressible
  the latents are. Its source is the label-histogram mismatch between S
  and S′ (Lemma 3).
- **Proofs not checked here.** Of the proofs, only the general technique
  and Theorem 4 were read, as above.
- **The constant in Theorem 4.** Its proof uses Lemma 3 under a looser
  condition than the lemma states (1.36 against 0.68).
- **The experiment is narrow.** One dataset and one small architecture.
  Accuracies are 62–65%, and there is no comparison beyond VIB.
- **Single tasks only.** The authors flag multiple downstream tasks as
  open.

## Open questions

- What is the numerical value of the Theorem 4 bound for a trained
  network? A computation in the two-layer Gaussian setting they propose
  would show whether it is non-vacuous in practice.
- Which priors capture "joint compressibility" beyond products of
  Gaussians, and does a better prior give a measurably smaller bound and
  gap?
- Does the K + 2 term limit the bound's use for many-class problems?
