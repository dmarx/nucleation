# LEAD-173: the five conditions in a linear Gaussian VAR

Exact (covariance-level, no sampling) computation of the five conditions of
QUESTION-252 for linear coarse-grainings of stable linear Gaussian VAR(1)
and VAR(2) models, with constructions for every configuration the proved
entailments allow, and a random search for counterexamples to them.

- `fivecond.py`: the declared regime and the defects of P, D, M, A, C.
- `witnesses.py`: the constructions, one per configuration of (P, D, M, A);
  `pad` appends independent AR(1) coordinates to Y, which leaves P, D, M, A
  unchanged and switches C off.
- `run.py`: evaluates the witnesses, checks the realized set equals the set
  the entailments allow in each regime, derives the pairwise and
  leave-one-out tables, and runs 3,000 random sparse models per class.
- `test_fivecond.py`: pytest checks (CLAIM-389's 0.1200 nats, the AR(2)
  memory 0.147 and 0.0315, Kalman versus finite-lag transfer entropy, the two
  memory criteria, the witnesses' cells, the target-is-Y collapse).
- `results.json`, `results.md`: the output.

Rerun (CPU, about 40 s, then 2 s for the tests):

    cd scratch/studies/lead-173
    python3 -I run.py
    python3 -I -m pytest -q test_fivecond.py -p no:cacheprovider
