# LEAD-015 progress

- Lead: LEAD-015 (derive the two-institution version of the symmetry-breaking condition, building the coupled meaning-influence model for two regulators).
- Branch: `claude/lead-015-two-institution-condition`, cut from origin/staging.
- Task as understood: couple two copies of LEAD-090's reduced one-institution model (CASE-tmpz4n6b), an evaluator (regulator) and an evaluated party, by stating how the evaluated party affects the evaluator's evidence or resources and how the evaluator's reading affects the evaluated party's standing (CLAIM-404's cross-institution beta and gamma); linearize at the symmetric state; derive the instability condition; check numerically; file as Proposed CLAIM/CASE with dated notes and a changelog fragment.

## Done

- Step 1: not already held. Grep of record/ and scratch/ for "two-institution", "two institutions", "two regulators", LEAD-015: only LEAD-015's own note, CLAIM-404 and CASE-123 saying it has not been derived; LEAD-090's filings (CASE-tmpz4n6b, CLAIM-tmp6f8w8, CLAIM-tmpw3bak) give the one-institution model only.

- model.py, test_model.py (14 pass), run.py, README.md (derivation); results e1-e5 in results/.
- Result: with nonnegative channels and each institution stable alone, the symmetric state is unstable iff (theta + sigma_E omega)(chi + sigma_P psi) > Delta_E Delta_P, Delta_i = (1 - phi'_i) - g_i sigma_i^2/2; rho, delta cancel. General form: round-trip gain rho(G_P C_PE G_E C_EP) > 1. 1802/1802 random sets agree with the nonlinear map.

## Next

- File CASE (executed-study) and CLAIMs; dated notes on LEAD-015, CLAIM-404, CLAIM-330, CASE-092, QUESTION-100, CASE-tmpz4n6b? (new in staging: only if held); changelog fragment.

## Choices

- Each institution is LEAD-090's reduced model (Regime A soft, ema conferral) unchanged.
- Four channels, each a reading of CLAIM-404's words: evidence P->E (theta, into b_E), resources P->E (omega, additive tilt of E's conferral), evidence E->P (chi), standing E->P (psi, tilt of P's conferral). A21's chain = theta + psi.
- Alternative reading of resources: capacity (multiplicative, omega scales g_E). Zero at linear order; gives capture below the threshold from a large push, one-sided. Filed as an alternative.
- Corrective (negative) return channels: the nonnegative condition does not apply; instability there is oscillatory (complex pair) in 2158 of 2159 unstable draws. Reported, not claimed beyond that.
