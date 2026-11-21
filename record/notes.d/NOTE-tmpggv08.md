---
status: Read
paper: LIT-tmpipm3o
title: 'Baik, Ben Arous and Péché, Phase transition of the largest eigenvalue for nonnull complex sample covariance matrices, read for the spiked threshold'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    Read on 2026-11-21 by a delegated reader from arXiv math/0403022v2
    (21 Oct 2004), the authors' PDF: §1 in full (the known results, the
    definitions, Theorem 1.1, Corollary 1.1, Proposition 1.1, the
    Conjecture, Theorem 1.2), §2.1 and §6. The steepest-descent proofs of
    §§3–5 (pp. 14–48) were skipped, so the results are taken as stated. The
    published version (Ann. Probab. 33(5), 2005) was not fetched; v2
    postdates the correction of a typographical error in the main theorem
    that it credits to Paul. Running notes on the branch
    claude/readers/lit-tmpipm3o (ADR-108). Three works read beside it for
    what the record's entries need and this paper does not give, each with
    its own entry (ADR-114): Baik and Silverstein (LIT-tmpjtw0k), Paul
    (LIT-tmpxru3g), Benaych-Georges and Nadakuditi (LIT-tmp1q78e). Every
    quotation below rechecked by the filer by script against the
    downloaded text, and the change of notation checked by hand.
date: '2026-11-21'
summary: >-
  The proof that a spike in a population covariance separates the largest
  sample eigenvalue from the bulk exactly when it exceeds 1 + γ⁻¹ (M/N = γ²
  samples per variable), with Tracy–Widom fluctuations of order M^(−2/3)
  below, Gaussian-type ones of order M^(−1/2) above, and new laws at and
  near the threshold. Only for complex Gaussian samples, at least as many
  samples as variables, and the largest eigenvalue: the real case is a
  conjecture here, and eigenvectors are not treated.
---
<!-- inactive-ok-file: THEORY-tmp0covn THEORY-tmp0zr7o THEORY-tmp6808g THEORY-tmp4zojc CLAIM-tmp5y856 CASE-tmp59xy5 CLAIM-tmpk33au CLAIM-tmp8mvx8 CLAIM-tmpqbo50 ARG-tmppdhhb ARG-tmpvalfs ARG-tmpnwmcr ARG-tmpe2vrk — Proposed; the readings and the entries of 2026-11-21 this reading bears on -->

# NOTE-tmpggv08: Baik, Ben Arous and Péché, Phase transition of the largest eigenvalue for nonnull complex sample covariance matrices, read for the spiked threshold

## Contribution

The first proof that the spiked threshold is sharp, and the first limiting
laws for the largest sample eigenvalue across it, the "BBP transition". The
method is a Fredholm-determinant formula for the largest eigenvalue that
exists only for complex samples (an HCIZ integral over the unitary group).
The reading is [THEORY-tmp0covn](../theory.d/THEORY-tmp0covn.md).

## Key results

Notation: M samples of N variables, M/N = γ² ≥ 1; population eigenvalues
ℓ_1 ≥ … all 1 but for r of them.

- **Setting** (§1.1, pp. 2–3). "We assume that the samples ~y are complex
  Gaussian with mean ~µ and covariance Σ." The sample covariance is centred
  by the sample mean, X being "the (centered) N × M sample matrix".
- **Theorem 1.1** (p. 8). As M, N → ∞ with M/N = γ² in a compact subset of
  [1, ∞): (a) at ℓ_1 = … = ℓ_k = 1 + γ⁻¹, λ_1 centred at (1 + γ⁻¹)² and
  scaled by M^(2/3) tends to a new law F_k; (b) with ℓ_1 = … = ℓ_k in a
  compact subset of (1 + γ⁻¹, ∞), λ_1 centred at ℓ_1 + ℓ_1γ⁻²/(ℓ_1 − 1)
  and scaled by √M tends to G_k, the law of the largest eigenvalue of a
  k × k GUE matrix. Below the threshold, the edge's Tracy–Widom law
  (§1.1).
- **Corollary 1.1** (pp. 9–10). λ_1 → (1 + γ⁻¹)² in probability below the
  threshold and λ_1 → ℓ_1(1 + γ⁻²/(ℓ_1 − 1)) above it; "λ1 is separated
  from the rest of eigenvalues if and only if at least one eigenvalue of Σ
  is greater than 1 + γ⁻¹."
- **No reason given for the threshold** (p. 10): "Here the critical value
  1 + γ⁻¹ comes from a detail of computations and we do not have an
  intuitive reason yet." §6 offers a last-passage-percolation heuristic.
- **The real case is open** (p. 11): "The real question is the real sample
  covariance … Conjecture. For real sample covariance, the Theorem 1.1
  still holds true for different limiting distributions but with the same
  scaling." The technique is "not applicable to real sample matrices"
  (p. 13).
- **The critical window** (Theorem 1.2, p. 12). Spikes
  ℓ_j = 1 + γ⁻¹ − (1 + γ)^(2/3)w_j/(γM^(1/3)) give interpolating laws, so
  the transition has width of order M^(−1/3) in ℓ.
- **Fixed N** (Proposition 1.1, p. 10). With N fixed the top eigenvalue
  concentrates at ℓ_1; in the large-N case (b) the outlier's location
  depends on the unit eigenvalues too.

## Assumptions

Complex Gaussian samples; finitely many spikes, r fixed; M ≥ N, with M/N in
a compact set; spikes in compact sets away from the threshold except in
Theorem 1.2; a covariance centred by the sample mean, which for mean-zero
data is asymptotically the same as the uncentred one.

## Concepts

Spiked population model (Johnstone); the BBP transition; Tracy–Widom
F_GUE; the new laws F_k and the finite-GUE laws G_k; the Laguerre unitary
ensemble; the link to last-passage percolation and queues.

## Connections

The record's entries use the threshold in its own notation: D variables, N
samples, γ_rec = D/N, spike β = ℓ − 1. Then γ_BBP⁻¹ = √γ_rec, the threshold
ℓ > 1 + γ_BBP⁻¹ is β > √γ_rec, the outlier ℓ(1 + γ_BBP⁻²/(ℓ − 1)) is
(1 + β)(1 + γ_rec/β), and the edge is (1 + √γ_rec)². All agree with the
entries. But BBP needs γ_rec ≤ 1. What the entries need beyond that is in
three other works: real or non-Gaussian samples, any γ_rec and each of
several spikes in Baik and Silverstein ([THEORY-tmp0zr7o](../theory.d/THEORY-tmp0zr7o.md)); the eigenvector
overlap in Paul ([THEORY-tmp6808g](../theory.d/THEORY-tmp6808g.md)); the additive, uncentred models in
Benaych-Georges and Nadakuditi ([THEORY-tmp4zojc](../theory.d/THEORY-tmp4zojc.md)).

## Bearing on the record

- **[CLAIM-tmp5y856](../claims.d/CLAIM-tmp5y856.md)** (supports the threshold, qualifies the rest). Corollary
  1.1 gives β > √γ and the location; the opening (β − √γ)²/β is
  (1 + β)(1 + γ/β) − (1 + √γ)² by algebra. The eigenvector sentence is
  Paul's or Benaych-Georges and Nadakuditi's, not BBP's; real data needs
  Baik and Silverstein. BBP's own "phase transition" is a change in the law
  of λ_1, of fluctuation order M^(−2/3) to M^(−1/2), which fits the claim's
  reading of it as a detectability transition. [ARG-tmppdhhb](../arguments.d/ARG-tmppdhhb.md), [ARG-tmpvalfs](../arguments.d/ARG-tmpvalfs.md),
  [ARG-tmpnwmcr](../arguments.d/ARG-tmpnwmcr.md).
- **[CASE-tmp59xy5](../cases.d/CASE-tmp59xy5.md)** (qualifies). The formulas are exact after the change of
  notation, but the ±1 mixture is real and non-Gaussian; it is Benaych-Georges
  and Nadakuditi's additive rank-one model, not BBP's. [ARG-tmpe2vrk](../arguments.d/ARG-tmpe2vrk.md).
- **[CLAIM-tmpk33au](../claims.d/CLAIM-tmpk33au.md)** (qualifies). BBP centres by the sample mean, which
  would remove a mean shift; PCA of the uncentred second moment seeing a
  mean shift c as a spike β = c² is Benaych-Georges and Nadakuditi's
  additive model (θ = c), whose threshold θ > γ^(1/4) gives the claim's
  κ_BBP = √D·(D/N)^(1/4). [ARG-tmpe2vrk](../arguments.d/ARG-tmpe2vrk.md).
- **[CLAIM-tmp8mvx8](../claims.d/CLAIM-tmp8mvx8.md)** (qualifies). BBP gives only λ_1; a count of outliers
  needs Baik and Silverstein's per-spike limits, finitely many spikes. Its
  M is the number of samples of the covariance estimate, which supports the
  claim's "Which N" correction; the claim's remark that an outlier within
  about N^(−2/3) of the edge is invisible is Theorem 1.1(a) and 1.2.
  [ARG-tmpvalfs](../arguments.d/ARG-tmpvalfs.md).
- **[CLAIM-tmpqbo50](../claims.d/CLAIM-tmpqbo50.md)** (supports the formulas, qualifies the range). Its
  outlier and edge are Corollary 1.1 rescaled by σ²; its γ = 4 row lies
  outside BBP's M ≥ N and needs Baik and Silverstein. [ARG-tmpvalfs](../arguments.d/ARG-tmpvalfs.md).
- **[QUESTION-tmp7d1ws](../questions.d/QUESTION-tmp7d1ws.md)** (background). The proportional limit M/N → γ²
  is the regime it names.
- **Parallels and background, no edge**: [NOTE-666](NOTE-666.md) and [LIT-862](../literature.d/LIT-862.md) (a coherence
  threshold that is Benaych-Georges and Nadakuditi's θ > c^(1/4), called
  there a BBP transition); [NOTE-659](NOTE-659.md) (outliers at the upper and lower
  edges); [NOTE-660](NOTE-660.md) (the spiked model borrowed for analogy vectors);
  [NOTE-689](NOTE-689.md) and [NOTE-805](NOTE-805.md) (thresholds compared to BBP's).

## Limitations

- Complex Gaussian samples only; the real case is a conjecture here.
- The largest eigenvalue only; nothing on eigenvectors, nor on the other
  outliers' laws beyond λ_1.
- M ≥ N only.
- Finitely many spikes.
- The threshold is proved but not explained: the authors have "no
  intuitive reason yet", and the percolation heuristic of §6 is not a
  derivation. A gap the paper names itself.
