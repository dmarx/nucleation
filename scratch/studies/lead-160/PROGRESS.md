# LEAD-160 progress

- Lead: LEAD-160 (run the world-model achievements study, CASE-187, under matched competence)
- Branch: claude/lead-160-gridworld-agents (cut from origin/staging)

## Task as understood

Build CASE-187's three agents on a small gridworld in numpy: an explicit
transition model with planning, a directly learned goal-conditioned policy,
and a distributed predictive-state controller. Match them on competence over
a declared goal family. Run the four tests (goals; on-demand predictive and
interventional queries; targeted interventions on internals; environmental
change and damage to the predictive machinery). Report which achievements
are linked and which come apart. File the result as a Proposed
executed-study CASE plus claims as warranted.

Held-check (step 1): no executed study cites CASE-187, CLAIM-513/514/519 or
QUESTION-362; no lead-160 study dir or branch. Not held.

## Done

- Design and choices: README.md (8x8 mazes with loops; M table+VI, P
  hindsight Q-learning, D action-conditioned occupancy demons; matched by
  same stream and same "unknown = stay" prior; levels by planner success).
- gridagents.py + test_gridagents.py (12 tests pass).
- run_study.py over 20 mazes: results.jsonl (380 items), summary.md.

- Filed: CASE-tmp6hkf9 (executed study, Proposed, variant_of CASE-187),
  CLAIM-tmpq92r4 (query availability), CLAIM-tmpo59pd (intervention
  scope); dated notes on LEAD-160, CASE-187, QUESTION-362, CLAIM-513/514/519;
  changelog fragment record/changelog.d/lead-160.md.

## Next

- Report to the lead (no PR; the lead opens it).

## Choices made

- Tabular, deterministic, fully observed 8x8 mazes with loops (README).
- D = action-conditioned successor representation (occupancy demons).
- Matching by a shared stream and shared "unknown = stay" prior; levels by
  planner success; costs reported, not equalized.
- Budgets: own per-decision computation, and the planner's as common.
- Intervention: unit-level local fixed-point edit; D_global variant.
