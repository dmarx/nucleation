---
number: 175
status: Open
formerly:
- LEAD-tmpvdouu
title: 'Re-run the toy-model-of-superposition check: SGD at n = 1,000 and on both sides of n = 600, and posterior sampling across n for the chain''s critical sample sizes'
version: 1
stage: idea
priority: medium
method:
- empirical
tags:
- learning-theory
- loss-landscapes
date: '2026-11-19'
line:
- learned-structure
advances:
- QUESTION-363
summary: >-
  Named in [QUESTION-363](../questions.d/QUESTION-363.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CASE-tmpgqbyq CLAIM-tmpg8m7a CLAIM-tmp9zqvq CLAIM-tmpraadt — new, filed 2026-11-22 by LEAD-175's study -->

# LEAD-175: Re-run the toy-model-of-superposition check: SGD at n = 1,000 and on both sides of n = 600, and posterior sampling across n for the chain's critical sample sizes

## What it would do

Run the existing script across learning rates, batch sizes and
initializations, and sample the posterior across n.

Where the record names it:

- [QUESTION-363](../questions.d/QUESTION-363.md): "and SGD at n = 1,000 and on both sides of n"

## What would count

Whether the 6-gon is reached decides "inaccessible" against "not reached"
for [QUESTION-363](../questions.d/QUESTION-363.md).

## Note of 2026-11-22: carried out

Done by a delegated worker on branch claude/lead-175-superposition-sweep
(scratch/studies/lead-175/). The SGD sweep and posterior sampling across
n are filed as [CASE-tmpgqbyq](../cases.d/CASE-tmpgqbyq.md). The claims filed from it:

- [CLAIM-tmpg8m7a](../claims.d/CLAIM-tmpg8m7a.md): the 5-gon's dropped feature gets no gradient under
  SGD;
- [CLAIM-tmp9zqvq](../claims.d/CLAIM-tmp9zqvq.md): the 6-gon is not reached at any setting tried;
  "inaccessible", for this model;
- [CLAIM-tmpraadt](../claims.d/CLAIM-tmpraadt.md): the posterior's critical sizes differ from the
  formula's, and there is a factor-½ difference of scale in Chen et al.

**What remains:**

- the finite-dataset posterior (NUTS-like, per n, as Fig. 2);
- other trainers: weight decay, Langevin noise, Adam;
- whether the live 5⁺ route opens at some setting not tried.

The lead's stage and status are the owner's.

## Note of 2026-11-23: resumption in the study scripts, reviewed and fixed

A code review the owner forwarded on 2026-11-23 found two defects in this
lead's scripts (`scratch/studies/lead-175`).

- **Posterior sampler (P2).** `posterior.py` appended a block to the output
  and then saved the sampler state separately. An interruption between the
  two left the output a block ahead of the state, and a missing state file
  restarted fresh chains while keeping the block count, which skipped
  burn-in. A resume also reseeded the generator from the block count, so it
  never matched an uninterrupted run.
- **SGD sweep (P2).** `sgd_sweep.py` marked a whole (n, batch, epochs) job
  done once one of its result lines was written. A job interrupted midway
  would have been skipped on restart, short of its runs.

**Fixed.**
- The sampler now keeps one atomic checkpoint: block count, configuration,
  chains, step sizes and generator state. It reconciles it with the output
  on restart, dropping a block written but not checkpointed and rerunning
  it, and stops when the two cannot be reconciled.
- The sweep counts completion per run and completes a partly written job.
- Both drop a torn final line. `test_resume.py` simulates each
  interruption. A fresh run seeds as before, so the README's commands still
  reproduce the committed results.

**Whether the reported results were affected.**
- Every SGD job in `results/` has its full complement of runs (96 in the
  main grid, 24 or 36 in the extensions), with no duplicates. So the
  sweep's totals stand.
- Every posterior and restricted output has its blocks in unbroken
  sequence, with its burn-in blocks first. Neither file records an
  interruption, but a resume from a stale checkpoint would leave no mark in
  the output, and the checkpoints are not kept. That no posterior run was
  resumed is therefore likely, not shown.

