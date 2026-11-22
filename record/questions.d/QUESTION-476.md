---
number: 476
formerly:
- QUESTION-tmp2t6ve
status: Open
title: 'Does blameless post-incident practice in engineering keep accountability while giving up blame, and if it does, does it keep or lose the upstream provenance of an incapacity that blame supplies?'
version: 5
history:
- version: 2
  date: '2026-11-17'
  note: >-
    Reading of Shoemaker (2019) filed with bears_on this question:
    protest under answerability without angry blame under
    accountability is a model of a practice that gives up one kind of
    blame and keeps another. The NTSB's Tempe report and Elish (2019)
    read and filed with bears_on this question; the Tempe case is
    filed as a documented specimen bearing on it.
- version: 3
  date: '2026-11-18'
  note: >-
    Takes the line rightful-power first, as one of its root questions;
    its earlier lines (organizational-normativity, distributed-agency)
    are kept after it. No other change.
- version: 4
  date: '2026-11-18'
  note: >-
    Readings of blameless culture filed: the SRE chapter, Cook, Dekker
    and Nyce, and 49 U.S.C. 1154, each with bears_on this question; two
    claims and a proposed study filed in answer, with bears_on. No change
    of status or title.
- version: 5
  date: '2026-11-22'
  note: >-
    A dated note added: the SRE example postmortem, the SRE workbook
    chapter and the reports of the Tempe prosecution read for LEAD-189,
    each with bears_on this question; a claim, two objections and a
    specimen filed in answer. No change of status or title.
tags:
- society-and-governance
- ethics
- software-engineering
date: '2026-11-17'
line:
- rightful-power
- organizational-normativity
- distributed-agency
refines:
- QUESTION-470
summary: >-
  The owner's, from U48 of the exchange "Assess Depp Heard Abuse"
  (2026-11-17), its last turn: ""blameless culture" in modern
  engineering could be an interesting case for analysis here". The
  exchange ends there; A never answered, and no work was named. The
  question puts the owner's suggestion to the two claims of the owner's
  U47 it bears on: that accountability is not blame ([CLAIM-742](../claims.d/CLAIM-742.md)) and
  that blame supplies provenance for holding upstream actors accountable
  ([CLAIM-733](../claims.d/CLAIM-733.md)). The suggestion is the owner's; the wording of the
  question is the filer's (Claude, in this session), and adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-707 — Proposed or Open; filed from the first share of the same exchange (PR 510) and reconciled with this filing on 2026-11-18 -->
<!-- inactive-ok-file: CLAIM-717 CLAIM-733 CLAIM-742 TERM-127 — filed from the exchange "Assess Depp Heard Abuse" (2026-11-17), new and Proposed -->
<!-- inactive-ok-file: THEORY-144 — Proposed; the record's nearest entries, cited with their standing -->

# QUESTION-476: Does blameless post-incident practice in engineering keep accountability while giving up blame, and if it does, does it keep or lose the upstream provenance of an incapacity that blame supplies?

## Why it is a question

The owner's U48, the last turn of the exchange "Assess Depp Heard Abuse"
(https://chatgpt.com/share/6afcb46d-83a8-83e9-9c85-4a0c3604405b), 2026-11-17:

> "blameless culture" in modern engineering could be an interesting case for analysis here

**The exchange ends here, with no answer.** No assistant turn follows U48,
no source is named, and nothing in the exchange discusses blameless
culture, post-incident review or "just culture" before it. The question is
therefore the owner's prompt, put in the terms of the owner's U47, the turn
it answers to:

- **Accountability without blame** ([CLAIM-742](../claims.d/CLAIM-742.md)). The owner: "perhaps
  "blame" and "accountability" aren't the same thing." A blameless
  review is, on its face, a practice that keeps correction (find what
  failed, repair it, prevent recurrence) while withholding blame from the
  people involved. If it works, it is a real instance of correction whose
  grounds are not those of blame.
- **Blame as provenance** ([CLAIM-733](../claims.d/CLAIM-733.md)). The owner: ""blame" gives us
  provenance for holding upstream actors accountable as well." A practice
  that refuses to blame anyone may also stop tracing whose decisions
  produced the conditions of the failure. Or it may trace them better,
  because people report what happened when they are not punished for it.
  Which of these happens is the open part.

## What would count as an answer

- **Keeps correction and provenance:** a documented practice in which
  reviews without individual blame still trace contributing decisions
  upstream (who set the staffing, the deadline, the tooling, the review
  procedure) and lead to repair there. That would show the owner's two
  claims separable in practice: provenance without blame.
- **Keeps correction, loses provenance:** evidence that blameless reviews
  stop at the system as an impersonal cause, so that decisions by those who
  govern the system escape the account. That would be the failure A110 §8
  calls "blame displacement" turned round: no one is blamed, and the
  conditions some actors set are not repaired ([CLAIM-717](../claims.d/CLAIM-717.md)).
- **Neither:** evidence that "blameless" in practice relocates blame, for
  example to the person who did not follow the process, so that it is not
  an instance of accountability without blame at all.

## Sources, not from the exchange

The exchange names none. Candidate sources, offered by the lead filer and
not by the exchange, for whoever takes this up: John Allspaw's "Blameless
PostMortems and a Just Culture" (Etsy Code as Craft, 2012); Sidney Dekker's
*Just Culture*; and the chapter "Postmortem Culture" in Google's *Site
Reliability Engineering*. None is registered on the record, and none is
cited here as evidence.

## How it sits with the record

Nothing on the record holds blameless culture, post-incident review or just
culture. The nearest held material is in safety science: [THEORY-144](../theory.d/THEORY-144.md)
(Rasmussen's drift toward the boundary of acceptable performance, whose body
says it does not claim "that individuals are blameless"), and [CASE-151](../cases.d/CASE-151.md)
(Wells Fargo, where leadership blamed and disciplined individual employees
for what the board's investigation traced to the sales model), a case of
the opposite practice. From the same exchange, A17 §1's moral crumple
zone, the person nearest the failure absorbing the blame, is filed as
[CLAIM-707](../claims.d/CLAIM-707.md); A17 §9 had already said that "A person can be required to
explain their decisions and participate in correcting a failure without
necessarily being morally culpable for everything that happened", and
that an institution should "examine system failures without automatically
identifying the nearest human as their sufficient explanation". That is
the closest the exchange came to the owner's case before U48. The
responsibility senses at issue are [TERM-127](../terms.d/TERM-127.md)'s.

[QUESTION-470](QUESTION-470.md), from the first share of the same exchange, asks when an
organization's responsibility to repair a harm survives the absence or
dispersion of blameworthiness. This question refines it for one practice:
blameless post-incident review is an organization's attempt to keep
accountability and repair while setting blame aside, and whether it keeps
the upstream provenance blame supplies is a part of that question.

## Note of 2026-11-17: Shoemaker's corporate model, read: one kind of blame withheld, another kept
<!-- inactive-ok-file: NOTE-2048 THEORY-1974 LIT-2777 — Skimmed, new or Unavailable; the reading filed on 2026-11-18 and the unread paper it stands in for -->

Shoemaker 2019, read in part ([NOTE-2048](../notes.d/NOTE-2048.md), [THEORY-1974](../theory.d/THEORY-1974.md)), standing in for Shoemaker 2011 ([LIT-2777](../literature.d/LIT-2777.md)). The THEORY now carries `bears_on` this question.

Shoemaker splits responsibility into "three distinct types" that are "radically independent" (p. 913, n. 70), and splits blame with them. Corporations "may be blameworthy and blamable in answerability terms, but not blameworthy or blamable in accountability terms" (p. 915): they can be asked "Why did you do that?" and protested, but not angrily blamed, since "gratitude and anger aptly respond to empathic and emotional (dis)regard". That is a worked model of a practice that keeps one kind of blame, answerability's demand for reasons, while giving up another, accountability's anger: one candidate reading of "keep accountability while giving up blame". The fit is partial. Shoemaker builds it for agents that lack the capacities anger needs, while blameless practice in engineering withholds anger from persons who have them; and his "accountability" is the anger-tracking type, not the remedial sense the question's "accountability" may mean.

It says nothing about the question's second half, the provenance of an incapacity.

No status changes.

## Note of 2026-11-17: The NTSB's Tempe report and Elish's Therac-25 contrast, read: a no-blame investigation that keeps upstream provenance
<!-- inactive-ok-file: THEORY-1932 CASE-292 THEORY-1928 — new; the readings and case filed on 2026-11-18 -->

NTSB 2019, read for responsibility ([NOTE-2034](../notes.d/NOTE-2034.md), [THEORY-1932](../theory.d/THEORY-1932.md), bears_on); the case is [CASE-292](../cases.d/CASE-292.md). A statutory safety investigation is a blameless practice in the question's sense: "The NTSB does not assign fault or blame for an accident or incident"; its investigations "are fact-finding proceedings with no formal issues and no adverse parties". It still names a ranked allocation of cause, and carries it upstream: the operator's distraction as probable cause, with the company's "inadequate safety risk assessment procedures", "ineffective oversight of vehicle operators" and "lack of adequate mechanisms for addressing operators' automation complacency—all a consequence of its inadequate safety culture", and the state's "insufficient oversight", as contributing (p. v). So one blameless practice keeps the upstream provenance of the operator's incapacity: the culture "contributed ... specifically to the vehicle operator's extended distraction" (p. 46). It does so by naming contributing factors, not by blame. Whether this holds of blameless engineering post-mortems, the question's object, is not shown.

Elish 2019, read ([NOTE-2019](../notes.d/NOTE-2019.md), [THEORY-1928](../theory.d/THEORY-1928.md), bears_on). Her contrast case points the other way on where attribution goes when no blameless practice intervenes: after a publicized accident, blame lands on the nearest operator; in the slowly surfacing Therac-25 accidents, lawsuits went to the manufacturer (pp. 50–51).

No status changes.

## Note of 2026-11-18: blameless culture read, and two claims filed in answer
<!-- inactive-ok-file: THEORY-2000 THEORY-1998 THEORY-1997 THEORY-1999 CLAIM-751 CLAIM-750 CASE-293 ARG-118 — new; the readings and the entries filed on 2026-11-18 -->
<!-- inactive-ok-file: LIT-2785 LIT-2780 LIT-2781 — Unfetched or Unavailable; the three candidate sources not read -->

On 2026-11-18 the owner asked the lead to "consider how blameless culture in modern engineering could be an interesting case for analysis here" and, on its proposals, "all of the above please". Of the candidate sources this question named, the SRE chapter was read ([THEORY-2000](../theory.d/THEORY-2000.md)); Allspaw's post is Unfetched behind a bot check ([LIT-2785](../literature.d/LIT-2785.md)); Dekker's *Just Culture* is Unavailable ([LIT-2781](../literature.d/LIT-2781.md)), with Dekker and Nyce (2013) read in its place ([THEORY-1997](../theory.d/THEORY-1997.md)). Cook's "How Complex Systems Fail" ([THEORY-1998](../theory.d/THEORY-1998.md)) and 49 U.S.C. § 1154 ([THEORY-1999](../theory.d/THEORY-1999.md)) were also read; Reason (1997) is Unavailable ([LIT-2780](../literature.d/LIT-2780.md)). Each reading now carries `bears_on` this question.

- **First half (accountability kept, blame given up).** The SRE chapter is the practice by design: contributing causes "without indicting any individual or team", follow-up actions to prevent recurrence, and disclosure as the reason. It shows the practice exists and is codified, not that it works.
- **Second half (provenance).** No reading shows where a blameless postmortem's trace stops. The chapter says it runs to "the systematic reasons why an individual or team had incomplete or incorrect information"; it says nothing of decisions above the reviewing team. The NTSB at Tempe, no-blame by regulation and kept out of damages suits by § 1154(b), traced the operator's distraction to the company and the state and sent its recommendations to them: the first answer, for an investigator outside the organization. [CLAIM-751](../claims.d/CLAIM-751.md) files that, with [ARG-118](../arguments.d/ARG-118.md). [CLAIM-750](../claims.d/CLAIM-750.md) hypothesizes the second answer for reviews commissioned inside the organization, with a prediction, and [CASE-293](../cases.d/CASE-293.md) is the study that would test it.
- **Third answer (blame relocated).** Dekker and Nyce argue that a just-culture scheme in hospitals sorts blame by rank: "who gets to say".
- **Cook** gives the premise all of these start from: root-cause attribution reflects "the social, cultural need to blame specific, localized forces or events", so blame itself tends to stop near the event.

No status changes. The question stays Open: its second half, for engineering postmortems, is unanswered.

## Note of 2026-11-22: a pilot coding of postmortems
<!-- inactive-ok-file: CASE-335 CLAIM-905 — new; the pilot and its finding, filed for LEAD-119 on 2026-11-22 -->

The question's second half, for engineering postmortems, now has a pilot bearing on it: [CASE-335](../cases.d/CASE-335.md) and its finding [CLAIM-905](../claims.d/CLAIM-905.md). In 26 of 30 public postmortems the trace stops at the engineering group's own design or procedure. CSB investigations of chemical accidents mostly carry it to corporate oversight, funding and regulation. That is the second answer listed here, "keeps correction, loses provenance", for published internal reviews. One coder, the assistant (Claude, Opus 5.5), of the same model family that wrote the claim tested and the codebook, coding with the prediction known: the pilot is not independent. The arms differ in domain and severity (software outages against chemical accidents) as well as in who reviews.

No status changes. The question stays Open.

## Note of 2026-11-22: the SRE example postmortem, the workbook and the Tempe prosecution, read
<!-- inactive-ok-file: THEORY-tmp9j928 THEORY-tmpm653d THEORY-tmpfdyu6 CLAIM-tmp20uni CLAIM-tmp64hmn CLAIM-tmpauu5r CASE-tmptkkgm — new; filed for LEAD-189 on 2026-11-22 -->

Read for LEAD-189 on 2026-11-22; each reading now carries `bears_on` this question.

- **The second half, from the practice itself.** Google's example postmortem (THEORY-tmp9j928) is fictional and its causes are a bug and a surge, so it shows the template, not where a trace stops. The workbook (THEORY-tmpm653d) shows one real postmortem whole (CASE-tmptkkgm): blaming "No individual or team", it names a staffing limit among what went poorly and gives its fourteen action items, all technical, to engineers. Its examples of keeping review blameless recast a question to a manager, and a vice-president's question, as questions about process. That leans toward the second answer listed here, "keeps correction, loses provenance", for the single postmortem.
- **But the practice may keep provenance elsewhere.** The workbook puts "Is feature velocity trumping reliability fixes?" in the review of repeated incidents, and has "organizational leaders" review the process. CLAIM-tmpauu5r files that as an objection to testing CLAIM-750 one postmortem at a time. Whether those channels reach above the teams is not shown by anything read.
- **The blame-based counterpart.** On the Tempe crash, which the NTSB traced to the company and the state without blame, the criminal process charged and convicted the operator alone and declined to charge the company (THEORY-tmpfdyu6, CLAIM-tmp20uni). The objection, CLAIM-tmp64hmn: a civil settlement and the state's suspension of testing did reach the company, so the contrast is with the criminal law, not with blame as such.

No status changes. The question stays Open: what a blameless practice traces across incidents, as opposed to in one postmortem, is unanswered.
