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
- [ ] Push branch with PROGRESS.md.

## Next

- [ ] Write census.py + test_census.py; run.
- [ ] Write results.json + README.md.
- [ ] File CASE (executed-study) bears_on QUESTION-072; note on LEAD-122;
      changelog fragment.
- [ ] Report.
