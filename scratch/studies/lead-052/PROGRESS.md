# LEAD-052: progress

- Lead: LEAD-052 (advances QUESTION-217, QUESTION-039)
- Branch: claude/lead-052-acquisition-phases (cut from origin/staging)
- Task: on synthetic data with a known tree, set the spectral strength of
  each level independently of the tree; train deep linear, kernel-regime
  and small nonlinear networks; map when acquisition is coarse-first,
  fine-first, simultaneous or mixed; state sufficient conditions as a
  theorem where possible. File a CASE (executed-study), a CLAIM where the
  results warrant one, and dated notes on QUESTION-217, QUESTION-039 and
  LEAD-052. numpy, pytest, CPU, BLAS threads 1, about an hour.

## Step 1: is the target already held?

Checked 2026-11-22: no case, claim or workbench entry after the lead runs
this study. LEAD-052 is cited only by itself and the curation entry of
2026-11-19. QUESTION-217's notes record no run. Not held.

## Done

- Step 1 (not held).

## Next

- Design and code (data, learners, acquisition measure, classifier), tests.
- Runs, writing one JSON line per item.
- CASE, CLAIM, notes, changelog fragment.

## Choices
