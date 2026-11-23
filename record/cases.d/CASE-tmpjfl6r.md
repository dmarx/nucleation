---
status: Proposed
title: 'Open evaluations coded, under rules written before coding, for interventions of equal budget at different places in one organization: one meets the standard, a school system''s randomized arms of equal yearly cost in which teacher bonuses raised test scores three times as much as an extra teacher or materials, and two come closest, an immunisation trial with nested supply and demand arms and a supply chain pilot whose costs were not reached'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed by the lead run of 2026-11-23. The coding rules, written before
    the search, the search as run and the coding with its passages are
    under scratch/studies/lead-044/.
standing: documented
kind: executed-study
tags:
- social-science
- society-and-governance
- operations-research
- complex-systems
date: '2026-11-23'
line:
- realizability
illustrates:
- CLAIM-562
bears_on:
- QUESTION-380
reported_in:
- NOTE-tmphqrk0
- NOTE-tmpz3ek2
- NOTE-tmpmco2w
summary: >-
  CLAIM-562 holds, from mechanical systems, that where an intervention
  acts in a constraint structure can predict success better than how much
  intervention there is. A search of open evaluations for its
  organizational test, coded under six criteria fixed before the search,
  found one case that meets the standard: in Andhra Pradesh's randomized
  evaluation of 500 government primary schools, an individual teacher
  bonus, an extra contract teacher and a block grant for materials each
  cost about Rs 10,000 per school a year, and the bonus raised test scores
  by 0.27 SD against 0.09 SD for the two inputs. Place there is confounded
  with conditionality. Two cases come closest: Seva Mandir's immunisation
  camps, where the demand-side incentive was only ever added to the
  supply-side camps, and Zambia's supply chain pilot, two arms at two
  tiers whose costs are in a paper not reached. No case tests whether
  adding an intervention can make an organization fail. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-tmpqrmoy CLAIM-tmphbmpy CLAIM-tmpb125k THEORY-tmpmwhm1 THEORY-tmp7jput THEORY-tmp8j9f4 LIT-tmpuedwt — new; filed by the lead run of 2026-11-23 -->

# CASE-tmpjfl6r: Open evaluations coded, under rules written before coding, for interventions of equal budget at different places in one organization: one meets the standard, a school system's randomized arms of equal yearly cost in which teacher bonuses raised test scores three times as much as an extra teacher or materials, and two come closest, an immunisation trial with nested supply and demand arms and a supply chain pilot whose costs were not reached

## The study

LEAD-044 asks for "documented interventions of similar cost at different
places in one organization", effects differing by location to test
CLAIM-562. Before searching, six criteria were fixed
(`scratch/studies/lead-044/CODING-RULES.md`):

| | Criterion | "yes" means |
|---|---|---|
| C1 | One organization | arms act on one organization or on randomized units of it |
| C2 | Different locations | arms act at different tiers, steps, roles or sides through which one outcome is produced; dose or timing at one place is "no" |
| C3 | Equal budget | costs reported per arm in one unit, the larger at most 1.5 times the smaller; per outcome only is "partial" |
| C4 | Common outcome | one outcome reported for every arm |
| C5 | Identification | randomized or quasi-experimental with a comparison group |
| C6 | Location as the reason | the source says, or its results show, that the difference is due to where the arm acts; "partial" if only this filing says so |

A case **meets the standard** with C1, C2, C3, C4 and C5 "yes"; it is a
**closest case** with C1, C2 and C4 "yes" and C3 or C5 "partial". The
search ran on Europe PMC and OpenAlex; three candidates were read and
coded. The passages behind each code are in `CODING.md`.

## The coding

| Case | C1 | C2 | C3 | C4 | C5 | C6 | Verdict |
|---|---|---|---|---|---|---|---|
| Andhra Pradesh schools, inputs against incentives (THEORY-tmpmwhm1) | yes | yes | yes (three arms) | yes | yes | partial | meets the standard |
| Seva Mandir immunisation camps (THEORY-tmp7jput) | yes | partial | partial | yes | yes | yes | closest of its kind, outside the rules (C2) |
| Zambia supply chain pilot (THEORY-tmp8j9f4) | yes | yes | no, unread | yes | partial | partial | closest of its kind, outside the rules (C3) |

**Andhra Pradesh.** Five cells of 100 schools. Two-year effects on test
scores, and yearly spending per school:

| Arm | Acts on | Spending | Effect |
|---|---|---|---|
| Extra contract teacher | staff | Rs 10,000 | 0.09 SD (the two inputs pooled) |
| Block grant | materials | Rs 10,000 | (pooled above) |
| Individual bonus | effort of the teachers already there | about Rs 10,000 | 0.27 SD |
| Group bonus | the same, rewarded jointly | about Rs 6,000 | 0.16 SD |

At equal spending the effect differs threefold by where the money enters.
The group bonus falls outside the 1.5 bound and is not used for the
equal-budget comparison.

**Seva Mandir.** Camps alone 18 % fully immunised, camps with incentives
39 %, control 6 %; $56 against $28 per fully immunised child. The demand
side was only ever added to the supply side, so this is a superset
against a set, not two places at one budget.

**Zambia.** Two arms at two tiers: picking, packing and stock at the
district, or packages made at the national warehouse and cross-docked at
the district; the second had fewer days without stock. The costs are in
Vledder et al. (LIT-tmpuedwt), which showed a Cloudflare challenge at
both of its copies.

## What it can show

- **That the organizational comparison CLAIM-562 needs exists, once.**
  One evaluation meets a standard fixed in advance, and its effects
  differ threefold at equal cost. Whether the difference is one of place
  is read two ways, both filed: as place, the arm acting on effort rather
  than on staff or materials (CLAIM-tmpqrmoy, the filer's lean); or as
  instrument, conditional pay rather than unconditional resources, which
  the design cannot separate from place (CLAIM-tmphbmpy).
- **Nothing on the second half of CLAIM-562.** No coded case has a
  larger set of interventions doing worse than a smaller one;
  CLAIM-tmpb125k disclaims it.

## Limits

- A small search: three candidates read. Others likely exist; the rules
  and the coding sheet make adding them mechanical.
- The location criterion (C2) is a judgement about what counts as a
  different place in an organization's structure. The rules were written
  before coding; the judgement in each case is quoted in `CODING.md`.
- Count of interventions, the other half of CLAIM-562's comparison, is
  held fixed at one per arm here: the cases compare places at one
  budget, not place against amount.
