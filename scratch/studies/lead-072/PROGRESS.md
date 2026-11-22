# LEAD-072 progress

- Lead: LEAD-072 (signalling estimators with bias correction and stated error, or a signalling test with a stated null, applied to LIT-851's systems with their occurrence counts).
- Branch: claude/lead-072-signalling-estimators (cut from origin/staging 15c07a12f).

## Task as understood

Derive (a) a bias-corrected estimator of CbD signalling Δ = Σ_q |⟨R_q^c⟩ − ⟨R_q^c'⟩| for binary cyclic systems with a stated sampling error, and/or (b) an exact test of no-signalling with a stated null; check bias, coverage and size by simulation (numpy); apply to LIT-851's 90 rank-2 systems if their occurrence counts are in a lawful open copy.

## Choices made

- Both an estimator and a test (the lead allows either): no estimator can be unbiased (proof), so "bias correction" is the root of the unbiased squared difference; the stated error is a guaranteed (Bonferroni Clopper-Pearson) interval; the test is Bonferroni over per-content Fisher exact tests.
- LIT-851 not applied: copy blocked (UCL Discovery Cloudflare 403; Semantic Scholar API 429, 2026-11-22), and NOTE-654 says its appendix prints no counts. Applied instead to LIT-842's three printed binary systems (arXiv source, lawful), counts = least common denominator of each row (stated assumption).
- New entries Proposed, as LEAD-182's were.

## Done

- Step 1 (held check): LEAD-182's CLAIM-tmpalxab / CASE-tmpjp6vg quantify the plug-in bias and say a bias-corrected estimator "was not built"; nothing in record/ builds one. Target not held.
- sig.py + test_sig.py (9 pass); exact.jsonl (56 cells); floor.md; apply.md.
- CLAIM-tmp1o9d0 written (bare codes).
- mc.py running (PID in scratchpad lead-072/mc.pid), resumable.

## Next

- Finish mc.jsonl; summary.md; CASE-tmpl6unn (executed-study); dated notes on LEAD-072, CLAIM-235, CLAIM-105; changelog fragment lead-072.md.
