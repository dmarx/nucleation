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

## Next

- Write sim.py and test_sim.py; run; write README and results.
- File CASE, CLAIM (if warranted), notes, changelog fragment.
