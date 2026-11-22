# LEAD-066 progress

- Lead: LEAD-066, "Bound the commutator of Conjecture A's kind for the hierarchy question, reading Nadler and colleagues first".
- Branch: `claude/lead-066-commutator-bound`, cut from origin/staging (15c07a12f).

## Task as understood

The reading half is done: Nadler et al. is LIT-1250, read in NOTE-986; NOTE-985 states the
bound to attempt. LEAD-052 (branch `claude/lead-052-acquisition-phases`, not yet on staging)
shows the exact case: on tree-symmetric data every kernel of inner products and norms commutes
with the level projectors. This lead does the formal half: state and prove a bound on how far
kernel-flow acquisition departs from the level-by-level flow when [A, P_l] != 0, in terms of
the commutator and (corollary) of a perturbation of the data from the tree-symmetric case; say
what it implies for the acquisition order; check numerically with numpy.

## Done

1. Step 1 check: no entry holds a commutator bound (grep of claims, cases,
   theories, workbench for "commutator"; LEAD-066 named only in itself and
   the curation entry of 2026-11-19). NOTE-986 (Nadler) gives no bound.
2. Derivation in README.md: Lemma 0, Theorem 1 (time-uniform level-wise
   deviation eta_l/lambda_l), Corollaries 2 (acquisition-time intervals and
   the order criterion), 3 (data perturbation), 4 (resolution limit),
   Theorem 5 (moving operator, damped and integral forms; discrete form).
3. Code and tests (12 pass); runs E1 (810 kernel items), E2 (20, sharpness),
   E4 (54 trained networks), about three minutes; analysis; E1 compacted to
   788 KB (full copy in the session scratchpad, lead-066/E1_full.jsonl).
4. README results section.

5. Filed CLAIM-tmpo8cwu (thesis, demonstrated, Proposed) and CASE-tmp99n89
   (executed-study, documented, Proposed); dated notes on LEAD-066 (with
   `operationalized_in`) and QUESTION-217; changelog fragment lead-066.md.

## Next

- Nothing on this branch. For the lead: open the pull request; once
  LEAD-052 merges, relate CLAIM-tmpo8cwu to CLAIM-tmpzujm1 (the exact case).

## Choices

- The comparison flow is the pinching D = sum P A P (the same operator with
  cross-level couplings deleted), not the kernel of the nearest symmetric
  data: it needs no baseline, and covers moving operators. The symmetric
  baseline enters only in Corollaries 2 and 3.
- Level risk and T_l(delta) exactly as QUESTION-217 and LEAD-052 define them
  (the network's own output as decoder).
- LEAD-052's CLAIM-tmpzujm1 is not yet on staging, so it is not cited by
  code from this branch (a temporary code from an unmerged branch would not
  resolve); LEAD-052 is cited instead. Once it merges, a `rests_on` or
  `complements` link is the lead's to add.
