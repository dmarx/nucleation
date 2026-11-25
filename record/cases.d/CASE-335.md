---
number: 335
status: Proposed
formerly:
- CASE-tmp1ya4r
title: 'Postmortems and Chemical Safety Board reports'
statement: >-
  A pilot coding of 30 public postmortems of software incidents and 10
  Chemical Safety Board investigation reports, under a codebook fixed in
  advance, finds causes naming decisions above the engineering team in 2 of
  the postmortems and 7 of the reports, and action items above it in 4 and
  9; one coder of the same model family as the claim it tests
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-119 as a delegated
    lead worker. Codebook, sample log, coded items and scripts are committed
    under scratch/studies/lead-119/.
standing: documented
kind: executed-study
tags:
- society-and-governance
- software-engineering
date: '2026-11-22'
line:
- rightful-power
- organizational-normativity
illustrates:
- CLAIM-750
bears_on:
- QUESTION-476
draws_on:
- THEORY-2000
summary: >-
  A pilot of the study proposed as [CASE-293](CASE-293.md), run for [LEAD-119](../leads.d/LEAD-119.md). Internal arm:
  30 postmortems drawn at random (seed 119) from Dan Luu's public list of
  postmortems, each the organization's own account of its own incident.
  Independent arm: the 10 most recent completed investigations of the U.S.
  Chemical Safety Board with final reports. Each was coded for the highest
  organizational level whose decision a contributing cause names (0
  unattributed to 5 outside authority, 3 being management decisions on
  priorities, staffing, schedules or cross-team policy) and the highest level
  an action item targets. Causes at level 3 or above: 2 of 30 postmortems
  (7%) against 7 of 10 reports; level 4 or above: 0 against 5. Action items
  at 3 or above: 4 of 30 (13%) against 9 of 10. Under the rule fixed before
  coding, [CLAIM-750](../claims.d/CLAIM-750.md)'s prediction holds in the pilot. The arms differ in
  domain (software outages against fatal or serious chemical accidents) as
  well as in who reviews, and there was one coder, of the same model family
  that wrote [CLAIM-750](../claims.d/CLAIM-750.md) and the codebook, knowing the prediction; the pilot
  is not independent. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-750 CASE-293 THEORY-2000 CASE-292 CLAIM-719 — Proposed; the claim the pilot tests, the study it pilots, the reading whose format it uses, and the NTSB case -->
<!-- inactive-ok-file: CLAIM-905 — new; filed with this case -->

# CASE-335: Postmortems and Chemical Safety Board reports

## What was done

[LEAD-119](../leads.d/LEAD-119.md) asks for [CASE-293](CASE-293.md) to be run: code postmortems for the highest organizational level named among their contributing causes and for action items above the reviewing team's authority, and compare internal reviews with independent ones. This is a pilot of about the size the lead's large estimate allows: 30 internal and 10 independent documents.

**Fixed before coding** (scratch/studies/lead-119/codebook.md, committed before the first item was coded):

- **Internal arm.** Every entry link in the sections "Config Errors" through "Uncategorized" of Dan Luu's public list of postmortems, deduplicated and shuffled with seed 119, taken in order. An item was included if it fetched without a bot check, was the organization's own account of its own incident, and gave at least 300 words. 30 were included. The exclusions are logged in sample_log.jsonl. They include every web.archive.org link (the archive was unreachable from the session), one 403 from GitHub, and four pages that failed the inclusion rules: an engineer's conference paper, an encyclopedia article, an external review the organization had commissioned, and a page that now serves a blog index.
- **Independent arm.** The CSB's completed investigations in listing order, most recent first, taking each with a final report PDF, which gave 10. The CSB was chosen over the NTSB for the pilot because it has a plain listing and one report format. It sits outside the companies it investigates, and its findings may not be used as evidence in suits for damages.
- **Codes.** H, the highest level whose decision or practice a cause names: 0 unattributed ("the system", a component), 1 operator, 2 team or engineering practice, 3 management (priorities, schedules, staffing, resourcing, cross-team policy), 4 organizational leadership (budget, strategy, safety culture, corporate oversight, the safety management system), 5 an outside authority (regulator, standards body). A, the highest level an action item targets, on the same scale. SYS, whether any cause is stated as "the system" or a gap with no decision named. A vendor flag.
- **Decision rule.** The prediction holds in the pilot if internal H >= 3 and A >= 3 are each under 25% and the independent rates exceed them by 30 points or more. The defeater's direction is met if the internal rates are within 15 points of the independent ones, or above 50%. Anything else is inconclusive.

One rule was sharpened during coding, after the tenth item, and applied from then on consistently with the codes already given. Re-prioritisation counts as A = 3 only when it moves resources away from other work: a freeze, engineering functions moved, a change to the roadmap or to staffing plans, a company-wide investment. Saying that repair items are "prioritised" counts as 2.

## Result

| measure | internal (n = 30) | independent (n = 10) |
|---|---|---|
| cause at H >= 3 | 2 (7%) | 7 (70%) |
| cause at H >= 4 | 0 | 5 (50%) |
| action item at A >= 3 | 4 (13%) | 9 (90%) |
| action item at A >= 4 | 0 | 8 (80%) |
| "the system" language (SYS) | 12 (40%) | 2 (20%) |
| vendor named | 9 (30%) | 1 (10%) |

26 of the 30 postmortems stop at the engineering group's own design, testing, tooling or procedure (H = 2). The two that name a decision above it are Cloudflare's control-plane outage of 2023 ("We were also far too lax about requiring new products and their associated databases to integrate with the high availability cluster. Cloudflare allows multiple teams to innovate quickly") and Buildkite's outage of 2016, which names a push to cut the AWS bill: "We paused product development ... Since we felt pressure to get these changes out sooner rather than later, we didn't do our due diligence". The CSB reports name corporate governance (HEF Groupe's "ineffective corporate governance"), corporate oversight (Marathon's "inadequate oversight of the Martinez facility"), an unfunded capital project (Honeywell), and regulatory gaps ("insufficient regulatory coverage of reactive hazards", Bio-Lab). They address recommendations to parent companies, to EPA and OSHA, and to standards bodies. One CSB report, PEMEX Deer Park, stops at site procedures (H = 2, A = 2).

Under the rule fixed in advance, [CLAIM-750](../claims.d/CLAIM-750.md)'s prediction holds in the pilot.

**An observation not in the codebook.** The four internal postmortems with action items above the team were written by the organization's senior leadership. Cloudflare's was by its CEO, whose byline the page shows. Buildkite's was by its founders ("Tim, Sam and I"). GitHub's of October 2018 was by Jason Warner and Roblox's by Daniel Sturman. The coder gives those two authors' roles (CTO) from memory; the pages read do not state them. This fits [CLAIM-750](../claims.d/CLAIM-750.md)'s mechanism: the trace reaches as high as the authority of whoever writes it. But it was noticed after coding, and it was not coded for the other 26 items.

## What it cannot show

- **Not independent.** One coder: the assistant (Claude, Opus 5.5), the same model family that wrote [CLAIM-750](../claims.d/CLAIM-750.md), [CASE-293](CASE-293.md) and the codebook, knowing the predicted result. There was no second coder and no agreement measure.
- **The arms differ in domain.** The internal arm is software outages and the independent arm fatal or serious chemical accidents. The difference in level named may come from the domain, from the severity, or from the publication genre, as much as from who reviews. [CASE-293](CASE-293.md)'s own design problem, selection by publication, is untouched: published postmortems are edited for customers.
- **Coding depth.** The postmortems were coded from passages located by keyword in the stripped page text, not read end to end. The CSB reports were coded from the cause statement, the summary findings and the recommendations' addressees, not the technical body. Some codes are low-confidence and say so in coded.jsonl: two bug-hunt stories, and Okta's investigation, where no action items were found in the text read.
- **The scale favours the independent arm on A.** A recommendation to a regulator or a standards body scores 5 by construction, and internal postmortems have no such addressee. The difference holds without it: 7 of 10 CSB reports address the company at level 3 or above.
- **Completion is not measured.** Whether action items above the team were carried out, the measure [CLAIM-750](../claims.d/CLAIM-750.md) and [CLAIM-719](../claims.d/CLAIM-719.md)'s note of 2026-11-18 need, is not in any document coded.
- **NTSB.** NTSB reports are not in the pilot. The Tempe report ([CASE-292](CASE-292.md)) was not re-coded.

The pilot's finding, with its limits, is filed as [CLAIM-905](../claims.d/CLAIM-905.md). Units follow the postmortem format of the SRE chapter ([THEORY-2000](../theory.d/THEORY-2000.md)): contributing causes and action items.
