---
number: 210
status: Proposed
formerly:
- THEORY-tmpvl6ed
promote_when: >-
  The SGD half measured in a deep network trained on real data. The
  dynamical sources are now read first-hand: Neural Mechanics
  (LIT-1013) for the conservation laws and their breaking by weight
  decay and finite steps, and Ziyin et al. (LIT-1012) for the law of
  balance under minibatch noise. What would promote: drift of imbalance, or
  of another symmetry's conserved quantity, during the limiting dynamics of
  a deep network, toward the balanced value these results predict, at
  rates set by weight decay and by learning rate over batch size. What
  would refute it: a trained deep network whose position along a
  continuous symmetry orbit is determined by the loss alone, the same
  across initializations and optimizers. More catalogues of symmetries
  cannot settle it.
title: 'Continuous parameter symmetries stretch a network''s minima into connected manifolds along which the loss is flat, and give gradient flow conserved quantities that fix where on such a manifold training ends; finite steps, gradient noise and weight decay break them, so the position along a symmetry orbit is set by initialization and optimizer, not by the loss'
version: 2
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Filed from the reading of the LIT-970 survey, with its dynamical results
    secondhand.
- version: 2
  date: '2026-10-13'
  note: >-
    After reading the two sources the survey reported. Neural Mechanics
    (LIT-1013) and Ziyin et al. (LIT-1012) added as sources. One
    attribution corrected: the survey's "imbalance decays exponentially
    with large learning rates" is not found in Neural Mechanics, whose main
    text attributes the exponential decay of the norm difference to weight
    decay large enough to dominate. The Langevin comparison is restated:
    Ziyin et al. compare SGD with isotropic noise, not with THEORY-209's
    model. The claim is unchanged. promote_when is rewritten, since the
    reading it asked for is done.
tags:
- loss-landscapes
- learning-theory
- anthology-candidate
date: '2026-10-13'
source:
- LIT-970
- LIT-1013
- LIT-1012
summary: >-
  Zhao, Walters & Yu (2025), [LIT-970](../literature.d/LIT-970.md), read in [NOTE-712](../notes.d/NOTE-712.md): a survey,
  so the dynamical results are secondhand. Continuous parameter-space
  symmetries (GL, scaling, orthogonal, translation) make minima
  positive-dimensional and connected, which is one source of mode
  connectivity. Under gradient flow each gives a conserved quantity, such
  as layer imbalance, that is fixed by initialization and locates the
  endpoint on the manifold. Under SGD these are not conserved. Read
  first-hand (Neural Mechanics; Ziyin et al.), weight decay drives the
  conserved quantities toward zero, and minibatch noise drives a rescaling
  symmetry's toward the point where the layers' gradient noise balances.
  The survey had reported this as imbalance decaying with large learning
  rates, and a stationary distribution biased toward balanced solutions
  that a Langevin model does not predict. This is the null-space half
  that [THEORY-209](THEORY-209.md)'s limiting dynamics leave out. Proposed: one survey,
  with the SGD results unread here.
bears_on:
- QUESTION-058
- QUESTION-069
---

# THEORY-210: Continuous parameter symmetries stretch a network's minima into connected manifolds along which the loss is flat, and give gradient flow conserved quantities that fix where on such a manifold training ends; finite steps, gradient noise and weight decay break them, so the position along a symmetry orbit is set by initialization and optimizer, not by the loss

## Source

Zhao, Walters & Yu (2025), [LIT-970](../literature.d/LIT-970.md), read in [NOTE-712](../notes.d/NOTE-712.md): §§1–5 and 7–8,
and §6.1. It is a survey. The dynamical results below are the cited
papers', reported by the survey and not read here.

## The claim

**Symmetry makes flat, connected minima.** A continuous symmetry is a Lie
group acting on parameters without changing the loss. Its orbits are
positive-dimensional, so a minimum is a manifold, not a point. If
independently trained minima are related by an element of the group's
identity component, they are connected at constant loss (§3.1). This is
one source of mode connectivity. The survey states that it is not the
only one, and that not all points of a minimum are related by symmetry.

**Under gradient flow, position on the orbit is conserved.** Each
continuous symmetry gives a conserved quantity of gradient flow. Its
gradient is tangent to the loss level set. In linear networks it is the
imbalance W_h W_hᵀ − W_{h+1}ᵀ W_{h+1}. With homogeneous activations it is
each neuron's difference of incoming and outgoing squared norms (§5.1).
These are fixed by the initialization and label the endpoint among the
equivalent minima (§5.2). So, under gradient flow, where training ends
along a symmetry orbit is decided at initialization.

**Under SGD it is not.** Finite steps, gradient noise and weight decay
break the conservation laws. Read first-hand, there are three effects:

- **Weight decay pulls toward zero.** In Neural Mechanics ([LIT-1013](../literature.d/LIT-1013.md))
  each quantity decays as an exponential memory of its initial value. For
  rescale symmetry, "for large enough weight decay", the norm difference
  decays exponentially to zero.
- **Finite steps push outward.** For scale symmetry, discretization
  pushes the norm out, against weight decay's pull (Neural Mechanics,
  Eq. 21).
- **Minibatch noise balances.** The noise has no component along a
  symmetry, but its dependence on the parameters drives ‖u‖² − ‖w‖²
  toward the point where the two groups' gradient noise is equal, at a
  rate proportional to η/S (Ziyin et al., [LIT-1012](../literature.d/LIT-1012.md); [THEORY-211](THEORY-211.md)).
  The stationary distribution then differs from what gradient descent with
  isotropic noise would give, which diffuses along the orbit.

The survey's version of the first point, "imbalance decays exponentially
with large learning rates", is not found in Neural Mechanics; see the
history note.

On this account, the position along a symmetry orbit at the end of
training is set by the initialization and by how the optimizer breaks the
symmetry.

## What it bears on

- **[QUESTION-069](../questions.d/QUESTION-069.md)** asks whether the connectedness of trained solutions
  belongs to the solutions or to the instrument, history and regime. This
  account gives one mechanism on the solutions' side: continuous
  symmetry. Where solutions sit within a connected set depends on the
  history (initialization) and the regime (optimizer).
- **[QUESTION-058](../questions.d/QUESTION-058.md)** asks how much of a representation's group structure
  comes from the update's symmetry. The survey's intertwiner group is the
  symmetry shared by parameters and hidden representations. A symmetry
  shared by data and initialization is preserved by gradient descent in
  two-layer ReLU networks (§6.1).
- **[THEORY-209](THEORY-209.md)** models the end of training as Langevin dynamics on a
  quadratic loss, and is silent on the Hessian's null space. The flat
  directions this account describes are in that null space. Read
  first-hand, [THEORY-209](THEORY-209.md)'s model and the SGD results disagree there, for
  an identified reason. [THEORY-209](THEORY-209.md)'s
  noise covariance is independent of the parameters, which freezes the
  coordinate along a symmetry. [THEORY-211](THEORY-211.md)'s balancing drift comes from
  exactly that dependence.

## What this does not say

- It does not say all connectivity is symmetry. The survey says
  otherwise.
- It does not establish the SGD results in deep networks trained on real
  data. They are now read first-hand, but the evidence is VGG-16 with
  recorded gradients (Neural Mechanics) and small synthetic networks (Ziyin
  et al.).
- It does not cover hidden ReLU symmetries or global symmetries across
  non-adjacent layers, which the survey names as open (§§2.4, 7.1).
- It does not instruct. Teleportation and symmetry-invariant optimizers
  (§4) are practice, and belong to the anthology.
