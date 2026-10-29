---
status: Skimmed
paper: 'LIT-1216'
title: 'SEI CERT — Common Sense Guide to Mitigating Insider Threats, seventh edition'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in part on 2026-10-29 from the SEI's own PDF, linked from the
    library page the LIT names
    (https://sei.cmu.edu/documents/5777/5692_CSG_Book_20-optimized.pdf,
    175 pages, "Copyright 2022 Carnegie Mellon University", DM21-0782;
    the PDF's creation date is 2022-09-01); text extracted with
    pdftotext. Read in full: the front matter and executive summary, the
    history of the guide (Figure 1), the introduction with its data page,
    privacy and GDPR sections and "How to Use This Guide", the opening of
    Best Practice 1, and Best Practices 15 (separation of duties and
    least privilege), 21 (positive incentives) and 22 (learning from past
    incidents). Not read: Best Practices 2–14 and 16–20, the rest of 1,
    and the appendices. The data page (Figures 2–8) is charts; only the
    printed n values and the stated totals were taken from it, no other
    number.
date: '2026-10-29'
summary: >-
  A practitioners' guide of 22 best practices for insider risk, each
  with challenges, quick wins and mappings to NIST SP 800-53 and other
  standards, grounded in the CERT repository of more than 3,000 insider
  cases that ended in conviction or civil liability. Its separation of
  duties practice turns on collusion, and its positive-incentives
  practice argues, from three rated cases and a 23-response survey, that
  perceived organizational support lowers insider misbehaviour.
---
<!-- inactive-ok-file: CLAIM-359 LIT-1206 — Proposed, or Deferred and read only in part; cited as open or for what the part read covers -->

# NOTE-tmp3wx9h: SEI CERT — Common Sense Guide to Mitigating Insider Threats, seventh edition

## Contribution

It is the seventh edition of a guide first issued in 2005. It recasts
insider "threat programs" as insider risk management programs, adds a
twenty-second practice on learning from past incidents, and maps each
practice to NIST SP 800-53 Rev. 5, the NIST frameworks, ISO 27002, CIS
and the GDPR. Its evidence base is the CERT Insider Threat Incident
Repository.

## Key insight

From the parts read: insider risk is managed, not eliminated, and the
management is a balance. "Not all insiders can be stopped." Technical
forcing controls (separation, least privilege, monitoring) and positive
incentives that keep the workforce's goodwill are meant to work
together, because the same people are the threat and the mission.

## Key results

- **Definitions.** Insider threat: "the potential for an individual who
  has or had authorized access to an organization's critical assets to
  use their access, either maliciously or unintentionally, to act in a
  way that could negatively affect the organization". Insider risk: its
  impact and likelihood. Seven scenarios: IP theft, IT sabotage, fraud,
  misuse of authorized access, unintentional incidents, national
  security espionage, workplace violence.
- **Data.** The repository holds "over 3,000 cases of insider incidents
  in which the perpetrator was charged and convicted or found liable of
  a criminal or civil action", from public sources. The charts give
  n = 1,314 for incident types, 1,179 for financial impact and 1,515 for
  industry, so each breakdown covers under half the cases.
- **Best Practice 15.** Separation of duties divides functions "to limit
  the possibility that one workforce member could steal information or
  commit fraud or sabotage without the cooperation of others"; it is
  easily circumvented "if it is enforced by policy rather than by
  technical controls". Its first case: a motor-vehicles clerk and three
  accomplices issued over 1,000 fraudulent licences for more than five
  years, payment taken by one insider and processing by another. Its
  second: an executive director with access to both bank accounts and
  the accounting system issued himself cheques and altered the records.
  Mapped to AC-5 and AC-6.
- **Best Practice 21.** Positive incentives (job engagement, perceived
  organizational support, connectedness) "reduce the organization's
  baseline insider risk". Evidence: three incidents rated by three CERT
  researchers by consensus, in which perceived support was negative in
  all three, engagement in two and connectedness in one; and a survey of
  23 organizations in the SEI's OSIT group, reporting a statistically
  significant negative slope of −1.04 between perceived support and
  insider misbehaviour frequency. The guide says "it is impossible to
  draw general conclusions from this small number of cases".
- **Best Practice 22.** Keep an internal incident repository and share
  incident data; past incidents are limited to those "both detected and
  ... effectively investigated".

## Concepts

- **Insider risk management program (IRMP)**: "a designated set of
  capabilities and resources purposefully allocated to mitigate insider
  threat and manage insider risk"; formerly "insider threat program".
- **Trusted external entity**: a contractor or partner with authorized
  access.
- **Two-person rule**: two people must take part for a task to execute.

## Connections

The mappings tie it to SP 800-53 Rev. 5 (LIT-1206, NOTE-tmpgdnkh). Its
positive-deterrence argument extends Straub's 1998 deterrence model and
rests on Eisenberger's perceived-organizational-support scale and social
exchange theory.

## Bearing on the record

- **CLAIM-359 and CASE-108.** A41 named this research as the source of
  documented cases. Two things in the part read bear on the claim. The
  guide's own separation-of-duties case is a failure by collusion: four
  insiders split the steps the separation was meant to keep apart. That
  is CASE-108's "role-limited governance" failure, "coordination cost or
  collusion", observed. And Best Practice 21 states a version of the
  claim's trade-off from the practitioners' side: the CyLab survey it
  cites found concern that negative controls infringe rights, inhibit
  productivity, undermine trust and lose good staff, and its remedy is
  that positive incentives can make negative controls seem "more
  legitimate". The guide does not consider dissent or challenge to
  governance as a value to protect; its insider is a wrongdoer or a
  mistake-maker, never internal opposition. The repository, being
  convicted cases, also cannot contain the claim's harder case, a
  challenge that was legitimate.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- Fifteen of the twenty-two practices were not read.
- The case base is selected twice: public, and ending in conviction or
  liability. The guide notes the second limit itself in Best Practice
  22.
- The evidence for Best Practice 21 is three cases and 23 survey
  responses.
- **Errors and slips.** The GDPR is called "a directive" (it is a
  regulation). Footnote 10's list of EU members includes the United
  Kingdom, which left the EU in January 2020. The standards list cites
  "NIST Special Publication 800-53 Revision 5: Recommended Security
  Controls for Federal Information Systems and Organizations [NIST
  2015a]", the title of an earlier revision; Revision 5 is titled
  "Security and Privacy Controls for Information Systems and
  Organizations" and is dated 2020. The timeline (Figure 1) calls this
  edition "2021: Seventh Edition, Common Sense Guide to Managing Insider
  Risk", a title the document does not carry. Figures 15–18 each carry a
  second, stale caption ("Figure 6" to "Figure 9"), and Figure 18's
  extracted axis runs 0 to 8 for a scale labelled 1 to 5.

## Open questions

- Is the support–misbehaviour relation in Best Practice 21 more than the
  23-organization survey shows, and in which direction does it run?
