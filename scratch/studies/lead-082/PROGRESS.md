# LEAD-082 progress

- Lead: LEAD-082, "Run the suppressed-against-removed capability study with a benign sleeper-agent stand-in"
- Branch: `claude/lead-082-suppressed-removed` (cut from origin/staging)
- Task: run CASE-275's design at toy scale on CPU: a small model trained with a
  benign triggered behaviour (a trigger token switches the output to a harmless
  alternative mapping), then a safety-style fine-tune that stops the behaviour
  being expressed, then CASE-275's four measures (representation, recruitment,
  transmission, expression) plus recovery under brief retraining, to tell
  masking (suppression) from removal. File an executed-study CASE, a note on
  LEAD-082, a changelog fragment. LEAD-043 (forgetting study) is run by another
  worker; not duplicated here.

## Done

- Step 1: target not held (no executed study of CASE-275; grep of record/ for CASE-275, LEAD-082, sleeper).

- sleeper.py, test_sleeper.py (10 pass), run.py, summarize.py, README.md written.
- Smoke run (width 128, seed 0, all arms) done in scratchpad.
- Main run (width 128, seeds 0-4) started -> results.jsonl; width sweep (32, 512; seeds 0-2) -> results_width.jsonl.
- Template files from `luria new`: record/cases.d/CASE-tmp2zo3t.md, record/claims.d/CLAIM-tmp4223o.md (to fill).

- Main run done (40 rows). CASE-tmp2zo3t and CLAIM-tmp4223o filled; dated note on LEAD-082;
  changelog fragment record/changelog.d/lead-082.md.

## Next

- When the width sweep (results_width.jsonl) finishes: summarize.py, add a width paragraph to
  CASE-tmp2zo3t, commit, report.

## Choices

- numpy MLP (two ReLU layers) rather than a transformer: torch is not installed and a
  hand-written transformer backprop was not worth the risk at this scale. Said in the CASE.
- Behaviours A and B are random permutations of 24 symbols, so B on held-out symbols can
  only come from stored knowledge: recovery is measured on symbols never retrained.
- Recovery has three protocols plus a one-vector elicitation, because the smoke run showed
  full retraining overwrites item by item while gate-only retraining reopens the old map.
- Representation is measured as trigger-presence decodability; a reader for piB itself is
  confounded with decoding x (a permutation is a relabelling), so it was not used.
