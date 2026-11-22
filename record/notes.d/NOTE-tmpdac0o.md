---
status: Read
paper: LIT-2983
title: 'Dandi, Pesce, Cui, Krzakala, Lu & Loureiro — A Random Matrix Theory Perspective on the Spectrum of Learned Features and Asymptotic Generalization Capabilities'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    From the arXiv PDF of 2410.18938v1 (24 Oct 2024, the only version the
    arXiv API lists), fetched 2026-11-22 from arxiv.org without obstacle
    and converted with pdftotext. Read in full: abstract, §§1–6 with
    Figs 1–2, Assumptions 2.1–2.3, Lemma 3.1, Definitions 4.1–4.5,
    Theorem 4.6, Corollary 4.7, Theorem 4.8 and the proof sketch, the
    structure of Appendix A and the openings of C.1 and F.2. Skipped: the
    proofs in Appendices B–F. The PDF states no venue; the LIT's AISTATS
    2025 (PMLR 258) is not confirmed from this copy. Read by a reader
    subagent; filed by a second one, which rechecked every quote used here
    against the PDF text. No email address sent.
date: '2026-11-22'
summary: >-
  After one maximal-update gradient step (η = Θ(d)) on Gaussian
  single-index data, a two-layer network's first-layer weights are a random
  bulk plus a rank-one spike along the target (Lemma 3.1). The paper
  proves a deterministic equivalent for the resulting feature covariance:
  its bulk widens and grows longer tails, beside Θ(d) outliers that come
  from the features' means, and the ridge readout's test error is a
  functional of the whole deterministic equivalent, not of the outliers.
---
<!-- inactive-ok-file: THEORY-tmpcij35 CLAIM-799 ARG-tmp2mzk1 TERM-tmpf5ymd CLAIM-tmp2r6ur THEORY-2133 THEORY-2135 THEORY-106 THEORY-813 CLAIM-775 CLAIM-798 CLAIM-832 LIT-2984 LIT-tmpnwvnx LIT-tmp4kae5 LIT-tmpj4og3 LIT-tmpcyeab — Proposed, Deferred or new; the account this reading files, the entries it bears on and the works registered from it -->

# NOTE-tmpdac0o: Dandi, Pesce, Cui, Krzakala, Lu & Loureiro — A Random Matrix Theory Perspective on the Spectrum of Learned Features and Asymptotic Generalization Capabilities

## Contribution

1. Rigour for the maximal-update one-step regime, which earlier
   random-matrix work (Moniri and colleagues, LIT-tmp4kae5, step sizes
   Θ(d^(1/2+ζ)) with ζ < 1/2) did not reach. It is the rigorous version of
   the replica result of Cui and colleagues (LIT-tmpj4og3), in the one-step
   setting of Ba and colleagues (LIT-tmpnwvnx), extended to a second layer
   initialized from k values.
2. A deterministic equivalent for the feature covariance's resolvent, so
   the bulk spectrum and the exact test error.
3. A picture of what learning does to the feature spectrum: chiefly a
   **reshaped bulk**, plus outliers from the features' means.

## Key insight

The spike is in the weights. Pushed through the nonlinearity, it does not
reappear in the features only as one separated eigenvalue: it changes the
shape of the whole continuous bulk, and the test error depends on all of
it.

## Assumptions

- Isotropic Gaussian inputs; single-index target y = g(xᵀw⋆), g bounded
  Lipschitz, E g = 0, E g′ ≠ 0.
- Odd Lipschitz activation with bounded σ″, σ‴.
- One gradient step on the square loss with the second layer frozen, on
  n0 = Ω(d^(1+ε)) samples; n, p and η/d proportional to d; then ridge on n
  fresh samples.
- First layer uniform on the sphere; second layer from a finite vocabulary
  of k values (Assumption 2.1), the source of the "spurious spikes".
- Asymptotic in d.

## Key results

- **The weight spike** (§3, eq. 4; Lemma 3.1): "the hidden layer weights
  after one GD step are approximately low rank", W¹ ≈ W⁰ + u(w⋆)ᵀ in
  operator norm for n0 = Ω(d^(1+ε)). "It is precisely the presence of such
  correlated components that enables the trained model to surpass the
  Random Features performance".
- **Two scales in the features** (§4): "the first term varies only along a
  k-dimensional subspace with variations governed by κµ, while the second
  term contributes to the 'bulk' of the feature covariance."
- **Deterministic equivalent** (Theorem 4.6) and the bulk's Stieltjes
  transform (Corollary 4.7).
- **Test error** (Theorem 4.8): "given by the following low-dimensional,
  deterministic formula", a function of the deterministic equivalent's
  fixed point as a whole.
- **The spectrum after training** (§5, Fig. 1): "this bulk is modified
  from the unspiked RF spectrum ..., displaying in particular a wider
  support and longer tails in this particular instance. The spectrum also
  exhibits outlying eigenvalues of order Θ(d), arising from the means",
  which are "not represented in Fig. 1"; the spikes are "present due to
  the finite support assumption for the second layer". The authors tie
  the longer tails to "previous empirical observations ... that heavier
  tails can emerge after feature learning, a behaviour which further
  tends to correlate with better generalization" (Martin and Mahoney;
  Wang and colleagues, LIT-tmpcyeab).
- **Bulk and spikes** (§5): at the maximal step "it is largely unclear how
  the bulk and spikes recombine"; "the departure of the bulk from its
  untrained shape can be intuitively seen as a result of the recombination
  between the untrained bulk and some of the spikes", offered as
  intuition.
- **Expressivity** (§5, Fig. 2): "there is a net increase of the
  expressivity of the neural network for larger vocabulary sizes k".

## Concepts

- **Spiked random-features model**; **maximal-update step size**.
- **Conditional Gaussian equivalence**; **deterministic equivalent**;
  **extended resolvent**.
- **Bulk of the feature covariance** against Θ(d) **spurious spikes**;
  **bulk–spike recombination**.
- No BBP threshold, detectability transition or phase transition appears.

## Connections

The η = Θ(d) step is the maximal-update parametrization, the regime in
which THEORY-2133 and CLAIM-775 say features are learned; leaving the lazy
regime of THEORY-2135 and THEORY-813 is the point. The baseline, the dashed
initial spectrum, is the random-features model of THEORY-106. THEORY-283 is
the same Gaussian multi-index family asked a different question. Wang, Wu
and Fan (LIT-2984) is a sibling not cited. THEORY-420's random-matrix null
for weight spectra is the contrast: here learning reshapes the bulk and
adds outliers, and the bottom of the spectrum is not discussed.

## Bearing on the record

Filed as THEORY-tmpcij35. Dated notes of 2026-11-22 on each entry below.

- **LIT-2983's own summary was partly wrong**, corrected there: the spike
  is in the weights; the feature spectrum's headline is a reshaped bulk;
  its outliers come from the feature means; the error depends on the whole
  deterministic equivalent.
- **CLAIM-799**: supports A32 §6's narrow point that the spiked picture of
  learned features is a theorem, for one step, and qualifies the claim:
  learning shows spectrally as bulk reshaping, not only as an outlier
  crossing a threshold (ARG-tmp2mzk1, and the claim's change of
  2026-11-22).
- **TERM-tmpf5ymd**: a worked case where the two senses of "bulk" split.
- **CLAIM-tmp2r6ur**: leaves open, with a contrast: the top outliers come
  from the means but carry the task signal here.
- **CLAIM-798** (consistent: one step, no dynamics), **CLAIM-832**
  (background: heavier tails after learning), **THEORY-2133**,
  **CLAIM-775**, **THEORY-2135**, **THEORY-813**, **THEORY-106**,
  **THEORY-283**, **THEORY-420** (background, parallel or contrast; notes
  there).

Nothing here is filed as an instruction for machine-learning practice.

## Limitations

- One step, Gaussian isotropic data, single-index target, two layers,
  asymptotic.
- The finite second-layer support is the paper's own listed limit and the
  source of its outliers.
- The heavier-tails link to generalization is shown "in this particular
  instance" and cited as empirical, not proved; the recombination of bulk
  and spikes is intuition.
- The anisotropic regime n0 = Θ(d) is characterized only in the weights
  (App. F.2).
