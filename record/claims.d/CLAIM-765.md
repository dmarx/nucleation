---
number: 765
status: Proposed
formerly:
- CLAIM-tmpvnjh2
title: 'Identifiability and localization come apart'
statement: >-
  Two properties of what a learner retains come apart in all four
  combinations: identifiability, whether a retained change and its
  contribution can be established from observation and intervention, and
  localization, whether it sits in a place one can point to
version: 1
role: thesis
warrant: empirical
defeated_if: >-
  A showing that one property entails the other for retained learning in a
  declared class of systems: that every identifiable retained change is
  localized under some admissible interface, or that every localized
  change is identifiable up to stated ambiguities; or that one of the four
  combinations cited here is misdescribed by the readings that ground it.
tags:
- learning-theory
- representation-learning
- individuation
date: '2026-11-19'
line:
- learned-structure
rests_on:
- CLAIM-519
- CLAIM-135
grounds:
- THEORY-966
- THEORY-2059
- THEORY-2058
- THEORY-2060
- THEORY-2062
uses:
- TERM-131
bears_on:
- QUESTION-497
- QUESTION-035
summary: >-
  The owner's (2026-11-19): learning merely persisted in a stable
  representation differs from learning that is concretely indexable,
  sharpened at the owner's suggestion to identifiability against
  localization. The four combinations are shown by entries the record
  already holds. The case for each is the filer's assembly; adopting the
  claim is the owner's call.
---
<!-- inactive-ok-file: CLAIM-519 THEORY-2058 THEORY-2059 THEORY-2060 THEORY-2062 TERM-131 — Proposed or newly filed; cited in this filing of 2026-11-19 -->

# CLAIM-765: Identifiability and localization come apart

## The claim

Identifiability: one can establish, from observation and intervention,
that a particular retained change exists and what it contributes, up to
stated ambiguities, the second of [CLAIM-135](CLAIM-135.md)'s three achievements.
Localization: the change sits in a specific place, such as a component, an
address or a token position. The two are independent.

## The four combinations

- **Identifiable and localized.** In-context learning: the demonstrations
  occupy positions in the context, and deleting one is the intervention
  that identifies its effect on later outputs ([THEORY-2062](../theory.d/THEORY-2062.md); [TERM-131](../terms.d/TERM-131.md)
  version 2).
- **Identifiable, not localized.** Learning in the weights, measured by
  its effect: what pretraining is worth is identified as effective data
  transferred against same-size models trained from scratch, without
  locating any of it ([THEORY-2059](../theory.d/THEORY-2059.md)); per-example contributions are
  estimated by attribution because no example's effect has an address
  ([THEORY-2058](../theory.d/THEORY-2058.md), [THEORY-2060](../theory.d/THEORY-2060.md)).
- **Localized, not identifiable.** A located circuit that is one of
  several sufficient ones: greedy pruning keeps one input of a redundant
  set ([THEORY-966](../theory.d/THEORY-966.md)), so the place is real and its role is not uniquely
  fixed.
- **Neither.** Competent behaviour over a fixed interface and finite
  horizon that does not establish any internal model ([CLAIM-519](CLAIM-519.md)).

## Admission

A separating case for each direction of the independence, from held
entries; no derivation is offered. The warrant is empirical because the
combinations rest on readings. Whether an interface exists under which
weight learning becomes localized is left open: located subnetworks and
lesions show some can be, which would make localization relative to a
declared interface rather than absolute, and that is consistent with the
claim.

## Bearing

On [TERM-131](../terms.d/TERM-131.md): a claim about learning can say which kind of retention it
means. On individuation ([QUESTION-497](../questions.d/QUESTION-497.md), refining [QUESTION-035](../questions.d/QUESTION-035.md)):
localization gives separability, identifiability gives attribution, and
they diverge. [THEORY-1024](../theory.d/THEORY-1024.md) suggests a third property, editability, that
comes apart from localization; it is not part of this claim.
