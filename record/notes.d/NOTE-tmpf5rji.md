---
status: Read
paper: 'LIT-tmpi9wm8'
title: 'Scacco and Warren — Can social contact reduce prejudice and discrimination?'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from the published version deposited by
    the WZB on EconStor under a DFG national licence
    (https://www.econstor.eu/bitstream/10419/194860/1/f-21548-full-text-Scacco-et_al-Contact-v3.pdf,
    25 pages, the journal's pp. 654–677 with a cover sheet), text
    extracted with pdftotext. Read: every section, Tables 1–7, the
    footnotes and the references. Figures 1–3 (the design tree and two
    attendance charts) were read from the text only; no number was taken
    from a chart. Not read: the online appendix, which holds the
    stranger-only analyses (Tables A.33, A.42), the robustness checks and
    the mechanism items (A.19–A.30), and the replication files. Checked:
    the differences in Table 6 against its means (they agree to rounding);
    the text's conversions of Table 5's coefficients (₦2.5 of ₦5.8 for
    Muslims; about 70% for the full sample, 0.39/0.55); the 10% program
    effect in the destruction game (0.07/0.70). Checked on OSF
    (osf.io/p8dx2): the EGAP registration 20150617AA is dated 12 August
    2015 and states "Registration prior to researcher access to outcome
    data"; its abstract gives 720 subjects and five outcome families.
date: '2026-10-29'
summary: >-
  A randomized field experiment with 849 young Christian and Muslim men
  in Kaduna: sixteen weeks of cooperative computer training in mixed or
  single-religion classes left stated prejudice and its supposed
  mediators unchanged, while mixed classes discriminated less than
  single-religion classes in dictator and destruction games. The control
  arm shows the contrast is mostly in-group bonding raising
  discrimination in single-religion classes; the effect toward
  unfamiliar out-group members holds for Christians only.
---
<!-- inactive-ok-file: CLAIM-430 CLAIM-403 — Proposed; claims this reading bears on, cited as open -->

# NOTE-tmpf5rji: Scacco and Warren — Can social contact reduce prejudice and discrimination?

## Contribution

A randomized test of the contact hypothesis in an ongoing conflict
setting, on a random sample of the people who riot rather than
volunteers, with prejudice and discrimination measured separately. Its
two findings are that cooperative contact can change behaviour toward
the out-group while leaving stated attitudes where they were, and that
a pure control arm changes what the usual mixed-against-unmixed
comparison means: most of that contrast is the single-religion classes
becoming more discriminatory.

## Key insight

The usual contact comparison has two moving parts. Against people who
took no course, the mixed classes discriminated about as much as before
and the single-religion classes discriminated more, because they gave
their new generosity mostly to their own side. So "contact reduced
discrimination" here is better read as "contact prevented the rise that
same-group contact produced". The authors call it a substitution
effect: time with the out-group is time not spent bonding with the
in-group.

## Assumptions

- **Population.** Men aged 18–25 in the sixteen poorest Kaduna
  neighbourhoods with a history of violence, sampled by random walk;
  women and six neighbourhoods suspected of Boko Haram cells excluded.
- **Treatment.** 30 class sections (20 mixed, 10 single-religion), four
  hours a week for sixteen weeks, 29 sessions, pairs sharing a laptop on
  cooperative tasks, no peace or anti-prejudice content, and incentives
  (a ₦200 stipend per class, a laptop raffle). Students and teachers were
  told it was an educational programme.
- **Randomization** at three levels: invitation to the course (549)
  against survey-only control (300); mixed against single-religion class;
  same- against other-religion partner within mixed classes.
- **Measures, endline only**, four to six weeks after the course:
  prejudice by three stereotype indices (negative attributes, positive
  attributes, a three-pair out-group evaluation), self-completed and
  sealed; discrimination by ten rounds each of a dictator game (divide
  ₦100) and a destruction game (destroy another's ₦50 notes for ₦10
  each), against recipients named by first name, which signals religion,
  and for course participants flagged as classmate or not. No prejudice
  baseline, by design, to avoid priming.
- **Estimation.** Intent-to-treat OLS, no covariates in the main tables;
  game standard errors clustered by respondent, with round fixed effects.
  Compliance 84%; attrition 6% (4% treated, 10% control).

## Key results

- **Prejudice (Tables 2–4).** No arm reduced it. Of 27 coefficients two
  are significant at p < 0.05 and they point opposite ways (Christians in
  the course disagreed more with both negative and positive attributes of
  Muslims). The authors report over 90% power for r = −0.21. The mediator
  items (knowledge, anxiety, empathy) moved only for Muslims' anxiety
  under course assignment.
- **Program effect (Table 5, cols 1–3).** The course raised dictator
  giving by about 0.47 bills (₦4.7, about ₦4 by the text) to in-group and
  out-group alike, with no change in the gap.
- **Contact effect (Table 5, cols 4–6).** Mixed class × out-group
  recipient: +0.39 bills, p < 0.01, against a gap of −0.55, about 70%
  of it. Muslims +0.25 (p < 0.10) of −0.58; Christians +0.52 of −0.51,
  all of it.
- **Against the control (Table 6).** Gap between in-group and out-group
  giving: control 0.19, single-religion class 0.54, mixed class 0.17. By
  religion: Muslims 0.33, 0.58, 0.34; Christians 0.02, 0.51, 0.00.
- **Destruction game (Table 7).** The course cut destruction by about
  10% (−0.07 on 0.70), driven by Christians. Mixed class × out-group:
  −0.05 (p < 0.10), Christians −0.08 (p < 0.10). Other-religion partner ×
  out-group: −0.07 (p < 0.10), Christians −0.10 (p < 0.05).
- **Partner dose (Table 5, cols 7–9).** No further reduction in
  dictator-game discrimination from an other-religion partner; a further
  rise in giving to everyone among Christians.
- **Strangers (text; appendix not read).** Restricted to recipients who
  were not classmates, the mixed-class effect on dictator giving halves
  and is not significant; among Christians it stays large and
  significant. In the destruction game there is no overall reduction
  toward strangers; Christians' effects are of comparable size.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Sixteen weeks of cooperative intergroup contact did not change stated prejudice | moderate | three indices, nulls with stated power; endline only, self-report |
| C2 | Mixed classes discriminated less than single-religion classes in incentivized games | moderate | Table 5 (p < 0.01 dictator), Table 7 (p < 0.10 destruction); randomized |
| C3 | The contrast is mostly a rise in discrimination in single-religion classes | moderate | Table 6, a comparison of means against the control, no test reported |
| C4 | Contact reduced discrimination toward unfamiliar out-group members | weak | Christians only; the overall stranger effect is not significant; appendix tables not read |
| C5 | Behaviour changed before attitudes, as self-perception theory predicts | weak | offered as one of four interpretations; untested, one endline |
| C6 | Valued programme content draws participants and raises generosity to all | moderate | the program effect in Tables 5 and 7 |

## Concepts

- **Prejudice**: "negative beliefs about or attitudes toward an
  individual based solely on membership in a particular social group",
  measured by stereotype agreement.
- **Discrimination**: treatment that "differs based solely on group
  affiliation", measured as the gap between play toward in-group and
  out-group recipients.
- **In-group bonding effect**: the rise in in-group-favouring play among
  those given contact with unfamiliar members of their own group.
- **Program effect / contact effect / contact dosage effect**: the three
  randomized comparisons (course against control; mixed against
  single-religion class; other- against same-religion partner).

## Connections

The authors place themselves against Pettigrew and Tropp's optimism
(LIT-1413) and use its mean r = −0.21 for their power analysis; they cite
the 2008 mediator meta-analysis (LIT-1405) for knowledge, anxiety and
empathy, and find none of the three moved. Paluck, Green and Green
(LIT-1420, NOTE-1393) include this study among their three
pre-registered trials, pooled at 0.016; this reading shows that their
near-zero is the prejudice null, while the trial's own headline is a
behavioural effect. The authors' precedent for behaviour changing
without attitudes is Paluck's Rwanda radio study. Their Discussion cites
Bem's self-perception and Fazio on behaviour preceding attitude.

## Bearing on the record

- **QUESTION-262.** It meets the question's measurement demand, conduct
  scored by evidence that does not pass through the interpretation under
  test (incentivized, private, sealed games), and its stranger rounds
  are the "unfamiliar group members" the question names. It does not
  draw the question's first contrast. There is no arm with favourable
  information and no taking part; the course arms differ in who one took
  part with, not in whether one took part. Its "local against general"
  result is split: the effect on strangers holds for Christians and not
  overall. And it adds a contrast the question lacks: the comparison
  that matters may be same-group against cross-group taking part, since
  same-group cooperation itself moved conduct, toward more
  discrimination. A note on the question should say that its "near zero"
  for pre-registered trials is, for this study, a null on attitudes
  beside a positive result on behaviour.
- **CLAIM-430.** The pattern, conduct moved and stated view did not, is
  what part 2 of the claim, taking part before the reinterpretation,
  would show at the moment of measurement. It is not evidence that the
  reinterpretation follows: there is one endline, no later attitude
  measure, and the authors give the order only as one of four readings.
  Their first reading cuts against the claim's mechanism. If the
  behavioural contrast is mostly in-group bonding in the single-religion
  classes, the mixed classes were not given a new way of relating; they
  were spared a reinforced old one. The trial does not touch the claim's
  second defeater, since it has no information arm. The anonymous-favour
  defeater is not tested either.
- **CLAIM-275.** One more instance of conduct changing without a prior
  change of interpretation, in a randomized design. It does not show the
  act making the interpretation available.
- **CLAIM-403.** The trial measured no change in whose testimony moves
  judgement; its outcomes are stereotype ratings and allocations.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Behaviour in games.** Discrimination is play in two games against
  named strangers, at home, a month after the course; not conduct in
  daily life, and no conflict behaviour.
- **Small effects in the destruction game**, mostly at p < 0.10, and
  three comparisons by two religions per game invite multiplicity, which
  the paper does not correct for. The authors report that the
  religion × treatment interactions are not significant, so the
  difference between Christians and Muslims they discuss is not
  established either.
- **Registration after data collection.** The EGAP registration is dated
  12 August 2015 (ID 20150617AA), seven months after the January 2015
  endline; it attests registration before the researchers had the
  outcome data. It lists five outcome families (prejudice,
  discrimination, cooperation, conflict-related behaviour and attitudes,
  trust), 720 subjects, pre-specified controls and difference-in-
  differences where possible; the paper reports two families, 849
  subjects and parsimonious models, with the pre-specified controls in
  the appendix. Whether the other three families are reported elsewhere
  was not checked.
- **The partner arm** may be a weak dose: with at most sixteen students a
  class, the authors say, the difference between partners may have been
  small.
- **Slips.** The text's "approximately ₦4" program effect is 0.47 bills
  of ₦10, ₦4.7 (footnote 39's ₦26 to ₦30 rounds the same way). In
  the extracted text the paragraph on stranger play in the destruction
  game precedes the section that introduces Table 7, a layout effect. No
  error of substance found.

## Open questions

- Does stated prejudice move later in the mixed classes, as the
  self-perception reading predicts? A second endline would say.
- Would an arm that received the course's cross-group content without
  the shared work, for instance watching mixed pairs work, change
  conduct as much? That is QUESTION-262's first contrast and CLAIM-430's
  second defeater, and this design does not draw it.
