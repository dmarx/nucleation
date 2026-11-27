---
number: 199
status: Open
formerly:
- LEAD-tmp6do6f
title: 'Count, from the record''s git history, how often each claim takes a substantive revision before and after its first inbound rests_on or grounds edge, to see whether entries settle as relations accrue'
version: 2
history:
- version: 2
  date: '2026-11-26'
  note: >-
    A dated note: the owner's U18 and A34's first pilot in the
    exchange 'Alignment consequences brainstorm' (ChatGPT, 2026-11-26)
    build on this lead's scripts (see the note). No other change.
stage: specified
priority: medium
method:
- empirical
tags:
- design-rationale
- epistemology
date: '2026-11-20'
line:
- nucleating-argument
- record-as-apparatus
advances:
- CLAIM-778
- CLAIM-768
summary: >-
  The owner, 2026-11-20: "i think that edit rate count idea is worth
  filing too, doesn't need to be one or the other". The count of
  substantive revisions per claim against its inbound references, from git
  history. It tests the settling [CLAIM-778](../claims.d/CLAIM-778.md) predicts; by
  [CLAIM-768](../claims.d/CLAIM-768.md) it cannot by itself say whether exact copying or contraction
  did the settling, which is what [LEAD-201](LEAD-201.md) adds.
---
<!-- inactive-ok-file: CASE-307 CLAIM-864 CLAIM-863 — Proposed; LEAD-199's study of 2026-11-22 and its two readings -->
<!-- inactive-ok-file: CLAIM-778 CLAIM-768 — Proposed or Open; filed in this contribution of 2026-11-20 -->
<!-- inactive-ok-file: ARG-028 — Proposed; its inbound-reference measure is the one reused here -->

# LEAD-199: Count, from the record's git history, how often each claim takes a substantive revision before and after its first inbound rests_on or grounds edge, to see whether entries settle as relations accrue

## Design

**Population.** Every file in `record/claims.d/`, followed through its
temporary-code rename with `git log --follow`. The clone a session gets is
shallow; the count needs the full history (`git fetch --unshallow`).

**Revisions.** A commit touching the file counts as *substantive* if it
changes the `title`, `role`, `warrant`, `defeated_if` or the body outside
dated-note sections. It is excluded if it only appends a history entry or a
dated note, only adds or removes relation fields, or comes from the CI
repair bot (link targets and converse relations). Status changes are counted
separately: [CLAIM-778](../claims.d/CLAIM-778.md) predicts the text narrows while status stays open.

**Exposure.** For each claim, the date of its first inbound `rests_on` or
`grounds` edge, from the first commit at which some other file names its code
in either field, and the count of inbound edges over time. The inbound count
is [ARG-028](../arguments.d/ARG-028.md)'s measure, reused.

**Comparison.** Substantive revisions per month of exposure, before and after
the first inbound edge, and as a function of inbound count. Control for age:
young entries are revised more whatever their edges, so compare entries of
matched age with and without inbound edges.

**What would count against [CLAIM-778](../claims.d/CLAIM-778.md).** No fall in the substantive
rate after inbound edges arrive, at matched age (its `defeated_if` (a)).

**What the count cannot show.** Why entries settled. A fall is also what
contraction toward the record's conventions predicts ([CLAIM-768](../claims.d/CLAIM-768.md)), so a
positive result goes with [LEAD-201](LEAD-201.md) before it is read as support.

## Cost

A script over `git log`, an afternoon, once the history is unshallowed. The
classification of a commit as substantive is the part to check by hand on a
sample.

## Note of 2026-11-22: run

Run as specified ([CASE-307](../cases.d/CASE-307.md); scripts, data and hand-checks under scratch/studies/lead-199/). At matched age, cited claims are revised more often than uncited ones, which meets [CLAIM-778](../claims.d/CLAIM-778.md)'s defeater (a); readings filed as [CLAIM-864](../claims.d/CLAIM-864.md) and [CLAIM-863](../claims.d/CLAIM-863.md). The lead stays Open for the owner to mark Done; what remains, by [CLAIM-768](../claims.d/CLAIM-768.md), is [LEAD-201](LEAD-201.md)'s retention measure, and for [CLAIM-863](../claims.d/CLAIM-863.md) a count of audits.

## Note of 2026-11-26: the base of the temporal dependency graph

The owner's U18 in the exchange "Alignment consequences brainstorm" (ChatGPT,
2026-11-26), "maybe we can use git to derive edit histories for each file and
then from that we could model things like interaction intensity, prose
stability, neighborhood influence", became A34's first pilot, filed as
[LEAD-305](LEAD-305.md). This lead's scripts (scratch/studies/lead-199/) are its base:
`extract.py` already follows claims through their temporary codes and
`formerly:` and replays inbound `rests_on` and `grounds` edges, setting aside
CI repair, promotion and concretization commits, and `classify.py` already
separates substantive revisions from dated notes and normalised markup. [LEAD-305](LEAD-305.md) widens the extraction to every relation field,
status and the other schemes, and its first check is to reproduce [CASE-307](../cases.d/CASE-307.md) on
this lead's window. A33's suggested extraction, `git log main --first-parent`,
would see only the nightly promotions, so the new lead keeps this lead's walk
over staging's commits. This lead's status is unchanged.
