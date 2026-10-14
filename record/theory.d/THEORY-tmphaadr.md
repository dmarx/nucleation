---
status: Proposed
promote_when: >-
  An evaluation of Theorem 7's bound for a trained network that bounds
  or estimates the coupling coefficient M from data and keeps the 4Lε
  term, with the rate-distortion function estimated by a method whose
  error is controlled. That would settle whether the trajectory's
  compressibility given the sample accounts for generalisation, which is
  what the account invites. The theorem itself is refuted only by a
  counterexample to it. What cannot settle it: co-movement of an
  estimated rate with test error across learning rates or architectures,
  with M dropped, which is the evidence the paper offers.
title: "The average generalisation error along an optimisation trajectory is bounded by the rate-distortion function of the trajectory's law given the sample, plus a coupling term that carries the trajectory's dependence on the sample"
version: 1
tags:
- learning-theory
- information-theory
date: '2026-10-14'
source:
- LIT-233
summary: >-
  Sefidgaran & Zaidi (2023), [LIT-233](../literature.d/LIT-233.md), Theorem 7, read in [NOTE-tmps2bys](../notes.d/NOTE-tmps2bys.md).
  For an L-Lipschitz loss in [0, 1], with probability ≥ 1 − δ, the mean of
  gen(S, W^t) over iterations is at most √((RD(S, ε; π_S) +
  log(√(2n)M/δ))/(2n − 1) + 4Lε). RD is computed for the sample at hand.
  The coupling coefficient M depends on the unknown distribution and
  absorbs I(W^T; S). The CIFAR-10 experiment drops M and 4Lε and shows
  only that the estimated rate and the test gap fall together over
  learning rates. For FCN4 the plotted rate term is about 3, which is
  vacuous for 0–1 loss.
---
<!-- inactive-ok-file: THEORY-tmpgdeej THEORY-tmp7xiz6 — Proposed; the framework this theorem is an instance of and the fixed-rate bound it moves to trajectories, filed today -->

# THEORY-tmphaadr: The average generalisation error along an optimisation trajectory is bounded by the rate-distortion function of the trajectory's law given the sample, plus a coupling term that carries the trajectory's dependence on the sample

## Source

Sefidgaran & Zaidi (2023), [LIT-233](../literature.d/LIT-233.md), read in full in [NOTE-tmps2bys](../notes.d/NOTE-tmps2bys.md):
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

- **[THEORY-tmpgdeej](THEORY-tmpgdeej.md)** holds the variable-rate framework this theorem is an
  instance of (Theorem 4 with ε replaced by 4Lε).
- **[THEORY-tmp7xiz6](THEORY-tmp7xiz6.md) ([LIT-236](../literature.d/LIT-236.md))** bounds generalisation by the
  rate-distortion function of the final output's marginal law. This
  theorem moves the rate to the trajectory and conditions on the sample.
- **[THEORY-028](THEORY-028.md).** [NOTE-306](../notes.d/NOTE-306.md) composed a per-step bit count from that bound
  and found it vacuous. It named the information a training run actually
  carries about its data as the informative quantity. Here that quantity
  is exactly what M absorbs and the experiment drops.
