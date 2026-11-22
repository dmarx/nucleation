# LEAD-077: CASE-158's denoisers against a matched router, one arm per failure

The study behind the CASE filed for LEAD-077. CASE-158's design, built in
numpy: specialist denoisers with frozen low-rank operators propose for one
shared latent at each of five scheduler steps; an allocation combines their
proposals per region; the content each region needs changes halfway through
(episode 42 of 84). Held-out truth scores every arm.

## Model (`model.py`)

- **Content**: 4 types, each a rank-4 Gaussian in a 16-dimensional patch;
  4 regions; region r holds type r, then type r+1 after the reversal.
- **Specialists**: specialist k's operator is the rank-4 eigenbasis of type
  k's training covariance with Wiener shrinkage, fitted beforehand and
  frozen (except in the training arm).
- **Chain**: noise σ = 1 → 0.1 in five deterministic (DDIM-like) steps;
  at each step every specialist proposes and the allocation combines.
- **Audits**: 8 probes per region per episode, held-out patches with known
  injected noise at a random σ of the schedule; a probe's record is each
  specialist's one-step squared error. Audits of episode e are usable from
  episode e+1 only, by governance and router alike, and both consume the
  same number of probes (same audit cost: 8 × 4 × 84 = 2688 per run).
- **Allocators**: fixed (uniform); oracle (the right specialist per region,
  a floor); governance (EMA, α = 0.3, of audited competence per region and
  specialist; grants move with inertia η = 0.3 toward softmax of minus
  competence at temperature τ); conformity (the same update, scored by each
  proposal's distance from the episode's own combined proposal, no audit);
  router (per-specialist linear score predictor on region id, each
  specialist's captured energy of the noisy patch, their products and σ²,
  refitted by ridge with forgetting 0.7 per episode on the same audit
  records; gate softmax of minus predicted score at the same τ, per item and
  step).

## Arms (`study.py`), each applied to governance and router alike

| arm | failure (QUESTION-271) | what changes |
|---|---|---|
| full | none | every proposal probed, independent probes |
| bandit | 4, bandit feedback | each probe audits one specialist, drawn from the allocator's own allocation; `_explore` variants put a 10% floor on auditing |
| capture50, capture80 | 3, capture | that share of probe slots is chosen by the region's incumbent (the allocator's own top specialist) from 16 candidates, as the one most favourable to it, and entered twice |
| scale | 2, no common scale | specialist k's score is reported as a_k · mse^γ_k (a = 0.1, 0.46, 2.15, 10; γ = 1, 0.5, 2, 1); governance scores each member against its own history (standardized); controls: `governance_raw`, and `router_std` given the same standardization |
| cycles | 1, cycles | 3 specialists, each strong on one subtype and weak on the next; regions mix subtypes 0.4/0.3/0.3, so pairwise wins cycle (checked in the tests); audits are duels between two random specialists, win or loss only |
| full_rr | none (check) | the full arm again, adding `router_region`, a router that sees only the region id and σ, as governance's grants do |
| training | entrenchment loop | after each episode each specialist's covariance moves (rate 0.1) toward the content of the regions it was granted, in proportion to the grant, and its operator is refitted |

The gate temperature τ ∈ {0.03, 0.1, 0.3} is swept for both, and
`analyze.py` also compares each at the τ it does best at before the
reversal. 12 paired seeds per (arm, τ).

## Rerun

    python3 -I study.py        # appends to results/runs.jsonl, resumes
    python3 -I analyze.py      # writes results/summary.md
    python3 -m pytest -q test_model.py

The whole grid (8 arms × 3 τ × 12 seeds) took about 20 minutes on a loaded machine. `full_rr` was added after the first seven arms had run, to test where governance's steady-state edge over the contextual router came from.
