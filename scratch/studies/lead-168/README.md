# LEAD-168: an executive, a reviewer and an enforcer in two arrangements

QUESTION-278's minimal construction (A9): arrangement I, in which the
enforcer executes a corrective order whenever it is able, and arrangement C,
in which it executes only if the executive's signal permits. Every other rule
is shared. `model.py` states both; `study.py` finds where their observable
traces (action, challenge, ruling, enforcement, outcome; E's signal is not
observed) first part, under three readings:

- A. fixed policies, every probe enumerated (32 probes);
- B. conditioning as a hold of d steps against a deadline;
- C. anticipation: backward induction over a payoff grid, with the reviewer
  and then also the executive anticipating enforcement;
- D. what a non-execution shows in C: P(E withheld | not executed);
- E. structural: does F's act change under an intervention on E's signal.

Rerun (seconds, CPU, no randomness):

    cd scratch/studies/lead-168
    OPENBLAS_NUM_THREADS=1 python3 -I -m pytest -q test_model.py
    OPENBLAS_NUM_THREADS=1 python3 -I study.py

Writes `results.json` and `results.md`.
