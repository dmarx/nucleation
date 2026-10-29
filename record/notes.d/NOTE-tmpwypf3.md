---
status: Read
paper: 'LIT-1407'
title: 'Kalla and Broockman — Reducing exclusionary attitudes through interpersonal conversation'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from the authors' accepted manuscript on
    SocArXiv (OSF preprint 2ra9x, file
    https://osf.io/download/5e3b26d3f1369e00a68ad00b/, dated 17 January
    2020, "Forthcoming, American Political Science Review"; 81 pages, of
    which pp. 1–33 are the article and the rest the online appendix),
    text extracted with pdftotext. Read: the abstract, the whole article
    (introduction, theory, the three experiments, discussion), Table 1
    (re-read from a layout extraction, since the plain one scrambled it),
    the captions of Figures 1–3, the footnotes and the reference list.
    Not read: the online appendix (scripts, balance, attrition, the OA
    tables of point estimates and the heterogeneity tables); the
    figures' points were not read, only the numbers the text gives. The
    published APSR version was not seen, so any change made at proof is
    not known here. Checked: every t-statistic the text reports against
    its stated p-value under a normal two-sided test (record script,
    2026-10-29), which found two mismatches (Limitations); the
    condition sizes add to the samples randomized, and the three
    experiments' reached voters (2,374 + 1,858 + 2,637) to the
    abstract's 6,869.
date: '2026-10-29'
summary: >-
  Three pre-registered, placebo-controlled canvassing experiments
  (6,869 voters reached at the door or by phone). In Experiment 1, a
  conversation with narratives exchanged non-judgmentally moved an index
  of immigration attitudes by d = 0.08 pooled over 4.5 months; the same
  conversation without the narratives moved it by 0.02 (n.s.), and the
  difference, 0.06, is significant. Transphobia replications give 0.08
  (with or without the participants' own narratives) and 0.04 by phone.
---
<!-- inactive-ok-file: CLAIM-430 — Proposed; the claim this reading bears on, cited as open -->

# NOTE-tmpwypf3: Kalla and Broockman — Reducing exclusionary attitudes through interpersonal conversation

## Contribution

It takes deep canvassing, which Broockman and Kalla (2016) had shown
reduced transphobia in one Miami trial, and isolates one component. In a
field experiment the authors remove the exchange of narratives from an
otherwise identical canvass, and the effect goes with it. Two more
experiments carry the narrative strategy to a video narrative from a
stranger and to the phone. All three are pre-registered and run by
organizations with no prior experience of such canvassing.

## Key insight

People resist persuasion that threatens their self-image: admitting error,
or being seen to be manipulated. A conversation that asks for and gives
stories, and listens without judging what the listener says, lowers that
threat. In the field the effect of such a conversation is small, but it
lasts months. The same arguments delivered without the stories do nothing
detectable.

## Assumptions

- **The design (Broockman, Kalla and Sekhon 2017).** Registered voters are
  recruited by mail to an online baseline survey with no reference to
  canvassing. Respondents are randomized by household to treatment or a
  placebo conversation on an unrelated topic, and canvassers then visit or
  call. Effects are intent-to-treat among those who identified themselves
  at the door, estimated by linear regression with pre-registered
  covariates and household-clustered errors.
- **The comparison in Experiment 1.** The Abbreviated Intervention keeps
  the canvassers' questions, the correction of misconceptions and the
  supportive arguments, and removes the narratives. It also halves the
  conversation, 5 minutes against 11 (fn. 8). The authors argue that any
  arm matched on length would add some other content and so a different
  confound.
- **Outcomes.** Self-reported survey indices of policy support and of
  prejudice, standardized. No behaviour is measured.
- **The CACE.** Table 1's complier effects assume no effect on those who
  began the conversation and did not reach the "first rating".

## Key results

- **Experiment 1 (immigration, fall 2018, three California and
  Tennessee sites).** 7,870 baseline respondents in 6,551 households were
  randomized to Full (2,624), Abbreviated (2,623) or Placebo (2,623);
  2,374 were reached; follow-ups at 4 days (n = 1,578), 30 days (1,508)
  and 3–6 months (1,384; on average 4.5 months). Full against Placebo,
  policy index: d = 0.11, 0.06, 0.08 by wave, pooled 0.09 (t = 3.89).
  Prejudice index: 0.07, 0.07, 0.05 (t = 1.77, p < 0.08), pooled 0.07.
  Abbreviated against Placebo: indistinguishable from zero. Full against
  Abbreviated: policy pooled d = 0.06 (t = 2.57), prejudice pooled 0.05
  (t = 2.36); at 1 month neither index differs significantly (t = 1.40,
  0.93), and at 3–6 months the prejudice index does not (t = 1.11).
- **Table 1, the pooled overall index.** ITT d = 0.08 (Full), 0.02
  (Abbreviated, p = 0.27; Full minus Abbreviated 0.06, p < 0.01), 0.08
  and 0.08 (Experiment 2's two arms), 0.04 (Experiment 3), against 0.16
  for Broockman and Kalla 2016. CACEs: 0.22 (2016), 0.12, 0.03, 0.10,
  0.10, 0.08.
- **Experiment 2 (transphobia, 2016, Atlanta, Cleveland, Jacksonville,
  Scottsdale).** 8,456 baseline respondents in 3,485 households to
  Participants' and Video Narratives (2,815), Video Narratives Only
  (2,817) or Placebo (2,824); 1,858 reached; follow-ups at 1 week (1,044)
  and 1 month (989). Both arms work, and their difference is not
  significant but imprecise. Voters shared their own stories in 69% of
  full conversations and 12% of video-only ones. The effects survive an
  opposing advertisement shown mid-survey.
- **Experiment 3 (phone, same areas).** 6,879 treatment and 6,888 placebo
  in 12,081 households; 2,637 reached; conversations of 6.6 minutes.
  Prejudice index pooled d = 0.05 (t = 3.60); policy index pooled 0.03
  (t = 2.00), neither wave significant alone.
- **Not contact.** The effects do not depend on whether the canvasser is
  an immigrant (d = 0.12 and 0.08) or transgender, or on the voter's
  party; the authors take this to rule out brief contact as the
  mechanism, while noting (fn. 3) that a canvass meets few of Allport's
  conditions.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A canvass with non-judgmental narrative exchange reduced exclusionary immigration attitudes, measured over about 4.5 months | moderate | Exp. 1, pooled indices; the latest prejudice wave alone is p < 0.08 |
| C2 | Removing the narrative exchange removed the effect | moderate | Exp. 1, Full against Abbreviated pooled; confounded with a halved length; not significant at 1 month |
| C3 | The participants' own narratives are not necessary: a stranger's video narrative, discussed non-judgmentally, did as well | weak to moderate | Exp. 2; the arms' difference is imprecise |
| C4 | The strategy works by phone, with a smaller effect | moderate | Exp. 3 |
| C5 | The mechanism is the reduced threat to self-image | weak | theory from lab work; no mechanism is manipulated or measured |
| C6 | Contact with an outgroup canvasser is not what drives the effect | moderate | no moderation by canvasser identity, OA tables not read here |

## Concepts

- **Non-judgmental exchange of narratives**: persuading by giving and
  eliciting stories of relevant personal experience while listening
  without judgement to the views expressed. It joins narrative persuasion
  (Green and Brock; Slater and Rouner) and "high-quality listening"
  (Itzchakov, Kluger and Castro).
- **Analogic perspective-taking**: understanding another's situation by
  recalling a parallel one of one's own (Gehlbach and Brinkworth). The
  2016 study's proposed mechanism; Experiment 2 shows it is not necessary.
- **Self-persuasion**: the voter stating aloud implications of the
  narratives that run against the view stated earlier. Reported from
  canvassers' debriefs only.

## Connections

The sequel to Broockman and Kalla (2016, Science), which it reinterprets:
that study's scripts already exchanged narratives non-judgmentally, so its
effect need not have run through analogic perspective-taking. Paluck, Green
and Green's contact review (LIT-1420) includes the 2016 canvass among its
27 randomized studies, as one of the three pre-registered ones whose
pooled effect is near zero; this paper's own effects are of the same small
order. It draws its theory from lab work on self-affirmation (Cohen,
Aronson and Steele) and on listening.

## Bearing on the record

- **CASE-147.** The case's description is right on the reading and can be
  made exact. "Arguments alone did not produce comparable effects": the
  Abbreviated arm's pooled effect is d = 0.02 (p = 0.27), and its
  difference from the full arm is 0.06 (p < 0.01). But the full arm was
  also twice as long, and the arms' difference is not significant at the
  1-month wave or, for prejudice, at 3–6 months. "Persistent" means a
  pooled effect over waves ending at about 4.5 months, the last wave's
  prejudice effect alone being p < 0.08. The case's caveat, that "the arms
  also differ in warmth, attention and length", is borne out on length by
  the paper's own footnote 8.
- **CLAIM-430 and QUESTION-262.** Experiment 2 weighs against the
  stronger reading of "taking part": a stranger's video narrative, with
  voters sharing their own stories in 12% of conversations, did as well as
  the arm in which both parties told stories. What the arms shared was the
  non-judgmental conversation about a narrative, not the voter's own
  enactment. The paper is also silent on QUESTION-262's other contrasts:
  it measures no behaviour and no generalization to other groups.
- **CLAIM-275.** Not tested. The paper does not ask whether conduct came
  before the revised view; its outcomes are attitudes reported in a later
  survey.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Small effects, self-reported.** The authors say so: d = 0.08 and 0.04
  are small by social psychology's conventions, and changing aggregate
  opinion would need very many conversations. No behaviour, implicit
  measure or vote is observed.
- **The isolating contrast is one experiment, and confounded with length.**
  Only Experiment 1 has an argument-only arm.
- **Mechanism untested**, as the authors say.
- **Errors and slips.** Two p-values do not match their t-statistics:
  Experiment 2's prejudice index at 1 month, t = 3.01, is given as
  p < 0.001 (two-sided normal p ≈ 0.003), and Experiment 3's prejudice
  index at 1 week, t = 3.20, as p < 0.001 (p ≈ 0.001). Neither changes a
  conclusion. The first wave of Experiment 1 is "4 days" in the text and
  "1 Week" in Figure 1. "A policy index as a prejudice index" (p. 16) is a
  garbled phrase. These are in the accepted manuscript; the published
  version was not checked.

## Open questions

- Does the narrative exchange beat an argument-only conversation of equal
  length?
- Does the attitude change show in conduct toward members of the group, or
  toward other groups?
- Which part carries the effect, the narrative or the non-judgmental
  listening? No arm separates them.
