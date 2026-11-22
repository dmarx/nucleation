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

- Read CLAIM-357, CLAIM-586, CLAIM-568, CLAIM-571, TERM-106, TERM-115,
  CASE-198, CASE-233, record.md CASE/CLAIM fields.
- Model + 14 tests (pass); sweep run, results.jsonl and summary.txt
  committed. Key results: base B*_H = 1.3, B*_Z = 1.0; all four kinds
  plus "either" and "together" occur on open (b, rho) regions; with a home
  gap staging creates reachability, else lowers B* or does nothing;
  B*_Z = min(B*_H, max(max(h0,h1)+s, h1+beta1/4)) in all 960 sweep rows;
  any staging route takes >= 2.58 (gap: >= 2.1 at high b) against 1.0,
  so at tau = 2 admitting staging changes nothing and every K3 cell
  becomes K4, too expensive, or (with the gap) reachable-not-by-deadline.

- Filed CASE-tmp17sbe (executed-study), CLAIM-tmpmvt0a (thesis,
  demonstrated), dated notes on QUESTION-392, CASE-198, LEAD-075, and
  record/changelog.d/lead-075.md. All pushed.

## Next

- Nothing for the worker: report. The lead opens the pull request into
  staging; docs-check repairs links.

## Choices

See README.md, "Modelling choices" (staging C as architecture; CASE-198
numbers; gap as crease constraint; route-only time; Z as repertoire;
uniform background load and Bernoulli reserve for readiness).
