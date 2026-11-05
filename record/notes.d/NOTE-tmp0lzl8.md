---
status: Read
paper: 'LIT-tmp1b9oy'
title: 'Kline and Moretti — The Tennessee Valley Authority, agglomeration and the big push'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read on 2026-11-05 from NBER Working Paper 19293, "August 2013, Revised
    June 2014", on NBER's own site
    (https://www.nber.org/system/files/working_papers/w19293/w19293.pdf), a
    lawful open copy in the authors' working-paper series. It thanks "the
    referees, two editors" and Andrew Garin "for pointing out a mistake in
    an earlier version of this article", so it is the post-referee text,
    not the typeset QJE version of record. Text extracted by pdftotext.
    Read: main text Sections I–VI (WP pp. 1–26), Tables I–VII, figure
    notes, and the appendix bound into the PDF (border imputation;
    comparison of structural and reduced-form estimates; cost-benefit).
    Not read: the separate Online Appendix tables A1–A4 (spillovers to
    adjacent counties, robustness of the agglomeration estimates). Page
    numbers below are the working paper's, not QJE pp. 275–331.
date: '2026-11-05'
summary: >-
  TVA transfers, peaking at about 10% of household income in 1950–55 and
  near zero after 1959, raised agricultural and manufacturing employment
  growth by about 10–12 points a decade in 1940–1960. Afterwards
  agriculture reversed and manufacturing kept growing about 3 points a
  decade faster. A constant log agglomeration elasticity (about 0.4–0.47,
  p > 0.66 for equality across densities) implies a unique steady state:
  slow convergence with momentum, not a big push, and no aggregate gain
  from relocation. Identification assumes productivity shocks independent
  over 20 years.
---
<!-- inactive-ok-file: THEORY-tmp10msz THEORY-919 THEORY-885 CLAIM-tmpc3x0c CLAIM-tmpw4ai2 CLAIM-tmpoh07b CLAIM-tmpqa0qu CLAIM-597 CLAIM-445 — Proposed or new; cited from the reading of Kline and Moretti (2014) as open -->

# NOTE-tmp0lzl8: Kline and Moretti — The Tennessee Valley Authority, agglomeration and the big push

## Contribution

A long-run (1940–2000) evaluation of one of the largest place-based
programmes in US history, on both sides of the end of its subsidy, with an
unusually clean withdrawal date (1959). It contrasts a sector without
agglomeration (agriculture, which reverts) with one that has it
(manufacturing, which persists), and then tests explicitly whether the
persistence is a big push into a second stable equilibrium or slow
convergence to a unique one. The answer is the second. It adds a framework
in which relocating activity raises national output only if the
agglomeration elasticity is higher where activity is sent.

## Key insight

Persistence is not self-sustainment. Under a unique equilibrium,
agglomeration feedback stretches a transitory shock into decades of
faster growth that still decays: "even the log-linear model exhibits
momentum due to the convergence process. Structural estimates are
necessary to determine whether truly permanent effects underlie the
qualitative patterns" (§IV.C). Forty years of persistence after the
subsidy ended is what a decaying echo would also produce; telling the two
apart takes the curvature of the feedback, not the duration.

## Assumptions

- **Selection on observables (§III).** Oaxaca–Blinder reweighting on 38
  covariates from 1920 and 1930 balances the counterfactual; the 1900–1940
  placebo passes. The six proposed authorities are taken to have failed
  for "largely exogenous political reasons", and their county borders are
  imputed by an algorithm (appendix).
- **Data.** "The quality of some of the key variables is not ideal"
  (§II.B).
- **Structural model (§IV).** Labour perfectly mobile at a national
  reservation utility; agglomeration acts with a one-decade lag through
  manufacturing density per square mile; the county productivity shock has
  a unit root. The short-run labour-demand elasticity is set at 1.5 from
  the literature (Hamermesh), not estimated; Appendix Tables A2–A4
  (not read) are said to vary it.
- **Identification of agglomeration (§V, p. 22).** Density changes lagged two
  decades are valid instruments if "the shocks to productivity νit be
  independent over a horizon of 20 years", which, the authors note,
  "prohibits counties from possessing long lasting heterogeneous trends".
- **Cost-benefit (§V.E).** Rests on "several unverifiable assumptions
  regarding the functioning of labor markets".

## Key results

- **The subsidy and its end (§II.A, p. 5).** "In 1959, Congress passed
  legislation making the TVA power generation system self-financing. From
  that year on, federal subsidies declined sharply." At the 1950–55 peak,
  "roughly $750 per year, or about 10% of average household income"; about
  73% of transfers fell in 1940–1958.
- **Net effect 1940–2000 (Table III, p. 11).** Decadalized, −5.6%
  agriculture and +5.9% manufacturing against the rest of the US; against
  the proposed authorities −0.071 and +0.053. Manufacturing wages and
  housing values do not respond. Median family income rises about 0.024
  a decade against the South and the proposed authorities.
- **During the subsidy (Table IV, p. 12).** "the 10-year growth rate of
  employment in both agriculture and manufacturing is 10.6 - 11.9
  percentage points larger in the TVA region".
- **After it, agriculture reverses (pp. 12–13).** "employment growth in
  agriculture falls behind, reversing the gains of the previous period.
  Estimates range between -13 and -16 percentage points" (Table IV:
  −0.134, −0.130, −0.166).
- **After it, manufacturing persists (p. 13).** "even after the cessation
  of federal outlays, manufacturing employment keeps growing significantly
  faster in TVA counties (although less fast than in the early period)":
  3.3, 3.5 and 3.2 points a decade. From the introduction: "forty years
  after TVA became financially self-sufficient, manufacturing employment
  in the region was still growing at a significantly faster pace" (p. 3).
- **Who kept up the capital (§III.D, p. 13).** The agricultural collapse is
  read as consistent with infrastructure that "without maintenance" "would
  have fully depreciated by 2000" (footnote 15 calls this reasonable
  against planners' rates "often around 5%"); in practice "from 1959
  onwards maintenance of the TVA capital stock was paid for by local
  taxpayers and local users of electricity."
- **The authors' reading (p. 13).** "The resilience of manufacturing
  employment in the face of this depreciation of the initial capital
  infusion indicates that firms in the region enjoyed a competitive
  advantage even after the subsidies lapsed. This is suggestive of
  agglomeration effects". For agriculture they cite Hornbeck and Naidu:
  "agricultural production does not appear to generate local economic
  spillovers."
- **The big push set up (§IV.C).** With a nonlinear agglomeration function,
  "multiple steady state equilibria are present, two of which are stable
  and one of which is an unstable tipping point".
- **Levels spline (Table V col. 4, p. 23).** One more worker per square
  mile raises labour demand 9.7% at low density, 4.2% at medium and about
  0 at high, "a strikingly concave pattern"; equal slopes rejected.
- **Log spline, the decisive result (Table VI, p. 23).** "we cannot reject
  a constant elasticity relationship in any of the IV specifications"; the
  p-values "are all above 0.66", point estimates 0.40–0.45 (col. 4: 0.443,
  0.456, 0.466). With β = 0.47 the implied agglomeration elasticity is "in
  the neighborhood of 0.2" (p. 24).
- **Verdict (§V.D, pp. 24–25).** "the effects of TVA will eventually die
  out"; "the estimated shape of the curve implies the system admits a
  unique steady state equilibrium so that the TVA region will ultimately
  revert back to its pre-program equilibrium." From the introduction:
  "this finding casts doubt on the traditional big push rationale for
  spatially progressive subsidies" (p. 4).
- **Direct effects by period (Table VII, p. 24).** 0.185–0.225 on labour
  demand in 1940–1960; −0.036 to +0.033 and not significant in 1960–1980
  and 1980–2000.
- **What carries the persistence (appendix §2).** Fitting a decadal
  depreciation d to the reduced form gives d = 0.021, "an annual
  depreciation rate of" 0.002, and with the autoregressive coefficient 0.4
  predicts 1960–2000 manufacturing growth of 0.123 against 0.132 in the
  reduced form. The post-1960 gain is reproduced as an echo of the 1940–60
  shock through agglomeration momentum plus infrastructure that barely
  depreciated; no equilibrium switch is needed.
- **Aggregate (§IV.B, §V.E).** "When the agglomeration elasticities are
  everywhere equal", "spatially reallocating labor has no aggregate
  effects"; the TVA "should be thought of as only nominally place based in
  nature. Rather, it is a national investment". Benefits $23.8–36.5B
  against $17.3B of cost, present value at 3%.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | TVA raised agricultural and manufacturing employment growth in 1940–1960 | moderate to strong: three control groups, placebo passes, selection on observables | Table IV |
| C2 | After 1960 the agricultural gain reversed and the manufacturing gain persisted | moderate | Table IV |
| C3 | The manufacturing agglomeration elasticity is constant in logs across density ranges | moderate: p > 0.66, but power against modest nonlinearity not reported (s.e. about 0.10–0.15) and identification needs 20-year independence | Table VI |
| C4 | So the system has a unique steady state and the TVA's effects will die out | weak to moderate: follows from C3 within the model; a forecast | §V.D |
| C5 | The national benefit comes from the infrastructure's direct productivity effect, not relocation | weak: unverifiable labour-market assumptions | §V.E |

## Concepts

- **Big push (poverty trap)**: a large enough temporary investment crosses
  an unstable tipping point into the basin of a high equilibrium and then
  persists without support.
- **Agglomeration elasticity**: the elasticity of productivity with respect
  to manufacturing density. Constant, it makes the agglomeration function
  concave in levels and linear in logs, with a single equilibrium and
  geometric convergence.
- **Momentum against permanence**: under a unique equilibrium, feedback
  lengthens a transitory shock's effect without making it permanent.
- **Nominally place-based**: a programme whose national gain is from
  direct productivity, its local gain offset by losses elsewhere.

## Connections

It belongs with the work on temporary shocks that move economic activity
(Davis and Weinstein; Redding and Sturm), and NOTE-1122 already cites it
("Kline and Moretti 2014, p. 7") in that lineage. Its agglomeration
evidence draws on Greenstone, Hornbeck and Moretti (2010); for agriculture
on Hornbeck and Naidu (2012); for electricity alone, Kitchens. Neumark and
Simpson (2015), filed beside it, summarize it as evidence that
place-based gains need not be self-sustaining.

## Bearing on the record

- **CLAIM-tmpc3x0c (when support is safe to withdraw): qualifies,
  strongly.** The sector split fits the claim's first condition:
  agriculture, where the supply did the work, reverted; manufacturing,
  with feedback of its own, kept gaining for forty years. But the
  structural result says manufacturing is not self-sustaining either: it
  sits under a unique equilibrium and "will eventually die out", its
  persistence carried by momentum and by infrastructure that local
  ratepayers kept up. So persistence through a full turnover can be met by
  slow reversion; telling the two apart needs the curvature of the
  feedback, not the duration.
- **CLAIM-tmpw4ai2 (ignition threshold, collapse, hysteresis):
  qualifies.** A field test for the threshold signature in a
  state-dependent feedback, and no threshold is found: the log elasticity
  is constant, the steady state unique. Upkeep that rises with the
  structure's own state need not show ignition or hysteresis; whether it
  does depends on curvature, and these data favour a concave, log-linear
  form. The model is not contradicted; its empirical reach is narrowed.
- **CLAIM-597 (supplied upkeep never becomes optional): supports, for
  agriculture.** Gains tied to supplied infrastructure and inputs reversed
  once the federal supply stopped. Caveat: the paper's own depreciation
  figures disagree, about 5% a year in footnote 15 against about 0.2% a
  year in the appendix fit.
- **CLAIM-tmpoh07b (doing the work crowds out capacity): weak.** No
  capacity measure. One pointer: the sector whose advantage was built by
  firms' own activity (learning, thick markets) is the one that persisted.
- **CLAIM-tmpqa0qu (one-way against reciprocal supply): tangential.** The
  1959 switch turned a one-way federal transfer into a utility financed by
  its local users; the paper draws nothing from it.
- **QUESTION-398 (independence from the founding intervention).** A
  regional withdrawal experiment with a clean end date. The structural
  answer is that manufacturing has not become independent; it returns to
  the pre-programme equilibrium, slowly.
- **THEORY-919 (Juhász, the Napoleonic blockade): complements.** Both are
  temporary support followed by persistent manufacturing, credited to
  local increasing returns. Juhász's effect fading by 1896 fits slow
  reversion under a unique equilibrium; the constant-elasticity test is
  one she does not run, and it warns against reading her persistence as
  multiple equilibria. CLAIM-445 (a protective regime becomes
  self-maintaining): the TVA itself became self-financing after 1959, a
  fact the paper reports and does not analyse.
- **THEORY-863 (Arthur) and THEORY-885 (Pierson), increasing returns and
  lock-in.** The increasing returns found here are positive but too weak
  in curvature for lock-in.
- Filed: THEORY-tmp10msz. No instruction for machine-learning practice.

## Limitations

- **Bundled treatment.** The reduced form cannot separate electricity,
  roads, the canal, fertilizer and schools.
- **An indirect test.** The big-push test concerns an agglomeration
  function estimated on all US counties, 1960–2000, not the TVA region's
  own trajectory; nonparametric identification is "inherently untestable
  without further assumptions" (footnote 25), and power against modest
  nonlinearity in logs is not reported.
- **Restrictive identification.** Productivity shocks independent over 20
  years; the labour-demand elasticity set at 1.5, not estimated.
- **Persistence credited to agglomeration partly by elimination.** The
  appendix reproduces the post-1960 gain with momentum and near-zero
  depreciation (0.2% a year), while footnote 15 calls full depreciation by
  2000 at planners' rates of about 5% reasonable. The two are not
  reconciled.
- **Data.** "not ideal" (§II.B); the proposed-authority borders are
  imputed.
- **Reporting slips.** The text gives a p-value of 0.002 for equal slopes
  in Table V col. 4, where the table prints 7.1e-04; the text prints −0.51
  for −0.051 (p. 11).
- **Scope.** "our findings do not necessarily apply to all contexts":
  manufacturing, in a period of expansion. Not about displacement or
  coproduction, though selection favoured counties "willing to receive
  technical and advisory assistance" that "had planning agencies" (p. 5).
- **Version.** The working paper, not the typeset version of record.

## Open questions

- Is the agglomeration function nonlinear in logs at a scale these
  standard errors cannot see? A better-powered estimate would tell.
- Did the TVA region in fact converge back after 2000? A later follow-up
  would test the forecast.
- How much of the post-1960 persistence is locally maintained
  infrastructure rather than agglomeration? Separating the two needs a
  measure of the capital stock's upkeep.
