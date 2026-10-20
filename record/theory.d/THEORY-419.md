---
number: 419
status: Active
formerly:
- THEORY-tmp2k3a9
title: "In a structural causal model of autonomous equations, with intervention do(X = x) defined, as Pearl defines it, as a surgery that deletes X's own equation, sets X to x and solves the rest, and with observing X = x violating no equation and amounting to ordinary conditioning, models that agree on every observational distribution can disagree on the effect of an intervention, and in a structural equation y = βx + ε the coefficient β is the rate of change of E[Y | do(x)], which equals the regression slope of Y on X only when X is uncorrelated with ε"
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision
    for THEORY-419 (batch 054, ADR-047 v2). The definition is taken as
    Pearl gives it in the pages NOTE-696 read in full (§5.3.3 and the
    Epilogue). Its two consequences are re-derived in the dated note below.
    The regression clause is stated exactly. The note also corrects the
    body's quoted parameters for the two models: they agree as quoted only
    when x = u. The book-wide reading the promote_when asked for moves to
    QUESTION-tmpa4291.
tags:
- causality
- probabilistic-modeling
- philosophy-of-science
date: '2026-10-16'
source:
- LIT-894
summary: >-
  Pearl (2009), [LIT-894](../literature.d/LIT-894.md), skimmed in [NOTE-696](../notes.d/NOTE-696.md) from four excerpts the author
  posts: the contents, the second-edition preface, §§5.3.2–5.4.1 and the
  Epilogue, 46 of some 480 pages. The account is well established and the
  excerpts state it in full; Proposed because it rests on a skim. The
  surgery needs autonomous equations and a diagram saying which equation
  belongs to which variable. The excerpts state the three rules of the
  do-calculus without derivation, and contain no three-level hierarchy of
  association, intervention and counterfactual.
supports:
- CLAIM-127
- CLAIM-130
- CLAIM-341
---
<!-- inactive-ok-file: NOTE-696 — Skimmed; the reading this account rests on, as it says -->
<!-- inactive-ok-file: CLAIM-127 CLAIM-130 — Proposed; the claims that cite this account, named in Connections -->
<!-- inactive-ok-file: THEORY-491 — Proposed; named in Connections, not leaned on -->

# THEORY-419: In a structural causal model of autonomous equations, with intervention do(X = x) defined, as Pearl defines it, as a surgery that deletes X's own equation, sets X to x and solves the rest, and with observing X = x violating no equation and amounting to ordinary conditioning, models that agree on every observational distribution can disagree on the effect of an intervention, and in a structural equation y = βx + ε the coefficient β is the rate of change of E[Y | do(x)], which equals the regression slope of Y on X only when X is uncorrelated with ε

## Source

Pearl (2009), [LIT-894](../literature.d/LIT-894.md), *Causality: Models, Reasoning, and Inference*, second
edition, skimmed in [NOTE-696](../notes.d/NOTE-696.md). Read: the table of contents, the Preface to
the Second Edition (p. xix), §§5.3.2–5.4.1 (pp. 154–163) and the Epilogue
(pp. 401–428), each in full. Nothing else in the book was read. [NOTE-696](../notes.d/NOTE-696.md)
filed no THEORY because the excerpts ground no claim about language or
interpretation. This one is about the operator itself, which the excerpts
state in full; it is Proposed because it rests on a skim.

## What was actually shown

**Surgery (pp. 157–158, 417).** "Intervention amounts to a surgery on
equations (guided by a diagram) and causation means predicting the
consequences of such a surgery" (p. 417). Under do(X = x), X's own equation
"should be overruled and replaced with the equation X = x" (p. 158).
Structural equations "define a state of equilibrium – one that is violated
when the equilibrium is perturbed by outside interventions" (p. 157), so
they stand for every submodel an intervention can produce.

**Seeing is conditioning (pp. 158, 421).** "The passive observation X = x
should not violate any of the equations" (p. 158). E(Y | x) is "the
standard conditional or observational expectation", E(Y | do(x)) "the
controlled expectation". In P(Rain | Wet) "the vertical bar stands for the
phrase: 'given that we see'" (p. 421).

**Two models, one distribution (§5.3.3, p. 157).** Model M (x = u + ε₁,
z = αx + ε₂, y = βz + γu + ε₃) and M′ (x = ε₁, z = α′x + ε₂,
y = β′z + δx + ε₃), with α′ = α, β′ = β and δ = γ, "yield the same
probabilistic predictions". But E[Y | do(x)] is βαx in M and (β′α′ + δ)x in
M′. In M, E(Y | do(x)) = αβx while E(Y | x) = (αβ + γ)x.

**What a structural equation claims (§5.4.1, pp. 160–162).** Definition
5.4.1: y = βx + ε is structural if, "in an ideal experiment where we control
X to x and any other set Z of variables … to z", Y is βx + ε with ε not a
function of the settings. So β = ∂E[Y | do(x)]/∂x (5.24), which "has nothing
to do with the regression coefficient r_YX" (p. 161). Leaving a variable
out of an equation is a testable invariance under manipulation (5.23),
while "regression equations make no empirical claims whatsoever" (p. 160).

**What could have come out otherwise.** The two models could have been
told apart by their observational distribution. They cannot. Only the
interventional query separates them.

## What this does not say

- **That surgery is always defined.** It needs autonomy (each equation an
  independent mechanism, p. 414) and a diagram assigning each equation to
  its variable (p. 417). Rewrite the equations into an algebraically
  equivalent set and "there is no such thing as 'the equation for Y'".
  Causality also needs a cut between modelled and unmodelled: "If you wish
  to include the entire universe in the model, causality disappears"
  (p. 420).
- **That every do-query can be answered from data.** Surgery is well
  defined even for unknown functions, but identification, "uniquely, from
  the data and the graph", is a further question (p. 159). With an
  unobserved genotype, P(c | do(s)) is "noncomputable" (p. 423).
- **That an assigned input needs the operator.** For a parentless,
  unconfounded variable, as in an experiment that assigns it, seeing and
  doing coincide ([NOTE-696](../notes.d/NOTE-696.md)'s inference from Rule 2 and p. 418, not a
  sentence of the excerpts).
- **That there is a third operation besides observing and intervening.**
  The Epilogue names two components of science, observations and
  interventions (p. 421).
- **That the book states a three-level ladder.** None appears in the pages
  read, and the rest was not checked.
- **That the do-calculus is derived here.** Its three rules are stated
  (pp. 422–423), with graph notation defined in §3.4, which was not read.

## Connections

- Woodward's interventionism ([THEORY-138](THEORY-138.md)) defines cause by the possibility
  of an intervention and constrains what counts as one (M1–M4). This
  account supplies the formal semantics of the intervention in a
  structural model. The two are compatible; neither is filed as relying on
  the other.
- [CLAIM-127](../claims.d/CLAIM-127.md) and [CLAIM-130](../claims.d/CLAIM-130.md) cite the book for the definition of do(), and
  [CLAIM-127](../claims.d/CLAIM-127.md)'s point that observing and conditioning are one operation is
  stated here.
- Randomisation as surgery, with a coin as the new mechanism (p. 418),
  bears on the arguments weighed in [THEORY-491](THEORY-491.md).

## Note of 2026-10-20: the two consequences, derived

Derived for the promotion audit (batch 054, [ADR-047](../decisions.d/ADR-047.md) v2), taking the
surgery and conditioning definitions as stated on pp. 157–158, 417 and 421.

1. **Same observations, different interventions.** In M (x = u + ε₁,
   z = αx + ε₂, y = βz + γu + ε₃, with independent zero-mean Gaussian u
   and ε's), put k = σ_u²/(σ_u² + σ₁²) and ε₃′ = γ(u − kx) + ε₃.
   Cov(u − kx, x) = 0, so ε₃′ is independent of x and of ε₂. Then
   M′ (x exogenous, z = αx + ε₂, y = βz + γk·x + ε₃′) is a Markovian model
   with the same joint distribution of (x, z, y). Surgery on x gives
   E[Y | do(x)] = αβx in M and (αβ + γk)x in M′, which differ whenever
   γ ≠ 0 and σ_u > 0. A simulation (α = 0.7, β = 1.3, γ = 0.9, σ_u = 1,
   σ₁ = 0.8, 2·10⁶ draws) reproduced matching covariances and do-slopes
   0.91 and 1.46.
2. **The structural coefficient.** If y = βx + ε is structural (Definition
   5.4.1), then under do(X = x), Y = βx + ε with ε's distribution unchanged,
   so E[Y | do(x)] = βx + E[ε] and its derivative is β. The regression slope
   is β + Cov(X, ε)/Var(X), which is β exactly when X and ε are
   uncorrelated.
3. **A correction to "What was actually shown".** The quoted agreement of M
   and M′ with α′ = α, β′ = β and δ = γ, and E(Y | x) = (αβ + γ)x in M, hold
   only when σ₁ = 0, that is when x = u. For σ₁ > 0 the regression slope is
   αβ + γk, and the matching M′ needs δ = γk and
   Var(ε₃′) = γ²σ_u²(1 − k) + σ₃². The conclusion needs only one such pair,
   so it stands.

Whether the book defines intervention the same way in the chapters not read
is [QUESTION-tmpa4291](../questions.d/QUESTION-tmpa4291.md).
