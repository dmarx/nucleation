# LEAD-135 — Run individuation by probing at rising budgets

- Lead: LEAD-135 (operationalizes CASE-202; advances QUESTION-382, CLAIM-583, CLAIM-322)
- Branch: claude/lead-135-individuation-budgets (cut from origin/staging)

## Task as understood

Build CASE-202's individuation-by-probing component in numpy: take two
small constrained mechanisms that agree under a restricted (static) probe
family but differ internally, probe them at rising probe budgets (number of
single-flip moves a probe may attempt), and record at what budget each
verdict (distinguishable / not) stabilizes and whether they ever diverge.
Seed pair = CLAIM-583's two 3-bit systems: A = {000,111} (D1={000},
D2={111}, no admissible single-flip path) and B = {000,001} (D1={000},
D2={001}, one-flip path). Controls per CASE-202: reset vs acted-on copy
(discovering vs creating a difference). Test with pytest. Persist per item.

## Choices made (see report)

- "Verdict" = the reachability-between-demands relation (which demands are
  reachable within budget b from a config meeting a given demand); the
  static family (b=0) = "which demands does a config already meet".
- Probe budget = max single-flip moves staying inside the admissible set.
- Prober is non-destructive (queries only), so reset == acted-on by
  construction; that is itself the control result (difference discovered,
  not made). Owner's call left: whether to also model a destructive probe.
- Added a tunable path family (threshold = path length L) to show the
  stabilization budget is a measured quantity, not fixed at 1.

## Done

- (step 0) Read CLAUDE.md, run-lead skill, DPs, ADR-001/048, record.md,
  CASE-202, CLAIM-583/322/574/566/347, QUESTION-382, TERM-088/114.
- (step 1) Confirmed not already held: no executed-study cites CASE-202 or
  CLAIM-583; CASE-202 is a proposed-study, nothing operationalizes it yet.

## Next

- Write prober.py (numpy), run on seed pair + path family, write results jsonl.
- Write test_prober.py, run pytest.
- File: CASE (executed-study) + CLAIM (finding) + changelog + dated note on LEAD-135.
