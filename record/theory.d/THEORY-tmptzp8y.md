---
status: Proposed
promote_when: >-
  A proof, read by the record, of Theorem 7.1 under the stated conditions,
  in the 1992 AT&T report or a later published correctness proof of
  delete-and-rederive for recursive Datalog. Examples or benchmarks do not
  settle a correctness claim; a measurement of the overestimate's size would
  settle only the separate cost question.
title: "For recursive Datalog views under set semantics, deleting every derived tuple that has any derivation through a deleted base fact, then restoring each deleted tuple that still has a derivation from the remaining relations, then adding what insertions derive, is stated to leave exactly the tuples derivable from the new base (E − Δ⁻) ∪ Δ⁺, with no derivation counts stored; the proof and the extension to stratified negation and aggregation are referred to an unpublished report, and the size of the overestimate is not measured"
version: 1
tags:
- databases
- logic
date: '2026-10-15'
source:
- LIT-tmpoi6js
answers:
- QUESTION-105
summary: >-
  Gupta, Mumick and Subrahmanian (1993), [LIT-tmpoi6js](../literature.d/LIT-tmpoi6js.md), read in [NOTE-tmpgv5ap](../notes.d/NOTE-tmpgv5ap.md).
  DRed runs stratum by stratum: semi-naive Δ⁻-rules compute an overestimate
  of deletions, δ⁺-rules put back those with a derivation in the reduced
  database, and Δ⁺-rules add insertions. Theorem 7.1 states the result
  contains t if and only if t has a derivation in (E − Δ⁻) ∪ Δ⁺; the proof
  is in a 1992 AT&T report the record has not seen. The paper asserts, and
  does not show, that DRed handles stratified negation, aggregation and rule
  changes, that it beats the PF algorithm by up to an order of magnitude,
  and that it is slower than counting on nonrecursive views.
---

# THEORY-tmptzp8y: For recursive Datalog views under set semantics, deleting every derived tuple that has any derivation through a deleted base fact, then restoring each deleted tuple that still has a derivation from the remaining relations, then adding what insertions derive, is stated to leave exactly the tuples derivable from the new base (E − Δ⁻) ∪ Δ⁺, with no derivation counts stored; the proof and the extension to stratified negation and aggregation are referred to an unpublished report, and the size of the overestimate is not measured

## Source

Gupta, Mumick and Subrahmanian (1993), [LIT-tmpoi6js](../literature.d/LIT-tmpoi6js.md), SIGMOD '93 extended
abstract, Section 7, read in full in [NOTE-tmpgv5ap](../notes.d/NOTE-tmpgv5ap.md).

## What was actually shown

Stated, not proved. Step 1: δ⁻(p) :- s_1 & … & s_{i−1} & δ⁻(s_i) &
s_{i+1} & … & s_n over the old relations, iterated to fixpoint, and the
result removed from P. This is semi-naive deletion, which ignores other
derivations: "Semi-naive therefore computes an overestimate of the tuples
that actually need to be deleted." Step 2: δ⁺(p) :- δ⁻(p) & s_1^ν & … &
s_n^ν puts back deleted tuples that still have a derivation, iterated.
Step 3: Δ⁺-rules over the new relations add inserted consequences. The
program is processed stratum by stratum.

Theorem 7.1 (page image): "The new derived view computed by the DRed
algorithm contains tuple t if and only if t has a derivation in the
database E^ν = (E − Δ⁻) ∪ Δ⁺." "This three step process is formalized as
an algorithm, and proved correct, in [GMS92]." "Only set semantics can be
used for this algorithm."

Could have come out otherwise: a recursive program and change after which
the maintained view differs from the view recomputed on the new base would
refute Theorem 7.1.

## What this does not say

- **What it costs.** The overestimate can include everything downstream of
  a deleted fact, and the paper gives no bound and no measurement. Its
  comparisons (better than PF "by an order of magnitude", worse than
  counting on nonrecursive views) are asserted, with examples left to the
  full paper.
- **That negation, aggregation and rule changes are handled as shown.**
  They are described as handled in [GMS92]; this paper gives only the
  positive case.
- **Anything under duplicate semantics.**
- **That support is remembered.** Nothing about why a tuple held is kept;
  support is recomputed at each revision from what remains.
- **That incremental maintenance pays.** The paper calls it "only a
  heuristic": recomputation can be cheaper when a change is large.

## Connections

- [QUESTION-105](../questions.d/QUESTION-105.md): where support can be cyclic, the paper keeps no summary of
  support at all and rechecks it at revision time; the retained state is
  the base, the rules and the old view.
- [THEORY-tmp2ber8](THEORY-tmp2ber8.md): the nonrecursive case, maintained with one count per
  tuple.
- [THEORY-347](THEORY-347.md) and [THEORY-353](THEORY-353.md): here the revision is fixed by the change to
  the base, so no selection function or ordering is needed.
- [CLAIM-303](../claims.d/CLAIM-303.md): dependency tracking paid at revision time instead of at
  filing.
