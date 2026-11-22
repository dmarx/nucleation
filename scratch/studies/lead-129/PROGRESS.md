# LEAD-129 progress

- **Lead:** LEAD-129 — "Compare institutions with and without effective means to
  revise their governing standards, matched on resources and independence of
  evidence." Advances CLAIM-685 (reflexive accountability hypothesis).
- **Branch:** claude/lead-129-revision-means (cut from origin/staging)
- **Worktree:** /home/user/nucleation/.claude/worktrees/agent-a813af3ed1ad5c328

## Task as understood

CLAIM-685: institutions able to recognize, authorize and carry out revisions of
their own governing standards avoid persistent normatively significant failures
better than institutions that only monitor outcomes against fixed standards,
where inherited standards are inadequate, and not on routine work. The lead asks
for a comparison matched on resources and on independence of evidence
(CLAIM-342) — some institutions with effective revision means, some with
outcome-monitoring only. File the finding as a CASE (executed-study, standing
documented). Small-N matched comparison from public documents; illustrative,
not a powered test. State selection rule and matching explicitly.

## Design decisions

- Domain: public standards bodies with published revision procedures and
  revision histories (open, lawful sources).
- "Effective means to revise": a standing, resourced procedure that recognizes,
  authorizes and executes changes to the governing standard on a regular cadence
  with published errata/revisions.
- "Outcome-monitoring only": a body that tracks conformance/outcomes against a
  standard held effectively fixed (rare revision, no standing revision organ).
- Outcome: persistence of a normatively significant failure (a known defect in
  the standard) — time between recognition and correction.
- Matching: on resources (scale/funding/staff, proxied) and on independence of
  evidence (whether defect reports come from outside the body).

## Done

- (step 0) Read CLAUDE.md, run-lead skill, design principles, ADR-068, CLAIM-685,
  CLAIM-342, docs/record.md CASE contract, example executed-study CASE.
- (step 1) Confirmed target not already held (searched record/cases.d, claims.d).

- (step 2) Verified load-bearing facts against public pages (WHATWG FAQ, 2019
  W3C-WHATWG MOU, Unicode stability + reporting, Gregorian reform). No obstacle.
- (step 3) Built pairs.json, summarize.py (python3 -I), test_summarize.py (4
  pass), README.md. All three matched gaps positive; extreme = 857 yr.
- (step 4) Filed CASE-tmp3pe1j (executed-study, documented, Proposed):
  illustrates CLAIM-685, bears_on QUESTION-128. Owner's call on the illustrates
  link surfaced in the case and the lead note.
- (step 5) Dated note on LEAD-129 (status/stage untouched); changelog fragment
  record/changelog.d/lead-129.md.

## Done — complete

Everything pushed. No PR opened (lead opens it). Nothing left blocked.
