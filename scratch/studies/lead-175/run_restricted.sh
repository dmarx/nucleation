#!/bin/sh
# Region-confined HMC at every rung of the ladder, one region after another
# (each resumable). Run from this directory:  sh run_restricted.sh
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
for R in 6 5 5+ 4+ 4++- 4++ 4; do
  python3 -I posterior.py restricted "results/restricted_$R.jsonl" --region "$R" \
    --chains 8 --blocks 12 --iters 300 --burn 3 --ladder 0.5,10000,64
done
