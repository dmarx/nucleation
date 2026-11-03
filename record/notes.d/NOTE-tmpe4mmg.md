---
status: Read
paper: LIT-tmpgv3da
title: 'Levine et al. — Need frustration, negative affect and depressive symptoms'
version: 1
history:
- version: 1
  date: '2026-11-03'
  note: >-
    Read in full from the version of record, as Europe PMC's full-text
    XML of PMC8635315 (in the PMC Open Access Subset for the duration of
    the WHO COVID-19 declaration). Springer's PDF returned a client
    challenge and was not pursued. I read the abstract, the introduction,
    both studies' methods and results, Tables 1–5, the captions of
    Figures 1 and 2 (the figures themselves not seen), the general
    discussion, limitations, conclusion and footnotes. Not read: the OSF
    supplements (attrition analysis, the latent SEM and random-intercept
    cross-lagged models, syntax and output), which the paper cites for
    analyses it does not report. No page numbers are in the XML; the
    article is Motivation and Emotion 46(1), 126–136, and locations are
    given by study and table.
date: '2026-11-03'
summary: >-
  Two cross-lagged panel studies of university students: three waves
  over the 2018–19 academic year (N = 379) and two waves six weeks apart
  at the start of the COVID-19 pandemic (N = 235). Need frustration (the
  nine dissatisfaction items of the BMPN) predicted later depressive
  symptoms (β = .13 and .17; .18) and later negative affect, while
  negative affect predicted neither later depression nor, at the first
  lag, need frustration; depression predicted later need frustration at
  the first lag of Study 1 (β = .20). Other-reported depression was
  predicted marginally (β = .14, p = .074). Self-report, single-construct
  outcome, no random intercepts in the reported models.
---
<!-- inactive-ok-file: THEORY-052 QUESTION-tmpee04a — Proposed, Open or registered unread; the entries this reading bears on, cited as open -->

# NOTE-tmpe4mmg: Levine et al. — Need frustration, negative affect and depressive symptoms

## Contribution

It asks whether need frustration predicts depressive symptoms once negative
affect, which overlaps both, is in the same model, and whether it comes
before them or with them. Two student samples, one an ordinary academic year
and one the first six weeks of the pandemic, give the same answer: of the
three variables, need frustration was the one whose earlier score predicted
the others' later scores.

## Key insight

The study tests incremental validity over time against the nearest rival,
general negative affect, rather than against low satisfaction. In both
samples the frustration → later depression and frustration → later negative
affect paths are significant, and the negative affect → later depression
path is not (Tables 2 and 4). The authors read this as "need frustration is
an antecedent of depressive symptoms over time" (abstract).

## Assumptions

- **Measures.** Negative affect: five adjectives such as "unhappy" and
  "frustrated", cited to Emmons (1992), 7-point. Need frustration: "the
  9-item Balanced Measure of Psychological Needs scale (BMPN)", three items
  per need ("I feel lonely"; "I experienced some kind of failure or was
  unable to do well at something"; "I feel pressured in my life"), averaged
  into one score. Depressive symptoms: the CESD-R 10, averaged.
- **The BMPN items are its dissatisfaction half.** The BMPN has 18 items,
  satisfaction and dissatisfaction (Kermavnar et al., Table 3); the paper
  uses nine negatively worded ones and calls them frustration. Satisfaction
  was not modelled.
- **Model.** Fully cross-lagged path models in Mplus, observed variables,
  FIML; standardized coefficients (STDYX). Within-wave covariances
  estimated. No random intercepts in the reported model: footnote 3 says a
  latent SEM and a random-intercept model were tried, and are on OSF.
- **Samples.** Study 1: a Canadian university, Mage 20.44, 85% female;
  80% retained across three waves (T1 379, T2 333, T3 304). Study 2: the
  same university, 83% female, two waves in April and late May 2020; 242
  and 200 combined family and peer reports.

## Key results

### Study 1, the academic year (Table 2)

- Autoregressive paths all significant (e.g. depression .46 then .26;
  frustration .43 then .32).
- **Need frustration → later depression**: T1→T2 β = .13 [.03, .25],
  p = .01; T2→T3 β = .17 [.03, .31], p = .02.
- **Need frustration → later negative affect**: T1→T2 .18 [.06, .29],
  p = .002; T2→T3 .16 [.02, .31], p = .02.
- **Negative affect → later depression**: −.01, p = .85; .10, p = .25.
- **Depression → later need frustration**: T1→T2 .20 [.05, .34], p = .007;
  T2→T3 .01, p = .88. Depression → later negative affect: .19, p = .007;
  .01, p = .97.
- **Negative affect → later need frustration**: T1→T2 −.07, p = .27; T2→T3
  .17 [.01, .34], p = .04.
- Fit: χ²(9) = 36.77, p < .001, RMSEA = .09 [.06, .12], CFI = .979,
  SRMR = .048, called "good fit".
- Within-wave correlations of frustration with depression .56, .67, .62
  (Table 1).

### Study 2, the pandemic (Table 4)

- **Need frustration → later depression** .18 [.04, .32], p = .010; →
  later negative affect .17 [.03, .30], p = .018.
- Negative affect → later depression .07, p = .287; depression → later
  frustration −.01, p = .987; negative affect → later frustration .09,
  p = .287. "The only significant cross-lagged predictor was need
  frustration."
- The model is just-identified, so no fit is reported.
- **Others' reports (Table 5).** Predicting May 2020 other-reported
  depression ("is someone who is depressed", "can be moody"; α = .62, .67),
  controlling for the September 2019 report: baseline .62, p < .001;
  self-reported frustration .14 [−.01, .29], p = .074; self-reported
  depression .08, p = .397; negative affect .03, p = .743. R² = .486.

### The authors' conclusions (Discussion)

- Need frustration is "an antecedent and concomitant of depressive
  symptoms", and the research "further implicates need frustration as a
  transdiagnostic risk factor, as it was both a predictor of negative
  affect and depressive symptoms longitudinally".
- The others' reports "remove the problem of shared method variance that
  plagues self-report studies in this area".
- Limitations they state: personality not controlled (Nishimura & Suzuki
  2016 found it attenuates need–well-being links); one affect measure;
  samples underpowered for a full latent SEM; "cannot be used as evidence
  for causation".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Earlier need frustration predicts later depressive symptoms, controlling for earlier depression and negative affect, in students | moderate | three significant lagged paths over two samples, β .13–.18; self-report; observed-variable CLPM without random intercepts |
| C2 | Negative affect does not predict later depressive symptoms once need frustration is in the model | moderate | non-significant in all three lags; one five-adjective affect measure |
| C3 | Need frustration precedes depression rather than following it | weak | the reverse path was significant at the first lag of Study 1 (β = .20, larger than the forward .13) and not elsewhere; two-wave Study 2 cannot separate them |
| C4 | Need frustration predicts depression as seen by others | weak | β = .14, p = .074, two short items with α .62 and .67 |
| C5 | Need frustration is a transdiagnostic risk factor | weak | the outcomes are depressive symptoms and negative affect, one disorder and a mood state; asserted in the discussion |

## Concepts

- **Need frustration (as measured here)** — the mean of the BMPN's nine
  negatively worded items, described as "the active thwarting of one's
  needs" in the introduction.
- **Antecedent / concomitant** — a variable that predicts another's later
  value net of its own earlier value, versus one correlated with it at the
  same time.
- **Fully cross-lagged path model** — every variable at each wave regressed
  on every variable at the previous wave.

## Connections

- **Campbell et al. 2018** ([LIT-tmpazv5c](../literature.d/LIT-tmpazv5c.md)) is cited as showing need
  frustration "mediates the relationship between negative environments and
  depressive symptoms", and among works using it as a mediator. Its sample
  was self-critical perfectionism, not environments.
- **Cordeiro et al. 2016** and **Vermote et al. 2021** are named as the
  only prior multi-wave studies of need frustration and ill-being.
- **Sheldon and Hilpert 2012**: the BMPN.

## Bearing on the record

- **[THEORY-052](../theory.d/THEORY-052.md).** It is prospective evidence the record lacked, and it
  meets part of the promote_when ("prospective studies in which
  frustration … predicts") and fails the rest. One kind of disorder, not
  more: the outcomes are depressive symptoms and negative affect, so the
  authors' "transdiagnostic" is unsupported by their own design. The
  measure is a self-report of the kind the promote_when excludes: "I feel
  lonely" is a frustration item here, and loneliness is a depressive
  symptom on the CES-D 10 (that the CESD-R 10 used has a loneliness item is
  from the instrument, not this text). The outcome is symptom level, not
  first onset. And the reverse path, depression → later frustration, was
  as large as the forward one at the first lag of Study 1, which is the
  "vicious cycle" [THEORY-052](../theory.d/THEORY-052.md) already notes from [LIT-561](../literature.d/LIT-561.md). It does strengthen
  the claim that frustration predicts depression beyond negative affect,
  which the theory's "What this does not say" does not yet record.
- **[LIT-tmpjcuzb](../literature.d/LIT-tmpjcuzb.md) (Murphy et al.).** Levine's frustration score is the BMPN's
  negative half with no satisfaction half modelled, and the rival it beats
  is also a negatively valenced self-report. So the keying objection does
  not bite in its BPNSFS form (no satisfaction comparison is made), but the
  result is "a negatively worded need report predicts a negatively worded
  symptom report six weeks to four months later", and does not show that
  what predicts is frustration rather than low satisfaction.
- **[CLAIM-368](../claims.d/CLAIM-368.md)** separates frustration from distress as constructs in an
  organization. This paper separates their measures in individuals: need
  frustration and negative affect correlate .40–.67 within waves, yet
  their lagged roles differ. That is a parallel, at the individual and felt
  level, for the claim's "distinct from distress"; it is not evidence for a
  claim about organizations, and the claim does not need it.
- **[QUESTION-tmpee04a](../questions.d/QUESTION-tmpee04a.md).** Frustration predicting depression is the
  well-being route to need-hood again: a symptom report, not a functional
  deficit.
- **THEORY filed from this reading**: [THEORY-tmpymwd8](../theory.d/THEORY-tmpymwd8.md) (Active), the
  reported lagged paths and what they do not show.
- **No instruction for machine-learning practice.**

## Limitations

- **No random intercepts in the reported models.** A traditional CLPM mixes
  stable between-person differences into its lagged paths; the
  random-intercept model the authors tried is only on OSF. The lagged
  coefficients are therefore not within-person effects.
- **Students, mostly women**, at one Canadian university; Study 2 at a
  single six-week window of the pandemic.
- **Fit.** Study 1's RMSEA of .09 is at the poor end of the usual range,
  though called good; Study 2's model is saturated.
- **Study 2's Table 3 repeats Study 1's descriptives.** Its means and SDs
  for T1 and T2 depression, negative affect and frustration (2.06 (0.51),
  3.50 (1.08), 3.64 (1.10), 2.29 (0.61), 3.95 (1.28), 4.02 (1.25)) are
  identical to Table 1's for Study 1's first two waves, while the
  correlations differ. One of the two is a copying error; the paper does
  not say which. Study 2's sample is also described as "this year-long
  online study" though its waves were six weeks apart (it was part of a
  longer project).
- **The affect measure.** Five adjectives, among them "frustrated", cited
  to Emmons (1992); one negative-affect item names frustration, so the two
  predictors share a word.
- **Others' reports** are two Big Five items averaged over family and
  peers, α .62 and .67, and the frustration effect on them is not
  significant at .05.

## Open questions

- Do the forward paths survive a random-intercept cross-lagged model? The
  OSF supplement may say.
- Does frustration predict depression beyond low satisfaction, with keying
  balanced? The design leaves satisfaction out.
- Does the same score predict a second kind of disorder, or first onset?
