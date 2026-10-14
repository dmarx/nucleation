---
number: 321
status: Proposed
formerly:
- THEORY-tmprmrt9
promote_when: >-
  A case outside the model, a laboratory network experiment or field
  data, in which the updating rule is held fixed, the influence structure
  is changed, and the group's settled estimate moves away from the truth
  as the largest influence weight grows, as Proposition 2 predicts. The
  mathematics is proved; what is open is whether real communities update
  closely enough to DeGroot for the condition to decide their beliefs.
  It is refuted, as an account of real groups, by such an experiment in
  which accuracy does not track maximal influence. What cannot settle
  it: further simulations of the DeGroot model, which only restate the
  theorem.
title: "Under repeated DeGroot averaging, a large society's consensus converges to the truth if and only if the largest influence weight vanishes, so network structure alone, not the members' common updating rule, decides whether the group belief is right"
version: 1
tags:
- network-science
- social-science
- epistemology
date: '2026-10-14'
source:
- LIT-999
summary: >-
  Golub & Jackson (2010), [LIT-999](../literature.d/LIT-999.md), Proposition 2 with Lemma 1,
  Corollary 1, Proposition 3 and Theorem 1, read in [NOTE-840](../notes.d/NOTE-840.md) with
  the main proofs checked. The members are naïve, not sound: they
  ignore repeated information, and only the first round is Bayesian. The
  result is in a model with fixed weights, independent signals and
  n → ∞. Speed of consensus and its correctness are independent.
answers:
- QUESTION-047
---
<!-- inactive-ok-file: THEORY-143 THEORY-148 — Proposed; the bandit-model accounts this one sits beside, open -->

# THEORY-321: Under repeated DeGroot averaging, a large society's consensus converges to the truth if and only if the largest influence weight vanishes, so network structure alone, not the members' common updating rule, decides whether the group belief is right

## Source

Golub & Jackson (2010), [LIT-999](../literature.d/LIT-999.md), §§II–V and Appendix A–C, as read in
[NOTE-840](../notes.d/NOTE-840.md).

## What was actually shown

**Setting.** Each agent starts with an independent signal of mean μ and
variance at least σ², and repeatedly replaces its belief by a fixed
weighted average of others' beliefs, p(t) = T p(t−1). All agents use the
same rule; only the weights differ.

**The consensus.** For a convergent T the limit belief of every agent in
a closed group is s·p(0), where s is the unit left eigenvector of T
(Proposition 1, Theorem 3). Influence is recursive: s_i = Σ_j T_ji s_j.

**The characterization.** A sequence of growing networks is wise, all
limit beliefs converging in probability to μ, if and only if the largest
influence weight tends to zero (Lemma 1, Proposition 2; proof checked).
This holds for every admissible signal distribution or for none, so
"the network structure alone determines wisdom".

**Structure.** With reciprocal, equal weights, influence is proportional
to degree and wisdom holds iff max degree / total degree → 0
(Corollary 1). A finite group that everyone attends to within t steps
with weight bounded below prevents wisdom (Proposition 3). Influence can
be concentrated by indirect structure invisible a few steps out
(Example 4). Balance together with minimal out- or in-dispersion suffices
(Theorems 1 and 4).

**Speed.** Whether consensus is reached quickly is independent of
whether it is right; all four combinations occur (§V).

What could have failed: the theorem is an exact if-and-only-if. A
network with vanishing maximal influence whose consensus stayed off the
truth would contradict it, and Lemma 1's variance bound rules that out.

## What this does not say

- **Not that the members are sound.** They are naïve by design: they do
  not discount repeated information. A rational community might aggregate
  correctly where this one fails.
- **Not about real groups.** No data are analysed. Whether real
  communities update like DeGroot agents is not tested here.
- **Not about finite societies.** The criterion is asymptotic; it does not
  grade a group of fixed size.
- **Not about correlated errors, strategic agents or changing trust.**
  Signals are independent and weights fixed.
- **Not that sparse or slow networks are wiser.** Speed and wisdom are
  independent; the variable is concentration of influence, not density.

## Connections

- [QUESTION-047](../questions.d/QUESTION-047.md) asks whether a community can settle on a belief through
  community-level mechanisms with its members' reasoning held fixed. In
  this model it does: the rule is fixed and identical, and the settled
  belief is the truth or a leader's error according to the influence
  structure. That answers the question in part, in a model, with naïve
  rather than sound members.
- [THEORY-143](THEORY-143.md) and [THEORY-148](THEORY-148.md) make network structure decide the outcome in
  bandit models of inquiry, through density and transient diversity. This
  adds a third structural variable, the concentration of influence, in a
  model with no exploration.
