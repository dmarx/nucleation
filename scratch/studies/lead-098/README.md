# LEAD-098: CASE-179's network, run

A simulation of CASE-179's proposed study, with A12's three arms (CLAIM-616,
CASE-225) and QUESTION-063's two interventions.

- `sim.py`: the model. Stuart-Landau units on a graph (a ring of 8 with one
  chord, so two independent cycles); each edge carries a correspondence map,
  a phase offset; the coupling realizes its own maps, which may or may not
  be the apparatus's. Dissipative coupling is the connection Laplacian flow
  −Lz; conservative coupling is −iLz with no amplitude dynamics (unitary).
  Common drive F e^{i(Ωt+ψ_j)}. Optional slow capacity variables μ_j
  maintained by neighbours' activity (A12's adaptive capacity), and plastic
  maps (QUESTION-282). Stochastic Heun integrator, batched so that a
  control and an intervened copy share their noise. Also the cellular-sheaf
  Kron reduction used for QUESTION-283.
- `test_sim.py`: pytest tests (holonomy, twisted Laplacian, limit cycle,
  attraction to a section, norm conservation, gain recovery, Hansen-Ghrist).
- `run.py`: the study. One item per arm or configuration; each result is
  appended to `results.jsonl` as it is computed, and a rerun skips items
  already there.
- `results.jsonl`: the results.

Rerun (about five minutes on one CPU):

    python3 -I -m pytest -q test_sim.py
    python3 -I run.py            # resumes from results.jsonl

Seeds are fixed (numpy default_rng 98 for the network, 1-8 for the runs),
so a rerun from an empty results file reproduces the numbers.
