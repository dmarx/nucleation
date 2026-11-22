# LEAD-168 progress

- Lead: LEAD-168 (advances QUESTION-278, QUESTION-279)
- Branch: claude/lead-168-enforcement-arrangements (cut from origin/staging)
- Task: construct an executive, a reviewer and an enforcer in two arrangements
  alike in routine operation, one with enforcement of corrective orders
  independent of the executive (I) and one in which the executive can
  condition it (C); write both precisely and derive where they first differ.

## Done

- Step 1: checked the record. No entry formalizes the two arrangements
  (grep for enforcer/condition across claims, cases, terms, incl. tmp codes).
  Nearest: CLAIM-462 (Active), CLAIM-414 (method), TERM-069 (probe family),
  CLAIM-tmpsaql8 / CASE-tmp8riid (timing margin).

- Step 2: model.py, study.py, test_model.py (7 pass), README, results.
  Readings: A fixed policies (first difference at enforcement, only on an
  adverse order E withholds); B delay (timing first, outcome only past the
  deadline); C anticipation (moves to ruling, then to the action itself, so
  'alike in routine' fails where E is deterred in I); D non-execution
  ambiguous in C (QUESTION-279); E structural edge E->F.

## Next

- File CASE (executed study) and CLAIM(s); alternatives where readings part.
- Dated notes on QUESTION-278, LEAD-168; changelog fragment.
