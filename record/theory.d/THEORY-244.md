---
number: 244
status: Proposed
formerly:
- THEORY-tmp7cr5e
promote_when: >-
  A published version of LIT-224's two new results (Theorem 5.13, Theorem
  6.27), or of the Vereshchagin–Vitányi individual rate–distortion paper
  it follows, that fills in the step in Theorem 6.27's right-hand
  inequality this reading found asserted. The other bridges (Theorems 2.10
  and 3.6) were checked and are standard. Only the distortion-rate clause
  waits on that check. It is refuted by a computable source f for which
  expected Kolmogorov complexity exceeds entropy by more than K(f) plus a
  constant. It is also refuted by a recursive source and distortion for
  which (1/m) E h_x(mR) fails to converge to D*(R). Empirical compression
  ratios cannot settle it, since a real compressor gives only upper bounds
  on K.
title: 'Shannon entropy, mutual information and the distortion-rate function are the expectations of their Kolmogorov counterparts only to within the complexity of the source distribution'
version: 1
tags:
- information-theory
- learning-theory
date: '2026-10-14'
source:
- LIT-224
- LIT-239
summary: >-
  Grünwald & Vitányi (2004), [LIT-224](../literature.d/LIT-224.md), read in [NOTE-776](../notes.d/NOTE-776.md). For
  computable f: 0 ≤ E_f K(x) − H(f) ≤ K(f) + O(1) (Thm 2.10);
  I(X;Y) − K(f) < E I(x:y) < I(X;Y) + 2K(f) (Thm 3.6). The expected
  structure function brackets D*_m(R) with a K(f, d, m, R) shift in rate,
  and equals D*(R) per symbol in the limit (Thm 6.27). Sufficiency links
  only one way (Thm 5.13). None of this holds for a complex or unknown
  source, or for one string.
---
<!-- inactive-ok-file: THEORY-277 THEORY-238 THEORY-163 THEORY-157 — Proposed; the companion theory filed today and the entries named under Connections -->

# THEORY-244: Shannon entropy, mutual information and the distortion-rate function are the expectations of their Kolmogorov counterparts only to within the complexity of the source distribution

## Source

Grünwald & Vitányi (2004), [LIT-224](../literature.d/LIT-224.md), read in [NOTE-776](../notes.d/NOTE-776.md): Theorem 2.10
and eq. 2.5, Theorem 3.6 and Lemma 3.7, Proposition 5.3, Remark 5.11,
Theorem 5.13, Example 6.13, Theorem 6.27 and Corollary 6.29. The
structure function itself is Vereshchagin & Vitányi's ([LIT-239](../literature.d/LIT-239.md)), read in
[NOTE-787](../notes.d/NOTE-787.md).

## What was actually shown

**One mechanism.** A computable mass function f is dominated by the
universal distribution: f(x) ≤ 2^{K(f)+O(1)} m(x), with −log m(x) =
K(x) + O(1). So, pointwise, log 1/f(x) ≥ K(x) − K(f) − O(1), and the
noiseless coding theorem gives the other side in expectation.

**Entropy (Theorem 2.10).** 0 ≤ Σ_x f(x)K(x) − H(f) ≤ K(f) + O(1). The gap
is real. A point mass on one string x of length n with K(x) > n has
H = 0 and expected complexity above n, and then K(f) ≥ K(x). With f
supplied as an oracle, the gap is O(1) (eq. 2.5).

**Mutual information (Theorem 3.6, Lemma 3.7).** For computable joint f,
I(X;Y) − K(f) < Σ f(x,y) I(x : y) < I(X;Y) + 2K(f) to within O(1). With f
in the conditional, equality holds to O(1).

**Distortion–rate (Theorem 6.27, Corollary 6.29).** For a recursive
distortion d, a total recursive f and m i.i.d. repetitions,
(1/m) E h_x(mR + K(f, d, m, R) + O(log n)) ≤ D*_m(R) ≤ (1/m) E h_x(mR),
and lim_{m→∞} (1/m) E h_x(mR) = D*(R). For the uniform source with
log-cardinality distortion, E h_x(R) = (1 + o(1))(n − R) = (1 + o(1)) D*(R)
(Example 6.13).

**Sufficiency (Theorem 5.13), one way only.** A sequential statistic
that is algorithmically sufficient for every x is nearly sufficient in
expectation for every computable f_θ, with a constant depending on
K(f_θ). It is uniformly so only if sup_θ K(f_θ) < ∞. Individual and
expectation near-sufficiency are different notions once equality is
relaxed to a constant (Remark 5.11). No converse is claimed.

What could have come out otherwise: expected complexity might have
exceeded entropy by an amount growing with n for a fixed simple source.
For a source with K(f) = O(1) it does not.

## What this does not say

- **Not that a string's complexity estimates an entropy, or the reverse.**
  Every bridge is an expectation, and none says anything about one
  outcome. [NOTE-241](../notes.d/NOTE-241.md) applies this correctly to compressed model files.
- **Not that the identification holds for complex or unknown sources.**
  The error is K(f), and for a distribution with complex support or
  "trickily skewed" probabilities it is as large as the quantities
  compared.
- **Not that algorithmic and probabilistic sufficiency coincide.**
  Theorem 5.13 goes from algorithmic to probabilistic, in expectation, for
  computable models. [LIT-224](../literature.d/LIT-224.md)'s earlier summary called every pair an
  expectation identity. For sufficiency it is not, and the summary has
  been corrected.
- **Not that the structure function of structured data looks like rate–
  distortion.** The authors call Theorem 6.27 "a 'sanity check'" for i.i.d.
  sources whose typical data "have the characteristics of random noise".
  For a single structured string the structure function can take any shape
  ([LIT-239](../literature.d/LIT-239.md)), and averaging erases that.
- **Not that the Theorem 6.27 proof is complete.** Its right-hand step
  identifies h_x(mR) with the radius of x's sphere in a canonical cover.
  That is asserted, with complexity conditioned on mR where h_x is
  unconditional. The arXiv record carries the authors' own warning about
  errors in the draft.

## Connections

- **[THEORY-277](THEORY-277.md).** The individual structure-function theorem whose
  expectation appears here.
- **[THEORY-238](THEORY-238.md).** Its "MDL" is a Shannon coding rate under a prior, not
  Kolmogorov complexity. This theory says how far apart the two can be:
  up to K(f) in expectation, and without bound for one outcome.
- **[THEORY-163](THEORY-163.md).** The colour-naming account uses the information-bottleneck
  form of rate–distortion, an expectation over a known source. This
  theory says what an individual-data version would differ by. No reading
  connects the two directly.
- **[THEORY-157](THEORY-157.md) and [CLAIM-152](../claims.d/CLAIM-152.md).** Proposition 5.3 shows the individual,
  expectation and mutual-information definitions of classical sufficiency
  are equivalent when exact. Remark 5.11 shows they separate under
  approximation, which is how any computed sufficiency is held.
