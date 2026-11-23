# LEAD-183: a non-monotone predictor of productive seed sets, tested out of sample

Read PREREGISTRATION.md first: the predictor, the system and the criterion
were fixed and committed before the test runs, and the two amendments say
what changed and why, each committed before the run it governs.

## Files

- `nucleus_predictor.py`: architectures, islands (static `island_ac`, forward
  `island_forward`), predictors (VIC, ICN, TFF and the monotone baselines
  count, UFI analogue, joint coverage), Gillespie dynamics, metrics, driver.
- `test_nucleus_predictor.py`: 13 pytest tests.
- `results.jsonl`, `summary.json`: the amended pre-registered test,
  architectures 0–4 (p_r = 0.5) and sensitivity 100 (0.4), 101 (0.6).
- `recheck_decreases.py`, `recheck.json`: post hoc, each significant decrease
  re-estimated with 3000 runs.
- `diagnose_seeds.py`, `diagnosis.json`: post hoc, per-seed mean effect
  against island size and edge strengths.
- `results_fresh.jsonl`, `summary_fresh.json`, `fresh_flags.txt`: the test of
  the post hoc predictor TFF on fresh architectures 200–204.

## Rerun

    python3 -m pytest -q test_nucleus_predictor.py
    python3 -I nucleus_predictor.py            # resumes from results.jsonl
    python3 -I recheck_decreases.py
    python3 -I diagnose_seeds.py
    python3 -I nucleus_predictor.py --fresh    # resumes from results_fresh.jsonl

Each takes under a few minutes on one CPU. Delete a results file to rerun
from scratch.

## Results

| test | predictor | M1 (Spearman with V) | M2 AUC | recall | precision | transfer |
|---|---|---|---|---|---|---|
| v1, as first registered | all island-based | constant (AC island = whole lattice) | — | — | — | void |
| amended, arch 0–4 | VIC | 0.22 | 0.70 | 0.25 (2/8) | 0.01 | no |
| amended, arch 0–4 | ICN | 0.52 | 0.88 | 0 | 0 | no |
| amended, arch 0–4 | best monotone (UFI analogue) | 0.54 | 0.88 | 0 | — | cannot flag |
| fresh, arch 200–204 | VIC | 0.21 | 0.84 | 0.58 | 0.09 | no (M1) |
| fresh, arch 200–204 | ICN | 0.48 | 0.77 | 0 | 0 | no |
| fresh, arch 200–204 | TFF (post hoc) | 0.64 | 0.94 | 0.66 | 0.11 | yes |
| fresh, arch 200–204 | best monotone (joint) | 0.48 | 0.77 | 0 | — | cannot flag |

- Harmful additions are real: 38 of the 40 significant decreases of the
  amended run (6 of 8 on architectures 0–4, 32 of 32 on the sensitivity
  architectures) are confirmed at z < −2 with 3000 runs, the sensitivity ones
  typically halving V (median −0.07, for example 0.15 to 0.07).
- The harmful seeds have large islands, against the small-island mechanism
  VIC encodes (and Stern et al. describe). The fatal errors fall inside the
  island, on components that reach threshold through two weak bonds with the
  same distractor: an order effect the patient closure cannot see.
- Post hoc: on the amended system the static arc-consistency island of a
  single seed is still 61–64 of 64 components on architectures 0, 1, 2,
  200 and 201, while V ranges from 0 to 0.51.
- TFF's flags are mostly small effects: flagged additions change V by −0.011
  on average (55 % negative), unflagged by +0.023 (24 % negative).

## Limits

- The test system is the assistant's construction, in the spirit of the
  kinetic tile assembly model; it is not DNA origami, and its parameters were
  chosen on development architectures to make V non-degenerate.
- VIC, built from Stern et al.'s folding islands, is the only cross-system
  test, and it fails. TFF was built after seeing this system's failures, so
  its success on fresh architectures is transfer across architectures within
  one system, not across systems.
- TFF uses the growth rule's threshold, a condition of the dynamics, besides
  the constraints.
- V is low throughout (mostly below 0.3), 8 × 8 lattices, q = 4, 300 runs per set.
