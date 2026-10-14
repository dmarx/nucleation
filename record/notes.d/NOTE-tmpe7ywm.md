---
status: Read
paper: LIT-261
title: 'Schölkopf, Herbrich & Smola — A Generalized Representer Theorem'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the author-hosted PDF of the published chapter
    (alex.smola.org/papers/2001/SchHerSmo01.pdf, Springer LNAI 2111 footer,
    pp. 416–426), text extracted with pdftotext: §1 (eqs. 1–12), §2
    (Theorem 1 and its proof, eqs. 13–24; Theorem 2, stated without
    proof; Remark 1; Examples 1–5, eqs. 27–31), §3 and the reference
    list. The proof of Theorem 1 was checked line by line. Supersedes the
    seeded skim NOTE-230.
date: '2026-10-14'
summary: >-
  For any nonempty set X, real positive-definite kernel k, strictly
  increasing g and any cost c on the training triples, even coupled,
  non-convex or infinite-valued, every minimizer of c + g(‖f‖) over the
  class F of countable kernel expansions with finite RKHS norm is a finite
  expansion Σ α_i k(·, x_i) at the training points. The proof uses only the
  reproducing property and Pythagoras. Existence of a minimizer, the
  extension from F to the completed RKHS, and the semiparametric
  Theorem 2 are not proved here.
---
<!-- inactive-ok-file: THEORY-009 THEORY-tmpiw6t1 — Proposed; the account that cites this paper, and the one filed from this reading, open -->
<!-- inactive-ok-file: NOTE-230 — Superseded; the seeded skim this reading replaces -->

# NOTE-tmpe7ywm: Schölkopf, Herbrich & Smola — A Generalized Representer Theorem

## Contribution

Wahba's representer theorem covered squared loss (or hard constraints) with
the regularizer λ‖f‖². This paper extends it to any strictly increasing
function of the RKHS norm and to any cost on the training triples,
including costs that couple the points and costs that take the value ∞.
It gives a three-line proof in the feature space of the kernel. After it,
the finite-dimensionality of a large class of kernel problems rests on one
geometric fact, not on the convexity of a particular objective.

## Key insight

The cost sees f only through its values f(x_1), …, f(x_m), and by the
reproducing property those values are inner products with k(·, x_i). So
the part of f orthogonal to span{k(·, x_i)} is invisible to the cost and
only adds to the norm. A strictly increasing penalty on the norm therefore
removes it. Nothing about the cost is used except that it depends on f
through those m values.

## Assumptions

- X is any nonempty set; no topology or measure is assumed.
- k is a real-valued positive-definite kernel (Definition 3: every Gram
  matrix satisfies Σ_i Σ_j c_i c̄_j K_ij ≥ 0; for real coefficients
  symmetry must be added).
- g: [0, ∞) → ℝ is **strictly** monotonically increasing.
- c: (X × ℝ²)^m → ℝ ∪ {∞} is arbitrary. Hard constraints enter as c = ∞.
- The minimization is over F = {f = Σ_{i=1}^∞ β_i k(·, z_i) : β_i ∈ ℝ,
  z_i ∈ X, ‖f‖ < ∞} (eq. 13), with ‖Σ β_i k(·, z_i)‖² = Σ_i Σ_j β_i β_j
  k(z_i, z_j) (eq. 14). This is a class of countable expansions, not
  stated to be the completed space H_k.
- A minimizer is assumed to exist. The theorem says what any minimizer
  looks like; it does not say one exists.

## Key results

- **The RKHS from the kernel (§1.2, eqs. 7–12).** φ(x) = k(·, x).
  Finite combinations get ⟨f, g⟩ := Σ ᾱ_i β_j k(x_i, x′_j) (eq. 9),
  well defined because ⟨f, g⟩ = Σ_j β_j f(x′_j). Then ⟨k(·, x), f⟩ = f(x)
  (eq. 11), "i.e., k is the representer of evaluation", holds by
  construction. Cauchy–Schwarz for the kernel (eq. 6) gives
  |f(x)|² ≤ k(x, x)·⟨f, f⟩ (eq. 12), so ⟨f, f⟩ = 0 forces f = 0.
  Completion gives H_k. The Riesz representation theorem is not invoked.
- **Theorem 1 (Nonparametric Representer Theorem, eqs. 13–16).** Any
  f ∈ F minimizing c((x_1, y_1, f(x_1)), …, (x_m, y_m, f(x_m))) + g(‖f‖)
  admits f(·) = Σ_{i=1}^m α_i k(·, x_i). *Holds when:* the assumptions
  above; no convexity of c or g.
- **Proof (eqs. 18–24).** Write f = Σ α_i φ(x_i) + v with ⟨v, φ(x_j)⟩ = 0
  for all j (eqs. 20–21). By eq. 19, f(x_j) = ⟨Σ α_i φ(x_i), φ(x_j)⟩,
  independent of v (eq. 22). By orthogonality,
  g(‖f‖) = g(√(‖Σ α_i φ(x_i)‖² + ‖v‖²)) ≥ g(‖Σ α_i φ(x_i)‖), with
  equality iff v = 0 (eq. 23). So any minimizer has v = 0. Checked: the
  step needs v ∈ F, which holds because v is f minus a finite expansion,
  and it needs only strict monotonicity of g.
- **Remarks on the hypotheses (p. 420).** Monotonicity of g "is necessary
  to ensure that the theorem holds" (asserted, no counterexample given).
  Without strictness, each minimizer need not have the form, but "there is
  always another solution minimizing (15) that does admit the expansion".
  Convexity of c and g would be needed only to rule out multiple local
  minima.
- **Theorem 2 (Semiparametric, eqs. 25–26), stated without proof.** Add
  an unregularized part h ∈ span{ψ_p}_{p=1}^M with the m × M matrix
  (ψ_p(x_i)) of rank M. Then a minimizer of c(…f̃(x_i)…) + g(‖f‖) has
  f̃ = Σ α_i k(x_i, ·) + Σ β_p ψ_p, "with unique coefficients β_p".
- **Remark 1 (biased regularization).** Adding −⟨f_0, f⟩ adds a multiple
  of f_0 to the expansion; with g = ½‖f‖² it is ½‖f − f_0‖².
- **Examples.** SV regression (ε-insensitive loss, eq. 27) and SV
  classification (hinge, eq. 28) with g = ‖f‖² and offset ψ_1 = b; a
  strictly monotone bound-derived regularizer (eq. 29), reduced to the
  m-dimensional problem (eq. 30); MAP estimation, with g = λ‖f‖² a
  Gaussian-process prior and g = λ‖f‖ a "Laplacian prior"; kernel PCA as
  c = 0 if the empirical variance (1/m)Σ(f(x_i) − (1/m)Σ f(x_j))² = 1 and
  ∞ otherwise (eq. 31).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Every minimizer over F of an arbitrary output cost plus a strictly increasing function of the norm is a kernel expansion on the training points | strong | Theorem 1, proof eqs. 18–24, checked |
| C2 | The proof needs the reproducing property and orthogonal decomposition, not convexity and not Riesz | strong | proof eqs. 18–24; §1.2 builds the RKHS from k |
| C3 | With non-strict monotonicity some minimizer still has the form | moderate | asserted p. 420; follows from the same proof, not written out |
| C4 | The semiparametric extension holds with unique β_p | weak | Theorem 2, stated without proof |
| C5 | Monotonicity of g is necessary | weak | asserted p. 420, no counterexample |

## Concepts

- **Representer of evaluation.** The function k(·, x), whose inner product
  with f gives f(x) (eq. 11). Here a property of the construction.
- **Positive-definite kernel.** Every Gram matrix is positive
  semidefinite (Definitions 2–3); the paper's "definite" is the matrix
  theorist's "semidefinite" (fn. 2).
- **SV expansion.** The SV community's name for the form (16).

## Connections

It generalizes Kimeldorf and Wahba (1971, squared loss and λ‖f‖²) and Cox
and O'Sullivan (1990, non-quadratic but uncoupled costs). The feature map
and the construction of H_k follow Berg, Christensen and Ressel (1984).
Example 5 cites the authors' kernel PCA (1999). The skim ([NOTE-230](NOTE-230.md))
proposed Example 5 as a bridge to the spectral self-supervised results
([LIT-242](../literature.d/LIT-242.md), [LIT-258](../literature.d/LIT-258.md)). The paper itself draws no such link, and the
constraint in eq. 31 picks one unit-variance functional, so it does not by
itself give the top-d eigenspace those results need.

## Bearing on the record

- **[THEORY-009](../theory.d/THEORY-009.md)** cites "Schölkopf, Herbrich & Smola's proof (eqs. 18–24)"
  as using "the reproducing property and orthogonal projection, not
  Riesz". That is what the paper does. The word "Riesz" does not occur in
  it. The RKHS is built from k (§1.2), so the representer property is
  definitional, which is the stronger form of [THEORY-009](../theory.d/THEORY-009.md)'s point.
- **[LIT-261](../literature.d/LIT-261.md)'s summary** says "every RKHS minimizer". The theorem is stated
  for minimizers over F, the countable expansions of finite norm (eq. 13),
  and the paper does not show F = H_k. The summary should say "every
  minimizer over the class of kernel expansions of finite norm".
- **[THEORY-tmpiw6t1](../theory.d/THEORY-tmpiw6t1.md)** is filed from this reading.
- No instruction for machine-learning practice is drawn; the examples are
  existing algorithms recast, not advice. Nothing for the anthology.

## Limitations

- Existence of a minimizer is assumed, not shown.
- F is not proved to be the completed H_k. Each f ∈ H_k is a limit of
  finite expansions and can be written as a countable sum of them, but
  whether the double series (14) then converges to ‖f‖² for every such
  representation is not addressed.
- Theorem 2 and the necessity of monotonicity are asserted without proof.
- The paper does not treat costs that depend on f other than through
  point values (derivatives, integrals), where the theorem need not hold.

## Open questions

- A statement over the full H_k, with the existence condition (lower
  semicontinuity and coercivity of c + g) made explicit. A textbook proof
  of the general form would close it.
- Whether a cost that depends on f through any finite set of bounded
  linear functionals (not only evaluations) gives the analogous expansion
  in their representers. That would need Riesz, which this proof avoids.
