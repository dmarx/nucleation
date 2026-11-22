---
number: 43
status: Open
formerly:
- LEAD-tmp5pwlw
title: 'Run the forgetting study in small transformers: whether apparent forgetting is loss, readdressing, interference or suppression'
version: 1
stage: specified
priority: medium
method:
- empirical
tags:
- learning-theory
- representation-learning
- information-theory
date: '2026-11-19'
line:
- learned-structure
advances:
- QUESTION-274
- QUESTION-275
- QUESTION-010
- CLAIM-697
operationalized_in:
- CASE-274
summary: >-
  Named in [CASE-274](../cases.d/CASE-274.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CASE-274 CLAIM-697 — Proposed; cited in the backlog audit of 2026-11-19 -->

# LEAD-043: Run the forgetting study in small transformers: whether apparent forgetting is loss, readdressing, interference or suppression

## What it would do

Run [CASE-274](../cases.d/CASE-274.md): train, fine-tune away a capability, and test with probes,
relearning speed and targeted interventions which of loss, readdressing,
interference or suppression the forgetting was.

Where the record names it:

- [CASE-274](../cases.d/CASE-274.md): "It joins the owner's questions on concept erasure, sleeper
  agents, the hologram, test-time compute and RL into one experiment."

## What would count

Fast relearning and recoverable probes favour readdressing or suppression
over loss, bearing on [CLAIM-697](../claims.d/CLAIM-697.md); true loss supports the reading that
capability is overwritten.

## Note of 2026-11-22: a toy-scale run, done
<!-- inactive-ok-file: CASE-tmprir2y CLAIM-tmp2eemo CLAIM-tmpqvkag CLAIM-698 — new or Proposed; the run of this lead, the claims filed from it, and the claim the design's untested prediction is for -->

A delegated worker ran a toy-scale stand-in for CASE-274 on CPU (numpy; torch is not installed), filed as CASE-tmprir2y, with the findings as CLAIM-tmp2eemo (what the forgetting was) and CLAIM-tmpqvkag (why the matched world is needed). Scripts, tests, per-item results and the analysis are under scratch/studies/lead-043/.

Done:
- A two-layer transformer memorized 256 random facts under two query templates; 32 were fine-tuned away in nine arms (unlearning to uniform, gradient ascent and overwriting, each at one cue and at two; ascent also stopped at its criterion; an unrelated new task without rehearsal), 4 seeds (2 for early ascent), each with a twin trained on a world that differs only in the target values.
- Readers: another cue, the runner-up answer, logit lens and linear and MLP probes at each layer, reverting each block's update, sampling coverage, and relearning half the targets with the other half watched.

Result: except under gradient ascent, the forgotten facts stay recoverable well above the twin's rate, mostly by another cue and by reverting a first-layer block, so the forgetting was mostly readdressing and interference, with the update in the routing, not the read-out. Ascent collapses the whole model. The union of readers also recovers 28 to 46 percent of values the twin never held.

What remains of the lead:
- the study at language-model scale, on facts that can be inferred from correlates, where the matched world does real work;
- query variants that generalize (this toy's unseen template did not);
- closed-form linear erasure, task-vector merges, RL and the budget axis with a selector;
- CASE-274's response-geometry prediction (CLAIM-698), made before the recovery tests.

The lead also names QUESTION-274 (whether a feature circuit depends on the dictionary). Neither CASE-274's design nor this run uses learned dictionaries, so the run does not bear on it; whether QUESTION-274 belongs in the lead's `advances` is the owner's call. The stage and status are the owner's.
