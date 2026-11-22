# LEAD-016 progress

Lead: LEAD-016. Branch: claude/lead-016-adaptive-operators.

Task as understood: run CASE-117's population of identically parameterized
adaptive operators in numpy, with ordinary mixture-of-experts routing as the
baseline. Within it, run QUESTION-134's experiment separating loss of
influence, of competence and of access (coupled against decoupled training
exposure). The decisive comparison: final participation roughly matched,
mechanism varied (fixed usage balancing against endogenous recovery
feedback); measure recovery when rare (from a small positive start, no
further intervention, parameters frozen and trainable) and refill after
removal of a specialist. Scoped to about an hour of CPU; core arms first.
File a CASE (executed-study), a CLAIM if warranted, dated notes on the
entries LEAD-016 advances, on CASE-117 and on LEAD-016.

## Choices made

(none yet)

## Done

(none yet)

## Next

- Design the model and arms; write model.py and tests.
