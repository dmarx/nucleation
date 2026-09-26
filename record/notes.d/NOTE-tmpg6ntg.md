---
status: Skimmed
paper: LIT-tmpyrhlj
title: 'Kernel mean embedding of distributions (review)'
version: 1
date: '2026-09-26'
summary: >-
  Point evaluation is bounded on an RKHS, so the Riesz theorem gives the reproducing kernel k_x. Likewise, when E√k(X,X) < ∞ the expectation functional f ↦ E_P f is bounded, so Riesz gives a unique mean embedding μ_P with E_P f = ⟨f, μ_P⟩. MMD is then the RKHS distance ‖μ_P − μ_Q‖, and it separates distributions exactly when the kernel is characteristic.
---
<!-- inactive-ok-file: LIT-tmpyrhlj — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-tmpg6ntg: Kernel mean embedding of distributions (review)

## Contribution

A kernel mean embedding maps a probability distribution into a reproducing kernel Hilbert space, so that kernel methods can be applied to distributions themselves. It generalizes the feature map used by SVMs and other kernel machines. The survey introduces positive-definite kernels and RKHSs, treats the embedding of marginal distributions (theory, estimation, applications such as two-sample and independence testing and learning on distributional data), then conditional distributions (graphical models, probabilistic inference, reinforcement learning, causal discovery). It closes with open problems.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §2.2, Def. 2.4 and Thm 2.4: an RKHS is defined as a Hilbert space of functions with bounded evaluation functionals. Riesz is stated as Thm 2.4 (eq. 2.15). Prop. 2.1 (eq. 2.16) derives from it the representer k_x with f(x) = ⟨k_x, f⟩, and eq. 2.17 gives k(x,y) = ⟨k_x,k_y⟩.
- Thm 2.5, attributed to Aronszajn (1950): every positive-definite k has a unique (up to isometric isomorphism) RKHS with k as reproducing kernel, and conversely. Thm 2.1 states Mercer's theorem for the integral operator T_k on L²(X,μ).
- §3.1, Lemma 3.1 (credited to Smola et al. 2007): if E_P√k(X,X) < ∞ then μ_P ∈ H and E_P f = ⟨f, μ_P⟩. The proof bounds the functional L_P f = E_P f by Jensen and applies Riesz (Thm 2.4). The text calls the result "a reproducing property of the expectation operation".
- §3.2, eqs. 3.14–3.16: the cross-covariance operator C_YX is equivalently "the unique bounded operator" with ⟨g, C_YX f⟩ = Cov[g(Y), f(X)]. C_XX is "positive and self-adjoint", and C_XY is the adjoint of C_YX.
- §3.3.1, Def. 3.2: a kernel is characteristic if P ↦ μ_P is injective. §3.5: MMD[H,P,Q] = sup_{‖f‖≤1}(E_P f − E_Q f) = ‖μ_P − μ_Q‖_H (citing Borgwardt et al. 2006 and Gretton et al. 2012a, Lemma 4). The review states the representer theorem only by citation (Schölkopf et al. 2001), in §3.4 and §3.7.

## Open questions

- It is the one held text that runs the whole chain Riesz → k_x → Moore–Aronszajn → μ_P → MMD/HSIC in numbered statements. That makes it the natural citation for the claim that "Riesz makes kernels exist".
- For SSL: any objective written as E k(z,z′) over pairs is a squared norm or inner product of mean embeddings. SSL-HSIC (ra6) makes this explicit. A deeper read of §3.6 (HSIC) should supply the operator-level statements.
- Check §5, the relation to other methods, for anything on learned (non-fixed) kernels. Every result here assumes a fixed k, whereas SSL learns the feature map.
