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

## Next

- Design and choices (README.md)
- Code + pytest
- Run, persist per item
- File CASE, claims, notes, changelog
