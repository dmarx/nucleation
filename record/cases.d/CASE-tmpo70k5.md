---
status: Proposed
title: 'Four organizations alike in their members'' flexibility, one member trained in each, crossing that member''s leverage over the consequences colleagues meet with a culture that rewards or penalizes flexible action: only high leverage in a rewarding culture spreads it, low leverage there keeps it in the trained member alone, and a penalizing culture extinguishes it, so organizational flexibility is not the mean of members'' flexibility'
version: 1
standing: fictional
kind: construction
tags:
- behavioral-integration
- self-governance
- psychopathology-and-treatment
date: '2026-11-04'
line:
- will-organization
summary: >-
  A construction for the second reading of the slash in the owner's U19 of
  the exchange "Organizational Nucleation and SLT" (2026-11-04),
  "psychological flexibility / organizational effectiveness": one property
  named at two scales, joined by propagation and not by aggregation. It
  makes Guida, Minutola and Presti's P4 ([LIT-1218](../literature.d/LIT-1218.md), [NOTE-1353](../notes.d/NOTE-1353.md)) a weighted
  influence network, the reduction their reading said would be the
  record's contribution, with leverage as conferral ([TERM-tmplu4ih](../terms.d/TERM-tmplu4ih.md)). Made
  at the owner's review, which invited a case for an alternative reading.
  The construction is the filer's; the script is
  scratch/formal/r3_flexibility_propagation.py.
---

# CASE-tmpo70k5: Four organizations alike in their members' flexibility, one member trained in each, crossing that member's leverage over the consequences colleagues meet with a culture that rewards or penalizes flexible action: only high leverage in a rewarding culture spreads it, low leverage there keeps it in the trained member alone, and a penalizing culture extinguishes it, so organizational flexibility is not the mean of members' flexibility

## The case

Eight members each have a flexibility f ∈ [0, 1], at 0.3 except one
trained member at 1.0, so every organization starts with mean 0.387. A
matrix L gives what each member confers on the consequences each other
member meets ([TERM-tmplu4ih](../terms.d/TERM-tmplu4ih.md)): 0.02 everywhere, and 0.4 from the trained
member to each colleague in the high-leverage arms. Each step:

- colleagues take up flexible action in proportion to what flexible
  members confer on them, f_j += η Σᵢ L_ij (fᵢ − 0.3)(1 − f_j), with
  η = 0.15, but only where the culture rewards it;
- flexible action decays toward 0.3 at rate 0.01 in a rewarding culture
  and 0.15 in a penalizing one.

After 60 steps:

| leverage | culture | mean at start | trained member | untrained mean |
|---|---|---|---|---|
| high | rewarding | 0.387 | 0.754 | 0.831 |
| high | penalizing | 0.387 | 0.300 | 0.300 |
| low | rewarding | 0.387 | 0.692 | 0.368 |
| low | penalizing | 0.387 | 0.300 | 0.300 |

This is the shape of P4 in [NOTE-1353](../notes.d/NOTE-1353.md): retention and spread "depend
jointly on leverage and culture", and its falsifier, low-leverage members
in a penalizing culture whose action is retained and taken up, does not
occur.

## What it can show

- **Two scales, one property, no aggregation.** The four organizations
  have the same members' mean flexibility at the start and end with
  different organizational flexibility. Read this way, U19's slash names
  ACT's psychological flexibility at the member's scale and the same
  property at the organization's, which is how Guida, Minutola and Presti
  take Bond's organizational flexibility: "coordinated, values-consistent
  action that is retained and spread", "not as the mean of members'
  flexibility" ([NOTE-1353](../notes.d/NOTE-1353.md)).
- **Where the two readings of the slash part.** A19 set "Regulatory
  flexibility" apart from "Practical effectiveness", since "A system can
  be flexible among inappropriate goals". That holds for flexibility as
  success across contexts. ACT's flexibility is already relative to the
  system's own valued ends, "to change or persist in behavior when doing
  so serves valued ends" ([LIT-555](../literature.d/LIT-555.md)), so an organization flexible among
  goals its own values reject is not flexible in that sense. The two
  readings then differ in one place: whether effectiveness is judged by
  the organization's own values, the second reading, or by a standard
  specified independently of them, A19's.
- **Leverage is conferral.** What carries flexibility from one member to
  others is the effect of the one on the consequences the others meet,
  so P4's leverage index is a conferral matrix, and the circularity guard
  P4 asks for, leverage measured before spread, is the one [QUESTION-117](../questions.d/QUESTION-117.md)
  needs.

## What it cannot show

- That flexibility propagates this way in any organization. The update
  rule is chosen to have P4's shape; P4 is a hypothesis with no data.
- That leverage is fixed. Here L does not change; in the record's
  organizations conferral is itself allocated.
- Which reading of the slash the owner meant, which the owner has said
  does not matter: both readings are now on the record.
