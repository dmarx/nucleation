# LEAD-063: one integration measure and one anti-nesting rule, applied to a modular mind and to a group

Everything here is exact computation on linear Gaussian models; nothing is
sampled except in one test. numpy and pytest only, CPU, minutes.

## Files

- `phi.py`: the measure (Barrett and Seth's autoregressive integrated
  information, Phi_AR, at the size-normalized minimum information
  bipartition), the exclusion rule, the two models, and an exhaustive
  main-complex search for systems of at most 12 units.
- `test_phi.py`: pytest (15 tests): Lyapunov solution, the scalar AR(1)
  closed form, agreement with a sampled regression, Phi = 0 for disconnected
  parts, bipartition counts, model structure, the two limiting verdicts, and
  that the restricted MIB search for the 27-unit group is not beaten by 200
  random cuts.
- `run.py` -> `results.jsonl`: the sweep. Coupling between parts from 0 to
  0.25 in steps of 0.01, 1, 2 or 3 links between each pair of parts,
  size-normalized and unnormalized MIB, for the modular mind and for the
  group. One JSON line per item, resumable.
- `check_mind.py` -> `complex_check.jsonl`: for the mind, the level verdict
  checked against exclusion over all 502 subsets of two or more units.
- `check_small_group.py` -> `small_group.jsonl`: exhaustive exclusion over
  all 4083 subsets of a 12-unit group (2 members, each 2 modules of 3), so
  that no candidate set is assumed.
- `summarise.py` -> `summary.md`: thresholds and the matched-coupling table.

## Rerun

    cd scratch/studies/lead-063
    python3 -I -m pytest -q -p no:cacheprovider test_phi.py
    python3 -I run.py              # about 10 minutes
    python3 -I check_mind.py       # about 2 minutes
    python3 -I check_small_group.py  # about 15 minutes
    python3 -I summarise.py

Delete a `.jsonl` file to recompute it from scratch.

## Models

- Modular mind: 3 modules of 3 units. Inside a module every ordered pair,
  self-loops included, has weight w = 0.12. Each pair of modules is joined
  by `width` reciprocal unit pairs of weight c. Dynamics
  X_{t+1} = A X_t + e_t, e_t ~ N(0, I).
- Group: 3 members, each that modular mind with c = 0.15 and width 3 (a
  unified mind by the rule), joined member to member by `width` reciprocal
  unit pairs of weight g. The group is the mind's construction one level up.

## Measure and rule

phi(S; M1, M2) = I(S_t; S_{t-1}) - I(M1_t; M1_{t-1}) - I(M2_t; M2_{t-1}),
Phi(S) = phi at the bipartition minimizing phi / min(|M1|, |M2|).
Exclusion: of nested candidates (module within mind; module within member
within group), the subject is the candidate of largest Phi. For the 27-unit
group the MIB is searched over the 255 cuts along module seams and the 27
single-unit cuts; everything of 12 units or fewer is searched exhaustively.
