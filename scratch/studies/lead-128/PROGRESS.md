# LEAD-128 progress

- **Lead:** LEAD-128 — "Find or make a fit of the expected-value-of-control
  model in which control intensity falls with its cost."
- **Branch:** `claude/lead-128-evc-cost-fit`, cut from origin/staging.

## The task as understood

LEAD-128 advances CLAIM-358 and CLAIM-162, both held back because their
ground THEORY-070 (the EVC account, Shenhav/Botvinick/Cohen 2013, LIT-585)
is Proposed. THEORY-070's `promote_when` (1): a fit of the EVC computation
to behaviour in which control intensity — measured by an accumulator
parameter or by conflict adaptation — rises with the payoff for control at
fixed difficulty and falls with its cost, and does so better than a model
without the cost term. The lead's "what would count": intensity falling
with cost promotes CLAIM-358.

Plan: (step 1, done) confirm not already held — confirmed; no fit showing
intensity falling with cost is in the record, which is exactly why
THEORY-070/CLAIM-358/CLAIM-162 are Proposed. (step 2) search for a published
fit via Europe PMC / arXiv (lawful open copies only). If held/found, read and
file (read-and-file 5-9). (step 3) else fit the effort-cost/EVC model to an
open effort-discounting dataset with numpy/scipy, file as a CASE
(executed-study, documented), plus a Proposed CLAIM for the finding.

## Done

- Read CLAUDE.md, design-principles opening, run-lead skill, read-and-file
  as needed, docs/record.md fields for CASE/CLAIM.
- Read LEAD-128, CLAIM-358, CLAIM-162, THEORY-070, NOTE-446.
- Step 1: confirmed target not held.
- Branch cut from origin/staging; PROGRESS.md pushed.

## Search done (Europe PMC)

Closest published EVC accumulator fits found (open):
- Leng, Yee, Ritz, Shenhav 2021, PLOS Comp Biol, PMC8746743, CC BY — EVC
  model fit to Stroop; incentives adjust drift rate (accumulator) and
  threshold. Shows intensity RISING with payoff — the payoff half of
  THEORY-070 promote_when (1), not the cost half.
- Masís Obando, Musslick, Cohen 2025, PNAS, PMC12595486, CC BY-NC-ND — more
  control when task is learnable (benefit side), not cost side.
- Grahek, Leng, Musslick, Shenhav 2026, Psych Review, PMC13023295 — NOT open
  access; stop.

None plainly reports a fit in which control intensity FALLS as the cost of
control rises, model-compared against a no-cost model, on verifiable open
data. The direct match to "intensity falls with cost" is effort discounting,
which the lead suggests.

## Choice made (route)

Route: make the fit myself on an open effort-discounting dataset, as the lead
provides for ("Otherwise fit ... yourself"). Reason: no found published fit
delivers the cost-side direction as its demonstrated, model-compared result;
effort discounting is where chosen control intensity falling with its cost is
the measured result, and the lead names it. The found incentive-side fits are
noted on the lead as the complementary (payoff) half.

## Next

- Find a concrete lawfully-open effort-discounting dataset (OSF/GitHub).
- Fit EVC effort-cost model with numpy/scipy; compare to no-cost model;
  show chosen control intensity vs. cost. File as CASE + Proposed CLAIM.
