# LEAD-072: signalling estimators, a stated error and a no-signalling test

Run on 2026-11-22. CPU only, numpy 2.5 / scipy 1.18, BLAS threads 1.

| file | what it does |
|---|---|
| `sig.py` | plug-in and root-U2 estimators; simultaneous Clopper-Pearson ("box") and Newcombe intervals for Δ; Bonferroni-Fisher no-signalling test; exact moments and coverage by enumeration |
| `test_sig.py` | 9 pytest tests (U2 exactly unbiased; CLAIM-235's one-occurrence case; Newcombe's published example; exact Fisher size; CP coverage) |
| `exact.py` → `exact.jsonl` | per content, by exact enumeration: mean and RMSE of both estimators, coverage of each interval at the level a rank-2 system uses, rejection rate of Fisher at 2.5%; n = m in {1,2,3,5,10,30,100}, eight (p, p') pairs |
| `mc.py` → `mc.jsonl` | whole rank-2 systems (two contents sharing each context's occurrences, correlated), 4,000 replications a cell: Δ bias and RMSE, coverage of both Δ intervals, size and power of the test, rate at which the box lower bound reaches 2 |
| `floor.py` → `floor.md` | the least worst-case null probability of any table, n^n m^m/(n+m)^(n+m), checked for n, m ≤ 40, and the least counts at which any valid 5% (2.5%) test can reject |
| `apply.py` → `apply.md` | the estimators, intervals and test on LIT-842's binary systems (arXiv:2107.14589v1 LaTeX), counts taken as each row's least common denominator |
| `summary.md` | the tables the record entries quote |

Rerun, from this directory:

    export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
    python3 -I -m pytest -q -p no:cacheprovider test_sig.py
    python3 -I exact.py          # ~2 min; resumes, skipping cells written
    python3 -I mc.py             # ~25 min on a loaded machine; resumes
    python3 -I floor.py > floor.md
    python3 -I apply.py > apply.md

Seeds are fixed (mc.py: 7200 + 31 n + sum of the model name's code points).

LIT-851's appendix was not reachable (discovery.ucl.ac.uk: Cloudflare
challenge, HTTP 403, 2026-11-22; Semantic Scholar API: HTTP 429), and per
NOTE-654 it prints no occurrence counts anyway, so it is not applied here.
