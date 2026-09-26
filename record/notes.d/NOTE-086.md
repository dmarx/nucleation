---
number: 86
status: Read
formerly:
- NOTE-tmpzg69x
paper: LIT-058
title: 'I-MMSE: mutual information and MMSE in Gaussian channels'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv cs/0412108v1 (23 Dec 2004), 22 pp.
    Read: §I–§VII, Figs. 1–6 (captions; the plotted curves came through only
    as axis labels), Appendices I–VII and references [1]–[60]. Nothing
    skipped. PDF from arxiv.org/pdf/cs/0412108, extracted with PyMuPDF to
    raw4/cs_0412108.txt (pdftotext is not on this host). I did not compare
    the typeset IEEE Trans. IT 51(4):1261–1282 version, so revisions for
    publication are unverified.). Upgraded from `Skimmed` to `Read`: the
    claims table, assumptions and results are new, and the skim is corrected
    where the full text disagreed.
date: '2026-09-25'
summary: >-
  Let Y = √snr·X + N with N ~ N(0,1) independent of X, and let X have any
  distribution with E X² < ∞. Then d/dsnr I(X; √snr X + N) = ½·mmse(X |
  √snr X + N) in nats, equivalently I(snr) = ½∫₀^snr mmse(γ) dγ (Thm 1,
  Eq. 47). The vector form is d/dsnr I(X; √snr HX + N) = ½·E‖HX −
  H·E[X|Y]‖² (Thm 2). In continuous time, the same identity combined with
  Duncan's I = (snr/2)·cmmse gives cmmse(snr) = (1/snr)∫₀^snr mmse(γ) dγ
  (Thm 8).
---

# NOTE-086: I-MMSE: mutual information and MMSE in Gaussian channels

## Contribution

Before this paper, it was known that at vanishing SNR the mutual information is insensitive to the input distribution (Verdú; Lapidoth–Shamai; Prelov–Verdú). Duncan (1970) had written continuous-time mutual information as an integral of the **causal** MMSE. This paper proves that for every finite-power input in additive Gaussian noise, the SNR-derivative of mutual information (in nats) equals half the **noncausal** MMSE of the optimal estimator. The identity holds in scalar, vector, discrete-time and continuous-time settings. Combined with Duncan, it yields a new and previously unknown nonlinear-filtering identity: filtering MMSE equals smoothing MMSE averaged over SNR uniform on [0, snr]. The authors note that no non-information-theoretic proof of it is known (p. 2). The paper also writes entropy, differential entropy, non-Gaussianness and mutual information as integrals of MMSE over SNR (§VI).

## Key insight

Gaussian noise is infinitely divisible. So a channel at SNR snr is a degraded version of one at snr + δ, obtained by adding independent noise (the "incremental channel", Fig. 2). By the chain rule the information lost in that step is I(X; Y₁ | Y₂). Given Y₂ this is a channel of vanishing SNR δ whose input law is P_{X|Y₂}, and at vanishing SNR mutual information is (δ/2)·Var (Lemma 1). Averaging over Y₂ turns that conditional variance into the MMSE at snr. Mutual information is therefore the accumulation over SNR of the estimation error, I(snr) = ½∫₀^snr mmse(γ) dγ, along a "Gaussian pipe" that adds noise gradually (Fig. 3).

## Assumptions

- Additive Gaussian noise **independent of the input**:
  - scalar and vector: N ~ N(0, I);
  - continuous time: a standard Wiener process in dY_t = √snr·X_t dt + dW_t.
- **Finite power**: E X² < ∞ (Thm 1); E‖X‖² < ∞ (Thm 2); ∫₀^T E X_t² dt < ∞ (Thms 6–8).
  - There are no other conditions on P_X. It may be discrete, singular or heavy-tailed, provided the second moment is finite.
- **The input law is fixed and does not depend on snr** (stated as a proviso in §V-B). This excludes feedback for the noncausal identity.
- H is deterministic and known (vector case). Colored noise is handled by whitening (§V-C).
- **Units and normalization.**
  - Nats.
  - snr as defined need not be the physical power ratio unless E X² = 1 (footnote 3).
  - For complex channels with noise of variance ½ per real component, the factor ½ disappears (§V-D).
- Theorem 8 requires continuous time. The averaged MMSEs are time averages over [0, T], and stationarity is not required.

## Key results

- **Theorem 1 (scalar I-MMSE, Eq. 15).** For every P_X with E X² < ∞: d/dsnr I(X; √snr·X + N) = ½·mmse(X | √snr·X + N), where mmse(snr) = E(X − E[X|Y; snr])².
  - Equivalent integral form (Eq. 47): I(snr) = ½∫₀^snr mmse(γ) dγ.
  - Checks:
    - Gaussian input: I = ½ log(1+snr), mmse = 1/(1+snr).
    - Equiprobable ±1 input: mmse = 1 − ∫ φ(y)·tanh(snr − √snr·y) dy and I = snr − ∫ φ(y)·log cosh(snr − √snr·y) dy. App. I verifies these.
- **Theorem 2 (vector, Eq. 22).** For Y = √snr·HX + N with E‖X‖² < ∞: d/dsnr I(X;Y) = ½·E‖HX − H·E[X|Y]‖².
- **Corollaries 1–2.**
  - I(snr) is concave.
  - mmse(snr) ≤ (2/snr)·I(snr) ≤ mmse(0) = Var X.
- **Theorem 3.** d/dsnr D(P_{Y|X=x} ‖ P_Y) = ½·E[|X − X′|² | X = x] − (1/(2√snr))·E[X′N | X = x], with X′ drawn from the posterior ("retrochannel").
- **Theorem 4.** For Y = HΓX + N with Γ = diag(√snr_k): ∂I/∂snr_k = ½·Σ_i √(snr_i/snr_k)·[HᵀH]_{ki}·E Cov(X_k, X_i | Y).
- **Theorem 5 (equivalent to Thm 2).** d/dsnr D(P_{√snr X+N} ‖ P_N) = ½·E‖E[X | √snr X + N]‖².
- **De Bruijn equivalence (Eqs. 51–58).**
  - Theorem 2 is equivalent to d/dt h(HX + √t·N) = ½·tr J(HX + √t·N).
  - In the scalar case J(√snr·X + N) = 1 − snr·mmse(snr).
- **Low-SNR expansions (Eqs. 91–92).** For zero-mean, unit-variance X:
  - mmse(snr) = 1 − snr + snr² − (1/6)[(EX⁴)² − 6EX⁴ − 2(EX³)² + 15]·snr³ + O(snr⁴);
  - I(snr) = snr/2 − snr²/4 + snr³/6 − (1/48)[same bracket]·snr⁴ + O(snr⁵);
  - so moments beyond the variance do not affect I up to third order.
- **Continuous time.**
  - Theorem 6: d/dsnr I(snr) = ½·mmse(snr), with time-averaged mutual-information rate and noncausal MMSE.
  - Theorem 7 (Duncan): I(snr) = (snr/2)·cmmse(snr).
  - **Theorem 8:** cmmse(snr) = (1/snr)·∫₀^snr mmse(γ) dγ.
  - Consequences:
    - lim_{snr→0} (mmse(0) − mmse(snr))/(cmmse(0) − cmmse(snr)) = 2 (Eq. 118).
    - For stationary inputs, the average anti-causal MMSE equals the causal one.
    - The high-SNR "3 dB" causality penalty is not universal: for the random telegraph input it grows like log snr.
- **Discrete time.**
  - Corollary 3: dI(Xⁿ;Yⁿ)/dsnr = ½·Σ_i mmse(i, snr).
  - Theorem 9: (snr/2)·Σ cmmse(i) ≤ I(Xⁿ;Yⁿ) ≤ (snr/2)·Σ pmmse(i).
- **Preprocessing (Thm 10).** If X—Z—Y and Y = √snr·Z + N with E Z² < ∞, then dI(X;Y)/dsnr = ½·E(Z − E[Z|Y])² − ½·E(Z − E[Z|Y,X])².
- **Feedback (§V-B).**
  - Duncan / Kadota–Zakai–Ziv survives (Thm 12).
  - The noncausal identity fails (Eq. 172, counterexample Z = X/√snr).
- **New representations (§VI).**
  - Theorem 13: H(X) = ½∫₀^∞ mmse(g(X) | √snr·g(X) + N) dsnr for any one-to-one g.
  - **Theorem 14:** D(P_X ‖ N(EX, σ²_X)) = ½∫₀^∞ [σ²_X/(1 + snr·σ²_X) − mmse(X | √snr·X + N)] dsnr.
  - Hence h(X) = ½ log(2πe·σ²_X) − that integral (Eq. 182).
  - Eq. 184: I(X;Z) = ½∫₀^∞ E[(E[Z | √snr·Z + N, X])² − (E[Z | √snr·Z + N])²] dsnr.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | dI/dsnr = ½·mmse for every finite-power input to the scalar Gaussian channel | strong | proof, Thm 1 via §II-C incremental channel + Lemma 1 (App. II); four further proofs |
| C2 | The vector version holds with MMSE of HX | strong | proof, Thm 2 (App. IV, with Lemmas 8–9 justifying the interchanges) |
| C3 | The identity is equivalent to de Bruijn's identity | strong | derivation, §II-D.2, Eqs. 53–57 |
| C4 | In continuous time, filtering MMSE = smoothing MMSE averaged over SNR ∈ [0, snr] | strong | proof, Thm 8 = Thm 6 + Duncan (Thm 7); verified for the random telegraph input (App. V) |
| C5 | In discrete time, mutual information lies between the summed filtering and prediction MMSEs × snr/2 | strong | proof, Thm 9 |
| C6 | The noncausal identity does not extend to channels with feedback | strong | counterexample, §V-B |
| C7 | Entropy, differential entropy and non-Gaussianness are integrals of MMSE over SNR | strong | proofs, Lemma 6 (App. VII), Thms 13–14 (Thm 14 by Lemma 7, one line, + Thm 1) |
| C8 | Derivative of the conditional divergence (Thm 3) and per-user derivative (Thm 4) | weak | Thm 3 stated without proof; Thm 4 proof "omitted" |
| C9 | Continuous-time identity with arbitrary preprocessing (Thm 11) | weak | asserted by analogy with Thm 10 |
| C10 | Identity (1) "was unknown before this work" | moderate | the paper's survey of prior low-SNR results [1]–[4] and Duncan; a priority claim, not provable |
| C11 | Applications: CDMA joint/separate-decoding relation, GEXIT = −½·MMSE, "Gaussian maximizes I" ⇔ "Gaussian maximizes MMSE" | moderate | short arguments in §II-D.1, citing [30], [38] |

## Method

The proofs are information-theoretic, and there is no algorithm. The central devices are:
- the **SNR-incremental channel**: a cascade Y₁ = X + σ₁N₁, Y₂ = Y₁ + σ₂N₂ with σ₁² = 1/(snr+δ) and σ₁² + σ₂² = 1/snr, rewritten as (snr+δ)Y₁ = snr·Y₂ + δX + √δ·N with N independent of (X, Y₂);
- the **time-incremental channel**, used to reprove Duncan's theorem through a "time–SNR transform" (§III-D);
- the chain rule for mutual information along a Markov chain of increasingly noisy outputs;
- in App. IV, direct differentiation of −∫p_Y log p_Y, with dominated-convergence lemmas.

## Concepts

- **snr** — the gain in y = √snr·x + n. It is the physical SNR only if E X² = 1.
- **mmse(snr)** — E(X − E[X | Y; snr])². It is **noncausal** (smoothing) in continuous time, given the whole path Y₀ᵀ.
- **cmmse(snr)** — the causal (filtering) MMSE, time-averaged over [0, T]. **pmmse** is the one-step prediction MMSE (discrete time).
- **Incremental channel** — see Method.
- **Retrochannel** — samples X′ from the posterior P_{X|Y}, used in Thm 3.
- **Non-Gaussianness** — D_X = D(P_X ‖ N(EX, σ²_X)). γ_X = e^{−D_X} ∈ [0,1] measures how hard X is to estimate across SNRs.

## Connections

- The identity extends the low-SNR results of Verdú (1990, 2002), Lapidoth–Shamai (2002) and Prelov–Verdú (2004) to all SNRs.
- It pairs with Duncan (1970) and Kadota–Zakai–Ziv (1971) on causal filtering.
- It is equivalent to de Bruijn's identity (Stam 1959; Costa 1985), and the Cramér–Rao bound is tight here (Eq. 58).
- It uses Esposito (1968) and Hatsell–Nolte (1971) on likelihood-ratio gradients and Laplacians (Tweedie-type: ∇ log l(y) = E[Z | Y = y], Lemma 2).
- The paper points to Zakai's extension to abstract Wiener space (ref. [44], a preprint) and to a Poisson-channel counterpart ([60]), in which the error measure is not mean-square.
- No document in this record builds on it yet.

## Bearing on the record

- For this record: no THEORY document is supported or contradicted.
- **For the Anthology of the SOTA: a possible anthology boundary work, and a real one.** The paper carries no ML instruction. But the identity it proves is the exact-estimator form of the fact that diffusion models' likelihoods are integrals of denoising error over noise levels.
  - Theorem 1's integral form I = ½∫mmse dγ and Theorem 14's h(X) = ½ log(2πeσ²) − ½∫[σ²/(1+γσ²) − mmse(γ)] dγ are density/entropy-as-integrated-denoising-MSE statements.
  - In continuous time the dependence falls on the SNR range, which is what [ANTH-THEORY-027](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-027.md) ("in continuous time the diffusion bound depends on the noise schedule only through its endpoints", sourced to Variational Diffusion Models, [ANTH-LIT-446](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-446.md)) and [ANTH-THEORY-107](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-107.md) (monotone SNR weighting ⇔ maximum likelihood) rest on.
  - Neither of those cites this paper (checked by grep: none of [ANTH-THEORY-027](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-027.md), [ANTH-THEORY-107](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-107.md) and [ANTH-LIT-446](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-446.md) mentions Guo, Shamai, Verdú or MMSE, and the only "Guo"/"Shamai" hits in the whole anthology record are other authors named Guo).
  - One caution for whoever cites it. The identity concerns the **optimal** (conditional-mean) denoiser, whereas a trained diffusion model's ELBO uses a learned denoiser. Carrying the identity across needs the mismatched-estimation version, which is later work by Verdú and not in this paper. So it would be cited as the root of the "likelihood = integrated MMSE" reading, not as a proof of any diffusion bound.
  - It carries no practice.

## Limitations

- Gaussian noise is essential, through infinite divisibility and independent increments (§VII). The paper gives no non-Gaussian-noise version beyond a pointer to the Poisson channel.
- The noncausal identity requires an input law that does not depend on snr. It fails with feedback.
- Theorem 8 (causal = averaged noncausal) is a continuous-time result. Discrete time gives only bounds.
- Theorems 3, 4 and 11 are unproved in this text.
- The applications (CDMA, GEXIT) are sketched with citations, not developed.
- The paper says so itself: "It remains to be seen whether such representations lead to new insights and applications" (§VI, p. 16), and Theorem 8 has no non-information-theoretic proof (p. 2).

## Open questions

- An estimation-theoretic proof of Theorem 8, and of the entropy power inequality via Eq. 183 (both posed by the authors).
- Counterparts for other channels with independent increments (Lévy noise), where the error measure changes. The Poisson case is in [60].
- A mismatched version for a suboptimal estimator. This is what diffusion-model likelihoods need, and it is not in this paper (later work, not read here).

## Corrections to the seeded skim

- The dossier asks what "arbitrary input" allows. The full conditions, which the dossier does not state, are:
  - finite second moment (E X² < ∞, or E‖X‖² < ∞; finite average power ∫₀^T E X_t² dt < ∞ in continuous time);
  - noise independent of the input;
  - "a fundamental proviso": **the input distribution must not depend on snr** (§V-B, p. 14).

  The last condition is exactly what feedback breaks. §V-B shows by counterexample that the noncausal I-MMSE identity **fails with feedback** (Eq. 172). There, Z = X/√snr leaves the output unchanged, so dI/dsnr = 0 while the MMSE is non-zero. Duncan's causal identity survives feedback (Thm 12, Kadota–Zakai–Ziv). The dossier lists "feedback (via Kadota–Zakai–Ziv / Duncan)" among the generalizations without saying that the noncausal identity is the one that does not generalize.
- The dossier's summary states the filtering = averaged-smoothing result (Thm 8) as a consequence without qualification. It holds only in **continuous time**. It uses time-averaged MMSEs; stationarity is not needed (§I, p. 2). In discrete time the paper proves only a sandwich (Thm 9): (snr/2)·Σ cmmse(i) ≤ I(Xⁿ;Yⁿ) ≤ (snr/2)·Σ pmmse(i), between filtering and one-step prediction errors.
- The dossier locates the five proofs in "§II-E, §III-E". They are spread over five places:
  - §II-C, the SNR-incremental channel;
  - §II-D.2, equivalence with de Bruijn's identity;
  - §II-E, likelihood-ratio geometry via Esposito and Hatsell–Nolte, proving the equivalent Thm 5;
  - Appendices III–IV, direct differentiation, with App. IV justifying the interchanges by dominated convergence (Lemmas 8–9);
  - §III-E, from Duncan's theorem.
- Not every theorem in the paper is proved there, and the dossier does not note this:
  - Theorem 3 (derivative of the conditional divergence D(P_{Y|X=x}‖P_Y)) is stated with no proof.
  - Theorem 4 (per-user SNR derivative) has its proof "omitted" (p. 6).
  - Theorem 11 (continuous time with preprocessing) is asserted by analogy ("nothing prevents us", p. 14).
  - Lemma 7 has a one-line proof.
- The dossier's "H(X) = lim_{snr→∞} I(X; √snr X + N) for discrete X" is Lemma 6 (proved in App. VII, including countable X and the H(X) = ∞ case). The more usable statement is Theorem 13: H(X) = ½∫₀^∞ E(g(X) − E[g(X)|√snr·g(X) + N])² dsnr for **any one-to-one g**, and the integral does not depend on the choice of g.
