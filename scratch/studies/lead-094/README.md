# LEAD-094 study files

- `oa_invariance.py`: checks whether Ott and Antonsen's family F_n = alpha^n
  stays invariant under the continuity equation of globally coupled phase
  oscillators, with first-harmonic coupling only and with a second harmonic
  added. Result in `oa_invariance_result.txt`: defect about 1e-16 for the
  first harmonic alone; about 0.1 with a second harmonic, except at
  |alpha| = 1 (full locking), where it vanishes.
- `test_oa_invariance.py`: pytest for the check.
- `PROGRESS.md`: the lead's progress.

Rerun from this directory:

    python3 oa_invariance.py
    python3 -m pytest -q test_oa_invariance.py

CPU only, under a second. No downloaded text is committed here.
