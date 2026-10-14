---
number: 780
status: Read
formerly:
- NOTE-tmpdhrvi
paper: LIT-236
title: 'Sefidgaran, Gohari, Richard & Şimşekli — Rate-Distortion Theoretic Generalization Bounds'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv v2 PDF (arxiv.org/pdf/2203.02474, 49 pp.,
    29 Jun 2022, headed as PMLR vol. 178, COLT 2022), text extracted with
    pdftotext and page 11 re-extracted to check the worked example: §§1–5,
    Appendices A–D, and every proof in Appendix E (E.1–E.19). The proofs
    were followed step by step. The cited covering and error-exponent
    lemmas (Cuff et al.; Csiszár–Körner Lemma 9.1; Marton 1974; Berger
    Lemma 1) were taken as stated. The skim note filed with the paper is
    NOTE-200.
date: '2026-10-14'
summary: >-
  The expected generalisation error of any algorithm is at most
  √(2σ²·R/n) + ε, where R is the least mutual information I(S;Ŵ) of any
  surrogate output whose expected generalisation error is within ε. With
  ε = 0 this is Xu–Raginsky. With ε > 0 it stays finite where I(S;W) is
  infinite. For a Lipschitz loss R becomes the rate-distortion function of
  the output's marginal law, and as ε → 0 its rate-distortion dimension.
  A tail bound replaces I(S;W) by its supremum over laws within log(1/δ)
  in KL. Every bound depends on the unknown data distribution.
---
<!-- inactive-ok-file: THEORY-238 — Proposed; the account of LIT-245's bound, which descends from this framework, cited for context -->

# NOTE-780: Sefidgaran, Gohari, Richard & Şimşekli — Rate-Distortion Theoretic Generalization Bounds

## Contribution

The paper defines when a learning algorithm is compressible in Shannon's
block-coding sense, and proves that compressibility at rate R and
distortion ε bounds the generalisation error by √(2σ²R/n) + ε, in
expectation and with high probability. Three earlier families of bounds
come out as cases of it. Lossless compression gives the
mutual-information bound of Xu and Raginsky. Lossy compression with a
Lipschitz loss gives a rate-distortion bound on the output's marginal
law. Letting ε → 0 gives a rate-distortion dimension, which is a fractal
dimension. After it, I(S;W) has an operational reading, as the lossless
rate of a code for the algorithm's outputs.

## Key insight

What is compressed is not one trained model. It is a block of m
independent repetitions of the whole experiment, each with its own
training set S_i and its own output W_i. A "hypothesis book" of at most
e^{mR} candidate output blocks must, with probability tending to 1, hold a
block whose average generalisation error is within ε of the true one. The
generalisation error of a fixed book entry is a sum of independent
subgaussian terms, so a union bound over e^{mR} entries costs mR, and
dividing by m gives R. The rate R is a property of the algorithm's law,
not of any single output.

## Assumptions

- **Data and algorithm.** S = (Z_1, …, Z_n) i.i.d. from μ; a randomised
  algorithm P_{W|S}; gen(s, w) = L(w) − L̂(s, w).
- **Loss.** ℓ(Z, w) is σ-subgaussian for every w. Appendix A uses ℓ ∈
  [0, 1].
- **E|gen(S, W)| < ∞** for Theorem 2. Footnote 10 says the weaker
  |E gen| < ∞ is "seemingly true" but not shown.
- **Finite S and W** for the source-coding proofs (Theorems 3, 9 and the
  first proof of 10). The infinite case of Theorem 4 is proved separately
  (App. E.3), and of Theorem 10 by a second, variational proof (E.6.2).
- **Lipschitz loss** for Corollaries 6, 7, 11 and 26:
  |ℓ(z, w) − ℓ(z, ŵ)| ≤ L·ρ(w, ŵ).
- **Corollary 7** also assumes that sup_{ε'≤ε} RD(ε'; P_W, ρ)/log(1/ε')
  converges uniformly over n as ε → 0. P_W changes with n, so this is a
  strong assumption, and it is not discussed.

## Key results

- **Distortion (eq. 5).** d(w, ŵ; s) = gen(s, w) − gen(s, ŵ). It may be
  negative.
- **Theorem 2.** If A is (R, ε; |ϑ_m|)-compressible (Def. 1, block
  average distortion eq. 8), then |E gen(S, W)| ≤ √(2σ²R/n) + ε.
- **Theorem 3 (finite S, W).** A is (R_E(ε) + ν₁, ε + ν₂)-compressible
  for any ν₁, ν₂ > 0, where R_E(ε) = inf_{P_{Ŵ|S}} I(S; Ŵ) subject to
  |E[gen(S, W) − gen(S, Ŵ)]| ≤ ε (eq. 9). The proof uses Cuff et al.'s
  soft-covering construction.
- **Theorem 4.** |E gen(S, W)| ≤ √(2σ²R_E(ε)/n) + ε, for any spaces. The
  general proof (E.3) is two lines: the triangle inequality, then Xu and
  Raginsky's Theorem 1 applied to the surrogate Ŵ.
- **Corollary 5 (ε = 0).** |E gen| ≤ √(2σ²I(S; W)/n), which is Xu and
  Raginsky's bound.
- **Corollary 6 (Lipschitz).** |E gen| ≤ √(2σ²·RD(ε/(2L); P_W, ρ)/n) + ε,
  where RD is the rate-distortion function of the output's marginal law
  P_W. Footnote 12 gives the step: impose Ŵ – W – S, so I(S; Ŵ) ≤
  I(W; Ŵ).
- **The worked example (p. 11).** W is the mean of n Gaussian vectors in
  R^d, so I(S; W) = ∞. The paper's bound is min over ε of
  √(σ²d·log(2Ldσ₀²/(nε))/n) + ε, "which equals 2Ldσ₀²/n" at the top of
  the range. That expression is the Gaussian rate-distortion function
  for squared error, with the squared-error budget set to ε/(2L). But
  Corollary 6 needs E‖W − Ŵ‖₂ ≤ ε/(2L), unsquared. With consistent units
  the bound is of order √(d/n), up to a logarithm, not d/n.
- **Corollary 7 (rate-distortion dimension).** With dim_R(Q) =
  limsup_{ε→0} RD(ε; Q, ρ)/log(1/ε), for n ≥ n₀: |E gen| ≤
  √(4σ²·dim_R(P_W)·log(nL²)/n). dim_R is a lower bound on the
  Minkowski dimension of W, and equals the Rényi information dimension
  under conditions (Kawabata–Dembo).
- **Theorem 9 (tail).** If A is exponentially compressible (Def. 8, a
  covering failure that decays like δ^m) under the distortion φ_m of
  eq. 12, then with probability ≥ 1 − δ, gen(S, W) ≤ √(2σ²(R +
  log(1/δ))/n) + ε. The bound is one-sided.
- **Theorem 10 (tail, any algorithm).** With probability ≥ 1 − δ,
  gen(S, W) ≤ √(2σ²(R_p(δ, ε) + log(1/δ))/n) + ε, where R_p(δ, ε) =
  sup over Q with D_KL(Q‖P_{S,W}) ≤ log(1/δ) of RD*(ε; Q). At ε = 0,
  eq. 15: the supremum of I_Q(S; W) over the same KL ball. The authors
  call it "the first information-theoretic tail bound on the
  generalization error with the logarithmic dependence on 1/δ".
- **Theorem 12 / Lemma 24.** A variational formula for the tail
  probability of any real random variable, log P(X ≥ Δ) = sup over ν_X ≪
  μ_X of the infimum of −D_KL(ν_X‖μ_X) − λ[Δ − ε − E X̂]₊. Its first
  proof (E.15.1) shows it is an identity: the optimal ν is μ conditioned
  on [Δ, ∞).
- **Appendix A (conditional compressibility).** With a ghost sample and
  bounded loss, the bounds recover Steinke–Zakynthinou's CMI bound and
  VC bounds: |E gen| ≤ √(2d log(2en/d)/n) (Corollary 18), and a tail
  version (Corollary 22).
- **Appendix B.1.** Donsker–Varadhan's inequality is re-derived by a
  covering argument, for finite alphabets.
- **Corollary 26 (examples).** For W in a ball of radius r₀ in R^d with an
  L-Lipschitz loss, with probability ≥ 1 − e^{−d/2}, gen ≤ (4r₀L +
  σ√d)√(log n/n) for n ≥ 16. This is the ε-net bound.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | I(S;W) in Xu–Raginsky's bound is an upper bound on the lossless compression rate of the algorithm | strong | Theorems 2–3 and Corollary 5, finite alphabets; the operational reading is proved only there |
| C2 | The expected generalisation error is at most √(2σ²·R_E(ε)/n) + ε, for any surrogate Ŵ within ε | strong | Theorem 4, proved in general by E.3 |
| C3 | With a Lipschitz loss, the rate-distortion function of P_W bounds the expected generalisation error, and stays finite where I(S;W) is infinite | moderate | Corollary 6; the one worked example has a units error |
| C4 | The expected generalisation error is controlled by the rate-distortion dimension of P_W | weak | Corollary 7, under an unexamined uniform-convergence assumption in n |
| C5 | A high-probability bound needs the algorithm compressible under every law within log(1/δ) in KL of P_{S,W} | strong | Theorem 10, two proofs |
| C6 | The rate-distortion framework recovers CMI and VC bounds | moderate | Theorem 17 (proof omitted), Corollaries 18, 22 |

## Method

The block-coding construction: m independent copies of (S, W); a
hypothesis book H_m of at most e^{mR} blocks ŵ_j ∈ Ŵ^m; the optimal
compressor maps each realised block to the book entry of least
distortion; the error event (eq. 6) is that the least distortion exceeds
ε. For expectation bounds the distortion is the block average ϑ_m (eq. 8).
For tail bounds it is φ_m (eq. 12), the gap between the smallest
generalisation error in the block and the average of the compressed ones.
Covering failure must vanish (Def. 1) or decay like δ^m (Def. 8). The
tail theorems use "information-theoretic covering" (§4.1): cover only the
typical set of the block, not the whole space.

## Concepts

- **(R, ε; d_m)-compressible algorithm.** One whose output blocks can be
  covered at rate R within average distortion ε under d_m, with
  probability tending to 1.
- **Hypothesis book.** The codebook H_m ⊆ Ŵ^m of candidate output blocks.
- **R_E(ε).** The least I(S; Ŵ) over surrogates Ŵ, built from S, whose
  expected generalisation error is within ε of the algorithm's.
- **Rate-distortion dimension.** limsup_{ε→0} RD(ε; Q, ρ)/log(1/ε).
- **Lossless vs lossy.** ε = 0 against ε ≠ 0.

## Connections

The paper builds on Russo–Zou ([LIT-356](../literature.d/LIT-356.md)) and Xu–Raginsky ([LIT-347](../literature.d/LIT-347.md)), whose
bound is its lossless case. It treats the compression bounds of
Littlestone–Warmuth and Arora et al., and the fractal-dimension bounds of
Şimşekli et al., as the other two families it unifies. Negrea et al.'s
surrogate hypotheses are named as an informal precursor of lossy
compression (footnote 11). The conclusion lists computing the bounds,
relating dim_R to other fractal dimensions, and a link to PAC-Bayes as
future work. Sefidgaran and Zaidi's [LIT-233](../literature.d/LIT-233.md) carries out the PAC-Bayes link
and calls this paper's framework "fixed-size" and data-independent. The
same group's [LIT-245](../literature.d/LIT-245.md) applies a related block-coding argument to
representations.

## Bearing on the record

- **[THEORY-028](../theory.d/THEORY-028.md) needs updating.** Its "What this does not say" says
  "Lossy and data-dependent refinements ([LIT-236](../literature.d/LIT-236.md), [LIT-233](../literature.d/LIT-233.md)) exist but are
  Deferred and unread." Both are now read. On this paper it should say
  three things.
  - The lossy bound (Theorem 4) is a third remedy beside quantisation and
    injected noise, and the general proof is Theorem 1 of [LIT-347](../literature.d/LIT-347.md)
    applied to a surrogate Ŵ. No new information inequality is needed.
  - Its "Anything beyond expectation" item can name Theorem 10, a tail
    bound with log(1/δ) dependence that pays by replacing I(S;W) with
    its supremum over a KL ball around P_{S,W}.
  - It does not change the "informative for deterministic training" item
    for neural networks. The paper evaluates no bound for a network, and
    its one analytic example has a units error (Key results).
- **[NOTE-306](NOTE-306.md)'s bearing on this paper** is accurate: the lossless reading,
  and lossy bounds finite where I(S;W) is infinite. Its later line,
  that the per-step information of a training run "is what [LIT-236](../literature.d/LIT-236.md)'s
  lossy rates try to estimate", is not what this paper does. Its rates
  are of the final output's law, P_{S,W} or P_W. It treats no
  trajectory and estimates nothing. The trajectory version is
  [LIT-233](../literature.d/LIT-233.md)'s Theorem 7.
- **[NOTE-241](NOTE-241.md)** describes the compressibility as lossy compressibility of
  the output relative to its effect on the loss. That is accurate.
- **[LIT-347](../literature.d/LIT-347.md)'s status note** says the vacuity for deterministic algorithms
  on continuous hypotheses "is what the later compression and
  rate–distortion refinements ([LIT-236](../literature.d/LIT-236.md), [LIT-233](../literature.d/LIT-233.md)) address". For this paper
  that is right, in principle.
- **The heading the paper was filed under (K-complexity and minimal
  sufficient statistics).** The paper has no Kolmogorov complexity and no
  sufficient statistic. Its compression is Shannon block coding of an
  i.i.d. source of experiments. One echo, which is mine: R_E(ε) asks for
  the least-informative surrogate Ŵ that preserves expected
  generalisation error. That is a rate-distortion analogue of a
  statistic that is sufficient for one functional of the loss. The paper
  does not draw it.
- **[THEORY-238](../theory.d/THEORY-238.md)** (from [LIT-245](../literature.d/LIT-245.md)) uses a related block-coding bound for
  representations. This paper is the framework it descends from.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- **Every bound depends on μ** through P_{S,W} or P_W, and so cannot be
  computed from one sample. [LIT-233](../literature.d/LIT-233.md) §I says so, and this paper's
  Corollary 6 discussion concedes that knowing P_W is still needed.
- **The operational, source-coding meaning is proved for finite
  alphabets only.** For general spaces Theorem 4 is a surrogate argument,
  and the compression interpretation is a reading of it.
- **No bound is computed for a learned model.** The examples are a
  Gaussian mean, an ε-net ball, and i.i.d. Bernoulli, Laplace and Gaussian
  coordinates.
- **The Gaussian example's arithmetic** mixes squared and unsquared
  distortion (Key results), so its d/n rate is unsupported.
- **Corollary 7's uniform-convergence assumption** is over n, while P_W
  itself depends on n. The paper does not discuss when it holds.
- **The tail bounds are one-sided.** Theorem 10 can be worse than
  Hoeffding when S and W are independent (App. D.2), because I_Q(S; W)
  need not vanish for Q in the KL ball.
- Theorem 17's proof is omitted as "similar".

## Open questions

- Can R_E(ε) or RD(ε; P_W) be estimated for a trained network well enough
  to give a non-vacuous bound? The paper names this as future work.
- How does dim_R(P_W) relate to the trajectory dimensions used in
  fractal bounds, given that P_W is the law of the final output over
  datasets, not a set traced by one run?
- Is there a surrogate-based bound whose rate is computable from one
  sample? [LIT-233](../literature.d/LIT-233.md) answers in part.
