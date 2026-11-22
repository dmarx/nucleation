# LEAD-140 progress

- Lead: LEAD-140 (run CASE-255, adapting CASE-186).
- Branch: claude/lead-140-case255, cut from origin/staging.
- Task: on LEAD-048's simulation (scratch/studies/lead-048/model.py), let
  the organization improve its own procedures over generations; transplant
  an earlier and a later improver onto the same fresh state at equal budget
  (2x2 artifact x improver); then damage the diagnostic machinery
  (CASE-186's lesions, with shams). File a CASE (executed-study), a CLAIM if
  warranted, dated notes on CASE-255, CASE-186, QUESTION-457, QUESTION-388
  and LEAD-140. About an hour of CPU at most.

## Checked (step 1)

- CASE-255 is not already run: CASE-300 (executed) is an archival study of
  the record's decisions, not this simulation; CASE-tmpl0ccq ran CASE-186
  only. No lead-140 branch or study existed on staging.

## Choices made

- Artifact = LEAD-048's organization's procedures theta (audit interval and
  size, self-check interval, repair time, teacher-correction rate; TEACH
  added by subclassing Org). Improver = settings phi (candidates per
  generation, share of damage and out-of-family episodes in its suite,
  whether it reads its archive, a canary test of its suite) plus its record
  (archive of moves and measured effects). See rsi.py's docstring.
- Schedule shortened to 350 steps (injury 150, second change 200) for CPU.
- Episode score = throughput less 0.3 when the findings are wrong (S1 and S2),
  since regime 0 has no preferred action.
- Lineage arms: none (no record), archive (fixed phi, growing archive: the
  ADAS-like control), and four adaptive arms differing in how a change to
  the improver is judged: public (performance-gated), own (its own suite),
  external (fixed outer suite, separate seeds), layered (own, with an
  external veto on verification-weakening changes).
- 12 lineages per arm, G = 60; transplant H = 10 generations at 32
  episodes each, 2 replicates; held-out battery of 24 frozen seeds x 6 kinds.
- Two worker processes only (the machine is shared). Stop runs by PID only.
- Not modelled: plain-Markdown arm, schema extension (no mechanism to add a
  distinction), the CASE-108 specialist-with-poor-record arm.

## Done

- rsi.py, test_rsi.py (11 pass), study.py committed.
- Phase 1 (lineages) started.

## Next

- Phase 2 transplant, phase 3 damage; analyze.py; file CASE, CLAIM, notes,
  changelog.
