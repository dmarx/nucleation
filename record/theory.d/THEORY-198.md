---
number: 198
status: Active
formerly:
- THEORY-tmpc8tc8
title: 'For a finite-range lattice Hamiltonian, a block coarse-graining that keeps all the mutual information the block shares with the system beyond a buffer makes the coarse measure factorize across the block, in 1D and, in D dimensions, when capture by a hyperplane of blocks amounts to capture by each block; barring exact cancellation of existing couplings, the renormalized Hamiltonian then gains no range, and in 1D product disorder gains no correlations across the block. The coarse-grainings actually optimized fall short of that condition, and for them the link is computed only for two-spin blocks of 1D Ising chains'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted from Proposed to Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-198.yaml, batch 019, ADR-047).
    The title stated the factorization for every dimension. It now carries
    the D-dimensional proof's hypotheses: capture by a hyperplane of blocks
    amounting to capture by each block, and no exact cancellation of
    existing couplings when the buffer is summed out. The numerical clause
    names what was computed, two-spin blocks of the 1D Ising and dilute
    random Ising chains. The promote_when asked about coarse-grainings short
    of full capture in two or more dimensions, which the body disclaims. It
    moves, unchanged, to QUESTION-tmpavq90. The Lemma is re-derived in the
    note of 2026-10-19 below. Under ADR-047 v3 the hedged numerical clause
    rests on the one study, which NOTE-682 read in full.
tags:
- natural-sciences
- information-theory
date: '2026-10-09'
source:
- LIT-881
summary: >-
  Lenggenhager, Gökmen, Ringel, Huber and Koch-Janusz (2018),
  [LIT-881](../literature.d/LIT-881.md): proved in 1D, and in D dimensions under an extra per-block
  assumption and barring fine-tuned cancellations. The full-capture
  condition is not met in the paper's own worked case (decimation of
  two-spin Ising blocks keeps about half the information), and the decay
  of longer-range, many-spin and disorder-correlation terms as more
  information is kept is shown perturbatively for two-spin blocks of 1D
  chains only, and is monotonic only locally.
answers:
- QUESTION-065
---
<!-- inactive-ok-file: THEORY-194 THEORY-073 QUESTION-025 — Proposed or open; cited as the account this one underpins, a neighbour, and the question it does not answer -->

# THEORY-198: For a finite-range lattice Hamiltonian, a block coarse-graining that keeps all the mutual information the block shares with the system beyond a buffer makes the coarse measure factorize across the block, in 1D and, in D dimensions, when capture by a hyperplane of blocks amounts to capture by each block; barring exact cancellation of existing couplings, the renormalized Hamiltonian then gains no range, and in 1D product disorder gains no correlations across the block. The coarse-grainings actually optimized fall short of that condition, and for them the link is computed only for two-spin blocks of 1D Ising chains

## Source

Lenggenhager, Gökmen, Ringel, Huber and Koch-Janusz (2018; Phys. Rev. X
2020), [LIT-881](../literature.d/LIT-881.md): Sec. III and Appendix B (Lemma, Propositions 1 and
2, Eqs. B1–B22), Secs. IV and VI with Appendix D (Figs. 4, 5, 9–12); as
read in [NOTE-682](../notes.d/NOTE-682.md).

## What was actually shown

**The proof.** Blocks are taken large enough that only neighbouring
blocks interact. Fix a block (in D dimensions, a hyperplane of blocks),
call its neighbours the buffer and the rest the left and right
environments. If the coarse variable keeps all the block's information
about the environment, the block carries no further information about the
environment given the coarse variable; locality makes the two
environments independent given the block; together they make the two
environments independent given the coarse variable. The coarse measure
then factorizes across that variable once the coarse buffer is summed
out, so no effective term couples the two sides. Since the block was
arbitrary, the range does not grow. In 1D with a product distribution of
nearest-neighbour disorder, the same rule stays optimal under any change
of disorder confined to one side, so the renormalized disorder
distribution carries no correlations across the block.

This could have failed: full capture might have left the environments
correlated through the buffer, and in D dimensions it might require
coarse variables shared across blocks. The first is excluded by the
proof; the second is excluded by assumption.

**The numerics.** For every two-spin rule (λ₁, λ₂) on the 1D Ising chain
and on the dilute random Ising chain, the information kept is computed
exactly and the renormalized couplings perturbatively. Next-nearest
neighbour and four-spin couplings, and correlations between neighbouring
renormalized couplings, vanish where the information is greatest, at
decimation. Majority rule, which keeps least, generates them.

## What this does not say

- **Not that the maximizer gets full capture.** With the number and type
  of coarse variables fixed, it usually cannot. In the paper's worked
  case decimation keeps about half of I(V : E) (0.505 at K = 0.1 with a
  one-site buffer, by the reader's calculation), yet its Hamiltonian is
  exactly nearest-neighbour; that exactness is a property of the 1D
  chain, not a consequence of the theorem.
- **Not that complexity falls monotonically with information.** The
  authors find it monotonic only locally, with accidental zeros away from
  the maximum; what is kept is that the global maximum is a global
  minimum of the measured couplings.
- **Not a proof for two or more dimensions without conditions.** The
  D-dimensional step assumes that capture for a hyperplane amounts to
  capture by each block separately, called reasonable, not shown, and
  excludes fine-tuned cancellations of existing couplings. The disorder
  result is proved in 1D only.
- **Not that the block, buffer and environment are found.** They are a
  spatial partition fixed before anything is computed, and locality is
  stated with respect to it.
- **Not an instruction for machine learning.** No network is trained;
  the RBM is only a family of rules.

## Connections

It underpins [THEORY-194](THEORY-194.md), which records that the information-maximizing
coarse-graining matched the known RG variables of the Ising and dimer
models: this is the argument for why such a coarse-graining should keep
the effective Hamiltonian short-ranged. It does not meet [THEORY-194](THEORY-194.md)'s
`promote_when`, which asks for a statement about the maximizer, not the
perfect case. The Lemma is a screening statement of the kind [THEORY-073](THEORY-073.md)
examines for Markov blankets, with the screening region likewise placed
in advance; that parallel is the reader's. It does not bear on
[QUESTION-025](../questions.d/QUESTION-025.md).

## Note of 2026-10-19: the Lemma, re-derived, and the narrowing

Written for the promotion audit's batch 019 ([ADR-047](../decisions.d/ADR-047.md)). The re-derivation
is in record/promotion-audit/decisions/THEORY-198.yaml and is restated
here.

Order the 1D chain E_L, B_L, V, B_R, E_R, with V one block, B_L and B_R the
buffer blocks beside it, and E_L, E_R the rest. H is V's coarse variable,
drawn from P(H | V), so H is independent of everything else given V.

1. **Full capture screens.** By the chain rule,
   I(V, H : E) = I(V : E) + I(H : E | V) = I(V : E), and also
   I(V, H : E) = I(H : E) + I(V : E | H). So full capture,
   I(H : E) = I(V : E), gives I(V : E | H) = 0.
2. **Locality.** Only neighbouring blocks interact, so the Gibbs measure is
   Markov along the chain and V separates the two sides: E_L ⊥ E_R | V.
3. **Combined.** For any v with P(v | h) > 0, step 1 gives
   P(e_L, e_R | h) = P(e_L, e_R | v), which step 2 splits into
   P(e_L | v) P(e_R | v). Step 1 again, marginalised, turns each factor into
   P(e_L | h) and P(e_R | h). So E_L ⊥ E_R | H.
4. **To the coarse lattice.** The coarse variables of E_L's blocks are drawn
   from E_L's spins alone, and likewise for E_R, so the independence passes
   to them. With the coarse buffer summed out,
   P(X′_{≤−2}, X′_{≥2} | X′_0) = P(X′_{≤−2} | X′_0) P(X′_{≥2} | X′_0).

No term of that marginal measure couples the two sides across X′_0.
Reading this as "the renormalized Hamiltonian gains no range" needs the
source's exclusion of fine-tuning: summing out the coarse buffer must not
exactly cancel a longer coupling. The title now says so. The
D-dimensional proof runs the same steps on hyperplanes of blocks. It
needs full capture for the hyperplane to amount to full capture by each
block, which the source calls reasonable and does not show, and the title
now states that too.

The promote_when asked what happens short of full capture, which this
account disclaims. It moves, unchanged, to [QUESTION-tmpavq90](../questions.d/QUESTION-tmpavq90.md).
