---
number: 189
status: Open
formerly:
- LEAD-tmpxrybg
title: 'Read the blameless post-incident practice and check the Tempe prosecution'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    A dated note added: the lead carried out on 2026-11-22, its readings
    and filings listed and what remains. No change of status, stage or
    title.
stage: idea
priority: medium
method:
- reading
- historical
tags:
- society-and-governance
- ethics
- software-engineering
date: '2026-11-19'
line:
- rightful-power
- organizational-normativity
advances:
- QUESTION-476
- CLAIM-750
- CLAIM-751
summary: >-
  Named in the curation entry of 2026-11-18 (062004). Filed by the backlog
  audit of 2026-11-19.
---
<!-- inactive-ok-file: CLAIM-751 LIT-2785 — Proposed, Unfetched; cited in the backlog audit of 2026-11-19 -->

# LEAD-189: Read the blameless post-incident practice and check the Tempe prosecution

## What it would do

Read Allspaw ([LIT-2785](../literature.d/LIT-2785.md), Unfetched behind a bot check), the SRE book's
Appendix D, Google's SRE workbook chapter on postmortems and Dekker
(2009), registering the last three; and find whether the Tempe prosecution
proceeded against the operator and not the company.

Where the record names it:

- The curation entry of 2026-11-18 (062004): "Whether criminal proceedings
  followed for the operator, and none for the company, would bear on
  [CLAIM-751](../claims.d/CLAIM-751.md)'s contrast"

## The works

- [LIT-2785](../literature.d/LIT-2785.md) (Unfetched): Allspaw 2012, "Blameless PostMortems and a Just
  Culture"

## What would count

A documented blameless practice that traces causes upstream answers part
of [QUESTION-476](../questions.d/QUESTION-476.md); proceedings against the operator alone support
[CLAIM-751](../claims.d/CLAIM-751.md)'s contrast.

## Note of 2026-11-22: carried out, and what remains
<!-- inactive-ok-file: THEORY-tmp9j928 THEORY-tmpm653d THEORY-tmpfdyu6 CLAIM-tmp20uni CLAIM-tmp64hmn CLAIM-tmpauu5r CASE-tmptkkgm ARG-tmpql8m1 ARG-tmp117cw — new; filed for this lead on 2026-11-22 -->
<!-- inactive-ok-file: LIT-tmp0on8b THEORY-2000 CLAIM-750 — Unavailable or Proposed; the paper not read, the theory whose promote_when is met and the claim advanced -->

Carried out on 2026-11-22 by a delegated worker (Claude, in this session), on the branch claude/lead-189-blameless-postmortem.

- **Read.** The SRE book's Appendix D, "Example Postmortem" (LIT-tmpnjnwq, NOTE-tmpdiani, THEORY-tmp9j928), and the SRE workbook's chapter 10, "Postmortem Culture: Learning from Failure" (LIT-tmpujx6j, NOTE-tmpf58r7, THEORY-tmpm653d), both in full from sre.google. For the prosecution, three NPR reports, read in full: the AP's report of the plea (LIT-tmpum8to, NOTE-tmpeb1f9, THEORY-tmpfdyu6), and, as supplements, the declination for Uber (LIT-tmp4sapc, NOTE-tmphxo80) and the charge (LIT-tmpca1pz, NOTE-tmpi1l0m).
- **The prosecution.** It proceeded against the operator and not the company. Prosecutors found "no basis for criminal liability for the Uber corporation" (March 2019); the operator was charged with negligent homicide (September 2020) and pleaded guilty to endangerment, with three years of supervised probation (July 2023). What this lead said would count, "proceedings against the operator alone support CLAIM-751's contrast", is met for the criminal process. CLAIM-tmp20uni files the contrast, with ARG-tmpql8m1; CLAIM-tmp64hmn objects that it is a contrast between the criminal law and the NTSB, since a settlement and the state's suspension of testing reached the company.
- **The blameless practice.** Neither Google text documents a postmortem that traces causes to decisions above the teams. The workbook's real exemplar names a staffing limit and routes no action item to it (CASE-tmptkkgm, ARG-tmp117cw, for CLAIM-750). The workbook puts questions about priorities set above the team in reviews across incidents, which CLAIM-tmpauu5r files as an objection to how CLAIM-750 is tested. So the other thing this lead said would count, "a documented blameless practice that traces causes upstream", is not found within a postmortem, and is left open across incidents.
- **Not read.** Allspaw (LIT-2785): the archived copy, tried once more, failed with a connection reset; it stays Unfetched. Dekker (2009), registered as LIT-tmp0on8b: Unavailable, no lawful free copy found.
- **For the owner.** The workbook reading meets THEORY-2000's `promote_when`. Whether CASE-tmptkkgm illustrates CLAIM-750 is filed with an alternative reading in the case.

What remains: Allspaw's text and Dekker (2009), if a copy is supplied; and evidence of what Google's cross-incident reviews find, which would settle CLAIM-tmpauu5r. No change of status or stage.
