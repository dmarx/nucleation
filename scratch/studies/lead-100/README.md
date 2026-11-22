# LEAD-100: numerical checks of the receiver-restricted order

- `rorder.py`: finite experiments, receiver classes given by the vertices of
  their rule hulls, usable risk, the achievable-set (Ach) criterion by LP,
  the test for a garbling the class respects, factoring receivers.
- `test_rorder.py`: pytest sanity tests.
- `run_checks.py`: the examples (E1 CLAIM-199's XOR on a common medium, E2
  a strict reversal of Blackwell's order) and random checks (T1 Ach
  criterion and prior independence, T2 the respected-garbling theorem,
  T3 the ceiling, T4 factoring receivers inherit the finite converse).
  Writes `results.json`; about 25 s on one thread.

Rerun from this directory:

    OMP_NUM_THREADS=1 python3 -I -m pytest -q test_rorder.py
    OMP_NUM_THREADS=1 python3 -I run_checks.py
