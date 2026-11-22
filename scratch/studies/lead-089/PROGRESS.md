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

- Read CLAUDE.md, run-lead skill, LEAD-089, QUESTION-056, QUESTION-041,
  CLAIM-024, CLAIM-174, CLAIM-487, CLAIM-154, CLAIM-027, CLAIM-021,
  CLAIM-122, CLAIM-159, CLAIM-482, CLAIM-427, ARG-025, CASE-023, CASE-003,
  CASE-002, CASE-036, CASE-158, CASE-166.
- Found the three fronts already held as readings, so no outside fetch is
  needed for the reading part: planning (Bratman, LIT-567, NOTE-464,
  THEORY-076); control theory's regulation (Ashby, THEORY-324; Powers et
  al., NOTE-954, NOTE-959); institutional theory (Polski and Ostrom,
  THEORY-1809, NOTE-1842; Crawford and Ostrom's grammar, THEORY-1787).

## Next

1. model.py + test_model.py: Northstar episodes, the will-organization
   model (WO) and four control-only models (C0 blind, C1 saturated lookup,
   C2 additive metacontrol gate, C3 gate with pairwise interactions).
2. study.py: three worlds (governed, idle authority, idiosyncratic
   authority), train on four arrangements, test on four unseen ones; log
   evidence and held-out log predictive; per-item JSONL.
3. File CASE (executed-study), CLAIM(s), notes on held entries, changelog.

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
  training, which is the "intervention" grade of CLAIM-427.
- **Teeth**: the WO model is also scored in worlds where it is false
  (authority idle, CLAIM-089's surviving case; authority idiosyncratic),
  so that the test can come out against it.
