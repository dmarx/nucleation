# LEAD-080: the readiness simulator under spend-matching and carry-over

The simulator QUESTION-394 records from A's proposal, run under CLAIM-577's
budget rule and under carry-over (2026-11-22). Filed as CASE-tmpvnozj, with
CLAIM-tmpocsw4 (temporary codes as filed).

- `sim.py`: the simulator, the budget rules, the summary measures and the
  run grid. The model is stated in its docstring.
- `test_sim.py`: 13 tests: the budget rules on CASE-200's numbers; CLAIM-577's
  steps 1 and 3 (the budget never rises; one quiet month forecloses, for
  good); full carry-over holding the budget; CASE-200's rule skipping a
  month after use; CASE-213's timing (max(A, T) against A + T); a cancelled
  dispatch counting as peak spending; the skill half-life; the loss
  probability 1 − (1 − e^(−λ))^n against 2,000 runs; CASE-200's recursion
  over several periods.
- `results.txt`, `results.json`: 65 configurations, 300 seeds each, 120
  months each.

Rerun from the repository root (CPU, about 30 seconds):

    python3 -I scratch/studies/lead-080/sim.py scratch/studies/lead-080/results.json > scratch/studies/lead-080/results.txt
    python3 -I -m pytest -q -p no:cacheprovider scratch/studies/lead-080

Seeds: run i of a configuration uses `numpy.random.default_rng([20261122, i])`,
so every configuration sees the same call histories for the same λ.

## Choices left open, made before running

- **Capacity and spending.** CLAIM-577's capacity resource: r = 0.7 holding
  (engine on duty, squad kept in quarters) plus 0.6 for each squad mobilized
  (dispatched and not back, or drilling). One squad out costs 1.3, the
  claim's worked numbers. Spending s_t is the month's peak of r, so a
  cancelled provisional dispatch spends 1.3 for the month as much as a full
  rescue does. A mobilization is refused when it would exceed B_t.
- **Period**: a month; horizon 120 months; B_0 = 1.3 (one squad), k_0 = 1.
- **The two regimes.** Spend-matching, B_{t+1} = s_t. Carry-over is run two
  ways, since the lead does not say which: the peak rule with the unspent
  part rolled over, B_{t+1} = s_t + ρ(B_t − s_t) (ρ = 1 holds B at 1.3, and
  serves as the control; ρ = 0.6 is partial), and CASE-200's recursion,
  B_{t+1} = B̄ + ρ(B_t − s_t) with B̄ = 1.0, α = 0, ρ = 1 and 0.6,
  uncapped. CASE-200's is the record's own carry-over rule; the peak-plus-
  rollover rule is the nearest variant of CLAIM-577's.
- **Incidents**: reported collisions, Poisson, λ = 2 or 6 a month; a share
  p = 0.1 need extrication (the two incident types). Assessment accuracy
  0.9 (sensitivity = specificity).
- **Geography**: engine distance U(0.3, 3) km, A = 1 + d/0.7 + 2 minutes
  (turnout, travel, assessment); squad distance U(1, 14) km, T = 1.5 + d/0.8.
  Mutual aid, the substitute, is 12 km farther, qualified, and outside the
  budget.
- **Deadline**: a qualified responder on scene within 20 minutes of the
  call. A missed need (assessment wrong) is recognized 10 minutes after
  the assessment.
- **Policies**: provisional dispatch with cancellation (CASE-213: the squad
  goes at once and is cancelled at A if the engine reports no need, unless
  it is on scene first and sees for itself) and dispatch after
  confirmation. QUESTION-394's other two policies are not run: the lead
  asks about the budget, not the policy ranking.
- **Skill**: k ← min(1, 0.91 k + 0.3 × (drills + extrications)) a month;
  qualified when k ≥ 0.5 (half lost in about 7.4 months, CLAIM-558).
  Drills every 1 or 3 months or never, four hours, at the start of the
  month, subject to the budget like any mobilization.
- **Costs** (CLAIM-561's example): H = 10 a need not met in time, c0 = 1 an
  unneeded dispatch, c1 = 0.5 a needed one. At p = 0.1 provisional dispatch
  is below CLAIM-561's threshold (0.143), so it costs more here; the cost
  column is reported, not optimized.
- **Lost for good**: the budget stays below 1.3 from some month to the end,
  for at least 12 months.

Rates, distances and costs are invented to show mechanisms; none is a
measurement.

## Columns of results.txt

lost: share of runs lost for good; lost-month IQR: 25th, 50th, 75th
percentile month of loss; reach: share of months with B ≥ 1.3; P(met):
share of true needs met by a timely qualified responder, mean and sd over
runs, over all ten years and over years 6 to 10; k_end: final skill;
cancel/mo; busy h/mo (squad); blocked: true needs the budget refused, per
run; cost/mo; mean B.
