---
status: Read
paper: 'LIT-1405'
title: 'Pettigrew and Tropp — Meta-analytic tests of three mediators of contact'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from the published article's PDF in a
    University of Washington course's readings folder
    (https://courses.washington.edu/pbafhall/563/Readings/pettigrew.pdf,
    13 pages, EJSP 38, 922–934, Wiley's 2008 copyright line), under the
    owner's ruling of 2026-10-29 that course-page copies count. Text
    extracted with pdftotext, plain and layout. Read: the abstract, the
    introduction, the method, Tables 1–3, the results and discussion,
    the limitations, the footnote, the reference list and the list of
    studies in the meta-analyses. Figure 1 (the saturated path model) is
    an image; its coefficients were not read and none is used. The
    extraction drops minus signs in the tables; signs are restored from
    the table's printed plus signs and the text's convention that a
    negative r means less prejudice. Checked: the six Sobel statistics
    of Table 3 recomputed from its coefficients and standard errors
    (record script, 2026-10-29), which found one wrong; the sample
    counts; the footnote's 26% (1 − .95⁶ = .265).
date: '2026-10-29'
summary: >-
  Meta-analytic mediation tests over 54 studies of contact and prejudice
  that also measured knowledge of the outgroup (17 samples), intergroup
  anxiety (60) or empathy and perspective taking (14). All three
  mediate. Knowledge is much the weakest (Sobel Z = 3.87); anxiety
  reduction (26.6) and empathy (12.4) are strong, and in nine samples
  measuring both, anxiety and empathy together account for about half of
  the contact–prejudice covariance.
---
<!-- inactive-ok-file: CLAIM-417 LIT-1700 LIT-1728 — Proposed or Unavailable; a claim cited as what this reading bears on and works cited as registered, nothing here rests on their being settled or read -->

# NOTE-tmpdp52y: Pettigrew and Tropp — Meta-analytic tests of three mediators of contact

## Contribution

It turns the question of how contact reduces prejudice into a
quantitative comparison. Three mediators proposed in the literature are
tested on the same footing, by pooling, for each, the three correlations
a mediation test needs and running a Sobel test on the pooled matrix.
The result moves the weight of the explanation from what contact teaches
about the outgroup to what it does to feeling: anxiety goes down,
empathy goes up.

## Key insight

Contact mostly works through affect. Learning about the outgroup, the
mid-century account, does mediate, but weakly; reduced anxiety about
intergroup interaction and increased empathy and perspective taking
mediate strongly. Anxiety correlates with both of the others, which
suggests, untested, a sequence in which anxiety must fall before empathy
and knowledge can do their work.

## Assumptions

- **Mediation from pooled correlations.** For each mediator, the
  contact–mediator, mediator–prejudice and contact–prejudice
  correlations are meta-analysed over the same samples, a structural
  model gives the two path coefficients and their standard errors, and
  the Sobel test is applied (Shadish 1996; Premack and Hunter 1988).
- **Random effects**, inverse-variance weights, Pearson r; then a
  repeat on homogeneous subsets formed by dropping outliers until Q is
  non-significant.
- **The file** is the 515 studies of the 2006 meta-analysis ([LIT-1413](../literature.d/LIT-1413.md))
  plus studies through June 2005 that measured a mediator; same
  inclusion rules, with the added requirement that the mediator's
  relations be reported.
- **Correlational**: the mediation is statistical, and the authors say
  causal influence cannot be inferred from it.

## Key results

- **Samples.** Knowledge: 11 studies, 17 samples, 2,543 participants.
  Empathy and perspective taking: 9 studies, 14 samples, 2,362.
  Anxiety: 45 studies, 60 samples, 13,343. 54 studies in all; one tests
  all three mediators.
- **Pooled correlations, all samples (Table 1).** Knowledge: contact →
  knowledge +.22, knowledge → prejudice −.14, contact → prejudice −.30.
  Anxiety: contact → anxiety −.29, anxiety → prejudice +.37, contact →
  prejudice −.29. Empathy: +.35, −.41, −.37.
- **Sobel tests (Table 3, text).** All samples: knowledge Z = 3.87,
  anxiety 26.55, empathy 12.43, all p < .001. Homogeneous subsets:
  3.64, 13.44, 9.87. The pattern is the same in both.
- **Mediators intercorrelated**, in the few samples with two or more:
  anxiety with knowledge r = −.24 and with empathy −.32; knowledge with
  empathy +.05, n.s.
- **Joint model.** In the nine samples with contact, prejudice, anxiety
  and empathy, both mediate in a saturated path model and together
  account for "roughly half" of the contact–prejudice covariance.
- **Publication status.** No path involving knowledge or empathy
  differs by publication. Contact → anxiety is stronger in unpublished
  samples (−.36) than published (−.28), QB(1) = 3.72, p = .05, the
  opposite of what publication bias would produce.
- **Contact–prejudice is larger here** (−.29 to −.37) than the 2006
  mean of −.21; the authors attribute it to half these studies being
  post-2000 and to the rising rigor of later studies.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Knowledge of the outgroup, intergroup anxiety and empathy each statistically mediate the contact–prejudice association | moderate | Table 3, all and homogeneous samples |
| C2 | Knowledge is a markedly weaker mediator than anxiety reduction and empathy | moderate | Table 3; but different sample sets per mediator |
| C3 | Anxiety and empathy together carry about half the association | weak | nine samples, saturated model |
| C4 | Anxiety must fall before empathy and knowledge can work | weak | suggested from intercorrelations; untested |
| C5 | Publication bias does not drive these mediation results | moderate | publication-status comparisons |

## Method

Four steps per mediator: weight each sample's correlations by inverse
variance (Wilson's SPSS macros); pool the three-variable matrix; fit a
structural model for the unstandardized contact → mediator coefficient
and the mediator → prejudice coefficient with contact held constant,
each with its standard error; apply the Sobel test. Repeated on
homogeneous subsets obtained with DSTAT by removing extreme outliers.

## Concepts

- **Knowledge**: learning about the outgroup through contact, the
  mediator of Allport and the Human Relations Movement.
- **Intergroup anxiety**: after Stephan and Stephan (1985), the threat
  and anxiety aroused by the prospect or fact of cross-group
  interaction.
- **Empathy and perspective taking**: taken together, since too few
  studies allow them to be separated; perspective taking is "a more
  cognitive dimension of empathy".

## Connections

The mediators are three of the processes in Pettigrew's 1998 review
([LIT-1408](../literature.d/LIT-1408.md)): learning about the outgroup, and the "affective ties" under
which that review put both anxiety and empathy. Ingroup reappraisal,
the review's fourth process, appears here only in the list of mediators
not tested ("broadened views of the ingroup"). The file of studies is
the 2006 meta-analysis's ([LIT-1413](../literature.d/LIT-1413.md)). The empathy line is Batson's: the
1997 study it cites, on empathy for a stigmatized member improving
attitudes to the group, is not registered; the record holds other
Batson work ([LIT-1700](../literature.d/LIT-1700.md), [LIT-1728](../literature.d/LIT-1728.md), [LIT-1783](../literature.d/LIT-1783.md)).

## Bearing on the record

- **[CLAIM-275](../claims.d/CLAIM-275.md)**: the paper supports contact acting on feeling before
  belief: anxiety reduction and empathy carry more of the association
  than knowledge does. But its mediation is cross-sectional and
  statistical, and the sequence it suggests (anxiety first) is
  proposed, not shown.
- **[CLAIM-417](../claims.d/CLAIM-417.md)** (perspectives revised by being made one of several):
  the perspective-taking leg is the nearest the paper comes, and it
  could not separate perspective taking from empathy. Nothing here tests
  a change in how one's own view is held; that is the 1998 review's
  ingroup reappraisal, which this paper does not test.
- **[LIT-1405](../literature.d/LIT-1405.md)'s own "why this is here"** is right that knowledge mediates,
  only less strongly. The paper's words are "the mediational value of
  increased knowledge appears less strong", and in the text "simply
  knowing more about the outgroup typically does not have a major
  effect".

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Different sample sets per mediator**, so differences between the
  mediators may partly reflect the sets, as the authors say.
- **Few studies** for knowledge (11) and empathy (9); the joint model
  rests on nine samples.
- **Statistical mediation on correlational data**; reverse and
  non-recursive paths are acknowledged and not modelled.
- **Half the association is unexplained**; the authors list other
  mediators (self-disclosure, broadened ingroup views, outgroup
  variability, threat) and expect the missing ones to be affective.
- **Errors and slips.** Table 3 gives the Sobel Z for empathy over all
  samples as 4.38; its own coefficients and standard errors give 12.43,
  the value in the text, so the table is wrong. Table 3 gives anxiety's
  as 26.60, the text 26.55; recomputation gives 26.55. The method says 14
  of the 60 anxiety samples are unpublished; the publication comparison
  uses 13 unpublished and 47 published. "54 studies with 91 independent
  samples" adds the three mediators' samples (17 + 14 + 60); since at
  least nine samples measured both anxiety and empathy, there are at
  most 82 distinct samples. The knowledge-to-prejudice range "between
  +.13 and .38" is garbled in the extraction.

## Open questions

- Does anxiety reduction precede the growth of empathy and knowledge?
  The authors call for longitudinal and experimental tests.
- Do empathy and perspective taking mediate separately?
