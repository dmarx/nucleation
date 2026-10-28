---
number: 822
status: Active
formerly:
- THEORY-tmpz4ja2
title: 'For a Markov chain and a partition of its states, strong lumpability, every state of a block sending the same probability into each block, is the column-equitability of the master-equation operator and makes the block label informationally closed; when the chain is irreducible, an informationally closed label that is itself Markov is strongly lumpable, with no aperiodicity needed; weak lumpability gives a Markov label that need not be closed; and the same holds on the causal-state chain of any stationary process'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-1030. The results are the paper's
    Proposition 4 and Theorem 3, with Counterexamples 4, 6 and 7. The
    paper proves the converse through a cited theorem of Geiger and Temmel
    for stationary, irreducible, aperiodic finite chains. It is re-derived
    below directly, without aperiodicity, and the forward direction
    without irreducibility. Theorem 3 (3) is re-derived by a shorter route.
    The identification with THEORY-755's column-equitability is the
    record's. The examples were checked numerically. This meets ADR-047 v2.
tags:
- complex-systems
- information-theory
- mathematics
date: '2026-10-20'
source:
- LIT-1306
- LIT-1242
summary: >-
  Rosas et al. (arXiv 2024), [LIT-1306](../literature.d/LIT-1306.md), read in [NOTE-1030](../notes.d/NOTE-1030.md), on Kemeny–Snell lumpability, joined to Shpak et al.'s column-equitable partitions ([LIT-1242](../literature.d/LIT-1242.md), [THEORY-755](THEORY-755.md)). Exact closure of a block label in a Markov chain is a condition on transition rows, a symmetry, and not weak coupling. The converse needs the label to be Markov: a closed label can have memory. Exact results only, with no bound for nearly lumpable partitions.
supports:
- CLAIM-409
bears_on:
- QUESTION-218
---
# THEORY-822: For a Markov chain and a partition of its states, strong lumpability, every state of a block sending the same probability into each block, is the column-equitability of the master-equation operator and makes the block label informationally closed; when the chain is irreducible, an informationally closed label that is itself Markov is strongly lumpable, with no aperiodicity needed; weak lumpability gives a Markov label that need not be closed; and the same holds on the causal-state chain of any stationary process

## Source

Rosas et al. (2024), arXiv:2402.09090, [LIT-1306](../literature.d/LIT-1306.md), read in full in
[NOTE-1030](../notes.d/NOTE-1030.md): Definition 7, Lemma 4 (cited from Geiger and Temmel 2014),
Proposition 4, Theorem 3 and Counterexamples 4, 6 and 7. Lumpability is
from Kemeny and Snell (*Finite Markov Chains*, §6.3–6.4). The link to
column-equitable partitions is the record's, from [THEORY-755](THEORY-755.md) (Shpak et
al., [LIT-1242](../literature.d/LIT-1242.md)). The derivations below are the record's.

## What was actually shown

X is a Markov chain on a countable state space with transition matrix P
(rows are origins). The blocks C₁, C₂, … partition the states, and
Z_t = f(X_t) is the block label. Write P(x → C) = Σ_{y∈C} P(x, y).

**Strong lumpability is a row condition.** Kemeny and Snell define it as:
Z is Markov, with the same transitions, for every initial law. Suppose
P(x → C_I) = q(J, I) for every x ∈ C_J (the row condition). Then
p(Z_{t+1} | X⃗_t) = p(Z_{t+1} | X_t) = q(Z_t, ·), so Z is Markov with q
from any start. Conversely, start from a point mass at x ∈ C_J:
P(Z₁ = I | Z₀ = J) = P(x → C_I) must equal q(J, I) for every such x.

**It is [THEORY-755](THEORY-755.md)'s column-equitability, for the master equation.** The
law evolves as p_{t+1} = Pᵀp_t. For A = Pᵀ, the column sum of block I over
column j is Σ_{i∈C_I} A_ij = P(j → C_I). Column-equitability asks that it
be the same for every j ∈ C_J, which is the row condition. So "the block
occupation probabilities evolve autonomously from every initial law"
([THEORY-755](THEORY-755.md), with point masses among the initial states) is strong
lumpability.

**Strong lumpability ⟹ informational closure.** By the row condition,
p(Z_{t+1} | X⃗_t) = q(Z_t, ·), a function of Z_t. So
I(X⃗_t; Z_{t+1} | Z⃗_t) = 0, and by [THEORY-820](THEORY-820.md) (a) Z is
informationally closed, i.e. dynamically independent. No irreducibility,
aperiodicity or stationarity of the start is needed. The paper's
Proposition 4 assumes all three.

**Closure with a Markov label ⟹ strong lumpability, if X is irreducible.**

- Take the stationary law π. If X is irreducible and positive recurrent
  (as every finite irreducible chain is), then π(x) > 0 for every x.
- Closure gives H(Z_{t+1} | Z⃗_t) = H(Z_{t+1} | X⃗_t) = H(Z_{t+1} | X_t).
  Markovity of Z gives H(Z_{t+1} | Z⃗_t) = H(Z_{t+1} | Z_t). So
  I(Z_{t+1}; X_t | Z_t) = 0.
- Then p(z′ | x) = p(z′ | f(x)) for every x of positive mass, and hence
  for every x. That is the row condition.
- Aperiodicity is not used. The paper's footnote 109 leaves open whether
  it can be dropped.

**The Markov hypothesis is needed.** Let X_t = (Z_t, Z_{t−1}) for a
binary second-order Markov Z with all transitions positive. X is an
irreducible, aperiodic Markov chain. X_t is a function of Z⃗_t, so Z is
closed. It is not strongly lumpable, because p(Z_{t+1} | X_t) depends on
Z_{t−1}. The paper's Counterexample 6, a deterministic 4-cycle, makes the
same point with a periodic chain.

**Weak lumpability does not give closure.** Counterexample 4 (checked).
Under the uniform stationary law Z is i.i.d., hence Markov, yet the
transfer entropy is 1 bit. Weak lumpability is closure of the label's
law from one initial law. Informational closure needs the micro state to
add nothing, whatever the micro state is.

**Second-order lumpability does not give closure either.** Counterexample
7, checked: H(Z_{t+1} | Z_t, Z_{t−1}) = 0.7329,
H(Z_{t+1} | X_t) = 0.5521, and the transfer entropy is 0.1808 bits at
both 2 and 6 steps of history.

**A numerical check of the forward direction.** A three-state chain with
P(a → c) = P(b → c) = 0.3, lumped as {a, b}, {c}: transfer entropy 0 at
one to four steps of history. With P(b → c) moved to 0.2, it is
0.0064 bits.

**On the causal-state chain** (Theorem 3). Let E_t be the causal states
of any stationary process X, a Markov chain with unifilar transitions.

- *(4) Strong lumpability gives closure.* Suppose E is strongly lumpable
  under f, and set Z_t = f(E_t). The law of X_{t+1} given X⃗_t depends
  only on E_t, and E_{t+1} is fixed by E_t and X_{t+1}. So
  p(Z_{t+1} | X⃗_t) = p(Z_{t+1} | E_t) = q(Z_t, ·), and Z is
  informationally closed. Z is then a coarse-graining of X's past, not in
  general of its present state.
- *(3) Closure gives strong lumpability.* Let Z = f(X_t) be spatial and
  informationally closed. By [THEORY-820](THEORY-820.md), E′_t = f*(E_t), with
  E′_{t+1} = δ(E′_t, Z_{t+1}) by unifilarity. So
  p(E′_{t+1} | E_t) = Σ_z p(Z_{t+1} = z | E_t)·1[δ(E′_t, z) = ·].
  Here p(Z_{t+1} | E_t) = p(Z_{t+1} | X⃗_t) = p(Z_{t+1} | Z⃗_t) =
  p(Z_{t+1} | E′_t), by closure. So p(E′_{t+1} | E_t) depends on E_t only
  through E′_t. That is the row condition, and E is strongly lumpable
  under f*, for every causal state of positive mass.
- *(1)–(2) Weak lumpability.* Computational closure, E′ = f*(E), makes E
  weakly lumpable under f*, because E′ is Markov under the stationary law.
  Conversely, if f(E) is Markov under the stationary law, its causal
  states are a function of f(E_t), hence of E_t. The paper's definition
  asks for Markov "for at least one initial distribution". The proof
  needs the stationary one.

What could have failed: closure of the label could have needed more than
a row condition, such as conditions on how mass is spread inside blocks.
It does not. The within-block distribution matters only for weak
lumpability, which is the wrong notion for closure.

## What this does not say

- **Not that the closed coarse-grainings form a lattice.** Strongly
  lumpable partitions are closed under common coarsening: within a block
  of the join, states are linked by chains of shared blocks of either
  partition, and each link preserves the probabilities into the join's
  blocks. They are not closed under common refinement ([THEORY-820](THEORY-820.md)'s
  three-bit example, where A and B are strongly lumpable and (A, B) is
  not).
- **Not anything approximate.** A partition whose row sums nearly agree
  is not shown to be nearly closed. One example in [NOTE-1030](../notes.d/NOTE-1030.md) (a
  jittered modular walk) fits that, and it is no bound.
- **Not that closure needs modularity.** On a random walk with uniform
  weights, every partition is strongly lumpable (checked on 50 random
  partitions of eight nodes into two or three groups). The paper's modular walk closes for every
  ratio r_b/r_w, including r_b > r_w (checked at 0.01, 1 and 3).
- **Not closure of a single block's indicator.** The label of the whole
  partition closes. Membership in one block need not.

## Connections

- **[THEORY-755](THEORY-755.md).** For a Markov chain's master equation, its condition is
  strong lumpability. This entry adds that the block label is then
  dynamically independent, which [THEORY-755](THEORY-755.md) showed only for the linear
  Gaussian VAR reading.
- **[THEORY-733](THEORY-733.md).** Its L A = B L is the Gaussian counterpart of the row
  condition: p(Y_{t+1} | X_t) depends on X_t only through Y_t. There,
  with Σ ≻ 0, closure forces it without assuming Y is Markov. Here a
  closed label can have memory, because a chain can carry exact delayed
  copies (X_t = (Z_t, Z_{t−1})), which non-degenerate noise rules out.
- **[CLAIM-388](../claims.d/CLAIM-388.md).** Uniform coupling makes every partition aggregable in the
  VAR. Uniform weights make every partition strongly lumpable in the
  walk. In neither is any group a weakly coupled block.
- **[CLAIM-389](../claims.d/CLAIM-389.md).** Counterexample 4 is its discrete counterpart: a label
  that is Markov in its own law and still dynamically dependent.
- **[QUESTION-218](../questions.d/QUESTION-218.md): answers in part.** The paper's closed units are
  partitions of the state space. In most of its examples these are the
  orbits of a permutation symmetry: counts, energy levels, overlaps,
  module labels. That is the equitable-partition kind of unit [THEORY-755](THEORY-755.md)
  added, not a block.
