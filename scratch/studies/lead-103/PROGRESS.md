# LEAD-103 progress

- Lead: LEAD-103 — State the operational equivalences among renderings a
  pragmatic experiment assumes and derive the noncontextual inequality they imply.
- Branch: claude/lead-103-pragmatic-inequality (from origin/staging).
- Advances: QUESTION-067, QUESTION-001, QUESTION-026.

## Done
- Read CLAUDE.md, run-lead skill, design-principles opening, LEAD-103,
  QUESTION-067/001/026, CLAIM-142/046/044/009/037, THEORY-315, NOTE-825,
  THEORY-010, TERM-014/031/042, docs/record.md field spec.
- Step 1: target NOT already held in the record's own voice. Nearest is
  THEORY-315 (reading of Catani et al.), which answers QUESTION-067 "in part".
  "operational equivalence" hits in distributed-agency (TERM-055 etc.) are a
  different sense. Kunjwal & Spekkens 2015 unregistered, unread (THEORY-015).
- Derivation + numeric study: scratch/studies/lead-103/ (inequality.py,
  test_inequality.py, results.jsonl, README.md). LP bound = 1.0 on all four
  diamond faces; non-deterministic corroboration 0.874 < 1; qubit orbit
  violates up to √2; OE2 load-bearing (drop it -> 2.0). 5 pytest pass.
- Filed CASE-tmp7nwhq (executed-study) and CLAIM-tmp59ejz (thesis,
  interpretive); dated notes on LEAD-103 and QUESTION-067; changelog fragment.

## Next
- Commit + push filings. Attempt optional Kunjwal&Spekkens 2015 reading if
  time (lead names it; not required — method grounded by held THEORY-315).
- Write report via SubagentHandback.

## Choices made
- Filed as ONE CASE (study) + ONE thesis CLAIM (warrant interpretive: the
  pragmatic mapping is the load-bearing interpretive content; the inequality
  itself is a theorem, demonstrated in THEORY-315 and verified in the CASE).
  Noted in bodies; flagged for owner.
- bears_on QUESTION-067 + QUESTION-001 (partial results, not answers).
  QUESTION-026 (compositionality) left out of relations: the bearing is
  indirect; noted rather than forced.
- Did NOT read Kunjwal & Spekkens 2015: optional, unregistered, and the
  derivation is grounded by the held THEORY-315/NOTE-825. Left in lead note.
