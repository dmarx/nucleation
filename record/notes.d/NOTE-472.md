---
number: 472
status: Read
formerly:
- NOTE-tmp2k5h4
paper: 'LIT-607'
title: 'Natural Gradient Works Efficiently in Learning'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the published PDF deposited by Amari's laboratory in
    RIKEN's database (26 pages, text layer extracted). Sections 1–9 read;
    the proofs of Theorems 1–4 and 6 followed; Theorem 7 (systems space) is
    stated without proof in the paper. Results Amari takes from his earlier
    work (Amari 1967, 1985, 1987; Yang & Amari 1997) are taken as he
    reports them.
date: '2026-10-03'
summary: >-
  Natural gradient ∇̃L = G⁻¹∇L is steepest descent under metric G (Theorem
  1); for a statistical model G is the Fisher information. Online learning
  w_{t+1} = w_t − (1/t)∇̃l is Fisher efficient, Ṽ_t = G⁻¹/t + O(1/t²)
  (Theorem 2). Explicit G and G⁻¹ for a perceptron (Theorems 3–4) and the
  natural gradient ∇L·WᵀW on the matrix group (Theorem 6). The plateau
  claim for multilayer perceptrons is a conjecture resting on Yang & Amari
  (1997).
---

<!-- inactive-ok-file: LIT-349 — Deferred: Rao 1945 is unread; named as the cited source of the Fisher metric, with no relation claimed -->
<!-- inactive-ok-file: LIT-354 — Deferred: Watanabe's book is unread; named for the singular-model caveat, with no relation claimed -->

# NOTE-472: Natural Gradient Works Efficiently in Learning

## Contribution

It makes the natural gradient a general learning rule. Before it, Amari had
used Riemannian gradients for Boltzmann machines and blind separation. This
paper states the rule for any parameter space with a metric, proves that with
the Fisher metric and a 1/t schedule online learning is as efficient as
optimal batch estimation, and derives the metric explicitly for perceptrons,
for nonsingular matrices and for linear systems. It is the extended journal
version of Amari's NIPS 9 paper (1996).

## Key insight

The ordinary gradient depends on how a model is parameterized; the direction
that most improves the loss for a given change in the *model* does not. When
the parameter space is a family of probability distributions, the natural way
to measure a change is the Fisher information, and preconditioning the
gradient by its inverse gives an update whose online version reaches the
Cramér–Rao bound.

## Assumptions

- **A Riemannian metric** G(w) on the parameter space, positive definite, so
  that G⁻¹ exists (Section 2).
- **Statistical setting** for the efficiency result: i.i.d. examples from a
  realizable teacher, q(y | x) = p(y | x, w*), log loss
  l = −log p(x, y; w) (Section 4).
- **Convergence of w̃ₜ to w*** by stochastic approximation, so that
  G(w̃ₜ) = G(w*) + O(1/t), and a differentiable loss. For a
  nondifferentiable loss online learning is worse than batch by a factor of
  2 (Section 1).
- **Gaussian inputs** x ~ N(0, I) and output noise N(0, σ²) for the
  explicit perceptron metric (Section 6).
- **Semiparametric exception**: in blind separation and deconvolution the
  source densities are unknown, the Cramér–Rao bound need not hold, and
  Theorem 2 does not apply unless the true densities are used (Remark,
  Section 4).

## Key results

- **Theorem 1.** Under |dw|² = ε², the steepest descent direction of L is
  −G⁻¹(w)∇L(w), the natural (contravariant) gradient.
- **Fisher metric** gᵢⱼ(w) = E[∂ᵢ log p · ∂ⱼ log p] (Eq. 3.5), "the only
  invariant metric" on a statistical model (citing Chentsov 1972). The same
  definition for a multilayer network with Gaussian output noise is Eq. 3.11.
- **Theorem 2.** With w̃ₜ₊₁ = w̃ₜ − (1/t)∇̃l, the error covariance obeys
  Ṽₜ₊₁ = Ṽₜ − (2/t)Ṽₜ + G⁻¹/t² + O(1/t³), so Ṽₜ = G⁻¹/t + O(1/t²): Fisher
  efficient. For an unrealizable teacher, use K(w) = E[∂²l] instead
  (Eq. 4.9), locally Newton–Raphson.
- **Adaptive learning rate (Eqs. 5.1–5.2)**: ηₜ₊₁ = ηₜ exp{α[β l − ηₜ]}. In
  the averaged continuous-time analysis eₜ = a/t and ηₜ = b/t, with b = 1/2
  and a = (1/β)(1/2 − 1/α), requiring α > 2: the optimal 1/t rate for the
  generalization error. Amari notes the basin of attraction of (0, 0) has a
  fractal boundary.
- **Theorems 3–4.** For y = f(w·x) + n with f(u) = (1 − e⁻ᵘ)/(1 + e⁻ᵘ),
  G(w) = w²c₁(w)I + {c₂(w) − c₁(w)}wwᵀ, with c₁, c₂ one-dimensional
  integrals, and G⁻¹ is explicit, giving the update Eq. 6.7.
- **Theorem 5.** The Jeffreys prior √|G(w)| and the volume of the
  perceptron manifold are explicit; the manifold has finite volume.
- **Multilayer perceptron (Eq. 6.13).** The Fisher matrix splits into
  m + 1 blocks; each off-diagonal block has the form
  cᵢⱼI + dᵢᵢwᵢwᵢᵀ + dᵢⱼwᵢwⱼᵀ + dⱼᵢwⱼwᵢᵀ + dⱼⱼwⱼwⱼᵀ, so inversion reduces
  to a 2(m + 1)-dimensional problem rather than (n + 1)m.
- **Theorem 6.** With the right-invariant metric on Gl(m), the natural
  gradient is ∇L·WᵀW, and the blind-separation rule becomes
  dW/dt = ηₜ(I − φ(y)yᵀ)W (Eq. 7.11).
- **Theorem 7.** In the manifold of linear systems ∇̃l = ∇l(z)Wᵀ(z⁻¹)W(z);
  the result is neither FIR nor causal, so a delay is needed for an online
  algorithm. Proof omitted.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The natural gradient G⁻¹∇L is the steepest descent direction in a Riemannian space | strong (derivation) | Theorem 1 |
| C2 | Online natural gradient learning with step 1/t is Fisher efficient in the realizable, regular case | strong for the stated assumptions; asymptotic expansion, not a finite-sample bound | Theorem 2, Eqs. 4.5–4.8 |
| C3 | The proposed adaptive learning rate converges at the optimal 1/t rate | moderate: averaged, continuous-time analysis near w* | Eqs. 5.3–5.11 |
| C4 | The Fisher metric and its inverse for a simple perceptron have closed forms | strong (derivation) | Theorems 3–4 |
| C5 | The natural gradient on Gl(m) is ∇L·WᵀW | strong (derivation) | Theorem 6 |
| C6 | Natural gradient learning may avoid or soften the plateaus of backpropagation | weak: a conjecture resting on a preliminary simulation in Yang & Amari (1997), not shown here | Sections 1, 6, 9 |

## Concepts

- **natural gradient**: G⁻¹∇L, the contravariant form of the gradient.
- **Fisher efficient**: an estimator whose covariance attains G⁻¹/T
  asymptotically.
- **nonholonomic basis**: the basis dX = dW·W⁻¹ of the tangent space of
  Gl(m), locally defined but not the differential of any coordinate map.
- **plateau**: a long stretch of slow progress in backpropagation learning
  of multilayer perceptrons.

## Connections

- **Rao (1945) and Chentsov (1972)** are the cited sources of the Fisher
  metric and its uniqueness. The record holds Rao only as an unread seed
  ([LIT-349](../literature.d/LIT-349.md)).
- **Martens & Grosse (2015, [LIT-622](../literature.d/LIT-622.md))** build their K-FAC approximation on this
  definition, F⁻¹∇h, and add what this paper does not have for deep
  networks: a way to invert the Fisher at scale.
- **Amari (1967)** is the source of the general preconditioned stochastic
  gradient form wₜ₊₁ = wₜ − ηₜC(wₜ)∇l (Eq. 3.2); the natural gradient is the
  choice C = G⁻¹.

## Bearing on the record

- It is the root of the `information-geometry` half of the owner's line
  ([ADR-026](../decisions.d/ADR-026.md)). A THEORY candidate built on it would say: steepest descent is
  metric-dependent, and on a statistical model the Fisher metric is the
  canonical choice. That is a definition plus a uniqueness theorem it cites
  rather than proves, so it would need Chentsov or Amari's 1985 book as
  evidence too.
- **The singular caveat.** Theorem 2 requires G(w*) invertible. For
  multilayer networks the w-blocks of Eq. 6.13 scale with vᵢ², so G loses
  rank at vᵢ = 0; this is my reading, not the paper's. Watanabe ([LIT-354](../literature.d/LIT-354.md))
  makes degeneracy the general case for neural networks. The record should
  not cite this paper for efficiency of natural gradient learning in deep
  networks without that caveat.
- It carries an instruction for practice (precondition by the inverse
  Fisher), hence the `anthology-candidate` flag.

## Limitations

- Efficiency is asymptotic and local; nothing is said about the transient
  "exploration" phase where K-FAC later found damping to be essential.
- The multilayer perceptron metric is written down but not inverted in
  general; the paper itself says inversion "is not easy except for simple
  cases".
- No experiment is reported in this paper. The plateau claim rests on
  Yang & Amari (1997).
- Eq. 3.11 prints ∂p(x, y; w)/∂wⱼ in the second factor where Eq. 3.5 has
  ∂ log p; read as a typo for the log.

## Open questions

- What replaces the Cramér–Rao bound, and the efficiency claim, at singular
  points where G is degenerate? Singular learning theory's answer is in
  terms of the real log canonical threshold.
- How to invert or approximate G for large multilayer networks: the problem
  K-FAC and Shampoo take up.

## Corrections

- none (there was no seed)
- **Typo in the paper**: Eq. 3.11, as noted under Limitations.
