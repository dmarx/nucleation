---
status: Active
status_note: 'read 2026-10-14 ([NOTE-tmppltl7](../notes.d/NOTE-tmppltl7.md)) in full; worth reading as the short proof that the restricted isometry property follows from the concentration inequality used in Johnson–Lindenstrauss proofs, by a union bound over nets on the sparse supports. Read it knowing that it proves sufficiency only, with constants left implicit; that the optimality of k ≲ n/(log(N/n) + 1) it cites from Gelfand widths, not from concentration; that its constants are Achlioptas''s; and that the route "through" the JL lemma in §6 is sketched, not written out.'
title: 'A Simple Proof of the Restricted Isometry Property for Random Matrices'
version: 2
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Filed, not read, at the owner's request after a survey found the record
    meets random projections from three directions without holding the
    result they share. Citation checked against Crossref on 2026-10-14. Not held in the Anthology of the SOTA: a grep of its record/ (clone at commit d1573d2) for the title, the identifier and the result's name found nothing.
- version: 2
  date: '2026-10-14'
  note: >-
    Read in full (NOTE-tmppltl7) from the author-posted copy on Mark
    Davenport's Georgia Tech page, mdav.ece.gatech.edu/publications/bddw-ca-2008.pdf,
    the 11-page Constructive Approximation version with the DOI header:
    §§1–6 and the references. The standard-statement takeaways are
    replaced with the reading, the summary is rewritten from it, the
    status moved from Deferred to Active, keywords from the paper's own
    terms are added, and Standing in the record is corrected on the
    source of the concentration and on what the paper shares with the
    superposition bound. The copy prints the DOI and "© 2008" but no
    volume, issue, pages or online date, so 28(3): 253–263 and the
    published date are kept from Crossref, unconfirmed by the copy and
    not contradicted by it.
tags:
- mathematics
date: '2026-10-14'
published: '2008-01-15'
doi: '10.1007/s00365-007-9003-x'
first_author: 'Baraniuk'
keywords:
- 'restricted isometry property'
- 'compressed sensing'
- 'Johnson-Lindenstrauss lemma'
- 'random matrices'
- 'concentration of measure'
- 'concentration inequalities'
- 'covering numbers'
- 'n-widths'
- 'Gelfand widths'
- 'universality'
extends:
- LIT-tmp7skui
implementations: []
summary: >-
  Baraniuk, Davenport, DeVore & Wakin (2008), *Constructive Approximation* 28(3): 253–263. If an n × N random matrix satisfies the concentration inequality of Johnson–Lindenstrauss proofs, Pr(|‖Φx‖² − ‖x‖²| ≥ ε‖x‖²) ≤ 2e^{−n c₀(ε)}, then a union bound over a (12/δ)^k-point net on each of the (eN/k)^k coordinate k-subspaces, with a bootstrapping step from net to subspace, gives the restricted isometry property for all k ≤ c₁n/log(N/k) with probability at least 1 − 2e^{−c₂n} (Theorem 5.2). Gaussian, ±1 and Achlioptas's sparse ensembles qualify, also in any fixed orthonormal basis. That this range is the widest possible the paper takes from Gelfand widths.
---

# LIT-tmpcfdvm: A Simple Proof of the Restricted Isometry Property for Random Matrices

Richard Baraniuk, Mark Davenport, Ronald DeVore and Michael Wakin (2008), "A Simple Proof of the Restricted Isometry Property for Random Matrices", *Constructive Approximation* 28(3): 253–263 — [doi:10.1007/s00365-007-9003-x](https://doi.org/10.1007/s00365-007-9003-x)

## Key takeaways

*From the reading, [NOTE-tmppltl7](../notes.d/NOTE-tmppltl7.md).*

- **The one assumption (4.3).** For every fixed x,
  Pr(|‖Φx‖²_{ℓ₂ⁿ} − ‖x‖²_{ℓ₂ᴺ}| ≥ ε‖x‖²_{ℓ₂ᴺ}) ≤ 2e^{−n c₀(ε)}, 0 < ε < 1.
  Φ is n × N: n measurements, ambient dimension N.
- **Ensembles (§4).** Gaussian N(0, 1/n), ±1/√n, and the sparse
  ±√(3/n) with probability 1/6 each and 0 with probability 2/3 all satisfy
  (4.3) with c₀(ε) = ε²/4 − ε³/6, which the paper attributes to
  Achlioptas ([LIT-tmppzjx6](LIT-tmppzjx6.md)).
- **One support (Lemma 5.1).** For #T = k and 0 < δ < 1,
  (1 − δ)‖x‖ ≤ ‖Φx‖ ≤ (1 + δ)‖x‖ on all of X_T with probability
  ≥ 1 − 2(12/δ)^k e^{−c₀(δ/2)n}. A δ/4-net of at most (12/δ)^k points
  takes (4.3) at ε = δ/2, and a least-constant bootstrap extends it from
  the net to the subspace.
- **All supports (Theorem 5.2).** A union bound over C(N, k) ≤ (eN/k)^k
  supports gives failure probability ≤ 2e^{−c₀(δ/2)n + k[log(eN/k) +
  log(12/δ)]}. So the RIP holds with the prescribed δ for every
  k ≤ c₁n/log(N/k), with probability ≥ 1 − 2e^{−c₂n}, where
  c₂ ≤ c₀(δ/2) − c₁[1 + (1 + log(12/δ))/log(N/k)]. The family counted is
  supports times net points, not supports alone.
- **Optimality is cited, not proved.** The range k ≤ C₃n/(log(N/n) + 1) is
  the widest possible by the Garnaev–Gluskin lower bound on the Gelfand
  width of the ℓ₁ ball (2.3) and Candès–Tao's error bound (3.9).
- **JL implies RIP (§6).** Applying the JL lemma to Q_T with the origin
  added gives "a similar result with only slightly worse constants", so a
  distribution that gives JL embeddings gives RIP matrices. The paper does
  not claim the converse.
- **Universality (§6).** The same proof gives the RIP for Φ(ω)Ψ for any
  fixed orthonormal Ψ; new for the ±1 and sparse ensembles, the authors
  say.
- **Scope.** Sufficiency only, with c₁ and c₂ left implicit. Theorem 5.2's
  RIP is in squared norms while Lemma 5.1 is in unsquared ones, so the
  squared constant is about 2δ (an observation in the NOTE, not the
  paper's).

## Standing in the record

Filed on 2026-10-14 for [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md) as the bridge between two of
its threads, and read the same day in [NOTE-tmppltl7](../notes.d/NOTE-tmppltl7.md). The
compressed-sensing bound that Toy Models of Superposition proves in its
appendix ([NOTE-278](../notes.d/NOTE-278.md)) assumes the restricted isometry property. This paper
derives that property from the concentration inequality of the simplified
Johnson–Lindenstrauss proofs, with Achlioptas's constants
([LIT-tmppzjx6](LIT-tmppzjx6.md)). It cites the lemma itself to Johnson and Lindenstrauss
([LIT-tmp7skui](LIT-tmp7skui.md)) and Dasgupta and Gupta ([LIT-tmpjy3gf](LIT-tmpjy3gf.md)) only in a list.

The registration said "if this proof is right, the superposition bound and
the lemma share their mechanism". The proof is right. The conclusion does
not follow. The superposition bound is a lower bound, m = Ω(k log(n/k)),
with RIP as its hypothesis. This paper shows that random matrices meet the
hypothesis once n is of order k log(N/k). What makes k log(N/k) necessary
it takes from Gelfand widths, not from concentration. So for the question,
the sufficient side has the proposed shape, the log of a family's size over
a squared tolerance, and the necessary side is still open.
