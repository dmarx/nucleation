# LEAD-122 progress

- **Lead:** LEAD-122 — Count, in the workbench reconstructions, the share of
  moves of comparable content filed by contributor and by kind of move.
  Advances QUESTION-072.
- **Branch:** claude/lead-122-workbench-move-census (cut from origin/staging)

## Task as understood

The workbench reconstructions (`record/workbench.d/`) record working sessions
on the record's own argument, marking which moves were filed and which were
not. QUESTION-072 part 1 asks whether, holding content fixed, a move's chance
of being filed is independent of who made it (owner vs assistant). The lead
asks for the count: share filed, broken down by contributor and by kind of
move. Deliver a Python script, a results file and a README under
`scratch/studies/lead-122/`, then file a CASE (executed-study, documented)
bearing on QUESTION-072.

## Operationalization (choices made, see README)

- A **move** = a disposition item under the reconstructions' own bold labels
  (Filed / Missed / Not filed / Struck / Held / Not done / Corrected).
- **filed** vs **not-filed** bins from those labels; Corrected reported apart.
- **contributor** from attribution tokens in the item: owner (`owner`/`U\d`),
  assistant (`A\d`/the assistant), reader, both, or unattributed.
- **kind of move** from the dominant scheme code named (CLAIM/QUESTION/TERM/
  CASE/ARG/NOTE/THEORY/LIT).
- Known limit: only label-bearing entries are captured; free-prose entries are
  reported as uncaptured. "Comparable content" cannot be verified by script.

## Done

- [x] Read CLAUDE.md, design principles, run-lead skill, LEAD-122, QUESTION-072,
      workbench template + samples, docs/record.md CASE/CLAIM schema.
- [x] Step 1: confirmed no executed-study already counts workbench moves.
- [x] Pushed branch with PROGRESS.md.
- [x] Wrote census.py + test_census.py (6 tests pass); ran over 135 entries.
- [x] results.json written (149 KB).

## Result (headline)

135 workbench files; 47 carry the record's bold disposition labels, 88 are
free prose (uncaptured). 698 label-spans = moves; 454 are filed/not-filed
(209 filed, 245 not). Share filed: owner-attributed spans highest (0.70 block
/ 0.67 span-only), assistant lower (0.57 / 0.41), most spans co-attributed
("both" 0.41/0.38). By kind: note 0.79, case 0.59, question 0.55, claim 0.44,
term 0.39, work 0.26, theory 0.0. The owner > assistant filing-rate gap is
robust to the attribution window, but is NOT content-matched (QUESTION-072
part 1's "content held fixed" is not met) and kind confounds contributor.

## Done (filing)

- [x] README.md written.
- [x] Filed CASE-tmpkge6r (executed-study, documented, Proposed) bears_on
      QUESTION-072.
- [x] Dated note of 2026-11-22 on LEAD-122 (done + what remains) and on
      CLAIM-177 (aggregate counterpart). No status/stage change.
- [x] Changelog fragment record/changelog.d/lead-122.md.
- [x] Pre-commit checks pass (FM parses, no code in title, H1 matches).

## Next

- [ ] Final commit + push; report.
