# LEAD-076: frustration against thwarting, and CASE-153's sentry

Two parts, numpy only, CPU, a few minutes in all.

- `frustration.py`: finite constructions that separate structural
  frustration (CLAIM-347) from operative thwarting, with thwarting tested by
  counterfactual silencing of a process. `python3 -I frustration.py` prints
  `constructions.md`.
- `sentry.py`: CASE-153's self-protecting sentry with a hidden world state,
  a sentry that can block inspection, governance feedback, evidence
  restriction and correction rights, and Bayesian and habit baselines.
- `run_sentry.py`: the first experiment, the factorial (with a fixed-authority
  level and habit rows), CLAIM-446's four interventions, a phase diagram over
  the sentry's strength kappa and the authority learning rate eta, and
  sensitivity to the assumed hazard h, to authority fixed at a trained level
  and to a second seed set. Writes `results/*.jsonl` one line per condition
  and skips lines already written, so a stopped run resumes.
- `analyze.py`: writes `results/summary.md` from the JSON lines.
- `test_frustration.py`, `test_sentry.py`: pytest.

Rerun:

    cd scratch/studies/lead-076
    export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
    python3 -I -m pytest -q
    python3 -I frustration.py > constructions.md
    rm -f results/*.jsonl && python3 -I run_sentry.py && python3 -I analyze.py

Parameters are in `sentry.Params` and `results/params.json`: 150 steps of
danger, 400 safe, 100 of danger again; inspection accuracy 0.9 at cost 0.05;
protection costs 1 a step, engaging in danger 5; assumed hazard 0.02;
kappa 1.5 (posture bias kappa, inspection block 0.2 kappa in value units);
eta 0.02; audit rate 0.2; protected investigator's floor 0.2; 1000 seeds
with common random numbers (seed 20261122). The parameter values are the
assistant's choices, not estimates of anything.

Choices the case left open, made here:

- Reward structure. CASE-153 names two actions, shelter and inspect. A
  second decision, posture (protect or engage), carries the costs, so that
  needless protection has a price and the sentry's authority can act on
  action as well as on evidence (CLAIM-446's "authority over action,
  attention and evidence acquisition").
- Value of inspection. Myopic: the expected reduction in the next posture
  loss. It is zero when the belief is extreme, so even the Bayesian
  inspects rarely in steady danger.
- Independent feedback. The evaluator's belief in danger from the evidence
  it receives. Without an audit that is the agent's own evidence, which is
  what lets the sentry's block on inspection reach the evaluation.
- Success feedback. 1 when the agent protected or was harmed, 0 when it
  engaged safely. Without harm events, this is the habit trace of
  protecting; see the CASE.
- Correction rights. Run at two levels, an audit reaching the evaluator and
  a protected investigator, giving a 3 x 2 x 3 design with fixed authority
  as a third feedback level.
- Measures. Recognition: the belief first below the posture threshold
  1/5. Exit: the first step from which P(protect) averages below 0.5 over
  20 steps.
