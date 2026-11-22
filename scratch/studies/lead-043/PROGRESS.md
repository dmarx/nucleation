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

## Next

- Write the model and study script, with tests; smoke-test pace.

## Choices

(none yet)
