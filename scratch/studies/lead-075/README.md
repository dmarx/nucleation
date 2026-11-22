# LEAD-075: the staging experiment

A's experiment (QUESTION-392): states A and B with a staging state C,
measuring the bottleneck budget B*(A,B) (CLAIM-571), the least time
T*(A,B;b) at budget b, and the readiness R^pi(A->B;b,z) (TERM-115), to
produce cases where B is statically feasible but unreachable, reachable but
too expensive, reachable only through an architectural change, or reachable
only when temporary reserve capacity is available.

## Files

- `staging_model.py`: the model; B*, T*, the T*(b) step function, the least
  capacity c_tau for a deadline, exact readiness, a Monte Carlo check, and
  the classifier of kinds.
- `test_staging_model.py`: pytest (14 tests), including CASE-233's
  B* = 1.3 and CASE-198's 1.0, and readiness against Monte Carlo.
- `sweep.py`: phase diagrams of the kinds over budget b in [0.6, 1.5] and
  reserve rho in [0, 0.6] (step 0.025) for four variants, the same under
  deadlines 2.0, 2.8 and 3.0, readiness curves, and a 960-point parameter
  sweep of what admitting the staging architecture does.
- `results.jsonl`: one record per item, appended as produced.
- `summary.txt`: `python3 sweep.py summary`.

## Rerun

    cd scratch/studies/lead-075
    export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
    python3 -m pytest -q -p no:cacheprovider test_staging_model.py
    rm results.jsonl && python3 sweep.py      # about 3 minutes on one CPU

## Modelling choices (the lead leaves them open)

1. **C is a staging architecture, not a third configuration.** CASE-198,
   which the lead names as its operationalization, reads A's "staging C" as
   the route (q_A,z0)→(q_A,z1)→(q_B,z1)→(q_B,z0). A state is (q, z), and
   C is any (q, staging). This keeps the model continuous with CASE-198 and
   CASE-233 so its numbers can be checked against them.
2. **CASE-198's numbers as the base**: r0 = 0.7 + 2.4q(1−q), r1 = 0.8 +
   0.4q(1−q), switch surcharge s = 0.2. Switching is allowed at every q
   (the base) or only on part of [0, 1] (a variant).
3. **Unreachability by a gap.** A crease or linkage constraint is modelled
   as home-architecture steps forbidden in q ∈ (0.45, 0.55): the home
   configuration space is disconnected (CLAIM-568's geometric
   disconnection), while every configuration stays holdable.
4. **Time.** Crossing [0, 1] takes 1 under home, 2 under staging; a switch
   takes 0.5. Time does not depend on headroom; T* changes with b only
   because b changes which routes are admissible. Chosen so that the one
   trade-off in play is the route's, not a speed–capacity law the lead
   does not ask for.
5. **Readiness.** "z" in R^pi(A→B;b,z) is read as the architectural
   repertoire Z the policy may use ({home} or {home, staging}). The
   contingency "be at B by tau" is imposed while a background load
   U ~ Uniform[0, 0.3] holds part of b and a temporary reserve rho = 0.2
   is available with probability 0.5; the capacity for the transition is
   b − U + rho·K, held for its duration, and B must be holdable on b − U
   afterwards. The policy takes the fastest admissible route within its
   capacity. Uniform U makes R exact and piecewise linear in b.
6. **Kinds.** With B*_H (home only) and B*_Z (staging admitted), at budget
   b and reserve rho: reachable as is (B*_H ≤ b); only through
   architectural change (B*_Z ≤ b < B*_H, and b + rho < B*_H); only with
   reserve (B*_H ≤ b + rho, B*_Z > b); either suffices; both needed
   together (B*_Z ≤ b + rho only); too expensive (finite B*_Z > b + rho);
   statically feasible but unreachable (B*_Z infinite, ends holdable); not
   holdable (r(A) or r(B) > b). Under a deadline, c_tau replaces B*, and
   a target reachable only too late is its own kind.
