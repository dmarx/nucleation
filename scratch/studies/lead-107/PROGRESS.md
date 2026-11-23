# LEAD-107 progress

- Lead: LEAD-107 (restatement distance against re-derivation; coded against uncoded items)
- Branch: claude/lead-107-restatement-distance (cut from origin/staging, 2026-11-23)
- Task as understood: code the restatement events reported in the workbench
  reconstructions of exchanges (record/workbench.d/, read only); for each, code
  whether it was re-derived as new or retrieved, whether its item had a code when
  it was restated, and, where the restatement's wording is quoted, its lexical
  distance from the coded original. Compare re-derivation before and after an
  item got its code. Reproducible script with pytest tests here. File a CASE
  (executed-study), Proposed empirical CLAIMs, dated notes on LEAD-107,
  CLAIM-180, CLAIM-182, CLAIM-191, and a changelog fragment.

## Step 1 (already held?)

Not held. grep of record/ for LEAD-107 / LEAD-tmpild5i finds only the lead and
curation 2026/11/19/224759; no changelog fragment, case or claim reports a
restatement-distance measurement or a before/after re-derivation count. Nearest
held work: CASE-306 (LEAD-079, re-derivations in one exchange, no coded/uncoded
split) and CASE-372 (LEAD-122, filing census by contributor).

## Done

## Next

- Survey the reconstructions; write coding rules; script; tests; run.
