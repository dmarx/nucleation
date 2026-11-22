---
number: 122
status: Open
formerly:
- LEAD-tmpkwy7i
title: 'Count, in the workbench reconstructions, the share of moves of comparable content filed by contributor and by kind of move'
version: 1
stage: idea
priority: medium
method:
- empirical
tags:
- epistemology
- design-rationale
date: '2026-11-19'
line:
- record-as-apparatus
advances:
- QUESTION-072
summary: >-
  Named in [QUESTION-072](../questions.d/QUESTION-072.md). Filed by the backlog audit of 2026-11-19.
---

# LEAD-122: Count, in the workbench reconstructions, the share of moves of comparable content filed by contributor and by kind of move

## What it would do

Script the count over the workbench entries.

Where the record names it:

- [QUESTION-072](../questions.d/QUESTION-072.md): "A count: in this record's workbench reconstructions, for
  moves of comparable content, the share filed by contributor and by kind of
  move."

## What would count

The count is the answer the question asks for.

## Note of 2026-11-22: carried out, as a census over the labelled entries

Carried out on this branch and filed as [CASE-372](../cases.d/CASE-372.md) (executed-study, documented), bearing on [QUESTION-072](../questions.d/QUESTION-072.md). The script, test, result and README are at `scratch/studies/lead-122/`. Operationalization: a move is one bold-label disposition span (Filed / Missed / Not filed / Struck / Held, not filed), contributor read from owner (`U\d`) and assistant (`A\d`) turn tokens, kind from the scheme named. Result: 47 of 135 entries label their moves; over 454 filed-or-not-filed spans, share filed is owner 0.70, assistant 0.57, both 0.41 (block context), and by kind note 0.79 down to work 0.26 and theory 0.00.

What remains: the count does not answer [QUESTION-072](../questions.d/QUESTION-072.md) part 1's counterfactual (comparable content held fixed), because the prose carries no content-matched contributor pairs and kind confounds contributor, and it covers only the 47-of-135 entries that use disposition labels — a matched-pair design over single-contributor moves is the follow-up the finding points to. Status and stage unchanged; adoption is the owner's.
