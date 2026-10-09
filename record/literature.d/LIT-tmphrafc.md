---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmp23s9u](../notes.d/NOTE-tmp23s9u.md)); worth reading as the reference account of Markov categories and of how much probability and statistics follows from copying, discarding and composing kernels: determinism, four notions of conditional independence with the semigraphoid rules (weak union only with conditionals), almost-sure equality, and sufficiency, completeness and ancillarity. Basu''s theorem holds in every Markov category, and Fisher–Neyman and Bahadur under strict positivity, which Stoch has without conditionals. The abstract Fisher–Neyman is matched to the classical theorem only for finite sets.'
title: 'A synthetic approach to Markov kernels, conditional independence and theorems on sufficient statistics'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from arXiv v8 (31 May 2020, 98 pages): Sections 1, 2, 4, 6, the
    first half of 10, and 11–16 closely; Sections 3, 5, 7–9 and the
    strictification half of 10 skimmed (NOTE-tmp23s9u). Details checked
    against arXiv (v1 submitted 19 August 2019; v8 current) and Crossref
    (Adv. Math. 370, article 107239, August 2020). `published:` is the arXiv v1 date. Not
    held in the Anthology of the SOTA: a grep of its record/ (clone of
    2026-10-09, commit 1cffe8f) for the authors, the identifier and the
    title found nothing.
tags:
- mathematics
- probabilistic-modeling
date: '2026-10-09'
published: '2019-08-19'
arxiv: '1908.07021'
doi: '10.1016/j.aim.2020.107239'
first_author: 'Fritz'
keywords:
- 'Markov categories'
- 'synthetic probability'
- 'conditional independence'
- 'sufficient statistics'
- 'category theory'
- 'Fisher–Neyman'
- 'Basu'
- 'Bahadur'
implementations: []
summary: >-
  Fritz (2020), Adv. Math. 370:107239. Markov categories as a framework
  for synthetic probability and statistics: conditioning, conditional
  independence, almost-sure equality and sufficient statistics stated in
  categorical terms, with the Fisher–Neyman, Basu and Bahadur theorems
  proved there. Basu needs no extra axiom; Fisher–Neyman and Bahadur need
  strict positivity, not conditionals. Fisher–Neyman is matched to the
  classical theorem only in FinStoch.
---

<!-- inactive-ok-file: THEORY-tmpm1g8e — Proposed; filed from this reading, which is its source -->

# LIT-tmphrafc: A synthetic approach to Markov kernels, conditional independence and theorems on sufficient statistics

Tobias Fritz (2020), *Advances in Mathematics* 370:107239 —
[ARXIV-1908.07021](https://arxiv.org/abs/1908.07021)

## Key takeaways

- **The definition** (Definition 2.1). A Markov category is a symmetric
  monoidal category with a commutative copy/discard comonoid on every
  object, compatible with ⊗, and with discard natural, so the unit is
  terminal. Copy is deliberately not natural. The morphisms for which it is
  are the *deterministic* ones (Definition 10.1). Examples: FinStoch,
  Stoch, BorelStoch, Gauss (affine maps plus Gaussian noise), the Radon
  Kleisli category, and stochastic processes as diagram categories
  (Section 7).
- **Optional axioms** (Section 11): conditionals, randomness pushback,
  positivity and causality. FinStoch, BorelStoch and Gauss have
  conditionals. Stoch does not, but is positive, strictly positive and
  causal. Conditionals are unique only in a meet-semilattice (Proposition
  11.15), and unique a.s. in general (Proposition 13.7).
- **Conditional independence without conditionals** (Section 12). The
  paper has four notions: conditioning on an output, on an input, on both,
  and the Markov-chain form A ⊥⊥ Y | X. Symmetry, decomposition and
  contraction hold everywhere; weak union is proved only with conditionals.
  With conditionals, Dawid–Studený conditional products exist and are
  unique (Proposition 12.9).
- **Almost surely** (Section 13). Probability spaces and kernels modulo
  a.s. equality form a symmetric monoidal category (Proposition 13.9).
  With conditionals, Bayesian inversion is a dagger functor on it (Remark
  13.10).
- **Statistics** (Sections 14–16). A statistic is a deterministic
  morphism. Sufficiency means the sample can be regenerated from the
  statistic independently of θ. Completeness is a property of the kernel
  sp; in Stoch it is bounded completeness. Basu (Theorem 15.8) holds in
  every Markov category. Fisher–Neyman (14.5) and Bahadur (16.3) need
  strict positivity. Fisher–Neyman is shown to be the classical
  factorisation in FinStoch only.
- **Signed probabilities** (Example 11.27). FinStoch± satisfies the
  Markov axioms but is not positive and has no conditionals.

## Standing in the record

Filed on 2026-10-09 at the owner's request, as one of the works in the
reference list of the owner's working manuscript (October 2026) that the
record did not yet hold. See the curation entry of that day.

Read the same day ([NOTE-tmp23s9u](../notes.d/NOTE-tmp23s9u.md)). Its result on which axioms the
sufficiency theorems use is filed as [THEORY-tmpm1g8e](../theory.d/THEORY-tmpm1g8e.md). Within the record,
Fritz's earlier convex spaces enter the reading of [LIT-038](LIT-038.md) ([NOTE-050](../notes.d/NOTE-050.md)), and
Baez–Fritz–Leinster's entropy characterisation is cited in [NOTE-088](../notes.d/NOTE-088.md). Its
example of signed kernels (FinStoch±) shows where negativity enters,
against [THEORY-012](../theory.d/THEORY-012.md)'s finding that signed global sections always exist.
The paper does not draw that connection; it is mine. Baez and Fong's
Noether theorem for Markov processes ([LIT-tmpj84ja](LIT-tmpj84ja.md)), filed with it, works
with the same kernels as operators and declares no relation.
