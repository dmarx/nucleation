# LEAD-077 progress

- Lead: LEAD-077
- Branch: claude/lead-077-denoisers-router
- Task: build CASE-158's design in numpy (frozen low-rank specialist
  denoisers proposing for one shared latent per step, spatial grants), with
  audited governance against a contextual router matched on audit delay
  (next episode only) and audit cost; fixed and conformity arms; then one
  arm per QUESTION-271 failure (cycles, no common scale, capture, bandit
  feedback) plus a continued-training arm. Scoped to about an hour of CPU,
  core arms first. File a CASE (executed-study), a CLAIM if warranted,
  dated notes on CASE-158, QUESTION-271, the entries LEAD-077 advances, and
  LEAD-077.

## Done

- Read the lead, CASE-158, QUESTION-271, CLAIM-467 and the other advanced
  entries' summaries; docs/record.md's CASE fields.
- model.py, study.py, analyze.py, test_model.py (9 tests pass), README.md.
- Grid launched 13:02 UTC: 7 arms x 3 gate temperatures x 12 seeds, one
  JSONL line per (arm, tau, seed) in results/runs.jsonl; resumable.

- Grid complete: 288 items (8 arms x 3 tau x 12 seeds), results/runs.jsonl
  (curves stripped to stay under 1 MB), results/summary.md. Two runs were
  killed by a signal from outside (exit 144) and resumed from the file.

## Headline

- Full information: governance beats the contextual router at tau 0.03 and
  0.1 (12/12, 11/12) but loses at tau 0.3 (1/12), the best pre-reversal tau
  for both; a router seeing only the region id beats governance 0/12 at
  every tau. Governance's edge was the contextual router's noisy per-item
  gate, not anything governance uses.
- Cycles: router 12/12 (per-item routing). Capture 80%: router 12/12 at
  every tau. Scale: governance (self-standardized) beats a raw router 12/12
  but ties a router given the same standardization (6/12). Bandit: naive
  governance loses; with a 10% audit floor at tau 0.3 it beats the router
  with the same floor 12/12, but not the router without one. Training: as
  full, no entrenchment of either.

## Choices made

- Router = per-specialist linear score predictor (ridge, forgetting 0.7) on
  region id + each specialist's captured energy of the noisy patch; gate
  softmax(-predicted score). Same audit records, same delay (next episode),
  same probe count (cost) as governance.
- Gate temperature swept for both (0.03, 0.1, 0.3) so neither is compared
  at a setting tuned for the other; also each at its best pre-reversal tau.
- Cycles arm: duel-only audits on an environment whose pairwise wins cycle
  (tested). Scale arm: governance standardizes each member against its own
  history; controls governance_raw and router_std. Bandit: one specialist
  audited per probe, drawn from the allocator's own allocation; _explore
  variants with a 10% audit floor. Capture: 50% and 80% of probe slots
  curated by the incumbent (filtered from 16, entered twice).
- Not run: CASE-158's grant-reset counterfactual (out of the core arms).

## Next

- File CASE (executed-study), CLAIM if warranted, dated notes on CASE-158,
  QUESTION-271, CLAIM-467, QUESTION-264, QUESTION-089, CLAIM-277, CLAIM-342,
  CLAIM-286, LEAD-077; changelog fragment.
