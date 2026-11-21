---
status: Proposed
title: "A model's parameter complexity and its behavioural complexity come apart: when its predictions depend on a few stiff combinations of parameters and barely on the rest, it can be hard to fit and still predictive, so simplicity can belong to how a system responds to observation rather than to its mechanism"
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that, in the multiparameter models where sloppiness is
  reported (systems biology, the hopping model, the critical Ising model
  under decimation), predictions for the observables in question depend
  on parameter directions that the fitting data leave unconstrained, so
  that a model fitted only along its stiff directions predicts those
  observables no better than one fitted to wrong values along them; or
  that the spread of Fisher eigenvalues reported in those models is an
  artefact of the parametrization that a reparametrization of the same
  model removes. A model that predicts badly because a sloppy direction
  matters for a new observable does not defeat it: the claim is relative
  to the observables fitted.
tags:
- information-geometry
- mathematical-statistics
- philosophy-of-science
- complex-systems
date: '2026-11-21'
line:
- formal-apparatus
- learned-structure
grounds:
- THEORY-774
- THEORY-777
- THEORY-742
- LIT-tmpsqbr9
- THEORY-tmpd7a4j
- LIT-tmp0fpti
- LIT-1299
uses:
- TERM-tmp5z2du
summary: >-
  A's thesis at A19 §1, §4, §7 and §10 of the exchange "Rich Get Richer
  Power Laws": a model can need many numbers to specify (parameter
  complexity) and few to describe what it predicts (behavioural
  complexity), because its predictions are sensitive to a few
  combinations of parameters and barely to the rest; such a model can be
  hard to fit and still predictive, and "simplicity can be a property of
  how a system responds to observation". The record held the spectra in
  two worked cases ([THEORY-774](../theory.d/THEORY-774.md), [THEORY-777](../theory.d/THEORY-777.md)) but not the general claim.
  A's analogy to neural networks is recorded and not adopted: sloppiness
  assumes a regular Fisher matrix, which overparameterized networks lack.
  The wording is A's (the other assistant in the exchange "Rich Get
  Richer Power Laws", A19); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-777 — Proposed reading, one of the two worked cases -->
<!-- inactive-ok-file: LIT-tmpsqbr9 LIT-tmp0fpti — Deferred, registered 2026-11-21 from the exchange, unread -->
<!-- inactive-ok-file: TERM-tmp5z2du — filed with this claim from the same exchange, Proposed -->
<!-- inactive-ok-file: SYNTHESIS-075 — Proposed account, cited for the target-relativity this claim sits beside -->
<!-- inactive-ok-file: ARG-tmpmvc5e — new and Proposed or Rejected, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21 -->
<!-- inactive-ok-file: ARG-tmpv3nqz THEORY-tmpd7a4j THEORY-tmpgsgka THEORY-tmpkoje5 — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# CLAIM-tmpficzj: A model's parameter complexity and its behavioural complexity come apart: when its predictions depend on a few stiff combinations of parameters and barely on the rest, it can be hard to fit and still predictive, so simplicity can belong to how a system responds to observation rather than to its mechanism

## The claim

A19 §1 draws the distinction: "**Parameter complexity:** How many
independent numbers are required to specify the microscopic model?
**Behavioral complexity:** How many independent quantities are needed to
describe its observable predictions? The first can be enormous while the
second is surprisingly small."

They come apart when the model is **sloppy**: its Fisher eigenvalues,
under the experiment in question, spread over many decades, so its
manifold of predictions is a hyperribbon ([TERM-tmp5z2du](../terms.d/TERM-tmp5z2du.md)). Three
consequences follow, all A's:

1. **Hard to fit, still predictive.** "A model can be extremely difficult
   to fit at the microscopic parameter level while still making highly
   accurate predictions" (A19 §4), because the predictions in question
   depend on the few stiff combinations the data do constrain. The
   converse holds too: "even a sophisticated model can fail when its
   poorly constrained directions affect the particular outcome you want
   to predict."
2. **Understanding as invariance.** Reduction and effective theories are
   complementary, and an effective theory finds "**which details can be
   changed without changing the answer**" (A19 §7).
3. **Simplicity as a response to observation.** "**Simplicity can be a
   property of how a system responds to observation.** If an enormous
   collection of microscopic models all produce nearly the same
   macroscopic predictions, then the observable phenomenon is effectively
   simple—even if its underlying mechanism is not" (A19 §10).

## Why the record should hold it

The record has the two cases the general claim rests on in physics: in the
hopping model, eigenvalues separate by a factor of order t when the
density is seen after t steps ([THEORY-774](../theory.d/THEORY-774.md)); in the critical Ising model
under decimation, the irrelevant directions fall by up to six decades
while two stay ([THEORY-777](../theory.d/THEORY-777.md)), and the Fisher information lost is a
conditional covariance ([THEORY-742](../theory.d/THEORY-742.md)). Machta and colleagues read both as
"a model is sloppy because it is observed at a scale much larger than its
own" ([LIT-1299](../literature.d/LIT-1299.md), as read in its note). The breadth of the claim, across
systems biology models, rests on Gutenkunst and colleagues
([LIT-tmpsqbr9](../literature.d/LIT-tmpsqbr9.md)) and the reviews ([LIT-tmpm1tji](../literature.d/LIT-tmpm1tji.md), [LIT-tmp0fpti](../literature.d/LIT-tmp0fpti.md)). The 2015
review was read on 2026-11-21 and grounds the claim through
[THEORY-tmpd7a4j](../theory.d/THEORY-tmpd7a4j.md) (see the note below); the survey and the 2023 review are
Deferred and unread, so the claim stays interpretive and Proposed.

It sits beside [CLAIM-401](CLAIM-401.md) and [SYNTHESIS-075](../syntheses.d/SYNTHESIS-075.md): adequacy relative to a
declared target. Sloppiness is the parametric face of that relativity:
which directions are stiff depends on which observables are fitted.

## What it does not say

- **Not that the sloppy directions do not matter.** They matter for
  other observables; the claim is relative to the experiment
  ([TERM-tmp5z2du](../terms.d/TERM-tmp5z2du.md), condition 1).
- **Not that a hierarchy of sensitivities indicates criticality** or a
  power law in event sizes (A19 §5; [TERM-tmp5z2du](../terms.d/TERM-tmp5z2du.md)).
- **Not, yet, that it holds for neural networks.** A19 §10 presses the
  analogy: "A neural network may contain billions of parameters, but only
  some combinations may significantly affect particular outputs or
  tasks", and calls the connection "strong" while granting the analogy
  "isn't exact". The record does not adopt it. Sloppiness is stated for a
  regular model, whose Fisher matrix has full rank; an overparameterized
  network is singular, its Fisher matrix degenerate on sets of
  parameters, and the record's account of its effective parameter count
  is the learning coefficient, which falls below half the parameter count
  where the optimal set is degenerate ([THEORY-087](../theory.d/THEORY-087.md), [THEORY-1253](../theory.d/THEORY-1253.md)). How a
  hyperribbon and a singular stratification relate is the owner's
  question at U24 and is filed with that turn. The analogy and why it
  fails are [ARG-tmpmvc5e](../arguments.d/ARG-tmpmvc5e.md).

## Errors in the turn

A19 §5's table pairs "critical exponents" with the "rates at which
perturbations grow or shrink under rescaling". For the Fisher eigenvalues
the rate the record holds is b^(2y−d) per step, with the dimension d in
it ([THEORY-777](../theory.d/THEORY-777.md)), and the metric passes exactly to the coarse data only
when the renormalized Hamiltonian stays in the family ([THEORY-742](../theory.d/THEORY-742.md)). A's
own caveat in the same section ("One should not equate stiffness and RG
relevance in every setting") stands. It is A's, not the sources': the 2015
review says the Ising model develops stiff directions "along precisely
those parameter combinations deemed 'relevant' under the renormalization
group" ([LIT-tmpm1tji](../literature.d/LIT-tmpm1tji.md), §V; note of 2026-11-21).

## Note of 2026-11-21: Transtrum, Machta & Sethna (2010, 2011) and Transtrum et al. (2015), read

Read in [NOTE-tmpamhd2](../notes.d/NOTE-tmpamhd2.md), [NOTE-tmpzxtnv](../notes.d/NOTE-tmpzxtnv.md) and [NOTE-tmphbpab](../notes.d/NOTE-tmphbpab.md) ([THEORY-tmpkoje5](../theory.d/THEORY-tmpkoje5.md),
[THEORY-tmpgsgka](../theory.d/THEORY-tmpgsgka.md), [THEORY-tmpd7a4j](../theory.d/THEORY-tmpd7a4j.md)).

- **Consequence 1 is theirs.** 2015, §I: "As long as the model predictions
  depend on the same stiff parameter combinations as the data, the
  predictions of the model will be constrained in spite of large numbers
  of poorly determined parameters." 2010: "although parameters cannot be
  reliably extracted by fitting degenerate models, it is still possible to
  constrain the outcome of new experiments". 2011: "one can still make
  falsifiable predictions about model behavior without knowing the
  parameter values". The review grounds the claim ([THEORY-tmpd7a4j](../theory.d/THEORY-tmpd7a4j.md)
  replaces the unread LIT in its grounds); the 2010 and 2011 papers
  corroborate it. Consequence 3 matches the review's thesis, "simple
  theories of macroscopic behavior are hidden inside complicated
  microscopic processes".
- **The second clause of defeated_if** (a spread removed by
  reparametrization) is conceded by the sources for the eigenvalues ("the
  FIM can be transformed into any positive definite matrix by a simple
  linear transformation of parameters") and answered with the widths of
  the model manifold, which are invariant ([TERM-tmp5z2du](../terms.d/TERM-tmp5z2du.md)). The claim is
  safer read over widths than over eigenvalues.
- **Neural networks.** The originators did apply the hyper-ribbon to
  networks: the 2011 paper finds the geodesic widths of a 4-4-2 tanh
  network, weights as parameters, tracking its singular values (Fig. 6b);
  the 2015 review treats an autoencoder's code ("parameters θ_α giving the
  outputs of the digital neurons") as parameters and reports unpublished
  work showing "a clear hyperribbon structure". The 2011 paper's count
  makes finite singular points of the metric generic when the data number
  fewer than twice the parameters (M < 2N), which is the overparameterized
  regime. So "Not, yet, that it holds for neural networks" stands for
  overparameterized networks: the small network is regular where measured
  and the autoencoder's parameters are not its weights ([ARG-tmpv3nqz](../arguments.d/ARG-tmpv3nqz.md),
  Rejected as an inference to this claim for such networks).
