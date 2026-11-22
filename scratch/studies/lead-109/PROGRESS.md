# LEAD-109: self-consistent factorizations into agents — progress

- Lead: LEAD-109 (Settle whether a fixed level and target can have several
  self-consistent factorizations into agents).
- Branch: claude/lead-109-factorization-uniqueness, cut from origin/staging.

## Task as understood

The lead advances CLAIM-168 (circularity objection), CLAIM-170 (owner's
thesis: agents = a factorization of a system relative to a level and
target; willed agents individuated by will-organization), CLAIM-174 (the
admission test). The open part (CLAIM-170 note of 2026-10-29, CLAIM-174
"two objections it answers"): at a FIXED level and target, can the
self-consistent fixed-point condition (every block of a partition passes
the admission test) have several solutions that DISAGREE on which regimes
each agent governs, with nothing at that level to choose? CLAIM-170's
defeated_if is exactly such a disagreeing tie.

Notion of self-consistent factorization (CLAIM-170/174/157/154/TERM-044):
a partition P of the system's regimes into blocks is self-consistent at
(level L = variable set, target T) when every block passes:
 (1) System/threshold (CLAIM-157, TERM-049): near-decomposable block whose
     spectral gap delta/eps > tau, tau^2 = Occam (CLAIM-154).
 (2) Description: goal-directed model beats device model by > Occam cost.
 (3) Adaptation (Kenton). (4) Will, for willed agents.

## Plan

Construct, in numpy, small explicit coupling systems and (a) enumerate
partitions clearing the test-1 gap; (b) test whether two crosscutting
(disagreeing) partitions can both clear it; (c) show nested/grain
multiplicity with the CLAIM-154 pricing. Then state the structural result.

## Done

- Read CLAUDE.md, design principles, ADR-001/048, run-lead skill, LEAD-109,
  CLAIM-168/170/174/157/154, TERM-044/047/048/049/023/046, QUESTION-032.
- Step 1 held-check: no executed-study CASE and no CLAIM settling
  factorization uniqueness found in record/ (grep CLAIM-168/170/174).
- Branch cut, PROGRESS pushed.

## Next

- Write the numerical study + pytest under scratch/studies/lead-109/.
- File CASE (executed-study), CLAIM(s) with alternatives, TERM, changelog.

## Choices made

- "self-consistent factorization" read as the per-block membership
  fixed-point of CLAIM-174, not an argmax (per CLAIM-168/174 wording).
- Where the fix is the owner's (define "level" to fix grain, or add a
  selection rule), alternatives are filed, not chosen.
