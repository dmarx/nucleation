# LEAD-182 progress

- Lead: LEAD-182 (find or run an adequately powered CbD test on human pragmatic judgements)
- Branch: claude/lead-182-pragmatic-cbd (cut from origin/staging)

## Task as understood

1. Literature check for a powered CbD test on pragmatic judgements (Europe PMC, arXiv, OpenAlex; no email). Log queries in search.md. Register at most ~8 works, read at most 3.
2. If none: write the design: signalling-robust estimators, outcome coding fixed in advance, power analysis by simulation (the lead's method includes `empirical`; the study itself is not run).
3. File: a CASE (proposed-study) for the design, a CASE (executed-study) for the power simulation, readings per read-and-file 5-9, a dated note on LEAD-182, a changelog fragment.

## Done

- search.md: Europe PMC and arXiv searched; OpenAlex refused (rate limit, no key; stopped). No powered CbD test on pragmatic judgements found.
- Read Lo, Sadrzadeh and Mansfield 2023 (arXiv 2308.16498): LIT-tmpgkx6w, NOTE-tmplr2g0, THEORY-tmpdcw35.
- Bruza, Lee and Hoyte 2025 (faces, CbD): Europe PMC fullTextXML returned HTTP 500, MDPI PDF 403, PMC page reCAPTCHA. Stopped; to file as Unfetched (LIT-tmpj8zjs).
- cbd.py (estimators), test_cbd.py (14 tests pass), power.py (grid, JSONL resume).
- Full power run started 2026-11-22 (184 cells, 800 reps, 799 bootstrap resamples; ~4 s a cell).

## Choices made

- Rank-4 cyclic (Bell-CHSH) layout, between subjects, two free binary answers per respondent: keeps Lo et al.'s layout but elicits each pronoun's answer, so signalling is observed and discounted, not designed away.
- Statistic: CbD Delta_C with the odd sign pattern fixed in advance (alternatives simulated: maximum over patterns; one-SE soft-thresholded signalling; Wald).
- Inference: percentile bootstrap within contexts, one-sided 0.05; eight items Bonferroni as a variant.
- Not registered: Dzhafarov and Cervantes 2026 (levels of joint distributions; a cyclic system's contexts are pairs, so it adds nothing to this design).

## Next

- Register LIT-tmpj8zjs (Bruza, Unfetched), LIT-tmp43x53 (Snow Queen, Deferred), LIT-tmptblig (garden-path, Deferred).
- When the run ends: summarise results (summary.md), README.md.
- File CASE-tmpl2va4 (proposed-study design), CASE-tmpjp6vg (executed-study power simulation), CLAIM-tmpu482h (pooling counterbalanced cells can create CbD contextuality), CLAIM-tmpalxab (plug-in signalling bias and the sample size it costs).
- Dated notes: LEAD-182 (+ operationalized_in), CASE-053, CLAIM-325, CLAIM-009, CLAIM-105.
- Changelog fragment record/changelog.d/lead-182.md.
