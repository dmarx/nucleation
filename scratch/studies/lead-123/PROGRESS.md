# LEAD-123 progress

- **Lead:** LEAD-123 — Build the three-perspective agenda model with a latent
  Condorcet cycle, in which a chair or a legibility regime controls which
  pairwise contests enter the record.
- **Branch:** `claude/lead-123-condorcet-agenda`, cut from origin/staging.
- **Advances:** CLAIM-448 (Active), CLAIM-451 (Proposed), CLAIM-440 (Proposed).

## Task as understood

CLAIM-448 names this model under "What would settle it": a three-perspective
agenda model with a latent Condorcet cycle, where a chair or legibility regime
controls which pairwise contests enter the record; compare the graph of all
possible contests with the graph of admitted ones, then add a protected
challenge channel. Build it in numpy. Show how the recorded outcome depends on
the agenda rule (chair control, agenda order, legibility filter). Relate to
CLAIM-448/451/440. Test with pytest.

CASE-221 (Proposed, kind `construction`) already does the smallest case by hand
(`scratch/formal/agenda_cycle_check.py`): a chair admitting two of three
contests. It explicitly does NOT show persistence, real interventions, or
intent, and is a single round. This lead builds the full numpy model
(generalizing over agenda rules and legibility filters, with a protected
challenge channel and a persistence/sequential-window variant) as an
executed-study CASE giving CLAIM-448's existence half a demonstrated warrant.

## Choices made

- File the study as a CASE, kind executed-study, standing documented,
  illustrating CLAIM-448; a variant_of CASE-221 (the hand construction it
  generalizes). (Not a counterexample: it confirms, it does not refute.)

## Done

- Read CLAUDE.md, design principles, ADR-001, ADR-048, run-lead skill, lead
  file, CLAIM-448/451/440, CASE-157, CASE-221, docs/record.md CASE fields.
- Step 1: target not already held as an executed study (CASE-221 is a hand
  construction, smallest case only). Proceeding.
- Branch cut, PROGRESS.md pushed.

## Done (continued)

- Built agenda_model.py, test_agenda_model.py (9 pass), results.json, README.
- Filed CASE-tmpn19tk (executed-study, documented, Proposed; illustrates
  CLAIM-448, variant_of CASE-221, bears_on QUESTION-269).
- Dated notes of 2026-11-22 on CLAIM-448, CLAIM-451, CLAIM-440, LEAD-123.
- Changelog fragment record/changelog.d/lead-123.md.
- Per-file checks pass (yaml parses, no code in title, H1 matches).

## Next

- Commit/push filing. Report. (No PR; owner decides status/stage/warrant.)
