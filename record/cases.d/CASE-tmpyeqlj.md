---
status: Proposed
title: 'Two organizations with the same rules, appeal rights, decision rate and initial corrective capacity, one whose decisions leave that capacity intact and one whose decisions each use some of it up: with the rule revised after T days, the first can still correct its accumulated errors until T = 100, the second only until T = 20'
version: 1
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
<!-- inactive-ok-file: CLAIM-tmpfmmkt CLAIM-tmp5zzud — filed from the exchange "Assess Depp Heard Abuse", Proposed -->
<!-- inactive-ok-file: CLAIM-478 CLAIM-327 CLAIM-423 — Proposed; the timescale claims, cited with their standing -->

# CASE-tmpyeqlj: Two organizations with the same rules, appeal rights, decision rate and initial corrective capacity, one whose decisions leave that capacity intact and one whose decisions each use some of it up: with the rule revised after T days, the first can still correct its accumulated errors until T = 100, the second only until T = 20

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
correction would be carried out. So at day T, A has K₀ = 100 units and B
has K₀ − δrT.

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
  (CLAIM-tmpfmmkt for a stream of challenges).
- **Specification lag**: the governing institution has not yet formulated
  the objection. It is T, the variable on the horizontal axis, and is the
  same for both (A35 §5; CLAIM-475).
- **Endogenous foreclosure**: the actions themselves diminish the capacity
  to carry out the correction once it is identified. Only B has it, and it
  alone accounts for the window 20 < T ≤ 100 in which A can still correct
  and B cannot.

Up to the moment correction is attempted, A and B are indistinguishable:
same outputs, same errors, same formal rights. That is CLAIM-462's point,
that capacity for effective action is no evidence of capacity to be
corrected, in a case where the difference is a single parameter. B's
foreclosure is CLAIM-464's effect produced by the ordinary run of
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
  answers for it is CLAIM-tmp5zzud's question, and that claim needs the act
  to be wrongful.
- **Anything about the timescale claims' general form.** CLAIM-331,
  CLAIM-478, CLAIM-327 and CLAIM-423 say why governing variables are slow;
  this construction takes the slowness (T) as given.
