---
status: Read
paper: 'LIT-tmphrafc'
title: 'Fritz — A synthetic approach to Markov kernels'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from arXiv v8 (31 May 2020, 98 pages, text layer), the version
    matching the Advances in Mathematics paper. Read closely: Section 1
    (introduction and summary), Section 2 (Definition 2.1, FinStoch and
    FinSetMulti), Section 4 (Stoch, BorelStoch and Lemma 4.2; the
    Sacksteder and Dawid candidates skimmed), Section 6 (Gauss), the first
    half of Section 10 (deterministic morphisms, Examples 10.3–10.8,
    Lemma 10.9), Section 11 (conditionals, randomness pushback, positivity,
    causality, with their examples), Section 12 (all four notions of
    conditional independence and the semigraphoid propositions), Section 13
    (almost surely, ProbStoch, strict positivity, supports) and Sections
    14–16 (sufficiency, Fisher–Neyman, completeness, Basu, Bahadur).
    Skimmed: Section 3 (Kleisli construction), Section 5 (Radon monad),
    Sections 7–9 (diagram, hypergraph and comonoid categories), and the
    strictification half of Section 10 (Definition 10.14 to Remark 10.19).
    The string diagrams did not survive text extraction, so the content of
    the defining equations (sufficiency 14.1, positivity 11.8, causality
    11.12, conditional independence 12.1 and 12.16) is taken from the
    surrounding prose and the Notation 2.8 formulas, and diagrammatic proof
    steps were not checked. The reference list was skimmed.
date: '2026-10-09'
summary: >-
  Markov categories (symmetric monoidal, a commutative copy/discard
  comonoid on every object, discard natural) carry enough structure to
  define determinism, conditionals, four kinds of conditional independence
  with the semigraphoid rules, almost-sure equality, sufficiency,
  completeness and ancillarity. Basu's theorem then holds in every Markov
  category; Fisher–Neyman (Theorem 14.5) and Bahadur (Theorem 16.3) need
  strict positivity, which existence of conditionals implies but which
  Stoch has without them. The abstract Fisher–Neyman is checked against the
  classical one only in FinStoch.
---

<!-- inactive-ok-file: THEORY-tmpm1g8e — Proposed; filed from this reading -->
<!-- inactive-ok-file: THEORY-017 — Proposed; named for bases as extra structure, a parallel the reader draws, with no relation claimed -->
<!-- inactive-ok-file: LIT-tmpsujnn — Deferred; Blackwell's comparison of experiments, named as a neighbour, not cited by the paper -->
<!-- inactive-ok-file: LIT-tmpoo2k7 — Deferred; Torgersen's comparison of experiments, named as a neighbour, not cited by the paper -->

# NOTE-tmp23s9u: Fritz — A synthetic approach to Markov kernels

## Contribution

The paper fixes a definition, the Markov category, and shows how far it
reaches. Golubtsov and Cho and Jacobs had already used the same structure,
the latter for disintegration, Bayesian inversion and conditional
independence when conditionals exist. Fritz gives the name and works
without assuming conditionals. He splits conditional independence into
several notions, conditioning on inputs as well as outputs. He relativises
determinism to "almost surely". He states sufficiency, completeness,
ancillarity and minimal sufficiency purely in this language and proves
abstract Fisher–Neyman, Basu and Bahadur theorems. Each result is then
available in every Markov category satisfying its hypotheses: finite,
measure-theoretic and Gaussian probability, and processes built from them.

## Key insight

A Markov kernel is a process that may be random, and two operations on it
are free: copying a value and discarding it. Requiring only that discarding
commutes with every process (nothing comes from nowhere), and not that
copying does, is the whole difference between probability and
deterministic functions. A process is deterministic exactly when copying
its output equals running it twice on a copied input. Independence is a
diagram that falls apart into pieces. Much of elementary statistics is
equations between such diagrams. Its hardest step, the one that turns out
to need positivity of probability, is reduced to a single axiom.

## Assumptions

- **Markov category** (Definition 2.1): a symmetric monoidal category in
  which every object X carries a commutative comonoid, copy_X : X → X ⊗ X
  and del_X : X → I. These are compatible with ⊗ (2.4), and del is natural:
  del_Y ∘ f = del_X for every f (2.5). Equivalently, the category is
  semicartesian, with I terminal (Remark 2.3). Copy is *not* required to be
  natural.
- **Optional axioms** (Section 11), each stated where used:
  - *conditionals*: every f : A → X ⊗ Y factors as f(x, y|a) =
    f|X(y|x, a) f(x|a) (Definition 11.5);
  - *positivity*: if gf is deterministic, the joint of f's output and gf's
    output is the product (Definition 11.22);
  - *strict positivity*: the same relativised to p-almost surely
    (Definition 13.16);
  - *causality* (Definition 11.31), a generalised equality strengthening;
  - *randomness pushback* (Definition 11.19).
  Conditionals imply strict positivity, positivity and causality (Lemmas
  11.24, 13.18, Proposition 11.34).
- **Where each axiom holds.** FinStoch, BorelStoch and Gauss have
  conditionals. Stoch (all measurable spaces) does not, but is positive,
  strictly positive and causal (Examples 11.3, 11.18, 11.25, 11.35, 13.19).
  FinStoch± (signed "stochastic" matrices) is a Markov category that is not
  positive and has no conditionals (Example 11.27).
- **Statistics** (Definitions 14.1–14.2): a statistical model is any
  morphism p : Θ → X, and a statistic is a *deterministic* s : X → V.

## Key results

- **Deterministic morphisms** (Definition 10.1): f is deterministic iff
  copy ∘ f = (f ⊗ f) ∘ copy. In FinStoch these are the 0/1 matrices. In
  Stoch they are the kernels landing in {0, 1}-valued measures, which need
  not be Dirac (countable–cocountable σ-algebra), so Meas → Stoch_det is
  neither full nor faithful in general (Example 10.4). In BorelStoch they
  are exactly the measurable maps (10.5). In Gauss, (M, C, s) is
  deterministic iff C = 0 (10.7).
- **Conditionals are unique only in trivial categories** (Proposition
  11.15): uniqueness forces all parallel morphisms to be equal, a
  meet-semilattice. They are unique up to almost-sure equality
  (Proposition 13.7).
- **Gauss has conditionals** (Example 11.8), by the Moore–Penrose formula:
  (C_ηξ C_ξξ⁻, N − C_ηξ C_ξξ⁻ M, C_ηη − C_ηξ C_ξξ⁻ C_ξη, t − C_ηξ C_ξξ⁻ s).
- **Semigraphoid properties** (Lemma 12.5, Proposition 12.17): symmetry,
  decomposition and contraction hold in every Markov category; weak union
  is proved only assuming conditionals. For A ⊥⊥ Y | X (Proposition 12.20)
  symmetry cannot be stated; right decomposition and contraction hold, and
  weak union needs conditionals.
- **Conditional products** (Definition 12.8, Proposition 12.9): with
  conditionals, the unique joint with given marginals displaying
  X ⊥ Y | W. They satisfy Dawid and Studený's axioms, as a gleaf.
- **Positivity consequences**: every isomorphism is deterministic (Remark
  11.28); every comonoid structure on an object equals the distinguished
  one (11.29); a morphism with deterministic marginals is deterministic
  (Corollary 12.15).
- **ProbStoch(C)** (Proposition 13.9): for causal C, probability spaces
  and kernels modulo a.s. equality form a symmetric monoidal category. With
  conditionals it is the category of couplings, and Bayesian inversion is a
  symmetric monoidal dagger functor on it (Remark 13.10). Fritz says this
  answers an open problem of Clerc, Danos, Dahlqvist and Garnier, who had
  proved it for BorelStoch.
- **Sufficiency** (Definition 14.3): s is sufficient for p if some
  α : V → X makes the joint of (s, id) after p equal to the joint of
  (id, α) after s ∘ p. That is, given s the sample is redrawn from α
  independently of θ. Then sα = id holds sp-almost surely.
- **Theorem 14.5 (Fisher–Neyman).** In a strictly positive C, s is
  sufficient iff some α has αsp = p and sα = id sp-a.s. In FinStoch this
  gives p(x|θ) = α(x|s(x)) Σ_{x′∈s⁻¹(s(x))} p(x′|θ). The converse
  construction is α(x|v) = h(x)/Σ_{x′∈s⁻¹(v)} h(x′) (Example 14.6).
- **Completeness** (Definition 15.1) is a property of the kernel sp alone:
  f is complete if gf = hf implies g = h f-a.s. In FinStoch: the affine hull
  of f's image is a face of the simplex (15.3). In Stoch: bounded
  completeness (15.4). Every deterministic morphism is complete (Lemma
  15.5).
- **Theorem 15.8 (Basu)**, in any Markov category with no extra axiom: if
  s is sufficient, sp complete and a ancillary, then the joint of (s, a)
  after p displays V ⊥ W || Θ.
- **Theorem 16.3 (Bahadur)**, for strictly positive C: if a minimal
  sufficient statistic exists, a complete sufficient statistic is minimal.
  Minimality is leastness in the preorder t ≤ s iff t = cs p-a.s.
  (Definition 16.1).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Copy/discard with natural discard suffices to define determinism, conditionals, conditional independence, a.s. equality and sufficiency uniformly across finite, Borel, Gaussian and process settings | strong (definitions plus checked instances) | Sections 2, 4, 6, 10–14 |
| C2 | Symmetry, decomposition and contraction need no conditionals; weak union is proved with them | strong (proofs); that weak union fails without conditionals is not shown | Lemma 12.5, Propositions 12.17, 12.20 |
| C3 | Conditionals are never unique except in a meet-semilattice | strong | Proposition 11.15 |
| C4 | Basu's theorem holds in every Markov category | strong (diagrammatic proof; steps not checked here, diagrams lost) | Theorem 15.8 |
| C5 | Fisher–Neyman and Bahadur hold under strict positivity, which Stoch has without conditionals | strong | Theorems 14.5, 16.3, Example 13.19 |
| C6 | The abstract Fisher–Neyman is the classical factorisation | moderate: shown for FinStoch only; the measure-theoretic case is left open by the author | Example 14.6, end of Section 14 |
| C7 | Abstract completeness is bounded completeness in Stoch, so Theorem 15.8 recovers the standard Basu theorem | moderate to strong | Example 15.4, Remark 15.9 |
| C8 | Positivity is what separates probability from signed "probability": FinStoch± satisfies the Markov axioms but not positivity, and has no conditionals | strong for the example | Example 11.27 |
| C9 | Stoch is not the best Markov category for measure theory; BorelStoch is better behaved | moderate (argued from pathologies) | Examples 10.4, 11.3, 11.18 |

## Concepts

- **Markov category**: as in Assumptions. Cho and Jacobs' *affine
  CD-category*.
- **distribution**: a morphism I → X; a *probability space* is (X, ψ).
- **deterministic**: commutes with copy (Definition 10.1).
- **p-a.s. equal** (Definition 13.1): f and g agree after copying p's
  output and feeding one copy to them. In Stoch, the integrals of f(T|·)
  and g(T|·) against p(·|θ) agree on every measurable S. This is weaker
  than pointwise a.s. equality for non-countably-generated σ-algebras
  (Fremlin's example, Example 13.3).
- **X ⊥ Y | W**: conditioning on an output, for distributions
  (Definition 12.1). **X ⊥ Y || A**: conditioning on an input
  (Definition 12.12). **X ⊥ Y | W || A**: both (Definition 12.16).
  **A ⊥⊥ Y | X**: the morphism factors as a Markov chain A → X → Y
  (Definition 12.19), the form in which sufficiency is stated.
- **sufficiency witness**: the α of Definition 14.3; it plays the role of a
  conditional of the sample given the statistic, and needs no conditionals
  to exist.
- **complete**: a property of a morphism, not of a statistic relative to a
  model (Remark 15.2).
- **ancillary**: sp is constant in θ, sp = ψ ∘ del_Θ (Definition 15.7).
- **support** (Definition 13.20): an object representing morphisms out of
  X modulo p-a.s. equality. It exists in FinStoch; elsewhere it is
  conjectural.

## Connections

- **Cho and Jacobs (2019)**, the main precursor, which the record does not
  hold. Their a.s. equality, conditional independence with conditionals,
  and equality strengthening are generalised here. Causality is equivalent
  to a generalised equality strengthening (Remark 11.36).
- **Golubtsov**'s information transformers, the earliest form of the
  structure. **Lawvere (1962)**, **Čencov (1965)** and **Giry (1982)**
  for Stoch as a Kleisli category.
- **Dawid** on conditional independence and statistical operations, and
  **Dawid–Studený** conditional products, recovered in Section 12.
- **Coecke and Spekkens**, the quantum-foundations route to the same
  diagrams.
- **Fong**'s categorical Bayesian networks, where the structure appears
  implicitly.
- **Within the record.** Fritz's earlier convex spaces enter the reading of
  [LIT-038](../literature.d/LIT-038.md) ([NOTE-050](NOTE-050.md)). Baez–Fritz–Leinster's characterisation of entropy,
  stated on FinStoch, is cited in [NOTE-088](NOTE-088.md). Mansfield–Fritz appears in the
  reading of the sheaf-theoretic contextuality paper ([NOTE-016](NOTE-016.md)). FinSetMulti
  (Example 2.6) is the possibilistic counterpart of FinStoch, the same
  passage from probabilities to supports that [LIT-016](../literature.d/LIT-016.md) makes for
  contextuality (its Proposition 4.4). That link is mine.
- **Comparison of experiments.** The sufficiency witness and the ≤ order on
  statistics (Definition 16.1) are close to the order of informativeness
  in Blackwell ([LIT-tmpsujnn](../literature.d/LIT-tmpsujnn.md)) and Torgersen ([LIT-tmpoo2k7](../literature.d/LIT-tmpoo2k7.md)). The paper
  cites neither, and the link is mine.

## Bearing on the record

- **[THEORY-012](../theory.d/THEORY-012.md) (Active).** It holds that signed global sections always
  exist for no-signalling models, so negative probability does not mark
  contextuality. Fritz's FinStoch± (Example 11.27) fits that picture.
  Signed kernels satisfy every Markov-category axiom: copying,
  discarding, composition. What they lose is positivity, and with it
  conditionals and "every isomorphism is deterministic". So within this
  framework negativity is invisible to the copy/discard structure and
  appears only at the positivity axiom. This neither supports nor
  contradicts [THEORY-012](../theory.d/THEORY-012.md); it locates where negativity enters. The
  connection is mine.
- **[THEORY-017](../theory.d/THEORY-017.md) (Proposed).** It holds that a basis is extra data on a
  Hilbert space. In a Markov category the copy maps play the role of a
  chosen classical basis. Remark 11.29 shows that under positivity that
  choice is forced: every comonoid structure on an object equals the
  distinguished one. This is a parallel, not evidence for or against
  [THEORY-017](../theory.d/THEORY-017.md), since the settings differ.
- **New THEORY filed: [THEORY-tmpm1g8e](../theory.d/THEORY-tmpm1g8e.md)**, on which axioms the classical
  sufficiency theorems actually use.
- **Anthology.** No instruction for machine-learning practice. Not an
  anthology candidate.

## Limitations

- **The author says the definitions are provisional** and "will almost
  surely be subject to revision" (Section 1). Several are flagged as
  candidates, among them the axioms of Section 11 and supports.
- **Fisher–Neyman is matched to the classical theorem only in FinStoch.**
  The general measure-theoretic form is left as future work (end of
  Section 14).
- **The conditional independence of Definition 12.1, in Stoch, is not
  shown to agree with the conditional-expectation definition** (12.2);
  Remark 12.4 says the author does not see how to get it.
- **Weak union** is proved only with conditionals, and Stoch lacks them.
- **Randomness pushback in Stoch is open** (after Example 11.20).
  Conditionals in diagram categories, and so for stochastic processes
  through Section 7, are an open problem (Problem 11.9).
- **No new statistical theorem.** The payoff is uniformity and a sharper
  account of hypotheses, not new classical results.
- **Small slips in the text**: Definition 15.7 writes Θ ⊥⊥ T | I for a
  statistic into V; the Basu proof's ψ : I → U should land in W.

## Open questions

- Does Theorem 14.5 recover the measure-theoretic Fisher–Neyman theorem
  (Halmos–Savage form) in Stoch or BorelStoch? A proof in BorelStoch would
  close it.
- Does weak union fail in some Markov category without conditionals? A
  counterexample in Stoch, or a proof from causality or positivity, would
  settle it.
- When do minimal sufficient statistics exist (Problem 16.4)? Fritz
  suggests colimits.
- Is the Definition 13.20 support the topological support of a Radon
  measure (Remark 13.21)?
