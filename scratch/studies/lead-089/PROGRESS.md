# PROGRESS: LEAD-089

- Lead: LEAD-089
- Branch: claude/lead-089-northstar-priced
- Task: model the Northstar case twice, once with control and metacontrol
  mechanisms alone and once with a will-organization over them; price the
  difference as CLAIM-174 does (test 4: does a model with a
  will-organization beat the model without one by more than its Occam
  cost); set planning, control and institutional theory beside the account
  (open sources only).

## Done

- Read CLAUDE.md, run-lead skill, LEAD-089 and what it advances and cites.
- The three fronts are already held as readings, so nothing was fetched:
  planning (THEORY-076, NOTE-464), control's regulation (THEORY-324,
  NOTE-959), executive control (THEORY-1110), institutional (THEORY-1809,
  THEORY-1787).
- model.py, test_model.py (8 tests pass), study.py (320 items, plus C4),
  analyze.py, asymptote.py, README.md; results in results/.
- Filed CASE-tmpokq28 (executed study), CLAIM-tmp92xul (demonstrated
  finding), CLAIM-tmp773u9 (interpretive reading of the three fronts).
- Dated notes on LEAD-089, QUESTION-056, CLAIM-024, CLAIM-487, CLAIM-174.
- Changelog fragment record/changelog.d/lead-089.md.

## Next

- Report to the lead (no pull request: the lead opens it).

## Choices

- **The simplest model that prices the difference.** Discrete episodes:
  context (specialist objection o, incident signal r, business-critical
  b), outcome one of three regimes (routine deploy, cautious verification,
  emergency suspension), arrangement of authority a = (s, j, v): whether
  an objection suspends (CASE-003's A/B), who classifies severity
  (CASE-002), whether a business-critical override exists (CASE-002).
  Chosen because it is the case's own variants, the outcome set is small
  enough for exact conjugate evidence where a model allows it, and the
  arrangement can be intervened on independently of the attitudes.
- **Price as CLAIM-174 and CLAIM-154 do**: log marginal likelihood (Occam
  priced), exact by Dirichlet conjugacy or quadrature where possible,
  Laplace for the logistic gates (regular, so CLAIM-154's condition holds).
  Beside it, held-out log predictive on arrangements never seen in
  training, which is the "intervention" grade of CLAIM-427 / ARG-025.
- **Teeth**: the WO model is also scored in worlds where it is false
  (authority idle, CLAIM-089's surviving case; authority idiosyncratic;
  one relation composing differently), so that the test can come out
  against it. It did, in the first two; the third showed that training
  evidence alone cannot catch it.
- **C3 omits products of two authority bits**: they are never observed in
  training (no training arrangement has two changes), so they would only
  add prior noise. Stated in the CASE.
- **The lead's "What would count" read as inverted** (a difference an
  existing theory already gives supports CLAIM-024 on that front); said in
  CLAIM-tmp773u9 and the lead's note, for the owner.
