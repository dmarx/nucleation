---
number: 783
status: Read
formerly:
- NOTE-tmpenm87
paper: LIT-974
title: 'Han, Papyan & Donoho — Neural Collapse Under MSE Loss'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (v4 of 10 May 2022, the ICLR 2022
    version, 36 pages), fetched from arxiv.org/pdf/2106.02073 and extracted
    with pdftotext, both plain and -layout. Read: the main text (§§1–5);
    Appendix A (setup, Table 1, Figures 3–12, the STL10 exceptions, the
    open questions); Appendices B and C (the proofs of Theorems 1 and 2);
    Appendix D (invariance, aligned SNR coordinates, the renormalized flow,
    and the proofs of Proposition 2 and Corollaries 1 and 2, Lemmas 1, 3–5
    and 7); and Appendix E. The proofs were followed, not re-derived; the
    constants of Proposition 2 and Lemma 1 were checked against the
    -layout text. The figures were read from their captions.
date: '2026-10-14'
summary: >-
  Networks trained with MSE loss show neural collapse on five datasets and
  three architectures. The MSE loss splits exactly into a term for the
  least-squares classifier of the current features and a non-negative
  deviation term, and the deviation becomes negligible early in training.
  On that "central path", in an unconstrained-features model with no
  weight decay and features continually renormalized to identity
  within-class covariance, gradient flow drives every singular value of
  Σ_W^(−1/2)M̃ to infinity as (4t/N)^(1/4), and drives them to equality.
  That gives NC1–NC4 in closed form.
---
<!-- inactive-ok-file: THEORY-083 THEORY-209 THEORY-039 — Proposed; the record's statement of collapse, its account of limiting dynamics, its comparison of late training phases, and the account filed from this reading -->

# NOTE-783: Han, Papyan & Donoho — Neural Collapse Under MSE Loss

## Contribution

Before it, neural collapse was measured under cross-entropy and its
dynamics were unknown. After it, the four collapses are measured under MSE
loss on standard nets, with a decomposition of the loss measured during
training. There is also one model in which collapse follows from explicit,
closed-form dynamics. The model is an unconstrained-features model under a
modified flow, not ordinary gradient descent on a network.

## Key insight

With MSE the classifier can be solved for. If the classifier stays at the
least-squares optimum for the current features, and the paper measures
that it nearly does, then predictions and loss depend on the features only
up to an invertible linear map. Whitening by the within-class covariance
loses nothing. In whitened coordinates the class means are the
signal-to-noise matrix SNR = Σ_W^(−1/2) M̃. The loss is ½ Σ_j 1/(ω_j² + C)
in its singular values, so descent pushes each ω_j up at a rate that is
the same function of ω_j for every j. The small ones catch up. Unbounded
equal singular values are collapse (NC1) onto a simplex (NC2).

## Assumptions

For the theory (§3, Appendix D):

- **(A1) Central path.** The classifier is exactly
  W̃_LS = (1/C) M̃ᵀ (Σ̃_T + μ̃_G μ̃_Gᵀ + λI)^(−1) for the current features.
  This is measured as approximate (Figure 2), and imposed exactly.
- **(A2) Zero global mean.** The least-squares bias subtracts the global
  mean from features and targets.
- **(A3) Continual renormalization.** After every step the features are
  mapped back to Σ_W = I. This is not gradient descent: it is projected
  gradient flow on the manifold of identity-covariance features,
  dX/dt = −Π_(T_X 𝒳)(∇_X L_LS(X)).
- **Unconstrained features**, Σ_W full rank throughout, P > C.
- **λ = 0 in the theory.** The experiments use weight decay as in [LIT-618](../literature.d/LIT-618.md).
- **Balanced classes**, N per class.

For the experiments: the protocol of [LIT-618](../literature.d/LIT-618.md) (SGD with momentum, weight
decay, batch normalization, no augmentation, one run per learning rate,
best test error kept). MNIST, FashionMNIST, SVHN, CIFAR10 and STL10, with
VGG, ResNet and DenseNet. CIFAR100 and ImageNet are left out, because MSE
needs a rescaling heuristic there.

## Key results

- **Proposition 1 (Webb & Lowe with weight decay).** For fixed features,
  W̃_LS = (1/C) M̃ᵀ (Σ̃_T + μ̃_G μ̃_Gᵀ + λI)^(−1).
- **Theorem 1.** L(W̃, H̃) = L_LS(H̃) + L⊥_LS(W̃, H̃), with
  L⊥_LS = ½ tr{(W̃ − W̃_LS)(Σ̃_T + μ̃_G μ̃_Gᵀ + λI)(W̃ − W̃_LS)ᵀ} ≥ 0, which
  is zero only at W̃ = W̃_LS. *Holds:* any features, any λ ≥ 0.
- **Theorem 2.** L_LS = L_NC1 + L_NC2/3. Here
  L_NC1 = ½ tr{W̃_LS (Σ̃_W + λI) W̃_LSᵀ} is a variance term, and
  L_NC2/3 = (1/2C)‖W̃_LS M̃ − I‖²_F measures the distance from classifier and
  means being the same simplex ETF.
- **Figure 2 (measured).** L⊥_LS becomes negligible against L_LS from an
  early epoch and stays so through the terminal phase, in all 15
  dataset–network cells. L_NC2/3 falls fastest. The network first spreads
  the means into a simplex and then compresses within-class variation.
- **Invariance (Eq. 7).** For symmetric full-rank A,
  W_LS(AH̃)AH̃ = W_LS(H̃)H̃. The least-squares predictions are invariant to
  the linear coordinates of the features.
- **Lemma 1.** With λ = 0, on the central path,
  L = ½ Σ_(j=1)^(C−1) 1/(ω_j² + C). The pieces are
  L_NC1 = ½ Σ ω_j²/(C + ω_j²)² and
  L_NC2/3 = ½ Σ (1/C)(ω_j²/(ω_j² + C) − 1)².
- **Lemma 5 and Proposition 2.** Under the renormalized flow,
  dω_j/dt = (1/N) ω_j/(C + ω_j²)². Integrated, this gives
  C²N log ω_j + CN ω_j² + (N/4) ω_j⁴ = a_j + t, with a_j set by ω_j(0).
- **Corollary 1.** ω_j(t) → ∞ with ω_j(t)/(4t/N)^(1/4) → 1 for every j,
  and max_j ω_j / min_j ω_j → 1.
- **Corollary 2.** SNR_t/ω_max(t) → Û₀V̂₀ᵀ, the singular vectors at t = 0.
  Then tr(Σ_B† Σ_W) → 0 (NC1), the renormalized means tend to a simplex ETF
  (NC2, Lemma 7), and NC3–NC4 follow from Theorem 1 of [LIT-618](../literature.d/LIT-618.md). Also
  Σ_W^(−1/2)H_t/ω_max → (Û₀V̂₀ᵀ) ⊗ 1_Nᵀ.
- **MSE collapse measured (Appendix A).** NC1–NC4 trends under MSE match
  those under cross-entropy (Figures 3–8).
  - The median test-accuracy gain from first zero error to the last
    epoch is 0.962 points, the mean 1.833 (Table 1).
  - Activation collapse is faster under MSE than under CE (Figure 10).
  - Adversarial robustness is better under MSE, "sometimes several
    magnitudes" (Figure 11).
  - STL10 with ResNet and DenseNet is an outlier (A.7).
- **Test data (Figure 12).** NC1 also falls on test data, much more
  slowly, and ends higher, "roughly monotonic with the difficulty of the
  dataset".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Neural collapse occurs under MSE loss on standard nets and datasets | moderate | Figures 3–8; one run per cell, [LIT-618](../literature.d/LIT-618.md)'s protocol, ten-class datasets only |
| C2 | MSE splits exactly into a least-squares term and a non-negative deviation term | strong | Theorem 1, Appendix B |
| C3 | Trained nets lie near the central path from early in training | moderate | Figure 2, 15 cells, measured |
| C4 | On the central path the least-squares predictions are invariant to invertible linear maps of the features | strong | Eq. 7 |
| C5 | Renormalized gradient flow of unconstrained features on the central path produces NC1–NC4, with ω_j ~ (4t/N)^(1/4) | strong, for that model | Proposition 2, Corollaries 1–2, Appendix D |
| C6 | Ordinary training reaches collapse by the mechanism of C5 | weak | not shown; (A3) is imposed, not measured, and λ = 0 in theory but not in the runs |
| C7 | Collapse on test data is slower and incomplete | weak | Figure 12, one figure, not analysed |

## Method

1. Decompose the MSE loss around the least-squares classifier (Theorems
   1–2) and measure the parts during training (Figure 2).
2. Restrict to the central path, and use the invariance there to work in
   whitened coordinates X = Σ_W^(−1/2)H̃.
3. Rotate into the SVD basis of the SNR matrix (aligned-SNR coordinates).
   There the loss and the flow decouple by singular value (Lemmas 1, 3,
   4).
4. Solve the scalar ODE for each ω_j and read off the limits.

## Concepts

- **Central path.** The set of pairs (W̃_LS(H̃), H̃): features with their
  own least-squares classifier.
- **Renormalized features.** X = Σ_W^(−1/2)H̃, features with identity
  within-class covariance. They are one representative of a fibre of
  equally performing feature matrices (Appendix D.1).
- **SNR matrix.** Σ_W^(−1/2)M̃, the class means in whitened coordinates. It
  has rank C − 1. Its singular values ω_j measure class separation in
  each direction.
- **Continually renormalized gradient flow.** A gradient step followed by
  re-whitening; in the step-size limit, the flow projected onto the
  tangent space of the identity-covariance manifold.
- **NC1 as defined here.** Σ_B†Σ_W → 0, stated more precisely than in
  [LIT-618](../literature.d/LIT-618.md) (footnote 3), which measured its trace.

## Connections

It follows Papyan, Han & Donoho (2020), [LIT-618](../literature.d/LIT-618.md), using their protocol and
their Theorem 1 for NC3–NC4. It sets itself against Mixon et al. (2020),
who linearize the UFM ODE near zero initialization, and against Poggio &
Liao (2020), who use homogeneous weight-normalized networks. Neither gives
closed-form dynamics. The landscape results of Zhu et al. (2021) and Fang
et al. (2021) describe minima without dynamics (Appendix E). The review
[LIT-978](../literature.d/LIT-978.md) summarizes it, and [LIT-985](../literature.d/LIT-985.md) cites it as a UFM analysis that cannot
see the data.

## Bearing on the record

- **[QUESTION-051](../questions.d/QUESTION-051.md).** Its "What would answer it" asks for "a derivation
  showing why gradient descent on cross-entropy reaches collapse". This
  paper gives a derivation for MSE, not cross-entropy. It is for
  unconstrained features, not a network, and for a renormalized flow, not
  gradient descent. It answers part of the question's first half, in a
  stated model. Its measured part, proximity to the central path, is about
  real networks. It says almost nothing on the second half: Figure 12 is
  one look at test data.
- **[QUESTION-080](../questions.d/QUESTION-080.md).** On the central path with λ = 0 there is no finite
  minimum. The loss falls only as the singular values grow without bound,
  as t^(1/4). Collapse here is a limit approached at a power-law rate, not
  a fixed point. And the direction it approaches, Û₀V̂₀ᵀ, is fixed by the
  singular vectors at entry to the central path. That bears on the
  question's "if collapse … fluctuates during the limiting dynamics, then
  measurements of it depend on when training was stopped". In this model
  the degree of collapse depends on t by construction, and the shape
  depends on the start. The theory is silent on weight decay and noise,
  which [THEORY-209](../theory.d/THEORY-209.md)'s limiting dynamics need.
- **[THEORY-083](../theory.d/THEORY-083.md).** Its summary says "the dynamics are unexplained", and its
  promote_when asks for "a held paper that derives collapse as the limit of
  gradient descent on cross-entropy". This paper is held now and is not
  that paper: it is MSE and a modified flow. The THEORY should name it as
  the record's one derivation of collapse dynamics, under MSE, and keep the
  cross-entropy condition open. Its MSE runs are a replication of
  [THEORY-083](../theory.d/THEORY-083.md)'s measurements under a second loss. They are not under the
  conditions promote_when names (augmentation, label noise, imbalance,
  seeds), because the protocol is [LIT-618](../literature.d/LIT-618.md)'s.
- **[THEORY-039](../theory.d/THEORY-039.md).** The ordering in Figure 2 is a measured sub-phase
  structure of the terminal phase. L_NC2/3 is driven down first and the
  within-class variance afterwards. That is not among the phases
  [THEORY-039](../theory.d/THEORY-039.md) compares.
- **Filed.** The mechanism, stated at the model's strength, is filed as
  [THEORY-278](../theory.d/THEORY-278.md).
- No instruction for machine-learning practice is relied on.

## Limitations

- The mechanism is shown for a model three steps from practice. Features
  are free, the classifier is held at its optimum, and the features are
  re-whitened continually. The authors motivate (A3) by batch
  normalization and by the invariance. They do not measure whether
  training follows the renormalized flow.
- λ = 0 in the theory; every experiment uses weight decay.
- Balanced classes, ten-class datasets, one run per learning rate, best
  test error kept. CIFAR100 and ImageNet are excluded.
- Assumes Σ_W stays full rank. That holds in practice (footnote 12), but
  means exact collapse is never reached.
- The authors list as open the roles of weight decay, batch
  normalization, SGD and test data (A.8).

## Open questions

- Does ordinary gradient descent on unconstrained features, without
  renormalization, follow the same ω_j dynamics? A measurement of the SNR
  singular values in a trained network, against (4t/N)^(1/4), would
  settle whether the closed form describes training.
- Is there an analogue for cross-entropy, where the classifier has no
  closed form?
- With weight decay the MSE loss has a finite minimum. What is the flow
  then, and where does it stop?
