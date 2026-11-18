---
number: 280
status: Proposed
formerly:
- CASE-tmpyeqlj
title: 'Two organizations with the same rules, appeal rights, decision rate and initial corrective capacity, one whose decisions leave that capacity intact and one whose decisions each use some of it up: with the rule revised after T days, the first can still correct its accumulated errors until T = 100, the second only until T = 20'
version: 3
history:
- version: 2
  date: '2026-11-16'
  note: >-
    Clarified at the second review of 2026-11-16 (ChatGPT's, forwarded by
    the owner): B's capacity is floored at zero, K_B(T) = max(0, 100 − 4T),
    exhausted at day 25; the capacity is a reserve dedicated to correction,
    not needed for routine execution; and A and B are indistinguishable in
    their stipulated observable outputs, not in their reserves. The result is
    unchanged.
- version: 3
  date: '2026-11-18'
  note: >-
    Reconciled with the continuation's filing of the same exchange (PR 512):
    its CASE-285 (a proposed study varying the acting institution's
    speed) was compared with this construction and judged distinct; a
    sentence on the difference added. No change of status or title.
standing: stipulated
kind: construction
tags:
- society-and-governance
- complex-systems
date: '2026-11-16'
line:
- distributed-agency
illustrates:
- CLAIM-464
- CLAIM-462
bears_on:
- QUESTION-278
- QUESTION-279
summary: >-
  A separating construction requested at the review of 2026-11-16
  (ChatGPT's, forwarded by the owner), to show which organizational
  difference makes a governing arrangement lose effective control, rather
  than connecting the record's timescale and correction claims in prose.
  The design is the review's; the model and numbers are the filer's. Two
  organizations decide at the same rate with the same error share, rules,
  appeal rights and initial corrective capacity, and perform identically
  until correction is attempted. Errors can be corrected only once the
  governing rule is revised, after T days. In A execution leaves corrective
  capacity intact; in B each decision uses some of it up. A can still
  correct all accumulated errors for T up to 100 days, B only up to 20. It
  separates three mechanisms: throughput (accumulated corrections exceed
  capacity), specification lag (T) and endogenous foreclosure (the
  decisions themselves reducing capacity). The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-285 — filed from the continuation of the same exchange on 2026-11-17, Proposed or Open -->
<!-- inactive-ok-file: CLAIM-705 CLAIM-701 — filed from the exchange "Assess Depp Heard Abuse", Proposed -->
<!-- inactive-ok-file: CLAIM-478 CLAIM-327 CLAIM-423 — Proposed; the timescale claims, cited with their standing -->

# CASE-280: Two organizations with the same rules, appeal rights, decision rate and initial corrective capacity, one whose decisions leave that capacity intact and one whose decisions each use some of it up: with the rule revised after T days, the first can still correct its accumulated errors until T = 100, the second only until T = 20

## The construction

Two organizations, A and B, alike in everything stated:

- the same governing rule and the same formal right of appeal;
- the same decision rate, r = 10 decisions a day, and the same error
  share, e = 0.1, so one erroneous decision a day;
- the same corrective capacity at the start, K₀ = 100 units, and the same
  cost of correcting one error, c = 1 unit;
- the same lag in revising the rule: errors become correctable only once
  the governing rule is revised, T days after decisions begin (until then
  no one has formulated the objection that would justify correcting them).

They differ in one respect. In A, executing a decision leaves the
corrective capacity as it was. In B, each decision uses up δ = 0.4 units of
it: the staff, records, relationships or access through which a later
correction would be carried out. The capacity is a reserve dedicated to
correction, not a resource routine execution needs, so B goes on deciding
after the reserve is spent. At day T, A has K_A = 100 units and B has
K_B(T) = max(0, K₀ − δrT) = max(0, 100 − 4T), which reaches zero at day 25.

When the rule is revised at T, correcting all accumulated errors needs
c·e·r·T = T units.

- **A** can correct them if T ≤ K₀ / (c e r) = **100 days**.
- **B** can correct them if T ≤ K₀ / (r(δ + c e)) = **20 days**.

| T (days) | needed | A has | A correctable | B has | B correctable |
|---|---|---|---|---|---|
| 10 | 10 | 100 | yes | 60 | yes |
| 20 | 20 | 100 | yes | 20 | yes |
| 21 | 21 | 100 | yes | 16 | no |
| 50 | 50 | 100 | yes | 0 | no |
| 100 | 100 | 100 | yes | 0 | no |
| 101 | 101 | 100 | no | 0 | no |

Checked with `python3 -I` (scratchpad, 2026-11-16).

## What it separates

Three mechanisms the exchange connected in prose:

- **Throughput overload**: the corrections needed exceed the corrector's
  capacity. Both fail past T = 100; that limit is the same for both
  ([CLAIM-705](../claims.d/CLAIM-705.md) for a stream of challenges).
- **Specification lag**: the governing institution has not yet formulated
  the objection. It is T, the variable on the horizontal axis, and is the
  same for both (A35 §5; [CLAIM-475](../claims.d/CLAIM-475.md)).
- **Endogenous foreclosure**: the actions themselves diminish the capacity
  to carry out the correction once it is identified. Only B has it, and it
  alone accounts for the window 20 < T ≤ 100 in which A can still correct
  and B cannot.

Up to the moment correction is attempted, A and B are indistinguishable in
their stipulated observable outputs: same decisions, same errors, same
formal rights. Their corrective reserves differ and could in principle be
inspected beforehand; what the case shows is that the outputs do not reveal
them. That is [CLAIM-462](../claims.d/CLAIM-462.md)'s point,
that capacity for effective action is no evidence of capacity to be
corrected, in a case where the difference is a single parameter. B's
foreclosure is [CLAIM-464](../claims.d/CLAIM-464.md)'s effect produced by the ordinary run of
decisions rather than by one intervention. The novel variable is not
execution speed alone but the relation between how fast decisions are
executed, how fast the rule can be revised, and how fast execution erodes
the capacity for correction: raising r shortens both thresholds, and
shortening the lag T is what B needs and A does not.

## What it does not show

- **That real organizations have a single capacity stock or a fixed δ.**
  It is a construction: it shows the mechanisms can come apart, not how
  often or how much.
- **That foreclosure is wrongful or intended.** B's erosion of its own
  corrective capacity may be an unchosen side effect; whether anyone
  answers for it is [CLAIM-701](../claims.d/CLAIM-701.md)'s question, and that claim needs the act
  to be wrongful.
- **Anything about the timescale claims' general form.** [CLAIM-331](../claims.d/CLAIM-331.md),
  [CLAIM-478](../claims.d/CLAIM-478.md), [CLAIM-327](../claims.d/CLAIM-327.md) and [CLAIM-423](../claims.d/CLAIM-423.md) say why governing variables are slow;
  this construction takes the slowness (T) as given.

The continuation of the same exchange filed A33 §10 C as a proposed study,
[CASE-285](CASE-285.md): the same overseer's authority, two speeds of the acting
institution, and precommitted limits, automatic suspension and pauses
added in turn. It is distinct from this construction, which holds speed
fixed and varies whether execution erodes corrective capacity; run, it
would test the throughput and timing mechanisms that this case holds
equal.
