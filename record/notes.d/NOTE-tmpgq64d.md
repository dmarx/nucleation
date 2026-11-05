---
status: Read
paper: 'LIT-tmp0gnxg'
title: 'Knack — Aid dependence and the quality of governance'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read in full on 2026-11-05 in the working-paper version, World Bank
    Policy Research Working Paper 2396 (July 2000, 37 printed pages), from
    the World Bank's own scan stamped "Public Disclosure Authorized"
    (https://documents.worldbank.org/curated/en/200401468741328803/pdf/multi-page.pdf),
    44 PDF pages, text extracted by pdftotext -layout. The OCR runs words
    together and misreads some characters; quotes below are re-spaced and
    otherwise as printed. Read: the summary findings, the whole body (pp.
    1–24), the Appendix, Tables 1–5 and the figure captions. Skimmed: the
    reference list. Not read: the 2001 Southern Economic Journal version,
    whose estimates may differ. Page numbers below are the working paper's
    printed pages.
date: '2026-11-05'
summary: >-
  A cross-section of 80 aid recipients: the change in the ICRG governance
  index (corruption, bureaucratic quality, rule of law) from 1982 or 1984 to
  1995, regressed on mean aid over 1982–95. More aid goes with less
  improvement; the coefficient roughly doubles under 2SLS with need and
  donor-interest instruments and survives eight changes of sample, Africa
  only among them. Technical assistance carries coefficients several times
  larger; more variable aid harms less; initial governance does not
  moderate it. No first stage, no tax variable, no withdrawal.
---
<!-- inactive-ok-file: LIT-tmpw4aef THEORY-tmpymvl9 THEORY-1460 THEORY-1459 THEORY-1483 THEORY-1463 CLAIM-600 CLAIM-601 CLAIM-602 CLAIM-603 CLAIM-604 CLAIM-597 CLAIM-558 LIT-2151 — Unavailable, Proposed or new; cited from the reading of Knack (2000) as open -->

# NOTE-tmpgq64d: Knack — Aid dependence and the quality of governance

## Contribution

An early quantitative test, with instruments, of the thesis from
Bräutigam, Moore and Bauer that aid dependence erodes the institutions of
the state it supports. It replaces the single-year correlation of −.12 for
31 African countries (Bräutigam and Botchwey, cited in n. 4) with a
regression of the change in governance over thirteen years on mean aid,
and it adds moderators: the kind of aid, its variability, the initial
level of governance and ethnic composition. It turns the institutional gap
that conditions aid effectiveness in Burnside and Dollar into an outcome:
the gap "itself increases with aid levels" (summary findings).

## Key insight

Aid is not only conditioned on institutions; it shapes them. Where the
state is supplied from outside, the governance it would need for its own
growth improves less than it otherwise would, most of all when donors do
the work themselves (technical assistance) and when the supply is steady
enough to be counted on.

## Assumptions

- **ICRG is cardinal.** The 0–18 index (corruption, bureaucratic quality,
  rule of law) is treated as an interval measure; ordered logit is offered
  for the ordinal reading (p. 13).
- **Change scores remove fixed effects.** Time-invariant determinants such
  as religion, legal origin and colonial history drop out of a thirteen-year
  change; added cultural variables were not significant (n. 10).
- **Governance had not adjusted to aid by 1982**, because aid "is
  relatively non-persistent, with some recipients eventually becoming
  donors" (p. 12). Asserted, not shown.
- **Exclusion.** Infant mortality, initial income, population and the
  regional dummies affect the change in governance only through aid, with
  initial ICRG and income growth controlled. Argued only through the
  overidentification tests.

## Key results

- **Design (p. 10).** "the dependent variable analyzed is the end of period
  (1995) ICRG value minus the initial (1982 for most countries, and 1984 for
  most others) value." Aid is the country mean over 1982–95, as ODA/GNP
  (80 countries) or ODA/government spending (68).
- **Sample (Table 1).** ICRG change mean +2.47 (s.d. 3.38, range −6 to
  +10); aid/GNP mean 8.7 percent, maximum 69.1; aid/government spending
  mean 26.3 percent. Governance improved on average: aid goes with less
  improvement, not necessarily with decline.
- **OLS (p. 12; Table 2).** Aid/GNP −0.067 (s.e. 0.021); aid/government
  spending −0.027 (0.010). "a 15 percentage point rise in aid's share of GNP
  reduces the ICRG index by 1 point"; a one-s.d. change in aid "is
  associated with a .25 standard deviation change in the dependent
  variable". Dropping aid lowers R² from .55 to .45. Initial ICRG −0.77:
  "A very strong regression-to-the-mean effect".
- **Other estimators (p. 13).** Aid/GNP −.058 (.021) robust, −.049 (.022)
  median, −.052 (.018) ordered logit.
- **2SLS (pp. 13–14; Table 2).** Instruments: infant mortality 1980 and
  initial GDP per capita (need), initial population, Franc-zone and
  Central-America dummies (donor interest); "infant mortality is easily the
  most important predictor of aid". Overidentification p = .52 and .81.
  Aid/GNP −0.154 (0.037), aid/government −0.054 (0.014): "The estimated
  impact of aid roughly doubles", which Knack reads as donors directing aid
  "towards countries with improving rather than deteriorating
  institutional quality". **No first-stage statistics are reported.**
- **Size (p. 14).** A 20-point rise in aid/GNP "is estimated to reduce the
  ICRG index by about 3 points", which a Barro-type regression links to a
  one-point "drop in the average annual rate of per capita income growth".
- **Components (p. 15; Table 3).** Under OLS aid is significant for
  bureaucratic quality and the rule of law "but not to corruption"; under
  2SLS all three are "significantly and inversely related to aid levels".
- **Samples (pp. 15–17; Table 4).** The 2SLS aid/GNP coefficient runs from
  −0.126 to −0.190 across the extended, large-country, below-$4000,
  below-$2000, high-aid, non-socialist and Africa-only samples.
- **Africa only (Table 4, row 8).** Aid/GNP −0.074 (0.030) OLS, −0.126
  (0.057) 2SLS, 31 countries; aid/government −0.017 (0.016) OLS, −0.035
  (0.022) 2SLS, 24 countries, not significant. The text says only that
  "aid/GNP remains statistically significant" (p. 17).
- **Technical assistance (p. 17; Table 4, row 9).** OLS −0.346 (0.089),
  2SLS −0.699 (0.159). "Coefficients for technical assistance are several
  times greater than those for aid overall", read as consistent with the
  undermining of local expertise and administrative capacity. Entered
  together with the rest of aid, which it correlates with at .87, "only the
  former is significant" (n. 18).
- **Variability (pp. 18–19; Table 5, eqs. 1–2).** Aid variability "tempers
  rather than reinforces" the effect of aid levels: the coefficient of
  variation enters at +2.569 (0.593) and its interaction with aid at +0.145
  (0.070), and "the negative effects of aid levels disappear when the CV is
  about .78", higher than all but 15 of 80 values. "Variability in aid
  matters, but trends--i.e., "predictable variability"--do not."
- **Initial conditions (pp. 19–20; Table 5, eqs. 3–4).** Testing Bräutigam
  and Botchwey's view that aid harms only where governance starts weak:
  "Results provide no support for the hypothesis that initial conditions
  matter"; interactions −0.002 (0.008) and 0.003 (0.003).
- **Ethnic homogeneity (pp. 20–21; Table 5, eqs. 5–6).** "the corrosive
  impact of aid dependence on the quality of governance worsens with greater
  ethnic homogeneity", contrary to Svensson; the ELF interactions are
  "positive but insignificant" (n. 23).
- **Resources (p. 22).** Mineral and fuel exports are associated "with
  declining quality of governance, but the relationship is not
  statistically significant" (not tabulated).
- **Mechanisms, argued in section 2 (pp. 2–7) and not tested.** Aid lowers
  "the cost of doing nothing" (after Rodrik); it weakens accountability "by
  reducing government's dependence on its citizenry for tax revenues";
  donors draw talent away and make "end runs around local institutions"
  (quoting Dollar and Pritchett); it feeds rents and patronage.
- **Withdrawal, cited only.** Meyer (1992) on the Dominican Republic: "When
  external funding ended, the new institutions broke down" (p. 5); and the
  end of U.S. aid "is often credited for the Korean and Taiwanese reforms of
  the 1960s" (p. 3).
- **Policy (pp. 22–23).** "Policy implications must be phrased very
  tentatively". More budget support or debt relief for reformers, since
  without donor-run projects, tied aid and technical assistance recipient
  governments "may face greater opportunities to build administrative
  capacity".

## Concepts

- **Aid dependence** measured against government budgets as well as GNP,
  a dependence "not of economies but of governments" (Moore, cited in n. 5).
- **"Zairean disease"** (p. 2): the aid analogue of Dutch disease.
- **Windfall revenue**, and **reverse causation through donor selection**.
- **Aid variability against predictable trend.**
- **Technical assistance as capacity substitution.**

## Connections

It is the empirical companion to Bräutigam's argument and the same
research programme as Bräutigam & Knack (2004), [LIT-tmpw4aef](../literature.d/LIT-tmpw4aef.md), unread, for
which it partly stands in. It restates that article's cross-country
governance result for sub-Saharan Africa in its own Africa-only subsample
(aid/GNP significant, aid/government spending not). It does not restate the
article's tax-revenue or tax-effort analysis, which it lacks, its own
sample or years, its wording, or the exit-strategy recommendations a
third-party summary attributes to it.

In the record: Moss, Pettersson and van de Walle ([LIT-2144](../literature.d/LIT-2144.md), [NOTE-1661](NOTE-1661.md))
cite it for the moral-hazard effect, and [THEORY-1460](../theory.d/THEORY-1460.md) carries that citation;
Moore ([LIT-2182](../literature.d/LIT-2182.md), [NOTE-1663](NOTE-1663.md)) cites it as showing only some association,
with reverse causation possible, and [THEORY-1459](../theory.d/THEORY-1459.md) asks for within-country
evidence. Azam, Devarajan and O'Connell ([LIT-2156](../literature.d/LIT-2156.md), [THEORY-1483](../theory.d/THEORY-1483.md)) model a
threshold in initial institutions that Knack's null initial-conditions
interaction does not bear out, though Knack measures governance rather
than tax capacity. Pritchett, Woolcock and Andrews ([LIT-2164](../literature.d/LIT-2164.md), [THEORY-1463](../theory.d/THEORY-1463.md))
describe the persistent low capability whose aid-related part this
measures. The record's withdrawal evidence, which Knack's design lacks, is
the FANTA exit-strategy study ([LIT-2151](../literature.d/LIT-2151.md), unread, with its Kenya and India
summaries [LIT-2154](../literature.d/LIT-2154.md) and [LIT-2148](../literature.d/LIT-2148.md)). Ahmed (2012), filed in this batch,
carries the same unearned-income logic to incumbent survival.

## Bearing on the record

- **[CLAIM-600](../claims.d/CLAIM-600.md) (the synthesis).** Qualifies it. The evidence is about
  support in progress, with no withdrawal episodes and no persistence after
  withdrawal, so it cannot test the withdrawal conditions. It supports the
  clause that support failing them leaves decay, for support that
  substitutes for the state's own work. The variability result complicates
  it: steady supply harms more than erratic supply of the same mean.
- **[CLAIM-604](../claims.d/CLAIM-604.md) (thresholds, collapse, hysteresis).** No threshold, collapse
  or hysteresis is tested; the model is a linear change regression. The
  null initial-conditions interaction is evidence against a governance
  threshold above which aid stops harming.
- **[CLAIM-602](../claims.d/CLAIM-602.md) (supply doing the work crowds out learned capacity).**
  Supports it in part: technical assistance, donors doing the work, carries
  coefficients several times aid overall, and only it survives when both
  are entered. The order of use is not observed, and the .87 correlation
  makes the separation weak.
- **[CLAIM-603](../claims.d/CLAIM-603.md) (one-way against reciprocal supply).** Supports it and gives
  a measurable handle: harm falls with aid's unpredictability and vanishes
  near a coefficient of variation of .78, while predictable trends do not
  matter, consistent with loss favoured where outside supply is reliable.
- **[CLAIM-597](../claims.d/CLAIM-597.md), [CLAIM-558](../claims.d/CLAIM-558.md), [CLAIM-601](../claims.d/CLAIM-601.md).** None tested. No supply is stopped;
  the talent-drain and bypassing mechanisms are argued, not measured.
- **[QUESTION-398](../questions.d/QUESTION-398.md) (independence from the founding intervention).** No
  withdrawal design. The cited anecdotes point both ways: institutions
  broke down at exit in the Dominican Republic; reform followed exit in
  Korea and Taiwan.
- **[THEORY-1460](../theory.d/THEORY-1460.md) (Moss et al.).** Supplies the identified governance half
  of its `promote_when`, but as cross-country 2SLS on a single change
  score, not within-country panel evidence; nothing on its grant/loan or
  tax-effort half.
- **[THEORY-1459](../theory.d/THEORY-1459.md) (Moore).** Does not meet its within-country `promote_when`.
  Moore's reverse-causation reservation is addressed only by instruments
  whose exclusion is untested; the rise under 2SLS suggests the OLS bias
  runs the other way.
- Filed: [THEORY-tmpymvl9](../theory.d/THEORY-tmpymvl9.md).
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **One observation per country**: N = 80, 31 in Africa.
- **Instruments of doubtful exclusion**: initial income and infant mortality
  may affect governance change directly (catch-up, state capacity). No first
  stage or F statistic is given.
- **ICRG is a commercial investor-risk rating**, possibly "inferred by ICRG
  in part from observations of economic performance" (p. 11).
- **No tax or revenue variable**, so the fiscal-contract mechanism is
  untested here.
- **The paper's own errors.** The 2SLS aid/GNP standard error is 0.037 in
  Table 2 but 0.045 in Table 4, row 1, for the same "Basic" specification.
  Section numbering skips from 4 to 6 (policy implications are "section
  6"). The findings are called "work in progress".
- **The Africa-only aid/government result is not significant**, and the
  text passes over it.
- **The 2001 journal version was not read.**
