# LEAD-016 progress

Lead: LEAD-016. Branch: claude/lead-016-adaptive-operators.

Task as understood: run CASE-117's population of identically parameterized
adaptive operators in numpy, with ordinary mixture-of-experts routing as the
baseline. Within it, run QUESTION-134's experiment separating loss of
influence, of competence and of access (coupled against decoupled training
exposure). The decisive comparison: final participation roughly matched,
mechanism varied (fixed usage balancing against endogenous recovery
feedback); measure recovery when rare (from a small positive start, no
further intervention, parameters frozen and trainable) and refill after
removal of a specialist. Scoped to about an hour of CPU; core arms first.
File a CASE (executed-study), a CLAIM if warranted, dated notes on the
entries LEAD-016 advances, on CASE-117 and on LEAD-016.

## Choices made

- Model (opmodel.py): C = 4 contexts (p = .33, .33, .32, .02; context 3
  rare), linear targets with orthonormal coefficient vectors, K linear
  operators (fixed features), context-conditioned influence shares.
  K = 4 (no spare operator) and K = 6 (two spare).
- Influence rules: moe (Jacobs-style softmax gate, baseline), moe_aux
  (+ load-balancing loss, imposed in the gradient), moe_bias (+ usage bias,
  imposed outside the gradient, after auxiliary-loss-free balancing),
  rep (multiplicative contribution: collective loss minus own loss),
  uniform (reference, differentiation only).
- Held-out competence is analytic risk on the generating distribution,
  independent of every sample the loop saw.
- Decoupled exposure (QUESTION-134's control) applies to the suppressed
  specialist only, in its own context, fixed at its pre-suppression share.
- Weight decay (1e-4 per step) as the maintenance cost, applied only in the
  test window; wd = 0 arms as the contrast.
- Not attempted (scope): learned features, historical-grant influence,
  revisable authority-update rule, abrupt shifts, internally maintained
  exploration.

## Done

- opmodel.py, test_opmodel.py (12 tests passing).
- Pilot: every rule but uniform differentiates in 40,000 steps, with a
  distinct specialist for the rare context, ~4-5 s per run.
- study.py written (resumable JSONL per rule).

- Smoke test (1 seed) passed; fixed the R-sample offset in the release
  window, and made the sham an operator as incompetent in R as the
  residents (a copy of context 0's specialist); added a frozen-at-release
  suppression arm.
- Main run launched 2026-11-22: 12 seeds x {moe, moe_aux, moe_bias, rep}
  (+ uniform), four processes, estimate 20 min, limit 60 min. Results
  append to results/runs_<rule>.jsonl; rerun `python3 -I study.py RULE 12`
  resumes.

- The machine is shared with other workers (load ~14 on 4 cores), so the
  pace was ~4x slower than the smoke test. Restructured at 13:12: seeds
  cut from 12 to 6 (resume keeps finished items), single-threaded BLAS,
  time limit 60 min against an estimate of ~35 min.
- analyze.py and README.md written. First seeds show: (K = 4, matched
  participation) a rare specialist's recovery rate scales with its share
  under softmax-gradient routing (moe, moe_aux) and does not under rep;
  (K = 6) a spare refills a removed or suppressed specialist's niche and
  the returning specialist is then pre-empted even with its competence
  intact.

## Next

- When the run finishes (6 seeds per rule): run analyze.py, commit
  results/summary.md, then file the CASE (CASE-tmpnti0m created by
  `luria new case`, template not yet replaced), the CLAIM, dated notes and
  the changelog fragment.
