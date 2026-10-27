---
number: 387
status: Active
formerly:
- THEORY-tmptzp8y
title: 'For positive recursive Datalog views under set semantics, deleting every derived tuple that has any derivation through a deleted base fact, then restoring each deleted tuple that still has a derivation from what remains, then adding what insertions derive, leaves exactly the tuples derivable from the new base (E − Δ⁻) ∪ Δ⁺, with no derivation counts stored; the extension to stratified negation and aggregation is asserted, not shown, and the size of the overestimate is not measured'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted at the owner's direction, carrying out the
    promotion audit's decision for THEORY-387 (batch 042, ADR-047 v2).
    The proof of Theorem 7.1 the paper refers to an unseen report was
    supplied for positive recursive programs by re-derivation, in the
    dated note below, which meets the former promote_when for that case.
    The title now asserts the result for positive programs and reports
    the extension to stratified negation and aggregation as asserted, not
    shown. That extension and the size of the overestimate move to
    QUESTION-188.
tags:
- databases
- logic
date: '2026-10-15'
source:
- LIT-1114
summary: >-
  Gupta, Mumick and Subrahmanian (1993), [LIT-1114](../literature.d/LIT-1114.md), read in [NOTE-915](../notes.d/NOTE-915.md).
  DRed runs stratum by stratum: semi-naive Δ⁻-rules compute an overestimate
  of deletions, δ⁺-rules put back those with a derivation in the reduced
  database, and Δ⁺-rules add insertions. Theorem 7.1 states the result
  contains t if and only if t has a derivation in (E − Δ⁻) ∪ Δ⁺; the proof
  is in a 1992 AT&T report the record has not seen. The paper asserts, and
  does not show, that DRed handles stratified negation, aggregation and rule
  changes, that it beats the PF algorithm by up to an order of magnitude,
  and that it is slower than counting on nonrecursive views.
bears_on:
- QUESTION-105
---

# THEORY-387: For positive recursive Datalog views under set semantics, deleting every derived tuple that has any derivation through a deleted base fact, then restoring each deleted tuple that still has a derivation from what remains, then adding what insertions derive, leaves exactly the tuples derivable from the new base (E − Δ⁻) ∪ Δ⁺, with no derivation counts stored; the extension to stratified negation and aggregation is asserted, not shown, and the size of the overestimate is not measured

## Source

Gupta, Mumick and Subrahmanian (1993), [LIT-1114](../literature.d/LIT-1114.md), SIGMOD '93 extended
abstract, Section 7, read in full in [NOTE-915](../notes.d/NOTE-915.md).

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
- [THEORY-362](THEORY-362.md): the nonrecursive case, maintained with one count per
  tuple.
- [THEORY-347](THEORY-347.md) and [THEORY-353](THEORY-353.md): here the revision is fixed by the change to
  the base, so no selection function or ordering is needed.
- [CLAIM-303](../claims.d/CLAIM-303.md): dependency tracking paid at revision time instead of at
  filing.

## Note of 2026-10-19: Theorem 7.1 for positive programs, re-derived

The paper states Theorem 7.1 and refers its proof to a report the record
has not found. The promotion audit (batch 042) re-derived it for positive
recursive Datalog under set semantics. Write M for the old view, M′ for
what E − Δ⁻ derives and M″ for what (E − Δ⁻) ∪ Δ⁺ derives; the rules are
monotone, so M′ lies in both M and M″.

1. *Overestimate.* The Δ⁻-rules, run on the old relations from the
   deleted base facts, mark exactly the tuples of M that have some
   derivation using a deleted fact. A tuple of M not in M′ has only such
   derivations and at least one, so it is marked. What survives unmarked
   therefore lies in M′, and includes every base fact of E − Δ⁻.
2. *Rederive.* Restoring marked tuples that have a rule instance with its
   body in the current relations, until nothing changes, yields exactly
   M′. Everything restored is derivable from the survivors, which lie in
   M′, and M′ is closed under the rules. Conversely, by induction on
   derivation height from E − Δ⁻, every tuple of M′ is present: its body
   is present by hypothesis, and it is either unmarked or restored by its
   rule instance.
3. *Insert.* Adding what the insertions derive, from M′ and Δ⁺, gives
   the least set containing them that is closed under the rules, which is
   M″.

For a positive program, processing strata in order, with each lower
stratum's net changes as the next one's deletions and insertions, applies
the argument stratum by stratum. No derivation counts are used. Set
semantics is used in the second step, where a tuple is restored once
whatever its number of derivations. Under negation a deletion can add
tuples, and the argument does not apply; that case is [QUESTION-188](../questions.d/QUESTION-188.md).
