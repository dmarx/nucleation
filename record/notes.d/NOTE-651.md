---
number: 651
status: Read
formerly:
- NOTE-tmpvuygo
paper: 'LIT-846'
title: 'Categories of Empirical Models'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF (1804.01514v3, the EPTCS 287
    version, 14 pages, text layer extracted): §§1–5, every definition,
    example and theorem, the appendix proof of Theorem 4.7 and the
    reference list. The proofs of Theorems 4.1, 4.3, 4.5 and 4.8 and of
    Lemma 3.12 were followed step by step; the no-cloning induction was
    followed but not re-derived. The monoidal structure is asserted
    ("straightforward but tedious") and not checked. Cited works not
    read: Wester 2018, Amaral et al. 2018, Mansfield's thesis.
date: '2026-10-09'
summary: >-
  Gives empirical models on different measurement scenarios a category:
  a simulation answers each target measurement with a jointly measurable
  set of source measurements and a stochastic outcome map natural in the
  context. Non-contextuality becomes simulability from nothing, the
  non-contextual fraction becomes a functor (contextuality cannot grow
  along a simulation), strong contextuality is reflected, Graham
  reductions are simulations, and contextual models cannot be cloned.
---

<!-- inactive-ok-file: CLAIM-100 CLAIM-105 — Proposed; open, and cited as open: the claims this reading bears on -->
<!-- inactive-ok-file: THEORY-174 THEORY-156 — Proposed; cited for what this reading bears on, not as settled -->

# NOTE-651: Categories of Empirical Models

## Contribution

Before this paper, morphisms between empirical models (Mansfield's
thesis, Wester) were deterministic and sent each measurement to one
measurement. This paper allows a target measurement to be answered by a
set of source measurements and allows the outcome map to be stochastic,
using the Kleisli category of the distribution monad. With these
morphisms it recasts known facts about contextuality as facts about one
category, Emp_R, and proves a no-cloning theorem for contextual models.
The category is offered as a resource theory of contextuality.

## Key insight

One empirical model can stand in for another when a team of
non-communicating agents, each told only which target measurement to
perform, can answer it by measuring a fixed set of the source model's
measurements and processing the outcomes with shared classical
randomness. Classical processing of this kind cannot manufacture a global
inconsistency that was not already in the source. So contextuality is
what cannot be simulated from nothing, and every simulation is monotone
for it.

## Assumptions

- **Finite scenarios.** ⟨X, M, (O_x)⟩ with X finite, each O_x finite, and
  M an antichain covering X (Definition 2.1).
- **Distributions over a semifield R** (R≥0, ℝ or the Booleans), so that
  conditional distributions exist (Definition 2.3). Only Theorem 4.7
  uses the semifield restriction.
- **No-signalling built in.** Empirical models are compatible families
  (Definition 2.6). Remark 3.2: the pushforward is well defined only
  because d restricted to π(C) does not depend on which source context
  contains π(C), so signalling models are excluded by necessity, not by
  choice.
- **Morphisms point the other way from the map of complexes.** A
  morphism Y → X has π : X → Y (footnote 1), chosen so that maps from
  the terminal object are global sections.
- **No preprocessing.** π is fixed: no randomised or adaptive choice of
  which source measurements to perform (§5).

## Key results

- **Definition 3.1 (deterministic morphism).** A simplicial relation
  π : X → Y (every target context C has π(C) inside some source context)
  and a natural transformation σ : E_Y(π(−)) → E_X(−). Pushforward:
  (σ_*d)_C = D_R(σ_C)(d|π(C)). Lemma 3.3: since E_X is a sheaf, such σ
  glue uniquely along any cover.
- **Definition 3.9 (R-stochastic morphism, simulation).** As above with
  σ : E_Y(π(−)) → D_R ∘ E_X(−); composition is Kleisli. A simulation
  d → e is a morphism with σ_*d = e. Lemma 3.12: stochastic σ glue along
  partitions (by independent product), not uniquely and not along
  arbitrary covers, because D_R ∘ E_X is not a sheaf.
- **Proposition 3.13.** Simulations of e_1, …, e_n from d with the same π
  mix into a simulation of their convex combination.
- **Theorem 4.1.** Simulations 1 → e from the terminal model on the empty
  scenario correspond bijectively to global distributions explaining e;
  so e is R-non-contextual iff a simulation 1 → e exists.
- **Theorem 4.2.** A semifield homomorphism R → S gives a functor
  Emp_R → Emp_S preserving the terminal object; so S-contextuality of the
  image implies R-contextuality, and logical contextuality implies
  probabilistic contextuality. The possibilistic-collapse functor is
  neither surjective on objects nor full.
- **Theorem 4.3.** For R = R≥0 or the Booleans, if d → e and e is strongly
  contextual, then d is strongly contextual.
- **Lemma 4.4 and Theorem 4.5.** Pushforward preserves convex mixtures,
  so a decomposition d = λd^NC + (1 − λ)d′ pushes to one of e;
  NCF(d) ≤ NCF(e) whenever d → e. Equivalently CF(e) ≤ CF(d).
- **Theorem 4.7.** If x lies in exactly one maximal context S, there is a
  simulation e|X\{x} → e (sample x from the conditional e_S(− | s)). So
  any model on a cover reducible to nothing by Graham reductions is
  non-contextual: Vorob'ev's theorem in this language.
- **Theorem 4.8 (no-cloning).** With e ⊗ d on the join of covers, a
  simulation e → e ⊗ e exists iff e is non-contextual. The proof is by
  induction on |X|, using that π from the n-fold copy back to X must
  either cover X in every copy (forcing X itself to be a context) or
  miss part of it in some copy.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A model is non-contextual iff it can be simulated from the empty model | strong (proof) | Theorem 4.1 |
| C2 | Simulation never increases the contextual fraction, across scenarios with different covers | strong (proof) | Lemma 4.4, Theorem 4.5 |
| C3 | Simulation reflects strong contextuality | strong (proof) | Theorem 4.3 |
| C4 | Acyclic covers admit only non-contextual models, via simulations | strong (proof) | Theorem 4.7 |
| C5 | A model can be cloned by classical simulation iff it is non-contextual | strong (proof), monoidal structure asserted | Theorem 4.8 |
| C6 | The morphisms capture "simulation with shared classical randomness" fully | not claimed; open | §5: preprocessing is missing |

## Method

Category theory over the sheaf-theoretic framework. Scenarios are
simplicial complexes with an outcome sheaf; morphisms are pairs of a
simplicial relation and a (Kleisli) natural transformation, by analogy
with morphisms of ringed spaces. Results are proved by turning a
property of a model into the existence of an arrow (from the terminal
object, or to a product with itself).

## Concepts

- **simplicial relation**: a relation π : X → Y such that the image of
  every face is contained in a face.
- **event sheaf** E_X: U ↦ ∏_{x∈U} O_x, with projections.
- **simulation d → e**: a morphism of scenarios whose pushforward takes
  d to e; "d simulates e".
- **non-contextual fraction** NCF(e): the largest λ with
  e = λe^NC + (1 − λ)e′, e^NC non-contextual; CF = 1 − NCF.
- **Graham reduction**: deleting a vertex that lies in exactly one maximal
  face; acyclic means reducible to the empty complex.

## Connections

Builds on Abramsky and Brandenburger ([LIT-016](../literature.d/LIT-016.md)) for scenarios, models and
the global-section criterion, and on the contextual fraction of Abramsky,
Barbosa and Mansfield ([LIT-265](../literature.d/LIT-265.md)), which it shows to be functorial. The
resource-theory reading follows Coecke, Fritz and Spekkens. The direct
successor is the comonadic paper ([LIT-847](../literature.d/LIT-847.md)), which replaces the
relation by a simplicial map plus adaptive measurement protocols and adds
preprocessing; the chapter "Closing Bell" ([LIT-845](../literature.d/LIT-845.md)) revises the
morphisms again (mixtures of deterministic procedures) and characterises
which maps of models they induce.

## Bearing on the record

- **[CLAIM-100](../claims.d/CLAIM-100.md)** (directed transport between scenarios whose covers
  change is the theory's open problem). This paper is prior art that
  [CLAIM-100](../claims.d/CLAIM-100.md)'s "Partial prior art" lacks. A morphism here is a directed,
  stochastic transport from one scenario to another whose cover may be
  entirely different: π assigns each target measurement a jointly
  measurable set of source measurements, and σ maps local outcomes
  stochastically. The paper proves what such transport preserves:
  non-contextuality is preserved and the contextual fraction cannot
  increase (Theorem 4.5), strong contextuality is reflected (4.3). So
  the "compatibility structure" half of A94's question has a partial
  answer from 2018. What remains open, relative to [CLAIM-100](../claims.d/CLAIM-100.md): transport
  of signalling data (excluded by Remark 3.2), and preservation of
  "decision-relevant information", which no result here addresses. The
  simulation order is a resource order on contextuality, not an
  informativeness order.
- **[CLAIM-121](../claims.d/CLAIM-121.md) and [CLAIM-070](../claims.d/CLAIM-070.md)** (the manuscript's Propositions 1 and 2).
  Both are special cases of results here, read by me rather than stated by
  the paper. A natural transformation σ is exactly a family of local
  kernels that commutes with restriction ([CLAIM-121](../claims.d/CLAIM-121.md)), and because it is
  defined on every subset of X, including X itself, it carries a global
  kernel σ_X whose restrictions are the local ones: [CLAIM-070](../claims.d/CLAIM-070.md)'s "one
  global stochastic kernel". Theorem 4.1 composed with any simulation
  gives [CLAIM-070](../claims.d/CLAIM-070.md)'s conclusion, a global section of the target. Lemma
  3.12 and the remark before it give [CLAIM-070](../claims.d/CLAIM-070.md)'s stated limit: local
  stochastic kernels need not glue to a global one, since D ∘ E is not a
  sheaf. The manuscript's caution that "cover-changing … maps demand
  separate analysis" (§6) is answered for no-signalling models: π may
  change the cover arbitrarily so long as it is simplicial.
- **[CLAIM-105](../claims.d/CLAIM-105.md) and [QUESTION-004](../questions.d/QUESTION-004.md)** (transports that destroy or create
  contextuality). Destroying it is possible (any simulation to a
  non-contextual model). Creating it by free (classical) transport is
  impossible (Theorem 4.5).
- **[THEORY-156](../theory.d/THEORY-156.md)** (Blackwell: more informative iff garbling). A
  structural parallel the paper does not draw: a simulation must use one
  procedure for every target context, as a garbling uses one kernel for
  every state, and both orders are characterised by monotones. On a
  single-context scenario a simulation is a stochastic map of outcomes,
  a garbling of a one-state experiment. This is my observation; nothing
  here relates the simulation preorder to Blackwell's.
- Produces [THEORY-174](../theory.d/THEORY-174.md), with its two successors.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- No-signalling models only (Remark 3.2).
- No preprocessing: randomised or adaptive choice of measurements is
  left open (§5); the comonadic paper supplies it.
- The monoidal structure is asserted to be symmetric monoidal without a
  written proof.
- Strong contextuality has no categorical characterisation here, only
  monotonicity (§4).
- No quantitative or computational content: whether a simulation d → e
  exists is not shown to be decidable or computable.

## Open questions

- Whether other classes (strongly contextual, All-vs-Nothing,
  cohomologically obstructed, quantum-realisable) are characterised by
  the category (§5).
- Whether simulation with preprocessing (or with quantum resources) gives
  the "right" category; the author names the risk that combining a
  relation π with stochastic preprocessing is ill-defined (mixing x₁ with
  {x₂, x₃}).
- An analogue of complexity-theoretic completeness: is there a model
  that simulates every model of a fixed scenario's contextuality class?
