---
number: 210
status: Proposed
formerly:
- THEORY-tmpvl6ed
promote_when: >-
  A first-hand reading of the dynamical results the survey reports,
  enough to say what SGD does along symmetry orbits: Kunin et al. (2021),
  Neural Mechanics, on the drift of conserved quantities under finite
  steps and noise; Ziyin et al. (2023a), on SGD's stationary distribution
  under a rescaling symmetry; or Marcotte et al. (2023), on the count of
  independent conservation laws. What would promote: measured drift of
  imbalance, or of another symmetry's conserved quantity, during the
  limiting dynamics of a deep network, toward the balanced value these
  results predict and away from where a Langevin model on the quadratic
  loss would leave it. What would refute it: a trained deep network whose
  position along a continuous symmetry orbit is determined by the loss
  alone, the same across initializations and optimizers. More catalogues
  of symmetries cannot settle it.
title: 'Continuous parameter symmetries stretch a network''s minima into connected manifolds along which the loss is flat, and give gradient flow conserved quantities that fix where on such a manifold training ends; finite steps, gradient noise and weight decay break them, so the position along a symmetry orbit is set by initialization and optimizer, not by the loss'
version: 1
tags:
- loss-landscapes
- learning-theory
- anthology-candidate
date: '2026-10-13'
source:
- LIT-970
answers:
- QUESTION-069
- QUESTION-058
summary: >-
  Zhao, Walters & Yu (2025), [LIT-970](../literature.d/LIT-970.md), read in [NOTE-712](../notes.d/NOTE-712.md): a survey,
  so the dynamical results are secondhand. Continuous parameter-space
  symmetries (GL, scaling, orthogonal, translation) make minima
  positive-dimensional and connected, which is one source of mode
  connectivity. Under gradient flow each gives a conserved quantity, such
  as layer imbalance, that is fixed by initialization and locates the
  endpoint on the manifold. Under SGD these are not conserved. The
  results the survey cites find imbalance decaying with large learning
  rates, and a stationary distribution biased toward balanced solutions
  that a Langevin model does not predict. This is the null-space half
  that [THEORY-209](THEORY-209.md)'s limiting dynamics leave out. Proposed: one survey,
  with the SGD results unread here.
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
break the conservation laws. The survey reports three results:

- imbalance decays exponentially with large learning rates (Kunin et al.
  2021, *Neural Mechanics*);
- with a rescaling symmetry, SGD's stationary distribution is biased
  toward balanced solutions, "different from predictions from a Langevin
  model" (Ziyin et al. 2023a);
- large weight decay or noise favours the constraints that mirror
  symmetries impose (Ziyin 2024).

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
  directions this account describes are in that null space. The result
  reported from Ziyin et al. says that along them SGD's stationary
  behaviour is not what a Langevin model predicts. So the two accounts
  describe complementary halves of the limiting dynamics, and they may
  disagree about the null-space half.

## What this does not say

- It does not say all connectivity is symmetry. The survey says
  otherwise.
- It does not establish the SGD results. They are reported, not read.
- It does not cover hidden ReLU symmetries or global symmetries across
  non-adjacent layers, which the survey names as open (§§2.4, 7.1).
- It does not instruct. Teleportation and symmetry-invariant optimizers
  (§4) are practice, and belong to the anthology.
