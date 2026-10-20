---
number: 16
status: Open
formerly:
- QUESTION-tmpk199j
title: 'Under what conditions does iterated reconstruction preserve, or progressively destroy, task-relative sufficiency?'
version: 1
tags:
- information-theory
- philosophy-of-language
date: '2026-10-08'
line: pragmatic-transport
refines:
- QUESTION-002
summary: >-
  A86 §10, the second of three "target results". Neither it nor the
  other two was proved or stated in C6 or the manuscript, which has the
  data-processing inequality for a fixed Markov chain and a drift bound,
  not a sufficiency result.
refined_by:
- QUESTION-010
- QUESTION-189
---
<!-- inactive-ok-file: CLAIM-081 CLAIM-182 THEORY-155 THEORY-157 THEORY-194 — listed as material that may bear on this question, not as settled -->
<!-- inactive-ok-file: CLAIM-050 CLAIM-056 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->
<!-- inactive-ok-file: CLAIM-199 CLAIM-258 — Proposed; cited in a note of 2026-10-12 as open, for what each holds, not as settled -->

# QUESTION-016: Under what conditions does iterated reconstruction preserve, or progressively destroy, task-relative sufficiency?

## Why it is a question

A86 §10 named three results the theory should aim at: (a) compression that
preserves a chosen family of decision problems; (b) when iterated
reconstruction preserves or destroys sufficiency; (c) how much decoder
adaptation compensates for lower rate ([QUESTION-020](QUESTION-020.md)). This is (b).

## Where it stands

The manuscript §8 has I(Z;U_(n+1)) ≤ I(Z;U_n) for a fixed Markov chain, with the
caveat that added evidence changes the graph, and a bound on distributional
error ([CLAIM-056](../claims.d/CLAIM-056.md)). Neither says when a chain keeps the Blackwell sufficiency for a
family Q of communicative decisions ([CLAIM-050](../claims.d/CLAIM-050.md)). A garbling of a garbling is a
garbling, so sufficiency for Q can only decline along a pure chain. The open
part is the case the manuscript flags, interpreters with side information, where
a retelling "can then improve an audience's task performance" (A86 §3).

## Note of 2026-10-11: material in the record that may bear on this

A synthesis review of 2026-10-11 found these entries bearing on this
question without being linked to it. Each is listed for what its title
says; none has yet been assessed as an answer, and none is linked by
`answers`.

- [THEORY-157](../theory.d/THEORY-157.md): The classical theorems on sufficient statistics need only
  the copy/discard structure of Markov kernels:…
- [CLAIM-081](../claims.d/CLAIM-081.md): Retaining information about the ancestor and drifting in the
  population's distribution are different…
- [THEORY-155](../theory.d/THEORY-155.md): Iterated learning by Bayesian agents who sample from the
  posterior converges to the shared prior
- [CLAIM-182](../claims.d/CLAIM-182.md): Storage is not anchoring, addressability is: a structure that
  is kept but cannot be pointed at part by…
- [THEORY-194](../theory.d/THEORY-194.md): For the 1D and 2D Ising and 2D dimer models, the block
  coarse-graining that maximizes mutual information…
- [THEORY-198](../theory.d/THEORY-198.md): For a finite-range lattice Hamiltonian, a block coarse-
  graining that keeps all the mutual information the…

[CLAIM-182](../claims.d/CLAIM-182.md) bears from the other end: side information that is stored is not
thereby used unless it is addressable.

## Note of 2026-10-12: entries on the side-information case

The note of 2026-10-11 lists material as unassessed. PR [#121](https://github.com/dmarx/nucleation/issues/121)'s round of
2026-10-10 filed three entries on the part this question holds open,
interpreters with side information. [CLAIM-199](../claims.d/CLAIM-199.md), a proposal, separates
what a rendering makes possible from what a given receiver can use, and
holds that a garbling can raise a receiver's usable information "but never
above what the source makes possible". [CLAIM-258](../claims.d/CLAIM-258.md), an open counter,
says a translator with context knowledge yields a rendering that is not a
garbling of the source, and suggests handling the side-information case by
a measure such as deficiency rather than by Blackwell's order.
[CLAIM-237](../claims.d/CLAIM-237.md), granted, says that for a contextual model what is open is
the converse direction or a deficiency bound. None is linked by `answers`.

## Note of 2026-10-14: a bounded-degradation instance

[THEORY-289](../theory.d/THEORY-289.md), filed from [LIT-971](../literature.d/LIT-971.md), is an instance of a chain anchored to
the source in which degradation is bounded. When each round of a linear
regression is refit to labels from the previous fit and every earlier
round's data is kept, test error is bounded at π²/6 times the first fit's;
when the data are replaced, it grows linearly. The loss is bounded, not
stopped: every round adds error. What is retained is the real sample, not
an interpreter's side information, and every model is still a garbling of
the real data, for one squared-error task rather than a family Q. It
carries no `answers` edge.
