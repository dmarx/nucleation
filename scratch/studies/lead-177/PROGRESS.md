# LEAD-177 progress

- Lead: LEAD-177 (advances QUESTION-285, QUESTION-128; operationalized in CASE-239)
- Branch: claude/lead-177-forager-ladder (cut from origin/staging)

## Task as understood

Build, in numpy, a ladder of systems with identical sensory correlations
but different memory persistence, downstream use and adaptive capacity:
CASE-238's fail-safe relay, CASE-240's debugger's test, CASE-242's
four-probe chain, then CASE-239's forager that learns its own failure
criteria (five arms, three unforeseen changes), and a sensor network that
revises its correspondences for the top rung. Run the comparison, test
with pytest, file the result as an executed-study CASE (Proposed) and
claims as warranted; dated notes on held entries and the lead.

Step 1 check (2026-11-22): no executed study of CASE-239/238/240/242
is held; LEAD-177 has no earlier filing. CLAIM-648 and CLAIM-tmp974nn
cite CASE-239 as not yet run.

## Done

- forager.py, ladder.py, network.py built; 18 pytest tests pass.
- Runs complete: results/forager.jsonl (1,760), ladder.jsonl (2,400),
  network.jsonl (360); summaries in results/*_summary.md.
- Choices made: see README.md.

- Filed: CASE-tmpz762n (ladder + forager), CASE-tmp33vf4 (network),
  CLAIM-tmppa4rs, CLAIM-tmpnc1mf / CLAIM-tmphrp1s (alternatives),
  CLAIM-tmpvqmwc; dated notes on LEAD-177, CASE-239, QUESTION-285,
  QUESTION-128, CLAIM-648; changelog fragment record/changelog.d/lead-177.md.

## Next

- Nothing for this worker. The lead opens the pull request; the owner
  chooses between CLAIM-tmpnc1mf and CLAIM-tmphrp1s.
