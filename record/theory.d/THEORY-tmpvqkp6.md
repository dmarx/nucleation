---
status: Active
title: 'In DeGroot''s model, where each member repeatedly replaces its opinion by a fixed weighted average of all members'' current opinions, F⁽ⁿ⁾ = PⁿF, the group reaches a consensus from every starting set of opinions exactly when the chain P has a single closed class of communicating members and that class is aperiodic; the consensus is then Σπᵢ Fᵢ with π the unique stationary vector, πP = π, which gives members outside the closed class no weight; two closed classes, or one periodic class, give no consensus'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed Active from NOTE-tmp5sbzm, the reading of the copy the owner
    supplied on 2026-10-25. The conditions are DeGroot's Theorems 1 and 2
    and his negative statement in §5, and the weights his Theorem 3. The
    paper states all of them without proof, as standard Markov-chain
    results. They are re-derived below and checked numerically, which
    meets the condition for Active under ADR-047 v2. The equivalence of
    the two theorems, the quantifier "from every start", and the
    continuous-time contrast are the record's.
tags:
- network-science
- social-science
- probabilistic-modeling
date: '2026-10-25'
source:
- LIT-tmpwlnuv
summary: >-
  DeGroot (1974), [LIT-tmpwlnuv](../literature.d/LIT-tmpwlnuv.md), read in [NOTE-tmp5sbzm](../notes.d/NOTE-tmp5sbzm.md). Repeated averaging
  with fixed weights is a Markov chain run on opinions, and whether it
  ends in agreement is a question about the chain's closed classes and
  their periods. It is not about how much each member trusts itself. The
  weights are fixed and no evidence enters, so nothing here says the
  consensus is right, and the periodic failure is a discrete-time one.
supports:
- CLAIM-tmpfd9lk
---
<!-- inactive-ok-file: CLAIM-262 — Proposed; named for the exchange's reading of influence, nothing here rests on it -->
# THEORY-tmpvqkp6: In DeGroot's model, where each member repeatedly replaces its opinion by a fixed weighted average of all members' current opinions, F⁽ⁿ⁾ = PⁿF, the group reaches a consensus from every starting set of opinions exactly when the chain P has a single closed class of communicating members and that class is aperiodic; the consensus is then Σπᵢ Fᵢ with π the unique stationary vector, πP = π, which gives members outside the closed class no weight; two closed classes, or one periodic class, give no consensus

## Source

DeGroot (1974), "Reaching a Consensus", *Journal of the American
Statistical Association* 69(345): 118–121, [LIT-tmpwlnuv](../literature.d/LIT-tmpwlnuv.md), read in full in
[NOTE-tmp5sbzm](../notes.d/NOTE-tmp5sbzm.md) from the JSTOR scan the owner supplied. Theorems 1 and 2
and the negative cases are in §5, Theorem 3 in §6. The paper gives no
proofs. Theorem 1 is "adapted from a result given by Doob", and the rest
is referred to Feller, Karlin and Parzen. The derivations below are the
record's.

## What was actually shown

**The model.** k members, opinions F = (F₁, …, F_k)ᵀ (distributions, or
points of a convex set in a linear space), and a row-stochastic P chosen
once: p_ij ≥ 0, Σⱼ p_ij = 1. Each round F ← PF, so F⁽ⁿ⁾ = PⁿF. A consensus
is reached when every component of F⁽ⁿ⁾ converges to the same limit.

**From every start, consensus is Pⁿ → 1π.** If Pⁿ → 1π then
F⁽ⁿ⁾ → 1(πF), a consensus at πF = Σπᵢ Fᵢ. Conversely, if the opinions
converge to a common limit for every F, take F = e_j: column j of Pⁿ
converges to a constant vector π_j 1, which is DeGroot's (4.2). For one
given F the converse fails (see below), so DeGroot's "if and only if" in
§4 holds with the quantifier "for every F".

**Sufficiency (Theorems 1 and 2).** Suppose the chain has one closed class
C and C is aperiodic. Then P restricted to C is primitive, so for some m
every entry of P^m on C × C is positive. Every member outside C reaches C
with positive probability within k steps. Hence for some n, column j of
Pⁿ is positive for any j ∈ C: that is Theorem 1's hypothesis. Under it,
with ε the smallest entry of that column, each application of Pⁿ shrinks
the spread maxᵢ xᵢ − minᵢ xᵢ of any vector x by a factor at most (1 − ε),
because every row of Pⁿ puts weight at least ε on the same entry. So
Pⁿᵗ x tends to a constant vector for every x, and Pᵗ x as well, since the
spread never increases under a stochastic matrix. That is Pᵗ → 1π.

**The two theorems are one condition.** Conversely, if column j of Pⁿ is
positive, every member reaches j, so j lies in every closed class, and
there is only one. Column j of P·Pⁿ = Pⁿ⁺¹ is then positive too (a
stochastic matrix times a positive vector), so (Pᵗ)_jj > 0 for every
t ≥ n, and j's class is aperiodic. So Theorem 1's condition and Theorem
2's are equivalent for a finite chain. DeGroot calls Theorem 2 "an
analogous result".

**Necessity (the negative cases).** With two closed classes C₁ and C₂,
members in C₁ never see C₂: F = 1_{C₁} stays 1 on C₁ and 0 on C₂ for ever.
With one closed class of period d > 1, its members split into d cyclic
groups. F = indicator of one group then rotates among the groups and never
converges. So there is no consensus from every start in either case, and
the characterization is complete.

**The weights (Theorem 3).** If Pⁿ → 1π then π = lim eᵢᵀPⁿ⁺¹ = πP, π ≥ 0 and
Σπᵢ = 1. Any stationary σ satisfies σ = σPⁿ → (σ1)π = π, so π is the unique
stationary vector. For a transient member i, (Pⁿ)_ji → 0 for all j, so
πᵢ = 0. The invariant behind it: πF⁽ⁿ⁾ = πPⁿF = πF at every round, so the
consensus can only be πF.

**Checked by script** (numpy, when filed):

- DeGroot's examples. P = [[½, ½], [¼, ¾]] gives π = (⅓, ⅔). The
  three-member extension gives (⅓, ⅔, 0), and P²⁰⁰'s third row is (⅓, ⅔, 4e-96).
  For the four-member two-block P, P² = P: agreement within each block
  after one revision, as the paper says.
- Theorem 1's condition (some Pⁿ, n ≤ (k − 1)² + 1, with a positive
  column) against Theorem 2's (one closed class, aperiodic): the same
  verdict in 3,000 of 3,000 random sparse stochastic matrices with k from 2
  to 6. Against a rank-one P⁴⁰⁰⁰ the verdicts agreed in 2,992. The eight
  others all had a second eigenvalue of modulus 0.996 to 0.9995, so they
  had not yet converged.
- A periodic closed class: [[0, 1], [1, 0]] swaps (0.2, 0.7) for ever, while
  equal opinions stay equal. With a transient third member who averages
  the two, P²⁰⁰ and P²⁰¹ still differ.

What could have failed: the condition could have needed more, such as a
positive diagonal or symmetric weights, or less, such as connectivity
alone. Aperiodicity is needed, and connectivity among the transient
members is not.

## What this does not say

- **Not that the consensus is right.** No observation enters and the
  weights never change. Whether the pooled opinion tracks a truth is Golub
  and Jackson's question ([THEORY-321](THEORY-321.md)), asked of this model.
- **Not that agreement fails for every start** in the negative cases.
  Members who start equal stay equal, and a start with no component along
  the oscillating or separating modes may converge. The negative cases
  deny consensus from every start.
- **Not about continuous time.** With ẋ = (P − I)x, a periodic P
  converges: e^{50(P−I)} for the swap matrix is [[½, ½], [½, ½]] (checked).
  Only one closed class is needed there.
- **Not about speed.** How fast Pⁿ approaches 1π, set by the second
  eigenvalue, is not in the paper.
- **Not about changing weights.** DeGroot names that possibility in §8 and
  leaves it unstudied.

## Connections

- **[THEORY-321](THEORY-321.md).** Golub and Jackson's influence vector s is this π, and
  their Proposition 1 is this theorem for a strongly connected, aperiodic
  society. The present account says what that narrowing excludes: several
  closed groups, which give no consensus, and a periodic one, which gives
  none in discrete time. A single closed class with transient members is
  allowed here, with those members getting no weight.
- **[CASE-tmpvmjgd](../cases.d/CASE-tmpvmjgd.md).** Its ℓ, with ℓᵀW = ℓᵀ and Σℓᵢ = 1 for a row-stochastic
  W, is π for P = W. The invariance it uses, ℓᵀ(κW − λI) = (κ − λ)ℓᵀ, is the
  invariant πPⁿF = πF given a leak and a drive. Its discrete-time
  amendment (aperiodicity) is DeGroot's own periodic case. Its exclusion of
  a reducible W can be narrowed to several closed classes. Checked: for a
  W with one closed class of two members and two transient members,
  ℓ = (0.429, 0.571, 0, 0), the closure ℓᵀ(κW − λI) − (κ − λ)ℓᵀ is 3 × 10⁻¹⁷,
  and the other eigenvalues of W are 0.5, 0.5 and 0.3.
- **[CLAIM-262](../claims.d/CLAIM-262.md).** The exchange called ℓ "an emergent summary of who is
  listened to". In DeGroot that is literal. The weights are chosen and
  fixed, so π summarizes the network of attention and not anyone's
  accuracy.
