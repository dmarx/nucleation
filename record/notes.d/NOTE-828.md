---
number: 828
status: Read
formerly:
- NOTE-tmp8mfe9
paper: LIT-256
title: 'Belghazi et al. — Mutual Information Neural Estimation'
version: 2
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (1801.04062v5, 14 Aug 2021, 18 pages),
    text extracted with pdftotext in reading-order and layout modes:
    abstract, §§1–6, every table and figure caption, and the whole
    appendix (8.1 experimental details, 8.2.1 the Donsker–Varadhan proof,
    8.2.2 the consistency proofs, 8.2.3 the sample-complexity proof, 8.2.4
    the reconstruction bound, 8.3). Pages 4 and 15 were rendered as images
    to read Theorem 3 and to check the direction of the Radon–Nikodym
    derivative in Eqs. 25 and 30, which the text layer garbles. Figure 1 is
    a plot without a text layer and was read from the image and caption.
    The ICML version (PMLR 80:531–540) was not compared. Replaces the
    seeded skim NOTE-224.
- version: 2
  date: '2026-10-17'
  note: >-
    Annotated with the now-held Kraskov et al. (LIT-1163) at the 20-dimension comparison.
date: '2026-10-14'
summary: >-
  Mutual information is the KL divergence of the joint from the product of
  marginals, and its Donsker–Varadhan dual is tight exactly at the log
  Radon–Nikodym derivative plus a constant. Maximizing that dual over a
  compact family of neural critics gives an estimator that is strongly
  consistent, for the exact empirical maximizer, on a compact domain with
  Lebesgue densities, with a uniform deviation bound of order d log d/ε²
  in the parameter count d. The mini-batch gradient is biased; a moving
  average is offered as a heuristic fix without proof.
---
<!-- inactive-ok-file: THEORY-237 THEORY-001 THEORY-308 NOTE-224 — Proposed, Deferred or Superseded; the family account that cites this paper, the account set beside it, the consistency account filed from this reading, Adler's coda named in the skim, and the skim this reading replaces -->

# NOTE-828: Belghazi et al. — Mutual Information Neural Estimation

## Contribution

Before this paper, estimators of mutual information between
high-dimensional continuous variables were nonparametric (binning, k-NN,
kernel densities) and scaled badly with dimension. The paper makes the
Donsker–Varadhan dual of the KL divergence a training objective for a
neural "statistics network", calls the result MINE, and proves two
things about it: that the supremum over a compact family of networks can
approximate MI arbitrarily well, and that its empirical version converges
to that supremum almost surely. It adds a uniform sample-complexity bound
in the number of network parameters, and uses the estimator as a
differentiable MI term in GAN, ALI and information-bottleneck objectives.

## Key insight

The Donsker–Varadhan bound has an exact gap: for any critic T, the
distance from KL(P‖Q) to E_P[T] − log E_Q[e^T] is itself a KL
divergence, KL(P‖G), where G is the Gibbs measure dG = e^T dQ / E_Q[e^T].
So maximizing the bound is fitting a Gibbs reweighting of Q to P, and the
optimum is the critic whose Gibbs measure is P itself: the log
Radon–Nikodym derivative dP/dQ, up to an additive constant. A neural
network trained on the bound is therefore a log density-ratio estimator,
and its value at the optimum is the divergence.

## Assumptions

- **Measure-theoretic setting (§1–2.1).** I(X;Z) = ∫ log [dP_XZ /
  d(P_X⊗P_Z)] dP_XZ (Eq. 1); KL(P‖Q) := E_P[log dP/dQ] "whenever P is
  absolutely continuous with respect to Q", infinite otherwise (Eq. 4,
  footnote 2). Footnote 1 invites the reader to think of Lebesgue
  densities on a compact Ω ⊂ R^d.
- **Theorem 1 (DV).** The supremum is "over all functions T such that the
  two expectations are finite".
- **Consistency (App. 8.2.2).** "the input space Ω = X × Z is a compact
  domain of R^d, and all measures are absolutely continuous with respect
  to the Lebesgue measure"; feedforward networks "with continuous
  activations, with a single output neuron", so (ω, θ) ↦ T_θ(ω) is
  continuous on Ω × Θ; Θ ⊂ R^k compact. The main-text Lemma 2 says
  "bounded"; the proof needs compactness, and the appendix says so.
- **Sample complexity (Thm 3).** T_θ L-Lipschitz in θ; |T_θ| ≤ M and
  e^{T_θ} ≤ M; ‖θ‖ ≤ K, Θ ⊂ R^d.
- **The estimator is the exact empirical maximizer.** Definition 3.1
  takes sup over θ ∈ Θ of the empirical objective. Every guarantee is
  about that supremum, not about what gradient ascent reaches.

## Key results

- **Theorem 1, Donsker–Varadhan (Eq. 5; App. 8.2.1, Eqs. 22–26).**
  KL(P‖Q) = sup_T E_P[T] − log E_Q[e^T]. Proof: with dG = e^T dQ / Z,
  Z = E_Q[e^T], one has E_P[T] − log Z = E_P[log dG/dQ] (Eq. 23), so the
  gap Δ = KL(P‖Q) − (E_P[T] − log E_Q[e^T]) equals E_P[log dP/dG] =
  KL(P‖G) ≥ 0 (Eq. 25). "the bound is tight whenever G = P, namely for
  optimal functions T* taking the form T* = log dP/dQ + C for some constant
  C ∈ R." *Holds when:* P ≪ Q and both expectations finite. The paper
  says "whenever". The converse follows from Eq. 25, since KL(P‖G) = 0
  only if G = P. One consequence the paper does not draw: G has a strictly
  positive density e^T/Z with respect to Q, so G = P forces P and Q to be
  mutually absolutely continuous. When P_XZ vanishes on a set of positive
  P_X⊗P_Z measure, no real-valued critic attains the supremum, and it is
  only approached.
- **Eq. 7.** The same tightness in the main text: dP = (1/Z)e^{T*} dQ.
- **f-divergence (NWJ) bound (Eq. 8).** KL(P‖Q) ≥ sup_T E_P[T] −
  E_Q[e^{T−1}]. For any fixed T the DV value is at least the NWJ value
  (footnote 4, from x ≥ e log x at x = E_Q[e^T]). "MINE-f" is the
  estimator built on Eq. 8.
- **Neural information measure (Eqs. 9–10).** I(X;Z) ≥ I_Θ(X,Z) :=
  sup_θ E_{P_XZ}[T_θ] − log E_{P_X⊗P_Z}[e^{T_θ}]. A population-level
  inequality.
- **MINE (Def. 3.1, Eq. 11).** Î(X;Z)_n = sup_θ E_{P^(n)_XZ}[T_θ] −
  log E_{P^(n)_X ⊗ P̂^(n)_Z}[e^{T_θ}]. Algorithm 1 draws b joint pairs and b
  marginal samples of Z (or shuffles Z along the batch). The paper does
  not say whether a finite-sample Î_n is a lower bound. It is not, in
  general: the log of an empirical mean is biased (Poole et al., [LIT-246](../literature.d/LIT-246.md),
  [NOTE-739](NOTE-739.md)).
- **Gradient bias (§3.2, Eq. 12).** The mini-batch gradient
  E_B[∇T] − E_B[∇T e^T]/E_B[e^T] is a biased estimate of the full-batch
  gradient. Replacing the denominator by an exponential moving average
  "can be made to have arbitrarily small bias" for small learning rates.
  That is asserted, not proved. Footnote 6 notes that MINE-f's gradients
  are unbiased.
- **Lemma 1 / 3, approximation (App. 8.2.2, Eqs. 28–37).** For every
  η > 0 there is a network family with compact Θ such that
  |I(X,Z) − I_Θ(X,Z)| ≤ η. Proof: T* = log dP/dQ satisfies E_P[T*] = I and
  E_Q[e^{T*}] = 1 (Eq. 30), and the gap is bounded by
  E_P|T* − T| + E_Q|e^{T*} − e^T| (Eq. 31, by log x ≤ x − 1). If T* ≤ M,
  universal approximation in L¹(P + Q) (Hornik 1989, footnote 8) and the
  e^M-Lipschitz bound on exp give the result. Otherwise they split Ω at
  {T* > M}, using integrability of T* under P (footnote 9) and of e^{T*}
  under Q. *Reader's note:* Eqs. 32 and 35 need E_Q|T* − T_θ| small, so the
  proof as written needs T* finite Q-almost everywhere and Q-integrable on
  {T* ≤ M}. It truncates T* from above only. Where P_XZ vanishes on a set
  of positive P_X⊗P_Z measure, T* = −∞ there and the stated bound cannot
  hold. A truncation from below, which costs little because e^{T*} is
  small there, would likely repair it, but the paper does not give one.
- **Lemma 2 / 4, estimation (Eqs. 38–42).** For a fixed compact family,
  "there exists N ∈ N such that ∀n ≥ N, Pr(|Î_n − I_F| ≤ η) = 1". Proof:
  continuous T_θ on compact Θ × Ω are uniformly bounded by M; log is
  e^M-Lipschitz on [e^{−M}, e^M] (Eq. 40); the uniform law of large numbers
  (van de Geer 2000) controls sup_θ |E_P T_θ − E_{P_n} T_θ| and the same for
  e^{T_θ} (Eq. 41). *Reader's note:* the uniform law gives almost-sure
  convergence, sup_θ |…| → 0 a.s., with a sample-path-dependent N. It does
  not give one deterministic N after which the deviation is ≤ η with
  probability one, which is what Eq. 38 states. The conclusion that
  survives is Î_n → I_F almost surely, which is what strong consistency
  needs.
- **Theorem 2 / 5, strong consistency (Def. 3.2, Eq. 43).** For every ε
  there are a network family and an N such that |I − Î_n| ≤ ε for n ≥ N,
  "a.e." The family is chosen after ε. The triangle inequality joins
  Lemmas 1 and 2. *Holds when:* the 8.2.2 assumptions, the reader's
  caveats on the two lemmas, and the exact empirical supremum.
- **Theorem 3 / 6, sample complexity (Eqs. 14–15, 44–53).**
  Pr(|Î_n − I_Θ| ≤ ε) ≥ 1 − δ whenever
  n ≥ 2M²(d log(16KL√d/ε) + 2dM + log(2/δ))/ε², i.e. Õ(d log d/ε²) with d
  the number of parameters. Proof: Hoeffding, a covering of the parameter
  ball with N_η(Θ) ≤ (2K√d/η)^d (Shalev-Shwartz & Ben-David), radius
  η = εe^{−2M}/(8L), and a union bound. *Holds when:* the Thm 3
  assumptions, which exclude an unbounded optimal critic. The bound is in
  the parameter count, not the data dimension, and it controls deviation
  from I_Θ, not from I.
- **Experiments (§4).**
  - Correlated Gaussians with componentwise correlation ρ (Fig. 1): MINE
    and Kraskov's k-NN estimator are "virtually indistinguishable" from the
    truth in 2 dimensions. In 20 dimensions MINE is much closer than
    Kraskov's, and, by the figure, still below the true MI at large |ρ|.
    (Annotated 2026-10-17: Kraskov et al. is now held, [LIT-1163](../literature.d/LIT-1163.md), read in
    [NOTE-938](NOTE-938.md). Its own Gaussian tests, Fig. 15 at N = 50 000, report
    agreement "for all dimensions tested here"; the reading did not
    recover the largest d tested, so whether d = 20 lies inside that range
    is open. MINE's comparison may also differ in N and k, which this note
    does not record.)
    MINE is tighter than MINE-f.
  - Y = f(X) + σ⊙ε with f ∈ {x, x³, sin x} (Fig. 2): the MINE estimate
    depends on σ, not on f, which the paper calls equitability.
- **Applications (§5).**
  - GAN + MINE: the generator maximizes I(G([ε,c]); c) (Eq. 17), with the
    MI gradient clipped to the discriminator's norm (Eq. 21). It covers all
    modes on spiral and 25-Gaussians, and all 1000 Stacked-MNIST modes with
    KL 0.05 (Table 1).
  - ALI + MINE: App. 8.2.4 proves the reconstruction error
    R ≤ KL(q(x,z)‖p(x,z)) − I_q(x,z) + H_q(z) (Eq. 58), tight when the
    aggregated posterior q(z) equals the prior. MINE improves
    reconstruction over ALI on MNIST and CelebA (Table 2).
  - Information bottleneck: §5.3 writes the IB Lagrangian as
    H(Y|Z) + βI(X,Z) (Eq. 20) and estimates I(X,Z) with MINE, which needs
    only samples of the encoder, not its density. Permutation-invariant
    MNIST error falls to 1.01–1.11% against DVB's 1.13% (Table 3,
    averaged over ten runs).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | MI is the expected log Radon–Nikodym derivative of the joint with respect to the product of marginals | strong | definition, Eqs. 1, 3–4 |
| C2 | The DV gap for a critic T is KL(P‖G_T), so the bound is tight exactly at T = log dP/dQ + C | strong | App. 8.2.1, Eq. 25; the converse and the mutual-absolute-continuity condition are the reader's |
| C3 | For fixed T, the DV value is at least the NWJ value | strong | footnote 4 |
| C4 | The supremum over some compact neural family approximates MI within any η | moderate | Lemma 3; the proof handles only upper truncation of T* |
| C5 | The empirical supremum over a fixed compact family converges almost surely to its population value | moderate | Lemma 4 via the uniform LLN; the stated quantifier (deterministic N) is stronger than the argument gives |
| C6 | MINE is strongly consistent | moderate | Thm 2 = C4 + C5, for the exact empirical maximizer |
| C7 | Uniform deviation ≤ ε with probability 1 − δ after Õ(d log d/ε²) samples, d the parameter count | strong | Thm 3, Hoeffding plus covering, under boundedness and Lipschitz assumptions |
| C8 | The moving-average gradient has arbitrarily small bias at small learning rates | weak | asserted in §3.2, no proof |
| C9 | MINE estimates MI better than k-NN in 20 dimensions and is invariant to the deterministic part of Y = f(X) + noise | moderate | Figs. 1–2, toy Gaussians and 1-D functions |
| C10 | Reconstruction error in bidirectional models is bounded by KL(q‖p) − I_q + H_q(z) | strong | App. 8.2.4, an identity plus KL ≥ 0 |

## Method

Draw b pairs from the joint and b samples of Z from its marginal (or
shuffle Z in the batch); evaluate V(θ) = (1/b)Σ T_θ(x_i, z_i) −
log((1/b)Σ e^{T_θ(x_i, z̄_i)}); ascend the gradient with the denominator
replaced by a moving average; repeat to convergence (Algorithm 1). When
MI is a regularizer for another network, the MI gradient is clipped to
the norm of that network's own loss gradient (Eq. 21).

## Concepts

- **Statistics network** — the critic T_θ: X × Z → R in the DV dual.
- **Neural information measure I_Θ** — the population DV bound
  maximized over a parametric family (Eq. 10), a lower bound on MI.
- **Strong consistency** — as defined here, for every ε a choice of
  network and an N after which the estimate is within ε almost surely
  (Def. 3.2).
- **Gibbs distribution G_T** — dG = e^T dQ / E_Q[e^T]; the DV gap is
  KL(P‖G_T).
- **Equitability** — an MI estimate that depends on the noise level and
  not on the deterministic transformation (Kinney & Atwal 2014).

## Connections

It builds on Donsker & Varadhan (1983), Nguyen, Wainwright & Jordan
(2010), Nowozin et al.'s f-GAN, and Ruderman et al. (2012), who derive
both bounds by Fenchel duality. Footnote 3 identifies Eq. 6 as the
compression lemma of PAC-Bayes (Banerjee 2006). Poole et al. ([LIT-246](../literature.d/LIT-246.md),
read in [NOTE-739](NOTE-739.md)) later place the DV, NWJ and MINE objectives inside one
family derived from an unnormalized Barber–Agakov bound. They show the
Monte-Carlo DV estimate is neither an upper nor a lower bound, and that
MINE's moving-average gradient is the exact gradient of a valid bound,
TUBA. That is the proof §3.2 lacks. Tschannen et al. ([LIT-247](../literature.d/LIT-247.md)) argue
that maximizing such estimates is not what makes representations good.

## Bearing on the record

- **[THEORY-006](../theory.d/THEORY-006.md) and [THEORY-237](../theory.d/THEORY-237.md) cite this paper correctly.** Both cite
  Eqs. 1, 3–4 and App. 8.2.1 for MI as the expected log Radon–Nikodym
  derivative and for DV tightness at that log derivative plus a
  constant. The paper states both. Two precisions:
  - The paper says "whenever". "Exactly", in both theories, is the
    converse, which follows from Eq. 25 but is not stated.
  - The supremum is attained by a real-valued critic only if P_XZ and
    P_X⊗P_Z are mutually absolutely continuous. Otherwise it is
    approached, not attained. Neither theory needs more than this, but
    "tight at" should be read as "the supremum is reached in the limit"
    when the joint vanishes where the product does not.
- **[THEORY-237](../theory.d/THEORY-237.md) lists "MINE's" bound among the relaxations.** Correct for
  the population objective (Eqs. 9–10), which is the DV bound. The
  finite-sample estimator (Eq. 11) is not a bound. The paper never claims
  it is, and says nothing about its finite-sample bias beyond the
  gradient. [THEORY-237](../theory.d/THEORY-237.md)'s "MINE's bias-corrected gradient is the exact
  gradient of TUBA" is Poole et al.'s result, not this paper's. Here the
  moving average is only a heuristic.
- **What the skim asked ([NOTE-224](NOTE-224.md)).**
  - *How §3 handles the Monte-Carlo DV bias.* It treats only the
    gradient bias (§3.2, heuristically). The estimate's own bias is
    covered only asymptotically, by consistency.
  - *What "strongly consistent" is proved under.* A compact domain,
    Lebesgue densities, continuous activations, compact Θ, and the exact
    empirical supremum, with the two gaps in the proof noted under Key
    results.
  - *The information bottleneck (§5.3).* It is stated with entropies and
    MI, H(Y|Z) + βI(X,Z), in neither the Radon–Nikodym form nor density
    form. Its point is that MINE needs no encoder density. The density
    notation of §5.2 (footnote 7) does not extend to it.
- **No existing THEORY holds the consistency and sample-complexity
  results.** [THEORY-308](../theory.d/THEORY-308.md) is filed from this reading, held to what
  the proofs establish.
- **[THEORY-001](../theory.d/THEORY-001.md).** The DV optimum is the log density ratio plus a
  constant, unique up to that constant. That is a general-density
  instance of the shared optimum [THEORY-001](../theory.d/THEORY-001.md) names. This paper treats DV
  only, not the spectral or logistic losses.
- The paper carries ML-practice content: using MINE to regularize GANs,
  ALI and the IB, and gradient clipping. That is the anthology's kind of
  material, and the `anthology-candidate` flag stands.

## Limitations

- Consistency is for the exact supremum over θ. Nothing is shown about
  gradient ascent, local optima, or how large the network must be for a
  given η.
- The sample-complexity bound assumes bounded critics and e^{T_θ} ≤ M,
  which excludes the unbounded log-ratio that large MI requires. Its
  constants grow like e^{2M}, so it is vacuous for high MI.
- No finite-sample bias result for the estimate itself. A Monte-Carlo DV
  estimate is neither an upper nor a lower bound ([LIT-246](../literature.d/LIT-246.md)).
- Experiments are on synthetic Gaussians, 1-D functional relations, and
  standard image benchmarks. The 20-dimensional estimate falls below
  the truth at high correlation (Fig. 1).
- The abstract's "linearly scalable in dimensionality as well as in
  sample size" is a computational claim. No theorem addresses it.

## Open questions

- Does Lemma 3 hold, with a lower truncation, when the joint vanishes on
  a set of positive product measure? The likely answer is yes; a
  corrected proof would settle it.
- At what rate does Î_n approach I when the family grows with n? The
  paper fixes the family, and an approximation-estimation trade-off
  would need a rate for Lemma 1.
- Does the moving-average gradient converge to a stationary point of the
  DV bound? Poole et al.'s TUBA reading suggests it does, for a different
  bound.
