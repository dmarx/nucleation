---
number: 837
status: Read
formerly:
- NOTE-tmpeh5ik
paper: LIT-255
title: 'Bach — Information Theory with Kernel Methods'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (2202.08545v2, 26 August 2022, 47
    pp.), text extracted with pdftotext: §§1–8 with every in-text proof
    and figure caption, and appendix A (A.1–A.4, the operator convexity,
    monotonicity and concavity proofs). Followed at the level of their
    statements and structure, not line by line: appendix B (the proof of
    Proposition 5) and appendix C (the concentration and
    degrees-of-freedom arguments behind Propositions 7 and 8). The
    published IEEE Transactions on Information Theory version was not
    read.
date: '2026-10-14'
summary: >-
  With a continuous kernel normalised to k(x,x) = 1 on a compact set, the
  uncentred covariance operator Σ_p is a density operator. Its quantum
  relative entropy is sandwiched between the KL of two kernel-smoothed
  distributions and the KL itself, D(p̃‖q̃) ≤ D(Σ_p‖Σ_q) ≤ D(p‖q), with
  equality on the right only for an orthonormal, hence discrete,
  embedding. On the torus the gap is O(σ²) in the bandwidth. Kernel
  mutual information characterizes independence; conditional
  independence only one way.
---

# NOTE-837: Bach — Information Theory with Kernel Methods

## Contribution

It defines a von Neumann entropy and relative entropy for probability
distributions through their RKHS covariance operators. It proves that
they have the main properties of the Shannon quantities and lower-bound
them. It gives estimators from samples at rate O(1/√n) without
regularization. It applies the construction to independence, data
processing and submodularity, and to upper bounds on log-partition
functions. Before it, kernel mean embeddings gave a metric on
distributions (MMD) with no direct tie to Shannon quantities. After it,
the second moment gives one that has that tie.

## Key insight

The uncentred covariance Σ_p = ∫ϕ(x)ϕ(x)* dp(x) of a unit-norm feature
map is a mixture of rank-one projections, so it is a density operator.
The map p ↦ Σ_p is then a channel from classical distributions to
quantum states. Every quantum inequality, from joint convexity to
monotonicity to Pinsker, becomes a statement about distributions. The
loss relative to Shannon is exactly the overlap between the states
ϕ(x)ϕ(x)* for nearby points.

## Assumptions

- **(A1)** X compact; k continuous, positive definite, with k(x,x) = 1
  for all x. So ‖ϕ(x)‖ = 1 and tr Σ_p = 1. §7 relaxes this to
  k(x,x) ≤ 1, where the upper bound on KL survives.
- **Uncentred.** Footnote 1: the usual centring µ_pµ_p* is not
  subtracted. The object is a second moment, not a covariance in the
  statistical sense.
- **Injectivity** needs k² universal. On a compact set this follows
  from k universal.
- **Kernel entropy** needs a base measure τ. It simplifies to −tr Σ_p log Σ_p
  only on "symmetric sets", where a transitive group preserves k and τ:
  the torus, spheres, finite sets with permutation-invariant K.
- **Proposition 5** needs strictly positive Lipschitz densities with
  respect to τ and a metric on X.
- **Proposition 7** needs the density bounded below by α and a finite
  integrated maximal leverage score c.

## Key results

- **Proposition 1.** Σ_p is self-adjoint, PSD, unit trace. p ↦ Σ_p is
  injective if k² is universal. Σ_p has trivial null space if p has
  full support. Σ_p ≽ µ_p ⊗ µ_p. By definition ⟨g, Σ_p f⟩ = E_p[f(X)g(X)].
- **Proposition 3.** If dp/dq ≤ α, both the kernel and the Shannon KL
  lie in [0, log α].
- **Proposition 4.**
  - (a) D(Σ_p‖Σ_q) ≥ 0, and = 0 iff p = q when k² is universal.
  - (b) The kernel entropy lies in [0, −min_x⟨ϕ(x), (log Σ)ϕ(x)⟩].
  - (c) Joint convexity.
  - (d) **D(Σ_p‖Σ_q) ≤ D(p‖q)**, by joint convexity applied to
    Σ_q = ∫(dq/dp)ϕϕ* dp. "We can only have equality if for all x ≠ y,
    k(x, y) = 0, that is, we have an orthonormal embedding, which is only
    possible for discrete X."
  - (e) D(Σ_p‖Σ_q) ≥ ½‖Σ_p − Σ_q‖²_* ≥ ½‖Σ_p − Σ_q‖²_HS (quantum Pinsker).
- **Eq. (8).** D(p̃‖q̃) ≤ D(Σ_p‖Σ_q) ≤ D(p‖q), where p̃(y) = ∫h(x,y)dp(x)
  with h(x,y) = ⟨ϕ(x), Σ^{−1/2}ϕ(y)⟩², a non-negative smoothing kernel
  that integrates to 1 under τ. The left inequality is monotonicity of
  quantum relative entropy under the measurement D(y) = Σ^{−1/2}ϕ(y)ϕ(y)*Σ^{−1/2}.
- **Proposition 5 and the torus.** 0 ≤ D(p‖q) − D(p̃‖q̃) ≤
  E(p,q)·sup_x ∫h(x,y)d(x,y)²dy. On [0,1]^d with k̂(ω) ∝ e^{−σ‖ω‖₁} and
  d² = Σ sin²π(x_j − y_j), the integral is ≤ dσ²/16. So the kernel KL
  is within O(σ²) of the Shannon KL for Lipschitz densities. The
  constant is linear in d, not exponential.
- **Proposition 6.** tr Σ̂_p log Σ̂_p = tr[(K/n) log(K/n)] for the
  empirical Σ̂_p = (1/n)Σϕ(x_i)ϕ(x_i)*. The non-zero spectra of Σ̂_p and
  K/n coincide. With weights η: Diag(η)^{1/2}K Diag(η)^{1/2}.
- **Proposition 7.** E|tr Σ̂ log Σ̂ − tr Σ log Σ| ≤ (1 + c(8 log n)²)/(nα) +
  (17/√n)(2√c + log n). On the torus c ∝ σ^{−d}. Balancing against the
  O(σ²) bias with σ ∝ n^{−1/(d+4)} gives n^{−2/(d+4)} for Shannon
  entropy, the square root of the minimax n^{−4/(d+4)}. By Jensen, the
  plug-in overestimates the negative entropy in expectation.
- **Proposition 8.** Projecting onto the span of ϕ at n points from τ
  gives a pointwise lower bound on D(Σ_p‖Σ_q). Its error decays as
  exp(−(Bn)^{1/(d+1)}/4) when the leverage scores grow like B log(C/λ)^d.
  This needs integrals of k(x,y)k(x,z) under p, not samples.
- **§6.1 and Proposition 9.** For product kernels and a product base
  measure, H(Σ_{p₁}⊗Σ_{p₂}) = H(Σ_{p₁}) + H(Σ_{p₂}). The kernel mutual
  information I = D(Σ_{p₁₂}‖Σ_{p₁}⊗Σ_{p₂}) = H₁ + H₂ − H₁₂ lower-bounds
  Shannon MI, and is zero iff X₁ ⫫ X₂ when k² is universal. Conditional
  entropies do not decompose: if they did, the axiomatic
  characterizations would force the Shannon entropy back.
- **Proposition 10 (data processing).** D(Σ_{p₁₂}‖Σ_{q₁₂}) ≥ D(Σ_{p₁}‖Σ_{q₁})
  by partial trace. Equality implies equal conditionals p(x₂|x₁) =
  q(x₂|x₁) for universal k. The converse fails.
- **Proposition 11 (submodularity).** H₁₂₃ − H₁₂ − H₂₃ + H₂ ≤ 0. Equality
  implies X₁ ⫫ X₃ | X₂; the converse fails. So the kernel quantities do
  not characterize conditional independence.
- **§7.** Because D(Σ_p‖Σ_q) ≤ D(p‖q), the convex dual
  b(f) = inf_M log tr exp(M + log Σ_q) s.t. f(x) = ⟨ϕ(x), Mϕ(x)⟩
  upper-bounds log ∫e^f dq. As the temperature → 0 it becomes the
  kernel sums-of-squares formulation of global optimization.
  D(Σ_p‖Σ_q) is concave in the kernel and monotone in the PSD order, so
  the bound can be tightened by kernel learning (§7.5, Figs. 3–4). On
  {−1,1}^d this gives an entropy bound that beats the log-det bound in
  Fig. 5.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under (A1) the covariance operator is a density operator, and p ↦ Σ_p is injective when k² is universal | strong | Proposition 1, proofs in text |
| C2 | Kernel relative entropy lower-bounds Shannon relative entropy, with equality only for orthonormal embeddings | strong | Proposition 4(d), proof in text |
| C3 | It is in turn bounded below by the KL of kernel-smoothed distributions, so it is within O(σ²) of KL on the torus for Lipschitz densities | strong | Eq. (8), Proposition 5, torus computation |
| C4 | The empirical kernel entropy is the matrix entropy of K/n and converges at O(1/√n) up to logs, without regularization | strong | Propositions 6–7 |
| C5 | Kernel mutual information characterizes independence exactly, but kernel conditional quantities characterize conditional independence only one way | strong | Propositions 9–11 |
| C6 | The dual of the kernel KL gives computable upper bounds on log-partition functions that the kernel can be optimized to tighten | moderate | §7 derivations; tightness left to future work; toy illustrations |

## Concepts

- **Covariance operator** Σ_p = ∫ϕ(x)ϕ(x)* dp(x). Uncentred here.
- **Kernel relative entropy** D(Σ_p‖Σ_q) = tr[Σ_p(log Σ_p − log Σ_q)].
- **Kernel entropy** H(Σ_p) = −D(Σ_p‖Σ) − min_x⟨ϕ(x), (log Σ)ϕ(x)⟩,
  relative to a base measure τ with covariance Σ.
- **Symmetric set.** One with a transitive group of bijections preserving
  k and τ, on which ⟨ϕ(x), f(Σ)ϕ(x)⟩ is constant in x.
- **Smoothing kernel** h(x,y) = ⟨ϕ(x), Σ^{−1/2}ϕ(y)⟩², which is both PSD
  and a Markov kernel.
- **Kernel mutual information** D(Σ_{p₁₂}‖Σ_{p₁}⊗Σ_{p₂}), not Shannon MI.

## Connections

The construction is the "kernel mean embedding" of the feature map
x ↦ ϕ(x)ϕ(x)*, whose RKHS is that of k². So injectivity reduces to
characteristic kernels. It differs from Bach and Jordan's kernel
generalized variance, which takes the Gaussian MI of a joint covariance
operator and loses independence characterization beyond two variables.
The log-partition bounds connect to the kernel sums-of-squares
formulation of global optimization (reference [44] in the paper). The
quantum tools are taken from Petz, from Wilde's textbook and from the
operator-convexity literature, and appendix A re-proves those it uses.

## Bearing on the record

- **Not held by any THEORY.** No THEORY, CLAIM or QUESTION cites the
  paper. The claim C2–C3 is filed as [THEORY-313](../theory.d/THEORY-313.md).
- **[THEORY-233](../theory.d/THEORY-233.md) (CKA vs normalized Bures).** The seeded LIT says the
  paper's objects are "what the representation-similarity literature
  compares" through fidelity and Bures. Bach never mentions fidelity,
  Bures or representation similarity. The link is the seeder's, and it
  is partly right. For a unit-diagonal kernel, K/n = K/tr K. So
  [THEORY-233](../theory.d/THEORY-233.md)'s trace-normalized kernel is the empirical Σ̂ of Proposition 6
  when its kernel has unit diagonal. But [THEORY-233](../theory.d/THEORY-233.md)'s kernels are
  centred linear kernels of representations over a fixed stimulus set.
  They are neither unit-diagonal nor uncentred, so Bach's results do not
  transfer to them as stated.
- **The GNS link the seed asked about.** Bach does not draw it. The
  words GNS, C*-algebra and Gelfand do not occur in the text. The
  identity ⟨g, Σ_p f⟩ = E_p[fg] is in §2.2 as a definition, nothing
  more.
- **The Radon–Nikodym/KL strand.** The seed's description is right:
  kernel KL lower-bounds KL (Proposition 4(d)). The proof writes Σ_q as
  ∫(dq/dp)ϕϕ* dp, so the density ratio appears inside the bound.
- **Information-bottleneck readings.** §6's kernel MI lower-bounds
  Shannon MI and characterizes independence. It does not decompose into
  conditional entropies, so a chain rule that IB arguments use is not
  available.
- No instruction for machine-learning practice.

## Limitations

- **Upper bound only on KL.** The kernel quantities never exceed the
  Shannon ones. They approach them only as the bandwidth shrinks, at a
  rate shown for the torus and Lipschitz densities.
- **Estimation is not competitive** for Shannon entropy: n^{−2/(d+4)}
  against the optimal n^{−4/(d+4)}. Bach says his goal was not entropy
  estimation.
- **Kernel entropy depends on the base measure**, unlike the relative
  entropy, and is simple only on symmetric sets.
- **Tightness of the log-partition bounds** is left to future work. The
  experiments are one-dimensional or on independent hypercube
  distributions.
- **Typographical slips.** Eq. (13) prints D(Σ_q‖Σ_q) for D(Σ_p‖Σ_q).
  Proposition 9 says "X₁ and X₁ being independent". The proof of
  Proposition 10 prints log Σ_{p₁₂} − log Σ_{p₁₂}. None affects a
  result.

## Open questions

- Is there a kernel quantity that characterizes conditional independence
  and keeps the link to Shannon? Bach points to other covariance-operator
  tools (Fukumizu et al.), which lose the link.
- Does the O(σ²) gap hold beyond translation-invariant kernels on compact
  groups? Bach's leverage-score heuristic suggests it does, given a
  non-asymptotic version of Pauwels, Bach and Vert.
- Rényi versions are named in §8. They would bear on the
  fidelity-based similarity of [THEORY-233](../theory.d/THEORY-233.md), since fidelity is the
  sandwiched Rényi-½ quantity. Appendix A.4's f(t) = 1 − √t divergence
  is the Petz-type affinity 1 − tr(A^{1/2}B^{1/2}), not the Uhlmann
  fidelity, so the link is not yet exact.
