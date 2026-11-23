# LEAD-044 progress

- Lead: LEAD-044, "Compare equal-budget interventions at different locations in an organization's constraint structure"
- Branch: claude/lead-044-equal-budget-interventions (from origin/staging)
- Advances: CLAIM-562 (placement predicts better than count; adding can hurt)

## Task as understood

Search open organizational histories and evaluations for documented
interventions of similar cost at different places in one organization, and
code them under rules written before coding. If none meets the lead's
standard, say so and either file the closest cases with what they lack, or
build a small numpy simulation with pytest tests here. Results as a CASE and
CLAIMs, all Proposed; dated notes on LEAD-044 and CLAIM-562; a changelog
fragment.

## Step 1: already held?

Not held. Grep of record/ for LEAD-044, "equal-budget", "equal budget" and
"equally costly": only CLAIM-562's note of 2026-11-05 (A's prediction),
CASE-215 (a fictional construction in A's assembly model, not an
organization), LEAD-183's run (CASE-tmp2a9lm, mechanical kinetic model) and
CLAIM-272 (equal action budgets and influence, a different claim). No
changelog fragment names LEAD-044.

## Done

- Coding rules written before the search: CODING-RULES.md.
- Search and coding: CODING.md. Three candidates coded.
  - AP RESt (Muralidharan and Sundararaman, NBER w15323): meets the
    standard. Equal-cost arms (Rs 10,000/school) at different places:
    individual bonus 0.27 SD against 0.09 SD for inputs.
  - Banerjee et al. BMJ 2010 (Seva Mandir camps): closest case; nested
    arms, cost per outcome only.
  - Zambia supply chain pilot: closest case; Vledder et al. behind
    Cloudflare (tandfonline, deepblue); read through Leung et al. 2016.

## Choices

- One case meets the standard, so no simulation is built.
- Readings filed per read-and-file: LIT, NOTE, THEORY for each of the
  three works read; Vledder et al. as an Unfetched LIT.
- Alternatives on AP RESt: a placement reading (lean) and a
  conditionality reading (counter), both filed.

## Next

- Register LITs, NOTEs, THEORYs.
- File the CASE (executed-study) and CLAIMs.
- Dated notes on LEAD-044, CLAIM-562, QUESTION-380; changelog fragment.
