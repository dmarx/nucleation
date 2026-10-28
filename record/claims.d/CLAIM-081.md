---
number: 81
status: Proposed
formerly:
- CLAIM-tmpn361s
title: 'Retaining information about the ancestor and drifting in the population''s distribution are different profiles: a chain can forget where it started while staying far from the original, so convergence is not preservation and transmission is not degradation'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Warrant corrected from demonstrated to interpretive, carrying out the
    promotion audit's batch 029 (the ADR-040 parent sweep, ADR-047).
    Under ADR-040 its general content was filed as CLAIM-270, which is
    Active. What this claim keeps is the reading of serial reconstruction
    as such a chain, through CLAIM-056, which is interpretive, and its
    defeat condition is a universal over real serial reconstruction with
    no observation under it. Under ADR-043 that is interpretive, and a
    warrant is not inherited along rests_on. Status, statement and defeat
    condition are unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  In serial reconstruction, ancestral information retention and
  distributional drift from the source always move together, so that one
  profile predicts the other.
tags:
- information-theory
- philosophy-of-language
date: '2026-10-08'
line: pragmatic-transport
works:
- what-survives-translation
rests_on:
- CLAIM-056
- CLAIM-270
summary: >-
  C1 Appendix D's two profiles and E1's two forgettings (A59). The
  manuscript §11 keeps it in one line ("converge in surface form while
  diverging in ancestral information"); the named profiles and the
  synthetic construction are gone.
illustrated_by:
- CASE-017
---
<!-- inactive-ok-file: CLAIM-056 CLAIM-068 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-081: Retaining information about the ancestor and drifting in the population's distribution are different profiles: a chain can forget where it started while staying far from the original, so convergence is not preservation and transmission is not degradation

## The claim

C1 Appendix D: "A directed information-retention profile can record
I(G_j(U_0);U_n) for pragmatic features G_j, while a distributional drift profile
uses D[P(G_j(U_n)),P(G_j(U_0))]. The quantities answer different questions:
information about a particular ancestor versus evolution of the population's
feature distribution. Separating them prevents equating transmission with
degradation."

A59, from [CASE-017](../cases.d/CASE-017.md): the chains "distinguish two phenomena that are easy to
conflate: **forgetting the original** and **forgetting which initial state the
chain started in**. In one contractive model, the separation between chains
initialized in different pragmatic states approached zero, while the resulting
distribution remained substantially different from the original ...
transmission converged toward a common convention rather than faithfully
preserving the starting message."

Manuscript §11: "An iterated chain may converge in surface form while diverging
in ancestral information"; §8: the data-processing inequality "is not a theorem
that messages get less comprehensible".

A86 §3 (U31) gave it in information terms: the telephone game is progressive
garbling, and "a message can become more legible while becoming less informative
about what originally happened". "Increasing conventionality alongside
decreasing information about the origin" would be "a natural
information-theoretic explanation of cultural attractors", and the same reply
added the caveat: "The Markov assumption matters here." The manuscript keeps the
caveat (§8) and drops the attractor explanation.

## What it does not say

Which profile matters for fidelity: that depends on whether the question is
about the original or about the convention ([CLAIM-068](CLAIM-068.md)).

The crystallized argument's form (A110 §20): "**The emergence of stable meaning
within a community need not imply faithful retention of ancestral meaning.**" The
manuscript keeps the point and adds a caveat the argument lacked: "adding
independent historical evidence to later interpreters changes the Markov graph
and invalidates a naive application of the inequality" (§8).

## Note of 2026-10-13: the general content is filed separately

Under [ADR-040](../decisions.d/ADR-040.md), the distinction between retention and drift is filed on its own as [CLAIM-270](CLAIM-270.md), in the
formal-apparatus line, resting on no claim. This claim now rests on it for
the general content, and keeps [CLAIM-056](CLAIM-056.md), for reading the chain as a reconstruction chain. Claims in other lines that need
only the general content cite [CLAIM-270](CLAIM-270.md), so setting pragmatic-transport aside
does not take it from them.
