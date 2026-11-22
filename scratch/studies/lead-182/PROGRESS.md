# LEAD-182 progress

- Lead: LEAD-182 (find or run an adequately powered CbD test on human pragmatic judgements)
- Branch: claude/lead-182-pragmatic-cbd (cut from origin/staging)

## Task as understood

1. Literature check for a powered CbD test on pragmatic judgements (Europe PMC, arXiv, OpenAlex; no email). Log queries in search.md. Register at most ~8 works, read at most 3.
2. If none: write the design: signalling-robust estimators, outcome coding fixed in advance, power analysis by simulation (the lead's method includes `empirical`; the study itself is not run).
3. File: a CASE (proposed-study) for the design, a CASE (executed-study) for the power simulation, readings per read-and-file 5-9, a dated note on LEAD-182, a changelog fragment.

## Done (all pushed)

- search.md: Europe PMC and arXiv searched; OpenAlex refused (rate limit, no key; stopped). No powered CbD test on pragmatic judgements found.
- Read Lo, Sadrzadeh and Mansfield 2023: LIT-tmpgkx6w, NOTE-tmplr2g0, THEORY-tmpdcw35 (corroborates CLAIM-325, bears_on QUESTION-001).
- Registered LIT-tmpj8zjs (Bruza 2025, Unfetched: Europe PMC 500, MDPI 403, PMC reCAPTCHA), LIT-tmp43x53 (Snow Queen, Deferred), LIT-tmptblig (garden-path, Deferred).
- cbd.py, test_cbd.py (15 pass), power.py -> results.jsonl (184 cells), absence.py -> absence.jsonl (144 cells), summary.md, README.md.
- CASE-tmpjp6vg (executed-study), CASE-tmpl2va4 (proposed-study), CLAIM-tmpalxab (plug-in signalling bias), CLAIM-tmpu482h (pooling creates CbD contextuality).
- Dated notes: LEAD-182 (+ operationalized_in CASE-tmpl2va4), CASE-053, CLAIM-325, CLAIM-009, CLAIM-105.
- Changelog fragment record/changelog.d/lead-182.md.

## Choices made

- Rank-4 cyclic layout, between subjects, two free binary answers: signalling observed, not designed away.
- Statistic: CbD Delta_C, odd sign pattern fixed from a pilot. Detection by the plug-in statistic (valid, conservative); absence only by the Bonferroni bound (plug-in and soft-thresholded absence are invalid in simulation).
- Soft-thresholded statistic rejected (size up to 0.62).
- Reads: one of three allowed (the others were not reachable or not needed).

## Next

- Report to the lead (no PR; the lead opens it).
