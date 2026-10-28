---
number: 748
status: Active
formerly:
- THEORY-tmp784do
title: 'Block entropies, and so every lag-τ entropy rate of a stationary signal, are unchanged by the reflection x → −x and by time reversal, so they cannot detect the odd-order asymmetry the 4/5 law ties to energy flux; Granero-Belinchón, Roux and Garnier''s entropy rate conditioned on the sign of the increment breaks the reflection invariance, but h⁺ ≠ h⁻ shows only that the two-point distribution lacks central symmetry, which a skewed one-point distribution produces with exactly symmetric increments, so the test does not by itself detect skewed increments or an energy cascade'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-970. The invariance and the implication
    "central symmetry ⇒ h⁺ = h⁻" are proved below. The counterexample is
    computed two ways: by quadrature on a grid, converged to 10⁻⁴, and by
    the paper's k-nearest-neighbour estimator at its sample size. That
    meets ADR-047 v2. The paper itself states the gap ("The reciprocal may
    not hold") but then draws the conclusion it blocks; the counterexample
    built on the paper's own measured one-point skewness is the record's.
tags:
- information-theory
- natural-sciences
date: '2026-10-20'
source:
- LIT-1243
summary: >-
  Granero-Belinchón, Roux and Garnier (2016), [LIT-1243](../literature.d/LIT-1243.md), read in
  [NOTE-970](../notes.d/NOTE-970.md), claim that conditioning the entropy rate on the sign of
  the increment lets one "prove the existence of the energy cascade" using
  information theory. The record finds two limits. The unconditioned
  entropy rate is exactly blind to reflection and time reversal. The
  conditioned one detects any central asymmetry of the two-point law,
  including one with no increment skewness at all. Independent pairs with
  the paper's one-point skewness of 0.175 give h⁺ − h⁻ ≈ 0.066 nats with
  symmetric increments. Nothing in the paper ties an information quantity
  to the energy balance.
bears_on:
- QUESTION-219
---

# THEORY-748: Block entropies, and so every lag-τ entropy rate of a stationary signal, are unchanged by the reflection x → −x and by time reversal, so they cannot detect the odd-order asymmetry the 4/5 law ties to energy flux; Granero-Belinchón, Roux and Garnier's entropy rate conditioned on the sign of the increment breaks the reflection invariance, but h⁺ ≠ h⁻ shows only that the two-point distribution lacks central symmetry, which a skewed one-point distribution produces with exactly symmetric increments, so the test does not by itself detect skewed increments or an energy cascade

## Source

Granero-Belinchón, Roux and Garnier (2016), *EPL* 115, 58003, [LIT-1243](../literature.d/LIT-1243.md),
read in full in [NOTE-970](../notes.d/NOTE-970.md) from arXiv:1607.05511v2. The conditioning
procedure and its symmetry argument are the paper's ("Conditioned entropy
rate", Fig. 3). The invariance statement and the counterexample are the
record's.

## What was actually shown

**Setting.** x(t) is a stationary signal with a joint density for every
finite block. The paper's entropy rate is
h_τ^(m) = H(X^(m+1,τ)) − H(X^(m,τ)), where X^(n,τ) = (x(t), x(t − τ), …,
x(t − (n − 1)τ)).

**Step 1. Invariance of the entropy rate.** Differential entropy is
unchanged by any map of unit absolute Jacobian determinant.

- *Reflection.* x → −x maps each block by −I, with |det| = 1. So every
  block entropy, and so every h_τ^(m), is the same for x and −x.
- *Time reversal.* The reversed signal y(t) = x(−t) has the block
  (y(t), y(t − τ), …, y(t − mτ)) = (x(−t), x(−t + τ), …, x(−t + mτ)). That
  is the x-block ending at s = −t + mτ with its coordinates in reverse
  order. By stationarity it has the law of a permuted x-block, and a
  permutation has |det| = 1. So y and x have the same block entropies and
  the same entropy rates, for every m and τ.

The longitudinal increment skewness, and the third-order structure function
S₃ that the 4/5 law equates to −(4/5)εr, change sign under both maps.
Under Taylor's hypothesis, temporal reversal of the probe signal is
spatial reflection of the frozen field. So no entropy rate, at any
embedding, can distinguish a signal from the one with the opposite sign of
S₃. The paper's "cannot probe the energy cascade because it is not
sensitive enough to the asymmetry" understates this. The blindness is
exact, and it comes from symmetry, not from sensitivity.

**Step 2. What the conditioned rate tests.** The paper splits the points
x(t) by the sign of δ_τ(t) = x(t) − x(t − τ) and estimates h^(1) on each
subset, giving h⁺ and h⁻. For m = 1 it says the test probes "the asymmetry
of the joint PDF p(x(t), x(t − τ))". Write a = x(t), b = x(t − τ). The
subsets are the half-planes a > b and a < b, and the central reflection
(a, b) → (−a, −b) maps one onto the other with |det| = 1. So if
p(a, b) = p(−a, −b), then h⁺ = h⁻, which is the paper's statement. The
converse does not follow, and the paper says so: if the increments are
skewed, the joint PDF is not centrally symmetric, but "the reciprocal may
not hold". So h⁺ ≠ h⁻ establishes that the joint law lacks central
symmetry. That is necessary for skewed increments, and it is not
sufficient.

**Step 3. Counterexample.** Let a and b be independent with the same
skew-normal law, skewness 0.175. That is the one-point skewness the paper
reports for its Modane signal, and it is what the joint law of any
stationary signal tends to at lags beyond the correlation time. Since
(a, b) is exchangeable, a − b has the law of b − a, so the increments are
exactly symmetric and S₃ = 0. But p(a)p(b) ≠ p(−a)p(−b), and

- by quadrature (grids of 1401² and 2801² on [−8, 8]²),
  h⁺ − h⁻ = H(a | b, a > b) − H(a | b, a < b) = 0.0657 nats;
- by the paper's estimator family (Kozachenko–Leonenko, k = 5, maximum
  norm) at its sample size N = 2¹⁷, on standardized samples, ten
  replicates: 0.0645 ± 0.0066 nats, with a measured increment skewness of
  0.002.

With a Gaussian copula of correlation c and the same marginal, the
difference falls with c: 0.046 nats at c = 0.5, 0.021 at c = 0.9 and
0.0065 at c = 0.99. A centrally symmetric (Gaussian) marginal gives 0 in
every case, as Step 2 requires.

**Bearing on the paper's result.** The paper reports h⁺ − h⁻ "almost
constant around 0.1 ± 0.01" across all scales, with a standard deviation of
h^(1)(X^±) near 0.03. Increment skewness in turbulence grows toward small
scales and vanishes beyond the integral scale, where samples decorrelate.
A difference that stays roughly constant into the integral range is what
one-point skewness predicts, by Step 3. Nothing in the paper separates the
two sources. Its two robustness checks, equalizing the subset sizes and
comparing with a random half, address estimator bias from sample size. They
do not address this. Fig. 3's lower axis is labelled with a normalization,
(h⁺ − h⁻)/σ_h in extraction, so the stated 0.1 may not be in nats. The
argument does not depend on its exact value.

## What this does not say

- **That the Modane signal has no skewed increments.** It surely has them;
  the 4/5 law is well tested. The claim is that this test does not show
  it, because a signal with symmetric increments and the same one-point
  skewness would also pass.
- **That no conditioned information measure can detect S₃.** Conditioning
  on the sign of the increment while removing one-point asymmetry (for
  example by testing on a rank-transformed or symmetrized marginal), or
  measuring an asymmetry functional of the increments directly, could
  isolate it. The paper does neither.
- **Anything about information transfer across scales.** The paper defines
  no information flux, no transfer entropy and no mutual information
  between scale bands. Its only link from an information quantity to the
  energy balance is the chain h⁺ ≠ h⁻ → skewed increments → 4/5 law, and
  the first link fails as shown. It computes no ε, no S₃, and no sign.

## Connections

- **[QUESTION-219](../questions.d/QUESTION-219.md).** It sharpens A3's caution. Energy transfer has a
  direction across scales because S₃ is odd. The entropy rates are even
  under the maps that flip that sign, so they assign no direction at all.
  The one asymmetric quantity the paper builds detects a different
  asymmetry.
- **[THEORY-750](THEORY-750.md).** The companion result: the unconditioned rate in
  these data is S₂ in nats.
- **[THEORY-754](THEORY-754.md).** The energy flux there is a signed, Galilean-invariant
  triple product with a budget. No information quantity in this paper has
  either property.
