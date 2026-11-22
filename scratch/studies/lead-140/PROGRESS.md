# LEAD-140 progress

- Lead: LEAD-140 (run CASE-255, adapting CASE-186).
- Branch: claude/lead-140-case255, cut from origin/staging.
- Task: on LEAD-048's simulation (scratch/studies/lead-048/model.py), let
  the organization improve its own procedures over generations; transplant
  an earlier and a later improver onto the same fresh state at equal budget
  (2x2 artifact x improver); then damage the diagnostic machinery (with
  shams). File a CASE (executed-study), a CLAIM if warranted, dated notes on
  CASE-255, CASE-186, QUESTION-457, QUESTION-388 and LEAD-140.

## Checked (step 1)

- CASE-255 is not already run: CASE-300 (executed) is an archival study of
  the record's decisions, not this simulation; CASE-tmpl0ccq ran CASE-186
  only. No lead-140 branch or study existed on staging.

## Choices made

- Artifact = LEAD-048's organization's procedures theta (audit interval and
  size, self-check interval, repair time, teacher-correction rate; TEACH
  added by subclassing Org). Improver = settings phi (candidates, damage and
  out-of-family shares of its suite, reads its record or not, canary) plus a
  record of moves and measured effects. See rsi.py's docstring.
- Schedule shortened to 350 steps. Episode score = throughput less 0.3 when
  the findings are wrong (regime 0 has no preferred action).
- Arms: none, archive (ADAS-like), public, own, external, layered.
- 12 lineages per arm, G = 60; transplant H = 10 at 32 episodes, 2 reps;
  battery 24 frozen seeds x 6 kinds. Two processes; runs stopped by PID only.
- Not modelled: agents with prose records, plain-Markdown arm, schema
  extension, CASE-108's specialist, a second correction of the improver.

## Done

- rsi.py, test_rsi.py (11 pass), study.py, analyze.py, README.md.
- Phases 1-3 run (about 64 CPU-minutes); results/*.jsonl, results/tables.md.
- Filed CASE-tmp6btcq (executed-study) and CLAIM-tmp7ggg0.
- Dated notes on CASE-255, CASE-186, QUESTION-457, QUESTION-388, LEAD-140.
- Changelog fragment record/changelog.d/lead-140.md.

## Next

- Nothing for this worker: report to the lead, who opens the pull request.
