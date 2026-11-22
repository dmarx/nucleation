# LEAD-095: committors with a withdrawable scaffold

Code for CASE-tmplsvee and CLAIM-tmp5hyz1 (temporary codes as filed on 2026-11-22).

- `committor_model.py`: the chain, the exact committor solver (linear solve), A's D(s) at every state in four mechanisms, the decomposition identity check, withdrawal at a clock time, and the state/rate factorial. The model is stated in its docstring.
- `sweep.py`: 2,000 random parameter sets (seed 20261122), giving how often D(1, n) rises or falls with n in each mechanism.
- `test_committor_model.py`: gambler's ruin (known answer), CLAIM-596's construction (0.8 and 17/30), Monte Carlo agreement, the identity, and the limits of timed withdrawal.

Rerun from the repository root (CPU, seconds):

    python3 -I scratch/studies/lead-095/committor_model.py scratch/studies/lead-095/results.json > scratch/studies/lead-095/results.txt
    python3 -I scratch/studies/lead-095/sweep.py scratch/studies/lead-095/sweep.json > scratch/studies/lead-095/sweep.txt
    python3 -I -m pytest -q -p no:cacheprovider scratch/studies/lead-095

Rates are invented to show mechanisms; none is a measurement.
