# LEAD-191 progress

- **Lead**: LEAD-191, "compare a sheaf route that allows signalling with
  CbD 2.0 on one signalling data set".
- **Branch**: claude/lead-191-sheaf-cbd, cut from origin/staging.
- **Task**: reanalyse LIT-844's data (arXiv 2412.16806) by two routes,
  the signalling-corrected sheaf test and CbD 2.0, if its per-instance
  counts are published, and compare the verdicts. If they are not, build
  a signalling system of the lead's kind, compare the routes on it, and
  say that the reanalysis was not possible.

## Done

- **Step 1: not already held.** There is no changelog fragment, and no
  dated note on LEAD-191 or CLAIM-037. NOTE-648 and THEORY-623 hold only
  the open question.
- **Data.** The per-instance probabilities are not published. The
  authors' repository holds only a README, the release page returned 403,
  and Zenodo has nothing. See README.md.
- **The LPs and the closed forms.**
  - routes.py has the routes and test_routes.py the tests; 249 pass.
  - study.py writes results.json.
  - They cover the published counts, the 25 printed instances, the
    uniform family and a cube sample.
- **Choices made.**
  - CbD 2.0 is the same as CbD 1.0 here, since each connection has two
    binary variables (THEORY-722).
  - The sheaf route is the criterion LIT-844 applies, CF > 2|M|·SF.
    Vallée et al. was not read; the record relies only on LIT-844's
    statement of the criterion.
  - Two more sheaf-side readings are the assistant's own and are labelled
    so: ns-part contextual, and nearest-NS in the sum and max norms.

## Results (short)

- **Sheaf** contextual iff SF < 1/6; **CbD** contextual iff Δ < 2.
  - The sheaf set lies inside the CbD set, so 36,861,830 instances
    (70.9%) diverge, all of them CbD-contextual and not sheaf-contextual.
- **The ns-part reading** is contextual iff SF < 1, which covers at least
  71.1% of the instances.
- **The nearest-NS reading**:
  - in the sum norm, it is contextual on every sampled model with SF < 1;
  - in the max norm, it crosses CbD in both directions.
- **The printed instances.**
  - 25 in all: 9 contextual by both, 8 diverging, 7 noncontextual by both,
    and 1 (videos/text, Δ = 2.000) that rounding leaves undecided.
  - All 25 printed (SF, Δ) pairs can be realised.

## Filing plan

- **A CASE** (executed-study, documented).
- **A CLAIM** (thesis, demonstrated): the formal comparison.
- **Three alternative CLAIMs** (interpretive) on which verdict is right.
  The worker leans to alternative 1 (the data cannot discriminate).
- **Dated notes** on LEAD-191, CLAIM-037 and THEORY-623.
- **A changelog fragment**: record/changelog.d/lead-191.md.

## Next

- File the entries above and commit each one.
