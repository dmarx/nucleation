# LEAD-039 progress

- Lead: LEAD-039 (advances QUESTION-220)
- Branch: claude/lead-039-ib-nesting, cut from origin/staging
- Task: find a structural condition on P(X, Y), beyond Y = f(X) and X, Y
  both binary (THEORY-757), under which information-bottleneck optima are
  nested (refinable, THEORY-753) at every pair of budgets. The
  counterexample disjunct is already held (CLAIM-387, CLAIM-392,
  QUESTION-244), per the lead's note of 2026-11-22.

## Done

- Step 1: checked the record. No structural condition beyond THEORY-757 is
  held (searched QUESTION-220, CLAIM-387/392, THEORY-743/753/757,
  NOTE-976/981, "nest", "refin").
- Library ibnest.py with 6 pytest checks (reproduces CLAIM-392).
- Studies S1 (two rows: 300/300 nest), S2 (three rows: failures common),
  S3 (products: tensorization holds on grid). results.md, README.md.
- Filed CLAIM-tmp8xj7x (two distinct rows nest, any finite Y),
  CLAIM-tmplxbtx (closure under independent products), CLAIM-tmpzohh5
  (erasure chord-gap bound on the cost of forcing nesting), CASE-tmpo9u3y
  (the study), dated notes on LEAD-039 and QUESTION-220, changelog
  fragment record/changelog.d/lead-039.md.

## Next

- Nothing for this worker. Report. The lead opens the pull request.

## Choices

- Worked the open disjunct only (structural condition), since the
  counterexample disjunct is held.
- Stated the theorems for the primal problem at every pair of budgets,
  matching THEORY-757, rather than for the Lagrangian path.
- Filed the loss bound as its own claim, with bears_on rather than
  answers, since it bounds the loss without giving its size.
- No alternatives filed: no choice here was judged to be the owner's.
