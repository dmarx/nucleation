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
- Code: phases.py, test_lead052.py (11 tests pass), run_all.py.
- Run started 2026-11-22 (PID in the session scratchpad, lead-052/run.pid),
  writing results/runs.jsonl one line per item; rerun resumes.

- Run finished: 2699 items in 419 s; compacted (compact.py) to 1.0 MB;
  summaries at five (delta, tol) settings.
- README.md with design, derivation (commutation by tree symmetry; kernel
  T_l exact; deep linear order by c_l g_l) and results.

- Filed: CASE-tmp7n58t (executed-study), CLAIM-tmpzujm1 (demonstrated),
  CLAIM-tmp0h57p (empirical); dated notes on QUESTION-217, QUESTION-039,
  LEAD-052 (plus operationalized_in); changelog fragment lead-052.md.
  Frontmatter, titles and H1s checked with python3.

## Next

- Report to the lead. No pull request (the lead opens it).

## Choice: two claims

The derivation (exact, for two learner classes) and the trained ReLU
network (empirical) have different warrants, so they are filed as two
claims rather than one.

## Choices

- Tree: binary, depth 3, 8 items. Levels are the Haar levels (1, 1, 2, 4
  vectors). Inputs and targets are written in the Haar basis, each with
  its own per-level strength (c for inputs, g for targets), then rotated
  at random. So Sigma_x has eigenvalue c_l^2 and Sigma_yx singular value
  c_l g_l on level l: strength is set per level, independently of the tree.
- Acquisition: T_l(delta), the first time level l's relative risk of the
  network's own output falls to delta (main delta = 0.1). The decoder is
  the network's output, not a probe on hidden units.
- Order classes: two levels tie when the later time is within 1.25 times
  the earlier; coarse-first, fine-first, simultaneous or mixed by the
  pairwise relations. Robustness at delta 0.5 and 0.02.
- Learners: deep linear (2 and 3 weight layers, small init); two-layer
  ReLU in standard parametrization at small (0.01) and order-one scale;
  NTK-parametrized ReLU at width 64 and 2048; exact infinite-width ReLU NTK
  and the linear kernel (shallow linear net) by closed form.
- LEAD-045's network.py was not reused beyond its antisymmetric
  initialization (its task is scalar-output skills, not a tree).
