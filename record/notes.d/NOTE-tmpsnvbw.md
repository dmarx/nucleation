---
status: Read
paper: 'LIT-1420'
title: 'Paluck, Green and Green — The contact hypothesis re-evaluated'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from the publisher's open-access PDF (CC
    BY 4.0) on Cambridge Core,
    https://www.cambridge.org/core/services/aop-cambridge-core/content/view/142C913E7FA9E121277B29E994124EC5/S2398063X18000258a.pdf/div-class-title-the-contact-hypothesis-re-evaluated-div.pdf
    (Behavioural Public Policy 3(2), 129–158, 30 pages), text extracted
    with pdftotext. Read: the abstract, every section, Tables 1–3, the
    captions of Figures 1–2, the footnotes and the references. Not read:
    the online supplementary materials (the p-hacking tests, Appendix A
    on excluded studies) and the OSF archive; no number was taken from
    the two figures. Checked: Table 1's and Table 2's counts sum to 27;
    I² = (Q − df)/Q = (173.178 − 26)/173.178 = 0.85; the random-effects
    interval 0.231–0.554 is centred on 0.39; Table 3's intervals follow
    from its coefficients and standard errors at 25 degrees of freedom;
    the sign-test probabilities, 24 of 27 and 26 of 31 positive, are
    2.5 × 10⁻⁵ and 9.6 × 10⁻⁵ under a fair coin, below the 0.001 stated
    (record script, 2026-10-29).
date: '2026-10-29'
summary: >-
  The 27 randomized contact studies with outcomes measured at least a
  day later give a random-effects average of Δ = 0.39 SD, but the
  effects are heterogeneous (I² = 0.85), shrink with precision (the
  meta-regression's intercept is −0.01), are largest for disability,
  fall to 0.25 for ethnic, racial, religious and immigrant targets, and
  are 0.016 in the three pre-registered studies. No study tests
  interracial contact on anyone over 25.
---
<!-- inactive-ok-file: LIT-1413 LIT-1408 CLAIM-430 — Unavailable or Proposed; the meta-analysis this paper updates and Pettigrew's review, unread here, and a claim cited as open -->

# NOTE-tmpsnvbw: Paluck, Green and Green — The contact hypothesis re-evaluated

## Contribution

It re-asks Pettigrew and Tropp's question (LIT-1413) of the only studies a
policy-maker can act on: those that randomly assign face-to-face contact
and measure prejudice at least a day after it begins. There are 27, of
which 8 were in the 2006 meta-analysis. Pooled, they say contact reduces
prejudice. Looked at closely, the largest and best-designed studies say
much less, and the population the hypothesis was built for, adults across
racial lines, is not studied at all.

## Key insight

A pooled average can be large while the studies that would settle the
question are small in number and small in effect. Here the estimate
shrinks toward zero as precision grows, and the three pre-registered field
trials average 0.016. So the meta-analysis "offers qualified support": it
does not show that contact fails, and it does not show that contact works
for the prejudice and population that motivated the hypothesis.

## Assumptions

- **Inclusion.** Pettigrew and Tropp's definition of contact, "actual
  face-to-face interaction between members of clearly defined groups";
  random assignment; an outcome measured at least one day after the
  intervention began (a weaker filter than one day after it ended, which
  would drop ten studies); published or circulated by July 2016.
- **One estimate per treatment arm**, chosen by eight rules: the highest
  dose, the dominant group, the latest post-test, a linear estimator, the
  authors' primary outcome, and the specification with the smallest
  apparent standard error.
- **Effect size.** Glass's Δ, the treatment–control difference over the
  control group's standard deviation, with Hedges' small-sample
  correction. Three studies' arms (four arms) lack variance information
  and enter only the sign test, leaving 25 studies and 27 arms.
- **Random effects**, the variance estimated by method of moments, since
  Cochran's Q rejects homogeneity.

## Key results

- **Coverage.** Thirteen studies use college students, six adults over
  25, seven children or adolescents; 11 address racial or ethnic
  prejudice, all with participants from elementary school through
  college. Nineteen took place in the USA. Sixteen date from 2000 or
  later. Twenty-six of 27 had authority approval; 17 are classed as equal
  status, 14 as cooperative, 12 as having a common goal.
- **Direction.** 24 of the 27 estimates are positive (26 of 31 counting
  the arms without standard errors).
- **Pooled.** Random-effects Δ = 0.39, 95% CI 0.231–0.554; Q(26) =
  173.178, I² = 0.85. Only 20 of 27 intervals cover 0.39, and four of the
  ten most precise fall below it.
- **Precision (Table 3).** Regressing Δ on its standard error: slope
  2.086 (SE 1.007, p = 0.049), intercept −0.014 (CI −0.458 to 0.430), the
  expected effect of an infinitely large study.
- **Target (F-test p = 0.01).** Disability differs most from the base
  (p = 0.001). Ethnic, racial, religious and immigrant targets: 0.25, CI
  0.08–0.42, with four of the five largest studies below it. Without the
  disability studies: 0.20.
- **Robustness.** Adding seven borderline quasi-experiments: 0.373 (SE
  0.075), target heterogeneity p = 0.0024, precision slope p = 0.058.
  The three pre-registered studies (Broockman and Kalla 2016; Scacco and
  Warren 2018; Finseraas and Kotsadam 2017): 0.016, against 0.451 for the
  rest.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Most randomized contact studies with delayed outcomes find prejudice reduced | strong | 24 of 27 positive |
| C2 | The average effect is about 0.39 SD | weak | heterogeneity, the precision gradient and the pre-registered subset all undercut it |
| C3 | Effects vary by target, largest for disability, smaller for ethnic and racial prejudice | moderate | meta-regression, p = 0.01; contradicts Pettigrew and Tropp's near-equality |
| C4 | Larger studies find smaller effects, consistent with a file drawer | weak | p = 0.049, and 0.058 with the borderline studies; "statistically equivocal" in the authors' words |
| C5 | No randomized study with delayed outcomes tests interracial or interethnic contact on adults over 25 | strong | the inventory, Table 1 |
| C6 | Allport's conditions have never been varied experimentally in such a study, so whether they are needed cannot be decided | strong | the inventory |

## Concepts

- **Policy-relevant study**: randomized assignment of contact and an
  outcome measured at least a day after the intervention began.
- **Glass's Δ**: the effect over the control group's standard deviation,
  used because pre-treatment deviations are not always reported.
- **Allport's conditions**: equal status, common goals, intergroup
  cooperation and the support of authorities, law or custom. Pettigrew and
  Tropp found them "not essential"; Allport warned that without them "the
  more contact the more trouble".

## Connections

An update of Pettigrew and Tropp's 2006 meta-analysis (LIT-1413), with
which it agrees that contact "typically reduces prejudice" and disagrees
on two things: the near-equality of effects across targets, and their
claim that "the most rigorous studies tend to provide the largest
effects". It draws studies from Lemmer and Wagner (2015) and from Paluck
and Green's 2009 review of prejudice reduction. Its sample includes
Broockman and Kalla's 2016 canvass, whose sequel is Kalla and Broockman
(LIT-1407). Enos (2014), excluded as proximity without interaction, found
prejudice increased.

## Bearing on the record

- **QUESTION-262.** The question says "contact reduces prejudice and often
  generalizes (LIT-1413)". On the randomized evidence with delayed
  outcomes the first half is qualified: positive in direction, 0.25 for
  ethnic and related targets, near zero in the pre-registered field
  trials. The second half is untested here: the review's outcomes mostly
  concern the group met, and its pooling does not separate generalization
  to the group or to other groups. Nor does any included study isolate
  taking part from receiving information, the question's first contrast.
- **CLAIM-430.** Its defeater, information of equal favourable content
  changing attitudes as much as taking part, has no test in this
  literature. Contact is compared with no contact.
- **Pettigrew 1998 (LIT-1408).** The review does not cite the 1998
  review and does not use the word "deprovincialization", so it does not
  bear on LIT-1408's flag.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Small numbers.** Twenty-seven arms, eleven on racial or ethnic
  prejudice, three pre-registered; every subgroup estimate rests on a
  handful of studies, and the 0.016 has no interval given.
- **The selection rules are the authors'.** Taking the specification with
  the smallest apparent standard error and the highest dose favours
  larger, more significant estimates; the direction of that bias runs
  against the paper's sceptical findings, not with them.
- **Within the interventions, little is known.** Most reports describe the
  contact too thinly to say which of Allport's conditions held.
- **Errors and slips.** None of substance found. "Hedge's G correction"
  is Hedges' g. Table 1's cell layout did not survive text extraction;
  its margins (3, 4, 13, 1, 6 participants; 11, 2, 3, 3, 1, 4, 2, 1
  targets) sum to 27 and agree with the prose. The text's "four of the
  five largest studies come in below this average" is not checkable
  without the figure.

## Open questions

- Does randomized contact reduce racial or ethnic prejudice in adults,
  measured weeks later?
- Do Allport's conditions moderate the effect when they are manipulated
  rather than coded after the fact?
- Is the precision gradient a file drawer, or the difference between
  small intensive interventions and large naturalistic ones?
