# LEAD-044 coding rules

Written on 2026-11-23, before any search for cases. Not to be changed after
coding begins; a rule found wrong is amended below with a dated note, and
every case already coded is recoded under both versions.

## What a case is

A documented comparison, in a public evaluation report or open-access study,
of two or more interventions made in one organization (or in a set of
comparable units of one organization: facilities of one health system,
schools of one ministry, districts of one supply chain).

## Criteria (each coded yes / partial / no, with the passage)

- **C1. One organization.** The arms act on the same organization or on
  randomized or matched units of it.
- **C2. Different locations.** The arms act at different places in the
  organization's structure of constraints: a different tier, step, role or
  side (supply or demand) through which the same outcome is produced. Arms
  that differ only in dose, timing or delivery style at the same place are
  "no".
- **C3. Equal budget.** Costs of each arm are reported, by the source, in a
  common unit, and the larger is no more than 1.5 times the smaller
  ("yes"); costs reported but further apart, or equalized only per unit of
  outcome ("partial"); no costs ("no").
- **C4. Common outcome.** The arms are compared on one outcome measure the
  source reports for each.
- **C5. Identification.** Randomized, or a stated quasi-experimental design
  with a comparison group ("yes"); before and after only ("partial"); none
  ("no").
- **C6. Location named as the reason.** The source itself says, or its
  results directly show, that the difference in effect is due to where the
  arm acts in the structure (for example, which constraint binds). Coded
  "partial" if only this filing's reading puts it so.

## Verdict

- **Meets the lead's standard**: C1, C2, C4 and C5 "yes", and C3 "yes".
- **Closest case**: C1, C2, C4 "yes", and C3 or C5 "partial".
- **Not a case**: anything else.

## What a case shows about CLAIM-562

- **Placement.** Effects differ by location at (near) equal budget:
  supports the first half; equal effects at equal budget and different
  locations tell against it.
- **Adding can hurt.** An arm that is another arm plus a further component
  does worse on the common outcome: supports the second half. Coded only
  where such nested arms exist.

## Search rules

- Lawful copies only: Europe PMC REST API, PMC, arXiv, author and
  institution pages, open-access journals, public evaluation reports
  (World Bank Open Knowledge Repository, 3ie, J-PAL, government sites).
- Stop at any bot check, captcha, 403, 429 or paywall; record it.
- No email address in any request.
- Candidates are searched by these phrases: "cost-equivalent arms",
  "equal cost" with "randomized" and "health system" or "supply chain";
  "bottleneck" with "randomized" and "organization"; "supply-side versus
  demand-side" with "cost per"; multi-arm trials of health-system tiers.
