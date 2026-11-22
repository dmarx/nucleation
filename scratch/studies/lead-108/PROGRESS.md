# LEAD-108 progress

- Lead: LEAD-108 (state one cost model for stored work; price the cockpit's
  speed bugs, a filed argument and a LEGO bin with the same terms)
- Branch: claude/lead-108-cost-model
- Task as understood: write a cost model with terms for (a) predictability of
  the later query, (b) retrieval cost including search, (c) staleness/bias on
  reuse, (d) erosion of the alternative; keep operational feasibility, lifetime
  efficiency and distributed costs separate (CLAIM-761); price the three cases
  with the same terms. State each choice where the lead leaves a term open;
  give alternatives where the choice is the owner's. A case that needs a new
  term is a counterexample to the single trade (QUESTION-095).

## Done

- Read CLAUDE.md, run-lead skill, design principles opening, LEAD-108,
  QUESTION-095, QUESTION-114, CLAIM-761, CLAIM-303, CLAIM-308, CLAIM-307,
  CLAIM-310, CLAIM-314, CLAIM-630, CLAIM-760, CLAIM-755, CLAIM-647, CASE-094,
  CASE-088, NOTE-867 (Hutchins), docs/record.md (CLAIM, CASE fields).

## Next

1. DONE: model as code, costmodel.py + test_costmodel.py (6 pass).
2. Price the three cases: price_cases.py -> results.json / results.md.
3. File CASE (executed-study, documented) for the run; CLAIM (thesis) for the
   result, with the owner's alternatives in the body.
4. Dated notes on LEAD-108, QUESTION-095, QUESTION-114; changelog fragment.

## Choices made

- Term list fixed before pricing: the lead's four (predictability pi;
  retrieval rho incl. search and recognition, miss; staleness sigma with v,
  delta, L, R; erosion eps) plus CLAIM-303's (F, c, U), CLAIM-761's per-task
  budget B and revision R, the price of work by moment lam, error on the
  on-demand route (sigma_A, L_A), store-level spill (CLAIM-310 k/2, CLAIM-314),
  and a party on each item (CLAIM-760).
- Risk neutral expectations; feasibility as chance over paths (TERM-055 alpha);
  no discounting; erosion a fixed fraction paid on fallback.
