---
status: Proposed
title: 'A function-preserving rescaling of a ReLU network''s hidden units, taken as a disruption of its learned state, is exactly a change of the optimizer''s per-coordinate step sizes on the original parameters, so the two arms of a crossed intervention are not separated by anything the network computes'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed 2026-11-23 by the assistant, from the lead run of that date,
    where the rescaling was one of the learned-state disruptions.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the identity below: a positive rescaling c of hidden units
  under which gradient descent, sign descent or Adam (with ε → 0) on the
  rescaled parameters does not trace, in the original coordinates, the
  same function-space path as the same optimizer with step sizes divided
  by c² (input side) and multiplied by c² (output side) for gradient
  descent, or divided by c and multiplied by c for sign descent and Adam.
tags:
- learning-theory
- mathematics
date: '2026-11-23'
line:
- learned-structure
- formal-apparatus
bears_on:
- QUESTION-122
grounds:
- CASE-tmphp4pt
summary: >-
  For a ReLU unit, scaling its input weights and bias by c > 0 and its
  output weight by 1/c leaves the network's function unchanged. The
  gradients scale inversely, so one step of gradient descent at step size
  η on the rescaled weights is, written in the original weights, a step of
  size η/c² on the input side and ηc² on the output side; for sign descent
  and Adam, which ignore the gradient's scale, η/c and ηc. The same
  function, the same data and the same optimizer family; only the
  optimizer's coordinate-wise step sizes differ. A crossed intervention
  that counts this disruption as the network's arm and an optimizer change
  as the other arm is assigning one thing to two arms by a choice of
  coordinates. It is checked exactly in the run's tests
  ([CASE-tmphp4pt](../cases.d/CASE-tmphp4pt.md)). The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmphp4pt — new; the study filed by the lead run of 2026-11-23 -->

# CLAIM-tmp2k67n: A function-preserving rescaling of a ReLU network's hidden units, taken as a disruption of its learned state, is exactly a change of the optimizer's per-coordinate step sizes on the original parameters, so the two arms of a crossed intervention are not separated by anything the network computes

## The claim

Let hidden unit i compute h_i = relu(w_iᵀx + b_i) and contribute v_i h_i
to the output. For c_i > 0, set w′_i = c_i w_i, b′_i = c_i b_i,
v′_i = v_i / c_i. Since relu(c z) = c relu(z), the function is unchanged.
The gradients satisfy ∂L/∂w′_i = (∂L/∂w_i)/c_i and ∂L/∂v′_i = c_i ∂L/∂v_i.

- **Gradient descent.** w′_i ← w′_i − η ∂L/∂w′_i is, in the original
  coordinates, w_i ← w_i − (η/c_i²) ∂L/∂w_i, and v_i ← v_i − η c_i² ∂L/∂v_i.
- **Sign descent.** The sign of a gradient is unchanged by a positive
  factor, so the step is w_i ← w_i − (η/c_i) sign(∂L/∂w_i) and
  v_i ← v_i − η c_i sign(∂L/∂v_i).
- **Adam.** Its update is invariant to a fixed positive scaling of each
  gradient coordinate, up to ε, so the same as sign descent's: η/c_i and
  η c_i.

In each case, the rescaled network under the optimizer is the original
network under the same optimizer with different per-coordinate step
sizes, and the two trace the same path in function space. The test
`test_sgd_on_rescaled_equals_preconditioned_sgd_on_original` in
scratch/studies/lead-105/ checks the gradient-descent case to 10⁻⁹ over a
hundred steps.

[CASE-113](../cases.d/CASE-113.md)'s crossed design reads a change in the network's response
under "disrupt a learned state, hold the optimizer fixed" as evidence that
the regulation sits in the network. This disruption leaves everything the
network computes unchanged and is an optimizer change in other
coordinates. Which arm it belongs to is decided by the parameterization,
not by the network. It is the same kind of fact as [CLAIM-366](CLAIM-366.md)'s: the
sign of a gradient inner product, and here the assignment of an
intervention to network or optimizer, is not invariant under
reparameterization.

For a crossed design to separate the arms, its learned-state disruptions
must change what the network computes (as ablation does) or be stated in
coordinates fixed in advance.

## What it does not say

- That the rescaling changed the response much here. In the run it left
  task A's forgetting unchanged within its intervals and changed only the
  relearning time.
- That disruptions which change the function are optimizer changes. An
  ablation is not.
- That the network and the optimizer are one thing. The function belongs
  to the network; how parameter coordinates are scaled against step sizes
  belongs to neither alone.

## Note of 2026-11-23: Lippl and Lindsey, read
<!-- inactive-ok-file: CLAIM-tmp7n00e CLAIM-tmpew899 THEORY-tmpw69kb — Proposed or new; filed by the lead run of 2026-11-23 -->

Its identity applies exactly to Lippl and Lindsey's technique of
rescaling the weights after pretraining (THEORY-tmpw69kb; NOTE-tmpw2i45),
which they present as part of fine-tuning. CLAIM-tmpew899 rests on it to
read the case of CLAIM-tmp7n00e as one learner under two procedures. No
status change.
