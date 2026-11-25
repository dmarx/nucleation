---
number: 1130
status: Proposed
formerly:
- CLAIM-tmpl9022
title: 'When each period of learning multiplies what every later period can earn by more than discounting shrinks it, no learning policy is optimal: investing one period more always beats stopping, and never stopping earns nothing; so a scalar optimum of learning needs the horizon or the discount to bound the growth of learnability, and declaring a task distribution, costs, a horizon and a valuation does not by itself supply one'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the arithmetic, or a policy in the stipulated class that
  attains the supremum. A showing that no real learner's returns grow
  geometrically without bound would leave the claim true and narrow its
  reach; it would not defeat it.
tags:
- learning-theory
- epistemology
date: '2026-11-23'
line:
- learned-structure
- realizability
complements:
- CLAIM-754
- CLAIM-756
- CLAIM-758
bears_on:
- QUESTION-495
summary: >-
  Filed by the lead run of 2026-11-23, on the reading of the lead in which
  what is learned changes what can later be learned, and so what later
  work can earn. With everything [CLAIM-754](CLAIM-754.md) asks for declared (a task law,
  costs, an infinite horizon with discount γ, a valuation), a learner whose
  every period of investment multiplies its later payoff rate by g, with
  γ·g > 1, has no optimal policy: investing n periods and then exploiting
  is worth (γg)ⁿ·r/(1 − γ), which grows with n, and never exploiting is
  worth 0. A bounded version, the one exam that can be sat at any time,
  has a finite supremum no policy reaches. A finite horizon restores an
  optimum, which can lie late. This is [CLAIM-1197](CLAIM-1197.md)'s third and fourth
  conditions failing, and [QUESTION-495](../questions.d/QUESTION-495.md)'s choice between investing in
  learnability and present competence, in the regime where investing always
  wins and so never pays. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-754 CLAIM-756 CLAIM-758 — Proposed; cited by the lead run of 2026-11-23 -->
<!-- inactive-ok-file: CLAIM-1197 ARG-227 — new; filed by the lead run of 2026-11-23 -->

# CLAIM-1130: When each period of learning multiplies what every later period can earn by more than discounting shrinks it, no learning policy is optimal: investing one period more always beats stopping, and never stopping earns nothing; so a scalar optimum of learning needs the horizon or the discount to bound the growth of learnability, and declaring a task distribution, costs, a horizon and a valuation does not by itself supply one

## The construction

In each period a learner either invests, earning nothing, or exploits,
earning its current rate. Each period of investment multiplies the rate
by g > 1, starting from r > 0. Exploiting commits: once the learner turns
to use what it holds it consolidates and stops acquiring, the pattern
[CLAIM-758](CLAIM-758.md) calls overconsolidation, here taken as a stipulation. The policies
are then π_n, invest n periods and then exploit for ever, and π_∞, never
exploit. Returns are discounted by γ < 1 over an infinite horizon.

V(π_n) = Σ_{t ≥ n} γ^t · g^n · r = (γg)^n · r / (1 − γ), and V(π_∞) = 0.

Every value is finite, the task law, costs, horizon and valuation are all
declared, and the policy class is countable.

- If γg > 1, V(π_{n+1}) = γg · V(π_n) > V(π_n) for every n, and
  V(π_∞) = 0 is below all of them. The supremum is infinite and no policy
  attains it. With γ = 0.9 and g = 1.5, the values run 10, 13.5, 18.2,
  24.6, 33.2, … .
- If γg = 1, every π_n is optimal and the optimum is not unique.
- If γg < 1, π_0 is optimal: learning never pays.

**Bounded.** One exam may be sat at any time, with no discount; after n
periods of study it is passed with probability 1 − 2⁻ⁿ, worth 1, and never
sitting it is worth 0. Every value is below 1, each n is beaten by n + 1,
and the supremum 1 is not attained. The value is finite and still no policy
is optimal, so attainment is a condition of its own.

**A finite horizon restores an optimum.** With H periods the class is
finite and some n is best; with γ = 0.9, g = 1.5 and H = 20 it is n = 17,
investing for 17 of the 20 periods. `scratch/studies/lead-011/` checks
all three cases in exact arithmetic.

**Without the commitment** the learner may interleave investing and
exploiting, and when γ²g ≥ 1 a policy that alternates them already has
infinite value, so the values are not all finite. The stipulation keeps
the failure to attainment, not to divergence; dropping it makes things
worse, not better.

## So

[CLAIM-754](CLAIM-754.md) says a scalar can rank learning processes once a task
distribution, costs, horizon and evaluative preferences are declared. Here
all four are declared and no policy is best. What a scalar optimum needs
in addition is that the horizon or the discount bound the growth of what
learning makes attainable: [CLAIM-1197](CLAIM-1197.md)'s third and fourth conditions.
The failure is specific to learning that changes what can later be
learned: a learner whose investments did not raise later returns would
face γ·1 < 1 and an optimum at once.

For [QUESTION-495](../questions.d/QUESTION-495.md)'s narrower question, when investing in future learnability
is better than improving present competence, the construction answers in
the crudest case. Investing is better exactly when γg > 1, and then it is
always better, so the question "how much" has no answer without a
deadline, a cost of delay, or a ceiling on g.

## What it does not say

- That real learners face unbounded geometric growth. Returns to learning
  usually saturate, and then an optimum exists. The claim marks which
  assumption is doing the work, not how often it fails.
- That the right response is to stop at some arbitrary n. An ε-optimal
  policy exists for every ε under the bounded version; under γg > 1 not even
  that.
- Anything against [CLAIM-756](CLAIM-756.md), which shows that a loss-making acquisition can
  belong to the best policy; here there is no best policy.

[ARG-227](../arguments.d/ARG-227.md) carries the inference from this construction to the claim that
[CLAIM-1197](CLAIM-1197.md)'s third and fourth conditions are not implied by the others.
