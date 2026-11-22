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

## Next

- Write the study script and tests; smoke-run; full run; file.

## Choices
