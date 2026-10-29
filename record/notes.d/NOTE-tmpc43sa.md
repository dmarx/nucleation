---
status: Read
paper: LIT-tmpg3ver
title: 'Managing the Terror of Publication Bias: A Systematic Review of the Mortality Salience Hypothesis'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full from the authors' accepted version on PsyArXiv (kvcmg,
    TMTReviewFinal.docx), from OSF, under APA's copy-of-record notice:
    body, two tables, figure captions and footnotes; the figures and the
    Supplementary Online Material were not read. Not compared with the
    published text in JPSP 129(1). The copy has no page numbers, so
    citations are by section. Read in place of Burke, Martens & Faucher
    2010 (LIT-tmp2s109), whose figures it restates and whose analysis it
    re-runs with bias corrections.
date: '2026-10-29'
summary: >-
  Re-runs Burke et al.'s meta-analysis of the mortality-salience
  hypothesis on a decade more data, with five tools for bias. Uncorrected,
  635 effects give g = 0.81 (about r = .37), close to Burke et al.'s
  r = .35. Selection models (g = 0.36) and WAAP-WLS (g = 0.39) put the
  average near r = .18; PET-PEESE finds no positive effect. A p-curve of
  825 focal tests finds evidential value at 25% average power; z-curve
  puts the expected replication rate at 19% and the expected discovery
  rate at 8%. Five of nine preregistered replications succeeded. True
  effects are so heterogeneous that 95% of them span r = −.47 to .66. The
  authors conclude some MS effects are real, the average is about half
  the published one, and most studies could not detect it.
---
<!-- inactive-ok-file: LIT-tmp2s109 LIT-tmpd9qw4 LIT-tmpcbh59 QUESTION-tmpruhu4 CLAIM-tmpjylq8 CLAIM-tmprudek — Deferred, Open or Proposed; the meta-analysis this stands in for, unread TMT and legacy works, and the question and claims it bears on -->

# NOTE-tmpc43sa: Managing the Terror of Publication Bias: A Systematic Review of the Mortality Salience Hypothesis

## Contribution

The largest assessment of the mortality-salience (MS) literature, and the
first to correct it for publication bias and p-hacking. It codes the
literature twice: once as Burke et al. (2010) did, for simple MS-versus-
control effects, and once for the focal test of each study, as p-curve
requires. It runs five tools on the result and reports that they
disagree. Its second contribution is methodological: no single tool
should be trusted to judge a literature.

## Key insight

Burke et al.'s moderate effect is reproduced exactly when the same
uncorrected method is used, and shrinks by about half, or to nothing,
when publication bias is modelled. The literature is also so
heterogeneous that an average says little about any one paradigm: under
the selection model, 95% of the true effects lie between g = −1.05 and
1.77 (r = −.47 to .66). The authors' conclusion (Conclusion): the
literature "contain[s] studies that appear to be testing nonzero effects,
although the literature is highly heterogeneous and underpowered,
rendering many individual effects to be likely spurious."

## Assumptions

- **TMT in brief** (Introduction). People manage the anxiety of knowing
  they will die by defending cultural worldviews "to achieve feelings of
  symbolic immortality". Because a culture outlasts its members, they
  share its immortality by bolstering it or living up to its standards.
- **Only the MS hypothesis is assessed**, not the anxiety-buffer or
  death-thought-accessibility hypotheses. Defenses are distal (worldview
  defense, strongest after a delay) or proximal (such as resolving to live
  more healthily, when death is consciously in mind).
- **Direction is taken from the authors.** Effects in the predicted
  direction are coded positive, against it negative. The authors grant
  that HARKing can bias this.
- **Published, English, peer-reviewed only.** Dissertations were
  excluded so that p-curve, which uses only significant results, and the
  other tools work on comparable literatures.
- **Not preregistered.** An analysis plan was posted on OSF at the
  outset, but the analyses changed in revision (Statement of
  Limitations).

## Key results

- **Search** (Methods). PsycINFO, prior reviews' references and the TMT
  website gave 1,373 manuscripts. After exclusions, the remaining papers
  held 1,396 studies.
- **Burke et al. as reported** (Past Evaluations; Results of Traditional
  Meta-Analysis). The most extensive earlier meta-analysis: random
  effects over 277 studies, average r = .35, no bias correction. Yen and
  Cheng (2013) re-analysed it and found experimenter effects accounted for
  much of the variance. This review adapts Burke et al.'s search and
  selection rules so its uncorrected result can be compared directly.
- **Traditional meta-analysis**: 643 effects coded, 8 with g > 5 dropped
  as likely reporting errors, leaving 635 tests from 557 studies.
  - g = 0.805, 95% CI [0.757, 0.854], τ = .533; about r = .37.
    Heterogeneity Q(634) = 2972.7.
  - The funnel plot is strongly asymmetric.
  - Dropping the largest 10% (64 effects): g = 0.622, about r = .30.
- **Selection model** (three thresholds, JASP defaults). 430 significant,
  69 marginal, 130 non-significant and 6 "surprising" effects.
  - Non-significant effects are estimated published at .259 the rate of
    significant ones.
  - Adjusted g = 0.357, 95% CI [0.168, 0.546], τ = 0.716, p < .001;
    about r = .18. Without the largest 10%: g = 0.457, about r = .22.
- **PET-PEESE.**
  - PET gave a significant negative estimate: g = −0.114, 95% CI
    [−0.202, −0.026], t(633) = −2.527, p = .012. By the procedure's rule,
    no positive PET effect means no evidence for MS, and PEESE is not
    read.
  - The authors judge the negative estimate spurious: PET underestimates
    under heterogeneity, small samples and p-hacking.
  - Without the largest 10%: PET g = 0.035, p = .322; still no effect.
- **WAAP-WLS.** Only 139 of 635 effects (21%) had 80% power. Their
  estimate: g = 0.385, 95% CI [0.340, 0.430]; about r = .19. Without the
  largest 10%: g = 0.354.
- **p-curve** (825 studies; one or two focal tests each).
  - Significant right skew: half curve Z = −13.76, full curve Z = −14.23,
    both p < .001. So some studies test non-zero effects.
  - Average power 25%, 90% CI [21%, 29%], below the 33% benchmark.
  - Mean N was 114, about 57 per cell, enough to detect r = .18 with
    27% power.
  - Without the largest 10%: right skew holds (full Z = −4.08; half
    Z = −1.42, p = .0785), but estimated power falls to 8%.
- **z-curve** (the same 825 tests).
  - Expected replication rate (ERR) .19, 95% CI [.13, .26]: an exact
    replication of a published significant effect would succeed about one
    time in five.
  - Expected discovery rate (EDR) .08, 95% CI [.05, .17], close to the
    5% a literature of only null effects would give.
  - Without the largest 10%: ERR and EDR both .06.
- **Preregistered replications.** Of 9 found, 5 supported the MS
  hypothesis (Arnoult et al. 2023; Courtney et al. 2022; Dunn et al.
  2020; Schindler et al. 2019; Vail et al. 2019) and 4 did not
  (Rodríguez-Ferreiro et al. 2019; Sætrevik and Sjåstad; Schindler et al.
  2021 and 2022). Those studies were powered on published, likely
  inflated, effects.
- **Many Labs 4** (Past Evaluations; General Discussion). Reported as 21
  labs, 2,220 participants and g = 0.03. Chatard et al. (2020), the
  original authors' critique, re-analysed only the sites that met the
  preregistered minimum and found g = 0.13, p = .045, for the
  author-advised sites under one exclusion rule, and nothing under the
  others.
- **Two takes** (What Can We Conclude).
  - Liberal: p-curve, selection models and WAAP-WLS find an effect; five
    of nine preregistered studies replicated; studies after 2011, and
    those with longer delays or at least two distractor tasks, look
    better in the SOM.
  - Conservative: z-curve's EDR is near the null; PET-PEESE finds nothing
    in any subgroup; Many Labs 4 failed; conditional power is 19–25%.
  - Reconciled: effects are real in some studies, highly heterogeneous
    and mostly underpowered. Replications should assume r = .18, follow
    expert protocols, and expect conceptual replications to fail more
    often.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Uncorrected, the MS literature yields a moderate-to-large average effect (about r = .37), matching Burke et al. 2010 | strong as a replication of the method; the authors reject the estimate as inflated | traditional meta-analysis |
| C2 | Corrected for publication bias, the average MS effect is small, about r = .18 | moderate: two tools agree; a third finds no effect; all three are known to misbehave under this literature's heterogeneity and p-hacking | selection models, WAAP-WLS, PET-PEESE |
| C3 | Some published MS studies test non-zero effects | moderate to strong: p-curve right skew survives dropping the largest effects; p-curve's null is that every effect is zero | p-curve, z-curve ERR |
| C4 | Most MS studies are underpowered and many published effects are likely spurious | moderate: 25% (p-curve) and 19% (z-curve) conditional power, 8% unconditional power, 21% of effects adequately powered | p-curve, z-curve, WAAP |
| C5 | MS effects vary so much across designs that an average is of limited use | strong: τ = .72; the 95% range of true effects spans negative to large positive | selection model |
| C6 | Replications fare better with expert guidance and strict protocols | weak: rests on Chatard et al.'s re-analysis under one exclusion rule and on SOM subgroups not read here | General Discussion |

## Concepts

- **mortality salience (MS) hypothesis**: reminders of one's death
  increase defense of one's cultural worldview.
- **symbolic immortality**: in TMT, the sense of outliving death by
  belonging to, upholding or living up to a culture that will outlast
  one.
- **distal and proximal defenses**: worldview defense after death thoughts
  leave attention, against direct responses such as health resolutions
  while death is in mind.
- **selection model, PET-PEESE, WAAP-WLS**: corrections that model
  publication by p-value, regress effect on standard error, or keep only
  adequately powered studies.
- **p-curve; ERR and EDR**: the distribution of significant p-values;
  z-curve's power of published significant studies (ERR) and of all
  studies run, file drawer included (EDR).

## Connections

- **Burke, Martens and Faucher 2010 ([LIT-tmp2s109](../literature.d/LIT-tmp2s109.md))**, the work this note
  stands in for. The review takes its search and selection rules, its
  pooled r = .35 over 277 studies, and its subgroup ideas (with
  Pyszczynski et al. 2015). It reproduces the uncorrected result and then
  corrects it.
- **Many Labs 4 (Klein et al. 2022)**, read alongside. The review's
  figures for it (21 labs, 2,220 participants, g = 0.03) do not match the
  accepted version the record read (2,281 collected, 1,550 analysed,
  g = 0.07). They may come from the first preprint.
- **Lifton ([LIT-tmpcbh59](../literature.d/LIT-tmpcbh59.md))** is not cited. The review traces symbolic
  immortality to Becker (1973).
- **Castano et al. ([LIT-tmpd9qw4](../literature.d/LIT-tmpd9qw4.md))** is not named. Its outcomes,
  in-group identification and bias, are among the many worldview-defense
  measures the review pools.

## Bearing on the record

- **The legacy question ([QUESTION-tmpruhu4](../questions.d/QUESTION-tmpruhu4.md)).** The question cites
  Burke et al. as the evidence for TMT, whose account is the record's
  route from death to an enlarged self: people defend the worldview and
  group that will outlast them, for symbolic immortality. What this
  review changes, as inference:
  - **The effect is smaller and less certain than the question assumes.**
    The best-supported average is about r = .18, half Burke et al.'s;
    one correction finds none; the expected discovery rate is near the
    null. Whether a given study's effect is real cannot be read from its
    publication.
  - **It is not gone.** p-curve's right skew says some MS studies test
    real effects. The review cannot say which. Subgroups with longer
    delays and post-2011 studies look better, by the authors' report of
    an SOM the record has not read.
  - **The mechanism is untested.** The review assesses whether death
    reminders change worldview defense, not whether the change is a
    search for symbolic immortality. That reading belongs to the theory.
    Even a robust effect would support the extended-self interpretation
    only as the theory's gloss.
- **The owner's thesis ([CLAIM-tmpjylq8](../claims.d/CLAIM-tmpjylq8.md)).** The thesis does not depend on
  TMT. TMT is a candidate mechanism for enlarging the self under threat,
  across a group and past death. It is now a weak one to cite: a small,
  highly variable effect whose core paradigm failed in Many Labs 4.
- **The triviality objection ([CLAIM-tmprudek](../claims.d/CLAIM-tmprudek.md)).** The MS literature's
  outcome measures, worldview defense in many forms, record evaluative
  attachment to one's group and its standards. Those are measures of
  caring, not of the self's extent apart from caring. The review offers
  no criterion of the kind the objection asks for (an inference).
- **A dated note should be added to [QUESTION-tmpruhu4](../questions.d/QUESTION-tmpruhu4.md)**, jointly with
  Many Labs 4. The proposed text is in the Many Labs 4 draft; the part
  this review supplies: "Chen et al. (NOTE-tmpc43sa) reproduce Burke et al.'s
  uncorrected effect (r = .37 over 635 effects, against .35 over 277) and
  then correct it for publication bias: selection models and WAAP-WLS
  give about r = .18, PET-PEESE no effect, and z-curve an expected
  discovery rate of 8%. Some mortality-salience effects are real, but
  the average is about half the published one and most studies could not
  detect it." No note is needed on [CLAIM-tmpjylq8](../claims.d/CLAIM-tmpjylq8.md).
- **[LIT-tmp2s109](../literature.d/LIT-tmp2s109.md)'s summary should be checked.** "A moderate effect" is
  right for Burke et al. (r = .35). The record now holds a source for the
  figure but not for its moderators, such as delay.
- **No THEORY filed.**
- **No ML instruction.**

## Limitations

- **The figures and SOM were not read.** The subgroup results behind the
  "liberal take" (delay, distractors, post-2011 studies, country) are
  reported only in summary.
- **Quality was not checked study by study**, by the authors' own
  account. A few errors were found and corrected or dropped.
- **Pooling across heterogeneous paradigms.** The authors say an average
  over well- and badly-designed studies may misrepresent both.
- **Inconsistencies in the copy.**
  - The search arithmetic does not close: 1,396 studies less 578
    excluded is 818, not the 825 analysed.
  - Mean per-cell N is given as about 57 (Results of P-Curve) and as
    about 28 (A Conservative Take).
  - Table 1 gives PET as g = −0.14 and WAAP as "13% of effects"; the text
    gives −0.114 and 21% (139 of 635).
  - Many Labs 4 is described as 21 labs and 2,220 participants with
    g = 0.03, against 2,281, 1,550 and 0.07 in its accepted version.
  - Sætrevik and Sjåstad are dated 2022 in one place and 2019 in another.
- **Typos.** "Hedge's g" throughout; "Stanley and Douliagos";
  "Iaonnidis"; "Simmons, Nelson, & Simonsohn, 2014a" for Simonsohn et al.;
  "expected replication rate (EDR)" where ERR is meant; "worth nothing"
  for "worth noting"; "performed in in the R"; "Sladevokova" in the
  references; a garbled sentence in Results of Selection Models where
  text has dropped out ("nonsignificant effects (one tailed .05 ≤
  pour universe of studies yielded").

## Open questions

- Which MS paradigms carry the real effects? The authors' Shiny
  application and coded data allow subgroup p-curves; a subgroup of
  studies whose outcome is identification with a lasting group (the
  Castano et al. design) would bear most directly on the legacy question.
- Does any MS study measure symbolic immortality, the putative mediator,
  rather than inferring it from worldview defense?
