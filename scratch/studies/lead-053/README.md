# LEAD-053: the dependence rule for a capacity's constraint set, tested

`maintenance_rule.py` states the dependence rule for choosing the constraint
set K of a regulatory capacity, and applies it to the record's cases:

- CASE-036 (Northstar), as a finite toy stipulated for this test, with a
  discrete viability kernel; a control variant in which the emergency does
  not defer maintenance; and the stipulated-K rival (the organization's own
  standard, CLAIM-195's route carried to an agent).
- CASE-111 (fold in boundary maintenance): the kernel of K = {b >= b_f}.
- CASE-112 (tilted bistability): the structural level mu_c past which a
  bounded higher-order volition can no longer switch regime.
- CASE-227 (a mode kept by a decaying capacity): K = (1/2, inf) against the
  kernel [0.642, inf), and the effect of an outside supply.

Rerun, from this directory:

    python3 -I maintenance_rule.py > results.txt
    python3 -m pytest -q -p no:cacheprovider test_maintenance_rule.py

`results.txt` is the output of the first command. CPU only, under a second.
