---
number: 970
status: Read
formerly:
- NOTE-tmp5kark
paper: LIT-1243
title: 'Granero-Belinchón, Roux and Garnier — Scaling of information in turbulence'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from arXiv:1607.05511v2 (29 September 2016, "epl draft",
    7 pages), text extracted with pdftotext in layout and plain modes: the
    abstract, the introduction, "Information measurements" (definitions,
    estimation), "Turbulence signal analysis" (entropy rate, robustness,
    embedding, autocorrelation, Batchelor model, fBm), "Conditioned entropy
    rate", the discussion, the conclusion and the references. The
    published EPL version was not compared, and neither was v1. The two
    columns interleave in extraction, and several superscripts (the m in
    h_τ^(m), the ± in h^±) were reconstructed from context. Figures 1–3
    were read from their captions, axis labels and the text. The lower
    panel of Fig. 3 has an axis label that extracts as
    (h⁺ − h⁻)/σ_h, so whether the reported 0.1 is in nats or normalized
    could not be settled. The cited data paper (Kahalerras et al. 1998)
    and the earlier information-theoretic turbulence papers (Cerbus and
    Goldburg 2013, 2016; Ikeda and Matsumoto 1989) were not read.
date: '2026-10-20'
summary: >-
  Estimates, with k-nearest-neighbour estimators, the conditional entropy
  of a velocity sample given samples a lag τ before it (the "entropy
  rate") on one Modane wind-tunnel record, as a function of τ. It finds
  slopes of −1/3 (inertial) and −1 (dissipative) against log of inverse
  lag, and shows these are S₂'s scaling through a Gaussian formula the
  data obey. A sign-of-increment conditioning gives unequal entropy rates,
  which the paper reads as proof of the energy cascade. That inference
  fails: one-point skewness alone produces the inequality. No information
  quantity is tied to the energy balance, and none is transferred.
---
<!-- inactive-ok-file: CLAIM-157 CLAIM-331 THEORY-257 — Proposed; open claims and readings this reading bears on, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-1252 — Unavailable; cited as open, nothing here rests on it -->
# NOTE-970: Granero-Belinchón, Roux and Garnier — Scaling of information in turbulence

## Contribution

An application of k-nearest-neighbour information estimators to one
turbulent velocity record, with the delay τ of the embedding as the
variable. It shows that the conditional entropy of a sample given the
sample(s) a lag τ earlier separates the integral, inertial and dissipative
ranges. It derives the inertial and dissipative slopes from a Gaussian
formula and the Batchelor structure-function model, and the fBm slope from
fBm's covariance. It then introduces a "conditioned entropy rate",
the same estimate on the points whose increment is positive (or negative).
The two differ on the turbulence signal and coincide on fBm. What is new is
the conditioning device and the observation that the entropy-rate curve
reproduces S₂'s breakpoints. That the curve is S₂ rewritten is the
paper's own conclusion for m = 1.

## Key insight

For a near-Gaussian signal, "how much new information a sample carries
given a sample a lag τ away" is ½ log(1 − c(τ)²) plus a constant, a
monotone function of the autocorrelation. So the "scaling of information"
is the scaling of the second-order structure function, halved. To see the
asymmetry that carries the energy cascade, one has to break the entropy
rate's symmetries by conditioning, and the conditioning chosen here breaks
them in a way that does not single out the increments.

## Assumptions

- **Taylor's frozen-turbulence hypothesis**, used throughout, to read a
  time lag τ dt as a spatial scale τ⟨v⟩dt, with ⟨v⟩ = 20.5 m/s.
- **Stationarity of the record**, implicit in pooling all t into one
  sample per lag.
- **No Theiler correction.** Temporally adjacent points are kept as
  candidate nearest neighbours: "we do not care about the Theiler
  correction; on the contrary, we want to explore all domains where
  correlations are important". The estimators assume independent samples.
  See Limitations.
- **Gaussianity**, for (3), the Batchelor-model slopes and the fBm result.
  The empirical agreement of the estimate with (3) is reported, not
  assumed.
- **Batchelor model (4)**, S₂(τ) = (τdx/L)^(2/3)/[1 + (η_k/τdx)²]^(2/3), as
  extracted, with S₂ = 1 − c (normalized by 2σ²). As written it has no
  large-scale saturation, so L enters only as an amplitude.
- **Setting narrower than the title.** One signal (one-point, one velocity
  component, one flow, one Reynolds number), embedding dimension m ≤ 3 on
  the data and m ≤ 4 on fBm.

## Key results

- **Definitions (1)–(2).** h_τ^(m)(X) = H(X_τ | X^(m,τ)) = H(X^(m+1,τ)) −
  H(X^(m,τ)) = H(X) − I(X_τ, X^(m,τ)), with the delay vector x_t^(m) =
  (x(t), x(t − τ), …, x(t − (m − 1)τ)) and X_τ the one further sample. It
  is a finite-m, finite-lag conditional entropy, not the entropy rate of
  the process in the m → ∞ limit. Differential entropy, so it can be
  negative.
- **Estimator.** The MI term by Kraskov–Stögbauer–Grassberger ([LIT-1163](../literature.d/LIT-1163.md),
  [THEORY-709](../theory.d/THEORY-709.md)), whose bias partly cancels between its arguments; H(X) by
  Kozachenko–Leonenko. k = 5 (k = 10 checked); N = 2¹⁷ points per
  estimate, kept constant across τ; averaged over 195 independent
  samples. Standard deviation 0.03 (small τ) to 0.08 (large τ). Checked
  not to change for k = 5, 10 or N = 2¹⁶, 2¹⁷, 2¹⁹.
- **Data.** Longitudinal velocity from a grid-turbulence experiment in the
  ONERA wind tunnel at Modane (ref. 19, Kahalerras et al. 1998), sampled at
  25 kHz. R_λ ≈ 2700, turbulence intensity ≈ 8%, ⟨v⟩ = 20.5 m/s. One-point
  PDF almost Gaussian, skewness 0.175 ± 0.001. The paper reports about
  three decades of k^(−5/3) spectrum.
- **Entropy-rate curve (Fig. 1).** Flat at H(X) above τ dt ≈ 36 ms
  (integral). Linear with slope ≈ −1/3 against log(f_s/τ) in the inertial
  range. Steeper below ≈ 0.18 ms (dissipative), slope −1 for m = 1. The
  axis appears to be natural log: 36 ms is τ = 900 and ln(25000/900) ≈ 3.3,
  where the figure marks it. The inertial range so marked spans a factor
  of 200 in lag, about 2.3 decades.
- **Gaussian formula (3).** h_τ^(1) = H(X) + ½ log(1 − c(τ)²), H(X) =
  ½ log(2πeσ²). Computed from the measured autocorrelation, it is "almost
  identical" to the m = 1 estimate at all scales. Re-derived in
  [THEORY-750](../theory.d/THEORY-750.md).
- **Slopes from the Batchelor model.** S₂ ∝ τ^(2/3) (inertial) and τ²
  (dissipative) give −1/3 and −1 through (3). Fitting S₂ or the entropy
  rate gives the same L and η_k. Re-checked: 0.337 and 1.000 on the model
  ([THEORY-750](../theory.d/THEORY-750.md)).
- **Embedding.** m = 2, 3 change the curve only below 0.18 ms, where it
  falls further with m. "For m > 2, there is no measurable evolution
  anymore". The authors suggest the small-scale effect "may originate from
  the experimental processing of the signal".
- **fBm (5)–(6).** h_τ^(1)(B) ≈ H log τ + ½ log(2πeσ₀²) for t ≫ τ.
  Measured slope 0.32 ± 0.01 for H = 1/3 at the same N. For m up to 4, the
  slope rises to 0.34 ± 0.01, with a small deviation at large τ that the
  authors attribute to finite size.
- **Conditioned entropy rate (Figs. 2–3).** X⁺ (X⁻) are the samples x(t)
  with δ_τ(t) = x(t) − x(t − τ) > 0 (< 0), about 48% and 52%. h^±,(m) is
  h^(m) estimated on them. If p(x(t), x(t − τ)) is centrally symmetric,
  h⁺ = h⁻. fBm: indistinguishable. Turbulence, m = 1: a difference "almost
  constant around 0.1 ± 0.01" across scales, against a standard deviation
  of h^(1)(X^±) of about 0.03. Equalizing the subset sizes leaves the
  difference unchanged, and a random half-sample gives the unconditioned
  h.
- **Conditional entropy given the increment value.** H(X_τ | X^(m,τ), δ_τ)
  was tried and found insensitive to skewness, because averaging over all
  increment values cancels the asymmetry.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The entropy rate as a function of τ separates the integral, inertial and dissipative ranges | strong, as a restatement | Fig. 1; but by (3) and the paper's own agreement with it, it separates them exactly as S₂ does |
| C2 | Inertial slope −1/3 and dissipative slope −1, "in perfect agreement" with the Batchelor model and fBm | strong for the slopes | (3) with S₂'s exponents 2/3 and 2, re-derived in [THEORY-750](../theory.d/THEORY-750.md); "perfect agreement" with a model fitted to the same data is weaker than it sounds |
| C3 | The entropy rate "describe[s] the distribution of information amongst scales" | weak | h_τ at different τ are not parts of a whole, satisfy no balance law, and come from down-sampling, not band filtering |
| C4 | The entropy rate is "more sensitive to correlations than the Power Spectrum", in particular for higher-order correlations at large embedding | weak | it is a monotone function of c(τ) for m = 1 in these data, by the paper's own measurement; the m > 1 test cannot distinguish non-Gaussian correlations from Gaussian multi-point ones at this resolution ([THEORY-750](../theory.d/THEORY-750.md)) |
| C5 | Higher-order correlations are "barely observable" in turbulence | weak | an inference from m-insensitivity, which is expected even for Gaussian fBm (shift ≈ 0.022 nats below a 0.03 standard deviation); entropy is in any case insensitive to odd-order asymmetry ([THEORY-748](../theory.d/THEORY-748.md)) |
| C6 | Turbulence gives h⁺ ≠ h⁻ and fBm does not | moderate | Fig. 3, one record, two robustness checks; the normalization of the plotted difference is unclear |
| C7 | "The existence of an energy cascade can be proven using only Information Theory (and, of course, Kolmogorov 4/5 law)" | weak; the inference is invalid as stated | h⁺ ≠ h⁻ shows only lack of central symmetry, which one-point skewness 0.175 alone produces with symmetric increments (≈ 0.066 nats; [THEORY-748](../theory.d/THEORY-748.md)). The paper itself notes "the reciprocal may not hold" |
| C8 | The methods are "of general interest" for multiscale complex systems | weak | asserted; no second system analysed |

## Method

1. Delay-embed the signal with lag τ and dimension m.
2. Estimate h_τ^(m) as H(X) (Kozachenko–Leonenko) minus I(X_τ; X^(m,τ))
   (Kraskov et al.), k = 5, N = 2¹⁷, averaged over 195 blocks; vary τ from
   1 sample upward.
3. Compare with (3) from the measured autocorrelation, with the Batchelor
   model, and with a synthetic fBm of H = 1/3.
4. Split the samples by the sign of the lag-τ increment and repeat step 2
   on each half.

## Concepts

- **Entropy rate h_τ^(m)**: here the conditional differential entropy of one
  sample given m earlier samples spaced τ apart, at finite m. Not the
  Kolmogorov–Sinai or Shannon entropy rate of the process.
- **Information spectrum**: the paper's name for h_τ as a function of
  log(1/τ). Not a spectrum in the sense of a decomposition of a total.
- **Conditioned entropy rate h^±**: the entropy rate of the sub-sample whose
  increment at the same t has a given sign. The paper distinguishes it
  from the conditional entropy rate given the increment.
- **Scale τ**: a sampling lag, "equivalently … a signal down-sampled at the
  scale τ". Down-sampling without filtering keeps every smaller scale.
- **Organization**: lower entropy rate, i.e. a sample being more
  predictable from its neighbours. The paper calls the integral scales
  "the most disorganized".

## Connections

It follows Cerbus and Goldburg (2013, 2016), who also applied information
measures to turbulence and spoke of an information-theoretic demonstration
of the Richardson cascade, and Materassi et al. (2014) on a shell model.
None of these is filed. Its estimators are Kraskov et al.'s ([LIT-1163](../literature.d/LIT-1163.md),
[THEORY-709](../theory.d/THEORY-709.md)) and Kozachenko and Leonenko's. Its structure-function model is
Batchelor's (1951), and its fBm is Mandelbrot and Van Ness's (1968). The
authors' later work on information measures of intermittency is not filed.

## Bearing on the record

Answers to the coordinator's questions, in brief. The information
quantities are entropy rates of the **velocity signal itself**, not of
its increments, as functions of the delay τ, computed as H minus the
mutual information between a sample and its lagged embedding. The mutual
information is between time points, not between scales. The only
increment-based quantity is the sign used for conditioning. The estimators
are kNN: KSG for MI and Kozachenko–Leonenko for H, k = 5. The data are a
Modane ONERA wind-tunnel grid-turbulence record, not a jet. The scaling is
−1/3 (inertial) and −1 (dissipative) against log(f_s/τ), flat at H(X) in
the integral range. The cascade-asymmetry claim is the h⁺ ≠ h⁻ result and
its reading as a proof of the cascade. There is no claim about temporal
irreversibility as such: under Taylor's hypothesis, temporal asymmetry of
the probe signal is spatial parity asymmetry of the field. **No result ties
an information quantity to the energy balance law.** The only link is a
verbal chain through the 4/5 law, which is not computed. No ε, no S₃ and
no sign of anything is related to any entropy.

- **[QUESTION-219](../questions.d/QUESTION-219.md).** A3's caution, that energy and information
  transfer "should not be identified merely because both can be assigned a
  direction across scales", is if anything too generous to this paper.
  Nothing in it is an information *transfer*. There is no flux, no
  transfer entropy, no MI between bands and no budget, and the entropy
  rates are exactly invariant under the maps that reverse the direction of
  energy transfer ([THEORY-748](../theory.d/THEORY-748.md)). A5's precondition for a flux test, "a
  balance law for a specified transferred quantity", is met by energy in
  [NOTE-969](NOTE-969.md) and not by any information quantity here. The QUESTION's
  citation of this paper as a source of the caution is correct about
  what the paper lacks. It would be wrong if read as saying the paper
  assigns information a direction across scales; it does not. Recommended
  edit: in "What would count as an answer", after the A3 quotation, add
  that the paper (read in NOTE-970) defines no information flux, and
  that its scale-dependent entropy rate is S₂ in nats ([THEORY-750](../theory.d/THEORY-750.md))
  and blind to the direction of the cascade ([THEORY-748](../theory.d/THEORY-748.md)).
- **[THEORY-754](../theory.d/THEORY-754.md) and [NOTE-969](NOTE-969.md).** The NOTE's last bullet ("A3's
  caution … stands") can now cite this reading. "Scale" means different
  things in the two papers: a filter band with a telescoping budget there,
  a sampling lag with no budget here.
- **[THEORY-661](../theory.d/THEORY-661.md), [CLAIM-157](../claims.d/CLAIM-157.md).** Nothing on near-decomposability. The entropy
  rate is a smooth function of lag with breakpoints only at the integral
  and Kolmogorov scales, so it shows no block structure in scale, which is
  consistent with [THEORY-754](../theory.d/THEORY-754.md)'s banded picture but adds no evidence to
  it.
- **[QUESTION-222](../questions.d/QUESTION-222.md) (memory, Markovian augmentation).** A small,
  tangential bearing. The m-insensitivity of h_τ^(m) for m ≥ 2 outside the
  dissipative range says that, at this estimator resolution and lag
  spacing, conditioning on further past samples spaced τ apart adds
  nothing detectable. That is not evidence of Markovianity: even fBm, a
  non-Markov Gaussian process, shifts by only 0.022 nats. It
  should not be cited for memory effects either way.
- **[QUESTION-217](../questions.d/QUESTION-217.md), [QUESTION-220](../questions.d/QUESTION-220.md), [QUESTION-221](../questions.d/QUESTION-221.md),
  [QUESTION-218](../questions.d/QUESTION-218.md), [CLAIM-331](../claims.d/CLAIM-331.md), [THEORY-257](../theory.d/THEORY-257.md), [THEORY-733](../theory.d/THEORY-733.md).** Not addressed.
- **[THEORY-709](../theory.d/THEORY-709.md).** This paper uses the estimator on strongly dependent,
  temporally oversampled data, outside the iid setting in which it was
  derived. See Limitations.
- **The LIT's summary** said "entropy rates and related
  information-theoretic quantities … as a probe of the cascade beyond the
  energy spectrum". The reading finds that the entropy rate here does not
  go beyond the second-order statistics, and the cascade probe does not
  isolate the cascade. The LIT is corrected.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **The cascade "proof" does not follow** (C7). By the paper's own
  remark, skewed increments imply an asymmetric joint PDF, but not
  conversely, and h⁺ ≠ h⁻ establishes only the asymmetric joint PDF. The
  signal's one-point skewness of 0.175 makes the joint PDF asymmetric at
  every lag. Independent pairs with that skewness, whose increments are
  exactly symmetric, give h⁺ − h⁻ = 0.066 nats by quadrature and 0.064 ±
  0.007 with the paper's estimator at N = 2¹⁷ ([THEORY-748](../theory.d/THEORY-748.md)). A
  difference "almost constant" across scales, into the integral range
  where increments decorrelate and their skewness vanishes, is what that
  confound predicts. The paper's robustness checks (subset sizes, random
  halves) do not address it. Nor does it check the sign of the
  difference against the sign of S₃, which is what the 4/5 law needs.
- **"Not sensitive enough" understates it.** Block entropies are exactly
  invariant under x → −x and under time reversal, so no entropy rate, at
  any m, can see the sign of S₃ ([THEORY-748](../theory.d/THEORY-748.md)).
- **Estimator dependence.** The KSG and KL estimators assume independent
  samples. The record is sampled at 25 kHz with a correlation time of
  tens of milliseconds (about 900 samples), and the authors drop the
  Theiler window on purpose. They justify this as wanting "to explore all
  domains where correlations are important". That conflates the
  dependence being measured (between x(t) and x(t − τ)) with dependence
  between sample points, which biases the nearest-neighbour counts,
  especially for smooth, small-scale embeddings. The k and N checks do
  not test this. The dissipative-range m-dependence, which the authors
  put down to signal processing, could also be estimator bias of this
  kind. KSG also underestimates large mutual information, and at the
  smallest lags, where h is most negative, the MI is a few nats. Not
  re-checked on the data, which the record does not hold.
- **"Information amongst scales".** A lag is not a scale band. Every h_τ
  includes all fluctuations smaller than τ, and nothing sums over τ.
- **Gaussian dominance.** The Gaussian value is the maximum conditional
  entropy for given covariance, and entropy differences from moderate
  non-Gaussianity are small in nats. Agreement with (3) at the 0.03–0.08
  resolution is therefore weak evidence about higher-order structure (C4,
  C5).
- **The Batchelor model as written** has no large-scale saturation, so the
  "integral scale" it fits is an amplitude parameter. The agreement of the
  breakpoints is partly by construction, since the model is fitted to the
  same data.
- **"Three decades" of inertial range** is the spectrum's. The
  entropy-rate inertial range marked in Fig. 1 spans about 2.3.
- **One record**, one component, one Reynolds number. The general-interest
  claim (C8) is untested here.

## Open questions

- Does a sign-conditioned entropy rate computed on a rank-transformed or
  symmetrized marginal (removing one-point skewness) still give h⁺ ≠ h⁻,
  growing toward small scales as the increment skewness does? That would
  turn C6 into evidence about increments. It needs the data.
- Is there an information quantity across scales that satisfies a balance
  law, so that "information flux" could be compared with Π_ℓ term by term?
  Nothing here offers one. The record has no candidate.
- With a Theiler window, does the dissipative-range m-dependence survive?
