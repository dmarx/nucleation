---
status: Proposed
title: 'The deep-versus-shallow learning results separate three effects that aggregate loss conflates: a larger realizable function class, a larger set reachable within a fixed data and compute budget, and a different internal organization with the same attainable outcomes; the deep linear results show the third, the random-hierarchy results the second, and the depth-separation result for products of inputs the first, at fixed size'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that the cases are misassigned in a way that collapses the
  distinction: that the random-hierarchy advantage at the sizes studied
  is one of realizable class and not of sample budget, so that no held
  result shows the second effect apart from the first; or that the deep
  and shallow linear networks end training attaining different outcomes,
  so that no held result shows the third apart from the second. Not
  defeated by finding that one result shows two effects at different
  budgets, which the claim expects.
tags:
- learning-theory
- representation-learning
- individuation
date: '2026-10-18'
line:
- learned-structure
grounds:
- THEORY-186
- THEORY-187
- THEORY-195
- THEORY-200
- THEORY-206
summary: >-
  The owner's, U38 of the exchange of 2026-10-17, on A37's proposed
  experiment: "I think we may already have an empirical demonstration that
  would be useful here in the wide vs deep literature." A38 refined it into
  three effects, (A) enlarged realizable function class, (B) enlarged
  budgeted reachable set, (C) new internal organization without better
  attainable outcomes, filed Saxe et al. under C and the random hierarchy
  model under B, and said A "needs a separately established expressivity
  restriction". The record has one: Rolnick and Tegmark (THEORY-206), a
  separation at fixed neuron count. The sharp edge: which effect a result
  shows depends on the budget, and A38 warned against "depth produces
  individuation while width merely provides redundant capacity".
---

# CLAIM-tmppk4ya: The deep-versus-shallow learning results separate three effects that aggregate loss conflates: a larger realizable function class, a larger set reachable within a fixed data and compute budget, and a different internal organization with the same attainable outcomes; the deep linear results show the third, the random-hierarchy results the second, and the depth-separation result for products of inputs the first, at fixed size

## The claim

A37 proposed an experiment comparing learning systems "that have the same
initial tasks and broadly comparable capacity" but differ in how they
revise authority and reorganize representations. The owner, at U38: "I
think we may already have an empirical demonstration that would be useful
here in the wide vs deep literature."

A38 agreed and split what such a result can show:

- "**Effect A: Enlarged realizable function class.** A new architecture
  makes solutions expressible that the old architecture could not express."
- "**Effect B: Enlarged *budgeted* reachable set.** Both architectures
  could, in principle, express the desired function, but one can learn it
  within the specified data, time, and computational budget while the
  other cannot. This is practical frustration relief."
- "**Effect C: New internal organization without better attainable
  outcomes.** Both architectures achieve similar task performance, but
  through different representations, specialization patterns, or learning
  histories."

Aggregate loss conflates them. A lower loss at the end of training can be
any of the three, and equal losses can hide C. In the terms of
CLAIM-tmpq80iq, A and B enlarge R(O; H, B) and so can enlarge the
compatibility complex; C leaves it where it was and changes the
organization that reaches it.

## The record's cases, assigned

- **C: deep linear networks (THEORY-186).** A shallow and a deep linear
  network trained on the same data reach the same end-to-end map. The
  shallow one learns every mode exponentially on one timescale; the deep
  one learns them one at a time, strongest first, each in a sigmoidal
  transition, and between stages single predictions "can move the wrong
  way". A38: "same eventual capability but different developmental
  attainability". And "aggregate optimization improvement can coexist with
  temporarily worsening constituent predictions".
- **B, inside the same case, at a time budget (THEORY-186, THEORY-187).**
  The deep network reaches mode α at about (τ/s_α) ln(s_α/ε), the shallow
  one at about τ ln(s_α/ε), so with a deadline the deep network has the
  strong modes (s_α > 1) sooner and the weak ones later. From small initial strength
  the plateau lengthens with depth, from ln(1/ε) with one hidden layer
  towards 1/ε (THEORY-187). C holds at the end of training. Along the way
  the budgeted reachable sets differ, and depth can shrink them as well
  as grow them.
- **B: the random hierarchy model (THEORY-195, THEORY-200).** On
  hierarchically generated data, deep feature learners need a number of
  examples polynomial in the input dimension, and shallow and fixed-kernel
  learners an exponential number. Deep ones also need an exponential number
  when the class statistics are removed (THEORY-195). Networks become
  insensitive to synonymous swaps at about the training-set size at which
  they learn the task (THEORY-200). A38: "**Representational reorganization
  can change which demands are practically attainable under limited data
  and computation, even when a sufficiently expressive alternative
  architecture could theoretically represent the same solution.**"
- **A, at fixed size: products of inputs (THEORY-206).** A38 said "true
  Effect A needs a separately established expressivity restriction; we
  should not infer it from finite-training performance alone", and did not
  find one. The record holds it. Rolnick and Tegmark: one hidden layer needs
  exactly ∏(rᵢ + 1) neurons to approximate x₁^r₁⋯xₙ^rₙ and a deep network
  O(Σ log rᵢ). That is a separation of what each architecture can express
  at a given neuron count, with no learning in it. It is A relative to a
  size budget. Without one there is no separation, since a wide enough
  single layer approximates the monomial. THEORY-206's own limits apply:
  Taylor matching at the origin, bias-free units, and no separation for
  bounded-degree polynomials.

## Why it matters to the frustration program

The owner's point is that the experiment A37 wanted is partly done. What
the record's results show is B and C, which is the distinction relief
needs. B is relief of the original demands under a budget. C is a change
of organization with no relief, which is where individuation and
persistence questions live. A38 named two forms of nucleation during learning, a new
"*representational organization*" and a new "*governing organization*", and
said the literature "already supplies substantial evidence for the first,
under appropriate task and training assumptions". None of
the results bears on the second, persistent relations that decide which
learned capabilities are protected or revised. That is A38's third measure,
"Governance of persistence", and no held result tests it.

## What it does not say

- Not that depth individuates and width does not. A38: "I would not
  formulate a universal hypothesis that depth produces individuation while
  width merely provides redundant capacity. That would be too strong."
  Width and depth each change several mechanisms at once, and the record
  holds results where the variable that sets the regime is neither:
  balanced against unbalanced layers in one two-layer linear network
  (THEORY-212).
- Not that these results show a new individual or endorsement. A38 of the
  deep linear case: "it isn't a demonstration that a new autonomous
  individual has emerged or that the network has endorsed its learned
  modes."
- Not that the assignments hold outside their settings. The deep linear
  results need white inputs and decoupled, balanced starts; the random
  hierarchy law is fitted, not proved, for trained deep networks
  (THEORY-195).
- Not that a budget is a detail. Which effect a result shows changes with
  the data, time and size budget, and the claim is only as definite as the
  budget it states.
