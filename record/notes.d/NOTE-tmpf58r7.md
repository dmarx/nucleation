---
status: Read
paper: LIT-tmpujx6j
title: 'Rogers, Suriar, Lueder, Deo and Sudhakar — Postmortem Culture: Learning from Failure (workbook)'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read in full on 2026-11-22 from Google's open web edition,
    https://sre.google/workbook/postmortem-culture/, HTML converted to
    text: the chapter, both postmortems with their tables, the sections on
    organizational incentives and tools, and the footnote. Not read: the
    figures (images), the linked templates at
    g.co/SiteReliabilityWorkbookMaterials, and the third-party templates
    and tools it lists. Read by the filer, not a delegated reader; the
    quotes below were checked against that text on 2026-11-22.
date: '2026-11-22'
summary: >-
  Google's practical chapter on postmortem culture. A real outage
  (satellite machines sent to diskerase, 2014) is written up twice, badly
  and well; the good version blames "No individual or team", names a
  staffing limit among what went poorly, and assigns fourteen technical
  action items to engineers. Leaders are to model blamelessness; blameful
  questions to a manager and from a vice-president are redirected into
  questions about process. Repeated incidents prompt asking whether
  "feature velocity" is "trumping reliability fixes".
---
<!-- inactive-ok-file: CASE-tmptkkgm CLAIM-tmpauu5r CASE-335 — new or Proposed; the specimen and the objection filed from this reading, and the pilot it bears on -->
<!-- inactive-ok-file: CLAIM-750 CLAIM-742 CLAIM-905 THEORY-2000 — Proposed; the entries the reading bears on -->

# NOTE-tmpf58r7: Rogers, Suriar, Lueder, Deo and Sudhakar — Postmortem Culture: Learning from Failure (workbook)

## Contribution

Where the SRE book's chapter 15 (LIT-2784) states the norms, this chapter
shows them applied to one real postmortem and says how an organization
keeps them: by leaders' example, rewards, sharing, and response to signs
that the culture is failing. It is Google's own account, by its
practitioners.

## Key results

Quotations from the web edition (no page numbers; section names given).

- **Aim** (opening). "Our experience shows that a truly blameless
  postmortem culture results in more reliable systems". No data is given
  for it.
- **The bad postmortem** (Bad Postmortem). "Root cause: dylanfour@ ignored
  the automation setup and ran the cluster turnup logic manually"; "Due to
  careless ignorance"; an action item "sydneythree@ needs to learn proper
  cross-site handoff protocol". The critique: highlighting individuals
  "leads team members to become risk-averse because they're afraid of
  being publicly shamed. They may be motivated to cover up facts critical
  to understanding and preventing recurrence."
- **Ownership is accountability** (Missing ownership). "Declaring
  official ownership results in accountability, which leads to action."
- **The good postmortem: causes** (Root Causes and Trigger). "A
  longstanding input validation bug in the Traffic Admin server was
  triggered by the manual reexecution of a workflow". The manual run is
  attributed to a team: "When the Cluster Turnup team manually started
  another run of the workflow".
- **The good postmortem: a staffing limit named** (Things that went
  poorly, Recovery). ""The installer" has limited staffing. As a result,
  making changes is difficult and slow." Beside it, technical items
  ("Overly strict SSH timeouts", "A concurrency regression in
  Autoreplacer").
- **The good postmortem: action items** (Tables 10-8 to 10-12). Fourteen,
  in five themes, each with a priority, an engineer as owner and a bug:
  audits, input rejection, safety checks, an emergency stop, alerts, a
  reinstall protocol, tests. None addresses staffing, priorities or
  budgets.
- **What made it good** (Blamelessness). "No individual or team is blamed
  for the incident"; the root cause "Focuses on "what" went wrong, not
  "who" caused the incident"; action items "Are aimed at improving the
  system instead of improving people". (Depth) "Rather than only
  investigating the proximate area of the system failure, the postmortem
  explores the impact and system flaws across multiple teams."
- **A VP's rule** (Note). Ben Treynor Sloss: "all postmortems which follow
  a user-affecting outage must have at least one P[01] bug associated with
  them. I personally review exceptions."
- **A question to a manager, rewritten** (Use blameless language). The
  blameful version: "You're the manager; why aren't you making sure that
  everyone finishes the training?" The recommended one: "Maybe team
  members should be required to complete this training before joining the
  on-call rotation? ... Long term, we shouldn't really rely so much on
  training".
- **A VP's question, redirected** (Failing to reinforce the culture). "VP
  Ash: I know we are supposed to be blameless, but this is a safe space.
  Someone must have known beforehand this was a bad idea, so why didn't
  you listen to that person?" The response: "maybe we ask generically if
  there were any warning signs we could have heeded". The principle:
  "Individuals act in good faith and make decisions based on the best
  information available. Investigating the source of misleading
  information is much more beneficial to the organization than assigning
  blame."
- **Upstream questions, outside the postmortem** (Repeating incidents).
  "Is feature velocity trumping reliability fixes?"; "Is the faulty
  service overdue for a refactor?"; and "If you uncovered a systemic
  process or technical problem, it's time to take a step back and
  consider the overall service health." (Lacking time to write
  postmortems) "allow teams adequate time to implement the associated
  action plan."
- **Who governs the review** (Postmortem checklist; Conduct cross-team
  reviews). "Ensure action items are vetted and approved by the technical
  leads of the service." "A cross-functional group of developers, SREs,
  and organizational leaders reviews the overall postmortem process."
- **Leaders** (Organizational Incentives). "Ideally, senior leadership
  should support and encourage effective postmortems"; "engineering
  leaders should consistently exemplify blameless behavior".

## Assumptions

- That blameless review yields more reliable systems, asserted from
  experience.
- That people "act in good faith" and decide "based on the best
  information available", so that the useful question about a decision is
  what misled it.
- That "the system" can be repaired by engineering action items, owned by
  engineers.

## Concepts

- Ownership as accountability, distinct from blame.
- Blameful and blameless language.
- Postmortem culture failures: avoiding association, failing to reinforce,
  lacking time, repeating incidents.
- Postmortem analytics across incidents (Requiem).

## Bearing on the record

- **QUESTION-476** (bears on). The first half is answered by design as in
  chapter 15, with the gloss that ownership is "accountability, which
  leads to action". On the second half the chapter is the best evidence
  the record has from the practice itself, and it points both ways:
  - *toward losing provenance*: the good postmortem names a staffing
    limit and gives it no action item; the manager's question about
    training becomes a question about the rotation's rules; the VP's
    question about who was not listened to becomes a generic one about
    warning signs. In each, a matter that would reach a decision-maker is
    recast as a matter of process.
  - *toward keeping it elsewhere*: the chapter routes upstream questions
    ("Is feature velocity trumping reliability fixes?") to a review of
    repeated incidents and to a "cross-functional group ... and
    organizational leaders", and a vice-president reviews postmortems
    that lack a priority bug. Provenance may be kept, if at all, by
    channels beside the single postmortem.
- **CLAIM-750** (bears on, both ways). The good postmortem fits the
  prediction: its action items stay at the engineering teams, and the one
  contributing condition above engineering action, staffing, goes without
  one. CASE-tmptkkgm files it as a specimen. The blameless-language
  examples fit the mechanism: the norm against "indicting any individual
  or team" also turns questions to managers into questions about process.
  Against the claim as operationalized, the chapter's own channels for
  upstream questions sit outside the postmortem, so a coding of
  postmortems' action items may miss them: CLAIM-tmpauu5r files that
  objection. Whether "the installer" staffing lies above the reviewing
  team's authority is not stated: it may be a peer team's.
- **THEORY-2000** (meets its promote_when). Its `promote_when` asks for a
  reading of the chapter or of "Google's later SRE workbook on the same
  practice" confirming that a blameless postmortem identifies
  contributing causes and follow-up actions without indicting any
  individual or team, and that the reason given is that blame keeps people
  from bringing issues to light. This reading confirms both: "No individual
  or team is blamed", and individuals named "may be motivated to cover up
  facts critical to understanding and preventing recurrence". The reading
  is by other authors (one, Lueder, in common), of another book. Promotion
  is left to the owner (dated note on THEORY-2000).
- **CLAIM-742** (corroborates, as THEORY-2000 does; written on the
  THEORY). "Declaring official ownership results in accountability, which
  leads to action" separates accountability from blame in the practice's
  own words.
- **CLAIM-905 and CASE-335** (parallel). The pilot's finding, that public
  postmortems' traces stop at the engineering group, matches the good
  postmortem here, which is not in the pilot's corpus.

## Limitations

- One postmortem, chosen by Google to show good practice, with values
  redacted and parts elided. It is an exemplar, not a sample.
- "Our experience shows" is unsupported in the chapter: no data on
  reliability, on how often action items close, or on what levels they
  reach.
- The chapter's own argument has a gap that matters here: it says
  investigating "the source of misleading information" beats assigning
  blame, but it does not say who investigates when the source is a
  decision of the people who govern the review.
