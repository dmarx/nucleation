# LEAD-036 progress

- Lead: LEAD-036 (Model or trace the loop by which activity-based funding
  erodes rarely used capability, against a control that decouples
  maintenance funding from observed activity).
- Branch: claude/lead-036-funding-loop (cut from origin/staging).
- Task as understood: simulate QUESTION-386's loop (A's model,
  k_{t+1} = (1-δ)k_t + βm_t, B_{t+1} = B̄ + ηM_t, maintenance m drawn
  from the budget, observed activity M from rare contingencies, plus the
  coverage feedback: a weaker capability is committed less and so observed
  less), once coupled and once with maintenance funding decoupled from
  observed activity; numpy, pytest tests. File a CASE (executed-study), a
  CLAIM if warranted, dated notes on QUESTION-386 (advanced), CLAIM-577
  and LEAD-036.

## Step 1 check (is the target held?)

Not held. LEAD-080's CASE-tmpvnozj / CLAIM-tmpocsw4 ran CLAIM-577's
peak-capacity rule (B_{t+1} = s_t) against carry-over in A's readiness
simulator. That is the pure case the lead says to go beyond: it has no
budget-funded maintenance, no linear B̄ + ηM rule and no coverage
feedback. Its finding that funding and maintenance are separate conditions
is cited, not refiled.

## Done

- sim.py, test_sim.py (12 pass), README.md; grid run (80 configurations,
  2,000 runs each, under 10 s): results.jsonl, results.txt.

## Choices made

See README "Choices left open". Key: quarter periods; m = max(0, B - h);
commitment ramp 0.4..0.8; rarity swept at fixed eta*lam = 0.52; two
decoupled controls (full-use money, and the coupled rule's realized mean).

## Results in brief (B̄ = 1.2, k_base 0.25 < k_lo 0.4)

- coupled: absorbed in 100 % of runs at lam <= 0.1/quarter (median quarter
  19-25), 93 % at 0.25, 39 % at 1, 0.7 % at 4 (W = 1); W = 4 slightly less.
- decoupled_full: never; k = 0.9, met 0.90 at every lam.
- coupled_nocov: no absorption, but mean k 0.53-0.89, lower when rarer
  (lumpy budgets wasted at the cap).
- decoupled_equal: the coupled run's money, spread evenly, does not save it
  where that money sustains k < k_lo.
- B̄ = 1.35: no absorption, but at lam = 0.05 coupled holds k ~0.48 and
  meets 25 % against mean-field fixed point 1.0.

## Next

- File CASE (executed-study), CLAIM, notes on QUESTION-386, CLAIM-577,
  LEAD-036; changelog fragment.
