---
number: 229
status: Skimmed
formerly:
- NOTE-tmpl1ann
paper: LIT-255
title: 'Information Theory with Kernel Methods'
version: 1
date: '2026-09-26'
summary: >-
  With a kernel normalised to k(x,x) = 1, the covariance operator Σ_p = E_p[ϕ(x)ϕ(x)*] is a density operator (PSD, unit trace), injective in p when k² is universal. Its von Neumann entropy and relative entropy behave like Shannon quantities, with D(Σ_p‖Σ_q) ≤ D(p‖q), and the empirical versions are computed from the normalised Gram matrix K/n.
---
<!-- inactive-ok-file: LIT-255 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-229: Information Theory with Kernel Methods

## Contribution

The paper studies probability distributions through their covariance operators in a reproducing kernel Hilbert space. It shows that the von Neumann entropy and relative entropy of these operators are closely related to Shannon entropy and relative entropy, share many of their properties, and come with efficient estimators. For tensor-product kernels it defines kernel mutual information and joint entropies, which characterise independence perfectly and conditional independence only partially. It also uses the new relative entropies to derive upper bounds on log-partition functions, giving a family of variational inference methods.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §2.1–2.2, (A1) and Proposition 1: with k(x,x) = 1, Σ_p is self-adjoint, PSD and unit-trace, and p ↦ Σ_p is injective if k² is universal. It is defined by ⟨g, Σ_p f⟩ = E_p[f(X)g(X)], i.e. it is the L²(p) inner product pulled back to the RKHS.
- §3 opening: "Our covariance operators … can thus be seen as 'density operators'". Quantum-information quantities are then applied to them.
- §4, eq. (6) and Propositions 3–4: the kernel KL divergence D(Σ_p‖Σ_q) = tr[Σ_p(log Σ_p − log Σ_q)] is non-negative, zero iff p = q under universality of k², jointly convex, bounded above by the Shannon KL (Prop. 4(d)), and bounded below by ½‖Σ_p − Σ_q‖²_* (Prop. 4(e)).
- §5, Proposition 6, eq. (11): tr[Σ̂_p log Σ̂_p] = tr[(K/n) log(K/n)] for the empirical covariance. The normalised Gram matrix is the finite-sample density matrix.
- §8: the future directions named are Rényi-entropy versions and further log-partition approximation guarantees.

## Open questions

- It is the rigorous version of the "density matrix" reading of kernel embeddings. Σ_p is the state and the Gram matrix K/n its empirical estimate. The same objects (fidelity and Bures between normalised kernel matrices) are what the representation-similarity literature compares. It also connects this strand to the Radon–Nikodym/KL strand, since the kernel KL lower-bounds the true KL.
- The pull-back identity ⟨g, Σ_p f⟩ = E_p[fg] is exactly the commutative GNS inner product of the state E_p restricted to RKHS functions. A deeper reading should check whether Bach draws that link anywhere (not seen in the sections read).
- Check the multivariate section (§6) for kernel mutual information, which is relevant to information-bottleneck readings.
