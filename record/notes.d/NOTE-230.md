---
number: 230
status: Skimmed
formerly:
- NOTE-tmpprjax
paper: LIT-261
title: 'A Generalized Representer Theorem'
version: 1
date: '2026-09-26'
summary: >-
  For any strictly increasing regularizer g(‖f‖) and any (even non-convex, coupled) cost on the training outputs, every RKHS minimizer of c((x_i,y_i,f(x_i))_i) + g(‖f‖) is a finite kernel expansion f = Σ α_i k(·,x_i). The proof needs only the reproducing property and orthogonal decomposition onto span{k(·,x_i)}, not the Riesz theorem.
---
<!-- inactive-ok-file: LIT-261 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-230: A Generalized Representer Theorem

## Contribution

Wahba's representer theorem says that solutions of certain regularized empirical risk problems with a quadratic regularizer are expansions in kernel functions centred on the training points. The authors generalize it to a larger class of regularizers and risk terms and give a short self-contained proof in the feature space of the kernel. The result shows that many learning problems posed in possibly infinite-dimensional RKHSs have optimal solutions in the finite-dimensional span of the mapped training data, which is what makes kernel algorithms computable.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1.2, eqs. 7–12: the RKHS is built directly from a positive-definite kernel (the Moore–Aronszajn construction). The pre-Hilbert space is spanned by the k(·,x), with ⟨f,g⟩ := Σᾱ_iβ_jk(x_i,x′_j). Eq. 11, ⟨k(·,x), f⟩ = f(x), "i.e., k is the representer of evaluation", holds by construction, and eq. 12 bounds |f(x)|² ≤ k(x,x)⟨f,f⟩ before completion. Riesz is not invoked, because the kernel is given and the space is built from it.
- Thm 1 (Nonparametric Representer Theorem, eqs. 13–16): X is any nonempty set, g is strictly monotone on [0,∞), and c is arbitrary (hard constraints are allowed via c = ∞). Any minimizer admits f = Σ_{i=1}^m α_i k(·,x_i).
- Proof, eqs. 18–24: split f = Σα_iφ(x_i) + v with v ⊥ every φ(x_j). The reproducing property makes f(x_j) independent of v, and Pythagoras makes g(‖f‖) strictly larger unless v = 0.
- Thm 2 adds an unregularized parametric part (semiparametric version). Remark 1 covers biased regularization toward f₀. Examples cover SV regression and classification, bound-minimizing regularizers, MAP under a GP prior, and kernel PCA (Example 5: unit-empirical-variance "linear feature extraction functionals").
- §3: solutions "live in a specific subspace whose dimensionality equals at most the number of training examples".

## Open questions

- It corrects a natural overstatement: the representer theorem rests on the reproducing property plus orthogonal projection. Riesz is what runs the other direction, from a Hilbert space with bounded evaluations to a kernel (ra4, Prop. 2.1). The chain "Riesz → RKHS → representer theorem" is right only if the RKHS is given abstractly rather than built from k.
- Example 5 (kernel PCA) is the bridge to SSL. Johnson et al. (ra2) and [LIT-242](../literature.d/LIT-242.md) both land on kernel PCA, and [LIT-242](../literature.d/LIT-242.md)'s Prop. 5.1(c) characterizes the SSL solution as a minimum-RKHS-norm interpolant with a finite kernel expansion, i.e. representer-theorem-shaped.
- Note that the class F in Thm 1 is the set of countable kernel expansions with finite norm, not stated as the full completed RKHS. A deeper read (or a textbook) should confirm the extension to the full H_k.
