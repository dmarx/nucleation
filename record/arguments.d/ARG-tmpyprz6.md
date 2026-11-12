---
status: Rejected
title: 'EvoOntology''s gate ablation shows that governance raises the value of a modifiable schema'
version: 2
history:
- version: 1
  date: '2026-11-12'
  note: Filed Rejected with the readings of 2026-11-12.
- version: 2
  date: '2026-11-12'
  note: >-
    Aligned with the owner's review of #484 on 2026-11-12, which narrowed
    CLAIM-tmppk8g6 to the interaction and filed its routine-task
    prediction as CLAIM-tmpbszhs. The verdict is unchanged; the critical
    questions now name the missing misfit tasks rather than a missing
    split between misfit and routine tasks, and say that the paper does
    not bear on CLAIM-tmpbszhs either.
form: evidence
grounds:
- THEORY-tmp4d13i
concludes:
- CLAIM-tmppk8g6
tags:
- design-rationale
- databases
date: '2026-11-12'
line:
- record-as-apparatus
summary: >-
  The tempting reading of Chong, Zhang, Fan and Du's EvoOntology
  ([THEORY-tmp4d13i](../theory.d/THEORY-tmp4d13i.md), read on 2026-11-12): removing the acceptance gate costs
  11.2 points and schema-only evolution costs 8.7, so schema change does
  better with something around it, which is what [CLAIM-tmppk8g6](../claims.d/CLAIM-tmppk8g6.md) says of
  governance. Rejected: the gate is the performance-gated arm the claim's
  own defeat condition names as governance's rival, and the paper does not
  measure the outcome the claim is about. The reading is a comparator for
  the claim's study, not evidence for it. Filed so that the judgment is
  held once and can be overturned in one place.
---
<!-- inactive-ok-file: CLAIM-tmppk8g6 THEORY-tmp4d13i — Proposed, filed 2026-11-12; the claim and the reading this argument joins -->
<!-- inactive-ok-file: CASE-tmppm4do CLAIM-tmpbszhs — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# ARG-tmpyprz6: EvoOntology's gate ablation shows that governance raises the value of a modifiable schema

## The inference

1. [THEORY-tmp4d13i](../theory.d/THEORY-tmp4d13i.md), the reading of Chong, Zhang, Fan and Du in
   [NOTE-tmpu2q2p](../notes.d/NOTE-tmpu2q2p.md): an agent-facing ontology revised automatically, schema
   edits among its permitted changes, each patch accepted only if it
   improves a paired evaluation. Removing the gate "causes the largest
   drop (−11.2 Traj-Wise), because unfiltered candidates admit regressions
   that the next round cannot always undo"; "Content-only and Schema-only
   decrease performance by 3.6 and 8.7 points, respectively", while
   evolution at all three levels gains 7.7 over the initial ontology.
2. So schema change does better when something filters and accompanies
   it.
3. So, the argument runs, governance raises the value of a modifiable
   schema, as [CLAIM-tmppk8g6](../claims.d/CLAIM-tmppk8g6.md) says.

## Critical questions

- **Would the evidence be expected if the claim were false?** Yes. The
  claim's defeat condition names "a performance-gated arm, changes
  accepted on held-out tests alone" as the rival that, by matching the
  governed arm at no greater cost, would defeat it. EvoOntology's gate is
  that arm. A gate's value against its own validation metric is expected
  whether or not review, rationale and migration add anything beyond it.
- **Does it tell the claim apart from its rivals?** No. The claim is
  about an interaction: modifiability helps more with governance than
  without, on tasks whose inherited categories are inadequate, measured as
  justified correction without material regression. The paper has no
  governed arm (no review, no recorded decision, no migration of existing
  content: schema edits extend capacity "without changing its instantiated
  content"), no tasks set apart as ones whose categories are inadequate,
  and no held-out regression of what the old schema could express. Its
  rejected patches are logged with a stated expected effect, a thin form
  of rationale, but no arm varies it. Nor does it bear on CLAIM-tmpbszhs,
  the secondary prediction split from this claim, since it has no
  ungoverned arm on tasks that need no schema change.
- **Is the −8.7 for schema-only evolution the claim's premise?** Only in
  part. It shows that schema change unaccompanied can harm, which is
  compatible with the premise that modifiability needs something around
  it; but what accompanies it in the full system is co-evolution of the
  other two layers, not governance.

## Verdict

Rejected. EvoOntology neither corroborates nor counts against
[CLAIM-tmppk8g6](../claims.d/CLAIM-tmppk8g6.md); it supplies the performance-gated comparator the claim's
study needs ([CASE-tmppm4do](../cases.d/CASE-tmppm4do.md) draws on it) and a template for that arm, its
reciprocal two-fold protocol. The claim is unchanged.
