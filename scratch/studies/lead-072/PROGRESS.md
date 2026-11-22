# LEAD-072 progress

- Lead: LEAD-072 (signalling estimators with bias correction and stated error, or a signalling test with a stated null, applied to LIT-851's systems with their occurrence counts).
- Branch: claude/lead-072-signalling-estimators (cut from origin/staging 15c07a12f).

## Task as understood

Derive (a) a bias-corrected estimator of CbD signalling Δ = Σ_q |⟨R_q^c⟩ − ⟨R_q^c'⟩| for binary cyclic systems with a stated sampling error, and/or (b) an exact test of no-signalling with a stated null; check bias, coverage and size by simulation (numpy); apply to LIT-851's 90 rank-2 systems if their occurrence counts are in a lawful open copy.

## Done

- Step 1 (held check): LEAD-182's CLAIM-tmpalxab / CASE-tmpjp6vg quantify the plug-in bias and say a bias-corrected estimator "was not built"; nothing in record/ builds one. Target not held.

## Next

- Locate a lawful copy of LIT-851's appendix (counts?).
- Derive and simulate.
