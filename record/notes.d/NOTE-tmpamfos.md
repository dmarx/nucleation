---
status: Skimmed
paper: LIT-tmprn7bc
title: 'Belghazi et al., MINE'
version: 1
date: '2026-09-26'
summary: >-
  Mutual information is stated measure-theoretically as the expectation under the joint of log dP_XZ/d(P_X⊗P_Z), and its Donsker–Varadhan dual is tight exactly at T* = log dP/dQ + C, so a neural critic trained on the dual is a log Radon–Nikodym-derivative estimator.
---
<!-- inactive-ok-file: LIT-tmprn7bc — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-tmpamfos: Belghazi et al., MINE

## Contribution

The authors argue that mutual information between high-dimensional continuous variables can be estimated by gradient descent over neural networks. Their estimator, MINE, scales linearly with dimension and sample size, is trainable by backpropagation and is shown strongly consistent. They apply it to improve adversarially trained generative models and to the information bottleneck in supervised classification.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1, Eq. 1: I(X;Z) = ∫ log [dP_XZ / d(P_X⊗P_Z)] dP_XZ — the Radon–Nikodym form, with the marginals defined by integrating P_XZ.
- §2.1, Eq. 3–4: I(X,Z) = D_KL(P_XZ ‖ P_X⊗P_Z) with D_KL(P‖Q) := E_P[log dP/dQ] "whenever P is absolutely continuous with respect to Q" (infinite otherwise, footnote 2); footnote 1 says one can think of Lebesgue densities on a compact domain.
- §2.2, Theorem 1 (Donsker–Varadhan): D_KL(P‖Q) = sup_T E_P[T] − log E_Q[e^T]; Eq. 7: the bound is tight for T* with dP = (1/Z)e^{T*}dQ; Eq. 8 gives the weaker f-divergence (NWJ) bound E_P[T] − E_Q[e^{T−1}].
- Appendix 8.2.1, Eq. 23–25: the gap equals D_KL(P‖G) for the Gibbs measure dG = e^T dQ / Z, so the bound is tight exactly for T* = log dP/dQ + C.
- 8.2.2: consistency proofs assume a compact domain of R^d and all measures absolutely continuous w.r.t. Lebesgue measure.
- §5.3 is titled "Information Bottleneck" (not read).

## Open questions

- This is the representation-learning paper that states MI as the expectation of a log Radon–Nikodym derivative in so many words — the link from Adler's coda ([LIT-243](../literature.d/LIT-243.md), Thm 5.1) to the bottleneck objective.
- Poole et al. (rb1, §2.2) note that the Monte-Carlo DV estimate MINE uses is neither an upper nor a lower bound; a deeper reading should check how §3 handles this and what "strongly consistent" is proved under.
- Read §5.3 to see whether the IB experiment is stated in the RN form or with densities.
