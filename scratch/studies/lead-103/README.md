# LEAD-103 study: the noncontextual inequality a pragmatic experiment implies

Operational equivalences a pragmatic rendering experiment assumes, and the
Spekkens-style generalized- (preparation-) noncontextuality inequality they
imply, with a numeric check.

## Setup
- Four renderings R1..R4 (preparations) of one utterance; two binary
  relational probes X, Z (measurements), outcomes +-1.
- Predictability `<X>_i = p(+|Ri,X) - p(-|Ri,X)` in [-1, 1].

## The equivalences assumed
- **OE1 (equal-predictability orbit).** `|<X>_i| = x`, `|<Z>_i| = z` for all i,
  with sign patterns R1:(+,+), R2:(-,+), R3:(-,-), R4:(+,-).
- **OE2 (mixture equivalence).** `1/2 R1 + 1/2 R3 ~ 1/2 R2 + 1/2 R4`: the two
  equal mixtures give identical statistics for every probe.

Generalized (preparation) noncontextuality forces
`1/2 nu1 + 1/2 nu3 = 1/2 nu2 + 1/2 nu4` on the ontic space.

## Result
Any preparation-noncontextual model reproducing OE1 and OE2 satisfies the
diamond `|<X>| + |<Z>| <= 1`. This is Catani et al.'s Eq. 12 (THEORY-315,
NOTE-825) stated for the pragmatic experiment. It is not a sheaf /
Kochen-Specker criterion: X and Z are never measured together, so the cover
{X},{Z} has no overlap and a global-section test is vacuous.

## Checks (`results.jsonl`)
1. `nc_bound_lp_diamond_faces` - exact LP over deterministic ontic states:
   all four faces `+-x +-z` max at exactly 1.0.
2. `nc_bound_general_search` - LP over the ontic distributions for 200 random
   *non-deterministic* response functions: max x+z = 0.874 < 1 (corroborates
   that non-determinism cannot beat the bound; the analytic reduction to
   deterministic responses is Schmid-Spekkens-Wolfe).
3. `qubit_orbit` - the qubit realization (Bloch vectors (+-x,0,+-z)) satisfies
   OE1 and OE2 exactly (the two mixtures both equal I/2) and violates the
   bound, reaching x+z = sqrt(2) ~= 1.414 at x=z=1/sqrt(2).
4. `nc_bound_without_OE2` - dropping OE2 lets a noncontextual model reach
   x=z=1 (x+z=2): the mixture equivalence is what the inequality rests on.

## Rerun
    cd scratch/studies/lead-103
    export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
    python3 -I inequality.py            # appends to results.jsonl
    python3 -I -m pytest -q             # 5 tests

numpy + scipy (linprog highs), CPU, BLAS threads 1. Runs in well under a minute.
