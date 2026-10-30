---
number: 925
status: Active
formerly:
- THEORY-tmp1p6ly
title: 'In a cooperative stochastic game with decentralised actors and a centralised critic, a baseline for each agent that averages the critic''s value over that agent''s own alternative actions under its own policy, the other agents'' actions held fixed, leaves the expected policy gradient unchanged, so each agent can be credited with the advantage of its actual action over that counterfactual average without a default action or an extra simulation; the counterfactual values come from the learned critic, not from the environment'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings), under ADR-065 §5. A second checker followed the
    zero-expectation step and re-ran it by script with controls (status
    review 22). The step the body left implicit is now stated: the actors
    are decentralised, so the joint policy is a product and u^a is
    independent of u^−a given τ. The old promote_when: A checked
    re-derivation recorded in this file, which the reading made
    (NOTE-1152) and which ADR-047 counts toward promotion: the baseline's
    expected contribution Σ_u^a π^a ∇log π^a · b^a vanishes because b^a
    does not depend on u^a. It is refuted by an error in that step or by a
    dependence of the baseline on the agent's own action in the method as
    specified. The title claims nothing about how good the critic's
    counterfactual values are, or about performance; a result about those
    neither promotes nor refutes it.
tags:
- game-theory
- learning-theory
date: '2026-10-24'
source:
- LIT-1517
summary: >-
  Foerster et al.'s counterfactual baseline (COMA, Eq. 4 and Appendix A of
  arXiv v3), read in full in [NOTE-1152](../notes.d/NOTE-1152.md), with the zero-expectation step
  re-derived. A proved property of the estimator, not of performance. Its
  counterfactual is "had the agent acted as it usually does", not "had it
  not acted", and its values are a learned critic's, trained on occasions
  when each alternative was taken; it presupposes those occasions.
---

# THEORY-925: In a cooperative stochastic game with decentralised actors and a centralised critic, a baseline for each agent that averages the critic's value over that agent's own alternative actions under its own policy, the other agents' actions held fixed, leaves the expected policy gradient unchanged, so each agent can be credited with the advantage of its actual action over that counterfactual average without a default action or an extra simulation; the counterfactual values come from the learned critic, not from the environment

## Source

Foerster, Farquhar, Afouras, Nardelli & Whiteson, [LIT-1517](../literature.d/LIT-1517.md), read in
[NOTE-1152](../notes.d/NOTE-1152.md) from arXiv:1705.08926v3: Eq. 4 (p. 4), Lemma 1 and its proof
(Appendix A), and the errata.

## What was actually shown

- **The baseline.** b^a(s, τ, u^−a) = Σ_{u′a} π^a(u′a | τ^a)
  Q(s, τ, (u^−a, u′a)): the critic's value averaged over agent a's own
  alternatives under its policy, every other agent's action as taken.
- **Zero expectation.** Its contribution to the expected gradient is
  −Σ p(s, τ) Σ π^−a Σ_{u^a} π^a ∇log π^a b^a = −Σ … b^a ∇Σ_{u^a} π^a = 0,
  because b^a is constant in u^a (Eqs. 9–13). Re-derived when filed.
- **Convergence.** With the critic conditioned on (s, τ), the joint policy
  is a single-agent policy on an MDP over (s, τ) and Sutton et al.'s (1999)
  actor-critic result applies (Lemma 1, as corrected in v3).
- **Empirically**, on four StarCraft maps the counterfactual baseline beat a
  V baseline with the same critic in speed and final win rate (Table 1).

What could have come out otherwise: a per-agent baseline that depended on
the agent's own action would bias the gradient; this one is built not to.

## What this does not say

- **That the counterfactual is causal or simulated.** It is the critic's
  estimate, and the critic learns an action's value only from occasions
  it was taken; the policy keeps every action above ε/|U| in training.
- **That it values a process that never acts.** Every agent acts every
  step. A never-sampled alternative is valued by the critic's
  extrapolation alone.
- **That it answers "what if the agent had not acted".** That is the
  difference reward's default action, which COMA replaces by the agent's
  own average.
- **That COMA converges in practice.** Lemma 1 assumes a converged,
  compatible TD(1) critic; the experiments use TD(λ) with a deep critic.

## Note of 2026-10-30: the second check

The second check at the status review (ADR-065 §5) followed the step. The
actors are decentralised, so the joint policy is the product Π_b π^b(u^b |
τ^b), and u^a is independent of u^−a given τ. The baseline's contribution
to the expected gradient is therefore Σ p(s, τ) Σ_{u^−a} π^−a(u^−a | τ)
b^a(s, τ, u^−a) Σ_{u^a} π^a(u^a | τ^a) ∇log π^a(u^a | τ^a). The inner sum
is Σ_{u^a} ∇π^a(u^a | τ^a) = ∇ Σ_{u^a} π^a(u^a | τ^a) = ∇1 = 0. The
baseline can be taken out of it because it does not vary with u^a; it
multiplies the score and is not itself differentiated. Both conditions do
work: the baseline must not depend on the agent's own action, and the
agent's action must be independent of the others' given τ.

A script (numpy, in the session's scratchpad) computed the exact expected
gradient of one agent's softmax logits, with and without the baseline, in
five random games of three agents, three actions and four states. The two
differed by at most 4 × 10⁻¹⁷, against gradients of 0.02 to 0.07. Two
controls moved it: a baseline that also depended on the agent's own action
changed the gradient by 0.047, and a joint policy that was not a product
(agent a copying another agent half the time) changed it by 0.055.
