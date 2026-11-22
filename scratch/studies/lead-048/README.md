# LEAD-048: CASE-186's organization, simulated

A simulation of the organization CASE-186 designs: a hidden regime that
reverses (+ to −) and then either reverses back (in-family) or leaves the
hypothesis family (to 0); an audit apparatus whose **generate**, **admit**
and **score** operations are lesionable one at a time; diagnostic integrity
A and evidence-governance integrity G maintained reciprocally, by a paid
external service, or not at all; finite fuel; a teacher and an erased,
reconstructed student; a self-check of the apparatus on known inputs.

- `model.py`: the model, documented in its docstring. Reusable: import
  `Config`, `Org`, `run`; subclass `Org` to change one mechanism (LEAD-140).
- `test_model.py`: `python3 -I -m pytest -q test_model.py`.
- `study.py`: the driver. `python3 -I study.py core1` (reference apparatus,
  protected admission and independent scoring, every other factor),
  `core2` (the other admission × scoring arms, ample fuel), `core3` (those
  arms under lean fuel), `baselines` (no audit). One JSON line per cell
  (64 seeds) is appended to `results/<part>.jsonl`; a rerun skips cells
  already written.
- `analyze.py`: tables from the results.

Factors: maintenance (reciprocal, external, none) × admission (protected,
selective) × scoring (independent, captured, ipw) × second change
(in-family, out-of-family) × injury branch (sham, generate, admit, score,
A_partial, G_partial, producer_interrupt, internal_producer, double) ×
natural or matched first stage × self-check on or off × fuel (ample
ρ = 0.6, lean ρ = 0.36).

Schedule: + until t = 100, − from 100; S1 judged at 249; injury at 300;
second change at 400; S2 judged at 699.

Endpoints per cell: S1, S2, S1 ∧ S2 (counts of 64), S2's parts (correct,
viable, within budget), detection, median detection delay, false belief
changes, regret, fuel, final A and G, and for component lesions whether the
apparatus flagged itself before acting on its output.
