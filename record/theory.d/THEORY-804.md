---
number: 804
status: 'Proposed'
formerly:
- THEORY-tmpomt6b
promote_when: "A proof that I_ccs is continuous, together with a system whose redundancy is fixed independently of any measure's construction (by a mechanism both sides of the operational dispute accept, such as a shared bit copied to every source) on which I_ccs agrees and a rival with non-negative atoms does not; or an argument that settles whether unique information may depend on the source–source marginal, which decides between I_ccs and Bertschinger et al. It is weakened if subset equality, which fails for I_ccs as defined, cannot be restored by a modified sign rule without losing the properties it keeps. More examples judged by intuition do not settle it, nor does agreement on systems where every measure agrees."
title: "Ince's common change in surprisal is a correct measure of the redundancy among any number of sources, and the negative partial-information atoms it gives are local misinformation and mechanistic redundancy, not defects of the measure"
version: 1
tags:
- information-theory
- complex-systems
date: '2026-10-20'
source:
- LIT-1201
summary: >-
  The thesis [THEORY-714](THEORY-714.md)'s title carried before the promotion audit (batch 056) corrected and narrowed it to what I_ccs is and which properties it has. Ince (2017), [LIT-1201](../literature.d/LIT-1201.md), proposes I_ccs as the redundancy measure and reads its negative atoms as misinformation and mechanistic redundancy. Filed under [ADR-047](../decisions.d/ADR-047.md) v4. The re-derivation found that I_ccs fails subset equality, the property Ince argues licenses the lattice, which counts against the thesis without settling it.
extends:
- THEORY-714
answers:
- QUESTION-223
---


# THEORY-804: Ince's common change in surprisal is a correct measure of the redundancy among any number of sources, and the negative partial-information atoms it gives are local misinformation and mechanistic redundancy, not defects of the measure

## Source

Ince (2017), "Measuring multivariate redundant information with pointwise
common change in surprisal", [LIT-1201](../literature.d/LIT-1201.md), read in [NOTE-968](../notes.d/NOTE-968.md). The paper
offers I_ccs as a measure of redundancy that keeps symmetry,
self-redundancy, subset equality and identity for independent sources,
and gives up Harder et al.'s identity, monotonicity and non-negative
atoms. It reads the resulting negative atoms as "misinformation" and
"mechanistic redundancy" rather than as defects.

## What is asserted, and by whom

That I_ccs is the right redundancy function for the partial-information
lattice, and that the axioms it drops ought to be dropped. Ince argues it
from examples judged by intuition and from the claim that unique
information may depend on the source–source marginal, which Bertschinger
et al. ([LIT-1162](../literature.d/LIT-1162.md)) deny.

## What the record holds toward it

- [THEORY-714](THEORY-714.md) (Active): the definition, the three properties that hold,
  the failures of identity and monotonicity, and every discrete example,
  all re-derived.
- Against it: subset equality fails ([THEORY-714](THEORY-714.md)'s note of 2026-10-20, a
  two-source counterexample giving 0.0272 bit against 0.0073). Ince's
  proof cancels the co-information but not the sign rule. Since subset
  equality is what licenses restricting the measure to the lattice's
  antichains, the measure's rationale needs repair.
- For it, weakly: on XORCOPY I_ccs takes the negative atom exactly at the
  −1-bit bound [THEORY-713](THEORY-713.md) proves, rather than violating independent
  identity as I_min does.
- Continuity is conjectured and checked only locally.

## What would confirm or reject it

As the promote_when says: continuity plus agreement with a
mechanism-fixed redundancy where non-negative rivals disagree, or a
settled answer on the source–source marginal. [QUESTION-223](../questions.d/QUESTION-223.md) asks the same
thing as a question.
