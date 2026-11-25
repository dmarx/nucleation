# LEAD-188 study: the Juggernaut redub's route to the reshoot

Two parts: a testimony search (CODING.md, TESTIMONY.md) and a
circulation-network model of CASE-100 against the list of identifiable
contributions (model.py, sensitivity.py).

## Rerun

    cd scratch/studies/lead-188
    python3 -m pytest -q -p no:cacheprovider test_model.py   # 8 tests
    OPENBLAS_NUM_THREADS=1 python3 -I model.py               # results.json, ~1 s
    rm sensitivity.jsonl                                     # to redo the sweep
    OPENBLAS_NUM_THREADS=1 python3 -I sensitivity.py         # sensitivity.jsonl, ~1 min

numpy and scipy (scipy.sparse.csgraph for connected components), CPU only.

## The model, in one paragraph

A heavy-tailed contact network (configuration model, degree exponent
2.5). Three hundred fan videos per world, each posted by an ordinary person,
each spreading by bond percolation with its own transmissibility (Beta
prior). One decision-maker adopts one video's line. Three models of which
one he adopts: **M0**, the list of identifiable contributions without
distributors (every video equally likely; the spread adds nothing);
**MH**, the list with identifiable distributors (the H highest-degree
nodes, the named aggregators and news segments; weight 1 + κ·hubs
reached); **MC**, circulation (weight s^α, where s is how many people it reached; α = 0 is M0).
The case's observation: the adopted video was among the most circulated
(top q). Ascertainment weight s^γ allows for the case being known because
the video was famous. Free parameters are priced by the exact marginal
likelihood over stated priors (α uniform on [0, 2]; κ log-uniform on
[10⁻², 10²]), which CLAIM-154's rule approximates for large samples.

## Results (results.json, sensitivity.jsonl)

Base setting (n = 3000, H = 10, T ~ Beta(1, 6), 12 worlds), Bayes factors:

| ascertainment γ | q | MC/M0 | MH/M0 | MC/MH |
|---|---|---|---|---|
| 0 | 0.01 | 10.8 | 3.8 | 2.8 |
| 0 | 0.05 | 8.5 | 3.8 | 2.2 |
| 0.5 | 0.01 | 2.0 | 1.1 | 1.8 |
| 1 | 0.01 | 1.6 | 1.0 | 1.6 |
| 1 | 0.05 | 1.3 | 1.0 | 1.3 |

Sweep over n ∈ {1500, 3000}, H ∈ {3, 10, 30}, T ~ Beta(1, 6) or
Beta(1, 12), three seeds (36 settings, q = 0.01):

- γ = 0: MC/M0 from 10 to 32; MC/MH from 2.3 to 4.7.
- γ = 1: MC/M0 from 1.47 to 1.64; MC/MH from 1.33 to 1.60.

In words: one observation (the adopted line was a top-circulated video's)
favours circulation over a bare list by about ten to thirty, but over a
list that names the distributors by at most about five, and if the case
is known to us partly because the video was famous, by less than two
either way. The case does not meet CLAIM-332's defeater, and does not
discharge it either.

## Limits

- MH names distributors by count only (hubs reached saturates at H for
  every large cascade); a list that also records each named distributor's
  audience would track circulation more closely and could close the gap.
- The circulation quantile q of the redub is from the creators'
  recollection ("millions"), not a measured rank among 2006 fan videos.
- The model is a toy: one decision-maker, one adoption, no timing. Timing
  (posted 14 February 2006, a pickup day at Elstree before the 26 May
  release) is not used.
