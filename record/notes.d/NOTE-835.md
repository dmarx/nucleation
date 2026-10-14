---
number: 835
status: Read
formerly:
- NOTE-tmpdnj1q
paper: LIT-757
title: 'Grudin — Groupware and social dynamics'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the copy Microsoft Research posts on its own site
    (microsoft.com/en-us/research/wp-content/uploads/2017/01/groupware-and-social-dynamics.pdf),
    where the author worked; 14 PDF pages, CACM 37(1):92–105, ACM
    printing with its copyright and permission notice. Only the abstract
    page has a text layer; pages 94–105 are page images, rendered at 130
    dpi and read as images, every column, Table 1 and Figure 1, and the
    32 references. Quotations were transcribed by eye from those images.
    Page 105 also carries the end of an unrelated article in the same
    issue (an author note for Andrew Clement); it was ignored.
date: '2026-10-14'
summary: >-
  An argued review, not a study. Groupware fails less from technical
  problems than from eight social challenges, first among them that it
  asks extra work of members who get no direct benefit. The evidence is
  cases and the literature: meeting schedulers, voice annotation, project
  management, an abandoned issue-based system. Email succeeds because the
  sender who does the work is also the one who wants the message read.
---
<!-- inactive-ok-file: CLAIM-179 CLAIM-176 — Proposed; the claims this reading bears on, open -->
<!-- inactive-ok-file: LIT-759 — Unavailable; Grudin 1988, the earlier paper this one widens, not read here -->
<!-- inactive-ok-file: LIT-761 LIT-755 LIT-762 — Unavailable; design-rationale works of the batch with no lawful copy reached, named and not leaned on -->
<!-- inactive-ok-file: THEORY-311 — Proposed; the account filed from this reading -->

# NOTE-835: Grudin — Groupware and social dynamics

## Contribution

The article places groupware between single-user applications and
organizational information systems, and argues that the experience of
neither carries over. It lists eight challenges that "arise from" the
social dynamics of groups (Table 1, p. 97), illustrates each with cases
from products, prototypes and published studies, and closes by asking what
the successes, chiefly email, did differently. It turns the 1988 paper's
argument ([LIT-759](../literature.d/LIT-759.md)) into a checklist for developers. It reports no new
data.

## Key insight

Who does the work and who benefits are usually different people in a
group. "A groupware application never provides precisely the same benefit
to every group member" (p. 96), and when the work falls on those who do
not benefit, they decline to do it, so the application fails for everyone.
The applications that survive are those in which the person doing the work
is also a beneficiary, as the sender of an email is.

## Assumptions

- **Discretionary use.** The argument concerns products bought and used by
  choice in small groups. For mainframe systems an organization commits to,
  management can force use, hire administrators or rewrite job
  descriptions, and the problems are milder (pp. 94–96).
- **Groups, not organizations.** Groupware "targets smaller groups than
  systems serving organizational goals" (p. 95). Management is less
  committed to it, and "a small application program must adapt to the
  organization".
- **The developer's point of view.** The challenges are addressed to
  product developers. The author writes partly from his own experience as a
  developer and user (Acknowledgment, p. 104).

## Key results

There are no results in the sense of measurements. What the article
states, with its supporting cases:

- **Where groupware sits (Figure 1, pp. 94–95).** Three rings,
  organizations, groups and individuals, studied by MIS/IT (from 1965), CSCW
  (from 1985) and HF/CHI (from 1980), and built in internal and contract,
  product and telecom, and product development. CSCW conference attendance
  was "approximately 40%" from product development companies and 30% from
  universities.
- **The eight challenges (Table 1, p. 97).**
  1. "Disparity in work and benefit. Groupware applications often require
     additional work from individuals who do not perceive a direct benefit
     from the use of the application."
  2. "Critical mass and Prisoner's dilemma problems. Groupware may not
     enlist the 'critical mass' of users required to be useful, or can fail
     because it is never to any one individual's advantage to use it."
  3. "Disruption of social processes. Groupware can lead to activity that
     violates social taboos, threatens existing political structures, or
     otherwise demotivates users crucial to its success."
  4. "Exception handling. Groupware may not accommodate the wide range of
     exception handling and improvisation that characterizes much group
     activity."
  5. "Unobtrusive accessibility. Features that support group processes are
     used relatively infrequently, requiring unobtrusive accessibility and
     integration with more heavily used features."
  6. "Difficulty of evaluation. The almost insurmountable obstacles to
     meaningful, generalizable analysis and evaluation of groupware prevent
     us from learning from experience."
  7. "Failure of intuition. Intuitions in product development environments
     are especially poor for multiuser applications, resulting in bad
     management decisions and an error-prone design process."
  8. "The adoption process. Groupware requires more careful implementation
     (introduction) in the workplace than product developers have
     confronted."
  The first five need knowledge of the users' workplace; the last three
  need changes in the development process (p. 95).
- **Disparity, by case (pp. 96–97).**
  - Automatic meeting scheduling benefits the convener, but works only if
    everyone keeps an on-line calendar. Studies found calendars used "as
    communication devices by managers" and not maintained by individual
    contributors [8]. "Consequently, this groupware feature is rarely
    used."
  - Digitized voice annotation favours the speaker; the listener finds it
    slower to take in, scan and edit.
  - A distributed project-management system benefits the project manager
    and needs others to enter information "not typically kept on-line". A
    naval vessel's computer-assisted management system, developed over ten
    years [22], was replaced "due in part to the difficulty of getting
    everyone to use it".
  - Against organizational systems: there, "doing the additional work
    becomes someone's explicit job".
  - Remedies offered: reduce the work of non-beneficiaries, demonstrate the
    collective benefit, and "design, along with the technology, processes
    for using it that create benefits for all group members".
- **Critical mass and the prisoner's dilemma (pp. 96–97).** Even one or two
  defections can sink a scheduling or decision-support application. With
  discretionary databases, "as long as someone updates them, one's optimal
  strategy is to 'freeload'". These analyses show "that even a net benefit
  with equal costs and benefits for all users will not guarantee groupware
  success". An organization-wide voice-messaging system succeeded only
  after top management removed the alternative, the message-taking
  receptionists.
- **Social and political processes (p. 97).**
  - A scheduler that books a manager's apparently open time can be
    rejected, since secretaries know that time is "seldom really free".
  - A priority-based scheduler "foundered because participants were
    reluctant to acknowledge publicly that some of their meetings were low
    priority".
  - A work-management system that forwarded "priority problem" reports to
    the chief executive was sabotaged by a program that kept touching files.
  - "In one case, a management group considered using an issue-based IS in
    which issues, arguments, counterarguments, and decisions are entered,
    creating a record of decision making that could be used to
    communicate, review, and explore alternatives. The plan to use the
    system was abandoned because the manager wanted the group to project a
    strong sense of consensus. The explicit record of opposing positions
    that the application would immortalize was politically unacceptable."
    No source is given for this case.
- **Exception handling (pp. 98–99).** "Work processes can usually be
  described in two ways: the way things are supposed to work and the way
  they do work." Ishii and Ohkubo's office-procedure system [15] and a
  chocolate factory's order system [26] are the cases; the factory's
  system was made to work only by "hiring new personnel and taking other
  expensive measures", which a typical groupware feature will not get.
- **Infrequent features (pp. 99–100).** Most group features are used less
  often than individual ones, so they "will fare better if integrated with
  features that support individual activity". "If possible, add groupware
  features to an already successful application".
- **Evaluation (p. 100).** More than ten members of a research laboratory
  took part in usability tests of a coauthoring application; "several
  months later it was not being used outside the experimental setting".
- **Intuition (pp. 100–101).** Decision makers favour applications that
  "selectively benefit one subset of the user population: managers". "The
  greatest interface challenge for an intelligent project management
  application is to minimize the information entry effort required of each
  subordinate (or provide compensatory benefits), but attention is instead
  directed toward information visualization."
- **Adoption (pp. 101–102).** "A word processor that is immediately liked
  by one in five prospective customers could be a big success. A groupware
  application to support teams of five nurses that initially appeals to
  only one nurse in five is a big disaster." Lotus Notes and TeamFocus
  were sold with consulting; Wang Freestyle was not, and failed.
- **Email (pp. 102–103).** Grudin runs email through all eight challenges.
  On the first: "Email provides an equitable balance for sender and
  recipient. The person with a message to communicate must type it, while
  the receiver can read it easily at a convenient time. Thus, the primary
  beneficiary typically does a little more work." Databases and code
  management also succeed, and their primary beneficiaries "are not
  managers or decision makers, but people who use computer systems more
  routinely".
- **What to do (p. 104).** Extend single-user applications with group
  features; find niches; build on object management and shared databases;
  "find ways to provide direct benefits for all group members"; "be wary
  of applications that will selectively benefit managers"; educate
  managers and developers about the risks.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Groupware that asks work of members who get no direct benefit tends to go unused | moderate | several cited cases and studies (meeting scheduling [8], project management [22]), pp. 96–97 |
| C2 | Equal costs and benefits do not guarantee use, because of critical mass and freeloading | moderate | Markus and Connolly's model [21] and one voice-messaging case, pp. 96–97 |
| C3 | An explicit record of opposing positions can be refused for political reasons | weak | one uncited case, p. 97 |
| C4 | Groupware succeeds more often as features added to single-user applications than as standalone products | weak | argued from use frequency and cost, pp. 99–100, 104 |
| C5 | Email avoids the eight challenges, and the benefit to the sender who does the work is why it avoids the first | moderate | argued point by point, pp. 102–103 |
| C6 | Developers' and managers' intuitions mislead them about multiuser software | weak | the author's experience and anecdote, pp. 100–101 |

## Concepts

- **Groupware.** Software "designed to support groups" or "being used to
  support groups" (p. 93): desktop and video conferencing, coauthoring,
  email and bulletin boards, meeting support, voice applications, workflow
  and group calendars.
- **Disparity in work and benefit.** The gap between who must do extra
  work for an application and who benefits from it, which is usually a gap
  between roles (manager and subordinate, convener and invitee, speaker and
  listener), not between times.
- **Critical mass.** The fraction of members who must use an application
  for it to be useful to any of them.
- **Primary beneficiary.** The member for whom an application chiefly
  works: the convener of a meeting, the project manager.

## Connections

The article widens Grudin's 1988 CSCW paper ([LIT-759](../literature.d/LIT-759.md), held here unread)
from three problems to eight. It draws on Markus and Connolly for the
prisoner's dilemma, Ehrlich for adoption, Perin for the politics of email,
and Kraemer and King for decision support. Grudin had worked at MCC, where
gIBIS ([LIT-762](../literature.d/LIT-762.md)) was built, and at Wang; the article mentions neither IBIS
nor gIBIS by name, and its one issue-based case is unattributed.

## Bearing on the record

- **[CLAIM-179](../claims.d/CLAIM-179.md) is supported in its premise and qualified twice.**
  - **Supported.** The 1994 article states the disparity as challenge 1
    and gives the success condition [CLAIM-179](../claims.d/CLAIM-179.md) relies on: email works
    because "the primary beneficiary typically does a little more work".
    When the filer also benefits, the first challenge is met. [CLAIM-179](../claims.d/CLAIM-179.md)
    grounds the disparity in the unread 1988 paper; this read paper can
    ground it instead.
  - **Qualified: removing the disparity is not enough.** Grudin says that
    "even a net benefit with equal costs and benefits for all users will
    not guarantee groupware success" (pp. 96–97). [CLAIM-179](../claims.d/CLAIM-179.md) says agent
    filing "removes the disparity that design-rationale systems were
    abandoned over", which is consistent with this, but its defeater
    names only the disparity as the cause of abandonment. On Grudin's
    account a record could also be abandoned for the other seven reasons.
  - **Qualified: the one argument-record case failed for another reason.**
    The only issue-based system in the article was abandoned before use
    because "the explicit record of opposing positions that the application
    would immortalize was politically unacceptable" (p. 97). That is
    challenge 3, social disruption, not challenge 1. It bears on a record
    that retires by status and never deletes: an objection, once filed, is
    kept.
- **[ADR-030](../decisions.d/ADR-030.md)'s first failure mode is stated differently here.** The
  curation entry of 2026-10-06 puts it as "the cost of capture falls on the
  author while the benefit goes to a later reader". Grudin's disparity is
  between people in different roles at the same time, typically subordinate
  and manager. The author-against-later-reader form is closer to the
  design-rationale literature than to this article. In this record the
  filer is an agent and the later reader is the same agent in another
  session, so the role disparity Grudin describes falls, if anywhere, on
  the owner, who reviews.
- **The curation entry's check is answered in part.** It asked whether the
  record's experience bears out the first failure mode. Grudin's remedies
  are to reduce the work of non-beneficiaries and to design processes "that
  create benefits for all group members"; agent filing is a case of the
  first. His challenges 2 (critical mass) and 5 (infrequent use) do not
  arise for a record with one owner and one filer. Challenge 3 may.
- **[CLAIM-176](../claims.d/CLAIM-176.md).** Grudin's advice to add group features to "an already
  successful application" rather than launch a new one is a version of
  capturing inside work already being done. It does not bear on the
  second-occurrence throttle directly.
- **Filed from this reading:** [THEORY-311](../theory.d/THEORY-311.md), the disparity account, held
  at the strength of an argued review of cases.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- No systematic data. The cases are selected to illustrate, some are
  unattributed, and failure is not measured against a base rate.
- The author grants that "success and failure cannot be reliably predicted"
  (p. 96) and that the evidence on evaluation is itself thin (challenge 6).
- The article is about products for small groups in workplaces of 1994. It
  does not consider a single user whose collaborator is software.

## Open questions

- Whether the disparity, once removed, leaves the other challenges as the
  main causes of abandonment is not tested; a study of applications that
  meet challenge 1 and still fail would answer it.
- The issue-based case is unsourced. Whether records of opposing positions
  are commonly refused for political reasons would need the design-rationale
  field studies ([LIT-755](../literature.d/LIT-755.md), [LIT-761](../literature.d/LIT-761.md)) to settle.
