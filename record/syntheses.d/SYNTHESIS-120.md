---
number: 120
status: Proposed
formerly:
- SYNTHESIS-tmpsejrp
title: "In the record, how a high-dimensional representation comes to draw a new distinction is held in parts: concentration of measure sets a null that learning has to beat; geometric separation, decodability and spectral detectability are distinct, and cone occupancy, the BBP threshold and an alignment bifurcation are three thresholds on one scale; coupled embeddings under gradient flow relax rather than act; a factored feature switches on at a threshold quiet but consequential, a parent can gate it, and sample PCA sees it only after a window; entailment and refinement are partial orders; sloppiness and singular strata meet in two places and part in one; and whether stages of learning are transitions among singular strata ordered as the semantic refinements stays open"
version: 1
defeated_if: >-
  A component misstated or misattributed here, with its scope conditions;
  an in-force entry of the learned-structure line on how a learned
  representation comes to draw a distinction (its geometry in high
  dimension, its thresholds, its singular geometry and its orders) left
  out without a reason given; or a link this account states that no
  component states. Its standing is its components': a component retired
  takes its clause with it.
tags:
- representation-learning
- learning-theory
- information-geometry
date: '2026-11-21'
line:
- learned-structure
integrates:
- TERM-138
- CLAIM-802
- CLAIM-823
- ARG-132
- CLAIM-833
- ARG-126
- ARG-137
- ARG-130
- ARG-142
- QUESTION-515
- CLAIM-798
- CLAIM-818
- CLAIM-842
- THEORY-1085
- CLAIM-822
- CLAIM-797
- CLAIM-847
- CLAIM-848
- TERM-136
- CLAIM-838
- CLAIM-799
- CASE-301
- CLAIM-827
- CLAIM-804
- QUESTION-512
- QUESTION-217
- CLAIM-839
- CLAIM-800
- CLAIM-816
- ARG-153
- CLAIM-834
- QUESTION-363
- THEORY-087
- QUESTION-510
- CLAIM-808
- TERM-135
- CLAIM-813
- CLAIM-812
- CASE-302
- ARG-138
- CLAIM-811
- CLAIM-843
- CLAIM-844
- QUESTION-511
- CLAIM-835
- TERM-137
- ARG-139
- CLAIM-807
- CLAIM-828
- CLAIM-837
- QUESTION-514
bears_on:
- QUESTION-515
- QUESTION-512
- QUESTION-217
- QUESTION-363
- QUESTION-511
- QUESTION-514
- QUESTION-510
---
<!-- inactive-ok-file: LIT-2985 LIT-tmpu2kk5 LIT-tmp309tx THEORY-tmp1nvjs THEORY-tmpqma2p THEORY-tmpdfeto ARG-tmpx5evn — Unavailable, Deferred, Proposed or new; the Mermin–Wagner neighbours and their argument, 2026-11-22 -->
<!-- inactive-ok-file: ARG-tmpbad4y THEORY-tmpwtoad — Proposed, Deferred or new; the readings of 2026-11-22 and the entries they bear on -->
<!-- inactive-ok-file: TERM-138 — Proposed; filed 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-802 CLAIM-823 ARG-132 CLAIM-833 ARG-126 ARG-137 ARG-130 ARG-142 — Proposed or Rejected; filed 2026-11-21 after the coverage check -->
<!-- inactive-ok-file: CLAIM-798 CLAIM-818 CLAIM-842 CLAIM-822 CLAIM-797 CLAIM-847 CLAIM-848 TERM-136 CLAIM-838 CLAIM-799 CASE-301 CLAIM-827 CLAIM-804 CLAIM-839 CLAIM-800 CLAIM-816 ARG-153 CLAIM-834 CLAIM-808 TERM-135 CLAIM-813 CLAIM-812 CASE-302 ARG-138 CLAIM-811 CLAIM-843 CLAIM-844 CLAIM-835 TERM-137 ARG-139 CLAIM-807 CLAIM-828 CLAIM-837 — new and Proposed or Open; components filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21 -->
<!-- inactive-ok-file: SYNTHESIS-034 SYNTHESIS-030 SYNTHESIS-029 — Proposed or new; accounts this one sits beside -->
<!-- inactive-ok-file: THEORY-tmpwn1xp — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->

# SYNTHESIS-120: In the record, how a high-dimensional representation comes to draw a new distinction is held in parts: concentration of measure sets a null that learning has to beat; geometric separation, decodability and spectral detectability are distinct, and cone occupancy, the BBP threshold and an alignment bifurcation are three thresholds on one scale; coupled embeddings under gradient flow relax rather than act; a factored feature switches on at a threshold quiet but consequential, a parent can gate it, and sample PCA sees it only after a window; entailment and refinement are partial orders; sloppiness and singular strata meet in two places and part in one; and whether stages of learning are transitions among singular strata ordered as the semantic refinements stays open

*A part account of the learned-structure line, filed from the synthesis audit of the exchange "Rich Get Richer Power Laws" (2026-11-21; [ADR-075](../decisions.d/ADR-075.md) step 5, [ADR-131](../decisions.d/ADR-131.md)). It maps A's syntheses at A29 §12, A30 §10, A32 §8 and its close, A33 §9–10, A35 §9 and its close, A37 §6 and §11, A39 §8–9 and its close, A41 §8, A42's close and A43 §17 onto the entries filed from that exchange. The thesis those syntheses build was built from the owner's turns: U18 (active matter), U19 (concentration of measure), U21 (entailment cones), U23 (singularity theory), U24 (Watanabe's stratification and the hyperribbon) and U25 (informative small-eigenvalue subspaces). Each component below says whose it is.*

*Its scope is a part of [SYNTHESIS-034](SYNTHESIS-034.md)'s, which asks what sets when a network acquires a structure and holds only questions. Two of [SYNTHESIS-034](SYNTHESIS-034.md)'s components, [QUESTION-363](../questions.d/QUESTION-363.md) and [QUESTION-217](../questions.d/QUESTION-217.md) (the latter through [SYNTHESIS-029](SYNTHESIS-029.md)), are integrated here again. This scope is wider in one way: the geometry of the representation in high dimension, and singular geometry. It holds claims. So it is filed as a part, for [SYNTHESIS-034](SYNTHESIS-034.md)'s next version or the line's account, [SYNTHESIS-030](SYNTHESIS-030.md), to integrate, rather than as a revision of either. It adds nothing; its standing is its components'.*

## The account

### Active matter, and what it reduces to (U18)

- **The question.** [QUESTION-515](../questions.d/QUESTION-515.md) (the owner's, U18, Open) asks whether a deep network's representational manifold can be modelled as an active-matter system in high dimension, and in which sense.
- **Weak and strong readings.** [CLAIM-798](../claims.d/CLAIM-798.md) (A's, A29, interpretive, Proposed) separates a weak analogy, collective motion through a shared-parameter kernel, from a strong model with sustained nonequilibrium currents. The weak one follows from gradient flow; the strong one has to be shown.
- **Gradient flow relaxes.** [CLAIM-818](../claims.d/CLAIM-818.md) (the assistant's, demonstrated, Proposed): under gradient flow, coupled embeddings relax however the kernel changes, so activity has to come from the optimizer, mismatched noise or a changing objective.
- **When order survives.** [CLAIM-842](../claims.d/CLAIM-842.md) (A's, A29 §6, supposed, demonstrated, Proposed): under a local Gaussian elastic energy, long-wavelength fluctuations diverge for spectral dimension d_s ≤ 2. [THEORY-1085](../theory.d/THEORY-1085.md) (Active, Toner and Tu) is the flocking reading A draws on.

### The geometric null (U19)

- **The owner's point.** [CLAIM-822](../claims.d/CLAIM-822.md) (the owner's, U19, interpretive, Proposed): concentration of measure, as on a Gaussian annulus, is an important consideration in the active-matter model.
- **What it makes a null.** [CLAIM-797](../claims.d/CLAIM-797.md) (A's, A29–A30, demonstrated, Proposed): a thin shell, nearly orthogonal directions and nearly equal distances arise with no interaction, so they are a baseline and not evidence of learned order.
- **Effective dimension sets it.** [CLAIM-847](../claims.d/CLAIM-847.md) (A's, A30 §5, demonstrated, Proposed): concentration is set by the participation ratio, not ambient dimension. [CLAIM-848](../claims.d/CLAIM-848.md) (the assistant's, demonstrated, Proposed, resting on [CLAIM-847](../claims.d/CLAIM-847.md)): at realistic widths the participation ratio does not track intrinsic dimension. [TERM-136](../terms.d/TERM-136.md) (A's, Proposed) separates ambient, intrinsic, effective and spectral dimension.
- **Three scales of bias.** [CLAIM-838](../claims.d/CLAIM-838.md) (A's, A30–A35, demonstrated, Proposed): a directional bias acts at order one, at order √D and at order D, so discrimination changes long before visible clustering.

### Thresholds of a distinction

- **Three qualities.** [CLAIM-799](../claims.d/CLAIM-799.md) (A's, A31–A32, demonstrated, Proposed): geometric separation, decodability and spectral detectability are distinct. The BBP threshold √(D/N) marks when the estimator can see a signal, "not when the network acquired it". [CASE-301](../cases.d/CASE-301.md) (A32 §4, checked) is the construction.
- **Three thresholds, one scale.** [CLAIM-827](../claims.d/CLAIM-827.md) (the assistant's, demonstrated, Proposed, resting on [CLAIM-838](../claims.d/CLAIM-838.md) and [CLAIM-799](../claims.d/CLAIM-799.md)): cone occupancy (κ ∼ √D), BBP (κ = √D·(D/N)^(1/4)) and the alignment bifurcation (coupling ∼ D). Only the last is a transition of the system, and its ordering mode is BBP-visible before it.
- **A cascade of detectability.** [CLAIM-804](../claims.d/CLAIM-804.md) (A's, A32, supposed, demonstrated, Proposed): if signal strengths fall as a power law in rank, PCA separates a growing number of directions, a cascade of detectability thresholds and not a self-organized critical process.
- **The test.** [LEAD-210](../leads.d/LEAD-210.md) (A's programme, gathered; Open). Its sharpest test is A32's: does a supervised probe become informative before PCA separates an eigenvalue?

### Orders (U21)

- **The owner's question.** [QUESTION-512](../questions.d/QUESTION-512.md) (the owner's, U21, Open): can entailment cones help reason about progressive learning dynamics? It refines [QUESTION-217](../questions.d/QUESTION-217.md) (Open), the coarse-to-fine question on the orders of refinement, relevance and acquisition.
- **Two partial orders.** [CLAIM-839](../claims.d/CLAIM-839.md) (A's, A33 and A35, interpretive, Proposed, resting on [CLAIM-199](../claims.d/CLAIM-199.md)): semantic entailment and Blackwell refinement, neither of which need be a chain. A narrower region counts as progress only while it stays correct. [ARG-153](../arguments.d/ARG-153.md) (Proposed) carries A33's spherical-cap null to the cost of restricting hyperbolic cones.
- **Cone occupancy measures nothing alone.** [CLAIM-800](../claims.d/CLAIM-800.md) (A's, A35, demonstrated, Proposed): occupancy rises when boundaries move and under collapse, and nesting makes a coarse cone entered first by construction. Coarse-to-fine learning needs an independent measure of decodability.
- **Depth in high dimension.** [CLAIM-816](../claims.d/CLAIM-816.md) (A's, A33 and A35, interpretive, Proposed): dimension narrows the radial range hyperbolic embeddings use for depth, twice.

### Singular geometry (U23, U24)

- **The owner's suggestion.** [CLAIM-834](../claims.d/CLAIM-834.md) (the owner's, U23, Proposed): singularity theory's account of phase transitions in learning as resolutions of singularities may be useful here. It admits two readings, filed as alternatives: [CLAIM-802](../claims.d/CLAIM-802.md) (reading (a), stated by the assistant, Proposed), that training itself performs a resolution, against which [CLAIM-305](../claims.d/CLAIM-305.md) tells ([ARG-132](../arguments.d/ARG-132.md), the assistant's, Proposed); and [CLAIM-823](../claims.d/CLAIM-823.md) (reading (b), A's, A37, Proposed), that a transition is a change in which singularity dominates, with resolution as the tool for computing it. [QUESTION-363](../questions.d/QUESTION-363.md) (Open; its note of 2026-11-21 records A37 §5's three transitions, Bayesian, dynamical and representational) asks when the order SGD meets organizations follows the posterior's order. [THEORY-087](../theory.d/THEORY-087.md) (Active) holds the regular and singular complexity penalties. [QUESTION-510](../questions.d/QUESTION-510.md) (A's, A37 §9, Open) asks what replaces SLT's fixed-dimension asymptotics when width grows with the data.
- **The owner's bet.** [CLAIM-808](../claims.d/CLAIM-808.md) (the owner's, U24, interpretive, Proposed): Watanabe's stratification connects to the hyperribbon account ([TERM-135](../terms.d/TERM-135.md), A's, A19 §4).
  - [CLAIM-813](../claims.d/CLAIM-813.md) (A's, A39, demonstrated, Proposed): sloppiness and singularity are different properties.
  - [CLAIM-812](../claims.d/CLAIM-812.md) (the assistant's, demonstrated, Proposed): they meet in two places, a sloppy eigenvalue as squared distance to a stratum and an unresolved sloppy direction counting like a flat one, and part in how the coefficient moves with sample size.
  - [CASE-302](../cases.d/CASE-302.md) (A39 §§2–4, checked, with the assistant's additions) is the merging-mechanisms construction.
  - [ARG-138](../arguments.d/ARG-138.md) (Proposed) holds that these support the owner's bet at the hyperribbon's fold edges and in the finite-sample coefficient, not yet in its widths.
- **Slow relaxation without criticality.**
  - [CLAIM-811](../claims.d/CLAIM-811.md) (A's, A39 §5 and A42 §6, demonstrated, Proposed): flow into a degenerate minimum relaxes algebraically, at a rate the learning coefficient does not fix, and only on a balanced approach.
  - [CLAIM-843](../claims.d/CLAIM-843.md) (the assistant's, demonstrated, Proposed): a population of factored modes relaxes on average as a power law with a logarithmic correction, though almost every mode relaxes exponentially.
  - [CLAIM-844](../claims.d/CLAIM-844.md) (A's, A39 and A43, interpretive, Proposed) offers this as an alternative to reading training's slow modes as criticality.

### Small directions and the birth of a feature (U25)

- **Which spectrum is weak.** [QUESTION-511](../questions.d/QUESTION-511.md) (U25 quoting A39 §8, Open) asks whether a weak direction becomes informative before a degeneracy changes and before the distinction is decodable, and in which spectrum.
  - [CLAIM-835](../claims.d/CLAIM-835.md) (A's, A41, demonstrated, Proposed): smallness depends on the metric, and metrics can rank directions in opposite orders.
  - [TERM-137](../terms.d/TERM-137.md) (A's table, assembled by the assistant; Proposed): six senses of "weak direction".
  - [ARG-139](../arguments.d/ARG-139.md) (Proposed) holds that the recent findings support [CLAIM-835](../claims.d/CLAIM-835.md) but do not show the hyperribbon account mistook widths for importance.
- **A feature's threshold.** [CLAIM-807](../claims.d/CLAIM-807.md) (A's, A42, demonstrated, Proposed): a factored feature switches on at s = λ. There the parameters pitchfork, relaxation is algebraic and the local coefficient dips from 1 to 3/4. Just above, the feature is quiet (variance ε²) but consequential (gain ε). The pitchfork is in the parameters; the predictor kinks.
- **Gated by a parent.** [CLAIM-828](../claims.d/CLAIM-828.md) (A's, A43, demonstrated, Proposed): with a parent gate the child switches on when gs > λ, so acquisition follows a partial order of dependencies. The times of encoding, stability and expression can differ.
- **Seen only after a window.** [CLAIM-837](../claims.d/CLAIM-837.md) (the assistant's, from this audit, demonstrated, Proposed): onset and the singular point coincide at s = λ. Sample PCA detects the feature only once s − λ exceeds σ²√(D/N) in the hidden layer, or (s − λ)² does in its contribution to the output.
- **The test.** [LEAD-207](../leads.d/LEAD-207.md) (A's design across A37–A43, with the assistant's addition; Open): date decodability, the stability eigenvalue, held-out gain and the local coefficient for each distinction of a synthetic hierarchy.

### The correspondence, open

[QUESTION-514](../questions.d/QUESTION-514.md) (A's, A37 §6, A39 §§7–8 and A43 §14, Open) holds the thesis the syntheses converge on, as a question. Does the incidence order of the singular strata map onto the order in which representations refine one another, and how far from one-to-one is the map?

### Components filed after the coverage check

- [TERM-138](../terms.d/TERM-138.md) (the assistant's, Proposed): "separation" in three senses, of scales or levels, of classes, and spectral. In this part, senses 2 and 3 are decodability and spectral detectability.
- [CLAIM-833](../claims.d/CLAIM-833.md) (A's, A39 §6, supposed, Proposed): model reduction moves toward the model manifold's boundaries and feature differentiation away from singular strata, so learning and compression may be opposite movements through one stratified space. A calls it "not an established general law"; [ARG-138](../arguments.d/ARG-138.md) notes that such boundaries often lie at infinite parameter values.
- [ARG-126](../arguments.d/ARG-126.md) (the assistant's, Proposed): [CLAIM-818](../claims.d/CLAIM-818.md) closes A29's feedback loop as a route to activity, for [CLAIM-798](../claims.d/CLAIM-798.md).
- [ARG-137](../arguments.d/ARG-137.md) (the assistant's, Proposed): [CLAIM-843](../claims.d/CLAIM-843.md) narrows [CLAIM-844](../claims.d/CLAIM-844.md); a power law in training relaxation does not indicate a hierarchy of singular orders.
- [ARG-130](../arguments.d/ARG-130.md) (the assistant's, Proposed): [CLAIM-848](../claims.d/CLAIM-848.md) qualifies [CLAIM-847](../claims.d/CLAIM-847.md); A30's participation-ratio regimes separate only at very large widths.
- [ARG-142](../arguments.d/ARG-142.md) (A's argument, Rejected by the assistant): A19 §10's analogy from sloppy models to networks fails, since sloppiness assumes a regular Fisher matrix.

## Links the components state, and where

- [CLAIM-827](../claims.d/CLAIM-827.md) rests on [CLAIM-838](../claims.d/CLAIM-838.md) and [CLAIM-799](../claims.d/CLAIM-799.md). [CLAIM-804](../claims.d/CLAIM-804.md) rests on [CLAIM-799](../claims.d/CLAIM-799.md). [CLAIM-848](../claims.d/CLAIM-848.md) rests on [CLAIM-847](../claims.d/CLAIM-847.md).
- [CLAIM-812](../claims.d/CLAIM-812.md) rests on [CLAIM-813](../claims.d/CLAIM-813.md). [ARG-138](../arguments.d/ARG-138.md) concludes on [CLAIM-808](../claims.d/CLAIM-808.md).
- [CLAIM-807](../claims.d/CLAIM-807.md) rests on [CLAIM-811](../claims.d/CLAIM-811.md) (and [CLAIM-148](../claims.d/CLAIM-148.md), outside this part). [CLAIM-828](../claims.d/CLAIM-828.md) rests on [CLAIM-807](../claims.d/CLAIM-807.md). [CLAIM-843](../claims.d/CLAIM-843.md) and [CLAIM-844](../claims.d/CLAIM-844.md) rest on [CLAIM-811](../claims.d/CLAIM-811.md).
- [CLAIM-837](../claims.d/CLAIM-837.md) rests on [CLAIM-807](../claims.d/CLAIM-807.md) and [CLAIM-799](../claims.d/CLAIM-799.md), and bears on [QUESTION-511](../questions.d/QUESTION-511.md).
- [QUESTION-511](../questions.d/QUESTION-511.md) names [CLAIM-807](../claims.d/CLAIM-807.md), [CLAIM-828](../claims.d/CLAIM-828.md) and [CLAIM-812](../claims.d/CLAIM-812.md) as candidate answers, and [LEAD-207](../leads.d/LEAD-207.md) as its test.
- [CLAIM-800](../claims.d/CLAIM-800.md) is the reason [QUESTION-512](../questions.d/QUESTION-512.md)'s cones need an independent measure of decodability, the quality [CLAIM-799](../claims.d/CLAIM-799.md) separates.
- [CLAIM-818](../claims.d/CLAIM-818.md) answers [CLAIM-798](../claims.d/CLAIM-798.md)'s weak reading: gradient flow alone is not active.

## Not stated on the record

Integrating sentences of A's syntheses that no entry states, tested at the audit and not filed as claims:

- **"The stages of hierarchical representation learning correspond to transitions among functionally distinct strata of a singular neural-network model, while entailment geometry supplies the semantic ordering of those strata and high-dimensional concentration determines their observational detectability"** (A37 §11; restated at A39's close and A42's close). It is held only as [QUESTION-514](../questions.d/QUESTION-514.md) and tested by [LEAD-207](../leads.d/LEAD-207.md). A's own later turns withdraw the identification: A41 §8 allows onset "potentially preceding ... an identifiable transition in local singularity structure", and A43 §14 says the relation "is not automatically one-to-one". In the record's one worked model, the stages on either side of the threshold have the same local coefficient, and only the threshold point is singular ([CLAIM-807](../claims.d/CLAIM-807.md)).
- **"Higher-order singular directions can produce algebraic learning dynamics, while hierarchies of such directions may generate broad distributions of learning timescales"**, offered as "an unexpectedly precise connection back to power laws" (A39's close). The first half is [CLAIM-811](../claims.d/CLAIM-811.md), but only on a balanced approach. The second half is held only as [CLAIM-844](../claims.d/CLAIM-844.md)'s alternative, and [CLAIM-843](../claims.d/CLAIM-843.md) gets the power law from a spread of exponential rates with no singular direction needed. As a precise connection it is not stated.
- **"A critical regime might occur when the learned interactions become strong enough to overcome high-dimensional entropic dispersion"** (A30 §10). [CLAIM-827](../claims.d/CLAIM-827.md) places the alignment bifurcation at coupling of order D in a mean-field model. That the training of a network reaches such a regime is not stated, and [CLAIM-818](../claims.d/CLAIM-818.md) holds that gradient flow alone relaxes.
- **"Progressive learning is the dynamical construction of an increasingly informative partial order over semantic possibilities"** (A35's close). It is [CLAIM-839](../claims.d/CLAIM-839.md)'s sentence, so it is stated there. What A35's version adds, that concentration "governs the statistical thresholds at which those distinctions become detectable", is [CLAIM-827](../claims.d/CLAIM-827.md)'s for detectability. It is not stated for acquisition: [CLAIM-799](../claims.d/CLAIM-799.md) holds that detectability is not acquisition.
- **"We originally treated the hyperribbon hierarchy as a hierarchy of importance"** (A41 §8). [ARG-139](../arguments.d/ARG-139.md) holds that the findings do not show this. A hyperribbon is already measured in the metric of the predictions.

## What it does not say

- That any trained network has been shown to pass these thresholds in any order. The components are toy models, constructions and proposed studies. [LEAD-210](../leads.d/LEAD-210.md) and [LEAD-207](../leads.d/LEAD-207.md) have not been run.
- Which of the owner's suggestions the record adopts. Each is Proposed or Open.
- Anything with standing of its own.

## Note of 2026-11-22: Stringer and colleagues, read

Stringer and colleagues ([LIT-2972](../literature.d/LIT-2972.md), [NOTE-tmp923nm](../notes.d/NOTE-tmp923nm.md), [THEORY-tmpwtoad](../theory.d/THEORY-tmpwtoad.md)):
**background.** The measured spectrum (exponent 1.04 over ranks 11 to 500)
and the smoothness bound behind [CLAIM-848](../claims.d/CLAIM-848.md)'s participation-ratio table are
now read; the bound is strict and on the tail only, and [CLAIM-848](../claims.d/CLAIM-848.md) and
[ARG-130](../arguments.d/ARG-130.md) are corrected in place ([ARG-tmpbad4y](../arguments.d/ARG-tmpbad4y.md)). The synthesis's use of the
participation ratio is unaffected.

## Note of 2026-11-22: Ansuini and colleagues, read

Ansuini, Laio, Macke and Zoccolan ([LIT-2998](../literature.d/LIT-2998.md), [NOTE-tmptf55k](../notes.d/NOTE-tmptf55k.md), [THEORY-tmpwn1xp](../theory.d/THEORY-tmpwn1xp.md)): **qualifies
how "dimension" is read in this account.** In trained CNNs the
intrinsic dimension of the representations (TwoNN, far below width) and a
linear count of their variance (one to two orders larger) diverge, because
the manifolds are curved; [CLAIM-848](../claims.d/CLAIM-848.md) has the participation ratio failing to
track intrinsic dimension from the other side. Where a component here leans
on low or effective dimension, it should say which of [TERM-136](../terms.d/TERM-136.md)'s senses it
means. No component changes.

## Note of 2026-11-22: the Mermin–Wagner neighbours, read

The "When order survives" bullet maps [CLAIM-842](../claims.d/CLAIM-842.md) as A's supposition. Read
through three neighbours of Mermin and Wagner ([LIT-2985](../literature.d/LIT-2985.md), Unavailable),
the supposition's mathematics is held in the literature as Cassi's
theorem (1992, [LIT-tmpu2kk5](../literature.d/LIT-tmpu2kk5.md), after Hattori, Hattori and Watanabe 1987,
[LIT-tmp309tx](../literature.d/LIT-tmp309tx.md), both registered and unread, known through Gelfert and
Nolting, [THEORY-tmp1nvjs](../theory.d/THEORY-tmp1nvjs.md)) for spin models with a continuous symmetry in
equilibrium; its limits are Halperin's ([THEORY-tmpqma2p](../theory.d/THEORY-tmpqma2p.md)), and Toner and
Tu's flock ([THEORY-tmpdfeto](../theory.d/THEORY-tmpdfeto.md)) is a case where breaking equilibrium removes
the divergence. [CLAIM-842](../claims.d/CLAIM-842.md) now says so (version 2; [ARG-tmpx5evn](../arguments.d/ARG-tmpx5evn.md)). The
bullet still maps the claim faithfully; when the account is next
revised it should say that the criterion is a theorem elsewhere and a
supposition here. No status change.
