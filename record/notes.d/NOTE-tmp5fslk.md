---
status: Read
paper: 'LIT-tmplr1w9'
title: 'Seth — Measuring autonomy and emergence via Granger causality'
version: 1
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Read in full from the published version deposited in Sussex Research
    Online (eprint 29803), downloaded from Sussex figshare 23373605: a
    19-page PDF, a repository cover sheet and pp. 179–196. §§1–5, Tables
    and figure captions, the Appendix and the reference list. Extracted
    with pdftotext. Table 1's values came through without their row and
    column positions, so I read its caption and the prose that interprets
    it, not the cell values. Figures were read from captions and prose
    only. The MATLAB toolbox was not inspected.
date: '2026-10-16'
summary: >-
  G-autonomy ga_{X|E} is the log ratio of a variable's prediction-error
  variance without and with its own past, given external variables E.
  G-emergence ge_{M|m} = ga_{M|m}·(1/N)Σ gc_{mᵢ→M} makes a macro variable
  emergent to the extent that it is both autonomous from and Granger-caused
  by its micro variables. Validated in a predator–prey model and a boids
  model, where flocking shows high G-emergence and Granger causation from
  the flock's centre of mass to each boid. Seth says the measures are
  relative to the predictor and the variables included.
---

# NOTE-tmp5fslk: Seth — Measuring autonomy and emergence via Granger causality

## Contribution

Before this paper, weak emergence (Bedau) had only qualitative degrees, and
autonomy had information-theoretic measures (Bertschinger et al.) that were
hard to estimate for many variables. After it, both have regression-based,
graded measures with F-test significance: G-autonomy and G-emergence. It
also offers an "ontologically innocent" reading of downward causation, as
Granger causation from a macro variable to micro variables.

## Key insight

Granger's question, whether a series' past helps predict another, can be
pointed at a variable's own past (autonomy), or at the relation between a
macro variable and its parts. A weakly emergent macro variable is then one
that its parts do predict, but not completely, so that its own history
still helps.

## Assumptions

- **Covariance stationarity** of every series (§2.1). Both simulations
  first-difference the series to get it, and Dickey–Fuller tests confirm
  it for the predator–prey data (§3.2.2).
- **A regression model class**: linear MVAR, or polynomial (Taylor)
  regressors of order q for the nonlinear measures (Eq. 5). The model
  order is chosen by AIC.
- **The variable set is the analyst's.** G-emergence can be positive because
  relevant micro factors are left out, or because the macro variable is
  more transparent to the prediction algorithm than the micro variables
  are. With the system itself as the predictor it would be zero, "since …
  micro causes are jointly sufficient to give rise to macro properties"
  (§5.2).
- **No temporal (diachronic) emergence.** A process with new features over
  time is nonstationary and cannot be measured (§5.2.1).
- **Every element must vary over time.** Autonomy from a static feature of
  the environment cannot be measured (§5.1).

## Key results

- **Eq. 3, G-autonomy** — ga_{X1|X2} = log(var(ε₁ with X1's own lags
  omitted)/var(ε₁ full)). Significance by an F-test that X1's own
  coefficients are zero.
- **Eq. 4, G-emergence** — ge_{M|m} = ga_{M|m}·(1/N)Σᵢ gc_{mᵢ→M}. It is zero
  if M is independent of m (no G-causation) or fully predicted by m (no
  G-autonomy).
- **Eq. 7, Table 1, a constructed five-variable system** — the G-autonomies
  sort as built: white noise X1 and X1-driven X2 score zero, while X3 and
  X5, with their own autoregressive terms, score high. X4's own-past
  predictability is carried by X3, so its score is low. The three built-in
  G-causalities are the significant ones. So the set of G-causalities does
  not fix the G-autonomies.
- **§3, predator–prey** — mean predator G-autonomy, linear and nonlinear:
  random movement is highest, then the evolved controller (condition 4),
  then environment plus internal state (condition 3), then pursuit of one
  prey (condition 2). All pairwise differences are significant after
  Bonferroni correction (Fig. 3). Ten trials of 10⁴ steps, order-4 models,
  robust to order 8.
- **§4, boids** — 10 boids, 25 runs of 5000 steps per condition. Linear and
  nonlinear G-emergence of the centre of mass are significantly higher in
  the hand-chosen flocking condition H than in rigid-formation L or random
  R (Fig. 5). Over an 11 × 11 × 11 parameter sweep the measure mostly
  changes smoothly, with some sharp transitions (Fig. 6). Granger causation
  from the centre of mass to each boid is also highest in H (Fig. 7).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | G-autonomy captures autonomy as self-determination: zero for white noise and for purely driven variables | moderate | Eq. 7 construction and Table 1; by design |
| C2 | Evolutionary adaptation increases G-autonomy in the predator–prey model | moderate | Fig. 3; one model, one evolved controller, conditions ordered as built |
| C3 | High G-emergence tracks visually compelling flocking | moderate | Fig. 5; condition H chosen by hand as the compelling one |
| C4 | G-emergence is robust, changing smoothly over most of parameter space | weak | Fig. 6, by inspection |
| C5 | Downward causation can be measured, without ontological cost, as Granger causation from macro to micro | interpretive | §4.2; a definition, not a finding |
| C6 | G-emergence can be positive with every micro factor measured, because of the predictor's limits | assertion | §5.2; stated as a requirement for the measure to be useful |
| C7 | Weak emergence, not strong, is the right frame for consciousness; volition might correlate with downward G-causality in the brain | speculative | §5.3; a hypothesis, untested here |

## Method

1. Preprocess each series to one variable (distance from the arena's
   centre), drop transients, de-mean and first-difference.
2. Fit a full MVAR (or polynomial-regressor) model of order p by OLS, AIC
   for p.
3. G-autonomy: refit without the variable's own lags; take the log
   variance ratio. G-causality: refit without the other variable's lags.
4. G-emergence: Eq. 4, or Eq. 6 in the nonlinear case. It is significant
   if the G-autonomy and G-causality terms are.

## Concepts

- **G-autonomy** — how much a variable's own past improves its prediction
  given a set of external variables (§2.2).
- **G-emergence** — a macro variable both G-caused by and G-autonomous
  from its micro variables, measured by Eq. 4 (§2.3). A "continuous
  version" of Bedau's weak emergence, based on prediction, not on
  simulation or explanation (fn. 1).
- **Downward (Granger) causation** — G-causality from a macro variable to
  its micro variables (§4.2).

## Connections

- **Builds on** Granger (1969, [LIT-tmppqyor](../literature.d/LIT-tmppqyor.md)), Bedau's weak emergence, and
  Bertschinger et al. (2008) on autonomy. It compares itself in prose with
  Shalizi and Moore's predictive efficiency, Polani, Atmanspacher's
  contextual emergence and Bar-Yam's multiscale variety (§5.2.3). Transfer
  entropy is "a more general version of Granger causality" (§5.1.1). By
  Barnett, Barrett and Seth ([NOTE-tmp2veo7](NOTE-tmp2veo7.md)) the two are equivalent for
  Gaussian data.
- **The causal-emergence readings.** [NOTE-726](NOTE-726.md) relays Hoel et al.'s
  complaint that earlier measures, Seth's among them, were not based on
  causal models. That is right, and Seth says so himself (§2.1, §5.2).
  [NOTE-791](NOTE-791.md) reads Barnett and Seth's dynamical independence, a later
  criterion from the same group. It asks only that the micro history add
  nothing to the macro variable's self-prediction, T(X → Y | E) = 0,
  where G-emergence asks for dependence and autonomy at once. [NOTE-010](NOTE-010.md)
  lists Seth 2010 as a named alternative to ΦID.
- **[THEORY-497](../theory.d/THEORY-497.md)** says a macro feature can supervene on the present
  state and still carry information about the future, "because
  supervenience is instantaneous and prediction runs across time". That
  is the gap G-emergence measures. It is my connection; neither text
  makes it.

## Bearing on the record

- Filed as [THEORY-tmp427vb](../theory.d/THEORY-tmp427vb.md), Proposed: the measure behaves as designed
  in two hand-built models, and nothing tests it against a criterion
  independent of its construction.
- The centre of mass is a function of the boids' positions at the same
  time. An intervention on it that leaves the boids at that time unchanged
  does not exist. So the downward Granger causation of Fig. 7 cannot be an
  interventional effect in Eichler and Didelez's sense
  ([NOTE-tmpm48uq](NOTE-tmpm48uq.md)), with or without every boid measured. Seth claims no
  more than prediction, and [CLAIM-tmpa4kr6](../claims.d/CLAIM-tmpa4kr6.md) files the point so that
  the stronger reading has an address. The argument is mine.
- **For the Anthology of the SOTA:** no instruction for ML practice.

## Limitations

- Both validations are hand-built. The conditions are ordered by
  construction, and condition H is "selected by hand" as compelling
  flocking. Nothing scores emergence independently of the measure.
- Each position is collapsed to distance from the arena's centre, a
  nonlinear map, before any regression. For the linear measures, part of
  what Granger causation from the centre of mass to a boid detects may be
  this transformation, which a linear regression on the boids' transformed
  pasts cannot undo. The text does not say which variables the Fig. 7
  regressions condition on. This is my reading, not tested.
- Eq. 4 at its limits: if m's past predicted M exactly, both residual
  variances in ga would be zero, and the ratio would be undefined, not
  zero. "Fully predicted" can only mean that M's own past adds nothing.
  My reading.
- The Appendix's genotype count does not add up: a 29-element genotype is
  given as five biases and "the remaining 23" weights. The network it
  describes, 6–3–2 fully connected, has 24 weights. A typo, most likely,
  with no bearing on the results.
- Linear and nonlinear G-autonomy and G-emergence agree qualitatively
  throughout, which Seth reads as evidence that linear measures suffice.
  It is equally what one would see if the Taylor terms added little in
  these models.

## Open questions

- Does G-emergence track anything that an independent criterion of weak
  emergence picks out, outside models built to show it?
- How does G-emergence relate to dynamical independence ([NOTE-791](NOTE-791.md)) and
  to ΦID's causal decoupling ([NOTE-010](NOTE-010.md)) on the same system?
- G-autonomy against autonomy as organizational closure (Seth's own,
  §5.1).
