---
status: Active
title: 'In Contextuality-by-Default 2.0, whether a system of non-binary variables is contextual depends on which variables represent the measurements: coarse-graining can turn a noncontextual system into a contextual one, while for connections of two variables, and for consistently connected systems, CbD 1.0 and 2.0 agree'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-168 and filed Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-168.yaml, batch 005, ADR-047).
    THEORY-168's promote_when calls the coarse-graining failure "already
    proved". It asks for a second proof of the nominal-dominance theorem and
    a worked CbD 1.0 non-heredity case, neither of which bears on this
    result. LIT-831's Example 1 was checked again for the split, and a
    fine-grained witness of the record's own is given below. THEORY-168
    keeps the asserted parts and extends this one.
tags:
- contextuality
- mathematics
date: '2026-10-19'
source:
- LIT-831
summary: >-
  Dzhafarov & Kujala (2017), [LIT-831](../literature.d/LIT-831.md), Examples 1–3 and Section 4, read in
  [NOTE-643](../notes.d/NOTE-643.md) (claims C4 and C6). Under multimaximal couplings, lumping values
  of non-binary variables can destroy every multimaximal coupling, so a
  noncontextual system becomes contextual. The verdict on a fixed set of
  measurements therefore depends on which variables represent them. For
  connections of two variables, hence cyclic systems, and for consistently
  connected systems, the 1.0 and 2.0 definitions agree. It does not say the
  coupling choice changes verdicts in larger connections, which is
  [THEORY-168](THEORY-168.md)'s asserted part.
extended_by:
- THEORY-168
---
<!-- inactive-ok-file: THEORY-168 — Proposed; the account this result was split from and that extends it, cited as open -->

# THEORY-tmpm565o: In Contextuality-by-Default 2.0, whether a system of non-binary variables is contextual depends on which variables represent the measurements: coarse-graining can turn a noncontextual system into a contextual one, while for connections of two variables, and for consistently connected systems, CbD 1.0 and 2.0 agree

## Source

Dzhafarov & Kujala (2017), *Contextuality-by-Default 2.0* ([LIT-831](../literature.d/LIT-831.md)),
Section 4 and Examples 1–3, as read in [NOTE-643](../notes.d/NOTE-643.md) (claims C4, "strong
(immediate from the definitions)", and C6, "strong (counterexamples)").

## What was actually shown

Contextuality-by-Default gives each measurement a separate random variable
in each context. A connection is the set of variables that measure one
content in different contexts. CbD 2.0 calls a system noncontextual when
some coupling of all its variables agrees with each context's joint
distribution and is multimaximal on each connection. Multimaximal means
every subset of the connection is maximally coupled, which is equivalent
to every pair being maximally coupled ([LIT-831](../literature.d/LIT-831.md) Theorem 5).

**Coarse-graining can create contextuality (Examples 1–3).** Take one
connection of three 3-valued variables, each alone in its context, with
masses (0, ½, ½), (½, 0, ½) and (½, ½, 0) on {a, b, c}. A maximal coupling
of a pair puts on agreement the sum of the smaller masses, here ½: at c for
the first two variables, at b for the first and third, and at a for the
second and third. The three events {X = Y = c}, {X = Z = b} and
{Y = Z = a} are pairwise disjoint, since any two of them would require one
variable to take two values. Three disjoint events cannot each have
probability ½, so no coupling is pairwise maximal, and the system is
contextual. In [LIT-831](../literature.d/LIT-831.md) this connection is the lumping of a 6-valued one
that has multimaximal couplings (Examples 2 and 3).

A witness of the record's own shows the same thing. Split each value in
two: X has mass ½ on b and ½ on c, Y has ½ on a′ and ½ on c′, and Z has ½
on a and ½ on b′. No two variables share a value, so every pairwise
maximum is 0 and every coupling is multimaximal. That system is
noncontextual. Lumping a with a′, b with b′ and c with c′ gives the
contextual system above.

**Where the two versions agree (Section 4).** For a connection of two
variables, the only subset of two or more variables is the whole
connection, so a maximal coupling of the connection (CbD 1.0) and a
multimaximal one (CbD 2.0) are the same thing. Cyclic systems have such
connections throughout. In a consistently connected system every
connection's variables are identically distributed, so both versions
require them to be equal with probability 1, and both reduce to the
traditional definition.

What could have come out otherwise: multimaximality could have survived
the lumping of values. It does not, because lumping can raise each pair's
maximal agreement, and the raised agreements of different pairs can fall at
values that no single outcome reaches at once.

## What this does not say

- **That maximal and multimaximal couplings disagree on larger
  connections.** [LIT-831](../literature.d/LIT-831.md) says they do on Kochen–Specker systems, and that
  the 1.0 definition is not hereditary, but gives no worked example. That
  stays in [THEORY-168](THEORY-168.md).
- **Anything about dichotomizations.** The nominal-dominance theorem for
  all splits of a content-sharing pair ([LIT-790](../literature.d/LIT-790.md), Theorem 4.6) is
  [THEORY-168](THEORY-168.md)'s, and is waiting on a checked second proof.
- **That a verdict is wrong.** The papers present the representation as
  the analyst's choice. This result says only that the choice matters.
- **Anything about the sheaf framework.** There, coarse-graining outcomes
  cannot raise the contextual fraction ([LIT-265](../literature.d/LIT-265.md), Theorem 2). The contrast
  is between frameworks, and these papers do not draw it.
