#!/bin/sh
# Extensions of the SGD sweep, run after the main grid (each resumable).
# E1: higher noise (batch 1, rates up to 0.2), 1,000 epochs.
# E2: the 5+-gon initialisation on the main grid at n = 1,000.
# E3 (run_long): ten times the paper's budget, 45,000 epochs.
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
case "$1" in
  short)
    python3 -I sgd_sweep.py results/sgd_ext_highnoise.jsonl --epochs 1000 --ns 500,1000 --batches 1 \
      --lrs 0.05,0.1,0.2 --inits 4gon,5pgon,prior --seeds 4
    python3 -I sgd_sweep.py results/sgd_ext_5plus.jsonl --ns 1000 --batches 100,20 \
      --lrs 0.001,0.005,0.02,0.05 --inits 5pgon --seeds 6 ;;
  long)
    python3 -I sgd_sweep.py results/sgd_ext_long.jsonl --epochs 45000 --ns 1000 --batches 20 \
      --lrs 0.02,0.05 --inits 4gon,5pgon,prior --seeds 4 ;;
esac
