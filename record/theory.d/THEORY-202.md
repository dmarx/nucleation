---
number: 202
status: Active
formerly:
- THEORY-tmp5vljo
title: 'In variational renormalization over general Boltzmann machines, neither a matched partition function nor Kadanoff''s exact trace condition makes a coarse-graining a renormalization: the first holds for joint Hamiltonians whose marginal is not the data, the second for hidden variables that do not interact with the system, so the variables a renormalization keeps must be fixed by a further stated condition'
version: 3
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted under ADR-047, batch 049.
    The counterexamples are re-derived below.
    The remaining Kadanoff-family question is QUESTION-205.
- version: 3
  date: '2026-10-20'
  note: >-
    Added the Raju, Machta and Sethna connection
    (THEORY-742). This provides a candidate
    relevance condition using the singular Fisher
    metric but does not settle QUESTION-205.
    The Active theorem is unchanged.
tags:
- natural-sciences
- representation-learning
date: '2026-10-09'
source:
- LIT-887
- LIT-882
summary: >-
  Lin and Tegmark (2016), [LIT-887](../literature.d/LIT-887.md), arXiv v1–v2 appendix, a part
  dropped from the journal text: a family of joint Hamiltonians with
  Z_tot = Z and the wrong marginal, and the remark that any non-interacting
  pair meets the trace condition. Under Mehta and Schwab's identification
  ([LIT-882](../literature.d/LIT-882.md)) the trace condition is a perfect fit of the data, so even an
  exact variational RG step leaves the coarse variables' meaning free. The
  restricted Boltzmann machine proper needs visible–visible terms for the
  second construction; that narrows the example, not the claim.
  Promoted on 2026-10-20 with both constructions re-derived. Whether the
  trace condition suffices inside Kadanoff's kernel families is
  QUESTION-205.
supports:
- CLAIM-152
---
<!-- inactive-ok-file: QUESTION-025 — Proposed or open; cited as the accounts this one extends and is set beside, and the question it does not answer -->

# THEORY-202: In variational renormalization over general Boltzmann machines, neither a matched partition function nor Kadanoff's exact trace condition makes a coarse-graining a renormalization: the first holds for joint Hamiltonians whose marginal is not the data, the second for hidden variables that do not interact with the system, so the variables a renormalization keeps must be fixed by a further stated condition

## Source

Lin and Tegmark (2016), [LIT-887](../literature.d/LIT-887.md): arXiv v1, Section III E and Appendix
A; arXiv v2, Section III E and Appendix B, including the response to
Schwab and Mehta; as read in [NOTE-688](../notes.d/NOTE-688.md). The appendix is absent from v3,
v4 and the Journal of Statistical Physics text. Schwab and Mehta's comment
on v1 (arXiv:1609.03541), not held, was read for that note. Mehta and
Schwab (2014), [LIT-882](../literature.d/LIT-882.md), Eqs. 18–22, for the identification under which the
trace condition is an exact fit of the data, as read in [NOTE-683](../notes.d/NOTE-683.md).

## What was actually shown

**A matched partition function is not a matched distribution** (v1
Appendix A, kept in v2). For a system with Hamiltonian H(y) and any
non-constant K(y), the joint Hamiltonian H(y, y′) = H(y) + H(y′) + K(y) +
ln Z̃, with Z̃ = Σ_y e^{−H(y)−K(y)}, has Z_tot = Z but marginal e^{−H−K}/Z̃,
not e^{−H}/Z. Adding a parameter dependence keeps every derivative of
ln Z matched as well, so every macroscopic observable agrees while the
distribution does not. Checked. Schwab and Mehta accepted this, called
the biconditional of their Eq. 8 a typo, and noted the example violates
the trace condition Tr_h e^{T(v,h)} = 1.

**The trace condition does not select the coarse variables either** (v2,
argued in one sentence: "any two systems that do not interact with each
other will trivially satisfy their trace condition"). Written out under
[LIT-882](../literature.d/LIT-882.md)'s identification T = −E + H: take E(v, h) = H(v) + H′(h) + ln Z′
with Z′ = Tr_h e^{−H′(h)}. Then T = −H′(h) − ln Z′, Tr_h e^T = 1 for every
v, the visible marginal equals the data exactly, and the coarse
Hamiltonian is H′, chosen freely and unrelated to the system. [LIT-882](../literature.d/LIT-882.md)
states that its identity holds for any Boltzmann machine, so the
construction lies inside the scope of its "exact" step. The working-out
is the reader's; the observation is the paper's.

What could have come out otherwise: the trace condition could have
implied a coupling between hidden and visible variables, or constrained
the coarse Hamiltonian beyond normalization; it does neither.

## What this does not say

- **Not that Kadanoff's schemes are unsound.** Kadanoff's kernels have a
  fixed form that couples each hidden spin to a block, which rules out the
  non-interacting construction. The claim is about the two conditions
  taken as criteria; whether they suffice inside his kernel families is
  [QUESTION-205](../questions.d/QUESTION-205.md).
- **Not that an exact restricted Boltzmann machine keeps irrelevant
  variables.** An RBM proper has no visible–visible couplings, so it
  cannot fit interacting data with W = 0; the second construction needs a
  general Boltzmann machine. For an RBM, exactness forces coupling but
  still says nothing about which functions of the data the hidden units
  carry.
- **Not that renormalization must be supervised.** The paper concluded
  that; [THEORY-194](THEORY-194.md) and [LIT-873](../literature.d/LIT-873.md) show a target can come from the data's
  spatial structure (the environment beyond a buffer) without labels.
  This account says only that some target has to be stated.
- **Not a correction of [LIT-882](../literature.d/LIT-882.md)'s Eqs. 18–22**, which use the pointwise
  condition and stand; it extends [THEORY-197](THEORY-197.md)'s "content only at the exact
  point" to "and not enough there either".
- **Nothing about attribute hierarchies or embeddings**, so it leaves
  [QUESTION-025](../questions.d/QUESTION-025.md) as it was; and no instruction for machine learning.

## Connections

Together with [THEORY-197](THEORY-197.md) (the correspondence is an identity of
parametrizations) and [THEORY-194](THEORY-194.md) (the variables a compression keeps are
set by what it must stay informative about), it closes the triangle of
the 2014–2018 dispute: the formalisms correspond, neither exactness nor
partition-function matching chooses the coarse variables, and an
objective with a relevance target does.

## Note of 2026-10-20: both counterexamples, re-derived

Re-derived for the promotion audit (batch 049, [ADR-047](../decisions.d/ADR-047.md) v2).

**A matched partition function.** Let Z = Σ_y e^{−H(y)}, take any
non-constant K, and put Z̃ = Σ_y e^{−H(y)−K(y)} and
H(y, y′) = H(y) + H(y′) + K(y) + ln Z̃. Then
Z_tot = (1/Z̃) Σ_y e^{−H(y)−K(y)} · Σ_{y′} e^{−H(y′)} = Z, while the marginal
of y is e^{−H−K}/Z̃, not e^{−H}/Z. If H carries a parameter, the identity
Z_tot = Z holds at every value, so every derivative of ln Z matches too.

**The trace condition.** Under Mehta and Schwab's identification
T(v, h) = −E(v, h) + H(v), take E(v, h) = H(v) + H′(h) + ln Z′ with
Z′ = Σ_h e^{−H′(h)} and H′ arbitrary. Then T = −H′(h) − ln Z′, so
Tr_h e^{T} = 1 for every v. The visible marginal is proportional to
e^{−H(v)}, the data exactly, and the coarse Hamiltonian
−ln Tr_v e^{T(v,h)−H(v)} = H′(h) + ln Z′ − ln Z is H′ up to a constant,
chosen freely. The construction needs a visible–visible term H(v) in E,
which a restricted Boltzmann machine lacks, and it couples no hidden spin
to any block, which Kadanoff's kernels require. The title is held to
general Boltzmann machines for that reason.

**A candidate target (2026-10-20).** [THEORY-742](THEORY-742.md) (Raju, Machta and 
Sethna) proposes keeping the singular part of the Fisher metric of the
bare couplings. This record's non-interacting construction fails that
target, since its coarse variables carry no Fisher information about the
couplings. The identity map passes it, so it is necessary, not
sufficient. It does not meet this account's promote_when, which asks
about variational RG and the trace condition.
