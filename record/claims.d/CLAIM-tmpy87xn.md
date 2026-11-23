---
status: Proposed
title: 'An optimal learning policy is a well-defined scalar optimum when four conditions hold: a declared law for the tasks the learner meets given its history and what it has learned; one valuation over outcomes, the same for every policy compared, with resource costs on its scale; a finite value for every policy, from a finite horizon or a discount that outruns the growth of what learning makes attainable; and a policy class over which the best value is attained. That learning changes which tasks the learner will meet is not among the conditions that fail, since a declared dependence makes what has been learned part of the state'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A construction meeting all four conditions in which no policy attains the
  best value, or an error in the reduction of a task law that depends on
  what has been learned to a decision process over the learner's histories;
  not a showing that some declared valuation is the wrong one, which the
  claim does not deny.
tags:
- learning-theory
- epistemology
date: '2026-11-23'
line:
- learned-structure
- realizability
- formal-apparatus
complements:
- CLAIM-754
- CLAIM-756
uses:
- TERM-131
bears_on:
- QUESTION-495
summary: >-
  Filed by the lead run of 2026-11-23, for the lead asking which
  assumptions a scalar optimum of learning needs. CLAIM-754 says a
  scalar ranks learning processes once a task distribution, costs, horizon
  and preferences are declared; this states the conditions exactly and
  shows that one of them is more than is needed and the list less than
  enough. A fixed task distribution is not needed: a declared law that
  depends on what has been learned is a Markov decision process over the
  learner's organization, and backward induction gives an optimum. What
  can fail is the valuation (CLAIM-tmp6ppvo) and the finiteness and
  attainment of the best value (CLAIM-tmpl9022). The existence theorems
  are standard; the claim's own content is placing learning's effect on
  later tasks inside them. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-754 CLAIM-756 CLAIM-tmphjm0q TERM-131 — Proposed; cited by the lead run of 2026-11-23 -->
<!-- inactive-ok-file: CLAIM-tmp6ppvo CLAIM-tmpl9022 ARG-tmpi8mhy — new; filed by the lead run of 2026-11-23 -->

# CLAIM-tmpy87xn: An optimal learning policy is a well-defined scalar optimum when four conditions hold: a declared law for the tasks the learner meets given its history and what it has learned; one valuation over outcomes, the same for every policy compared, with resource costs on its scale; a finite value for every policy, from a finite horizon or a discount that outruns the growth of what learning makes attainable; and a policy class over which the best value is attained. That learning changes which tasks the learner will meet is not among the conditions that fail, since a declared dependence makes what has been learned part of the state

## The claim

A learner holds an organization M_t, what it has learned so far in the
sense of TERM-131. In each period it chooses an action a_t, an
acquisition or a use of what it holds, at a resource cost c_t; it meets a
task τ_t; it earns r_t. A learning policy π maps the learner's history to
its actions. A policy's value is the expected valuation of the trajectory
it produces, V(π) = E_π[U(trajectory)], most simply
E_π[Σ_{t<H} γ^t (r_t − c_t)].

An optimal learning policy is a policy π* with V(π*) ≥ V(π) for every
admissible π, and it is a well-defined scalar optimum when:

1. **A declared environment.** One probability law over the tasks met,
   given the learner's history, including what it has learned. The law may
   depend on M_t. It need not be fixed.
2. **One valuation.** A single real-valued U over outcomes, the same for
   every policy compared, and not indexed by the organization a policy
   produces. Costs and returns sit on its scale; where they are several
   resources with no declared exchange, a Pareto frontier is the most there
   is (CLAIM-585's case for thresholds). For a comparison of risky policies
   U must be cardinal, as in expected utility.
3. **A finite value.** A finite horizon with bounded returns per period; or
   an infinite horizon with γ < 1 and returns bounded, or growing by a
   factor per period below 1/γ. When learning can multiply the attainable return per
   period by up to g, γ·g < 1 suffices.
4. **Attainment.** The best value is reached by some policy. Finitely many
   organizations, tasks and actions suffice, with a finite horizon or with
   condition 3 for γ < 1. Infinite classes need compactness and upper
   semicontinuity, or the claim weakens to ε-optimal policies.

## Why it holds

Under condition 1 the learner's history, with M_t in it, is the state of a
decision process whose transitions are the declared law. With a finite
horizon and finite sets, backward induction defines the best value from
every history and picks a maximizing action at each, and the policy that
takes those actions attains it. For an infinite horizon with γ < 1 and
bounded returns, the Bellman operator is a γ-contraction on bounded
functions, its fixed point is the best value, and a greedy policy over
finitely many actions attains it. Both are the standard theory of Markov
decision processes. Conditions 2 to 4 are what that theory assumes beyond
condition 1.

So learning's effect on what the learner will later meet changes nothing
here. A learner whose acquisitions bring it harder or richer tasks is in a
process whose state includes what it has acquired, and the dependence is
one more transition. What matters is that the dependence be declared.

`scratch/studies/lead-011/` checks one case. Three organizations change
the chance that the next task is hard (0.1, 0.5, 0.8), and each
acquisition costs a period. Over a horizon of 6, backward induction gives
12.3 from the novice state, and enumerating all 4096 deterministic Markov
policies finds the same value attained: learn twice, then work. Each
acquisition is a loss on its own, as in CLAIM-756.

## Which conditions fail when learning changes what can later be learned

- **Condition 1** fails when the learner cannot declare how its learning
  will change what it meets: QUESTION-495's benefits that "cannot be
  specified in advance". A declared set of laws restores a scalar, the
  worst case over the set, but counts nothing outside the set.
- **Condition 2** fails when what is learned changes what is valued.
  CLAIM-tmp6ppvo shows that no scalar is then fixed by the valuations
  alone.
- **Conditions 3 and 4** fail when learnability grows faster than
  discounting shrinks it. CLAIM-tmpl9022 shows that no policy is then
  optimal, with all four of CLAIM-754's items declared.
- **Condition 2, as incompleteness**, fails when there are several
  criteria and no declared weights. CLAIM-754's three frontiers are such a
  case, and its point that no context-free scalar ranks learners is this
  failure.

ARG-tmpi8mhy carries the constructions that show conditions 2 to 4 are not
implied by the others.

## What it does not say

- That the four are necessary one by one. They are sufficient. Conditions 3
  and 4 can be weakened, by overtaking criteria or by ε-optimality, and
  what is shown is only that dropping each, with the others kept, can lose
  the optimum.
- That a declared optimum is the right one. Declaring the law, the
  valuation and the horizon is a commitment the mathematics does not
  select, as CLAIM-tmphjm0q says of regulation.
- Anything about how to find the optimum, which for a learner's real
  organization is intractable.
