---
number: 12
status: Active
formerly:
- THEORY-tmpjo7qe
title: 'An empirical model is Kochen–Specker-noncontextual exactly when its context distributions glue to one global distribution, and since signed global sections always exist for no-signalling models, negative probability does not mark contextuality'
version: 2
history:
- version: 2
  date: '2026-09-27'
  note: >-
    A "does not say" line added: the cohomological witness of Abramsky,
    Mansfield & Barbosa (LIT-277) is sufficient, not necessary. The
    claim itself is unchanged.
tags:
- contextuality
- quantum-foundations
- mathematics
date: '2026-09-27'
source:
- LIT-016
summary: >-
  Abramsky & Brandenburger (2011), [LIT-016](../literature.d/LIT-016.md), Thm 8.1 with Prop 3.1, and Thms
  5.4 and 5.9 — proved for finite measurement scenarios with no-signalling
  built into the definition. The graded version (the contextual fraction) and
  the review that places this formulation among its equivalents are seeded,
  not read.
extended_by:
- THEORY-011
- THEORY-014
- THEORY-015
---
<!-- inactive-ok-file: LIT-263 — Deferred: filed and skimmed on 2026-09-27 while bringing the contextuality threads together; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-265 — Deferred: filed and skimmed on 2026-09-27 while bringing the contextuality threads together; the theories citing it are Proposed until it is read closely -->

# THEORY-012: An empirical model is Kochen–Specker-noncontextual exactly when its context distributions glue to one global distribution, and since signed global sections always exist for no-signalling models, negative probability does not mark contextuality

## Source

Abramsky & Brandenburger (2011), [LIT-016](../literature.d/LIT-016.md), §§2.2–2.5, Prop 3.1, Props 4.2–4.4, Thms 5.4 and 5.9, Props 6.1 and 6.3, Thm 8.1 ([NOTE-016](../notes.d/NOTE-016.md)). Seeded, not read: Abramsky, Barbosa & Mansfield's contextual fraction ([LIT-265](../literature.d/LIT-265.md)) and Budroni et al.'s review ([LIT-263](../literature.d/LIT-263.md), §IV.A.1, which calls local consistency "the sheaf condition" and lists the sheaf, marginal-problem, polytope and graph formulations as substantially equivalent).

## What was actually shown

An empirical model is a family of distributions, one per maximal context of jointly performable measurements, that agree on overlaps; the agreement is no-signalling, and it is part of the definition (§2.5). The model is noncontextual when there is a global section: one distribution on joint outcome assignments to all measurements whose marginals are the context distributions. Thm 8.1 proves this holds iff there is a factorizable hidden-variable model, and Prop 3.1 that a global section is a deterministic hidden-variable model. Contextuality comes in three nested strengths — probabilistic, possibilistic, strong — witnessed by Bell, Hardy and GHZ (Props 4.2–4.4, 6.1), and strong contextuality is a non-contextual fraction of zero (Prop 6.3).

Over the reals the answer is always yes: noncontextual and no-signalling models span the same subspace (Thm 5.4), so every no-signalling model, the PR box included, has a signed global section (Thm 5.9). Negative probabilities therefore cannot single out quantum theory; what contextuality marks is that no *nonnegative* section exists.

## What this does not say

- Anything about data whose marginals depend on context (signalling, or imperfectly compatible measurements); no-signalling is assumed. Contextuality-by-Default handles that case (see the behavioural claim in this group).
- Anything about generalized (Spekkens) contextuality; how the two notions relate is a separate claim that extends this one.
- Anything infinite; the scenarios are finite.
- That contextuality can always be certified cohomologically. Abramsky,
  Mansfield & Barbosa's Čech obstruction ([LIT-277](../literature.d/LIT-277.md), [NOTE-250](../notes.d/NOTE-250.md))
  is a sufficient witness only. It vanishes on every section of the Hardy
  model, and on 9 of 15 sections of a strongly contextual Kochen–Specker
  cover (§8), because it tests extension to a compatible family of
  ℤ-combinations, not to a global section of the support. The criterion
  here is the exact one; the cohomology is a computable relaxation of it.
- The strictness of the hierarchy at the possibilistic step, which leans on a cited result, or GHZ for n other than 4k ([NOTE-016](../notes.d/NOTE-016.md)). This claim covers the equivalence and Thm 5.9, not those details.
