# LEAD-109: self-consistent factorizations into agents

Does a fixed level and target admit several self-consistent factorizations
into agents (CLAIM-170's defeated_if; CLAIM-168/174's open part)?

## Model

A fixed level = a fixed set of n regimes with a fixed symmetric coupling
matrix M (M[i,j] >= 0). A factorization = a partition P of the regimes
into blocks (candidate agents). The admission test (CLAIM-174):

- **Test 1** (one system; CLAIM-157/TERM-049, priced by CLAIM-154): a block
  is near-decomposable — strong within-block coupling, weak across-block —
  with gap(P) = b(P)/a(P) > tau, where a(P) is the strongest coupling P
  cuts and b(P) is the weakest within-block single-linkage merge level
  (max-bottleneck spanning tree). Singletons impose no within-constraint.
- **Test 2** (goal-directed beats device by the Occam cost): CLAIM-154's
  rule, reify iff d'^2 > Occam. Modelled as a per-block verdict.
- **Test 3** (adaptation): a further per-block gate; folded into test 2 here.

A factorization *into agents* requires every block to pass tests 1-3.

## Result (checked numerically, all in `test_factorization.py`)

1. **Crosscutting disagreement is impossible.** The test-1-clearing
   partitions are exactly cuts of M's single-linkage dendrogram, hence
   totally nested (a chain under refinement). Over 2000 random 6-regime
   couplings x 6 thresholds (12000 non-empty families) **zero** crosscutting
   ties were found; every family is a nested chain with a unique finest
   member. Max family size 6.
2. **Exact symmetry does not break this.** On the symmetric 4-ring the two
   rotation-related pairings {01,23} and {12,30} both have gap 1.0; neither
   clears any tau>1. They never both clear — a crosscutting tie cannot be
   forced even by symmetry, because each pair straddles a strong edge.
3. **Grain multiplicity is real.** In a two-level (watchmaker) hierarchy the
   fine partition (gap 3.33) and the coarse whole (gap inf) both clear test 1;
   under the full agent tests both the two-agent and the one-agent
   factorizations can hold at once (nested, differing only in grain). This is
   the only non-uniqueness, and it is CLAIM-170's two "levels" (room vs pair)
   and CLAIM-174's Kenton actor-critic-vs-one-agent-graph.

So: at a fixed level and target the self-consistent factorizations form a
nested hierarchy of coarsenings of a unique finest partition. Agents never
disagree about co-grouping two strongly-coupled regimes; the only
indeterminacy is how coarse to go. Tests 2-3 only prune the chain.

## Files

- `factorization.py`: partitions, test-1 gap, dendrogram cuts, CLAIM-154
  reify rule, self-consistent family, chain/finest helpers.
- `test_factorization.py`: 10 tests (the result above).
- `run.py`: headline numbers -> `results.json`.

## Rerun

    cd scratch/studies/lead-109
    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 \
      NUMEXPR_NUM_THREADS=1 python3 -I -m pytest -q
    OMP_NUM_THREADS=1 ... python3 -I run.py

Runs in seconds. CPU only, BLAS threads 1.
