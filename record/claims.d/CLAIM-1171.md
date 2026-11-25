---
number: 1171
status: Proposed
formerly:
- CLAIM-tmpt8pvt
title: 'New queries cannot change existing implications'
statement: >-
  In a time-indexed incidence of queries and answers with fixed meanings, a
  new query cannot change the implications or the compatibility among the
  existing queries, and a new answer can only remove implications and add
  compatible sets; implications among existing queries appear only when
  answers are lost or made unaffordable or when what counts as an adequate
  answer is revised
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the argument: a formal context with fixed incidence on the
  existing queries and answers in which adding a query changes Ψ(S) for
  some S among the existing queries, or adding an answer makes some
  implication S → T among existing queries hold that did not.
tags:
- mathematics
- logic
- society-and-governance
date: '2026-11-23'
line:
- realizability
- formal-apparatus
rests_on:
- CLAIM-564
summary: >-
  A gap fill ([ADR-137](../decisions.d/ADR-137.md)), a correction to A50 §6 of the exchange "Explain
  First Contact RL" (2026-11-23), which builds a time-indexed incidence
  I_t ⊆ Q_t × A_t on [CLAIM-564](CLAIM-564.md)'s Galois connection and says that "the
  introduction of new questions or answers can change the apparent
  implication relations among existing demands." With meanings fixed, a
  new question cannot, and a new answer can only remove implications.
  Checked by brute force with python3 -I. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---

# CLAIM-1171: New queries cannot change existing implications

## The step corrected

A50 §6 takes queries Q and answers A with q I a when a adequately answers
q, Ψ(S) the answers meeting every query in S and Φ(U) the queries every
answer in U meets: [CLAIM-564](CLAIM-564.md)'s antitone Galois connection. It distinguishes
query development, "new questions enter the formal context", from answer
development, "new capabilities or organizational configurations enter the
answer space", and says: "And the introduction of new questions or answers
can change the apparent implication relations among existing demands."
A50 then cautions that monotonic results fail when a reflexive game can
"revise or replace queries, alter acceptance criteria, and change the
target".

## The result

An implication S → T among queries holds when Ψ(S) ⊆ Ψ(T); a set S is
compatible when Ψ(S) is non-empty. With the incidence on existing pairs
unchanged:

1. **A new query** adds a column. Ψ(S) for S among the existing queries is
   computed from their columns alone, so no implication or compatibility
   among them changes. What a new query does is split answers previously
   alike (A50's "reveal a distinction between organizations previously
   considered equivalent", which is [CLAIM-574](CLAIM-574.md)'s monotonicity) and add new
   sets containing itself.
2. **A new answer** adds a row. Each Ψ(S) can only gain it, so a compatible
   set stays compatible and a failing implication stays failing (its
   witness answer is still there). It can make an incompatible set
   compatible (A50's "One new answer might satisfy several previously
   incompatible demands") and can break an implication, never create one.
3. **Implications among existing queries are created** only by losing
   answers, which includes their becoming unaffordable ([CLAIM-564](CLAIM-564.md): "fewer
   affordable configurations can only add implications"), or by revising
   the incidence, that is, what counts as an adequate answer.

So A50's sentence holds for answers only in one direction and does not
hold for questions; the change it has in view comes from losses and
revisions, which is its own caution.

## The check

`python3 -I`, 2026-11-23: 400 random contexts of 4 queries and 5 answers,
each enumerating all pairs of query subsets. Adding a query changed the
implications or compatible sets among the old queries in 0 of 400, and
merged two previously distinguished answers in 0. Adding an answer created
a new implication in 0, removed one in 206, removed a compatible set in 0.
Dropping an answer created a new implication in 226; flipping one
incidence did so in 210.

## Standing

Proposed, the assistant's. Elementary, but it fixes which side of the
query–answer game can create the dependencies among demands that
[CLAIM-564](CLAIM-564.md)'s lattice records.
