# LEAD-114 study: blind irreducible recovery from a group-composition network

Run (CPU, single thread):

    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 \
      python3 -I run.py          # trains + recovers, writes results.jsonl
    OMP_NUM_THREADS=1 python3 -I -m pytest test_lead114.py -q

Files: groups.py (abstract group tables, one-hot data), model.py (numpy MLP
+ training), reptheory.py (Peter-Weyl block decomposition, class-sum
characters, isotypic projection), run.py (pipeline), results.jsonl
(per-item results, append-only).
