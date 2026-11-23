# LEAD-011: constructions for a scalar optimum of learning

Three small checks of the arithmetic in the claims filed by the lead run of
2026-11-23. The claims are demonstrated by the arguments in their bodies;
these files only guard the numbers.

- `constructions.py`: the three constructions.
  1. Endogenous tasks: three learner organizations, each changing the chance
     that the next task is hard; learning costs a period. Backward induction
     over a horizon of 6 gives 12.3 from the novice state, and enumerating all
     4096 deterministic Markov policies finds the same value attained: learn
     twice, then work. A declared state-dependent task kernel leaves a
     scalar optimum in place.
  2. Valuation that moves with learning: two policies whose produced selves
     each endorse their own (both self-ratifying; the ex post ranking flips
     under a rescaling each self's preferences admit), and three policies
     each regretted by the self it produces (none self-ratifying). The ex
     ante valuation gives an optimum, unchanged whatever the learned self
     values.
  3. Learnability growing faster than discounting: investing n periods then
     exploiting is worth (gamma g)^n r / (1 - gamma); with gamma g > 1 each n
     is beaten by n + 1 and never exploiting is worth 0. A bounded version,
     1 - 2^-n, has a finite supremum that no policy attains. A finite
     horizon restores an optimum.
- `test_constructions.py`: 21 tests.

Rerun, from the repository root:

    python3 -I -m pytest -q -p no:cacheprovider scratch/studies/lead-011
    python3 -I scratch/studies/lead-011/constructions.py

Needs numpy and pytest; runs in under a second.
