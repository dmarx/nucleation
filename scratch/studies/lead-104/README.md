# LEAD-104: the competence-restriction loop

The model named by CLAIM-721: CLAIM-605's model
(`scratch/formal/capability_trap_toy.py`) with **reinstatement made a
threshold on capacity**. Instead of outside support doing the work, a
*restriction* removes the doing; the restriction lifts (one-way) when
capacity C reaches a reinstatement threshold C_r.

- `restriction_trap.py` -- the model and its demonstration; asserts every
  number. Run: `OMP_NUM_THREADS=1 python3 -I restriction_trap.py`.
- `test_restriction_trap.py` -- independent pytest re-deriving the facts.
  Run: `OMP_NUM_THREADS=1 python3 -I -m pytest test_restriction_trap.py -q`.

Parameters (CLAIM-605's, unchanged): lam=1, mu=0.3, tau=1.5; reinstatement
threshold C_r=0.6, party restricted at C0=0.5 (< C_r). Results: the bare
restriction is a self-perpetuating trap (C never rises to C_r); a
recoverability deadline t_dead=1.98; the route decides -- a practice route
needs rho>=0.8 and cannot ignite from below, a training route (direct
capacity) ignites from zero once g>=g_crit=mu*C_r=0.18; each of CLAIM-721's
three conditions is necessary.
