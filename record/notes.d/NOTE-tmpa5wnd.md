---
status: Read
paper: 'LIT-tmp5o7bs'
title: 'Hyperbolic Entailment Cones for Learning Hierarchical Embeddings'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v3 (arXiv:1804.01882v3, 6 June
    2018, 13 pp.), text extracted with pdftotext and kept as paper.txt in
    the scratchpad download directory (dl/reg-hyp-ganea): abstract, §§1–6,
    the reference list and Appendices A–G. The proofs of Lemma 2
    (Appendix E) and Theorem 3 with its Lemma 7 (Appendix F) were followed
    step by step, and the derivation of Eqs. 23–26 from Theorem 3 was
    re-derived. Theorem 1 and Corollaries 1.1–1.2 (Appendices B–D) were
    followed at the level the appendices give, which is by the isometry
    to the hyperboloid and "one derives". Theorem 5's proof is one line
    plus "an algebraic reformulation"; I checked Eq. 28 numerically
    against the hyperbolic law of cosines (agreement to 4·10⁻¹² on 2,000
    random pairs in D³). Theorem 4 has no proof in the paper. A numerical
    check in D² with K = 0.1 found no violation of transitivity in 3,539
    sampled chains x ≥ y ≥ z, and no entailed point nearer the origin than
    its apex. Table 1 read; Figures 1–3 from captions and text. The PMLR
    PDF (PMLR 80:1646–1655) was compared word by word: same main text,
    appendices in a separate supplement, not downloaded. The authors' code
    and the cited works (Vendrov et al., Nickel and Kiela, Sarkar) were not
    read.
date: '2026-10-09'
summary: >-
  Nested, axially symmetric, rotation-invariant cones in the Poincaré ball
  define a partial order, but nesting forces apertures of at most π/2 and
  r sin ψ(r)/(1 − r²) non-increasing. So no cone exists near the origin,
  and the widest family is sin ψ = K(1 − r²)/r, with a closed-form
  membership angle. The transitivity of that family is asserted, not
  proved. Learned on WordNet noun hypernymy, the cones predict held-out
  closure edges better than Poincaré and order embeddings once some
  closure edges are in training. Trained on the transitive reduction
  alone, every method fails.
---
<!-- inactive-ok-file: THEORY-tmp5l4pi THEORY-tmpzw8vz THEORY-185 THEORY-186 QUESTION-025 CLAIM-119 LIT-267 — Proposed or open; cited as what this reading produced and the accounts and question it bears on -->

# NOTE-tmpa5wnd: Hyperbolic Entailment Cones for Learning Hierarchical Embeddings

## Contribution

Before this paper there were two ways to embed a hierarchy:

- **Order embeddings** (Vendrov et al.) encoded entailment as coordinatewise
  order in ℝⁿ, an asymmetric relation, but with what the authors call
  linear capacity in the dimension.
- **Poincaré embeddings** (Nickel and Kiela) used hyperbolic space's room
  for trees, but with a symmetric distance. Direction of entailment had to
  come from a heuristic on the norm.

This paper joins the two. Entailment is containment in a cone, defined
intrinsically on a Riemannian manifold through the exponential map. It
derives what cone shape transitivity allows in the Poincaré ball and in
ℝⁿ, and trains the cones with a max-margin loss on the angle by which a
point misses a cone. It also derives a closed-form exponential map of the
Poincaré ball.

## Key insight

To make an order out of regions, each point's region must contain the
regions of everything inside it. In hyperbolic space, with cones pointing
away from the origin, that nesting is affordable only if cones narrow as
they approach the boundary at a definite rate. The quantity
r sin ψ(r)/(1 − r²) cannot grow outward. The same rate rules out cones
near the origin, so the order has no top element in the geometry. The
most general concepts sit at radius ε and the most specific near the
boundary. Where the order sits is fixed by its distance from the origin.

## Assumptions

- **The four requirements on cones** (§3), stated as "necessary
  conditions":
  1. axial symmetry about the outward ray A_x = {αx : 1 ≤ α < 1/‖x‖};
  2. rotation invariance, ψ(x) = ψ̃(‖x‖);
  3. continuity of ψ̃;
  4. transitivity: x′ ∈ S_x ⇒ S_x′ ⊆ S_x.
- **"Optimal"** means widest pointwise. Theorem 3 bounds
  sin ψ̃(r) ≤ h(ε)(1 − r²)/r. The paper sets equality "to maximize model
  capacity", so the closed form is the upper envelope for a given K. It is
  not shown to be the only transitive family, nor optimal for any
  criterion other than aperture.
- **The domain excludes a ball** B(O, ε), ε ≥ 2K/(1 + √(1 + 4K²)). In
  training, points are projected outside it, with ε = 0.1.
- **The data is a DAG given by edges.** The training signal is
  hypernym pairs from WordNet's noun hierarchy, with the root removed, so
  the remaining subgraphs are co-embedded. There are no node features,
  attributes or text.
- **Evaluation.** Binary classification of held-out closure edges. Ten
  corrupted negatives are used per positive. The threshold is tuned for
  F1 on validation.

## Key results

- **Theorem 1, Corollary 1.1.** Closed-form unit-speed geodesics and the
  exponential map exp_x(v) in Dⁿ, derived from φ(t) = x cosh t + v sinh t
  on the hyperboloid through the isometry ψ(x) = (λ_x − 1, λ_x x).
- **Corollary 1.2.** Every geodesic of Dⁿ is coplanar with the origin.
- **Lemma 2.** Transitivity (with properties 1–3) implies ψ(x) ≤ π/2.
  Proof: if ψ(x) > π/2, every point x′ on the cone's boundary must have
  ψ(x′) ≤ π/2, since the angles ∠yx′z and ∠zx′x sum to π and both must be
  at least ψ(x′). Continuity along the boundary toward x then gives a
  contradiction.
- **Theorem 3.** Transitivity implies h(r) = (r/(1 − r²)) sin ψ̃(r) is
  non-increasing. Proof: by the hyperbolic law of sines in the triangle
  Oxx′ for x′ on ∂S_x (Lemma 7), using
  sinh(‖x‖_D) = 2r/(1 − r²), and a boundary geodesic that reaches every
  radius r′ > r. Consequence: lim_{r→0} h = 0 for any ψ̃, so a non-zero
  ψ̃ cannot be defined on all of (0, 1).
- **Eqs. 24–26.** Setting h ≡ K gives
  ψ(x) = arcsin(K(1 − ‖x‖²)/‖x‖) on Dⁿ \ B(O, ε), with
  K ≤ 2ε/(1 − ε²).
- **Theorem 4.** With this ψ, transitivity holds. The paper says only that
  the proof is "similar to that of Thm. 3", and gives none. The numerical
  check in the history note found no counterexample in D².
- **Theorem 5.** S_x = {y : Ξ(x, y) ≤ ψ(x)}, with
  Ξ(x, y) = π − ∠Oxy given in closed form (Eq. 28). From the hyperbolic
  law of cosines (Appendix G).
- **Euclidean cones.** sin ψ = K/‖x‖ with K ≤ ε, and Ξ from the ordinary
  law of cosines (Eq. 31). The text says h(r) = r sin ψ(r) is
  "non-decreasing". By the argument of Theorem 3, and by the constraint
  K ≤ ε, it must be non-increasing; that looks like a slip.
- **Training (§4).** Loss: Σ_P E(u, v) + Σ_N max(0, γ − E(u′, v′)), with
  E(u, v) = max(0, Ξ(u, v) − ψ(u)) and γ = 0.01. Riemannian SGD scales
  the gradient by (1 − ‖u‖²)²/4. Hyperbolic cones are initialised from
  Poincaré embeddings trained 100 epochs and rescaled by 0.7. Euclidean
  cones are initialised from Simple Euclidean embeddings.
- **Table 1 (test F1, WordNet nouns).** Columns are 0 / 10 / 25 / 50% of
  the non-basic edges in training.

  | model | dim 5 | dim 10 |
  |---|---|---|
  | Simple Euclidean | 26.8 / 71.3 / 73.8 / 72.8 | 29.4 / 75.4 / 78.4 / 78.1 |
  | Poincaré | 29.4 / 70.2 / 78.2 / 83.6 | 28.9 / 71.4 / 82.0 / 85.3 |
  | Order embeddings | 34.4 / 70.2 / 75.9 / 81.7 | 43.0 / 69.7 / 79.4 / 84.1 |
  | Euclidean cones | 28.5 / 69.7 / 75.0 / 77.4 | 31.3 / 81.5 / 84.5 / 81.6 |
  | Hyperbolic cones | 29.2 / 80.1 / 86.0 / 92.8 | 32.2 / 85.9 / 91.0 / 94.4 |

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Nested axially symmetric, rotation-invariant, continuous cones in Dⁿ have aperture at most π/2 | strong (proof) | Lemma 2, Appendix E |
| C2 | For such cones, r sin ψ(r)/(1 − r²) is non-increasing, so none can be defined on a neighbourhood of the origin | strong (proof) | Theorem 3, Appendix F |
| C3 | The family sin ψ = K(1 − r²)/r is transitive | moderate | Theorem 4 asserted; proof "similar" and not given; consistent with my numerical check |
| C4 | That family is the optimal (widest) admissible one | moderate | pointwise maximal given K by Theorem 3; uniqueness among all transitive families not shown |
| C5 | Cone membership has the closed form of Eq. 28 | strong | Theorem 5; checked numerically here |
| C6 | Hyperbolic cones generalise better on WordNet closure edges than order and Poincaré embeddings | moderate | Table 1, single runs, no variance; holds from 10% closure in training, not at 0% |
| C7 | The gain is due to hyperbolic geometry | weak | the authors report that Euclidean cones initialised from Poincaré embeddings match hyperbolic cones, without numbers |
| C8 | Cones have more capacity than order embeddings | weak | argued from volume (footnote 2) and shown by generalisation numbers and Figure 3; no reconstruction or capacity experiment |

## Method

Embed each node as a point of Dⁿ outside B(O, ε). Score an ordered pair
(u, v) by the angle Ξ(u, v) by which v falls outside u's cone. Push
positive pairs to zero and corrupted pairs above the margin γ. Update by
Riemannian SGD with the retraction x + v in place of the exact
exponential map, which was found to make no significant difference.
Predict an edge when the energy is below a threshold tuned on validation.

## Concepts

- **S-cone at x**: exp_x(S) for a cone S in the tangent space T_xM.
  This is the generalisation of a convex cone to a geodesically complete
  manifold. In hyperbolic space it is geodesically convex.
- **angular cone S_x^ψ(x)**: the S-cone of tangent vectors within angle
  ψ(x) of the outward axis direction x̄.
- **entailment**: (u, v) with v a subconcept of u, modelled as v ∈ S_u.
  This reverses Nickel and Kiela's notation.
- **basic edges**: the transitive reduction of the DAG, always in
  training.
- **non-basic edges**: closure edges not in the reduction (578,477), from
  which validation, test and the 10–50% training additions are drawn.
- **Ξ(x, y)**: π − ∠Oxy, the angle between the half-line from x through
  y and the outward ray through x.

## Connections

The paper sets itself between Vendrov et al.'s order embeddings and
Nickel and Kiela's Poincaré embeddings. For why trees fit hyperbolic
space, it cites Gromov's δ-hyperbolicity (via Bowditch, Prop. 6.7: δ-
hyperbolic point sets are within O(δ log n) of a weighted tree), Sarkar,
and the arXiv version of Sala et al. as "De Sa et al., 2018"
([LIT-tmpt10fk](../literature.d/LIT-tmpt10fk.md)). It cites Krioukov et al. 2010 ([LIT-tmp0u9c9](../literature.d/LIT-tmp0u9c9.md)) among uses
of hyperbolic space for scale-free graphs. Riemannian SGD is Bonnabel's.

**Against Sala et al. ([LIT-tmpt10fk](../literature.d/LIT-tmpt10fk.md), [NOTE-tmprdxf9](NOTE-tmprdxf9.md)).** The two represent
an order in different ways.

- Sala's Proposition D.2 represents the transitive closure of a *tree*
  by symmetric distance: every ancestor is nearer than any
  non-ancestor. It has guaranteed distortion and no learning.
- Here the relation is asymmetric containment, it is stated for any DAG,
  and it is learned with no guarantee.
- Sala's evaluation is reconstruction (MAP); this paper's is held-out
  link prediction (F1). Their WordNet numbers are not comparable.
- Sala's precision result ([THEORY-tmpzw8vz](../theory.d/THEORY-tmpzw8vz.md)) bears on cones too, and this
  is my connection. Specific concepts sit near the boundary, where
  apertures shrink as (1 − r²)/r. Deciding membership for deep nodes
  needs coordinates resolved at about the depth in bits.

**Against Yang et al. ([LIT-tmpocqly](../literature.d/LIT-tmpocqly.md), [NOTE-tmp4751w](NOTE-tmp4751w.md)).** Yang's NOTE
records that they read hierarchy only as distance to the origin, and do
not consider entailment cones. Cones bind order to the origin by
construction. Entailment requires ∠Oxy ≥ π/2, so in the triangle Oxy the
side Oy is the longest, and every entailed point is farther out than its
apex. This is my derivation. In a perfectly fitted cone embedding,
radius is monotone along every chain, and the gauge freedom Yang
identify (an isometry moves the origin) is absent, since the cones
are not isometry-invariant. Whether trained cones achieve that fit is
the same question Yang ask, and this paper does not measure level order.

## Bearing on the record

- **[QUESTION-025](../questions.d/QUESTION-025.md)** asks whether attributes
  that imply or exclude each other in co-occurrence still give linear
  attribute directions, and a non-Boolean concept lattice. **Not
  answered.** There is no co-occurrence, no PMI, no attribute and no
  linear direction. Concepts are free points fitted to WordNet edges. What
  the paper supplies is a third encoding of implication, beside
  [THEORY-185](../theory.d/THEORY-185.md)'s half-spaces and Sala's distances. Here implication is
  containment of cones: non-linear, asymmetric and radial. Its Euclidean
  baseline, order embeddings, is the half-space encoding. Each coordinate
  acts as an attribute and a concept as a conjunction of thresholds, so
  Vendrov's order is an intersection of n axis-aligned half-spaces. (The
  posets that embed in that order are exactly those of order dimension at
  most n, by Dushnik and Miller; my connection.) The cones beat it once
  closure edges are in training. That is a finding about learned
  embeddings under supervision, not about what co-occurrence produces. It
  belongs to the question's open alternative: if linear directions fail
  for implicational attributes, a hierarchy may still be held by region
  containment rather than by directions.
- **Exclusion is not represented.** Disjoint cones would say that two
  concepts share no descendant. Training only penalises non-entailment,
  and a point that falls in two cones counts as below both. So "excludes"
  and "does not entail" are not distinguished. A concept lattice built
  from attributes that exclude each other would need that distinction.
- **[CLAIM-119](../claims.d/CLAIM-119.md)** (communicative categories form a
  concept lattice rather than a hierarchy).
  - What the paper allows: a non-tree partial order. Cones of
    incomparable apexes overlap, and my 2-D sampling found 75 triples
    with a point in both of two incomparable cones. So shared descendants
    are representable, unlike in Sala's tree construction.
  - What it does not give: a lattice. The intersection of two cones is
    not a cone, so meets and joins have no geometric counterpart. Nothing
    is proved about which finite posets or lattices embed, or in what
    dimension.
  - The evidence: WordNet nouns, a mostly tree-shaped DAG. The paper
    reports nothing separately for multi-parent synsets.
  - So it neither supports nor tells against [CLAIM-119](../claims.d/CLAIM-119.md). [CLAIM-119](../claims.d/CLAIM-119.md) is a
    claim about how categories are organised, and this paper is about
    what a geometry can hold.
- **Produces [THEORY-tmp5l4pi](../theory.d/THEORY-tmp5l4pi.md)**: what nesting forces on cones in the
  Poincaré ball, and the radial monotonicity it implies, with the scope of
  the proofs. The record held nothing on representing a partial order
  geometrically before this.
- **[THEORY-186](../theory.d/THEORY-186.md)** (Saxe et al.: tree-structured
  features give tree-wavelet directions in a linear network). This is a
  contrast, and my connection. There, the hierarchy becomes linear
  directions for branch contrasts. Here, it becomes nested regions with
  no directions. Both are supervised on a known hierarchy.
- **Anthology.** It carries ML practice: initialisation from Poincaré
  embeddings, rescaling by 0.7, the burn-in, and the finding that exact
  Riemannian steps do not help. An anthology topic could hold it
  (concept geometry, graphs). The anthology does not hold it, so the LIT
  carries `anthology-candidate`.

## Limitations

- **Theorem 4, the sufficiency of the closed form, is not proved** in the
  paper. Lemma 2 and Theorem 3 are necessity results.
- **"Optimal" is a choice.** Making h constant gives the widest
  apertures for a given K. That this is the only reasonable or the best
  family is not shown.
- **The Euclidean statement has a slip.** "Non-decreasing" for
  h(r) = r sin ψ should be non-increasing.
- **The experiments do not test the structure the method is for.**
  - There is one dataset, no full-reconstruction setting and no variance.
  - Performance on multi-parent nodes is not separated out.
  - At 0% closure, where a transitive geometry should have helped most,
    every method scores below 45 F1. The paper does not say whether
    training negatives can include true closure edges, which would work
    against transitivity.
- **Attribution of the gain is unsettled.** Euclidean cones initialised
  from Poincaré embeddings match hyperbolic cones, by the authors'
  account. Initialisation, not curvature, may carry much of the
  improvement. No numbers are given.
- **The order has no top.** The ball B(O, ε) is excluded, and the WordNet
  root is removed. The paper turns that consequence into a design choice
  without discussing it.

## Open questions

- A proof of Theorem 4, in any dimension, or a counterexample near the
  boundary of S_x where both cones are tight.
- Which finite posets embed in the cone order of Dⁿ, and in what
  dimension? Is there an analogue of order dimension for cones, and is it
  lower than for Vendrov's coordinatewise order? A capacity theorem of
  that kind is what C8 would need.
- Whether a concept lattice's meets can be made geometric. For example,
  is the largest cone inside S_x ∩ S_y the cone of a point exactly when
  x and y have a meet?
- For [QUESTION-025](../questions.d/QUESTION-025.md): whether an embedding learned from co-occurrence,
  not from hypernym edges, places attributes that imply each other so
  that one's region contains the other's. That would be a measurement on
  WordNet hypernymy in the question's own terms.
