# LEAD-142 study: the decision signature for the directed case

Operator `T: L2(P_A) -> L2(P_X)`, `(Tg)(x) = E[g(A)|X=x]`, for a joint law
`P+(x,a)`. The candidate directed signature (QUESTION-052) is the top-d **left**
singular space `span{mu_1..mu_d}` of `T`.

## Run

    cd scratch/studies/lead-142
    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 \
      NUMEXPR_NUM_THREADS=1 python3 -I directed_signature.py   # writes results.json
    OMP_NUM_THREADS=1 ... python3 -I -m pytest -q               # 7 tests

Runs in well under a second (3x3 and 4x4 matrices).

## What each check shows

- **A, reduction.** `span{mu_1..mu_d}` is exactly the top-d eigenspace of the
  self-adjoint two-step chain `M = T T*` (`x -> a -> x'`), and `M` is reversible
  w.r.t. `P_X`. `M mu_i = s_i^2 mu_i` to 1e-15. So for decisions that are
  functions of x, the directed case is a symmetric case with operator `M`;
  directedness adds no new obstruction for x-decisions.
- **B, THEORY-239 reproduction.** The non-reversible three-state chain:
  `pi=(0.287,0.338,0.374)`, singular values `(1,0.655,0.534)`,
  `mu2 ∝ (-1.30,1.22,-0.11)` (matches THEORY-239), left != right singular
  functions. The compatible-target worst-case tie: `r*=0.7708`, and
  `span{mu1, cos th mu2 + sin th mu4}` ties at r* for th=0.05,0.2,0.5, rising
  to 0.973 at th=1 -- spans tie even with a spectral gap.
- **C, beyond linear probes.** Product chain (rho_a=0.9, rho_b=0.8). The
  interaction `chi_a*chi_b` is a stable target (stability 0.518) with linear
  residual 1.0 on the top-2 span but nonlinear residual 0 (a product readout
  of the top-2 encoder). And target `chi_b` (stability 0.64) has residual 1.0
  from the top-1 encoder `chi_a` yet 0 from the competitor encoder `chi_b`:
  sufficiency is decision-relative.
- **D, direction obstruction.** The left signature is a function of x only. The
  order decision `sign(x-a)` has residual 0.2245 (of variance 0.824) from any
  function of x, and 0 from the ordered pair. Direction-dependent decisions are
  unserved by the left signature at any d.

Results in `results.json`.
