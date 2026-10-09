---
status: Active
title: 'noncommutativity, of events and of operations'
version: 3
history:
- version: 3
  date: '2026-10-08'
  note: >-
    A43 §2 and A48 §7.2 added a level below the others: noncommutativity of
    string concatenation, which is trivial. A52 dropped it again. Recorded
    here because it is what a language-model order effect is before controls.
- version: 2
  date: '2026-10-08'
  note: >-
    A40 §6.1 separated a third thing from both senses: order dependence in
    observed responses, measured by Δ_(A,B), which may come from framing,
    memory, learning, task demands or measurement disturbance. Version 1
    said observed order dependence establishes noncommutativity of the
    operations; version 2 says it is evidence for it, under a model.
tags:
- quantum-foundations
- probabilistic-modeling
date: '2026-10-08'
line: pragmatic-transport
summary: >-
  A30's disambiguation: noncommuting events or projectors (P_A P_B ≠ P_B
  P_A), which rule out a joint distribution for sharp measurements,
  versus noncommuting operations on probability states, which classical
  stochastic maps also show.
used_by:
- CLAIM-tmpbwst7
- CLAIM-tmpevciu
- CLAIM-tmpjwomz
- CLAIM-tmphq3fu
---
<!-- inactive-ok-file: CLAIM-tmpevciu CLAIM-tmphq3fu — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->
<!-- inactive-ok-file: CLAIM-tmpjwomz — Rejected; answered or abandoned, and cited as the history this entry answers -->

# TERM-tmpnvqh8: noncommutativity, of events and of operations

## Definition

Two senses, distinguished at A30 in answer to the owner's U13 ([CLAIM-tmpjwomz](../claims.d/CLAIM-tmpjwomz.md)):

1. **Of events.** Classical events are sets and their indicators commute;
   quantum projectors need not. "For projective measurements, noncommuting
   observables generally lack a joint measurement with the same sharp
   marginals."
2. **Of operations on probability states.** Classical stochastic maps can fail
   to commute ([CASE-tmp11vtm](../cases.d/CASE-tmp11vtm.md)).

3. **Order dependence in observed responses** (A40 §6.1): "Distinguish
   noncommutativity of state transformations from order dependence in observed
   responses", measured by Δ_(A,B) = d(P(Y | A→B), P(Y | B→A)), where "the
   observed difference may arise from framing effects, memory, learning, task
   demands, or measurement disturbance". The first two senses are properties of
   a model; this one is data.

4. **Of string concatenation** (A43 §2): "**Syntactic noncommutativity is
   trivial**": (c‖a)‖b ≠ (c‖b)‖a "is merely a fact about string concatenation".
   A substantive claim needs a difference in induced behaviour, separated from
   "artifacts of positional encoding, attention masks, recency, and instruction
   hierarchy". A48 §7.2 kept three levels (concatenation, effective operations,
   observed response distributions; "only the latter two have potential
   explanatory significance"). C1 Appendix C kept three tiers: "(i) syntactic
   noncommutation of prompt concatenation, (ii) noncommutation of inferred
   stochastic transition operators, and (iii) incompatibility of measurement
   observables in a quantum representation. A test of (i) never alone
   establishes (ii); even (ii) does not entail (iii)." The manuscript keeps
   (ii) and (iii) and does not mention concatenation.

## What it is not

Order dependence in judgements is evidence for the second sense, not the first. A30:
"observing order dependence is sufficient to establish noncommutativity of the
effective operations, but not sufficient to establish nonclassical
probability." The manuscript (§9) keeps the distinction.
