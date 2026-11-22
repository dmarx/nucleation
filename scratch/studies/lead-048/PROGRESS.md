# PROGRESS: LEAD-048

- Lead: LEAD-048
- Branch: claude/lead-048-case186-sim
- Task: simulate CASE-186's organization (hidden regime + then - then +
  or 0, audit with generate/admit/score lesionable separately, A/G
  maintenance by reciprocal production, external restoration or none,
  finite fuel), run the core arms (about an hour of CPU at most), measure
  P(S1 and S2), P(S2|S1), the matched-first-stage branch and self-flagging
  of a damaged apparatus. Code reusable by LEAD-140. File a CASE
  (executed-study), a CLAIM if warranted, dated notes on CASE-186, the
  advanced entries and LEAD-048.

## Done

- model.py, test_model.py (7 pass), study.py, analyze.py, README.md.
- Runs started 13:04 UTC: core1 (reference apparatus, 432 cells), core2
  (other admission x scoring arms, ample fuel, 1080 cells), core3
  (reference apparatus, tight fuel, 216 cells). Results append per cell to
  results/core{1,2,3}.jsonl; rerun resumes.

- All runs finished (core1 432, core2 1080, core3 216, baselines 108
  cells; about 10 min CPU). results/tables.md written.
- Filed CASE-tmpl0ccq (executed-study), CLAIM-tmpqaqtx (Proposed, thesis,
  demonstrated), dated notes on CASE-186, LEAD-048, CLAIM-414, CLAIM-522,
  QUESTION-086/285/271/279/016, changelog fragment
  record/changelog.d/lead-048.md.

## Next

- Report to the lead. Remaining work is listed in the LEAD-048 note.

## Choices

- Partial monitoring only (the primary condition); full feedback not run.
- Audit draws 256 samples (scaled by A) and uses them for both the
  likelihood rule and the 256-sample adequacy test.
- Captured scoring shift KAPPA = 0.4: at 0.3 a captured score of a −
  world (0.25 + 0.3 = 0.55) falls inside the adequacy band and the
  adequacy test frees the organization, an artifact.
- Self-check tests each operation on known inputs against commissioning
  values; a flagged apparatus's output is not acted on; repair needs the
  arrangement's producer (reciprocal: A, G >= 0.5; external: service up;
  none: never).
- Copier fidelity is G (evidence governance carries the copying machinery).
- Fuel: ample 0.6, lean 0.36 (equal to ordinary spend; never binds given
  the starting stock), tight 0.25 run on the reference apparatus only.
- Not run: router baseline, full-feedback condition, non-reference arms
  under lean or tight fuel (tiers 4, 5), no-audit baseline.
