# LEAD-093: a nucleus that makes the constraint of its own formation

A kinetic construction in numpy/scipy in which nuclei form fast only where a
teacher (template, scaffold) T is present, and each nucleus, once formed,
makes teachers from material: the student becomes a teacher. The study
measures when that loop closes (the teacher is kept without any outside
supply of it), the constraint turnover it survives, the outside supply it
still needs, and what changes when nuclei only repair teachers instead of
making them. Filed as an executed-study CASE with its claims.

## Model (`closing.py`)

    m' = J − δ m − F − β m N              material, supplied at J
    T' = σ − k_T T + β m N                teacher: outside supply σ, turnover k_T
    N' = (1 − ε) F − d N                  nuclei that teach
    B' = ε F − d B                        defective nuclei: same structure, teach nothing
    F  = a0 m² + a1 m T² / (K² + T²)      spontaneous + templated formation

Base: J = 1, δ = 0.1, a0 = 1e−6, a1 = 0.1, K = 2, d = 0.1, β = 0.02,
k_T = 0.1, ε = 0. Invented and illustrative. Formation is cooperative in T
(Hill 2), so a founding is needed; with linear templating the loop ignites
from any seed and there is nothing to found.

Repair arm: nuclei make no teachers (β = 0) but repair damaged ones,
T → D at k_T, D lost at λ, D → T at ρ N D, costing `rcost` material per
repair (0, and 1 as a check).

Generation-resolved version (`gen_rhs`): the outside teacher is generation 0;
a nucleus taught by generation g is g + 1 and makes generation g + 1
teachers. Gillespie version (`gillespie_extinction`): counts in volume Ω.

**Closed** at a parameter point: with σ = 0 there is a stable state with
N ≥ 50 × the spontaneous background. **Closed at time t**: switching σ off
for good at t leaves the nucleus maintained.

## Experiments (`experiments.py`)

Each writes one JSON line per item to `results/<name>.jsonl` as produced
and skips items already present.

| name | what |
|---|---|
| e1 | phase over k_T × β (25 × 25): self-igniting, bistable (closes once founded), open |
| e2 | critical k_T against β, ε and J; critical ε, J, β at base |
| e3 | material J needed for closure; teacher supply σ to hold N = 2 with and without the loop |
| e4 | shortest founding by an outside teacher; the state at that moment |
| e4b | where the loop self-ignites, how much a founding speeds formation |
| e5 | removal of T, N or both, and turnover pulses, survived without supply |
| e6 | repair arm: σ needed to hold N = 2, lifetime after withdrawal |
| e7 | populations matched in nuclei count, differing in the share that teaches |
| e8 | succession by generation after a founding |
| e9 | finite numbers: time to lose the loop after withdrawal, 40 runs per size |

## Rerun

    cd scratch/studies/lead-093
    export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
    python3 -I -m pytest -q -p no:cacheprovider test_closing.py   # 11 tests
    python3 -I experiments.py e1 e2 e3 e4 e4b e5 e6 e7 e8 e9

About 6 minutes for e1–e8 and about 20 for e9 on one core. Delete a
results file to recompute it.

## Notes on the results

- e6, λ = 0.01, ρ = 5: the run reports σ = 0 because the decay time
  (about 1/(λ D/(T + D)) ≈ 16 000) exceeds the 12 000 the steady-state runs
  integrate; the formula σ = k_T T/(1 + ρN/λ) gives 1e−4. Every other
  rcost = 0 row agrees with the formula within 2e−4.
- e4b: where a founding brings N past half its maintained value before
  it ends, the time reported is when it did, during the founding.
