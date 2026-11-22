# LEAD-076 progress

- Lead: LEAD-076
- Branch: claude/lead-076-sentry (cut from origin/staging)
- Task as understood: (1) construct cases of structural frustration without
  operative thwarting and the reverse (QUESTION-131), thwarting identified by
  counterfactual intervention; (2) run CASE-153's sentry design in full, with a
  hidden world state and a sentry that can restrict the evidence (inspection)
  used to judge it: five-condition first experiment and the 2x2x2 factorial,
  with Bayesian and habit baselines; numpy, pytest. File a CASE
  (executed-study), CLAIMs where warranted, dated notes on CASE-153, the
  advanced entries and LEAD-076, and a changelog fragment.

## Step 1 check (already held?)

- Not held as a whole. Nothing after 2026-11-19 cites LEAD-076 or runs CASE-153.
- Partly held: CLAIM-631 (Proposed, demonstrated) item 3 constructs structural
  frustration with no unmet, acting member (so no thwarting), and item 6 says
  the precondition of thwarting can occur inside the requirement complex. It
  gives a necessary condition, not thwarting with a counterfactual. So the
  frustration-without-thwarting direction is not filed again as such; the new
  parts are the counterfactual (but-for) test, thwarting inside the complex,
  and the sentry.

## Done

- frustration.py + test_frustration.py (12 tests pass); constructions.md.
- sentry.py + test_sentry.py (all pass); run_sentry.py: first experiment,
  3x2x3 factorial + habit rows, interaction contrasts, CLAIM-446's four
  interventions, phase diagram (kappa x eta, 5 cells), sensitivity (h,
  fixed g = 0.95, second seed set). analyze.py -> results/summary.md.
- Codes reserved: CASE-tmpxmuri (the executed study), CLAIM-tmpmcrb7
  (constructions, demonstrated), CLAIM-tmpqp1h6 (sentry finding, empirical).

## Key results (for the filing)

- Constructions: under a joint-satisfaction-seeking rule, an unmet acting
  member implies the read set is frustrated (so no thwarting inside K); in
  a minimal conflict exactly one member is unmet and each other is
  separately a but-for thwarter; pairwise attribution fails inside a larger
  organization (C4); thwarting inside K needs a rule that weighs authority
  or preference (C5, C6 = static sentry); frustration can be causally idle
  (C2) or unvoiced (C1 = CLAIM-631 item 3).
- Sentry: under success feedback the authority update is the habit of
  protecting (identical law but for harm steps); matched habit reproduces
  every intervention it can receive (belief: fails in both; authority/habit
  reset: works in both; evidence access: same). Only audit and
  reinforcement correction, which act on an evaluator a habit lacks, tell
  them apart. Restriction x success interaction +99 needless-cost units
  [95, 103]; neither correction removes it. Protected investigator gives
  the CASE's target regime (belief corrected in 6 steps, protection
  persists in 87%). Phase boundary in kappa ~1.25-1.5 under success, ~2.75
  under independent evaluation; protection when danger returns always kept.
  Sensitive to assumed hazard h.

## Choices made

- See README "Choices the case left open".
- Habit vs authority reading of CLAIM-446's defeater: both filed as
  alternatives in the sentry claim's body; the owner's call.

- Filed: CASE-tmpxmuri, CLAIM-tmpmcrb7, CLAIM-tmpqp1h6; dated notes on
  CASE-153, QUESTION-131, CLAIM-446, CLAIM-443, CLAIM-445, LEAD-076 (no
  note on CLAIM-631: the new claim `complements` it instead); excuses for
  new or Proposed codes; changelog fragment record/changelog.d/lead-076.md.
  Frontmatter, title and H1 checks pass.

## Next

- Nothing on this branch. Report. Not run: CASE-153's second version
  (risky inspection).
