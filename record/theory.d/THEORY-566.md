---
number: 566
status: Active
formerly:
- THEORY-tmpka1qg
title: 'In Ganea et al.''s hyperbolic neural networks, linear maps and nonlinearities are Euclidean ones read through the chart at the origin, so a stack of them without biases is a Euclidean network conjugated by that chart, and the curvature acts only through the bias translations and the distance-based output layer'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Promoted from Proposed to Active at the owner's direction, carrying out
    the promotion audit's decision for THEORY-566 (batch 027, ADR-047). The
    title is a structural fact about the construction, which the promote_when
    itself called settled. It is re-derived in the note of 2026-10-19 below.
    The promote_when asked for an ablation tying the networks' gains to the
    two operations, which the title does not claim and the body disclaims. It
    moves, unchanged, to QUESTION-162.
tags:
- representation-learning
- mathematics
- anthology-candidate
date: '2026-10-16'
source:
- LIT-879
summary: >-
  Ganea, Bécigneul & Hofmann (2018), [LIT-879](../literature.d/LIT-879.md), read in [NOTE-686](../notes.d/NOTE-686.md), which checked
  the closed forms numerically. Möbius layers are defined as exp₀ ∘ f ∘ log₀,
  so any composition of them is exp₀ ∘ (the Euclidean composition) ∘ log₀,
  as the paper notes; only the Möbius bias, which is parallel transport
  from the origin followed by the exponential map, and the hyperbolic
  logistic regression's distances to geodesic hyperplanes are not absorbed
  by the chart. The structural fact is proved; that the networks' gains,
  confined to a synthetic task and to separating WordNet subtrees in
  low-dimensional Poincaré embeddings, come from those two operations is
  this record's inference. [NOTE-686](../notes.d/NOTE-686.md) filed no THEORY.
---
<!-- inactive-ok-file: THEORY-421 — Proposed; neighbouring accounts of attribute directions, cones and radial hierarchy, named, not leaned on -->

# THEORY-566: In Ganea et al.'s hyperbolic neural networks, linear maps and nonlinearities are Euclidean ones read through the chart at the origin, so a stack of them without biases is a Euclidean network conjugated by that chart, and the curvature acts only through the bias translations and the distance-based output layer

## Source

Ganea, Bécigneul & Hofmann (2018), [LIT-879](../literature.d/LIT-879.md) (NeurIPS 2018), read in full in
[NOTE-686](../notes.d/NOTE-686.md). The reader checked Lemmas 2–3, Eq. 15 and Theorems 4–5
numerically and re-derived Theorem 4. [NOTE-686](../notes.d/NOTE-686.md) filed no THEORY: it judged
the closed forms established geometry and the experiments too thin. This
account states the structural point the reading found (its Key insight
and claim C5, rated strong), which is what the record lacks, and files it
Proposed because the part that would make it matter is an inference.

## What was actually shown

**The lift.** A map f between Euclidean spaces is lifted to the Poincaré
ball of curvature −c as its "Möbius version" f^{⊗c} = exp₀ ∘ f ∘ log₀
(Definition 3.2). That covers matrix multiplication and pointwise
nonlinearities. Möbius scalar multiplication has this form (Lemma 3), which
motivates the definition; nothing forces it. The paper notes the
consequence itself (§3.2): a composition of lifted maps is
exp₀ ∘ (the Euclidean composition) ∘ log₀.

**Where the chart cannot absorb the geometry.** The bias x ⊕_c b equals
exp_x((λ₀/λ_x) log₀(b)), parallel transport of log₀(b) from the origin to x
followed by the exponential map at x (Theorem 4 gives the transport as the
scaling λ₀/λ_x). The output layer's logits are hyperbolic distances to
geodesic hyperplanes exp_p({a}^⊥), in closed form (Theorem 5). Every
operation recovers its Euclidean counterpart as c → 0.

**What the experiments show.** All at dimension 5, each cell a best of
three runs. On SNLI, hyperbolic and Euclidean encoders score 78.2–81.5%,
with a Euclidean GRU best. On a synthetic noisy-prefix task, hyperbolic
models win most at 10% noise (error 3.1% against 10.4% for the RNN), and at
50% noise the fully hyperbolic RNN is worst (62.9% against 72.1%). In
pre-trained Poincaré embeddings of WordNet, hyperbolic logistic regression
separates subtrees better than Euclidean in 15 of 16 settings, most at 2–5
dimensions (Table 2).

## What this does not say

- **That the networks are Euclidean.** With biases and the hyperbolic
  output layer they are not, and those are the parts the account names.
- **That the gains come from the two operations.** No ablation removes
  either; that is this record's inference, and the promote_when.
- **That the lift is canonical.** It privileges the origin: translating
  the inputs by an isometry does not commute with it. Lifting at a
  learned point, or intrinsic operations such as Fréchet means, are not
  compared.
- **That hyperbolic networks help on tree-like data in general.** The
  gains are on one synthetic task whose tree-likeness is not measured, and
  on embeddings fitted to the hierarchy being classified, test nodes
  included, which measures separability, not generalisation.
- **That nested subtrees get nested half-spaces.** Each subtree's
  classifier is trained alone.

## Connections

- **[QUESTION-025](../questions.d/QUESTION-025.md)** lists encodings of hierarchy. This paper adds one,
  hyperbolic half-spaces, one per subtree, the analogue of a Euclidean
  attribute direction with a threshold ([THEORY-185](THEORY-185.md)). It does not answer
  the question ([NOTE-686](../notes.d/NOTE-686.md)).
- **[THEORY-189](THEORY-189.md)** is the same authors' entailment cones ([LIT-866](../literature.d/LIT-866.md)), which
  make an order relation into nested regions. This paper uses the cones
  paper's exponential map and optimiser, not its cones.
- **[THEORY-421](THEORY-421.md)** (Yang et al., [LIT-871](../literature.d/LIT-871.md)) names this paper among those
  that assumed training would place general concepts near the origin.

## Note of 2026-10-19: the composition argument

Carried out for the promotion audit's batch 027. On the Poincaré ball of
curvature −c, exp₀(v) = tanh(√c‖v‖) v/(√c‖v‖) maps ℝⁿ onto the open ball,
and log₀(y) = artanh(√c‖y‖) y/(√c‖y‖) is its inverse. A lifted map is
f^{⊗c} = exp₀ ∘ f ∘ log₀, so g^{⊗c} ∘ f^{⊗c} = exp₀ ∘ g ∘ f ∘ log₀, and by
induction a stack of lifted layers is exp₀ ∘ (the Euclidean composition) ∘
log₀. The Euclidean network inside does not depend on c. In the chart the
bias is F_b(v) = log₀(exp₀(v) ⊕_c b), which by Theorem 4 is a c-dependent
map, and reduces to v + b only as c → 0. The output layer's logits are
distances to geodesic hyperplanes, in closed form with c (Theorem 5).

"Conjugated" is meant in this sense. Any map on the ball can be written as
exp₀ ∘ F ∘ log₀ for some F. The content is that, for the lifted layers, F
is the standard c-free layer, while for the bias and the output layer it is
a c-dependent map. Whether the networks' gains come from those two
operations is [QUESTION-162](../questions.d/QUESTION-162.md).
