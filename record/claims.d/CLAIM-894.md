---
number: 894
status: Proposed
formerly:
- CLAIM-tmp9xo66
title: 'Own-future target leaves three conditions'
statement: >-
  If the declared target of an effective description is the coarse
  variable's own future, then for a linear coarse-graining of a stationary
  linear Gaussian process predictive sufficiency and fidelity of the
  memoryless reduced model are each equivalent to dynamical independence
  together with memory closure, so the five-condition table has three
  conditions, independence, memory closure and tractability
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the proof, or a stationary linear Gaussian process and
  linear coarse-graining Y for which, with target Y's own future, the
  current value Y_t is sufficient against the full past for Y_{t+1} while
  Y fails dynamical independence or memory closure, or the reverse.
tags:
- mathematics
- complex-systems
date: '2026-11-22'
line:
- formal-apparatus
bears_on:
- QUESTION-252
uses:
- TERM-065
grounds:
- CASE-327
complements:
- CLAIM-893
summary: >-
  The alternative declaration of [LEAD-173](../leads.d/LEAD-173.md)'s target, filed beside
  [CLAIM-893](CLAIM-893.md) because which target [QUESTION-252](../questions.d/QUESTION-252.md) means is the owner's
  choice. With Z = Y, sufficiency of Y_t against the full past is D and M
  at once, which is A3's warning that P and D need different conditioning
  sets, proved. Checked on 30 random models. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-327 CLAIM-893 — new; the study whose regime this varies and the claim under the primary declaration -->

# CLAIM-894: Own-future target leaves three conditions

## The claim

Take the regime of [CASE-327](../cases.d/CASE-327.md) with one change: the target is
Z_{t+1} = Y_{t+1}. Write X⁻ for the full past, Y⁻ for Y's own past.

- **P ⇒ D ∧ M.** P says E[Y_{t+1} | X⁻] = E[Y_{t+1} | Y_t]. Since Y_t is a
  function of Y⁻ and Y⁻ of X⁻, the tower property gives
  E[Y_{t+1} | Y⁻] = E[E[Y_{t+1} | X⁻] | Y⁻] = E[Y_{t+1} | Y_t], which is M
  (Y is Markov in its own law, R(k) = Ω^kR(0)); and then
  E[Y_{t+1} | X⁻] = E[Y_{t+1} | Y⁻], which is D. In the Gaussian case the
  conditional means fix the conditional laws.
- **D ∧ M ⇒ P.** Chain the two equalities.
- **A ⇔ D ∧ M.** At k = 1 A's defect is P's, so A ⇒ P ⇒ D ∧ M; and D ∧ M
  gives E[Y_{t+k} | X⁻] = Ω^kY_t, which is the reduced model with H = Ω,
  so A holds at every horizon and tolerance (with ε > 0, A ⇒ P fails and
  A is only implied by D ∧ M).

So under this declaration P and A are not conditions beside D and M but
their conjunction, and the leave-one-out design has three entries: D, M and
C. In VAR(1), with D ⇒ M ([CLAIM-389](CLAIM-389.md)), P is D alone. This is A3's warning in
[QUESTION-252](../questions.d/QUESTION-252.md), "P and D must have different conditioning sets ... Otherwise
the distinction risks collapsing by definition", shown to bite exactly.

## What it does not say

- **Not that this is the right declaration.** [CLAIM-893](CLAIM-893.md) takes an
  external target and finds the five separate. Which one [QUESTION-252](../questions.d/QUESTION-252.md)
  means is the owner's call; the two are alternatives of declaration, not
  rival readings of one fact.
- **Not about targets that are only partly Y.** A target that reads part
  of Y, or Y plus something else, gives intermediate tables.
