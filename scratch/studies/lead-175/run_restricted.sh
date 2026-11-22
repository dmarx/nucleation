#!/bin/sh
# Region-confined HMC at every rung of the ladder, one region after another
# (each resumable). Run from this directory:  sh run_restricted.sh [BLOCKS] [REGIONS...]
# As run: regions 6 and 5 with 12 blocks; then, in two parallel runners,
# "9 5+ 4+ 4++-" and "9 4++ 4" (time).
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
BLOCKS=${1:-12}; shift 2>/dev/null
REGIONS=${*:-"6 5 5+ 4+ 4++- 4++ 4"}
for R in $REGIONS; do
  python3 -I posterior.py restricted "results/restricted_$R.jsonl" --region "$R" \
    --chains 8 --blocks "$BLOCKS" --iters 300 --burn 3 --ladder 0.5,10000,64
done
