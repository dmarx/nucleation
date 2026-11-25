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

- Coding rules written before the search: CODING-RULES.md (unamended).
- Search and coding: CODING.md. Three candidates coded.
  - AP RESt (Muralidharan and Sundararaman, NBER w15323): meets the
    standard. Equal-cost arms (Rs 10,000/school) at different places:
    individual bonus 0.27 SD against 0.09 SD for inputs.
  - Banerjee et al. BMJ 2010 (Seva Mandir camps): closest case; nested
    arms, cost per outcome only.
  - Zambia supply chain pilot: closest case; Vledder et al. behind
    Cloudflare (tandfonline, deepblue); read through Leung et al. 2016.
- Filed:
  - LIT-tmpnoa89, NOTE-tmphqrk0, THEORY-tmpmwhm1 (Muralidharan and
    Sundararaman).
  - LIT-tmpiih9k, NOTE-tmpz3ek2, THEORY-tmp7jput (Banerjee et al.).
  - LIT-tmpa48v2, NOTE-tmpmco2w, THEORY-tmp8j9f4 (Leung et al., stand-in).
  - LIT-tmpuedwt (Vledder et al., Unfetched).
  - CASE-tmpjfl6r (executed study, documented).
  - CLAIM-tmpqrmoy (thesis, placement reading; lean), CLAIM-tmphbmpy
    (counter, instrument reading), CLAIM-tmpb125k (disclaimed: adding can
    hurt is not shown).
  - Dated notes on LEAD-044, CLAIM-562, QUESTION-380.
  - Changelog fragment record/changelog.d/lead-044.md.
- Checks: frontmatter parses, titles carry no code, H1 matches title,
  excuses used and complete (a local script, not luria lint).

## Choices

- One case meets the standard, so no simulation is built.
- Readings filed per read-and-file: LIT, NOTE, THEORY for each of the
  three works read; Vledder et al. as an Unfetched LIT.
- Alternatives on AP RESt: a placement reading (lean) and an instrument
  reading (counter), both filed; the owner chooses.
- bears_on QUESTION-380 for the case and claims, the open question on
  predicting a local intervention's effect from the constraint structure.

## Next (for the owner or a later run)

- Read the companion papers on the contract-teacher and block-grant arms
  (Muralidharan and Sundararaman, "Contract Teachers"; Das et al., "School
  Inputs, Household Substitution, and Test Scores") to separate the two
  input arms.
- Reach Vledder et al. (SSRN 2585671 not tried) for the pilot's costs.
- Widen the search under the same rules.
