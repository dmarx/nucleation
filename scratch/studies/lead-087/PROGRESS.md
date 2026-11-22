# LEAD-087 progress

- Lead: LEAD-087
- Branch: claude/lead-087-shared-perspective (cut from origin/staging)

## Task as understood

Write, before any simulation, the criterion that distinguishes a shared
perspective (TERM-072 sense 1, shared across agents) from merely
correlated responses or socially learned norms (CASE-145's A4 risk), and
commit it. Then simulate CASE-145's populations (same structured
training; interacting vs independent; with vs without a collective
decision mechanism) in numpy, apply the criterion, and file an
executed-study CASE, a CLAIM if warranted, dated notes on CASE-145,
CLAIM-418, QUESTION-260 and LEAD-087, and a changelog fragment.

## Step 1 check

Target not already held (2026-11-22): no executed study cites CASE-145,
CLAIM-418 or QUESTION-260; no criterion separating shared perspective
from correlated responses is filed (grep of CASE-145, LEAD-087,
QUESTION-276, TERM-072, NOTE-1802). QUESTION-276 asks a neighbouring
question (perspective vs common-cause coactivity); TERM-072's defeater
(A8's test) is the same risk.

## Choices

- The criterion is filed as two rival TERMs (Proposed), because its third
  condition admits two readings of A8/A11 that classify enforced norms
  differently: TERM-tmpsu4df (evidential answerability) and TERM-tmpo4pxh
  (restoration). Choosing is the owner's.
- Model, arms, thresholds and predicted verdicts are in README.md,
  "Stated in advance", committed with the TERMs before any code.

## Done

- Criterion written and committed before any simulation (TERM-tmpsu4df,
  TERM-tmpo4pxh, README pre-registration).

## Next

- Code model.py, measures, tests; smoke run; full run (results.jsonl).
- File CASE (executed-study), CLAIM if warranted, notes on CASE-145,
  CLAIM-418, QUESTION-260, LEAD-087; changelog fragment.
