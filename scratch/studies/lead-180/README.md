# LEAD-180: CASE-108's four governance architectures, simulated

A federated multitask learner with cooperative, honestly dissenting and
adversarial specialists, aggregated under unrestricted, reliability-weighted,
role-limited and adaptive governance, against an oracle, with variants that
compromise the evaluators and the monitor. See `record/changelog.d/lead-180.md`
for the codes filed.

## Rerun

    cd scratch/studies/lead-180
    export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
    python3 -I -m pytest -q -p no:cacheprovider --rootdir=. test_model.py   # 19 tests, < 1 s
    python3 -I run.py            # e1..e5, about 4 min on one thread
    python3 -I run.py e2 e3      # or some of them

Each experiment writes `results/<name>.json`; `results/tables.md` is rebuilt
from them. 30 seeds per cell; ± is a 95% half-width.

## Model

The docstring of `model.py` is the specification. In short: θ ∈ R^12, a main
block M (8 dims, every specialist's data covers it) and a minority block m
(4 dims). 14 cooperatives (right on M; on m their data has no examples and
they pull it toward 0), 3 honest dissenters (right on both), 3 adversaries
(cooperative for 100 rounds, then pushing the attacked block toward
θ* + 3u with 3× boost; `overt` attacks M, `mimic` attacks m, looking like
dissent). Evaluators: a pool of 7 with their own noisy validation estimate
(σ_v = 0.3); all cover M, 2 cover m. A compromised evaluator approves the
adversaries, rejects the dissenters and judges cooperatives honestly.

- `unrestricted`: mean of all updates.
- `rel-agree`: reputation from cosine agreement with the aggregate; softmax weights.
- `rel-val`: reputation from the pool's validation (prior 0 off coverage).
- `role`: a random panel of 3 evaluators votes per block, abstaining off its
  coverage; quorum 2/3 of the jurisdiction holders; approved updates
  clipped to their median norm and averaged.
- `adaptive`: `role` plus, every 20 rounds, a monitor (an auditor with its
  own validation estimate) that suspends proposers whose approved updates
  it scores below −0.2 for 60 rounds, raises a block's quorum when that
  block's loss rose, and stratifies the panel to include a jurisdiction
  holder for a starved block.
- `oracle`: `role` with one evaluator holding θ* exactly.

## Experiments

- e1: architectures × attack (none, overt, mimic) × compromised evaluators (0, 2 of 7).
- e2: role-limited and adaptive audit, central evaluator against the pool,
  panel 3 or 7, quorum 1/2 or 2/3, 0–3 compromised.
- e3: coverage of m by independent evidence (0–3 evaluators), mimic attack;
  and the relabelling check (dissenters' and mimics' targets swapped,
  boost 1, no farming): attack success in a world and its relabelling sums
  to 1 for every architecture when nobody holds evidence on m.
- e4: repair: role against adaptive with an honest or a compromised
  monitor; peak attack success, recovery, suspensions by type.
- e5: farming (attack from round 0 or after 100 cooperative rounds).
