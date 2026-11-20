---
status: Open
title: 'Count, from the record''s git history, how often each claim takes a substantive revision before and after its first inbound rests_on or grounds edge, to see whether entries settle as relations accrue'
version: 1
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
- CLAIM-tmpvm90n
- CLAIM-tmp4qvx2
summary: >-
  The owner, 2026-11-20: "i think that edit rate count idea is worth
  filing too, doesn't need to be one or the other". The count of
  substantive revisions per claim against its inbound references, from git
  history. It tests the settling [CLAIM-tmpvm90n](../claims.d/CLAIM-tmpvm90n.md) predicts; by
  [CLAIM-tmp4qvx2](../claims.d/CLAIM-tmp4qvx2.md) it cannot by itself say whether constraint or contraction
  did the settling, which is what [LEAD-tmp84yvk](LEAD-tmp84yvk.md) adds.
---
<!-- inactive-ok-file: CLAIM-tmpvm90n CLAIM-tmp4qvx2 — Proposed or Open; filed in this contribution of 2026-11-20 -->
<!-- inactive-ok-file: ARG-028 — Proposed; its inbound-reference measure is the one reused here -->

# LEAD-tmp6do6f: Count, from the record's git history, how often each claim takes a substantive revision before and after its first inbound rests_on or grounds edge, to see whether entries settle as relations accrue

## Design

**Population.** Every file in `record/claims.d/`, followed through its
temporary-code rename with `git log --follow`. The clone a session gets is
shallow; the count needs the full history (`git fetch --unshallow`).

**Revisions.** A commit touching the file counts as *substantive* if it
changes the `title`, `role`, `warrant`, `defeated_if` or the body outside
dated-note sections. It is excluded if it only appends a history entry or a
dated note, only adds or removes relation fields, or comes from the CI
repair bot (link targets and converse relations). Status changes are counted
separately: [CLAIM-tmpvm90n](../claims.d/CLAIM-tmpvm90n.md) predicts the text narrows while status stays open.

**Exposure.** For each claim, the date of its first inbound `rests_on` or
`grounds` edge, from the first commit at which some other file names its code
in either field, and the count of inbound edges over time. The inbound count
is [ARG-028](../arguments.d/ARG-028.md)'s measure, reused.

**Comparison.** Substantive revisions per month of exposure, before and after
the first inbound edge, and as a function of inbound count. Control for age:
young entries are revised more whatever their edges, so compare entries of
matched age with and without inbound edges.

**What would count against [CLAIM-tmpvm90n](../claims.d/CLAIM-tmpvm90n.md).** No fall in the substantive
rate after inbound edges arrive, at matched age (its `defeated_if` (a)).

**What the count cannot show.** Why entries settled. A fall is also what
contraction toward the record's conventions predicts ([CLAIM-tmp4qvx2](../claims.d/CLAIM-tmp4qvx2.md)), so a
positive result goes with [LEAD-tmp84yvk](LEAD-tmp84yvk.md) before it is read as support.

## Cost

A script over `git log`, an afternoon, once the history is unshallowed. The
classification of a commit as substantive is the part to check by hand on a
sample.
