# LEAD-192 progress

- Lead: LEAD-192, "Prove a projection perturbation bound for the coarse-graining claim, reading the biorthogonal diffusion wavelets first"
- Branch: claude/lead-192-projection-bound (cut from origin/staging)
- Advances: CLAIM-164. Named in NOTE-984 (Coifman and Maggioni, LIT-1256), whose open question asks for
  a bound of the form ||P_{V~_j} - P_{V_j}|| <= (something) * eps / gap_j for the compressed
  diffusion-wavelet algorithm across levels.

## Status: done; waiting for the owner's pull request and review

## Done

- Already held? No. No LIT for the biorthogonal paper; no changelog fragment or note names LEAD-192;
  no claim holds a bound for the compressed chain.
- Copy search, 2026-11-23, for the biorthogonal report (doi 10.1117/12.616909, SPIE 5914, 59141M,
  2005-08-18): SPIE paywalled; CiteSeerX record 10.1.1.132.8408 reset the connection (summary and
  document URLs); Wayback capture of Maggioni's Yale page
  (http://web.archive.org/web/20070703012238/http://www.math.yale.edu:80/~mmm82/) reset; Semantic
  Scholar closed; Bremer's Toronto directory lacks it. Not retried. Abstract read on Duke's listing.
  -> LIT-tmpzikaq, Unfetched.
- Neighbour: Sevi, Rilling and Borgnat, arXiv 1811.11636 v3 (ACHA 62 (2023) 390–440), §§1.2, 4.4, 8,
  8.2–8.3.1 read -> LIT-tmpyklac (Active), NOTE-tmpv196v (Skimmed), THEORY-tmpyi9zg (Proposed).
- Bound proved -> CLAIM-tmpdsu37 (Proposed, thesis, demonstrated): Lemma 2 (drift accumulation,
  column and row residuals), Theorem 3 (kept subspace within (d_j + f_j)/sigma_min(R^{2^j})),
  Theorem 3' (Davis–Kahan form, symmetric), Corollaries 4 (graded) and 5 (closure).
- Check: lead192.py, test_lead192.py (9 tests pass), results.txt/json. README.md says how to rerun.
- Dated notes: LEAD-192, CLAIM-164, NOTE-984, THEORY-758, QUESTION-218, QUESTION-222.
- Curation entry record/curation.d/2026/11/23/014039.md; changelog record/changelog.d/lead-192.md.
- Narrow diagnostic: luria.ref_status.scan on the changed files: no unused excuses, nothing lost.

## Choices made

- The bound is stated against the column residual the algorithm controls, not against eps directly,
  so it covers any truncation rule; for strong RRQR the residual is at most p(k, n) times the next
  singular value.
- The target subspace is an invariant subspace of the computed dimension, so a dimension mismatch at a
  gapless threshold shows up as a vacuous bound, not a wrong one.
- CLAIM-tmpdsu37 `corroborates` CLAIM-164 (alternative: `complements`; owner's call).

## Next (for the owner)

- Open the pull request into staging; choose corroborates or complements; decide whether to allow
  web.archive.org and citeseerx.ist.psu.edu so the 2005 report can be read.
- Open: whether the drift's doubling per level is ever attained.
