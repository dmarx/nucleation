# LEAD-075 progress

- Lead: LEAD-075 (advances QUESTION-392; operationalized_in CASE-198)
- Branch: claude/lead-075-staging-state (cut from origin/staging)
- Task: build A's staging-state model (states A, B and a staging state C),
  compute over parameters the bottleneck budget B*(A,B) (CLAIM-571), the
  least time T*(A,B;b) at budget b, and the readiness R^pi(A->B;b,z)
  (TERM-115); find which of the four kinds of case occur (statically
  feasible but unreachable; reachable but too expensive; reachable only
  through an architectural change; reachable only with temporary reserve
  capacity). File a CASE (executed-study), a CLAIM if warranted, dated
  notes on QUESTION-392, CASE-198 and LEAD-075, and a changelog fragment.
- Step 1 check: no case or claim already holds the experiment's results
  (grepped QUESTION-392's citers, CASE-198, CLAIM-571, TERM-115,
  LEAD-117, CLAIM-761, CLAIM-576). Not held.

## Done

## Next

- Read CLAIM-357, CLAIM-586, CLAIM-568, TERM-106, record.md fields.
- Write model + tests, run sweep.
- File CASE, CLAIM, notes, changelog.

## Choices
