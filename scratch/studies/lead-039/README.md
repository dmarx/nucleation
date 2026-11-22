# LEAD-039: when information-bottleneck optima nest

Numerical support for CLAIM-tmp8xj7x (two distinct rows of p(Y|x) nest at
every pair of budgets), CLAIM-tmplxbtx (closure under independent
products) and CLAIM-tmpzohh5 (erasure bound on the cost of forcing
nesting). The study is CASE-tmpo9u3y.

Method: a Lagrangian optimum at β is the decomposition of p(X) on the lower
convex envelope of F_β(r) = H(κᵀr) − H(r)/β (THEORY-753 step 5). On a
simplex grid the envelope is the lower hull of the lifted grid points; the
facet containing p(X) gives the decoder points. Nesting is the hull test
(THEORY-753 step 4), an L1 distance computed by linear programming. The
optima are grid-exact, not certified unique.

## Files

- `ibnest.py`: envelope, decoder points, hull distance, φ.
- `test_ibnest.py`: 6 pytest checks, including a reproduction of
  CLAIM-392's figures (I(X;T) = 0.546 and 0.952 bits, I(T;Y) = 0.097 and
  0.139 bits, failed hull test) and the concavity of φ on 200 random
  channels.
- `run_studies.py`: S1, S2, S3, each writing one JSON line per source and
  resuming from what is written.
- `s1_two_rows.jsonl`, `s2_three_states.jsonl`, `s3_products.jsonl`: results.
- `summarise.py` → `results.md`.
- `check_entries.py`: frontmatter, title and H1 check for the record files.

## Rerun

    cd scratch/studies/lead-039
    export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
    python3 -I -m pytest -q -p no:cacheprovider test_ibnest.py
    rm -f s1_two_rows.jsonl s2_three_states.jsonl s3_products.jsonl
    python3 -I run_studies.py s1   # about 1 minute
    python3 -I run_studies.py s2   # about 8 minutes on a shared machine
    python3 -I run_studies.py s3   # under 1 minute
    python3 -I summarise.py
