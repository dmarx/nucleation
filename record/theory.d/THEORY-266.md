---
number: 266
status: Active
formerly:
- THEORY-tmphaadr
title: "For a loss in [0, 1] that is L-Lipschitz in a distortion, with probability at least 1 − δ the average generalisation error along an optimisation trajectory is bounded, under a square root, by the rate-distortion function of the trajectory's law given the sample, a coupling term that carries the trajectory's dependence on the sample, and a distortion term 4Lε"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision
    for THEORY-266 (batch 038). The title now names the theorem's
    hypotheses (a loss in [0, 1], L-Lipschitz in a distortion), its form
    (a high-probability bound under a square root) and its third term,
    4Lε. The proof of Theorem 7 (App. E-H) was re-checked step by step,
    in the dated note below, given the general framework THEORY-263
    holds. The promote_when asked for an evaluation that would settle
    whether the trajectory's compressibility accounts for
    generalisation, which this account does not claim and its first
    "does not say" disclaims; it moves unchanged to QUESTION-tmphiinp.
tags:
- learning-theory
- information-theory
date: '2026-10-14'
source:
- LIT-233
summary: >-
  Sefidgaran & Zaidi (2023), [LIT-233](../literature.d/LIT-233.md), Theorem 7, read in [NOTE-806](../notes.d/NOTE-806.md).
  For an L-Lipschitz loss in [0, 1], with probability ≥ 1 − δ, the mean of
  gen(S, W^t) over iterations is at most √((RD(S, ε; π_S) +
  log(√(2n)M/δ))/(2n − 1) + 4Lε). RD is computed for the sample at hand.
  The coupling coefficient M depends on the unknown distribution and
  absorbs I(W^T; S). The CIFAR-10 experiment drops M and 4Lε and shows
  only that the estimated rate and the test gap fall together over
  learning rates. For FCN4 the plotted rate term is about 3, which is
  vacuous for 0–1 loss.
---
<!-- inactive-ok-file: THEORY-263 — Proposed; the framework this theorem is an instance of and the fixed-rate bound it moves to trajectories, filed today -->

# THEORY-266: For a loss in [0, 1] that is L-Lipschitz in a distortion, with probability at least 1 − δ the average generalisation error along an optimisation trajectory is bounded, under a square root, by the rate-distortion function of the trajectory's law given the sample, a coupling term that carries the trajectory's dependence on the sample, and a distortion term 4Lε

## Source

Sefidgaran & Zaidi (2023), [LIT-233](../literature.d/LIT-233.md), read in full in [NOTE-806](../notes.d/NOTE-806.md):
§IV-C (eqs. 32–34, Theorems 6 and 7), §V and Figure 1, Appendix B,
Appendix D, and proofs E-G and E-H.

## What was actually shown

**The quantity.** gen(S, W^T) is the average of gen(S, W^t) over
iterations t in a window T = [t₁ : t₂] (eq. 32). The authors take the
average rather than the supremum used by Şimşekli et al., because a
discrete-time trajectory has Hausdorff dimension zero.

**Theorem 7.** If the loss is in [0, 1] and L-Lipschitz in a distortion
ρ, then with probability ≥ 1 − δ,

E_{W^T∼π_S} gen(S, W^T) ≤ √((RD(S, ε; π_S) + log(√(2n)M/δ))/(2n − 1) + 4Lε),

where RD(s, ε; π_s) is the least I(W^T; Ŵ^T) with average
per-iteration distortion ≤ ε, under the trajectory law for the given
sample (eq. 34). M := exp(sup_{ν_S ∈ G^δ_S} E_{π_S} log dπ_S/d[π_S
ν_S]_{W^T}), with G^δ_S the KL ball around μ^{⊗n}.

**Where the dependence on the sample goes.** In the proof (E-H, steps d
and e) the chain rule splits I(W^T; S, Ŵ^T) into I(W^T; Ŵ^T | S) and
I(W^T; S). The first becomes the data-dependent RD term. The second is
bounded by the supremum in M. So RD measures how compressible the
trajectory is given the data, and the trajectory's information about the
data enters only through M. The paper says M "measures the dependency of
W^T on S" and can be bounded by I_∞(S; W^T).

**Theorem 6** is the data-independent version, with a supremum of the
rate-distortion function over the KL ball and no M.

**The experiment.** FCN4 and CNN4 on CIFAR-10, SGD at about seven
learning rates in [5e−5, 1e−3], trained to 100% training accuracy. RD is
estimated with a neural estimator (NERD) on random sub-blocks of the last
ten epochs of normalised weights, under RMSE at D = 6.5, and scaled to the
model's size. √(R(D)/(2n − 1)) is plotted on a second axis beside the
test-estimated gap. Both fall as the learning rate grows, and CNN4 has
the smaller rate and the smaller gap. M and 4Lε are ignored, "similar to
in [25]".

## What this does not say

- **Not that compressible trajectories explain generalisation.** The term
  dropped in the experiment is the one that carries the trajectory's
  dependence on the sample. With it gone, what is compared is how
  compressible the trajectory is given the data, and the theorem does not
  say that this alone bounds anything.
- **Not a non-vacuous bound.** For FCN4 the plotted term is about 2.9–3.1
  against a 0–1 generalisation gap of about 0.49. For CNN4 it is about
  0.3–0.55 against 0.32–0.37. Only the ordering over learning rates is
  compared, on separate axes.
- **Not data-dependent in full.** M depends on μ through G^δ_S, and no way
  to estimate it is given.
- **Not about the final model.** The bound is on the average over a
  window of iterations. The paper links it to the final model only by an
  ergodicity remark.
- **Not about rate-distortion dimension in practice.** The link to the
  rate-distortion dimension of a process, Rényi information dimension and
  metric mean dimension is stated through cited work, not proved for
  training trajectories.
- **Not advice.** That larger learning rates gave smaller gaps here is an
  observation on two networks, not an instruction, and any use of it as
  one belongs to the anthology.

## Connections

- **[THEORY-263](THEORY-263.md)** holds the variable-rate framework this theorem is an
  instance of (Theorem 4 with ε replaced by 4Lε).
- **[THEORY-248](THEORY-248.md) ([LIT-236](../literature.d/LIT-236.md))** bounds generalisation by the
  rate-distortion function of the final output's marginal law. This
  theorem moves the rate to the trajectory and conditions on the sample.
- **[THEORY-028](THEORY-028.md).** [NOTE-306](../notes.d/NOTE-306.md) composed a per-step bit count from that bound
  and found it vacuous. It named the information a training run actually
  carries about its data as the informative quantity. Here that quantity
  is exactly what M absorbs and the experiment drops.

## Note of 2026-10-19: the proof of Theorem 7, re-checked

The proof (App. E-H, arXiv v3 pp. 24–26) applies the general variable-rate
theorem (Theorem 4, the framework [THEORY-263](THEORY-263.md) holds) to f = gen², with
Δ = (RD(S, ε; π_S) + log(√(2n)M/δ))/(2n − 1) + 4Lε. The steps:

- **Compression with distortion 4Lε in f.** For each sample s, take a
  kernel from W^T to Ŵ^T with average distortion at most ε. Then replace it
  by the kernel from the joint marginal of (W^T, Ŵ^T), so that S − W^T − Ŵ^T
  is a Markov chain with the same (W^T, Ŵ^T) marginal. Since gen lies in
  [−1, 1], |gen(w)² − gen(ŵ)²| ≤ 2|gen(w) − gen(ŵ)|. Population and
  empirical risk are each L-Lipschitz, so |gen(w) − gen(ŵ)| ≤ 2Lρ(w, ŵ). The
  distortion in f is therefore at most 4Lε.
- **The exponential moment.** For a fixed ŵ^T, gen(S, ŵ^T) is a centred mean
  of n terms in [0, 1], hence 1/(2√n)-subgaussian. At λ = 2n − 1 this gives
  E e^{λ gen²} ≤ √(2n).
- **The information term.** By data processing under the Markov chain,
  I(S; Ŵ^T) ≤ I(W^T; Ŵ^T). That is at most I(W^T; S, Ŵ^T) =
  I(W^T; Ŵ^T | S) + I(W^T; S). The infimum of the first term over the
  per-sample kernels is the rate given the sample, RD(s, ε; π_s).
- **The coupling.** I(W^T; S) = E log dπ_S/d[π_S ν_S]_{W^T}, which is at most
  E log M for ν_S in the KL ball that defines M.
- Substituting Δ cancels these terms and leaves log δ, which is Theorem 4's
  condition. With probability at least 1 − δ, E_{π_S} gen² ≤ Δ, and Jensen
  gives E_{π_S} gen ≤ √Δ.

So the dependence of the trajectory on its sample enters only through M,
as the body says, and RD is a rate given the sample. Theorem 4 itself is
taken as [NOTE-806](../notes.d/NOTE-806.md) followed it and is not re-derived here.

