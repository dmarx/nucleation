---
status: Read
paper: 'LIT-tmpjk0t0'
title: 'A comonadic view of simulation and quantum resources'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF (1904.10035v1, the only version, 12
    pages, two-column, text layer extracted): §§I–V, Table II, equations
    (1)–(28), every proposition and theorem, and the reference list.
    Followed: the proofs of Propositions 7 (the new case CF(e[x?y]) =
    CF(e)), 8 and 11, the co-Kleisli axioms of §IV-C, and Theorems 20–22.
    The soundness of the equational theory (Proposition 10) is stated as
    "a tedious but straightforward verification" and was not checked.
    The no-cloning proof was followed; one printed step is garbled in the
    text extract ("NCF(MP(e ⊗ x)) = NCF(e) > NCF(e)²"), but the argument it
    belongs to (Theorem 21 gives NCF(e) ≤ NCF(e)², impossible for
    0 < NCF(e) < 1) is sound. Cited works not read: Barrett and Pironio
    2005, Acín et al. 2015, Coecke, Fritz and Spekkens 2016.
date: '2026-10-09'
summary: >-
  Makes simulation between empirical models adaptive: measurement
  protocols form a comonoidal comonad MP, and a simulation of e by d is a
  deterministic map MP(d ⊗ c) → e with c non-contextual. Proves that
  such simulations are exactly the conversions by terms in the free
  operations of the resource theory of contextuality, which now include
  conditional measurement, with an equational theory and normal forms;
  the non-contextual fraction is monotone and contextual models cannot be
  cloned.
---

<!-- inactive-ok-file: CLAIM-100 — Proposed; open, and cited as open: the claim this reading bears on -->
<!-- inactive-ok-file: THEORY-tmprxblg — Proposed; cited for what this reading bears on, not as settled -->

# NOTE-tmp6dxz0: A comonadic view of simulation and quantum resources

## Contribution

Two earlier lines compared contextual resources: the contextual fraction
with a list of free operations it is monotone under ([LIT-265](../literature.d/LIT-265.md)), and
Karvonen's simulations ([LIT-tmpes6yu](../literature.d/LIT-tmpes6yu.md)). This paper joins them. It adds an
adaptive free operation, conditional measurement, and an equational
theory for the free operations. It builds a comonad of measurement
protocols, so that adaptive simulations are co-Kleisli maps, and proves
that a simulation exists exactly when a term in the free operations
converts one model into the other.

## Key insight

The operational notion ("use box d, with classical randomness and
classical control, to behave like box e") and the algebraic notion ("e
is built from d by free operations") pick out the same preorder.
Adaptivity, which was the missing piece in Karvonen's definition, is
added by changing the scenario rather than the morphism: measure a
protocol in MP(d) rather than a measurement in d.

## Assumptions

- **Finite scenarios** ⟨X, Σ, O⟩ with Σ a simplicial complex
  (Definition 1), and **no-signalling** empirical models (Definition 3:
  compatible families; compatibility "generalizes … no-signalling").
- **Basic morphisms use simplicial maps**, not relations (Definition 12);
  joint measurement of several source measurements is recovered through
  protocols.
- **Randomness is shared and classical**, supplied by an auxiliary
  non-contextual model c (Definition 18). The authors note that letting c
  range over a different class (e.g. quantum-realisable models) gives
  "relative simulatability".
- **Single-use boxes**: a protocol is one round of possibly sequential
  measurements on one copy.

## Key results

- **Proposition 7.** CF(z) = CF(u) = 0; CF(f*e) ≤ CF(e);
  CF(e/h) ≤ CF(e); CF(e +_λ e′) ≤ λCF(e) + (1 − λ)CF(e′);
  CF(e & e′) = max{CF(e), CF(e′)}; NCF(e ⊗ e′) = NCF(e)NCF(e′);
  CF(e[x?y]) = CF(e). Only the last is new here; the rest are cited to
  [LIT-265](../literature.d/LIT-265.md).
- **Proposition 8.** A term without variables denotes a non-contextual
  model, and every non-contextual model is so denoted: a deterministic
  one as (f*u)/h, the rest by mixing.
- **Propositions 10–11.** The equations are sound up to isomorphism, and
  every term has a normal form: mixtures at the top, then translation
  and coarse-graining, then conditional measurements, then tensors of
  base cases. Completeness is open.
- **Definitions 13–16, Theorem 17.** Runs, protocols (prefix-closed,
  outcome-complete, deterministic in the next measurement), the scenario
  MP(X) whose compatibility is "can be interleaved without ever
  measuring an incompatible set", the model MP(e), and the proof that MP
  is a comonoidal comonad (counit: a measurement as a one-step protocol;
  extension: run π(y) whenever Q calls y, reusing outcomes already
  obtained).
- **Theorem 20.** d simulates e (a deterministic map MP(d ⊗ c) → e, c
  non-contextual) iff e ≅ t[d/v] for some typed term t. Forward: c is a
  closed term and protocols are built by conditional measurements.
  Backward: by the normal form.
- **Theorem 21.** If d simulates e then NCF(d) ≤ NCF(e).
- **Theorem 22 (no-cloning).** e simulates e ⊗ e iff e is non-contextual.
  The proof first forces NCF(e) > 0 by pigeonhole on the finitely many
  protocol components, then rules out 0 < NCF(e) < 1 by Theorem 21 and
  NCF(e ⊗ e) = NCF(e)².

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Adaptive simulation with shared classical randomness coincides with conversion by free operations | strong (proof) | Theorem 20, via Propositions 8 and 11 |
| C2 | Measurement protocols form a comonoidal comonad on empirical models | strong (proof) | Theorem 17, §IV-C |
| C3 | Conditional measurement leaves the contextual fraction unchanged | strong (proof) | Proposition 7 |
| C4 | No contextual model can be cloned by classical simulation | strong (proof) | Theorem 22 |
| C5 | The equational theory is complete | not supported; open | §III-C |

## Method

Category theory and term rewriting. Free operations are typing rules
(Table II) whose closed terms are the free resources. A comonad on
scenarios lifts deterministic simulations to adaptive ones, and the
co-Kleisli category is where simulations live. The equivalence of the
two views is proved through normal forms.

## Concepts

- **free operation**: an operation on empirical models a classical agent
  can perform with no contextual resource beyond its arguments.
- **conditional measurement** x?y: measure x, and on outcome o measure
  y_o (a vertex in the link of x); its outcome is the pair.
- **link** lk_σ Σ: the faces still performable after σ has been
  measured.
- **measurement protocol**: a non-empty prefix-closed set of runs that
  answers every outcome and fixes the next measurement; a deterministic
  adaptive strategy, a "wiring".
- **simulation d ⇝ e**: a deterministic morphism MP(d ⊗ c) → e with c
  non-contextual.
- **isomorphism of models**: a simplicial isomorphism and bijections of
  outcomes carrying one to the other (Definition 9).

## Connections

It generalises Karvonen ([LIT-tmpes6yu](../literature.d/LIT-tmpes6yu.md)), whose morphisms had no
preprocessing, and it adds conditional measurement to the free operations
of Abramsky, Barbosa and Mansfield ([LIT-265](../literature.d/LIT-265.md)). It rests on Abramsky and
Brandenburger ([LIT-016](../literature.d/LIT-016.md)) for the framework. Measurement protocols come
from Acín, Fritz, Leverrier and Sainz, where they are "wirings". The
chapter by Barbosa, Karvonen and Mansfield ([LIT-tmp5at9s](../literature.d/LIT-tmp5at9s.md), Remark 28)
returns to non-adaptive procedures to characterise the maps they induce,
and says why: its key lemma fails for adaptive protocols.

## Bearing on the record

- **[CLAIM-100](../claims.d/CLAIM-100.md)** (directed transport between scenarios with changing
  covers). Translation of measurements is along an arbitrary simplicial
  map between scenarios, and the conditional measurement extends a
  scenario's cover with new measurements and faces. So the free
  operations already include cover-changing, stochastic, directed
  transport, and Theorems 20–21 say that every such transport is monotone
  for contextuality. Together with [LIT-tmpes6yu](../literature.d/LIT-tmpes6yu.md) this answers the
  "global compatibility" half of A94's question for no-signalling models.
  The "decision-relevant information" half is not addressed; nor is
  signalling data.
- **The manuscript's "repeated reconstruction" and chains.** A
  composite of free operations is a free operation, and CF is monotone
  along each step, so along any chain of classical transports
  contextuality can only fall. This is a corollary I draw (Theorems 20–21
  with composition in the co-Kleisli category); it bears on the
  manuscript's interest in how compatibility evolves "during translation
  and repeated reconstruction" (A93), which [CLAIM-100](../claims.d/CLAIM-100.md) quotes.
- Produces [THEORY-tmprxblg](../theory.d/THEORY-tmprxblg.md), with [LIT-tmpes6yu](../literature.d/LIT-tmpes6yu.md) and [LIT-tmp5at9s](../literature.d/LIT-tmp5at9s.md).
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- No-signalling models only.
- Completeness of the equational theory is open.
- Simulations are qualitative: existence, not cost; there is no measure
  of how much resource a simulation uses beyond NCF monotonicity.
- Single-use boxes; sequential reuse with state is out of scope.

## Open questions

- Completeness of equations (1)–(28), and whether Theorem 20 is a
  bijection between simulations and terms up to equality.
- Relative simulatability: grading MP by the auxiliary resource (for
  instance quantum-realisable c) and by run length.
- The link the outlook draws between simulations of possibilistic models
  and reductions between constraint-satisfaction problems.
