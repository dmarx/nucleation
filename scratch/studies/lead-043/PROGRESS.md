# LEAD-043 progress

- Lead: LEAD-043 (forgetting study in small transformers), design CASE-274.
- Branch: claude/lead-043-forgetting-toy, cut from origin/staging.
- Task: a toy-scale, CPU-only run of CASE-274: train a tiny transformer on
  synthetic subject-relation-object facts, fine-tune a subset away, then
  test with probes, alternative cues, relearning speed and targeted
  interventions whether the apparent forgetting is loss, readdressing,
  interference or suppression. File the run as an executed-study CASE,
  its findings as claims, dated notes on LEAD-043 and the questions it
  advances, and a changelog fragment.

## Done

- Step 1: target not already held (no executed study cites CASE-274;
  CASE-tmpb4hg0 is LEAD-172's modular-addition run, a different design).

- Step 2: numpy transformer, probes, study and analysis scripts; 9 tests
  pass. Smoke run (seed 0, two arms) worked; settings revised after it
  (fine-tune lr 1e-3 -> 3e-4, fine-tune past criterion, relearning checked
  every step).
- Step 3 (done, 28 items): seeds 0,1 -> results_a.jsonl; seeds 2,3 ->
  results_b.jsonl. Pretrained weights cached in the scratchpad only.

- Step 3b (done, 4 items): ascent with ~100 steps collapsed the whole model
  (retained accuracy ~0.09), so arms ascentA_early and ascentAB_early
  (stop at the first step meeting the criterion) run for seeds 0 and 2 ->
  results_c.jsonl.

- Step 4: filed CASE-tmprir2y (executed-study), CLAIM-tmp2eemo (the
  finding), CLAIM-tmpqvkag (matched-world baseline); dated notes on
  LEAD-043, CASE-274, QUESTION-010, QUESTION-275, CLAIM-697; changelog
  fragment record/changelog.d/lead-043.md. QUESTION-274 not noted: the run
  does not bear on it (flagged in the LEAD note as the owner's call).

## Next

- Report to the lead. (Lines below are the earlier plan, kept for history.)

- Analysis done (summary.md, summary.json). File the CASE, claims, notes on
  LEAD-043, QUESTION-275, QUESTION-010 and QUESTION-274, and the changelog.

## Choices

- No torch: numpy with a hand-written backward pass (gradient-checked).
- Synthetic facts, 2-layer model, 4 seeds, matched twin per seed (the
  twin's values give every readout its false-positive baseline).
- Fine-tune-away method is open in the lead: run three (unlearn to
  uniform, gradient ascent, overwrite), each at one cue and at two, plus
  catastrophic forgetting by a new task without rehearsal.
- Train to criterion, then as many steps again (min 100): forgetting is not
  read at the boundary where any perturbation restores it.
- Template C (unseen for the target subjects) did not generalize in the
  smoke run (0.06-0.16 on targets before fine-tuning), so it cannot test
  readdressing through an unseen query variant; kept and reported.
- CASE-274's interventions not run: closed-form linear erasure, cue
  remapping, targeted parameter edits beyond overwrite, task-vector merge,
  RL; the budget axis is only coverage from p (no selector).
