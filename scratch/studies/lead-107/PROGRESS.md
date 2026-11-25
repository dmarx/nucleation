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

## Choices made

- Unit: a sentence of a reconstruction carrying a restatement cue; items are
  the codes it names; coded = code dated strictly before the exchange start.
- Distance only where the restatement is quoted; the original is the code's
  current title (and title + summary).
- Rules v1 fixed before the comparisons; v2 repairs four false positives
  found after the first run (CODEBOOK.md, Deviation). Both kept.
- The coder audited its own rules on 60 sampled events (AUDIT.md); no second coder.

## Done

- Codebook, script, tests (10 pass), results v1 and v2, audit, README.
- Filed: CASE-tmp4niuz; CLAIM-tmp9w3p9 (thesis); CLAIM-tmpc5mmp (counter,
  alternative A) and CLAIM-tmp49ilj (granted, alternative B, leaned to);
  dated notes on LEAD-107, CLAIM-180, CLAIM-182, CLAIM-191; changelog
  fragment record/changelog.d/lead-107.md.

## Next

- Nothing for this worker. Remaining for a separate lead / the owner: a
  verbatim transcript coded for every restatement (recognised or not) with
  its earlier statement; a human second coder; a blind direction rating for
  CLAIM-191; the owner's choice between the two readings.
