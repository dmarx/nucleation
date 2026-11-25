# LEAD-192: projection perturbation bound for the compressed diffusion-wavelet chain

- `lead192.py`: runs the compressed chain A_0 = T, A_{i+1} = P_{i+1} A_i^2 P_{i+1} on four
  operators (Coifman and Maggioni's circle, three Gaussian clouds, a prescribed gapped spectrum
  with a noisy truncation, and a directed small-world walk T = Pi^1/2 P Pi^-1/2) and records
  every quantity in the bound: column and row residuals, the true and the a priori operator
  error f_j, the true subspace error and both bounds, and closure defects.
- `test_lead192.py`: pytest checks that the bound holds at every level, that exact truncation
  gives the spectral space, that the per-level constant is attained, and that the row residual
  is not controlled by column selection for a non-symmetric T.
- `results.txt`, `results.json`: the output of one run.

Rerun (CPU, under a second each):

    OPENBLAS_NUM_THREADS=1 python3 -I scratch/studies/lead-192/lead192.py scratch/studies/lead-192/results.json
    OPENBLAS_NUM_THREADS=1 python3 -I -m pytest scratch/studies/lead-192 -q -p no:cacheprovider
