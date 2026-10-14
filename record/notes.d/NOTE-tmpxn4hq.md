---
status: Read
paper: LIT-226
title: 'Fischer — The Conditional Entropy Bottleneck'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv v1 PDF (arxiv.org/pdf/2002.05379, 14 pp.,
    the only arXiv version), text extracted with pdftotext: §§1–8 and
    Appendices A (model details), B (MI optimization) and C (hierarchical,
    sequence, unsupervised and denoising CEB). The Entropy 22(9):999
    version was not reached (MDPI refused the request; the PubMed Central
    copy answered with a bot challenge) and may differ. The skim note
    filed with the paper is NOTE-210.
date: '2026-10-14'
summary: >-
  The MNI criterion asks for I(X;Y) = I(X;Z) = I(Y;Z), and CEB targets it
  by minimizing I(X;Z|Y) − γI(Y;Z), which is IB with γ = β − 1. CEB beats
  VIB at every ρ on Fashion MNIST for accuracy and robustness, and a CEB
  Wide ResNet beats Madry's adversarially trained model on CIFAR-10
  without adversarial training. That retained information causes the
  robustness failures is a hypothesis, supported only by these
  experiments.
---
<!-- inactive-ok-file: THEORY-035 — Rejected; the IB-and-generalisation account that names this paper in its Connections -->

# NOTE-tmpxn4hq: Fischer — The Conditional Entropy Bottleneck

## Contribution

The paper names a criterion for a representation, the Minimum Necessary
Information (MNI) point, and an objective that targets it, the Conditional
Entropy Bottleneck (CEB). It shows that CEB is the Information Bottleneck
reparametrised, so the novelty is in which point of the IB curve to aim
for and in variational bounds that make the distance to that point
observable. It then reports that training at that point improves
accuracy, adversarial robustness, OoD detection and calibration, and
stops the memorisation of random labels.

## Key insight

Minimising I(X;Z) cannot say when to stop, because 0 ≤ I(X;Z) ≤ H(X).
Under the Markov chain Z ← X ↔ Y, I(X;Z) = I(Y;Z) + I(X;Z|Y), so
minimising the conditional term I(X;Z|Y) removes only information that
says nothing about Y. It has a natural floor of zero, reached at the MNI
point. Its variational upper bound, the residual information ReX,
therefore reads directly as "bits still to be compressed".

## Assumptions

- **Markov chain Z ← X ↔ Y**: Z depends on Y only through X. Every
  identity in §4 uses it, including I(X;Z|Y) = I(X;Z) − I(Y;Z) (Eq. 4).
- **The task is fixed by Y.** "Necessity" is defined relative to
  predicting Y from X. Footnote 2 declines the word "sufficiency" to avoid
  confusion with minimal sufficient statistics.
- **Deterministic datasets for γ = 1.** "For deterministic datasets
  (Section 3), γ = 1 will achieve the MNI for a sufficiently powerful
  model." In general Eq. (1) may not be attainable. The bound
  sup I(Y;Z)/I(X;Z) ≤ 1 (Eq. 2) is quoted from Anantharam et al., with
  equality "only when X → Y is a deterministic map", and is not proved
  here.
- **Stochastic encoders.** App. B.1 notes that the conditions for
  infinite mutual information in Amjad & Geiger do not apply, "as they
  both use stochastic encoders e(z|x)".
- **For CatGen (§6.3):** a uniform distribution over the training
  examples sampled in the minibatch, and log K ≥ I(X;Y).

## Key results

- **MNI point (Eq. 1).** I(X;Y) = I(X;Z) = I(Y;Z). Equivalently
  (Eq. 3), I(X;Y|Z) = I(X;Z|Y) = I(Y;Z|X) = 0.
- **CEB (Eq. 5).** min_Z I(X;Z|Y) − γI(Y;Z), equivalently
  min −H(Z|X) + H(Z|Y) + γH(Y|Z) (Eq. 7).
- **Equivalence to IB (§5).** With IB ≡ min I(X;Z) − βI(Y;Z) (Eq. 16),
  "CEB and IB are equivalent for γ = β − 1". The paper parametrises both
  by ρ = log γ = log(β − 1), with the MNI targeted at ρ = 0.
- **Variational CEB (Eqs. 9–15).** I(X;Z|Y) ≤ ⟨log e(z|x) − log b(z|y)⟩
  and I(Y;Z) ≥ ⟨log c(y|z)⟩ up to H(Y). Hence VCEB ≡
  min ⟨log e(z|x) − log b(z|y) − γ log c(y|z)⟩, with backward encoder
  b(z|y) where VIB has a marginal m(z).
- **Rate and residual information (Eqs. 19–20).**
  R ≡ ⟨log e(z|x) − log m(z)⟩ ≥ I(X;Z) and ReX ≡
  ⟨log e(z|x) − log b(z|y)⟩ ≥ I(X;Z|Y). "Observing ReX tells us exactly
  how many bits we are from the MNI point, assuming that our current
  classifier is optimal."
- **CatGen equals CPC (§6.3, Eqs. 27–31).** With c(y|z) =
  b(z|y)/Σ_{k=1}^{K} b(z|y_k) over the minibatch, CatGen "is
  mathematically equivalent to Contrastive Predictive Coding (CPC) … after
  an offset of log K", shown "using the proof from Poole et al. (2019),
  and substituting log b(z|y) for f(y,z)". "As with CPC, the CatGen bound
  is constrained by log K". The arXiv v1 text prints Eq. (30) as
  "I(Y;Z) ≤", but the surrounding text uses it as a lower bound ("without
  violating the variational bound"). The sign looks like a typo.
- **Fashion MNIST (§7.1, Fig. 3, Table 1, Fig. 4).** 60 models, 4 per
  type: deterministic, VIB and CEB at ρ ∈ {−1, …, 5}, with the same
  7×2 Wide ResNet encoder and a D = 4 latent.
  - "At every ρ the CEB models outperform the VIB models on both accuracy
    and robustness, while having essentially identical maximum rates."
  - At ρ = 0 the rate lower bound converges to "exactly I(X;Y) = log 10 ≈
    2.3 nats".
  - Targeted PGD attacks: robustness rises as ρ falls. CEB beats the
    deterministic baseline at all ρ except 5.
  - OoD: with the rate R as the threshold, CEB0 and VIB4 saturate
    detection on all four OoD sets, and VIB0 does not.
  - Calibration: CEB0 and VIB0 end "only slightly overconfident"; at
    ρ = 2 VIB is "almost as overconfident as Determ".
  - Random labels: "the CEB and VIB models with ρ < 6 never learn, even
    after 100 epochs", while deterministic models memorise after about
    40 epochs.
- **CIFAR-10 (§7.2, Fig. 5).** A 62×7 Wide ResNet with AutoAugment,
  bidirectional CatGen CEB, 3 runs each at ρ = 0 and ρ = 5, the best
  kept. CEB0 reached 97.51% accuracy and 93.6% on CIFAR-10.1. It beat the
  adversarially trained Madry model (87.3%) on PGD L2 and L∞ attacks
  "everywhere except the region of L∞ ε ∈ [2, 7]". Transfer attacks were
  weaker still, which the paper reads as evidence against gradient
  masking.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | CEB and IB are the same objective under γ = β − 1 | strong | algebra, Eqs. 4, 5, 16 |
| C2 | ReX upper-bounds I(X;Z|Y), so it measures the distance to the MNI given an optimal classifier | strong | Eqs. 9–11, 20 |
| C3 | CatGen is CPC/InfoNCE with the backward encoder as critic, and is capped by log K | moderate | Poole et al.'s proof cited and applied, Eqs. 30–31; the printed inequality sign is wrong |
| C4 | CEB beats VIB at equal ρ in accuracy and adversarial robustness | moderate | Fashion MNIST, 4 models per setting, Fig. 3 |
| C5 | MNI models are better calibrated, detect OoD inputs and do not memorise random labels | moderate | Fashion MNIST only, Table 1, Fig. 4, §7.1 |
| C6 | Robust-generalisation failures are caused "in part" by retaining too much information | weak | stated as a hypothesis; the mechanism for adversarial robustness is "an intuition" from Ilyas et al.; evidence is the correlation in §7 |
| C7 | A CEB model without adversarial training beats Madry's model on CIFAR-10 PGD attacks | moderate | 1 selected model per ρ, Fig. 5 |

## Method

- **Encoder** e(z|x): for Fashion MNIST, a full-covariance D = 4 Gaussian
  from a 7×2 Wide ResNet.
- **Backward encoder** b(z|y): a D = 4 Gaussian from a one-layer MLP on
  the label.
- **Classifier** c(y|z): a two-layer MLP, or the Consistent Classifier
  c(y|z) ≡ softmax b(z|y)p(y) (§6.2), or CatGen (§6.3).
- **Objective:** VCEB (Eq. 15) at γ = e^ρ. A separately optimised marginal
  m(z), a mixture of 240 Gaussians, reports R for CEB without affecting
  training (App. A.1).
- **Variants:** bidirectional CEB (Eqs. 25–26); hierarchical CEB, which
  minimises I(Z_{i−1};Z_i|Y) − I(Y;Z_i) (Eq. 32); predictive CEB for
  sequences (Eq. 34); and the denoising and noising CEB autoencoders
  (Eqs. 36–41).

## Concepts

- **Robust generalization.** (RG1) classical held-out performance, (RG2)
  performance under an adversary unknown at training time, (RG3)
  detection of data far from the training distribution.
- **Necessity.** I(X;Y) ≤ I(Y;Z). This is what others call sufficiency,
  renamed by the author.
- **Minimality.** I(X;Y) ≥ I(X;Z), and in the criterion's statement
  "inf_{Z∈𝒵} I(Z;X,Y)".
- **Information-free dataset.** One with I(X;Y) = 0, such as fixed random
  labels.
- **Consistency metric** C_{I(Y;Z)}(Z) ≡ |H(Z) − H(Z|Y) − H(Y) + H(Y|Z)|
  (Eq. 8). It is zero when both ways of counting I(Y;Z) agree, which the
  paper expects only at γ = 1.

## Connections

The paper reparametrises the IB of Tishby, Pereira & Bialek ([LIT-338](../literature.d/LIT-338.md)),
which [NOTE-300](NOTE-300.md) had already shown algebraically. Fischer states the
equivalence himself (§5, γ = β − 1). It replaces VIB's marginal m(z)
(Alemi et al. 2017) with a label-conditional backward encoder. Its
CatGen decoder borrows Poole et al.'s InfoNCE proof ([LIT-246](../literature.d/LIT-246.md)), and its
footnote 7 calls the rate lower bound R_X "the 'InfoNCE with a tractable
encoder' bound from Poole et al. (2019)". Its motivation for (RG1) quotes
Shamir et al. (2010), |I(X;Z) − Î(X;Z)| ≈ O(2^{I(X;Z)}/√N), and Bassily et
al. (2017). That is the kind of mutual-information generalisation bound
that Sefidgaran, Zaidi & Krasnowski ([LIT-245](../literature.d/LIT-245.md)) argue is vacuous or
infinite in realistic settings. Sefidgaran et al. also note that their
label-dependent priors "enables a connection with the 'conditional
information-bottleneck' of [Fischer, 2020]".

## Bearing on the record

- **[THEORY-006](../theory.d/THEORY-006.md) cites the paper correctly, with one qualification.** It
  says CEB "relies on the bound (§6.3)". It does: CatGen is shown to be
  CPC/InfoNCE after an offset of log K, using Poole et al.'s proof, and
  "constrained by log K". The qualification is that CatGen's negatives
  are the other labels in the same minibatch, under "an assumption of a
  uniform distribution over the training examples we sampled". That is
  the in-batch case [THEORY-006](../theory.d/THEORY-006.md) lists under "What this does not say". So
  CEB is an instance of the case the theory leaves open, not of the case
  it proves. The arXiv v1 Eq. (30) also prints the inequality as
  "I(Y;Z) ≤", where the use made of it requires ≥.
- **[THEORY-035](../theory.d/THEORY-035.md) (Rejected) names the paper only in Connections**, as
  inheriting the IB programme. That is accurate. Fischer's §4 argues
  that compressed models generalise better, on the strength of Shamir et
  al.'s bound and Bassily et al., and the experiments show it in
  accuracy. But the paper measures compression by its own variational
  bounds on a stochastic encoder, not by binning a deterministic network.
  It makes no claim about a compression phase of SGD. So it neither
  supports nor bears on the account [THEORY-035](../theory.d/THEORY-035.md) rejects. Its
  generalisation claim is of the "IB term controls generalisation" kind
  that [THEORY-035](../theory.d/THEORY-035.md) attributes to [LIT-240](../literature.d/LIT-240.md) and [LIT-245](../literature.d/LIT-245.md).
- **On the heading the paper was filed under**, *relating K-complexity to
  minimum sufficient statistics*: the paper does not relate MNI to
  sufficiency formally. Footnote 2 avoids the word. MNI is the IB point
  where Z is a minimal sufficient statistic of X for Y in the information
  sense, but the paper never says so, and it never mentions Kolmogorov
  complexity.
- **Practice and theory separate cleanly.**
  - *Practice:* train with CEB at ρ = 0, with the consistent classifier
    or CatGen. That is an instruction for machine-learning practice, so
    it belongs in the anthology, and the `anthology-candidate` flag
    stands.
  - *Theory:* "retained information causes robust-generalisation
    failures" is stated as a hypothesis. It has no theorem behind it, and
    the evidence is two image datasets.

## Limitations

- Two datasets, Fashion MNIST and CIFAR-10. CIFAR-10 is tested only for
  (RG1) and (RG2), with one selected model per ρ. There are no error bars
  on Fig. 5.
- The (RG2) mechanism is an intuition: "In this work, we treat it as a
  hypothesis that we investigate empirically rather than theoretically."
- The (RG3) claim is reported as a property of "specific modeling
  choices". The MNI criterion "does not directly apply".
- The ReX-to-MNI reading holds only "assuming that our current classifier
  is optimal".
- The MNI point is attainable only for deterministic X → Y in the limit
  of a sufficiently powerful model. For noisy labels the paper gives no
  target.
- The unsupervised "theoretical optimality of noise functions" (App. C.3)
  assumes an oracle that already knows which inputs share a label. That
  is circular as a method, and the paper presents it as a constructive
  illustration.
- The arXiv v1 is a preprint. The Entropy version was not read.

## Open questions

- Does the MNI advantage survive at ImageNet scale and outside vision?
  The paper argues that log K ≥ I(X;Y) is "practical" there, but shows
  no result.
- Is CEB0's adversarial robustness stable under stronger or adaptive
  attacks? A third-party attack evaluation would decide it.
- For non-deterministic datasets, which ρ is the right target, and is it
  identifiable from data?
