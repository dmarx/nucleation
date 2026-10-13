---
number: 712
status: Read
formerly:
- NOTE-tmpgyewi
paper: LIT-970
title: 'Symmetry in Neural Network Parameter Spaces'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Read from arXiv v3 (10 December 2025, TMLR) through the PDF text layer:
    §§1–5 and 7–8 in full, §6.1 in full, §6.2 (weight-space learning)
    skimmed. A survey, so the results it reports were not checked against
    the papers it cites. Where a point below rests on a cited paper, the
    paper is named.
date: '2026-10-13'
summary: >-
  A symmetry is a group action on parameters preserving the network
  function (Def. 2.4) or the loss (Def. 2.6), possibly only on given data
  or in expectation (Defs. 2.8–2.9). Common components have GL, scaling,
  sign-flip, orthogonal, translation and permutation symmetries (Table 1).
  Continuous symmetries make minima connected manifolds, and give gradient
  flow conserved quantities that label trajectories and endpoints (§5).
  SGD's finite steps, noise and weight decay break these, which is an open
  route to implicit bias (§7.2).
---

# NOTE-712: Symmetry in Neural Network Parameter Spaces

## Contribution

A unified vocabulary and catalogue. The survey separates symmetries of the
function from symmetries of the loss, and exact ones from data-dependent
and distributional ones. It lists the groups that common components carry,
including transformers. It then collects what follows from them: for
identifiability, for the shape of minima, for optimization algorithms, and
for the conserved quantities of training dynamics.

## Key insight

A continuous symmetry is a direction in which nothing the loss can see
changes. So it is flat in the landscape, and gradient flow never moves
along it. Whatever coordinate measures position along the orbit, such as
the imbalance between adjacent layers, is fixed by the initialization.
Where training ends among equivalent minima is therefore decided by where
it started, unless something that is not gradient flow, such as finite
steps, noise or weight decay, moves it.

## Assumptions

- Symmetries as defined are exact group actions. The relaxed kinds (loss,
  data-dependent, distributional) are weaker and largely unexplored beyond
  single data points (§7.1).
- The conserved quantities of §5 are for gradient flow, the
  infinitesimal-step limit. Under SGD they are not conserved.

## Key results

- **Catalogue (§2.2, Table 1).** Linear: GL(h). Homogeneous activations:
  positive scaling. Tanh: sign flips. Radial rescaling: O(h). Batchnorm:
  positive scaling of incoming weights. Softmax: translation. Pointwise
  activations: permutation. Attention: GL(d_k) per head, with head
  permutation and GL(d_v) in multi-head attention. LoRA: GL(r).
- **Identifiability (§2.4).** The known symmetries are complete for
  Gaussian RBF and tanh networks under stated conditions (Sussmann 1992;
  Fefferman & Markel 1993). ReLU networks can have hidden symmetries, and
  functional dimension can vary within a fiber (Grigsby et al. 2023,
  2025). For two-layer ReLU networks, permutation and scaling suffice
  outside a degenerate case (Petzka et al. 2020).
- **Landscape (§3).** Continuous symmetries make positive-dimensional
  minima, which explains some mode connectivity. The survey says not all
  points of a minimum are related by symmetry, and connectivity may have
  other mechanisms. Removing permutation and scaling makes networks more
  linearly mode connected (Lim et al. 2024b).
- **Conserved quantities (§5.1).** Imbalance, W_h W_hᵀ − W_{h+1}ᵀ W_{h+1},
  is conserved in linear networks (Arora et al. 2018b). Neuron-wise
  norm differences are conserved with homogeneous activations (Du et al.
  2018). For matrix factorization there are no other independent
  conservation laws (Marcotte et al. 2023).
- **Symmetry breaking by SGD (§5.2).** Imbalance decreases exponentially
  with large learning rates (Kunin et al. 2021, *Neural Mechanics*).
  For losses with a rescaling symmetry, the stationary distribution of SGD
  is biased toward balanced solutions, "different from predictions from a
  Langevin model" (Ziyin et al. 2023a). Mirror symmetries impose
  constraints that large weight decay or gradient noise favours (Ziyin
  2024).
- **Data symmetry (§6.1).** In two-layer ReLU networks, a G-invariant
  dataset makes the gradient equivariant, so an initialization with the
  data's symmetry keeps it throughout gradient descent.

## Claims

- Parameter symmetry is "a valuable, underexplored perspective" that
  "complements existing theory". As a survey it argues this by collection,
  not by a new result.

## Concepts

- **Fiber:** the set of parameters realizing one function. A symmetry
  group is complete when it acts transitively on every fiber.
- **Orbit:** the parameters a symmetry group reaches from one point.
- **Conserved quantity:** a function of parameters constant along gradient
  flow, whose gradient is tangent to the loss level set.
- **Intertwiner group:** the transformations an activation commutes with.
  It is the symmetry of both the parameters and the hidden
  representations (Godfrey et al. 2022).

## Connections

- **[THEORY-209](../theory.d/THEORY-209.md) (Kunin et al.).** The limiting-dynamics model is silent on
  the Hessian's null space, where the symmetries' flat directions lie.
  This survey says what happens there under gradient flow (nothing moves)
  and, secondhand, under SGD (conserved quantities drift toward balance,
  by a bias a Langevin model does not predict).
- **[THEORY-184](../theory.d/THEORY-184.md).** Coincident neurons stay coincident under a
  permutation-equivariant update. The survey's §6.1 gives a parallel:
  symmetry shared by data and initialization is preserved.
- **[THEORY-112](../theory.d/THEORY-112.md) and [CLAIM-263](../claims.d/CLAIM-263.md).** [CLAIM-263](../claims.d/CLAIM-263.md)'s protocol of quotienting the
  full symmetry group needs the group to be known. The survey's catalogue and its
  completeness results say when it is.
- **[QUESTION-058](../questions.d/QUESTION-058.md)** asks how much of a representation's group structure
  comes from the update's symmetry. The intertwiner group (§6.1) is where
  parameter symmetry and representation symmetry coincide.

## Bearing on the record

It fills [THEORY-209](../theory.d/THEORY-209.md)'s null-space gap with an account of its own, filed as
[THEORY-210](../theory.d/THEORY-210.md), which answers [QUESTION-069](../questions.d/QUESTION-069.md) in part. Continuous symmetry is
one source of connectivity, and the position along a symmetry orbit is set
by the initialization and the optimizer's symmetry breaking, not by the
loss.

## Limitations

- **Secondhand.** Every dynamical result is the cited papers'. The SGD
  results (Kunin et al. 2021; Ziyin et al. 2023a; Ziyin 2024) are not
  held in this record.
- **Gradient flow, mostly.** The conserved-quantity results are for
  infinitesimal steps. The survey itself names their fate under SGD as
  open (§7.2).
- **Layer-local.** The catalogued symmetries act on adjacent layers. The
  survey notes that global symmetries across non-adjacent layers may be
  missed (§7.1).

## Open questions

- How fast, and toward what, does SGD drift conserved quantities at the
  end of training, and is that drift the null-space half of the limiting
  dynamics?
- Are hidden ReLU symmetries common enough in trained networks to matter
  for alignment protocols?

## Corrections

The Deferred entry's seed said the survey "widens" [QUESTION-058](../questions.d/QUESTION-058.md)'s "source
called the symmetry of the update beyond the single permutation result in
[THEORY-184](../theory.d/THEORY-184.md)". The reading confirms that.
