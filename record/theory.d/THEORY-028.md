---
number: 28
status: Active
formerly:
- THEORY-tmp6r1ax
title: 'The expected bias of any data-dependent choice, and the expected generalisation error of any learning algorithm, is at most √(2σ²·I) for σ-subgaussian losses, where I is the information the output carries about the data'
version: 1
tags:
- learning-theory
- information-theory
- probabilistic-modeling
date: '2026-09-30'
source:
- LIT-356
- LIT-347
summary: >-
  Russo & Zou (2015), [LIT-356](../literature.d/LIT-356.md), Prop. 1: |E[φ_T − µ_T]| ≤ σ√(2·I(T;φ)) for any
  selection T among σ-sub-Gaussian statistics. Xu & Raginsky (2017),
  [LIT-347](../literature.d/LIT-347.md), Thm 1: |gen| ≤ √(2σ²·I(S;W)/n) for any algorithm P_{W|S}. Both
  proofs rest on Donsker–Varadhan and were checked by the readers. The
  bound is in expectation only. It is vacuous for deterministic learners on
  continuous hypotheses, where I(S;W) is infinite, and for any real network
  when I is bounded by counting bits. It is tight only for Gaussian argmax
  and threshold selection.
---

# THEORY-028: The expected bias of any data-dependent choice, and the expected generalisation error of any learning algorithm, is at most √(2σ²·I) for σ-subgaussian losses, where I is the information the output carries about the data

## Source

- Russo & Zou (2015; IEEE Trans. Inf. Theory 2020), [LIT-356](../literature.d/LIT-356.md), Props. 1–3 and 7, Lemmas 1–2, as read in [NOTE-308](../notes.d/NOTE-308.md).
- Xu & Raginsky (2017), [LIT-347](../literature.d/LIT-347.md), Lemma 1, Theorems 1–5 and eq. (36), as read in [NOTE-306](../notes.d/NOTE-306.md).

## What was actually shown

**The bound.** Russo & Zou let T choose which of m candidate statistics φ_i to report, by any rule, possibly using outside data and internal randomness. If each φ_i − µ_i is σ-sub-Gaussian, the selection bias obeys |E[φ_T − µ_T]| ≤ σ√(2·I(T;φ)) (Prop. 1). No independence of the data points is needed. Xu & Raginsky set φ to the empirical risks and T to the output hypothesis W, and extend the result to uncountable hypothesis spaces. They weaken the quantity by data processing to I(S;W). The result is |E[L_μ(W) − L_S(W)]| ≤ √(2σ²·I(S;W)/n) for any Markov kernel P_{W|S} (Thm 1). The mechanism is one decoupling inequality, Donsker–Varadhan plus a subgaussian moment bound. [NOTE-306](../notes.d/NOTE-306.md) checked the proof of Lemma 1, and [NOTE-308](../notes.d/NOTE-308.md) checked Props. 1, 2, 5 and 8–10 line by line.

**Why this is an explanation and not only a bound.** I(T;φ) = H(T) − H(T|φ), so bias falls in two ways ([NOTE-308](../notes.d/NOTE-308.md), key insight). Signal in the data lowers H(T): as a true effect grows, argmax selection becomes stable and I falls, as shown in simulation in §V-C. Randomisation raises H(T|φ). Only dependence on the part of the data that would change in a replication can bias the reported value. For Gaussian argmax the squared error is Θ(1 + H(T)) (Prop. 3), so there the quantity is the right one, not merely an upper bound.

**Composition.** Information adds over adaptive steps. For Russo & Zou it is I(T_{k+1};φ) ≤ Σ_i I(Y_{T_i}; φ_{T_i} | H_{i−1}, T_i) (Lemma 1), and for Xu & Raginsky I(S;W_k) ≤ Σ_j I(S;W_j | W^{j−1}) (eq. 36). With Gaussian answer noise of variance σ²√j/n, the k-th adaptive answer's error is O(σk^{1/4}/√n). Without noise it can be Ω(σ√(k/n)) (Prop. 7, App. H).

The theorems are proved and the readers checked them. The status is for the bound as stated, not for any claim that it explains deep-network generalisation.

## What this does not say

- **Anything beyond expectation.** Both headline bounds are on expected bias or error. High-probability versions need extra machinery ([LIT-347](../literature.d/LIT-347.md) Thm 3) or are left to the differential-privacy literature.
- **That it is informative for deterministic training.** For a deterministic algorithm on continuous W, I(S;W) is typically infinite. The remedies are quantisation (I ≤ H(W), eq. 20) or injected noise ([NOTE-306](../notes.d/NOTE-306.md)). A per-step bit count gives √((2σ²/n)·Σ_t S_grad,t). [NOTE-306](../notes.d/NOTE-306.md) composed this itself, and it is vacuous for any real network, since m·b·T ≫ n. Lossy and data-dependent refinements ([LIT-236](../literature.d/LIT-236.md), [LIT-233](../literature.d/LIT-233.md)) exist but are Deferred and unread.
- **That the bound is tight in general.** Russo & Zou's "tight in natural settings" is shown for squared error under Gaussian argmax and for large-threshold rules only ([NOTE-308](../notes.d/NOTE-308.md), C3). App. B.A gives a deterministic example with I = log m and zero bias.
- **That minibatch SGD is a noisy query in the sense of Lemma 2.** ½·log(1 + SNR) per query needs noise independent of the data. Minibatch noise is the data's own sampling, and no reading in the record makes the step to SGD ([NOTE-308](../notes.d/NOTE-308.md), Bearing 3).
- **That Prop. 5 bounds generalisation over random inputs.** It bounds label-noise overfitting with the inputs held fixed.

## Connections

- [LIT-348](../literature.d/LIT-348.md) (McCandlish) is the other half of the prior-art map's row 12. It shares no content with these two papers, and the bridge from its batch SNR to a per-step information term is an open question in [NOTE-306](../notes.d/NOTE-306.md) and [NOTE-308](../notes.d/NOTE-308.md).
- The Gibbs algorithm, e^{−βL_S}·Q ([LIT-347](../literature.d/LIT-347.md) Thm 5), is the information-regularised ERM. Its β is an inverse temperature only by analogy.
