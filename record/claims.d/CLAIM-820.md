---
number: 820
status: Proposed
formerly:
- CLAIM-tmpficzj
title: "A model's parameter complexity and its behavioural complexity come apart: when its predictions depend on a few stiff combinations of parameters and barely on the rest, it can be hard to fit and still predictive, so simplicity can belong to how a system responds to observation rather than to its mechanism"
version: 3
history:
- version: 2
  date: '2026-11-21'
  note: >-
    After the readings of LIT-2999 (NOTE-tmp1feoo) and LIT-2979
    (NOTE-tmphbnqd). The survey's reading, THEORY-tmpks8pd, replaces the
    unread LIT in the grounds (ARG-tmpddl7x); the reduction method's
    reading corroborates. The claim and its status are unchanged.
- version: 3
  date: '2026-11-22'
  note: >-
    After the reading of LIT-2958 (Quinn, Abbott, Transtrum, Machta &
    Sethna 2023, NOTE-tmp3keyy). Its reading, THEORY-tmpx26x7, replaces the
    unread LIT in the grounds (ARG-tmp6xwk9). Added, under "What it does
    not say": the review's qualification that sloppiness gives a
    low-dimensional description only relative to the precision demanded
    (ΛCDM). The sentence calling the survey and the 2023 review unread is
    corrected. The title and the status are unchanged.
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
- THEORY-tmpks8pd
- THEORY-2154
- THEORY-tmpx26x7
- LIT-1299
uses:
- TERM-135
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
<!-- inactive-ok-file: THEORY-tmpx26x7 ARG-tmp6xwk9 — Proposed or new; the 2023 review's reading and its argument, 2026-11-22 -->
<!-- inactive-ok-file: TERM-135 — filed with this claim from the same exchange, Proposed -->
<!-- inactive-ok-file: SYNTHESIS-075 — Proposed account, cited for the target-relativity this claim sits beside -->
<!-- inactive-ok-file: ARG-142 — new and Proposed or Rejected, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21 -->
<!-- inactive-ok-file: ARG-150 THEORY-2154 THEORY-2155 THEORY-2156 THEORY-tmpks8pd THEORY-tmpt1tw7 ARG-tmpddl7x — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->
<!-- inactive-ok-file: THEORY-tmpttfgp — Proposed; the reading of Shalizi and Moore, 2026-11-22 -->
<!-- inactive-ok-file: CLAIM-tmp3ima1 — Proposed; alternative (a), filed 2026-11-22 from the readings of Quinn and colleagues and of Shalizi and Moore -->

# CLAIM-820: A model's parameter complexity and its behavioural complexity come apart: when its predictions depend on a few stiff combinations of parameters and barely on the rest, it can be hard to fit and still predictive, so simplicity can belong to how a system responds to observation rather than to its mechanism

## The claim

A19 §1 draws the distinction: "**Parameter complexity:** How many
independent numbers are required to specify the microscopic model?
**Behavioral complexity:** How many independent quantities are needed to
describe its observable predictions? The first can be enormous while the
second is surprisingly small."

They come apart when the model is **sloppy**: its Fisher eigenvalues,
under the experiment in question, spread over many decades, so its
manifold of predictions is a hyperribbon ([TERM-135](../terms.d/TERM-135.md)). Three
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
([LIT-2999](../literature.d/LIT-2999.md)) and the reviews ([LIT-2994](../literature.d/LIT-2994.md), [LIT-2958](../literature.d/LIT-2958.md)). The 2015
review was read on 2026-11-21 and grounds the claim through
[THEORY-2154](../theory.d/THEORY-2154.md) (see the note below); the survey was read the same day
([THEORY-tmpks8pd](../theory.d/THEORY-tmpks8pd.md)) and the 2023 review on 2026-11-22 ([THEORY-tmpx26x7](../theory.d/THEORY-tmpx26x7.md)).
The claim stays interpretive and Proposed.

It sits beside [CLAIM-401](CLAIM-401.md) and [SYNTHESIS-075](../syntheses.d/SYNTHESIS-075.md): adequacy relative to a
declared target. Sloppiness is the parametric face of that relativity:
which directions are stiff depends on which observables are fitted.

## What it does not say

- **Not that sloppiness alone makes behaviour simple.** Behavioural
  complexity is counted against a precision. The 2023 review: "A sloppy
  model will have an effective low-dimensional description if many of its
  widths are small compared to the precision of the predictions demanded.
  This need not be the case"; the ΛCDM model of the cosmic microwave
  background "is sloppy ... because the experiments are so precise that
  all parameters are well determined from the data" ([LIT-2958](../literature.d/LIT-2958.md), §2;
  [THEORY-tmpx26x7](../theory.d/THEORY-tmpx26x7.md); [ARG-tmp6xwk9](../arguments.d/ARG-tmp6xwk9.md)). So the two complexities come apart
  relative to the observables fitted and to the precision demanded of
  them, not under sloppiness as such. Added 2026-11-22 (version 3).

- **Not that the sloppy directions do not matter.** They matter for
  other observables; the claim is relative to the experiment
  ([TERM-135](../terms.d/TERM-135.md), condition 1).
- **Not that a hierarchy of sensitivities indicates criticality** or a
  power law in event sizes (A19 §5; [TERM-135](../terms.d/TERM-135.md)).
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
  fails are [ARG-142](../arguments.d/ARG-142.md).

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
group" ([LIT-2994](../literature.d/LIT-2994.md), §V; note of 2026-11-21).

## Note of 2026-11-21: Transtrum, Machta & Sethna (2010, 2011) and Transtrum et al. (2015), read

Read in [NOTE-2240](../notes.d/NOTE-2240.md), [NOTE-2247](../notes.d/NOTE-2247.md) and [NOTE-2242](../notes.d/NOTE-2242.md) ([THEORY-2156](../theory.d/THEORY-2156.md),
[THEORY-2155](../theory.d/THEORY-2155.md), [THEORY-2154](../theory.d/THEORY-2154.md)).

- **Consequence 1 is theirs.** 2015, §I: "As long as the model predictions
  depend on the same stiff parameter combinations as the data, the
  predictions of the model will be constrained in spite of large numbers
  of poorly determined parameters." 2010: "although parameters cannot be
  reliably extracted by fitting degenerate models, it is still possible to
  constrain the outcome of new experiments". 2011: "one can still make
  falsifiable predictions about model behavior without knowing the
  parameter values". The review grounds the claim ([THEORY-2154](../theory.d/THEORY-2154.md)
  replaces the unread LIT in its grounds); the 2010 and 2011 papers
  corroborate it. Consequence 3 matches the review's thesis, "simple
  theories of macroscopic behavior are hidden inside complicated
  microscopic processes".
- **The second clause of defeated_if** (a spread removed by
  reparametrization) is conceded by the sources for the eigenvalues ("the
  FIM can be transformed into any positive definite matrix by a simple
  linear transformation of parameters") and answered with the widths of
  the model manifold, which are invariant ([TERM-135](../terms.d/TERM-135.md)). The claim is
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
  and the autoencoder's parameters are not its weights ([ARG-150](../arguments.d/ARG-150.md),
  Rejected as an inference to this claim for such networks).

## Note of 2026-11-21: Gutenkunst et al. (2007) and Transtrum & Qiu (2014), read

- **The survey supports the claim for systems-biology models, in one
  model for predictions** ([NOTE-tmp1feoo](../notes.d/NOTE-tmp1feoo.md), [THEORY-tmpks8pd](../theory.d/THEORY-tmpks8pd.md); [ARG-tmpddl7x](../arguments.d/ARG-tmpddl7x.md)).
  Across seventeen models the spectra "span many decades" with "no
  well-defined cutoff", and an idealized fit "leaves many parameters with
  greater than 100% uncertainty" in most. In the PC12 model, after a fit in
  which "Not a single parameter was constrained to better than a factor of
  50", a prediction is tight, while matching it by measurement needs "all
  24 involved parameters" to ±25%. The abstract generalizes ("modelers
  should focus on predictions rather than on parameters"); tight
  predictions are tested in one model only.
- **Relative to the observables fitted**, in the paper's words:
  "exhaustive experiments designed to decouple the system and separately
  measure each parameter will naturally not yield sloppy parameter
  sensitivities."
- **The second clause of defeated_if.** The survey answers it otherwise
  than the later papers: the bare parametrization is "fundamental to the
  system, not an artifact of the modeling process", and the PC12 model
  with every rate and concentration set to 1 "remains sloppy". That tells
  against an artefact of scales, not against reparametrization in
  general, which the widths answer (the note above).
- **Transtrum and Qiu corroborate** ([NOTE-tmphbnqd](../notes.d/NOTE-tmphbnqd.md), [THEORY-tmpt1tw7](../theory.d/THEORY-tmpt1tw7.md)), in
  the claim's own terms: "such models have more complexity in their
  description than in their predictions" (para. 6), and the EGFR model's
  48 parameters reduce to 12 with nearly the same predictions.

## Note of 2026-11-22: Quinn, Abbott, Transtrum, Machta & Sethna (2023), read

Read in [NOTE-tmp3keyy](../notes.d/NOTE-tmp3keyy.md) ([THEORY-tmpx26x7](../theory.d/THEORY-tmpx26x7.md)). **Supports the claim, with one
qualification** ([ARG-tmp6xwk9](../arguments.d/ARG-tmp6xwk9.md)); the reading replaces [LIT-2958](../literature.d/LIT-2958.md) in the
grounds.

- **Consequence 1:** "predictions are independent of all but a few
  parameter combinations, which is unfortunate if you want to deduce the
  parameters from collective behavior, but fortunate if you want to test
  the predictions of the model before the parameters are fully measured"
  (§8).
- **Consequence 3 and the relativity to observables**, nearly in the
  claim's words: "sloppiness is a property both of the scientific model
  and the predictions of interest. The Ising model is not sloppy ...
  unless one only cares about long length and time scales" (§8.2).
- **Qualification:** low behavioural dimension needs widths small against
  the precision demanded; ΛCDM is sloppy and fully determined (§2). Made
  in place under "What it does not say" (version 3).
- **The second clause of defeated_if** is answered again by the widths,
  which are coordinate-free (§2), and by the rates-set-to-one test, "The
  cost Hessian remains sloppy" (§3).
- **Why it happens: no single account.** The review's explanations for
  physics (coarse-graining) and for least squares (smoothness) "seem
  completely different" (§8.2); the claim says that the complexities come
  apart, not why, and is unaffected.
- **Neural networks:** "We have speculated about the relationship between
  sloppiness and large machine learning models" (§8). Consistent with
  "Not, yet, that it holds for neural networks".
- **A point the claim does not make:** new parameters "can therefore be
  added without harming model predictions", and a reduced model may be
  preferred "but not because the fuller model will overfit" (§1). Noted,
  not adopted.

## Note of 2026-11-22: Shalizi and Moore, read

**A parallel, in information terms**, no edge (LIT-2996, NOTE-tmpunt6q,
THEORY-tmpttfgp). Argon's microstate has Cµ = 6.6·10²⁰ bits against a
33.3-bit macrostate that is predicted more efficiently (0.87 against
0.5, §IV.A), and "Nature has no preferred questions" (§VI). That supports
clause 3, simplicity as a response to observation, by another mechanism:
coarse-graining of states rather than stiff combinations of parameters.
No bearing on clause 1 (fitting). CLAIM-tmp3ima1 (alternative a, Proposed)
widens this claim's relativity to coarse-graining and emergence. Status
unchanged.
