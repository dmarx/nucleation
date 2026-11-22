# LEAD-041: progress

- Lead: LEAD-041
- Branch: claude/lead-041-perspectives
- Task as understood: (1) write the argument that the evaluative space
  model's two channels (positivity, negativity) are perspectives in the
  sense CLAIM-440 consequence 4 needs; (2) specify the procedure that reads
  from a record of conduct which ordering prevails, how strongly and whether
  it resumes, separating ambivalence from neutrality (QUESTION-268);
  (3) apply it to one open, lawfully readable record of conduct, filed as a
  CASE.

## Done

- Read LEAD-041, QUESTION-268, CLAIM-440, TERM-072/076/077/078, NOTE-1101.
- Record of conduct chosen: the FOMC's policy-rate decisions, with the
  dual mandate's two channels (inflation, employment) as the perspectives.
  Rankings built from the Philadelphia Fed's real-time vintages (what was
  known at the time), decisions from the Fed's H.15 effective funds rate.
- Obstacles, 2026-11-22 (not retried): fred.stlouisfed.org empty reply /
  HTTP2 stream reset; api.bls.gov v1 "daily threshold ... reached";
  download.bls.gov 403 Access Denied; www.cbo.gov/data/budget-economic-data 403.
  So no CBO natural rate: u* is a trailing mean (choice, with sensitivity).
- Downloaded (scratchpad, not committed): H.15 package; Philly Fed
  rucQvMd.xlsx and cpiQvMd.xlsx.
- procedure.py and test_procedure.py (12 synthetic cases, passing).
- fomc.py run: 18 specifications, results/ and results/summary.md;
  power.py: results/power.txt. README.md says how to rerun.
- Findings: contests in 43-72 of 243 quarters, mostly 1970-83; most
  contested windows indeterminate; ambivalence shown only in Burns tenure
  (A nominal) and 1980-81 (C nominal); inertia prevails 1994-97 / 2014-17;
  no channel persists over two windows, so no resumption to read.

- Filed: CLAIM-tmp0uism (argument), CLAIM-tmpaibxx (alternative, counter),
  CLAIM-tmpkcsp7 (procedure, answers QUESTION-268), CASE-tmpjw1l1 (FOMC
  application); dated notes on LEAD-041, QUESTION-268, CLAIM-440;
  changelog fragment record/changelog.d/lead-041.md.

## Next

- Report to the lead (no pull request; the lead opens it).

## Choices made

- FOMC over Wells Fargo (CASE-151): a public, machine-readable record in
  time, two statutory channels mirroring the ESM's two, rankings measurable
  independently of the decisions, and known episodes (1970s stop-go,
  1980 interruption) that test ambivalence and resumption.
