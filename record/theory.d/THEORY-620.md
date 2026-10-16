---
number: 620
status: Active
formerly:
- THEORY-tmpqxzxm
title: "Walsh's 1923 functions are a closed orthonormal set on (0, 1) of ±1-valued step functions, each a parity of finitely many binary digits, whose expansions behave like Fourier series: grouped uniform convergence for continuous functions, convergence under bounded variation, localisation, Cesàro summability, and divergence at any chosen point for some continuous function"
version: 1
tags:
- mathematics
date: '2026-10-16'
source:
- LIT-300
summary: >-
  Walsh (1923), [LIT-300](../literature.d/LIT-300.md), read in full in [NOTE-281](../notes.d/NOTE-281.md), with the explicit
  formula and the Lebesgue-constant recurrence checked for small n.
  Closure is inherited from Haar's system, to which Walsh's is related by
  an orthogonal change of basis within each dyadic level. Theorems II–X
  give the Fourier-like convergence theory. The paper never mentions
  groups or characters: that these functions are the characters of the
  Cantor group, and of the Boolean cube on n digits, is a later
  identification.
---

<!-- inactive-ok-file: THEORY-019 — Proposed; named in Connections, not leaned on -->

# THEORY-620: Walsh's 1923 functions are a closed orthonormal set on (0, 1) of ±1-valued step functions, each a parity of finitely many binary digits, whose expansions behave like Fourier series: grouped uniform convergence for continuous functions, convergence under bounded variation, localisation, Cesàro summability, and divergence at any chosen point for some continuous function

## Source

Walsh (1923), "A closed set of normal orthogonal functions", *American
Journal of Mathematics* 45(1):5–24, [LIT-300](../literature.d/LIT-300.md), read in full in [NOTE-281](../notes.d/NOTE-281.md).

## What was actually shown

**The system (§2, formulas 2–4).** φ₀ ≡ 1, and each φ_{n+1} is built from φ_n
on the two halves of (0, 1) by rescaling and a sign. In binary x = Σ a_i/2^i
each function is (−1) raised to a sum of digits, for example
φ₂^(1) = (−1)^{a₁+a₂}. The nth has n sign changes, and each takes only ±1
except at finitely many points, where it takes the average of the one-sided
limits.

**Closure.** Each Haar function is a finite combination of Walsh functions
in the same dyadic level, and conversely. Haar's set is closed, so Walsh's
is (§2): no non-null integrable function is orthogonal to all of them.

**Convergence (Thms II–VIII).**
- For continuous F, the series converges uniformly when grouped in dyadic
  blocks of 2^{n−1} terms (Thm II), because the block sums equal Haar's.
- For F of bounded variation, the ungrouped series converges at every point
  of continuity and every dyadic rational (Thm IV).
- Convergence at a point depends only on F near it (Thm V).
- For continuous F on the closed interval, the series is uniformly Cesàro
  summable (Thm VII); the dyadic-rational case of the pointwise statement is
  omitted.
- For any point there is a continuous function whose expansion diverges
  there (Thm VIII), by Haar's criterion on unbounded Lebesgue constants.
- Any uniformly bounded orthonormal set obeys Riemann–Lebesgue, and Haar's
  set, being unbounded, fails it (Thm VI).

**Uniqueness (Thms IX–X).** A series converging to 0 uniformly off finitely
many points has all coefficients 0.

**What could have come out otherwise.** A ±1 system could have shared Haar's
pathologies, such as the failure of Riemann–Lebesgue. Being uniformly
bounded and global, it shares instead the behaviour of the trigonometric
system, including its divergence phenomena.

## What this does not say

- **That the Walsh functions are group characters.** The paper never
  mentions groups, characters or (ℤ/2)ⁿ, never states that a product of two
  Walsh functions is a Walsh function, and does not mention Rademacher
  ([NOTE-281](../notes.d/NOTE-281.md), corrections). That they are the characters of the compact group
  (ℤ/2)^ℕ is a later identification, an instance of [THEORY-645](THEORY-645.md). For the
  character view of the Boolean cube, cite [LIT-346](../literature.d/LIT-346.md).
- **The Paley or Hadamard ordering.** The order is by number of sign changes.
- **A discrete or multidimensional version.** The paper works on the interval
  only.
- **Anything about predicates or Boolean functions.** The owner's map row 7,
  "predicate harmonics", needs the character theory, which this paper does
  not supply.

## Connections

- [THEORY-019](THEORY-019.md) uses Walsh characters as an example of pieces inside a
  multiplet. [THEORY-645](THEORY-645.md) is the duality theorem of which their
  completeness is a case.
