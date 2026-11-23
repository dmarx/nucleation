# LEAD-005 progress

- Lead: LEAD-005 (reproduce a known no-feedback thermodynamics-of-prediction
  result, as the first milestone toward QUESTION-494)
- Branch: `claude/lead-005-thermo-prediction`, cut from `origin/staging`
- Task as understood: check whether the result is already held; if not,
  reproduce Still, Sivak, Bell & Crooks 2012 (arXiv 1203.3271) numerically in
  a small driven Markov system (numpy, pytest), then use the reproduction for
  what the lead's body asks (add feedback, compare memories keeping the
  predictive partition, the interventional partition, or neither), and file
  a CASE, CLAIMs, dated notes and a changelog fragment.

## Done

- Step 1, held check (2026-11-23). The reading is held: LIT-327 (Active),
  NOTE-295 (read in full from arXiv v3), THEORY-026 (Active). THEORY-026's
  note of 2026-10-19, step 4, reports a one-off numerical check (4 states,
  3 symbols, six steps) with no code and no CASE. No changelog fragment,
  CASE or claim holds a reproduction, and nothing holds the lead's feedback
  half. Choice: file no second LIT, NOTE or THEORY (ADR-072); file the
  reproduction and the feedback comparison as an executed-study CASE with
  claims. Alternative: treat the held check as the reproduction and file only
  dated notes (see the report).
- The paper's text re-checked from arXiv v3 (scratchpad, not committed) for
  the indices and for Eq. 9-10 vs Eq. 13: two readings of W_diss, both computed.
- Code: still2012.py, feedback_toy.py, run_study.py, test_lead005.py (15 pass),
  results/summary.md. Runs in about 30 s.

## Results in brief

- No feedback, 300 random systems: Eqs. 14, 17, 19 hold to 3e-15; Eqs. 16, 18,
  21 hold in all; per-step nostalgia never negative; the per-protocol reading
  also satisfies the bound; Monte Carlo agrees (20 of 20).
- Feedback, 500 random systems: identities and Eq. 18 still hold in all; a
  step's nostalgia is negative in 405, the summed nostalgia in 323, and
  W_diss and W_ex in 6 (min W_ex -0.29 k_BT).
- Toy: predictive partition {v} (random actions, or own loop) or {u,v}
  (fixed action); interventional {u} (outcome) or {u,v} (whole percept).
  Keeping only u is the cheapest memory that does the task, by nostalgia,
  heat per step and overwrite entropy, in four parameter settings. The policy
  changes the memory's nostalgia (ln 2 vs 0) but not its heat per step.

## Next

- File the CASE and CLAIMs; dated notes on LEAD-005, QUESTION-494,
  THEORY-026, CLAIM-tmpcbdgm; changelog fragment.
