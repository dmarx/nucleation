---
status: Read
paper: LIT-tmpo6c2h
title: 'Lunney and Lueder — Postmortem Culture: Learning from Failure'
version: 1
history:
- version: 1
  date: '2026-11-18'
  note: >-
    Read in full on 2026-11-18 from Google's open web edition,
    https://sre.google/sre-book/postmortem-culture/, HTML converted to
    text: the chapter and its four footnotes. Not read: Appendix D
    (Example Postmortem), which the chapter points to, and chapter 16
    (Tracking Outages). Read by the filer, not a delegated reader; the
    quotes below were checked against that text on 2026-11-18.
date: '2026-11-18'
summary: >-
  Google's statement of blameless postmortem practice. A postmortem
  records an incident, its root causes and follow-up actions; it must
  identify "the contributing causes of the incident without indicting any
  individual or team", because under blame "people will not bring issues to
  light for fear of punishment". It is reviewed by senior engineers and
  shared widely, and the practice is kept up by reward and by asking teams
  how the process could improve. Norms and practice, with no data on what
  postmortems trace or fix.
---
<!-- inactive-ok-file: LIT-tmpwev6r — Unfetched; the post the chapter cites -->
<!-- inactive-ok-file: THEORY-tmpuc245 CLAIM-tmp5g7xc CLAIM-tmpx4kjt CASE-tmpw9202 — new; the theory filed from this reading and the entries it bears on -->
<!-- inactive-ok-file: CLAIM-742 CLAIM-719 CLAIM-707 — Proposed; the entries the reading bears on -->

# NOTE-tmpu2cx9: Lunney and Lueder — Postmortem Culture: Learning from Failure

## Contribution

The practitioners' own account of blameless postmortems in a large
software organization: when to write one, what it must contain, the norm
against blame and its reason, review, sharing, and how the culture is kept
up. It is the published statement that most software organizations cite
for the practice.

## Key results

Quotations from the web edition (no page numbers).

- **What a postmortem is.** "a written record of an incident, its impact,
  the actions taken to mitigate or resolve it, the root cause(s), and the
  follow-up actions to prevent the incident from recurring." Its goals:
  that "all contributing root cause(s) are well understood, and,
  especially, that effective preventive actions are put in place".
  "Writing a postmortem is not punishment".
- **Blameless.** "For a postmortem to be truly blameless, it must focus on
  identifying the contributing causes of the incident without indicting any
  individual or team for bad or inappropriate behavior. A blamelessly
  written postmortem assumes that everyone involved in an incident had good
  intentions and did the right thing with the information they had."
- **Why.** "If a culture of finger pointing and shaming individuals or
  teams for doing the "wrong" thing prevails, people will not bring issues
  to light for fear of punishment." And: "An atmosphere of blame risks
  creating a culture in which incidents and issues are swept under the rug,
  leading to greater risk for the organization" (citing [Boy13]).
- **The object is the system.** "When postmortems shift from allocating
  blame to investigating the systematic reasons why an individual or team
  had incomplete or incorrect information, effective prevention plans can
  be put in place. You can't "fix" people, but you can fix systems and
  processes".
- **Origin claimed.** "Blameless culture originated in the healthcare and
  avionics industries where mistakes can be fatal." No source is given.
- **Review.** Senior engineers assess drafts; criteria include "Was the
  root cause sufficiently deep?" and "Is the action plan appropriate and
  are resulting bug fixes at appropriate priority?" "An unreviewed
  postmortem might as well never have existed."
- **Who keeps it up.** "senior management's active participation in the
  review and collaboration process", though "blameless postmortems are
  ideally the product of engineer self-motivation"; writing them should be
  rewarded "through individual and team performance management".
- **The process revises itself.** "We regularly survey our teams on how the
  postmortem process is supporting their goals and how the process might be
  improved."
- **Outcome claimed.** "thanks to our continuous investment in cultivating
  a postmortem culture, Google weathers fewer outages". No figures.

## Assumptions

The incidents are failures of a technical service run by the organization
that reviews them. Review is internal: the authors, the reviewers and
senior management belong to the same company. The good faith of those
involved is assumed by rule ("assumes that everyone involved ... had good
intentions"), not found.

## Concepts

- **Postmortem**: the written record above.
- **Blameless**: identifying contributing causes without indicting any
  individual or team.
- **Root cause(s)**, used in the plural beside "contributing causes".
- **Action items / follow-up actions**: what the postmortem commits to
  doing.

## Bearing on the record

Filed as THEORY-tmpuc245.

- **QUESTION-476.** The chapter is the practice the question asks about,
  in its own words. It keeps correction ("effective preventive actions")
  and gives up blame, on a stated ground: disclosure. On the question's
  second half it says only that the trace runs to "the systematic reasons
  why an individual or team had incomplete or incorrect information". It
  says nothing about decisions above the reviewing team, such as staffing,
  deadlines or budgets, and its norm covers teams as well as individuals.
  Whether postmortems reach those decisions is not shown.
- **CLAIM-742** (blame is not accountability). A documented organizational
  practice that keeps correction while withholding blame, with the ground
  stated: corroborates, as a practice that exists, not as evidence that it
  works.
- **CLAIM-tmp5g7xc** (the reviewing body's authority as the trace's limit).
  The chapter's design fits the claim's premise: review is internal, by
  senior engineers with senior management taking part, and blame of any
  team is excluded. It does not test the prediction.
- **CLAIM-719.** The survey of teams on the postmortem process is a
  practice that revises the mechanism of review itself, a small instance
  of second-order responsiveness. The chapter gives no figures on whether
  action items are completed (see CLAIM-719's note of 2026-11-18).
- **CASE-tmpw9202** takes its units, contributing causes and action items,
  from the format described here.

## Limitations

- Self-description by the practising organization, with no evaluation and
  no data.
- The claim that blameless culture "originated in the healthcare and
  avionics industries" is unsourced here.
- Internal review only; nothing on an independent investigator.
- Appendix D, the example postmortem, was not read.
