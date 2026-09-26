---
number: 49
status: Read
formerly:
- NOTE-tmpdirbv
paper: LIT-087
title: 'Feinman et al. 2025, grand narratives of inequality'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full main text of the open-access version of record
    (Europe PMC XML of PMC12037030, rawC4/c37.txt): significance statement,
    abstract, introduction, "Approach and Methods", "Empirically Assessing
    Grand Narratives", "Governance Matters", "Conceptual Implications", and
    the back matter. I also read the full 8-page SI Appendix
    (rawC4/c37_supp/pnas.2400698121.sapp.pdf → c37_si.txt): Sections 1–4,
    the captions of Figs. S1–S6, Table S1 and the SI references. I viewed
    main Figs. 1–5 as images to read the r² and P values printed on them,
    most of which are not in the text, and SI pp. 5–6 (Figs. S3–S6). I did
    not view the Fig. S1 (collapse boxplots) and Fig. S2 (loess time series
    by macroregion) images, so the temporal claims are taken from the text
    only. The deposited tDAR csv was not examined.). Upgraded from `Skimmed`
    to `Read`: the claims table, assumptions and results are new, and the
    skim is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  Across a global archaeological house-size compilation (SiteGiniLevel:
  1,176 sites, 47,019 houses), site Gini coefficients rise only weakly
  with the number of political levels (r² = 0.16 all sites, 0.22 apex,
  0.27 H50) and with log polity population (r² = 0.11, 0.21, 0.08; values
  printed on Fig. 2, not in the text). The spread widens at three or more
  levels. A 0–3 expert-coded autocracy score does about as well (r² =
  0.10, 0.18, 0.32; Fig. S4), and its sum with levels ("Hierarchical
  Clout") reaches r² = 0.30 (apex), 0.42 (H50) and 0.50 (H100). All tests
  are bivariate OLS fits with no controls and no correction for many sites
  sharing polity-level values.
---

<!-- inactive-ok-file: LIT-047 — Proposed by its close reading; named in Connections -->

# NOTE-049: Feinman et al. 2025, grand narratives of inequality

## Contribution

- The largest global, temporally anchored comparison of premodern domestic wealth disparity. It uses site-level Gini coefficients of house floor area from the GINI project's SiteGiniLevel file (Kohler et al., companion paper, "this issue") to test four "grand narratives":
  - inequality scales with political hierarchy;
  - inequality scales with population (Malthusian or functionalist);
  - it falls only after collapse;
  - it rises linearly after domestication and urbanism.
- An expert-coded governance index (collective ↔ autocratic, 0–3) and a composite "Hierarchical Clout" (number of levels + inverse governance, 1–9), used to argue that institutions condition how much of the scale-enabled "potential" for inequality is realized.

## Key insight

Scale, whether in levels of hierarchy or in polity population, raises the ceiling on house-size inequality but does not set the level. The variance of Gini widens as scale grows while the mean rises only a little. The sites that reach the ceiling are overwhelmingly autocratic apices of polities with three or more levels.

## Assumptions

- **Wealth proxy.** Relative house size is a valid proxy for household material wealth across all regions and periods ("housing is a principal component of domestic material wealth", p. "Approach"). The Tenochtitlan case (Gini .13, .30 or .75 depending on sample adjustment; SI §4) shows how sensitive single values can be.
- **Comparability.** Gini coefficients are comparable across sites "that employ similar aggregation methods". Sites with few houses are treated only by restricting to the H50 and H100 subsets. No small-sample bias correction is mentioned.
- **Dating.** Each site-phase is dated by the midpoint of its temporal range.
- **Level of analysis.** Sites are the unit. Polity-level predictors (levels, population, governance) are assigned to every site in the polity, so many sites share identical predictor values, visible as vertical stripes in Figs. 1–2 and 4. Sites are treated as independent observations in OLS.
- **Scales.** The number of levels (ordinal, 1–6) and governance (0–3, summed binaries with occasional 0.5) are treated as interval-scale in linear fits. Collective/autocratic is dichotomized at ≤1 vs ≥1.5.

## Key results

| predictor (Fig.) | all sites | apex | H50 | H100 (Fig. S5) |
|---|---|---|---|---|
| number of levels (1) | r² 0.158 (n 1,164) | 0.218 (711) | 0.269 (170) | 0.326 (92) |
| log polity population (2) | 0.107 (590) | 0.213 (243) | 0.085 (110) | 0.105 (66) |
| inverse governance (S4) | 0.096 (1,071) | 0.184 (643) | 0.316 (170) | 0.438 (94) |
| hierarchical clout (4) | 0.164 (1,059) | 0.295 (643) | 0.425 (164) | 0.498 (92) |

All of these have P < 0.01. The values come from the figure panels; the text reports only the level and clout values.

- **Governance, apex sites (Fig. 3).** Collective sites (n = 563) have a median Gini of about 0.23; autocratic sites (n = 80) about 0.41, with a much wider spread (read from the box plot). No test statistic is given. The pattern holds excluding level-1 sites (Fig. S3; n = 175 vs 76).
- **By macroregion, H50 (Fig. 5B).** The within-region clout slope is steep in Asia (r² 0.57), Europe (0.69) and South America (0.69), weak in Mesoamerica (0.06, P = .07), and flat in North America (0.003, P = .83).
- **The eight highest apex sites.** Every apex site in a polity of three or more levels with Gini > 0.75 is in Southwest Asia (Assur, Babylon, Zincirli, Nuzi, Tell el-Amarna), South America (Chan Chan, Galindo) or Europe (Knossos).
- **Collapse.** Inequality fell after Roman England (ca. 410 CE) but rose after Teotihuacan (ca. 600 CE) (Fig. S1). The authors say their sample "is not sufficiently robust to test this expectation fully".
- **Time.** None of the five macroregions shows a consistent subregional trend. The sites with the greatest inequality tend to come later. The largest upticks postdate the first cities: Southwest Asia after ca. 3500 BCE, Mesoamerica after ca. 500 BCE (Fig. S2, loess, span 0.75).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Political hierarchy and polity population are weak predictors of site house-size Gini; greater scale widens the range rather than fixing the level | moderate–strong | bivariate OLS across three subsets (Figs. 1–2), with consistent heteroscedastic fans visible in the scatters; no model of the variance itself |
| C2 | Inequality did not rise immediately or uniformly with domestication or first urbanism | moderate | descriptive loess per macroregion (Fig. S2); unbalanced, patchy temporal sampling (acknowledged in SI §1) |
| C3 | Collapse does not reliably reduce inequality | weak | two cases (Fig. S1), and the authors say the test is not robust |
| C4 | Governance (collective–autocratic) explains about as much variance as hierarchy | moderate | Fig. S4 vs Fig. 1 r² values; the governance index includes an architecture dimension coded alongside the house data |
| C5 | Concentrated power at scale (Hierarchical Clout) is what realizes high inequality | weak–moderate | the r² rise from 0.22–0.27 to 0.30–0.42 comes from summing two predictors; no two-predictor or interaction model, no controls for region or period, no handling of shared polity values |
| C6 | Collective polities recruit labour and so grow in population without concentrating wealth; autocratic ones do not | weak | a contrast of r² 0.14 vs 0.10 (P = .07) on apex sites (Fig. 5C), misdescribed in the text; clearer in H50 (Fig. S6) |
| C7 | External resources (herd animals, metals, trade routes) facilitated wealth concentration under permissive governance | weak | co-occurrence at the macroregion level (Fig. 5B), explicitly not causal |
| C8 | Grand narratives of universality, linearity and progress should be replaced by middle-range, context-specific theory | informal argument | follows from C1–C3 as a research-programme recommendation |

## Concepts

- **SiteGiniLevel** — the GINI project's site-level file: one Gini of house sizes per site and phase.
- **apex site** — a settlement at the top level of its polity. **H50 / H100** — sites with at least 50 / at least 100 measured houses.
- **NofL** — the number of levels of political hierarchy of the polity containing the site (1–6).
- **Gov / Gov_I** — the sum of three binary codes (political economy, leadership, architecture; 1 = collective), simplified from Blanton & Fargher. Gov_I is its inverse, so 3 = most autocratic.
- **Hierarchical Clout** — NofL + Gov_I (1–9).
- **Polity-Scale Effect** — small sites in hierarchical polities under-represent the polity's inequality (from ref. 48).
- **external resources** — wealth sources that can be accumulated and monopolized without heavy labour inputs (herds, metals, trade routes).

## Connections

- The paper is part of the PNAS special feature "The Global Dynamics of Economic Inequality over the Long Term" (eds. Kohler & Bogaard). It depends on the companion data paper (Kohler et al., "World prehistory of wealth inequality") for the SiteGiniLevel file.
- It sits against Scheidel's "Great Leveler" (collapse-only reversals), neo-Malthusian accounts, and stage-evolutionist accounts in which each step up in scale brings more stratification.
- It builds on Blanton & Fargher's collective-action theory of premodern states, and on Kohler et al. 2017 (Nature: greater post-Neolithic wealth disparities in Eurasia than in the Americas), whose Eurasia/Americas contrast reappears here as the herd-animal and metal regions.
- The land-limited vs labour-limited axis is left to another paper in the feature.
- In this record it pairs with [LIT-047](../literature.d/LIT-047.md) (Curry et al.) and [LIT-035](../literature.d/LIT-035.md) (Peters & Adamou) only loosely, as part of a governance-and-cooperation thread. No direct lineage.

## Bearing on the record

There is nothing for ML practice. Methodologically it is a useful cautionary example for any record entry: "r² rises when two predictors are summed into a composite" is not evidence for an interaction, and polity-level predictors copied to many sites inflate apparent significance. It supports no specific THEORY document and contradicts none by name.

## Limitations

- **Outcome proxy.** House size is one metric. The authors state this ("relative house sizes are just one metric", p. "Conceptual Implications"). SI §1 says the sample is "neither spatially nor temporally balanced or complete".
- **Statistics.** Only bivariate OLS with r² and P are reported. There is:
  - no multilevel model (sites nested in polities and regions);
  - no control for macroregion, period or house-sample size;
  - no test for the Fig. 3 group difference;
  - no two-predictor model separating levels from governance.
  With predictors shared across sites in the same polity, the P < 0.01 values are almost certainly overstated. The effective n is closer to the number of polities.
- **Circularity risk.** Governance is expert-coded, partly from architecture, contemporaneously with house data entry, which could lead to autocracy being read from large elite residences.
- **Single-site sensitivity.** Tenochtitlan's Gini ranges from .13 to .75 by method (SI §4). The headline "2 of 29" exception count turns on it.
- **Missing data.** The population analyses use only 590 of 1,176 sites (243 of 711 apex sites). Missingness is not characterized.
- **Scope of the negative conclusion.** The body shows that scale is not sufficient for high inequality. "Now-refuted presumptions of universality, linearity, and progress" (p. "Conceptual Implications") is stronger than bivariate correlations can establish.

## Open questions

- Does the governance effect survive a multilevel model with polity random effects, a region-by-period control, and a governance index recoded without the architecture dimension?
- Is the widening variance with scale robust to small-sample Gini bias? A test would be to regress the residual spread on house-sample size within H50.
- Do the collective/autocratic differences hold for other wealth proxies (grave goods, storage) at the same sites? The feature's companion papers may address this.

## Corrections to the seeded skim

- r² values. The dossier gives the hierarchy r² as "≈ 0.22–0.27" (apex and H50) and omits the all-sites value, r² = 0.16 (P < 0.01; Fig. 1A). For population, the dossier says only that it is "a weak predictor". The figures show r² = 0.107 (all), 0.213 (apex) and 0.085 (H50) (Fig. 2). On apex sites population predicts about as well as hierarchy, which the text does not say.
- Apex sample size. The dossier's "apex sites (717 sites)" follows the text, but Fig. 1B's caption and Table S1 give 711. The text and the SI disagree.
- "Polity-Scale Effect". It is not a correction the authors apply, as the dossier implies ("Check … the 'Polity-Scale Effect' correction"). It is their post-hoc explanation of why the apex subset shows a stronger relationship: small sites in hierarchical polities do not show the polity's full range of inequality (p. "Empirically Assessing").
- "Only 2 of 29 … show high inequality". The dossier's wording is inaccurate. The paper's claim is that only 2 of 29 collectively governed apex sites in polities of three or more levels lie above the regression line for autocratic apex sites (Fig. 5A). One of those two, Tenochtitlan, has Gini .75 here, and SI Section 4 says the lead author thinks it is overestimated because palaces are overrepresented. An earlier "social tables" estimate gave .30, which would put it below the line.
- Population and governance. The text says Fig. 5C shows "the significant relationship (r² = 0.14) … between polity population and governance for collectively organized polities" and "basically no relationship" for autocratic ones. The figure actually plots Gini against log population separately for each governance class. There, collective apex sites have r² = 0.139 (P < 0.01) and autocratic ones r² = 0.100 (P = .07, n = 34). That is a similar effect size with less power, not "no relationship". The H50 version (Fig. S6) shows a clearer contrast: 0.162 (P < 0.01) against 0.020 (P = .32).
- Governance coding, which the dossier flagged to check. It confirms the concern and adds one:
  - The coding was done by the same regional experts "at the same time that the individual houses and other variables were entered".
  - One of its three binary dimensions is "architecture" (p. "Governance Matters"; SI Section 3).
  - Gini is computed from house sizes, so autocracy coding may partly read the outcome.
- Authors. There are nine: Feinman, Cervantes Quequezana, Green, Lawrence, Munson, Ortman, Petrie, Thompson, Nicholas (SI title page).
