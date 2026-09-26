---
number: 167
status: Read
formerly:
- NOTE-tmpsvqk5
paper: LIT-155
title: 'Studying philosophy makes people better thinkers'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of the published open-access version (JAPA
    11(4), Dec 2025, pp. 640–658, 19 pp.), taken from Cambridge Core: the
    HTML full text for numbers and prose, and the PDF for layout, Figures
    1–3, Table 1, the Appendix (Tables A1–A3, Figure A1, propensity-score
    analysis) and footnotes 1–2. I read all of it: abstract, §§1–6, the
    Appendix and the references. Not read: the OSF analysis code
    (osf.io/6yz8m).). Upgraded from `Skimmed` to `Read`: the claims table,
    assumptions and results are new, and the skim is corrected where the
    full text disagreed.
date: '2026-09-26'
summary: >-
  In HERI/CIRP freshman–senior survey data (N = 649,511 students at 804 US
  institutions, 4,843 philosophy majors), one SD more SAT Verbal raises
  the odds of majoring in philosophy by 57% (OR 1.57), and freshman Habits
  of Mind by 34%. After adjusting for SAT or freshman scores, philosophy
  majors still score higher than non-majors on GRE Verbal (+33 points, SMD
  0.48), LSAT (+2, SMD 0.35), Habits of Mind (SMD .24) and Pluralistic
  Orientation (SMD .21), with no difference on GRE Quantitative. On point
  estimates they rank first of 57 or 62 majors on GRE Verbal, LSAT and
  Habits of Mind.
---

# NOTE-167: Studying philosophy makes people better thinkers

## Contribution

The paper tests premise B of a traditional argument for philosophy's value (§1): "Philosophical study cultivates valuable intellectual abilities and dispositions". It is the first large study to adjust for baseline differences when doing so. The authors' own earlier review (Prinzing & Vazquez 2024) found the evidence inconclusive. Here, using longitudinal HERI/CIRP data on 649,511 students, they show two things together. There is self-selection into philosophy, on verbal ability and on self-reported intellectual dispositions. And philosophy majors keep an advantage after adjustment on GRE Verbal, LSAT, Habits of Mind and Pluralistic Orientation, but not on GRE Quantitative.

## Key insight

The old fact that philosophy majors top the GRE and LSAT is uninformative about causation, because self-selection predicts it equally well (§2). The authors' own earlier finding, that first-week philosophy students already outscore the population on the Cognitive Reflection Test, shows selection is real. The remedy they adopt is to adjust for the freshman-year value of the outcome, or a proxy for it: SAT for the tests, the same scale for the self-reports. They argue this "remove[s] the influence of pre-college confounds" (§5.2) without anyone having to name them. On this design the verbal-reasoning advantage survives adjustment at a medium effect size, while the quantitative one does not exist.

## Assumptions

Premises and design assumptions (§§2, 4, 6; Appendix):

- **Premise A** ("If an activity cultivates valuable intellectual abilities and dispositions, then that activity is valuable") is taken as "extremely plausible" and not defended (§1).
- **Baseline adjustment removes confounding.** Confounders are assumed to have acted before college and to show up in the freshman scores (§2). The assumption needed for identification, that no unmeasured factor affects both the choice of major and the *change* in scores during college, is not stated as such.
- **SAT is a valid baseline for GRE Verbal and LSAT.** The authors themselves flag that the SAT has no logical-reasoning section, so the LSAT adjustment may be incomplete (§6).
- **Self-reported test scores are accurate.** SAT at entry and GRE/LSAT at graduation are student-reported survey answers (§4). This is not discussed as a limitation.
- **The HERI self-report scales measure intellectual dispositions.** The authors read Habits of Mind as curiosity, rigour, some humility and open-mindedness, and Pluralistic Orientation as open-mindedness. They base this on the item wording (Table 1), not on a validation study.
- **Selection into test-taking is captured by an SAT × major interaction** (§5.3).
- **Setting.** US undergraduates in HERI-participating institutions. Tests: 1994–2004 graduates (n = 392,858). Self-reports: 2010–2019 graduates (n = 122,352). The two sets of cohorts do not overlap.

## Key results

All from mixed-effects models with institution random intercepts, lme4/lmerTest, emmeans, and multiple imputation (mice) (§5).

- **Selection (§5.1, Table A1)**: logistic model for majoring in philosophy. SAT Verbal b = 0.45, OR 1.57, p < .001. SAT Math b = −0.01, OR 0.99, p = .872. Freshman Habits of Mind OR 1.34, p < .001. Freshman Pluralistic Orientation OR 1.13, p = .008. Predictors are z-scored.
- **Adjusted differences, philosophy vs pooled non-philosophy (§5.2, Table A2, Fig. 1)**:
  - GRE Verbal b = 33.25 [23.86, 42.64]. Adjusted means 573 vs 540. SMD 0.48 ("medium").
  - GRE Quantitative b = −3.91 [−18.51, 10.7], p = .619.
  - LSAT b = 2.12 [1.46, 2.78]. Adjusted means 157 vs 155. SMD 0.35.
  - Senior Habits of Mind b = 0.21 [0.16, 0.25]. SMD .24.
  - Senior Pluralistic Orientation b = 0.19 [0.15, 0.24]. SMD .21.
- **Rankings (§5.2, Figs 2–3)**: majors with fewer than 200 students are excluded, leaving 57 majors for the tests and 62 for the self-reports, out of 90. On point estimates philosophy is 1st on GRE Verbal, LSAT and Habits of Mind, 6th on Pluralistic Orientation and 30th on GRE Quantitative.
- **Second selection effect (§5.3, Table A1)**:
  - Taking the GRE: SAT OR 1.31, philosophy OR 1.29 (p = .039), SAT × philosophy OR 1.03 (p = .669).
  - Taking the LSAT: SAT OR 1.26, philosophy OR 3.53, SAT × philosophy OR 0.92 (p = .101).
  - The authors read the absent interaction as no evidence that only the best philosophy students take the tests.
- **IPTW robustness (Appendix, Table A3)**: the propensity model uses SAT V and M, academic self-concept, sex, race, religion, household income, political ideology, parental education and institution. Estimates: GRE Verbal 30.61 [22.15, 39.06]; GRE Quantitative −9.99 (p = .228); LSAT 2.30 [1.55, 3.04]; Habits of Mind 0.29 SD; Pluralistic Orientation 0.28 SD. Figure A1 shows "a substantial region of common support".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Students with higher SAT Verbal, and higher freshman Habits of Mind and Pluralistic Orientation, are more likely to major in philosophy. SAT Math does not predict it. | strong | §5.1, Table A1. Large N, but the SAT is self-reported. |
| C2 | After adjusting for SAT, philosophy majors score higher than non-philosophy majors on GRE Verbal (SMD 0.48) and LSAT (SMD 0.35), but not on GRE Quantitative. | strong (as an adjusted association) | §5.2, Table A2, Fig. 1. Replicated by IPTW in Table A3. |
| C3 | After adjusting for freshman scores, philosophy majors report more of the Habits of Mind (SMD .24) and Pluralistic Orientation (SMD .21) dispositions. | moderate | §5.2. Self-report scales, with items that partly describe classroom behaviour (Table 1). |
| C4 | Philosophy majors "outperform all other majors" on verbal and logical reasoning tests and on Habits of Mind (abstract, §6). | weak | Ranking of point estimates in Figs 2–3. Confidence intervals overlap with several majors on LSAT and Habits of Mind, and no pairwise test is reported. |
| C5 | Only the best philosophy students taking the GRE/LSAT does not explain the test results. | moderate | §5.3: no SAT × major interaction on test-taking. This addresses selection on SAT only, not selection on unmeasured ambition or aptitude. |
| C6 | These results are causal: studying philosophy *makes* people better thinkers, and this is "the strongest evidence to date", "short of a randomized experiment" (title, abstract, §6). | moderate for verbal-test gains, weak beyond that | Observational covariate adjustment plus IPTW. Identification rests on no unmeasured confounding of *change*, which is argued informally (§2) and not tested (no sensitivity analysis, no negative-control outcome). |
| C7 | The argument from premises A and B to "philosophical study is valuable" is sound (§1). | weak | Premise A is asserted as "extremely plausible", not defended. Premise B is supported only for "certain popular versions" (§1). |
| C8 | The measures do not capture intellectual virtue in the full philosophical sense (right reasons, objects, occasions). | assertion (a concession) | §6, citing King 2021. |

## Method

Longitudinal observational design (§§4–5).

1. HERI/CIRP Freshman Survey paired with the College Senior Survey, 1990–2019. The public archive covers 1994–2008 graduates; the later data were bought.
2. Selection is estimated with a mixed-effects logistic regression of philosophy major on SAT V, SAT M and the freshman scales.
3. Outcomes are compared with mixed-effects linear models: senior outcome ~ philosophy major + baseline, with institution random intercepts. SAT V and SAT M are the baselines for GRE/LSAT, and the freshman scale is the baseline for the self-reports. Estimated marginal means come from emmeans, and missing data are handled by multiple imputation.
4. Per-major rankings exclude majors with fewer than 200 students.
5. Selection into test-taking is tested with an SAT × philosophy interaction.
6. IPTW robustness check. As written, the weights are "the propensity score for non-philosophy majors and the inverse of the propensity score for philosophy majors" (Appendix). This is not the standard ATE weighting (1/(1−p) for controls) or ATT weighting (p/(1−p) for controls). Whether the prose misdescribes the code is unverified, since the OSF code was not read. As listed, the propensity model's covariates do not include the freshman Habits of Mind or Pluralistic Orientation scores.

## Concepts

- **Premise B**: that philosophical study cultivates valuable intellectual abilities and dispositions. It is treated as an empirical, not a priori, claim (§1).
- **Covariate / baseline adjustment**: controlling statistically for the freshman-year value of the outcome, or a proxy, so as to absorb pre-college confounds "without knowing exactly what they are" (§2).
- **Habits of Mind**: a HERI IRT factor score over 10 items on how often, in the past year, the student did things such as "Support your opinions with a logical argument", "Ask questions in class" or "Evaluate the quality or reliability of information you received" (Table 1). HERI describes it as behaviours tied to academic success and lifelong learning.
- **Pluralistic Orientation**: a HERI factor score over 5 self-ratings, such as "Openness to having my own views challenged". The authors read it as open-mindedness.
- **Second selection effect**: differential selection, by major, into taking the GRE or LSAT (§5.3).
- **Good thinking**: operationalised in two complementary ways (§3). Abilities are measured by standardized tests, called "objective" but a "thin" conception. Dispositions, a proxy for intellectual virtues, are measured by self-reports.

## Connections

- The paper builds on the authors' own review (Prinzing & Vazquez 2024, JAPA), which found no strong evidence either way. It also builds on work showing philosophers are more reflective on the Cognitive Reflection Test (Byrd; Livengood et al. 2010; Frederick 2005). Its one causal-inference predecessor is Farieta & Delprato (2024), a propensity-score-matching study of Colombian trainee teachers (footnote 1).
- In virtue epistemology it leans on King (2021), *The Excellent Mind*. In the §6 civic argument it points to political-philosophy claims (Brighouse, Gutmann, Nussbaum, Lynch) that reflective dispositions sustain democracy.
- **Account of mind held.** The paper holds no theory of representation or mental content. It presupposes a faculty-and-disposition picture of the thinker. Good thinking is a set of reasoning *abilities* (verbal, logical and quantitative, taken as measurable by tests) plus intellectual *dispositions* or virtues (curiosity, rigour, humility, open-mindedness), and education can train both. This is a virtue-epistemological and psychometric view, not a cognitive-scientific model of how reasoning works.
- **Cognition tag.** Justified as a secondary tag. The outcomes are reasoning abilities and cognitive reflection, which fall under the blurb's "reasoning and cognitive strategies", and someone browsing cognition could reasonably expect a study of whether training changes reasoning. The paper says nothing about the mind as information processing, though, so it should not lead.
- No work in the nucleation record is a direct neighbour. A grep for Prinzing, the Cognitive Reflection Test, intellectual virtue and propensity scores found only this note.

## Bearing on the record

- The paper carries nothing for ML practice. Its one transferable point is methodological and generic: baseline adjustment is a cheap guard against selection effects in observational comparisons, and it leaves the assumption of no confounding of *change* untested. The anthology has no document this bears on.
- For nucleation, it is the record's best-supported empirical data point on the value of philosophy and on intellectual virtue. It should be tagged `epistemology` alongside `social-science`.

## Limitations

- **Identification.** Adjusting for a baseline removes confounders only to the extent that they act through baseline *level*. Students who choose philosophy may also differ in their *rate* of verbal growth, in motivation, in reading volume, or in plans for law school. Plans for law school are especially relevant: philosophy majors are 3.5× as likely to sit the LSAT and may prepare harder. Such differences would bias the estimates upward. No sensitivity analysis, such as an E-value or a Rosenbaum bound, is reported.
- **Proxy baseline for the tests.** The SAT is not the GRE or the LSAT, and the authors concede that it lacks a logic section (§6). With an imperfect proxy baseline, residual confounding is expected (Lord's-paradox territory), not ruled out.
- **Self-reported scores throughout.** SAT, GRE and LSAT scores are all student-reported (§4). The §3 case for tests as "immune to reporting biases" does not apply to self-reported test results, and the paper does not address this.
- **Construct overlap in Habits of Mind.** Several items ("Ask questions in class", "Support your opinions with a logical argument", "Seek solutions to problems and explain them to others") describe what philosophy seminars require. A gain may partly reflect the curriculum's classroom demands rather than a general disposition.
- **The headline "all other majors" is a point-estimate ranking**, with overlapping intervals on LSAT and Habits of Mind. On GRE Verbal the separation from English is narrow.
- **Test-taking selection** is examined only on SAT. Selection on unobservables into taking the GRE or LSAT is not addressed. GRE/LSAT scores were also asked for at the end of senior year, so later test-takers are missing.
- **Two cohort windows.** The test results come from 1994–2004 graduates and the self-report results from 2010–2019 graduates. No single cohort shows both kinds of gain.
- **Scope of "better thinkers".** The authors concede that the measures do not capture intellectual virtue as philosophers conceive it (§6), and that other claimed goods (formation, autonomy, "powerful knowledge") are untested.
- **The IPTW weighting is described in a non-standard way** (see Method), and the OSF code was not checked here.

## Open questions

- Would a within-student design with the *same* test at entry and exit settle the causal claim for logical reasoning? The authors propose an LSAT-like test or the California Critical Thinking Skills Test given at the start and end of the degree (§6).
- Is there a dose–response relation, with majors gaining more than minors? And do subfields differ: ethics against metaphysics, analytic against continental departments (§6)?
- How large is the effect under a formal sensitivity analysis for unmeasured confounding of growth?
- Do the Habits of Mind and Pluralistic Orientation gains predict outcomes later in life, as the authors suggest could be tested (§6)?
- Does the GRE Verbal advantage survive a comparison with the nearest-ranked majors (English, Anthropology) tested pairwise?

## Corrections to the seeded skim

- The NOTE's open question "whether the gap on GRE Quantitative is also reported" is answered: it is. There is no significant difference (b = −3.91, 95% CI [−18.51, 10.7], p = .619; IPTW −9.99, p = .228), and philosophy ranks 30th of 57 majors (§5.2, Table A2, Table A3).
- The skim and the summary say philosophy majors "outperform all other majors" on GRE Verbal, LSAT and Habits of Mind. That is the abstract's wording, and in the body it is a ranking of point estimates (§5.2, Figs 2–3), not a pairwise test. In Figure 2 the LSAT confidence interval for philosophy overlaps those of Pharmacy, Economics and Aerospace Engineering. In Figure 3 the Habits of Mind interval overlaps General Studies and Earth & Planetary Sciences. No test against the second-ranked major is reported. Only the comparison with the pooled non-philosophy group is tested.
- The skim leaves out Pluralistic Orientation as an outcome. Philosophy majors also score significantly higher on it (b = 0.19 [0.15, 0.24]), but rank 6th of 62, behind Social Work, Anthropology, Ethnic/Cultural Studies, Political Science and International Business.
- The skim leaves out the Appendix's robustness check: IPTW propensity-score models give GRE Verbal +30.61, LSAT +2.30, Habits of Mind +0.29 SD and Pluralistic Orientation +0.28 SD. The §2 footnote says the propensity results are "identical" to the main ones. They agree in sign and significance, but the self-report effects come out somewhat larger (0.29 against the main text's 0.21).
- The skim's §5.1 figures are right (Table A1: SAT Verbal OR 1.57; Habits of Mind OR 1.34; Pluralistic Orientation OR 1.13, p = .008; SAT Math OR 0.99, p = .872). The skim does not note that the SAT and the GRE/LSAT scores are all self-reported on the HERI surveys (§4). §3 praises standardized tests as "immune to reporting biases" and never flags this.
- The NOTE's premise that the vocabulary "has no metaphilosophy or epistemology word" is out of date: `epistemology` is now a held topic, and its blurb ("the value of knowledge", evidence) fits the paper's intellectual-virtue and value-of-philosophy payload. The tag should be added.
- primary topic: social-science. This is an empirical, psychometric study in education research, which is squarely the social-science blurb. `cognition` is justified as a secondary tag. Add `epistemology`.
