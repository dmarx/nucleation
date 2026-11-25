# LEAD-111 study: the operational cover as the determinacy sub-cover

Formal check of whether CLAIM-201's "operational cover" (a context = a question
readers answer determinately) is a cover with restriction maps in the
sheaf-theoretic sense (THEORY-012, LIT-016, TERM-042), as CLAIM-251 presses.

## Files

- `operational_cover.py` — the construction: event presheaf and restriction
  maps (`restriction_matrix`), no-signalling check, the determinacy functional
  `det_theta` / `operational_cover`, the induced sub-cover `induced_cover`, and
  `is_down_closed_subpresheaf`.
- `test_operational_cover.py` — pytest, 10 tests (all pass).
- `demo_output.txt` — the worked scenario at four thresholds.

## Rerun

    cd scratch/studies/lead-111
    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 -I -m pytest -q

`python3 -I` drops the cwd from `sys.path`; pytest adds it back, so the tests
import `operational_cover` fine. For the ad-hoc demo, prepend
`import sys; sys.path.insert(0, '.')`.

## What it shows

Scenario X = {a,b,c}, cover M = {{a,b},{b,c}} (overlap {b}), binary outcomes.

1. **Restriction maps form a presheaf.** `res^U_U = id`, and
   `res^U_V ∘ res^W_U = res^W_V` for V ⊆ U ⊆ W (functoriality); each map sends a
   distribution to a distribution. (tests 1)
2. **The induced sub-cover is a genuine down-closed cover.** For the
   determinable base D = K_theta(e), the induced contexts M|_D = {C∩D : C∈M}
   sit inside D, are closed under restriction, and cover D — a sub-site of the
   scenario with inherited restriction maps. (horn 1 of the lead)
3. **The selection is a thresholded functional of the empirical model on a
   fixed cover.** Two models on the *same* M give different operational covers;
   so "which questions are determinate" is a property of the responses e, not of
   M. (reading A / CLAIM-251's point)
4. **A thresholded readout, not a canonical functor.** K_theta(e) shrinks
   monotonically as theta rises, and distinct models share a cover at fixed
   theta (non-injective). So there is no canonical, parameter-free functor from
   empirical models to covers — only a thresholded readout plus the induced
   sub-site.

See `demo_output.txt`: at theta 0.5 all of {a,b,c} is determinate; at 0.75 only
{a,b}; at 0.86 only {b}; at 0.95 none — the induced sub-site tracking each step.
