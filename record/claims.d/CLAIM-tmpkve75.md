---
status: Active
title: 'On a consistently connected system, Contextuality-by-Default and the sheaf criterion agree: a maximally connected coupling exists exactly when a global law has the contexts'' laws as its marginals'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from CLAIM-037 and filed Active at the owner's direction, carrying
    out the promotion audit's decision (record/promotion-audit/decisions/CLAIM-037.yaml,
    batch 002, ADR-047). CLAIM-037's defeat condition had this as its second
    disjunct. NOTE-600 states the coincidence as the reader's inference,
    not the paper's, so it is the record's own result, and it is written out
    here. CLAIM-037 keeps the methodological thesis and rests on this claim.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the proof below: a consistently connected system, with
  finitely many observables and outcomes, that is noncontextual by
  Contextuality-by-Default (Definition 3.4 of LIT-777) and has no global
  law in the sense of LIT-016, or the reverse.
tags:
- contextuality
- mathematics
date: '2026-10-19'
line:
- formal-apparatus
grounds:
- LIT-777
- LIT-016
- THEORY-012
summary: >-
  The record's derivation of what [NOTE-600](../notes.d/NOTE-600.md) marks as its own inference. In a
  consistently connected system, every observable has one distribution in
  all the contexts that contain it. Then each connection's maximal coupling
  makes its copies equal with probability 1 ([LIT-777](../literature.d/LIT-777.md), Theorem 3.3), so a
  maximally connected coupling is a joint law of one variable per
  observable, which is a global section in Abramsky and Brandenburger's
  sense ([LIT-016](../literature.d/LIT-016.md), [THEORY-012](../theory.d/THEORY-012.md)). Conversely, a global section gives such a
  coupling. The two criteria come apart only when marginals shift with
  context.
supports:
- CLAIM-037
---
<!-- inactive-ok-file: CLAIM-037 — Proposed; the methodological thesis this result was split from and that rests on it, cited as open -->

# CLAIM-tmpkve75: On a consistently connected system, Contextuality-by-Default and the sheaf criterion agree: a maximally connected coupling exists exactly when a global law has the contexts' laws as its marginals

## The claim

Take a system of finitely many observables q, each with finitely many
outcomes, measured in contexts c. In context c, the observables it contains
have a joint law P_c (the bunch), and R_q^c is q's random variable there.
The **connection** of q is {R_q^c : c contains q}. The system is
**consistently connected** when, for every q, all R_q^c have the same
distribution.

- **Sheaf criterion** ([LIT-016](../literature.d/LIT-016.md), [THEORY-012](../theory.d/THEORY-012.md)). The system is noncontextual
  when there is a law G on joint assignments of one outcome to every
  observable whose marginal on each context c is P_c.
- **Contextuality-by-Default** ([LIT-777](../literature.d/LIT-777.md), Def. 3.4). The system is
  noncontextual when there is a coupling of all the bunches, one jointly
  distributed copy T_q^c for each R_q^c, with each bunch's law preserved,
  whose subcoupling on every connection is a maximal coupling.

**On a consistently connected system, the two agree.**

## Proof

By Theorem 3.3 of [LIT-777](../literature.d/LIT-777.md) (Thorisson), the maximal coupling of a connection
has Pr[T_q^(c₁) = … = T_q^(c_k) = v] = min_i Pr[R_q^(c_i) = v] for every value
v. Under consistent connectedness each minimum is Pr[R_q = v], and these sum
to 1. So a coupling of a connection is maximal exactly when its copies are
equal with probability 1.

(CbD ⇒ sheaf.) Let T be a maximally connected coupling. On an event of
probability 1, T_q^c = T_q^(c′) for every q and every pair of contexts
containing it, so T_q is well defined there. The law G of (T_q)_q is a law
on global assignments. Its marginal on context c is the law of
(T_q^c)_(q∈c), which is P_c because T preserves each bunch.

(Sheaf ⇒ CbD.) Let G be a global law, and draw (X_q)_q from it. Set
T_q^c = X_q for each context c containing q. Each bunch (T_q^c)_(q∈c) has law
G's marginal on c, which is P_c. Each connection's copies are equal, so its
coincidence probability is 1 and its subcoupling is maximal.

The argument uses Theorem 3.3 for connections of any size k, so it covers
observables in more than two contexts. [CLAIM-069](CLAIM-069.md) raises that case.

## What it does not say

- **Anything about inconsistently connected systems.** There the criteria
  can diverge widely. [LIT-844](../literature.d/LIT-844.md) finds 71.1% of instances contextual by
  Contextuality-by-Default and 0.148% by the sheaf criterion that allows for
  signalling. Which to use there is [CLAIM-037](CLAIM-037.md)'s question.
- **That the sheaf criterion handles signalling.** It does not apply when
  marginals shift. [LIT-843](../literature.d/LIT-843.md)'s causal-past route is a different answer.
- **That a source states it.** [NOTE-600](../notes.d/NOTE-600.md) calls it "my inference rather than
  the paper's". This claim is that inference, proved.
