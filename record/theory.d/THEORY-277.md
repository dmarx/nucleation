---
number: 277
status: Proposed
formerly:
- THEORY-tmppce05
promote_when: >-
  An independent derivation of Theorem IV.8 of LIT-239, or a published
  restatement with its own proof, such as the later algorithmic-statistics
  surveys by Vereshchagin and Shen, read here. The record has read the
  proof once and checked its counting, but not every constant. It is
  refuted by a string x and a bound α for which some set of complexity at
  most α + O(log n) minimises two-part length and yet has randomness
  deficiency more than c log n above β_x(α), for every constant c. What
  cannot settle it is a practical MDL procedure that works or fails on
  parametric families. Those are not the complexity-bounded classes the
  theorem is about, and the authors say the result does not transfer
  directly.
title: 'For individual data, at every bound on model complexity, the model with the shortest two-part code is, to within O(log n), the best-fitting model in randomness deficiency, although the fit itself cannot be computed or approximated'
version: 1
tags:
- learning-theory
- information-theory
- mathematics
date: '2026-10-14'
source:
- LIT-239
- LIT-224
summary: >-
  Vereshchagin & Vitányi (2002/2004), [LIT-239](../literature.d/LIT-239.md), read in [NOTE-787](../notes.d/NOTE-787.md),
  Theorem IV.8: β_x(α) + K(x) and λ_x(α) agree to within O(log n) for a
  string of length n. Every set minimising K(S) + log |S| at complexity α
  is within O(log n) of the best fit there. h_x and λ_x are upper
  semicomputable, while β_x is not semicomputable. Restated by Grünwald &
  Vitányi, [LIT-224](../literature.d/LIT-224.md), §6.2. Finite-set models; computable distributions at
  O(log n) cost. It says nothing at the (k/2) log n scale of parametric
  model selection, and nothing about K(A) + K(x | A).
---
<!-- inactive-ok-file: THEORY-259 THEORY-244 THEORY-036 THEORY-087 — Proposed; the companion theories filed today and the entries named under Connections -->

# THEORY-277: For individual data, at every bound on model complexity, the model with the shortest two-part code is, to within O(log n), the best-fitting model in randomness deficiency, although the fit itself cannot be computed or approximated

## Source

Vereshchagin & Vitányi (arXiv 2002; IEEE Trans. Inf. Theory 2004),
[LIT-239](../literature.d/LIT-239.md), read in [NOTE-787](../notes.d/NOTE-787.md). The pointers are §§II–V, Lemma IV.2,
Theorems IV.4, IV.8 and IV.11, Remark IV.10, Lemma C.4, Claim C.5,
Appendix B and Theorems D.1–D.6. Restated without proof by Grünwald &
Vitányi, [LIT-224](../literature.d/LIT-224.md) §6.2, read in [NOTE-776](../notes.d/NOTE-776.md).

## What was actually shown

**Setting.** One finite string x, of length n and complexity K(x) = k.
Models are finite sets S ∋ x. Three functions of a complexity bound α:

- h_x(α) = min{log |S| : K(S) ≤ α}, Kolmogorov's structure function, or
  constrained maximum likelihood;
- λ_x(α) = min{K(S) + log |S| : K(S) ≤ α}, the constrained two-part MDL
  length;
- β_x(α) = min{log |S| − K(x | S) : K(S) ≤ α}, the best achievable
  randomness deficiency, or best fit.

Small deficiency means x has every simple property that most members of S
have (Lemma II.3).

**The theorem (IV.8).** β_x(α) + k and λ_x(α) are within O(log n) of each
other in argument and value, and so is h_x(α) + α by Lemma IV.2. One
direction is immediate from δ(x | A) = Λ(A) − K(A | x*) − k + O(1). The
other rests on Lemma C.4. For every A ∋ x there is an S ∋ x of the same
size with K(S) ≤ K(A) − K(A | x) + O(log Λ(A)). Its proof is a counting
argument over enumerated sets, and [NOTE-787](../notes.d/NOTE-787.md) checked the counting.
Remark IV.10 states the practical form. Every set of complexity at most
α + O(log n) that minimises two-part length has deficiency at most
β_x(α) + O(log n).

**What could have come out otherwise.** Before the paper, only
β_x(α) ≤ h_x(α) + α − K(x) + O(1) was known. Theorem IV.4 shows that
λ_x(α) ≫ K(x) happens for some (x, α). At those points nothing forces a
small set to be a typical one, and the theorem says it is anyway.

**The asymmetry.** The converse fails. A best-fitting set need not
minimise code length. In the counterexample, S₁ = {0,1}ⁿ ∪ {y} has
optimal fit for random x but two-part length 3n/2 against λ_x = n
(Remark IV.10). The two coincide only at "critical" α, where λ_x is still
falling (Theorem IV.11).

**Computability.** h_x and λ_x, and their witnesses, can be approximated
from above by dovetailing (§VIII). β_x cannot be approximated from below
within |x|/3 or from above within |x|/log⁴ |x| (Theorem D.6). Given x and
K(x), no algorithm approximates λ_x within |x|/(10 log |x|) or finds the
minimal sufficient statistic (Theorem D.2, Corollary D.3). So the fit is
reached by minimising code length, a quantity that can be searched,
although the fit itself cannot be measured.

## What this does not say

- **Not that practical MDL selects best-fitting models.** The models are
  complexity-bounded classes of finite sets, or computable distributions
  with K(P) ≤ n + O(log n) at O(log n) extra cost (Appendix B). The
  authors call parametric families "partially poorer and partially richer"
  and say the results "cannot be directly transplanted to the traditional
  setting" (§IV-D).
- **Not anything at the scale of parametric model selection.** The
  precision is O(log n). The (k/2) log n penalty that separates
  k-parameter models in BIC or NML ([THEORY-087](THEORY-087.md), [LIT-238](../literature.d/LIT-238.md)) lies inside the
  error term.
- **Not that minimising K(A) + K(x | A) works.** Only the worst-case data
  code log |S| (or −log P(x)) carries the guarantee. §V-B(iii) gives
  examples where the "ultimate compression" form picks a model of
  deficiency n/2 against a best of n/4. This bears on the ideal MDL of
  Vitányi & Li ([LIT-225](../literature.d/LIT-225.md)), filed as [THEORY-259](THEORY-259.md).
- **Not that best-fitting models are found in finite time.** The
  dovetailed MDL search converges at an unknown time. Before that it
  carries only the bound δ(x | L_t) + K(x) ≤ |p_t| + log |S_t| + O(1).
- **Not that the minimal sufficient statistic is unique or a canonical
  boundary.** At non-critical α, independent sets witness the same λ_x.
  The minimal sufficient statistic is defined to logarithmic precision and
  cannot be computed.
- **Not that most data have simple models.** Non-stochastic strings,
  whose structure function stays above the sufficiency line until α ≈ K(x),
  exist for every length and complexity (Corollary IV.9). The paper gives
  existence, not frequency.

## Connections

- **[THEORY-244](THEORY-244.md)** relates the expected structure function to Shannon's
  distortion-rate function ([LIT-224](../literature.d/LIT-224.md), Theorem 6.27). This theory is the
  individual-data statement that one averages.
- **[THEORY-259](THEORY-259.md)** is the Bayesian route to the same two-part code, and
  holds only for data random for the hypothesis. This theory needs no
  such condition: it holds for every x, and the deficiency it controls is
  the amount by which x fails that condition.
- **[CLAIM-152](../claims.d/CLAIM-152.md).** The algorithmic sufficient statistic has no target
  variable. It is sufficient for x itself, relative to the reference
  machine. That is a qualification of "any individuation built on
  sufficiency", and it does not give a unique boundary either (above).
- **[THEORY-036](THEORY-036.md).** The split of a shortest description into model bits and
  noise bits is a formal version of Dennett's "description more efficient
  than the bit map" that separates pattern from noise. Neither [LIT-239](../literature.d/LIT-239.md)
  nor [LIT-224](../literature.d/LIT-224.md) cites Dennett, and the link is the record's.
