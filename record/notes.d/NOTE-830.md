---
number: 830
status: Read
formerly:
- NOTE-tmp9jxqd
paper: LIT-248
title: 'Li et al. — Self-Supervised Learning with Kernel Dependence Maximization'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv v2 PDF (arxiv.org/pdf/2106.08320, 26 pp.,
    NeurIPS 2021 footer), text extracted with pdftotext: §§1–6, every
    appendix (A.1–A.3 with the proofs of Theorems A.1–A.3, B.1 with
    Lemma B.0.1 and Theorem B.1, B.2, B.3, C.1–C.3, D, E), and the tables.
    The extraction drops some signs and fraction bars; the expressions
    below were checked against the layout-preserving extraction and, for
    Theorem B.1, rederived by hand.
date: '2026-10-14'
summary: >-
  With image identity as a one-hot label, HSIC(Z,Y) is (Δl/N) times the
  gap between the mean kernel on positive pairs and on all pairs, and
  (1/2N²)Σ MMD²(i,j) = (N/Δl)·HSIC(Z,Y). The large-batch InfoNCE loss is
  exactly −HSIC(Z,Y) plus a log-mean-exp of the centred critic (eq. 28),
  and for a bounded kernel it bounds −HSIC(Z,Y) + γHSIC(Z,Z) up to a
  remainder of second order in the critic's variance (Thm B.1, whose
  printed remainder has the wrong sign).
---
<!-- inactive-ok-file: THEORY-227 — Proposed; the account this paper was filed for, and the mutual-information account its Figure 3 repeats -->
<!-- inactive-ok-file: THEORY-312 — Proposed; the account filed from this reading -->

# NOTE-830: Li et al. — Self-Supervised Learning with Kernel Dependence Maximization

## Contribution

The paper writes a self-supervised loss as kernel dependence between a
representation Z of an augmented view and the identity Y of its source
image: L = −HSIC(Z,Y) + γ√HSIC(Z,Z). With one-hot identities, HSIC(Z,Y) has
a closed form in the kernel on Z alone, and it is proportional to the mean
squared MMD between the images' view distributions. The paper also shows
that the large-batch InfoNCE loss splits exactly into −HSIC(Z,Y) and a
log-mean-exp term, and bounds it below by an HSIC loss with a variance
penalty. The rest is an unbiased estimator for the non-i.i.d. batches of
SSL, a random-Fourier-feature form linear in batch size, and ImageNet
results.

## Key insight

Once the label is the image's identity, every HSIC quantity becomes a
statement about the kernel mean embeddings μ_i of the N per-image view
distributions. HSIC(Z,Y) is their spread, and InfoNCE is that spread plus a
term that only sees how much the critic varies around its mean.

## Assumptions

- **Finite dataset, uniform identities.** N images, each drawn with
  probability 1/N; Y is one-hot in R^N (§3, App. A.1).
- **Label kernel of the form (13).** l(y_i, y_j) = Δl·1[y_i = y_j] + l₀,
  which covers any kernel that is a function of y_iᵀy_j or ‖y_i − y_j‖.
  Results are stated with Δl = N "for convenience".
- **Positive pairs are conditionally independent.**
  p_pos(Z,Z′) = Σ_i p(i)p(Z|i)p(Z′|i) (Thm A.1).
- **A positive-definite kernel on Z.** Dot product and scaled cosine are
  noted to be valid kernels (§3.1). The experiments use an inverse
  multiquadric kernel k(z,z′) = c/√(c² + ‖z − z′‖²) on unit-norm,
  batch-normalized projections.
- **Theorem B.1** needs a bounded kernel, |k| ≤ k_max.
- **The estimator theorem (A.2)** needs k(z,z) = 1, B < N images sampled
  without replacement and M views per image drawn independently.
- **InfoNCE is the large-batch form.** Eq. 6 / eq. 27 is "its infinite
  sample size limit" (citing Wang & Isola), E_Z log E_Z′ exp k(Z,Z′) −
  E_pos k(Z,Z′), not the finite-batch estimator with K negatives.

## Key results

- **Eq. 2 (HSIC in kernel form).** HSIC(X,Y) = E[k(X,X′)l(Y,Y′)] −
  2E[k(X,X′)l(Y,Y″)] + E[k(X,X′)]E[l(Y,Y′)], the squared Hilbert–Schmidt
  norm of the centred cross-covariance (eq. 1).
- **Theorem A.1 / eq. 14.** Under the assumptions above,
  HSIC(Z,Y) = (Δl/N)·E_(Z,Z′∼pos)[k(Z,Z′)] − (Δl/N)·E[k(Z,Z′)], where the
  second expectation is over independent Z, Z′ from the marginal. The l₀
  terms cancel. With Δl = N this is eq. 5 in the main text, written there
  with ∝.
- **App. B.2 (MMD).** With μ_i the RKHS mean embedding of image i's view
  distribution, (1/N²)Σ_ij MMD²(i,j) = 2E_pos[k] − 2E_Z E_Z′[k], so
  (1/2N²)Σ_ij MMD²(i,j) = (N/Δl)·HSIC(Z,Y). The derivation uses
  ⟨μ_i, μ_j⟩ = E_(Z|i, Z′|j)⟨φ(Z), φ(Z′)⟩ and equal label probabilities.
  The identity is unnumbered and states no integrability condition. The
  appendix heading says "HSIC(X,Y)" where it means HSIC(Z,Y).
- **Eq. 28 (exact).** With Δl = N and μ₁(Z) := E_Z′ k(Z,Z′),
  L_InfoNCE = −HSIC(Z,Y) + E_Z log E_Z′ exp(k(Z,Z′) − μ₁(Z)). This is an
  identity. It needs no smallness.
- **Eq. 7 (approximate).** Taylor-expanding exp around μ₁ and then
  log(1 + x) ≈ x gives L_InfoNCE ≈ −HSIC(Z,Y) + ½E_Z Var_Z′[k(Z,Z′)].
  *Holds when* k(Z,Z′) stays near μ₁; "higher order moments ... are
  dropped" (App. B.1).
- **Lemma B.0.1.** For 0 < α ≤ 1/4 and x ≥ −(1 + √(1 − 4α))/(2α),
  exp(x) ≥ 1 + x + αx².
- **Theorem B.1.** If |k| ≤ k_max, Δl = N, and γ solves
  min{−2, −2k_max} = −(1 + √(1 − 4γ))/(2γ), then −HSIC(Z,Y) + γHSIC(Z,Z)
  is bounded by L_InfoNCE plus a remainder E_Z[(γV)²/(1 + γV)], with
  V = Var_Z′[k(Z,Z′)].
  - The printed statement and proof carry the remainder with the opposite
    sign: "≤ L_InfoNCE(θ) − E_Z (γVar)²/(1+γVar)". They justify it with
    log(1 + x) ≥ x/(1 + x) = x − x²/(1 + x), which gives a minus inside the
    lower bound on the log term, and so a plus in the theorem. Rederived
    here, the bound is −HSIC(Z,Y) + γHSIC(Z,Z) ≤ L_InfoNCE +
    E_Z[(γV)²/(1 + γV)]. Main-text eq. 8 writes the same thing as "+
    o(variance)", which agrees with the corrected sign.
  - The last step uses HSIC(Z,Z) ≤ E_Z Var_Z′[k(Z,Z′)], which the paper
    credits to Cauchy–Schwarz.
  - For the cosine kernel z·z′/(τ‖z‖‖z′‖), k_max = 1/τ, and τ = 0.1 gives
    γ = 0.0475 (checked: 1600γ² = 76γ). For Gaussian and IMQ kernels the
    paper says γ can be replaced by 1/3.
  - The penalty here is γHSIC(Z,Z), not the √HSIC(Z,Z) of SSL-HSIC. Eq. 9
    adds that −HSIC(Z,Y) + γHSIC(Z,Z) ≤ L_SSL-HSIC when HSIC(Z,Z) ≤ 1.
    "InfoNCE and SSL-HSIC in general don't quite bound each other."
- **Eq. 10 (clustering).** With linear kernels on Z and Y, and Z centred
  and unit length, −HSIC(Z,Y) ∝ Σ_i Σ_p ‖z_i^p − z̄_i‖² − NM, with
  z̄_i the mean of image i's M views. This is k-means within-cluster
  scatter. The
  authors stress that the right-hand side "could be optimized by setting
  all z_i^p to the same vector for each i, but this does not actually
  optimize HSIC(Z,Y)", because the identity needs the centring.
- **Theorem A.2 / Corollary A.2.1 (estimators).** Eq. 15 is an unbiased
  estimator of eq. 14. Eq. 17 has bias O(1/B) if |k| ≤ 1. The i.i.d.
  estimator (3) misses the 1/N scaling and the 1/(M(M − 1)) correction,
  which matters at M = 2.
- **Theorem A.3.** The biased i.i.d. estimator of HSIC(Z,Z) has bias
  O(1/B), not O(1/(BM)), under SSL sampling.
- **Theorem C.1.** The IMQ kernel's random-Fourier-feature density is
  ∝ K_((n−1)/2)(cs)/s^((n−1)/2), with K_ν the modified Bessel function of
  the second kind.
- **Experiments (§§4–5).** ResNet-50, 1000 epochs: 72.2% top-1 linear
  evaluation without a target network and 74.8% with one. At 100 epochs
  without a target network, SSL-HSIC gets 66.7% and InfoNCE in the same
  codebase 66.0% (Table 8a). Linear, Gaussian and IMQ kernels get 65.27%,
  66.67% and 66.72%.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | With one-hot identity labels, HSIC(Z,Y) is (Δl/N) times the positive-pair minus all-pair mean kernel | strong | Theorem A.1, proved |
| C2 | The mean squared MMD between images' view distributions equals 2(N/Δl)·HSIC(Z,Y) | strong | App. B.2, a short exact derivation |
| C3 | The large-batch InfoNCE loss is exactly −HSIC(Z,Y) plus a log-mean-exp of the centred critic | strong | eq. 28, an identity |
| C4 | For bounded kernels, InfoNCE bounds a variance-penalized HSIC loss up to a second-order remainder | moderate | Theorem B.1, proved, with a sign slip in the remainder |
| C5 | InfoNCE "works because it implicitly estimates a kernel-based notion of dependence" | weak | an interpretation of C3–C4; no experiment separates it from rival accounts |
| C6 | BYOL's loss is the two-view case of the clustering form (10), with a target network in place of centring | weak | argued in §3.2; it needs the centring assumption, checked only by a z-test on BYOL features (App. B.3) |
| C7 | SSL-HSIC matches contemporary SSL methods on ImageNet and transfer | moderate | Tables 1–8, single runs, no error bars |

## Method

SSL-HSIC: for B images and M augmentations, encode each view, project and
normalize. Estimate HSIC(Z,Y) with eq. 17, and HSIC(Z,Z) with the biased
estimator, using random Fourier features of an IMQ kernel, resampled every
step, with independent features for the two copies of K in HSIC(Z,Z). The
loss is −HSIC(Z,Y) + γ√HSIC(Z,Z) with γ = 3. The IMQ scale is trained to
maximize the entropy of the kernel distances. An optional BYOL-style
target network and predictor can be added.

## Concepts

- **Self-supervised label.** Y_i = e_i ∈ R^N, the one-hot index of the
  source image. The "kinds" are single images.
- **Positive-pair distribution.** p_pos(Z,Z′) = Σ_i (1/N)p(Z|i)p(Z′|i): two
  independent views of the same image.
- **μ₁(Z).** E_Z′ k(Z,Z′), the critic's mean against the marginal. InfoNCE
  sees k only through k − μ₁ beyond the HSIC term.
- **Large-batch InfoNCE.** E_Z log E_Z′ exp k(Z,Z′) − E_pos k(Z,Z′), with
  the critic read as a kernel.

## Connections

It builds on HSIC (Gretton et al. 2005) and the HSIC bottleneck (Ma et
al.; Pogodin & Latham), and on centred kernel alignment (Cortes et al.)
for the metric-learning reading. It takes the large-batch InfoNCE form from
Wang & Isola. It sets the work against the mutual-information reading of
InfoNCE (van den Oord et al.; Poole et al.; Tschannen et al.). Its Figure 3
example is the same point Tschannen et al. make: equal mutual information,
different downstream quality. The MMD reading uses the mean-embedding facts
collected in Muandet et al.'s review ([LIT-260](../literature.d/LIT-260.md)), which also notes, in §3.6,
that MMD maximization in clustering is equivalent to dependence
maximization (Jegelka et al. 2009). That is the same identity in an older
setting.

## Bearing on the record

- **[THEORY-003](../theory.d/THEORY-003.md) is supported, with two corrections.**
  - **Supported.** The MMD identity holds as [THEORY-003](../theory.d/THEORY-003.md) uses it. It is an
    exact derivation in App. B.2 under the setting of Theorem A.1. For the
    bounded kernels the paper uses (IMQ, Gaussian, scaled cosine), the
    mean embeddings exist by Lemma 3.1 of [LIT-260](../literature.d/LIT-260.md), since E√k(X,X) ≤
    √k_max. The paper itself states no integrability condition, so that
    half of [THEORY-003](../theory.d/THEORY-003.md)'s promote_when is met by the reading together with
    [LIT-260](../literature.d/LIT-260.md).
  - **Correction 1.** [THEORY-003](../theory.d/THEORY-003.md) writes "(1/2N²)Σ_ij MMD²(i,j) = NΔ_l
    HSIC(Z,Y)". The paper has N/Δ_l, and its derivation gives N/Δ_l. It
    also cites "App. B.2, eq. 5": eq. 5 is the ∝ form from Theorem A.1, and
    the B.2 identity is unnumbered.
  - **Correction 2.** [THEORY-003](../theory.d/THEORY-003.md) calls InfoNCE ≈ HSIC "only a small-variance
    approximation". That is true of eq. 7, but eq. 28 is an exact
    decomposition, and Theorem B.1 is a non-asymptotic inequality for every
    bounded kernel. InfoNCE is still not HSIC, so [THEORY-003](../theory.d/THEORY-003.md)'s disclaimer
    stands. The bound is the stronger statement.
- **New account, [THEORY-312](../theory.d/THEORY-312.md).** It holds eq. 28 and Theorem B.1 at the
  strength they are established, with the sign corrected. It adds one step
  of the record's own: by Jensen the log-mean-exp term is nonnegative, so
  −HSIC(Z,Y) ≤ L_InfoNCE holds exactly.
- **[THEORY-006](../theory.d/THEORY-006.md) (InfoNCE ≤ log batch size).** No conflict. That bound is
  about the finite-batch estimator, and this paper works with the
  large-batch form, from which log K has been subtracted.
- **[THEORY-227](../theory.d/THEORY-227.md) (mutual information does not fix quality).** Figure 3 is a
  further instance of the same point, in the SSL setting.
- **[QUESTION-052](../questions.d/QUESTION-052.md).** The "kinds" here are single images, and the signature
  is the set of embeddings μ_i. The paper offers HSIC/MMD as the
  discrimination criterion that [THEORY-003](../theory.d/THEORY-003.md) relays. It says nothing about
  directed pairs.
- **For the anthology.** The method half (SSL-HSIC with random Fourier
  features, γ = 3, IMQ kernel, target network) is ML practice, and it is
  why [LIT-248](../literature.d/LIT-248.md) carries `anthology-candidate`. Nothing here takes it up.

## Limitations

- Everything is on a finite dataset with identity labels. Nothing is said
  about a population of images or about semantic classes. The authors
  call identity labels possibly "not wholly satisfactory".
- The kernel is on the learned Z and is fixed while the encoder changes. No
  result concerns what training reaches; all identities hold for any
  encoder.
- The InfoNCE link uses the large-batch form. The finite-batch estimator,
  with its log K ceiling, is not analysed.
- The BYOL connection needs centred features, supported only by a single
  z-test (App. B.3), and it treats the target network as the second view.
- The experiments are single runs without variance estimates. The
  InfoNCE-versus-SSL-HSIC comparison is a 0.7-point gap at 100 epochs.

## Open questions

- A finite-batch version of eq. 28: does the K-negative InfoNCE estimator
  decompose the same way, with a gap term that vanishes as K grows?
- Is the conclusion that "InfoNCE works because it estimates kernel
  dependence" separable from the alignment-and-uniformity account by any
  experiment? An ablation that keeps HSIC(Z,Y) fixed and changes only the
  log-mean-exp term would test it.
- Does anything carry over to semantic labels in place of image identity,
  where the per-class view distributions overlap?
