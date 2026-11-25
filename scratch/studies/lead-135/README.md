# LEAD-135 — individuation by probing at rising budgets

Operationalizes CASE-202's "individuation-by-probing component" on
CLAIM-583's seed pair. Advances QUESTION-382, CLAIM-583, CLAIM-322.

## What it does

`prober.py` models a resource-bounded constraint system (TERM-114) as a
finite transition system: an admissible set of n-bit configurations, a fixed
single-flip move rule that stays inside the admissible set, named demands
(config = target), and a probe budget b = the number of moves a probe may
attempt. The probe readout at budget b is the reachability-between-demands
relation (from a config meeting D_i, which demands are reachable within b
moves); at b=0 this is the static family "which demands does a config meet".
The verdict on a pair at budget b is whether the readouts differ. The run
records the least budget at which the verdict stabilizes and whether the
pair ever diverges.

Control (CASE-202): each probe is run on a reset copy and an acted-on copy;
the prober is non-destructive, so the two readouts coincide and any
difference is discovered, not created.

## Results (results.jsonl)

- **seed** (CLAIM-583: A={000,111}, B={000,001}): same compatibility complex,
  same move rule, same costs; indistinguishable at budget 0 (static), diverge
  at budget 1, verdict stabilizes at budget 1. Finite stabilization budget.
- **identical** (B vs B): never distinguishable — control for artefacts.
- **path_L2..L5**: a constructed family with distinguishing budget = path
  length L, so the stabilization budget is a measured quantity, tunable to
  any finite value, not fixed at 1.

All pairs: same_complex=True, control_reset_equals_acted=True, distinction
monotone in budget (CLAIM-574).

## Rerun

    cd scratch/studies/lead-135
    python3 -I prober.py            # writes results.jsonl, prints a summary
    python3 -I -m pytest -q         # 14 tests

Pure numpy, CPU, single BLAS thread, sub-second. No network, no downloads.
