---
number: 914
status: Proposed
formerly:
- CLAIM-tmpt226r
title: 'Golub–Jackson wisdom fails with many closed groups'
statement: >-
  Golub and Jackson's characterization of wisdom by a vanishing largest
  influence weight fails in its sufficient direction when a society has many
  closed groups, and holds with several closed groups when their number m
  satisfies s_1 log m → 0, in particular when it is bounded
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-061 as a
    delegated worker, from a rereading of Golub and Jackson's
    Definition 3, Proposition 2, Theorem 3 and the proof of Proposition 2
    in the published version on Benjamin Golub's website, and the
    computation in CASE-340.
role: thesis
warrant: demonstrated
defeated_if: >-
  A reading of the published paper under which the construction in
  CASE-340 is not a sequence of convergent stochastic matrices with
  influence vectors whose largest entry tends to 0, or under which that
  sequence counts as wise (for instance an erratum or a later statement by
  the authors that defines influence or wisdom differently for several
  closed groups); or an error in the union bound for the sufficient
  condition. Simulations of strongly connected networks cannot defeat it,
  since it concerns only societies with several closed groups.
tags:
- network-science
- probabilistic-modeling
- mathematics
date: '2026-11-22'
line:
- distributed-agency
- formal-apparatus
answers:
- QUESTION-184
grounds:
- CASE-340
- THEORY-321
summary: >-
  Settles the narrower matter of [QUESTION-184](../questions.d/QUESTION-184.md). Golub and Jackson
  ([LIT-999](../literature.d/LIT-999.md)) normalize influence to sum to 1 on each minimal closed group
  (Theorem 3) and define wisdom by the largest deviation over all agents
  (Definition 3), so their definitions do not exclude the audit's sketch,
  and [CASE-340](../cases.d/CASE-340.md) shows the sketch works: s_1 → 0 and the society is
  not wise. Proposition 2's proof of the "if" direction shows convergence
  along every fixed sequence of agents, which does not control the
  maximum. The "only if" direction holds as stated. The "if" direction
  holds when s_1(n)·log m(n) → 0, m the number of minimal closed groups,
  by Hoeffding's inequality and a union bound, and so whenever m is
  bounded, including the strongly connected case of [THEORY-321](../theory.d/THEORY-321.md). The
  question's other half, whether real groups behave so, stays open. The
  wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CASE-340 — Proposed; the construction this claim rests on, filed in the same batch -->

# CLAIM-914: Golub–Jackson wisdom fails with many closed groups

## The claim

Golub and Jackson's Proposition 2 ([LIT-999](../literature.d/LIT-999.md), p. 124) reads: "If (T(n)) is a
sequence of convergent stochastic matrices, then it is wise if and only
if the associated influence vectors are such that s1(n) → 0." Read with
the paper's own definitions, it is true in one direction and false in the
other once the number of minimal closed groups may grow.

**The definitions.** Influence is Theorem 3's s (p. 137): (i) Σ_{i∈B} s_i
= 1 for any minimal closed group B, (ii) s_i = 0 off the minimal closed
groups, (iii) s_B the left unit eigenvector of T_B. Section III takes s(n)
"as defined in Proposition 1 (or, more generally, Theorem 3)" (p. 123).
Wisdom is Definition 3: plim_{n→∞} max_{i≤n} |p_i^(∞)(n) − μ| = 0, "the
limiting beliefs converge jointly in probability to the true state μ".
Neither excludes a growing number of closed groups. Per-group
normalization makes s_1 smaller, not larger, than a normalization over
the whole society would.

**Only if: holds.** If s_1(n) does not tend to 0, along a subsequence
the leader's group B_n has consensus s_B·p_B with variance at least
σ²s_1² ≥ σ²c², and the bounded-variable argument of Lemma 1 shows that
this one consensus does not converge to μ in probability. The maximum
over agents is at least its deviation. This is the paper's own argument.

**If: fails.** [CASE-340](../cases.d/CASE-340.md): ⌊n/k⌋ closed groups of k = ⌈√(ln n)⌉ with
equal weights and Bernoulli(1/2) signals have s_1 = 1/k → 0, but some
group's consensus is 0 or 1 with probability 1 − (1 − 2^(1−k))^m → 1.

**Where the proof goes wrong.** The proof of the "if" direction (p. 141)
says that "it suffices to show that if i_n ≤ n is any sequence of agents
in minimal closed groups, then plim p_{i_n}^(∞)(n) = μ", and shows that by
applying Lemma 1 inside the group B_n of i_n. That gives convergence
along every sequence fixed in advance, but the agent attaining the
maximum depends on the realized signals. With m(n) independent groups the
maximum can miss although each fixed group does not.

**What suffices.** Agents outside the closed groups hold convex mixtures
of group consensus values (Theorem 3 (v)), so the maximum deviation is
the maximum over groups. A group's consensus s_B·p_B is a weighted sum of
independent [0, 1] variables, so by Hoeffding
P(|s_B·p_B − μ| ≥ ε) ≤ 2 exp(−2ε²/Σ_{i∈B} s_i²) ≤ 2 exp(−2ε²/s_1),
using Σ_{i∈B} s_i² ≤ s_1 Σ_{i∈B} s_i = s_1. A union bound over the m
groups gives P(max ≥ ε) ≤ 2m exp(−2ε²/s_1), which tends to 0 for every ε
when s_1·ln m → 0. Bounded m is a special case, and Chebyshev already
suffices there: P(max ≥ ε) ≤ m s_1/(4ε²). In the construction,
s_1·ln m ≈ √(ln n) → ∞; groups of size (ln n)² give s_1·ln m ≈ 1/ln n → 0,
and the computation confirms they are wise.

**What follows in the paper.** Corollary 1 (connected symmetric
networks), Lemma 1, Proposition 3 and the examples are untouched.
Theorem 1 and Theorem 4 reach wisdom through Proposition 2's "if"
direction (Theorem 4's proof: "By Proposition 2 … it suffices to show
that lim s_1(n) = 0"), so for societies with unboundedly many closed
groups they inherit the gap if their hypotheses can hold there. Minimal
out-dispersion appears to rule such societies out: a family of q members
inside a closed group of o(n) members gives no weight to the rest of
society, which is nearly all of it. Whether balance with minimal
in-dispersion can hold there was not settled; the balance ratio for a
whole closed group is 0/0.

## What it does not say

- Not that [THEORY-321](../theory.d/THEORY-321.md) is wrong. Its narrowing to a strongly connected
  society, made at the audit, is exactly where the characterization is
  safe, and the 2026-10-25 note's extension to one closed class with
  transient members is safe too (m = 1).
- Not that the paper's main message fails. For any society with boundedly
  many closed groups, the usual reading, a vanishing largest influence is
  necessary and sufficient.
- Not that s_1·ln m → 0 is necessary. It is a sufficient condition from a
  union bound; the exact boundary depends on the groups' sizes and
  weights.
- Not whether the authors know of this. A web search on 2026-11-22 found
  no erratum; the AEA article page and the authors' pages were not
  checked for one.
- Nothing about real groups, the other half of [QUESTION-184](../questions.d/QUESTION-184.md).
