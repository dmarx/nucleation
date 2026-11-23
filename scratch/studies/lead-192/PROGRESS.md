# LEAD-192 progress

- Lead: LEAD-192, "Prove a projection perturbation bound for the coarse-graining claim, reading the biorthogonal diffusion wavelets first"
- Branch: claude/lead-192-projection-bound (cut from origin/staging)
- Advances: CLAIM-164. Named in NOTE-984 (Coifman and Maggioni, LIT-1256), whose open question asks for
  a bound of the form ||P_{V~_j} - P_{V_j}|| <= (something) * eps / gap_j for the compressed
  diffusion-wavelet algorithm across levels.

## Task as understood

1. Check the record does not already hold the bound or the reading.
2. Read Maggioni, Bremer, Coifman and Szlam (2005), "Biorthogonal diffusion wavelets", from a lawful
   copy; file LIT, NOTE, THEORY per read-and-file.
3. Attempt the bound; if proved, file a CLAIM (Proposed, demonstrated) with the proof, plus a numpy/pytest check here.
4. Dated notes on LEAD-192, CLAIM-164 (and the entries the reading bears on), changelog fragment.

## Done

- Step 1 (already held?): not held. No LIT for the biorthogonal paper; no changelog fragment or
  note names LEAD-192; no claim holds a bound for the compressed chain.
- Copy search, 2026-11-23 (the biorthogonal paper, DOI 10.1117/12.616909, SPIE Wavelets XI vol. 5914,
  59141M, published 2005-08-18 per Crossref):
  - SPIE Digital Library: paywalled.
  - OpenAlex lists a CiteSeerX record, http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.132.8408;
    https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.132.8408 and the document URL both
    gave "connection reset by peer". Not retried.
  - Maggioni's Yale page has a Wayback capture
    (http://web.archive.org/web/20070703012238/http://www.math.yale.edu:80/~mmm82/), but
    web.archive.org reset the connection. Not retried. math.yale.edu does not resolve.
  - Bremer's Toronto papers directory lists no copy. Semantic Scholar: closed.
  - So the LIT is Unfetched (a lawful copy located, CiteSeerX, and not reached).
- Neighbour read: Sevi, Rilling and Borgnat, arXiv 1811.11636 v3 (ACHA 62 (2023) 390–440,
  doi 10.1016/j.acha.2022.10.003), §8.2–8.3.1, which restates the biorthogonal construction of [36]
  ("Our construction is identical but we also propose a definition for wavelets").
- Proof written (see the CLAIM): per-level bound s_{j+1} <= (d_j + f_j)/sigma_min(R^{2^j}),
  accumulation f_{i+1} <= (||T^{2^i}|| + ||A_i||) f_i + ||A_i||(d_i + d'_i). Symmetric case:
  f_j <= sum 2^{j-i} d_i... (2 d_i per level), sigma_min = lambda_k^{2^j}.
- Numerical check and pytest: lead192.py, test_lead192.py, 9 tests pass. results.txt.

## Choices made

- The bound is stated against the column (range) residual the algorithm controls, not against
  eps directly, so it covers any truncation rule; for RRQR the residual is at most p(k, n) times
  the next singular value.
- The target subspace is the top-k invariant subspace with k the computed dimension, so a
  dimension mismatch at a gapless threshold shows up as a vacuous bound, not a wrong one.

## Next

- File LIT (Unfetched), LIT + NOTE + THEORY for the neighbour, the CLAIM, dated notes on
  LEAD-192, CLAIM-164, NOTE-984? (held NOTE: dated note allowed), THEORY-758; changelog fragment.
