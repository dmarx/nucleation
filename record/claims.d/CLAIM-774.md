---
number: 774
status: Proposed
formerly:
- CLAIM-tmpmugkp
title: 'Spectral descent learns weakest modes first'
statement: >-
  In a two-layer linear network learning from small weights, steepest
  descent in the spectral norm, which moves every singular direction of each
  layer at the same rate, learns the modes of the input–output correlation
  in a time proportional to the square root of their strength, weakest
  first, where gradient descent learns them in a time proportional to the
  inverse of their strength, strongest first: equalizing rates within a
  layer reverses and compresses the staged hierarchy of learning rather than
  removing it
version: 3
history:
- version: 2
  date: '2026-11-20'
  note: >-
    A dated note: this claim is about the order of learning in training
    time and does not bear on what a network's depth organizes. No change
    of status or title.
- version: 3
  date: '2026-11-21'
  note: >-
    A dated note: the modular duality reading confirms the update rule and
    names three qualifications. No change of status or title.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: in the gradient being diagonal in the
  singular bases of the target under a decoupled, aligned, balanced
  start; in the polar factor of such a gradient being the sign of each
  diagonal entry; or in the product of two factors each growing by the
  learning rate per step reaching s/2 at t = √(s/2)/lr. Or, outside that
  start, a two-layer linear network from small random weights in which
  orthogonalized updates learn stronger modes first.
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-20'
line:
- learned-structure
- formal-apparatus
grounds:
- THEORY-186
- THEORY-740
summary: >-
  The owner asked (2026-11-20) whether the record's rate-difference and
  time-scale results connect to μP depth scaling and the modular duality
  program. One link is within a layer: modular dualization of a linear
  layer ([LIT-2952](../literature.d/LIT-2952.md)) is steepest descent in the spectral norm, whose
  update is the polar factor of the gradient, the same unit step in every
  singular direction. Saxe's deep linear dynamics ([THEORY-186](../theory.d/THEORY-186.md), [THEORY-740](../theory.d/THEORY-740.md))
  learn modes in order of strength because gradient descent moves each at
  a rate set by its strength. With the rates equalized, the order is set
  by how far each mode must travel instead: weakest first, in time ∝ √s.
  Derived and checked by simulation. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-2191 — Proposed; the reading of Lee et al. filed 2026-11-22 -->
<!-- inactive-ok-file: THEORY-2136 THEORY-2139 — Proposed, Unfetched or new; filed in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-771 CLAIM-767 — Proposed; the claims on depth this note points to -->
<!-- inactive-ok-file: CLAIM-781 CLAIM-478 THEORY-186 — Proposed, Deferred or Open; the work this applies and the claims it bears on -->

# CLAIM-774: Spectral descent learns weakest modes first

## The claim

Let a network f(x) = W₂W₁x learn the input–output correlation
Σ = U diag(s) Vᵀ on whitened inputs, with loss ½‖Σ − W₂W₁‖², from small
weights.

**Gradient descent** ([THEORY-186](../theory.d/THEORY-186.md), [THEORY-740](../theory.d/THEORY-740.md), Saxe and colleagues): from a
decoupled, balanced start each mode's strength rises logistically after a wait
of order (1/s)·log(1/ε₀), so modes arrive strongest first.

**Steepest descent in the spectral norm.** The update for each layer is
−lr·polar(G), where G is the layer's gradient and polar(G) = PQᵀ for G = PDQᵀ:
every nonzero singular direction of the gradient moves by the same amount, lr.
This is the duality map for the spectral norm, which modular dualization
assigns to linear layers ([LIT-2952](../literature.d/LIT-2952.md)).

**Derivation.** From a decoupled, aligned, balanced start, W₁ = diag(a)Vᵀ and
W₂ = U diag(a) in the target's bases, the gradients are diagonal in the same
bases, with entries −a_α(s_α − a_α²), negative for every mode below its target.
Their polar factor is minus the identity on those modes, so every such mode's
factor grows by lr per step: a_α(t) = a₀ + lr·t. Its strength a_α² reaches half
its target at

  t½ = √(s_α/2)/lr,

proportional to √s, so weaker modes arrive first. Over a range of strengths
s_max/s_min = r, gradient descent spreads arrival times by about r (times a
logarithmic factor), and the spectral update by √r, in the opposite order.

## Check

Simulated with a random small start (scale 10⁻³), not the aligned one, d = 8,
targets s = 8, 4, 2, 1 and four zero modes, lr = 0.01 (script in the curation
entry of 2026-11-20, 234553). Steps to half-learn each mode:

| Update | s = 8 | s = 4 | s = 2 | s = 1 |
|---|---|---|---|---|
| gradient descent | 95 | 179 | 345 | 617 |
| polar (spectral) | 200 | 141 | 100 | 70 |

√(s/2)/lr gives 200, 141, 100 and 71. With lr = 0.003 the polar times scaled to
666, 470, 333 and 235, as 1/lr predicts.

## What it bears on

- **Rate differences within a layer.** [CLAIM-781](CLAIM-781.md) and [CLAIM-478](CLAIM-478.md) (version
  5) say a hierarchy shows where rate differences between levels beat the
  spread within. Gradient descent's staged learning is a hierarchy in training
  time made by rate differences between modes. Equalizing the rates does not
  flatten it to one level: it leaves a hierarchy set by distance, compressed
  from a spread of r to √r and reversed. By the between-against-within test,
  its levels are harder to resolve.
- **Progressive differentiation.** Saxe and colleagues read the staged order
  as coarse-to-fine learning of a hierarchy of categories ([THEORY-186](../theory.d/THEORY-186.md)). On
  this claim, a network trained with orthogonalized updates would show it
  weakly or reversed. Whether real networks do is [QUESTION-502](../questions.d/QUESTION-502.md).

## What it does not say

- Not that it holds with momentum, noise, nonlinearity or depth beyond two.
  The deep-linear generalization is likely (each of k factors grows by lr per
  step, so strength ∝ t^k and t½ ∝ s^(1/k)) but was not checked.
- Not that modes with zero target behave: under polar updates they oscillate
  at amplitude of order lr, and a learned mode overshoots by of order lr,
  unless the rate decays.
- Nothing about which optimizer to use. It describes the order in which a
  linear network learns, not what anyone should do.

## Note of 2026-11-20: not a claim about depth

The owner first read this claim as evidence against transformer depth
corresponding to a hierarchy. It is not evidence either way. It concerns the
order in which a two-layer network's modes are learned over training time,
under two update rules; it says nothing about what successive layers of a
deep network represent. A network could learn its modes in any order and
still arrange its layers as a hierarchy, or learn coarse to fine without
one. What bears on depth is [CLAIM-767](CLAIM-767.md), and the claim filed on depth is
[CLAIM-771](CLAIM-771.md). Cite this claim for depth only with that caution.

## Note of 2026-11-21: modular duality read

Bernstein and Newhouse ([THEORY-2136](../theory.d/THEORY-2136.md), read in [NOTE-2232](../notes.d/NOTE-2232.md)) confirm that modular dualization of a linear layer is the polar factor scaled by √(d_out/d_in), 1 for this claim's square layers, with every singular value of the update the same. Three qualifications: the derivation uses the fixed-rate update of their eq. 2, not the exact steepest step of their Proposition 1, which scales by the gradient's dual norm (the weakest-first order should survive, since every mode still gets the same step); practical updates use Newton–Schulz, exact only in the limit; and non-square layers or unequal masses give the two layers unequal steps. The paper says nothing about the order of learning. The spectral-condition paper ([THEORY-2139](../theory.d/THEORY-2139.md)) rescales gradients without changing their spectrum, so it does not bear on this claim.

## Note of 2026-11-22: Lee, Smith, Adam and Hoogland, read

Background. Lee et al.'s analytic influence ([THEORY-2191](../theory.d/THEORY-2191.md)) is computed
in the same two-layer linear network under gradient flow, through each
mode's time-dependent strength. Under this claim's spectral-norm descent
the modes' timing changes, so the timing of their influence peaks would
too; the paper does not consider other optimizers.
