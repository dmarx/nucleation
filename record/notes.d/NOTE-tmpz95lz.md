---
status: Read
paper: 'LIT-1416'
title: 'Kleinman, Liu and Redding — International friends and enemies'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from NBER's own copy of the working paper,
    https://www.nber.org/system/files/working_papers/w27587/w27587.pdf
    (NBER Working Paper 27587, "July 2020, Revised March 2023", 41
    pages), text extracted with pdftotext. This is the revision that
    thanks "the editor, two anonymous referees", not the AEJ:
    Macroeconomics article of 2024, which was not seen; the two may
    differ. Read: the abstract, §§1–6, Tables 1–7, the figure captions,
    the footnotes, and the reference list skimmed. Not read: the
    separate online appendix (the derivations of (6)–(12), the arc
    elasticities, the EORA and Borusyak robustness checks, the network
    graphs); no number was taken from Figures 1–4. Checked: the hub and
    authority algebra of (5); the long-difference standardized effect
    against its R² (Limitations); each table's stars against its
    coefficient and standard error.
date: '2026-10-29'
summary: >-
  A country's real-income elasticity to a partner's productivity, from a
  constant-elasticity trade model with input-output links, predicts
  political alignment with that partner. Instrumented by a counterfactual
  Chinese productivity shock from the 1980 equilibrium (119 countries,
  1980–2010) or by air-versus-sea distance
  (pairs, 1970–2012), it moves UN voting similarity (0.094 SD per SD in
  the panel), lowers strategic rivalry, and raises formal alliances. The
  paper's own model is strategic: alignment is a costly action a country
  takes to raise a partner on whom its income depends.
---
<!-- inactive-ok-file: CLAIM-428 CLAIM-404 LIT-1422 LIT-1415 — Proposed, Unfetched or Unavailable; claims this reading bears on and works it names, cited as open or unread -->

# NOTE-tmpz95lz: Kleinman, Liu and Redding — International friends and enemies

## Contribution

It replaces bilateral trade, the usual measure of economic dependence in
the trade-and-conflict literature, with a general-equilibrium elasticity:
how much country n's real income moves when country i's productivity
rises. It computes this for 143 countries over 1970–2012, shows that
about 30 percent of pairs are "enemies" (negative elasticity), and then
asks whether the elasticity predicts political alignment. With two
instruments it finds that it does, and that the coefficient on bilateral
trade, controlled alongside it, is small and changes sign from one
specification to the next while the elasticity's does not.

## Key insight

Dependence is not trade. A country can depend on a partner it barely
trades with, through common markets and the cost of living, and two
exporters of the same raw material can be harmed by each other's growth.
Measured this way, a country whose income comes to rise with a partner's
productivity comes to vote with it, rivals it less and allies with it
more.

## Assumptions

- **The political model (1)–(3).** Each country's representative agent
  chooses costly political actions ξ_ni toward each partner i that raise
  i's productivity, z_i = z̄_i f_i(ξ_Ni). In the Nash equilibrium the
  first-order condition is U_ni · (∂ln z_i/∂ln ξ_ni) = (∂ln v_n/∂ln ξ_ni)
  (v_n/u_n): the larger n's real-income exposure U_ni, the more n does
  for i. The political part is non-parametric; the paper tests only this
  monotone prediction.
- **The trade model.** Constant trade elasticity θ (Armington in the
  exposition; Eaton–Kortum, Krugman, multi-sector and Caliendo–Parro
  input-output versions in the appendix). The empirical work uses the
  multi-sector input-output version with one median input-output matrix
  for all countries.
- **The exposure matrix.** U ≡ −(θ/(θ+1))(I − S)(I − V)⁻¹M + S, from
  linearizing market clearing and indirect utility, with S the
  expenditure shares, T the income shares, M = TS − I and world income
  the numeraire (12). Arc elasticities from exact-hat algebra give the
  same results, the paper says, for shocks up to the sample's cumulative
  productivity change.
- **Identification, China.** China's growth after 1978 is taken as
  supply-driven; the instrument is the counterfactual change in exposure
  from a 100 percent rise in Chinese productivity, computed from the
  1980 equilibrium.
- **Identification, air travel (Feyrer 2019).** Year-varying elasticities
  of sectoral expenditure shares to air and sea distance, with pair,
  importer-year and exporter-year fixed effects, predict shares, from
  which predicted exposure is computed. The exclusion restriction is
  that the changing relative cost of air and sea routes affects political
  alignment only through economic exposure.

## Key results

- **Descriptive.** Mean exposure is small and rises over time; about 30
  percent of pairs are enemies, typically raw-material exporters
  competing for markets (Chile and South Africa; Saudi Arabia and Niger).
  China moves from outside the top five authority scores in 1980 to first
  in 2010. PTA formation is followed by a rise in exposure, with no
  pre-trend (two-way fixed effects and de Chaisemartin–D'Haultfœuille).
- **China, long differences 1980–2010 (Tables 2–3, 119 countries).** OLS
  coefficient on Δexposure 44.12 (SE 15.10) for the κ-score of UN voting
  similarity, "a one standard deviation in real income exposure ... leads
  to a 0.26 standard deviation increase in political alignment"; similar
  for the S- and π-scores. IV 101.3 (27.67), first-stage Kleibergen–Paap
  F 21.82. With Δlog trade added (instrumented by 1980 trade), exposure
  stays at 81.23 (22.68) and trade is negative (−0.0173, n.s.), F 10.66.
- **Air travel, pair panel (Tables 4–5).** OLS 24.20 (3.824) on the
  κ-score, 653,214 pair-years. IV 60.66 (15.55), F 33.69, 480,452
  pair-years; "a one standard deviation increase in real income exposure
  leads to a 0.094 standard deviation increase in bilateral political
  alignment". With log trade instrumented as well, 77.09 (18.23), and
  trade enters positive (0.0255).
- **Rivalry and ideal points (Table 6).** IV coefficients on any,
  positional and spatial rivalry −21.41, −10.35, −15.55, all significant;
  ideological −3.819 (2.701), not significant, as the text later
  concedes. Ideal-point distance −88.06 (26.88).
- **Alliances (Table 7).** IV coefficients positive and significant for
  any alliance (17.79), defence pacts (15.02), non-aggression (21.90) and
  ententes (15.94); neutrality 10.75 (5.368), with an Anderson–Rubin p of
  0.1.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Countries that became more exposed to Chinese productivity growth moved toward China in UN voting, 1980–2010 | moderate | one cross-section of 119; IV F 21.82, 10.66 with trade |
| C2 | Within country pairs, exposure predicted by air-versus-sea distance raises UN voting similarity, lowers rivalry and raises alliances | moderate | Tables 5–7; the exclusion restriction is argued, not tested |
| C3 | The exposure measure is not proxied by bilateral trade | moderate | trade's sign and significance change across tables, exposure's do not |
| C4 | Economic dependence causes political alignment | moderate | two instruments agree in sign; the effect in the panel is 0.094 SD |
| C5 | The mechanism is strategic: costly political actions to raise a partner one depends on | weak | the model motivates the regression; no test separates it from other mechanisms |

## Concepts

- **Real income exposure U_ni**: d ln u_n / d ln z_i, the elasticity of
  n's real income per capita to i's productivity, all general-equilibrium
  effects included.
- **Economic friend / enemy**: U_ni > 0 / U_ni < 0, after the
  "friends and enemies" of neoclassical trade theory. U need not be
  symmetric.
- **Authority and hub scores** (Kleinberg 1999): the leading
  eigenvectors of U′U and UU′; an authority's growth moves others, a hub
  is moved by others'.
- **Market size, cross-substitution and cost-of-living effects**: the
  three channels through which a partner's productivity reaches n's real
  income in (10)–(11).

## Connections

It enters the trade-and-conflict literature (Polachek 1980; Mansfield 1995;
Barbieri 2002, the book after LIT-1422's article; Martin, Mayer and
Thoenig 2008) by changing the outcome from war to softer alignment, which
it argues is where most political influence lies (Nye 1990). Its second
instrument is Feyrer's air-travel design; by its abstract, the later NBER
paper of Feng and others on militarized conflict (LIT-1415) uses
air-against-maritime transport technology in the same way. Its measures of alignment
come from Signorino and Ritter, Bailey, Strezhnev and Voeten, Thompson and
Colaresi, and the Correlates of War alliances.

## Bearing on the record

- **CASE-150.** The flag on the case can be lifted: the outcomes include
  UN voting (S-, π- and κ-scores and ideal-point distance) and strategic
  rivalries (any, positional, spatial, ideological), and also formal
  alliances, which the case does not mention. The case's description is
  otherwise right. Three things the reading adds. The effect is small in
  the panel, 0.094 SD per SD of exposure. Ideological rivalry, the
  rivalry nearest to a change of view, is the one outcome the instrument
  does not move. And the case's "what it does not show" is sharper than
  it knew: the paper's own model is the strategic explanation the case
  sets against changed interpretive organization, since alignment there
  is an action chosen for its payoff, with preferences held fixed.
- **CLAIM-428.** The reading supports the claim's first half, that
  material interdependence couples outcomes, with a measure that can be
  negative: 30 percent of pairs are enemies. That a pair's dependence is
  organized as opportunity or as threat is, in the paper, decided by the
  sign of U, not by perspective; the paper offers nothing on the
  perspective that organizes the coupling.
- **CLAIM-404.** Not more than the case already says: alignment of
  states through what their incomes depend on is influence through
  payoffs, not through evidence or criteria.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Alignment is not attitude.** UN votes, rivalry codings and alliances
  are actions and classifications of states. Nothing in the paper speaks
  to opinion within a country.
- **The China cross-section is small** (119 observations), the R² of its
  OLS regressions under 0.1, and its IV with trade has a first-stage F of
  10.66.
- **The air-travel exclusion restriction** is argued from the fixed
  effects and not tested. Pairs whose air routes shortened relative to
  sea may have changed in other ways that matter politically (travel,
  migration, communication).
- **Errors and slips.** Footnote 4 says that by Perron–Frobenius U′U and
  UU′ "each have a unique eigenvector with all positive entries"; the
  theorem applies to positive or irreducible non-negative matrices, and
  U has negative entries for the 30 percent of enemy pairs, so the claim
  needs an argument the paper does not give. Table 2's column (1) has one
  regressor and R² 0.0484, so the standardized effect of exposure should
  be about √0.0484 = 0.22 SD, not the 0.26 stated, unless the regression
  carries unreported controls. The text first says that for rivalries
  "In all cases, we find a negative and statistically significant
  relationship" and a page later excepts ideological rivalry. "Inverse
  hyperbolic sign" (fn. 17) is sine; Table 5's third F is printed 33.629
  beside 33.69; "Kleinbergen-Paap" in Table 3's note.

## Open questions

- Does exposure move public opinion toward the partner, or only the
  state's votes and alignments?
- Can the strategic mechanism be told from a change in how a country's
  public or elite regards the partner, for instance by whether alignment
  persists after exposure falls?
- Why does ideological rivalry not respond to the instrument?
