# LEAD-059 progress

- Lead: LEAD-059, "File the demonstrated corollary that answers part of the question on reinforcing loops"
- Branch: claude/lead-059-corollary (cut from origin/staging)
- Task as understood: file, as a demonstrated CLAIM, the corollary of CLAIM-366 named as a by-product in the curation entry of 2026-11-07 (082259), answering part of QUESTION-127; give it a proof and a numeric check; add dated notes.

## Done

- Read CLAUDE.md, the lead, QUESTION-127, CLAIM-366, curation 2026/11/07/082259, CLAIM-629, QUESTION-499.
- Finding: the corollary 082259 names (common descent constant on orbits of function-preserving diffeomorphisms; a fixed Euclidean budget not, 612 at (4, 1) against 288 at (2, 2)) is already held as CLAIM-629 (filed 2026-11-07 from the same review, Active since 2026-11-20, demonstrated, with two numeric checks). Its part of QUESTION-127 is split off as QUESTION-499, Answered.

- Re-ran scratch/formal/orbit_descent_check.py (chain rule holds; common descent 0 mismatches on 300 rescalings and swaps; Euclidean Phi_r differs on 192 rescalings, 0 swaps; 612 vs 288) and scratch/formal/claim629_orbit_controls.py (verdicts 292/108 of 400; 0 mismatches on symmetries; controls fire 16 and 101). Hand check: gradients (6, 24) and (12, 12), diag(1/2, 2)^T (12, 12) = (6, 24).
- Dated note of 2026-11-22 on LEAD-059: held by CLAIM-629, checks re-run, title mislabelled ("reinforcing loops"), nothing remains; Done is the owner's call.
- Changelog fragment record/changelog.d/lead-059.md.
- run-lead skill, step 1: added a bullet to check whether the lead's target is already held before filing (the gap this run showed).

## Choices

- No new CLAIM filed: under ADR-072 an idea gets a code only when the record does not already hold it. A second code would duplicate CLAIM-629.
- No dated notes on QUESTION-127 or CLAIM-366: both already carry notes pointing to CLAIM-629 (2026-11-07 on CLAIM-366; 2026-11-11 and 2026-11-20 on QUESTION-127), and this run adds nothing to them.

## Next

- Nothing. Report to the lead.
