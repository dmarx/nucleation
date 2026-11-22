# LEAD-036: QUESTION-386's funding loop, coupled and decoupled

A's model from QUESTION-386, run with the three processes the question
names (funding feedback, competence decay, coverage feedback), once with the
budget tied to observed activity and once with maintenance funding
decoupled from it (2026-11-22). Filed as a CASE and a CLAIM (temporary codes
as filed; see the changelog fragment `record/changelog.d/lead-036.md`).

- `sim.py`: the model (stated in its docstring), the four budget rules, the
  mean-field fixed points, the summary measures and the run grid.
- `test_sim.py`: 12 tests: the commitment ramp; the steady competence under
  a fixed budget; the decoupled rule converging to it and ignoring
  occasions; A's budget rule with W = 1 and W = 4 recomputed from the
  record of commitments; the absorbing state (k < k_lo and k_base < k_lo:
  nothing committed, B = B̄ for good, k → k_base); no absorption when
  k_base > k_lo; the mean-field fixed points (three at B̄ = 1.2, one at
  1.35, one without coverage feedback); the mean budget without coverage
  feedback; common occasions across rules; the grid resuming.
- `results.jsonl` (one configuration a line, with its parameters),
  `results.txt` (the table).

Rerun from the repository root (CPU, under ten seconds):

    python3 -I scratch/studies/lead-036/sim.py scratch/studies/lead-036/results.jsonl > scratch/studies/lead-036/results.txt
    python3 -I -m pytest -q -p no:cacheprovider scratch/studies/lead-036

A rerun skips configurations already in `results.jsonl`; delete it to
recompute. Seeds: every configuration uses `numpy.random.default_rng([20261122, 1])`
for occasions and `[20261122, 2]` for commitment and success draws, so the
rules see the same occasions at the same λ.

## Choices left open, made before running

- **Period** a quarter; horizon 120 quarters (30 years); 2,000 runs a
  configuration; k_0 = 0.9; starting budget as if fully used.
- **Competence**: δ = 0.08 a quarter (half-life about two years), β = 0.1
  per unit of maintenance, capped at 1.
- **m from B**: everything above the fixed holding cost h = 1.0 goes to
  maintenance, m_t = max(0, B_t − h). QUESTION-386 says only that m is
  "funded from the current budget".
- **Base budget** B̄ = 1.2 (base alone sustains k_base = 0.25) and 1.35
  (k_base = 0.44), either side of the commitment threshold.
- **Coverage feedback**: commitment probability 0 below k_lo = 0.4, 1 above
  k_hi = 0.8, linear between. A committed capability meets the contingency
  with probability k.
- **Rarity at fixed money**: λ = 0.05, 0.1, 0.25, 1 and 4 occasions a
  quarter, with η = 0.52/λ, so a capability committed to every occasion is
  funded B̄ + 0.52 on average (k = 0.9 at B̄ = 1.2) whatever λ is.
- **Window**: the budget follows last quarter's activity (W = 1, A's rule)
  or the mean of the last four (W = 4).
- **Controls**: decoupled at what full use would earn on average
  (B = B̄ + 0.52, `decoupled_full`); decoupled at the coupled rule's
  realized mean budget in the same configuration (`decoupled_equal`, the
  same money, untied); and coupled without coverage feedback
  (`coupled_nocov`, an ablation).

Rates are invented to show mechanisms; none is a measurement.

## Columns of results.txt

lost: share of runs absorbed (coupled rule with k_base < k_lo only; k below
k_lo at the end, from which it cannot return); below: share with k < k_lo
at the end, any rule; lostQ: quartiles of the quarter it first fell below
k_lo, among the absorbed; k_end: mean final competence; met: share of
occasions met, over 30 years; met2: over the last 15; commit: share of
occasions committed to; B_mean: mean budget.
