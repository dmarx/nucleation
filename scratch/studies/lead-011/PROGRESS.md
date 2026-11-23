# LEAD-011 progress

- Lead: LEAD-011, "Show which assumptions are needed for a scalar optimum of
  learning to exist when what is learned changes what can later be learned"
- Branch: claude/lead-011-scalar-optimum (from origin/staging)
- Advances: QUESTION-495; cited beside CLAIM-754 (no context-free scalar ranks learners)

## Task as understood

State the conditions (a fixed task distribution, resource costs, a horizon,
a valuation) under which an optimal learning policy is a well-defined scalar
optimum, and show which of them fail when the learner's own learning changes
the tasks it will face (and what it values). Give at least one construction
in which an assumption fails and no scalar optimum exists; a small numeric
check with pytest here. File CLAIMs (Proposed, demonstrated), an ARG if it
fits, dated notes on LEAD-011 and its targets, a changelog fragment.

## Step 1: already held?

Not held. No changelog fragment names LEAD-011. Grep of claims, arguments,
cases and workbench for "scalar optimum", "optimal learning", "learning
polic", "no scalar", "preference change", "time inconsisten": the nearest are
CLAIM-754 (no context-free scalar ranks learners; one exists once task
distribution, costs, horizon and preferences are declared, asserted, not
shown), CLAIM-756 / CASE-295 / ARG-120 (an acquisition valued by its effect on
later acquisition costs), CLAIM-758 (overconsolidation), CLAIM-585 (no scalar
threshold for several resources) and CLAIM-tmphjm0q (no optimal regulation
until commitments are declared). None states the existence conditions or a
counterexample. QUESTION-495's notes hold readings only.

## Choices

- Reading of "what is learned changes what can later be learned": two
  readings, both filed, since they come apart in their answer:
  (R1) learning changes the tasks/opportunities met later: a declared
  state-dependent kernel absorbs it, so endogeneity alone breaks nothing;
  what can fail is the horizon (growth outpacing discount) and attainment.
  (R2) learning changes what is valued (the brief's gloss; QUESTION-495's
  "what the learner can later ask"): no scalar optimum without a declared
  evaluator with cross-self comparability; dilemma between ex ante and ex
  post evaluation.
- Constructions live in claim bodies, numbers guarded by pytest here; no CASE
  filed (the brief asks for CLAIMs and an ARG).

- CLAIM-754 is related by `complements`, not `objects_to`, though the run
  qualifies its last clause; whether it should be an objection is left to
  the owner.

## Done

- constructions.py, test_constructions.py (22 pass), README.md.
- CLAIM-tmpy87xn: the four conditions; endogenous tasks harmless.
- CLAIM-tmp6ppvo: valuation changed by learning; symmetric two-self and
  three-self constructions; ex ante / ex post / self-ratification dilemma.
- CLAIM-tmpl9022: learnability outgrowing the discount; no optimal policy.
- ARG-tmpi8mhy: existence, the conditions are independent.
- Dated notes on LEAD-011, QUESTION-495, CLAIM-754.
- Changelog fragment record/changelog.d/lead-011.md.

## Next

- Nothing for this run. Remaining for the record: which evaluator to adopt
  when valuation changes (owner's); a construction for an undeclared task
  law (condition 1); a worked case on a real learner.
