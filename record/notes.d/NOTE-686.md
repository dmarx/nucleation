---
number: 686
status: Read
formerly:
- NOTE-tmpfo6lq
paper: 'LIT-879'
title: 'Hyperbolic Neural Networks'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v2 (arXiv:1805.09112v2, 28 June
    2018, 21 pp.), text extracted with pdftotext and kept as paper.txt in
    the scratchpad download directory (dl/reg-cited-1805.09112): abstract,
    §§1–5, the reference list and Appendices A–F. The proof of Theorem 4
    (Appendix B) was followed step by step and re-derived: with
    γ̇ = Kγ, the Christoffel term reduces to cλK‖γ‖²X, so a field
    parallel to v with length scaled by λ₀/λ_γ is parallel. The proofs of
    Eq. 22 (Appendix C), Theorem 5 with Lemmas 7–9 (Appendix D) and the
    gyro-chain rule (Appendix E) were followed at the level given.
    Numerical checks, on random points and tangent vectors in D³_c with c
    between 0.3 and 2: Eq. 8 against Eq. 4 (agreement 10⁻¹⁴); Lemma 2,
    log_x(exp_x(v)) = v and d(x, exp_x(v)) = λ_x‖v‖ (10⁻¹¹); Lemma 3
    (10⁻¹⁶); Eq. 15 (10⁻¹⁴); Theorem 4's identity
    log_x(x ⊕ exp₀(v)) = (λ₀/λ_x)v (10⁻¹³); Theorem 5 against a grid
    search along the geodesic hyperplane in D² (2·10⁻⁵, the grid's
    resolution). Tables 1 and 2 read, the error-reduction factors of §4
    recomputed from Table 1; Figures 1–5 from captions and text. The
    arXiv v1, the NeurIPS PDF and the authors' code were not read, nor
    the cited works (Ungar, Tallec and Ollivier, Nickel and Kiela).
date: '2026-10-09'
summary: >-
  Möbius gyrovector operations give the Poincaré ball closed-form
  exponential and logarithmic maps, parallel transport from the origin
  as a scaling, and geodesic hyperplanes with a closed-form distance;
  from them come hyperbolic logistic regression, feed-forward layers and
  GRUs that reduce to the Euclidean ones as c → 0. Because linear maps
  and nonlinearities are lifted through the origin's tangent space, the
  curvature acts only through biases and output distances. Gains over
  Euclidean models are confined to a synthetic tree-like task and to
  separating WordNet subtrees in low-dimensional Poincaré embeddings.
---
<!-- inactive-ok-file: THEORY-185 THEORY-189 THEORY-196 THEORY-186 QUESTION-025 CLAIM-119 — Proposed or open; cited as the accounts and question this reading bears on -->

# NOTE-686: Hyperbolic Neural Networks

## Contribution

Before this paper, hyperbolic space was used in machine learning for
embeddings: points fitted to a graph by Nickel and Kiela, Sala et al.
([LIT-874](../literature.d/LIT-874.md)) and the same authors' entailment cones ([LIT-866](../literature.d/LIT-866.md)). There was no
way to compute with those points inside a network: no hyperbolic matrix
multiplication, bias, softmax or recurrent cell. This paper supplies
them. It ties Ungar's gyrovector operations to the Riemannian geometry of
the ball and derives closed forms for the exponential and logarithmic
maps, parallel transport from the origin, and distance to a geodesic
hyperplane. From these it builds logistic regression, feed-forward layers
and GRUs, each a one-parameter deformation of its Euclidean counterpart
in the curvature c.

## Key insight

A hyperbolic layer is a Euclidean layer read through a chart. The paper
lifts a map f between Euclidean spaces to the ball as exp₀ ∘ f ∘ log₀, so
any composition of lifted maps is exp₀ ∘ (the Euclidean composition) ∘
log₀. Geometry that the chart at the origin cannot absorb enters in only
two places. One is the bias, a Möbius translation, which is parallel
transport from the origin followed by the exponential map at x. The
other is the output layer, where logits are hyperbolic distances to
geodesic hyperplanes. Everything that makes these networks hyperbolic is
in those two operations.

## Assumptions

- **Constant curvature −c, Poincaré ball model.** Dⁿ_c = {x : c‖x‖² < 1},
  with metric λ_x² times the Euclidean one and λ_x = 2/(1 − c‖x‖²). The
  experiments use c = 1 throughout.
- **The lifting is a choice, made at the origin.** "Möbius version"
  f^{⊗c} = exp₀ ∘ f ∘ log₀ is a definition. It is motivated by Lemma 3,
  where scalar multiplication has this form, and it is not derived from
  any requirement. It privileges the origin; translating the inputs by an
  isometry does not commute with it.
- **Euclidean MLR as signed distances.** The construction starts from
  ⟨a, x⟩ − b = sign(⟨a, x⟩ − b)‖a‖ d(x, H_{a,b}), after Lebanon and
  Lafferty. Replacing + with ⊕_c in H = p + {a}^⊥ is the generalisation
  step; the scale factor λ_p‖a‖ (the norm of a at p) is chosen so that
  the c → 0 limit is the Euclidean softmax.
- **Experiments.** Embedding and hidden dimension 5, batch 64, 30 epochs.
  Euclidean parameters trained with Adam, hyperbolic ones (word
  embeddings, biases, MLR points) with full Riemannian SGD at fixed
  learning rates. Results clipped to radius 1 − 10⁻⁵. Each Table 1 cell
  is the test score of the best of three runs by validation.

## Key results

- **Eq. 8.** d_c(x, y) = (2/√c) tanh⁻¹(√c‖−x ⊕_c y‖), equal to the
  standard Poincaré distance at c = 1 and to 2‖x − y‖ as c → 0. Checked.
- **Lemma 1, Lemma 2.** Unit-speed geodesics and
  exp_x(v) = x ⊕_c tanh(√c λ_x‖v‖/2) v/(√c‖v‖), with log_x its inverse.
  The proof leans on the entailment-cones paper's Corollary 1.1 and an
  "algebraic check". Checked numerically.
- **Lemma 3.** r ⊗_c x = exp₀(r log₀(x)), and the geodesic from x to y is
  exp_x(t log_x(y)) (Eq. 15). Checked.
- **Theorem 4.** Parallel transport along the radial geodesic from 0 to x
  is P(v) = log_x(x ⊕_c exp₀(v)) = (λ₀/λ_x)v. Proved in Appendix B from
  the Christoffel symbols of a conformal metric; the proof is correct, and
  I re-derived it in two lines (history note). The paper uses this to
  make tangent parameters at moving points trainable as Euclidean
  vectors at the origin.
- **Definition 3.1, Eq. 22.** The Poincaré hyperplane through p with
  normal a is exp_p({a}^⊥) = {x : ⟨−p ⊕_c x, a⟩ = 0}, the union of
  geodesics through p orthogonal to a (proved in Appendix C).
- **Theorem 5.** d_c(x, H_{a,p}) =
  (1/√c) sinh⁻¹(2√c|⟨−p ⊕_c x, a⟩|/((1 − c‖−p ⊕_c x‖²)‖a‖)). Proved via
  the existence and uniqueness of an orthogonal projection onto a
  geodesic (Lemma 7), its minimality (Lemma 8, "similar to the Euclidean
  case"), and the hyperbolic law of sines. Checked numerically in D².
- **Lemma 6.** Möbius matrix-vector multiplication has the closed form of
  Eq. 27. It is associative, (MM′) ⊗ x = M ⊗ (M′ ⊗ x), and it equals Mx
  for orthogonal M.
- **Hyperbolic GRU (Eqs. 31–33).** Gates are σ of log₀ of a hyperbolic
  pre-activation. The update is h_t = h_{t−1} ⊕ diag(z_t) ⊗ (−h_{t−1} ⊕
  h̃_t), derived in Appendix E by redoing Tallec and Ollivier's
  time-warping argument with the gyro-derivative; the gyro-chain rule
  (Lemma 10) is proved.
- **Table 1 (test accuracy, dimension 5).**

  | model | SNLI | PREFIX-10% | PREFIX-30% | PREFIX-50% |
  |---|---|---|---|---|
  | fully Euclidean RNN | 79.34 | 89.62 | 81.71 | 72.10 |
  | hyperbolic RNN + FFNN, Euclidean MLR | 79.18 | 96.36 | 87.83 | 76.50 |
  | fully hyperbolic RNN | 78.21 | 96.91 | 87.25 | 62.94 |
  | fully Euclidean GRU | 81.52 | 95.96 | 86.47 | 75.04 |
  | hyperbolic GRU + FFNN, Euclidean MLR | 79.76 | 97.36 | 88.47 | 76.87 |
  | fully hyperbolic GRU | 81.19 | 97.14 | 88.26 | 76.44 |

  The text's error-reduction factors at PREFIX-10% (3.35 for the RNN,
  1.5 for the GRU) recompute from the table as 10.38/3.09 and
  4.04/2.64.
- **Table 2 (test F1, WordNet subtree against the rest, pre-trained
  Poincaré embeddings).** Hyperbolic MLR beats Euclidean MLR on the raw
  coordinates and Euclidean MLR after log₀ in 15 of the 16 subtree and
  dimension settings. Examples: *group.n.01* at dimension 2, 81.7 against
  61.1; *mammal.n.01* at dimension 3, 87.5 against 44.7. The exception is
  *animal.n.01* at dimension 10, 99.26 against 99.36. Intervals are over
  three runs.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Closed forms for exp_x, log_x, geodesics and Möbius scalar multiplication in Dⁿ_c | strong | Lemmas 1–3; checked numerically here |
| C2 | Parallel transport from the origin to x is the scaling λ₀/λ_x | strong (proof) | Theorem 4, Appendix B; re-derived here |
| C3 | Distance to a Poincaré hyperplane has the closed form of Eq. 23 | strong (proof) | Theorem 5, Appendix D; checked numerically in D² |
| C4 | The constructions are "principled" generalisations of MLR, FFNN and GRU | moderate | each recovers the Euclidean case as c → 0 and keeps some algebraic properties; the lift through the origin is a definition, not forced |
| C5 | A stack of Möbius layers without biases is a Euclidean network conjugated by exp₀ | strong | follows from the morphism property; stated in §3.2 |
| C6 | Hyperbolic RNNs and GRUs help most when the data is more tree-like | weak | one synthetic task at three noise levels, best of three runs; at 50% noise the fully hyperbolic RNN is far worse than the Euclidean one |
| C7 | Hyperbolic sentence encoders are on par with Euclidean ones on SNLI | moderate | Table 1; the best SNLI model is Euclidean, and the margins are under 2 points |
| C8 | Hyperbolic MLR classifies WordNet subtrees in Poincaré embeddings better than Euclidean MLR | moderate | Table 2, three runs with intervals; the embeddings were fitted to the full hierarchy, so it is a separability result |
| C9 | Hyperbolic models first arrange directions near the origin, then push norms outward, and accuracy rises with the norms | weak | training curves for some PREFIX-30% runs (Appendix F); no quantification |

## Method

- **Layers.** Linear map: M ⊗_c x = exp₀(M log₀ x). Nonlinearity:
  φ^{⊗c}. Bias: x ⊕_c b, equal to exp_x((λ₀/λ_x) log₀(b)). Concatenation:
  M₁ ⊗ x₁ ⊕ M₂ ⊗ x₂.
- **RNN.** h_{t+1} = φ^{⊗c}(W ⊗ h_t ⊕ U ⊗ x_t ⊕ b); the GRU as above.
- **MLR.** Per class, a point p_k in the ball and a normal
  a_k = (λ₀/λ_{p_k}) a′_k with a′_k Euclidean; logits as in Eq. 25.
- **Pipeline for the sentence tasks.** Two encoders, one per sentence;
  their outputs and squared distance go to a feed-forward layer and then
  MLR, each Euclidean or hyperbolic, with cross-entropy loss. With
  identity in place of tanh and ReLU, the hyperbolic models did slightly
  better, which the authors attribute to the nonlinearity already in the
  layers and to tanh keeping embeddings from the boundary.

## Concepts

- **Möbius addition x ⊕_c y**: Ungar's gyrogroup operation (Eq. 6), not
  commutative or associative, with left cancellation
  (−x) ⊕ (x ⊕ y) = y. The text's "x ⊕_c 0 = 0 ⊕_c x = 0" is a slip for
  "= x", which Eq. 6 gives.
- **Möbius version f^{⊗c}**: exp₀ ∘ f ∘ log₀ (Definition 3.2).
- **Poincaré hyperplane H̃^c_{a,p}**: exp_p({a}^⊥), Ungar's
  hypergyroplane. In the ball picture it is a spherical cap meeting the
  boundary at right angles.
- **Gyro-derivative**: lim (1/δt) ⊗ (−h(t) ⊕ h(t + δt)), after Birman and
  Ungar.
- **PREFIX-Z%**: synthetic pairs from a 100-word vocabulary. The positive
  is a random prefix of the first sentence with Z% of its words replaced;
  the negative is a random sentence of the same length.

## Connections

It is the sequel to the same authors' entailment-cones paper ([LIT-866](../literature.d/LIT-866.md),
[NOTE-671](NOTE-671.md)). From it, this paper takes the closed-form exponential map of
the ball (cited for the proof of Lemma 2), hyperbolic Riemannian SGD, and
the open-source Poincaré-embedding code used for Table 2 (the footnote
points to the cones repository). The two papers ask different things of
the geometry. The cones paper makes an order relation into nested regions
and has no network. This one gives a network the operations of the
space, and its only order-like task, SNLI entailment, is treated as
binary classification of pairs, with no transitivity built in. The cones
are not used.

It cites Sala et al. as "De Sa et al." ([LIT-874](../literature.d/LIT-874.md)) and Gromov and Hamann for
the tree-likeness of hyperbolic space, and Krioukov et al. 2010 ([LIT-865](../literature.d/LIT-865.md))
among embeddings of complex networks. Yang et al. ([LIT-871](../literature.d/LIT-871.md), [NOTE-669](NOTE-669.md)) list
this paper among works that took for granted that training would place
general concepts near the origin; the observation of Appendix F (norms
stay near 0 for a few epochs, then grow) is the kind of evidence they
test more directly. Sharpee 2019 ([LIT-875](../literature.d/LIT-875.md), [NOTE-670](NOTE-670.md)) cites it only as an
instance of hyperbolic representation in machine learning, and nothing in
this paper bears on that perspective's argument.

## Bearing on the record

- **[QUESTION-025](../questions.d/QUESTION-025.md)** asks whether attributes that imply or exclude each
  other in co-occurrence still give linear attribute directions, and a
  concept lattice that is not Boolean. **Not answered.** What this paper
  adds is the hyperbolic counterpart of the object the question is about.
  In [THEORY-185](../theory.d/THEORY-185.md), an attribute is a linear direction and a threshold on it:
  a Euclidean half-space. Here the analogue is a geodesic hyperplane and
  its hyperbolic half-space. Table 2 shows that in Poincaré embeddings
  fitted to WordNet, "being under node X" is close to such a half-space
  (F1 87–99% for three of the four subtrees from dimension 3 up), and in
  low dimensions much closer than to a Euclidean one. Three limits keep
  this from bearing directly:
  - the embedding is trained on hypernym edges, not on co-occurrence;
  - test nodes were in the embedding's training, so separability is
    measured, not generalisation;
  - each subtree's classifier is trained alone, so nothing shows that
    nested subtrees get nested half-spaces, which is what implication
    among attributes would need.

  So it adds a fourth encoding to the three the question already lists
  (Euclidean half-spaces, distances as in [THEORY-196](../theory.d/THEORY-196.md), cones as in
  [THEORY-189](../theory.d/THEORY-189.md)): hyperbolic half-spaces, one per subtree. In the Poincaré
  ball, Euclidean half-spaces do markedly worse at separating subtrees.
  That is evidence that the geometry an attribute direction lives in
  matters once the embedding is hierarchical, my reading of Table 2. A
  measurement for [QUESTION-025](../questions.d/QUESTION-025.md) could probe co-occurrence embeddings for
  both kinds of half-space.
- **Exclusion and meets.** Two hyperbolic half-spaces can be disjoint,
  nested or crossing, so the geometry could express exclusion and
  implication among attributes. The intersection of half-spaces is a
  convex region, unlike the intersection of two cones in [LIT-866](../literature.d/LIT-866.md), but
  the paper does not consider intersections at all. My observation; it
  bears on [CLAIM-119](../claims.d/CLAIM-119.md) only as a possibility. The paper neither supports
  nor tells against that claim.
- **[THEORY-186](../theory.d/THEORY-186.md)** (Saxe et al.: tree-structured features give one linear
  direction per branching in a linear network). A contrast, my
  connection: there, linear directions split sibling subtrees; here a
  subtree is cut off by one curved hyperplane in a space fitted to the
  tree.
- **No THEORY filed.** The mathematical results are closed forms within
  established hyperbolic geometry, true and checked, but not a finding
  about the world that the record lacks. The empirical results are too
  thin to state as one.
- **Anthology.** It is chiefly ML practice: layer design, mixed
  Adam/RSGD optimisation, clipping, identity in place of nonlinearities,
  best-of-three selection. The anthology's `model-architecture` or
  `concept-geometry` topics could hold it. Its clone does not, so the LIT
  carries `anthology-candidate`.

## Limitations

- **The experiments are small.** Dimension 5 only; SNLI and one synthetic
  task; each Table 1 cell is a best-of-three by validation, with no
  variance. The authors note that the Euclidean baselines had Adam and
  the hyperbolic parameters did not, which could cut either way in
  comparing them.
- **"More tree-like" is not measured.** The PREFIX noise level is used as
  a proxy for tree-likeness, with no measure of hyperbolicity (Gromov's δ,
  say) of the data. At 50% noise the fully hyperbolic RNN loses badly, and
  the paper explains this only as noise affecting "representational
  power".
- **Hyperbolic MLR shows no advantage on SNLI**, and the Table 2 test
  that does show one uses embeddings fitted to the labels' own hierarchy.
- **The lift through the origin is a choice.** Its dependence on the
  origin is not discussed, and alternatives (lifting at a learned point,
  or intrinsic operations such as Fréchet means) are not compared.
- **A small slip.** "x ⊕_c 0 = 0 ⊕_c x = 0" should read "= x".

## Open questions

- Whether nested subtrees of a hierarchy get nested hyperbolic
  half-spaces when classifiers are trained jointly, which is what would
  make a hyperbolic half-space an attribute in the sense of a concept
  lattice.
- Whether embeddings learned from co-occurrence, rather than from
  hypernym edges, have subtrees separable by geodesic hyperplanes better
  than by Euclidean ones. That would be a measurement in [QUESTION-025](../questions.d/QUESTION-025.md)'s
  own terms.
- How much of the gain on tree-like data is due to the bias translations
  and the distance-based output, the only places the curvature acts. An
  ablation removing each would show it.
