---
number: 67
status: Superseded
formerly:
- CLAIM-tmpj4s3r
title: 'If a transport exactly intertwines a generating set of communicative operations, it preserves every trajectory composed from them'
version: 1
role: thesis
defeated_if: >-
  A transport intertwines each generator exactly yet fails to intertwine
  some composition of them.
tags:
- mathematics
- philosophy-of-language
date: '2026-10-08'
line: pragmatic-transport
superseded_by:
- CLAIM-106
uses:
- TERM-033
summary: >-
  A49's "compositional preservation theorem", proposed as the paper's
  organizing result. True as algebra; superseded at U20 when the owner
  objected that fidelity is similarity within ε, not equivalence. Its
  rationale, test generators and infer trajectories, lives on in the
  drift bound.
objected_by:
- CLAIM-106
---
<!-- inactive-ok-file: CLAIM-056 CLAIM-063 CLAIM-106 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-067: If a transport exactly intertwines a generating set of communicative operations, it preserves every trajectory composed from them

## The claim

A49: ΦA_i = B_iΦ for all i implies ΦA_(i_k)⋯A_(i_1) = B_(i_k)⋯B_(i_1)Φ. "This is
elementary mathematically, but it gives the theory an organizing result:
**preservation of a generating set of communicative operations entails
preservation of every trajectory constructed by composing those operations.**"
The rationale: "we cannot test every possible communicative trajectory. We need
a principled account of when fidelity established on a smaller set of operations
generalizes to compositions we haven't directly evaluated." A49's Proposition 2
put this together with the commutator identity ([CLAIM-063](CLAIM-063.md)).

## Why it was replaced

U20 ([CLAIM-106](CLAIM-106.md)): "presenting this as an equivalence might be too constraining
... that's just a similarity constraint, not an equivalence." The theorem is not
false; its hypothesis is the wrong idealization. A50 kept the rationale in
approximate form: generator-level errors bound trajectory-level error through
the Lipschitz recursion ([CLAIM-056](CLAIM-056.md)).
