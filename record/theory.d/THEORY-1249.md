---
number: 1249
status: Active
formerly:
- THEORY-tmp07kll
title: 'In a fully observed, finite, communicating, stationary controlled Markov process, a deterministic goal-conditioned policy that achieves every composite goal of depth up to n with probability at least 1 − δ times the optimum determines every transition probability to within √(2P(1−P)/((n−1)(1−δ))), read from its first action on either-or goals; for a policy competent only at one-step goals no bound follows'
version: 1
tags:
- agency
- learning-theory
date: '2026-10-31'
source:
- LIT-1891
summary: >-
  Richens, Abel, Bellot and Everitt (2025), [LIT-1891](../literature.d/LIT-1891.md), Theorems 1
  and 2, read in [NOTE-1469](../notes.d/NOTE-1469.md). The reduction offers the agent a choice
  between "at most k successes of a transition in n attempts" and "more
  than k"; its switch point locates the binomial median. The final bound
  was re-derived and checked numerically against an adversarial
  δ-bounded agent. Active: a theorem, checked. It says the transition
  function is recoverable from the input-output map, not that any
  component of the agent represents it, and it needs full observation,
  determinism and the regret bound on every listed goal.
---

# THEORY-1249: In a fully observed, finite, communicating, stationary controlled Markov process, a deterministic goal-conditioned policy that achieves every composite goal of depth up to n with probability at least 1 − δ times the optimum determines every transition probability to within √(2P(1−P)/((n−1)(1−δ))), read from its first action on either-or goals; for a policy competent only at one-step goals no bound follows

## Source

Richens, Abel, Bellot and Everitt (2025), [LIT-1891](../literature.d/LIT-1891.md), Theorem 1 (pp. 4,
17–20), Lemma 6 (p. 16) and Theorem 2 (pp. 5, 20–21) of arXiv
2506.01622v5; read in [NOTE-1469](../notes.d/NOTE-1469.md).

## What was actually shown

**Setting.** A controlled Markov process (S, A, P) that is finite,
stationary and communicating, with |A| ≥ 2 (Assumption 1). A deterministic
policy π(a | h; ψ) over histories and goals ψ, where goals are sequences
of sub-goals "reach (s, a) ∈ g next, now or eventually", joined by
disjunction. The policy is δ-bounded at depth n if its success
probability is at least (1 − δ) times the optimum for every goal of depth
≤ n and every initial state (Def. 5).

**The reduction.** For a transition (s, a) → s′ with probability P, the
best achievable probability of "exactly r successes in n attempts, in
some order" is C(n, r)P^r(1−P)^{n−r} (Lemma 6). Offer the disjunction
ψ_a(k, n) ∨ ψ_b(k, n): take a first and then achieve at most k successes,
or take b first and achieve more than k. A δ-bounded agent's first action
certifies P_n(X ≤ k) ≥ (1 − δ)P_n(X > k) or the reverse. The smallest k
at which it takes a, k*, satisfies P_n(X ≤ k*) ≥ (1 − δ)/(2 − δ) and
P_n(X ≥ k*) ≥ (1 − δ)/(2 − δ). With the one-sided Chebyshev inequality,
(1 − δ)/(2 − δ) ≤ 1/(1 + t²) for t = (k* − nP)/√(nP(1−P)), so
t² ≤ 1/(1 − δ) and |k*/n − P| ≤ √(P(1−P)/(n(1−δ))). With depth N = 2n + 1
this is the stated bound. For small δ and large nP(1−P) it is
O(δ/√N) + O(1/N).

**Checked.** I re-derived the Chebyshev step. A numerical check let an
adversarial agent switch as early or as late as the regret bound allows,
for n from 5 to 300, δ from 0 to 0.9 and 201 values of P. In 12,060 cases
k*/n never left the bound, provided k may be 0, as the proof assumes.
The printed Algorithm 1 starts at k = 1 and returns (k* − ½)/n, which can
miss the bound by up to 1/(2n).

**Myopic agents (Theorem 2).** If goals only ask for a set at the next
step, an optimal policy needs only argmax_a P(s₁ ∈ Y | a, s₀). When every
action has the same transition law, every policy is optimal, for any
value of P. So no non-trivial bound can be read from it.

**What could have failed.** The switch point could have been uninformative,
or the agent could have satisfied the regret bound with a choice
pattern compatible with many P. Lemma 6 makes the two options'
optimal values a known function of P alone, and the regret bound then
pins the switch.

## What this does not say

- **That the agent has an internal model.** The map runs from the policy.
  The authors say "Theorem 1 proves the existence of a world model encoded
  in the agent's policy, not its specific use (e.g. for planning)" (p. 7).
  A lookup table over (history, goal) that reproduces a δ-bounded policy
  satisfies the theorem just as well ([THEORY-1260](THEORY-1260.md)).
- **Anything about a single task.** Competence at one fixed goal, or at
  one-step goals, fixes nothing about P (Theorem 2). The family of goals
  carries the result.
- **Anything under partial observation, stochastic policies,
  non-stationary or non-communicating environments.**
- **That real agents meet Def. 5.** The paper's own trained agents failed
  it for some goals at every size; the experiment that recovers models
  anyway used a model-based agent in one 20-state environment.
- **How large or costly a policy meeting Def. 5 must be.** There is no
  resource bound.
