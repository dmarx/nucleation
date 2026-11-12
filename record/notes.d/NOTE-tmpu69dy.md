---
status: Read
paper: LIT-tmpc2x78
title: 'Montero-Porras, Smets and Lenaerts (2026) — Enshittification of Algorithmic Recommendation: An Evolutionary Model of Platform-Creator Dynamics'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 for the reading pass the owner asked for ("read the
    works you can reach"), from a reader's draft the filer verified against
    the downloaded text. Copy and extent: - Read: the published IOS Press
    PDF (10 pp.; PDF metadata "Creator: IOS Press", first page "This article
    is published online with Open Access by IOS Press and distributed under
    the terms of the Creative Commons Attribution Non-Commercial License 4.0
    (CC BY-NC 4.0)"), as deposited in the Université libre de Bruxelles
    repository (DI-fusion),
    https://dipot.ulb.ac.be/dspace/bitstream/2013/409778/3/FAIA-423-FAIA260512.pdf.
    The earlier reader did not record the address; the filer recovered it
    from OpenAlex's location list and confirmed it by refetching the file,
    whose SHA-256 matches the copy that was read. Quotes were checked
    against a pdftotext extraction. - Sections read: Abstract; 1
    Introduction; 2 Methods (2.1 payoffs, 2.2 replicator dynamics, 2.3
    equilibria); 3 Results (3.1 asymmetry, 3.2 shock and lock-in; Figures
    1-3 captions); 4 Conclusions and Future Directions. Figures themselves
    not inspected as images. Outcome as the reader gave it: **Read** in full
    (2026-11-12): all ten pages, pp. 268-277, references scanned.
date: '2026-11-12'
summary: >-
  A two-population evolutionary game between a platform (x = probability its
  recommender rewards costly quality content) and creators (y = probability
  a creator invests in quality), under replicator dynamics: ẋ =
  x(1−x)(Ry−A), ẏ = y(1−y)(Vx−C). With R > A and V > C there are two stable
  pure equilibria, (1,1) "virtuous" and (0,0) "vicious", separated by an
  interior saddle at (x*, y*) = (C/V, A/R). Calibrated at R=1, A=0.8, V=1,
  C=0.5, the saddle is (0.5, 0.8): creators need the platform to reward
  quality half the time, but the platform needs 80% of creators investing,
  so the platform is "the more fragile actor" and most of the state space
  collapses. A temporary rise in A (to 1.2) models a lure to extraction
  (more lucrative ads, less moderation): if it lasts long enough for x to
  fall below 0.5, restoring A=0.8 does not restore quality; the system goes
  to (0,0). The critical shock duration rises with the platform's health at
  onset (convex boundary), so early intervention buys more. Conclusions add
  that generative AI raises A (cheaper content, costlier moderation), that
  content velocity may be an observable fragility proxy, and that escaping
  (0,0) may need joint changes of platform policy and creator participation.
---
<!-- inactive-ok-file: THEORY-150 THEORY-470 — Proposed; cited as on the record -->
<!-- inactive-ok-file: LIT-1501 — Unavailable; cited as on the record -->

# NOTE-tmpu69dy: Montero-Porras, Smets and Lenaerts (2026) — Enshittification of Algorithmic Recommendation: An Evolutionary Model of Platform-Creator Dynamics

## Contribution

A minimal formal mechanism for platform decay with path dependence: a transient incentive shock
that pushes the state across a separatrix produces decay that the removal of the shock does not
undo. It is offered as a baseline, not a calibrated model.

## Key results

- p. 268 (Abstract): "The model yields two equilibria: a cooperative outcome with sustained
  high-quality content, and a defective outcome in which both parties prioritise short-term
  gains." And: "a temporary relaxation of quality standards may shift the system beyond a tipping
  point from which restoring the original policy no longer recovers the prior equilibrium".
- p. 269 (§2): "This formulation deliberately abstracts away user" behaviour and platform power
  asymmetries; "Both are treated as populations whose strategies evolve through imitation of more
  successful peers, captured by replicator dynamics".
- p. 270 (§2.1): "R and A are treated as exogenous parameters"; p. 271: "The true values for the
  parameters R, A, C and V remain latent".
- p. 271 (§2.3): "The model has two stable pure equilibria".
- p. 272 (§3.1): "creators need only 50% of platforms to reward quality before investing becomes
  rational", whereas the platform "requires 80% of creators to be producing high-quality content
  before quality" curation pays; "The platform is therefore the more fragile actor"; "the collapse
  region is considerably larger than the proliferation region, meaning most starting conditions
  lead to collapse".
- p. 273 (§3.2): in the long shock, "the system is now in the collapse region and deteriorates
  irreversibly, despite identical external con[ditions]"; "Creators are unaffected during the shock
  itself in both cases"; "A platform with x = 0.6 at shock onset has a critical duration of roughly
  T ∗ ≈ 8" (≈ 25 at x = 0.9); "these properties imply that early intervention is structurally"
  more effective (p. 274: "more effective than late intervention: the same improvement in x buys
  substantially more" tolerance).
- p. 275 (§4): "The model suggests that transient incentive shifts alone may be insu[fficient]";
  "recovery may require joint changes in both platform policy and creator participation"; "The
  assumptions of the model currently re[flect reasonable structural choices]" rather than
  measured parameters.

(Brackets mark where the PDF's "ﬁ"/"ﬂ" ligatures or a page break interrupt the quote; the filer
should quote up to the bracket.)

## Assumptions

Two populations only (no users; "a three-population extension ... is the most natural next step");
fixed exogenous rates R, A, V, C; platform's only choice is x; replicator (imitation) dynamics;
pairwise interaction; engagement and quality aligned only to the degree x captures; shock modelled
as a step change in A. No empirical calibration.

## Concepts

Evolutionary game theory; two-population replicator dynamics; saddle point and basins of
attraction; tipping boundary; structural asymmetry of thresholds (y* > x* whenever A > C at
V = R = 1); transient shock and irreversibility; critical shock duration T*; content velocity as a
fragility proxy.

## Bearing on the record

**On the LIT's and the exchange's characterization.** A's account ("an evolutionary game of platform and creators with two stable outcomes, quality and
extraction, and tipping points with hysteresis") is right in substance. Two refinements: the paper
does not use the word "hysteresis"; it says "tipping point" and "irreversibly". And "extraction" is A's gloss for the defective
equilibrium, which the paper calls the "vicious cycle". The curation entry's note that A35 called
the model "not independent proof of Doctorow's historical claims" is borne out: the paper models
one mechanism and calls the model intentionally minimal (Abstract: "The model is inten[tionally]
minimal", broken by a line-end hyphen in the PDF).

- **CLAIM-463** (restoring the conditions need not restore the capacity; a capacity lost past a
  threshold returns only under better conditions or by rebuilding the activity directly).
  **supports**, as an independent model instance: restoring A to its
  pre-shock value leaves the system collapsing to (0,0). The paper's conclusion that "recovery may require joint changes in both platform policy and creator participation" matches the claim's second route, rebuilding the activity directly; the paper says "may".
- **CASE-111** (fold in boundary maintenance; maintenance lost past the fold is not restored by
  returning the parameter). Found in recheck. A second formal instance of the same structure, in
  a two-population game, not a one-variable normal form. Unlike CASE-111, recovery slowing near the
  fold is not discussed.
- **THEORY-150** (Doctorow's three-stage decay; exit cost sets how far it goes; lowering it is the
  remedy). **Qualifies / leaves open**: the paper cites Doctorow as its frame and models one
  mechanism (recommender incentives and creator investment). It does not model users, lock-in or
  exit costs; it explicitly fixes R and A as exogenous while noting that real platforms set them
  "knowing that creators and users often face high switching costs". So it neither tests the
  three stages nor the exit-cost remedy. It adds what Doctorow lacks: a mechanism for decay that a
  temporary lure can make permanent.
- **THEORY-470** (decay caused by weakened constraints; "reversible if those constraints are
  durably restored"). **Qualifies the reversibility clause**: in the model, restoring the external
  condition (A back to 0.8) after a long enough lapse does not reverse decay. If the four
  constraints act by holding A down, the model says restoration is sufficient only before the
  tipping point, and early restoration buys disproportionately more. The paper does not model
  competition, regulation, interoperability or worker power.
- Other held entries found in recheck: **QUESTION-453** (evolutionary routes to cooperation)
  only loosely: this is cooperation as coordination between two populations with no relatedness
  or retaliation. **CLAIM-060** names enshittification; no bearing beyond the word.
- Duplicate check: no other LIT holds DOI 10.3233/faia260512 or the title (git grep on the branch).
  The record holds other replicator-dynamics and EGT works (LIT-1501, LIT-1511 etc.) but none on
  platforms.

## Limitations

Uncalibrated; parameters are "reasonable structural choices rather than measured parameters";
no users; the platform is a population, not a strategic monopolist; time units are arbitrary, so
T* values are illustrative. One slip in the text: §3.1 says that starting just below the boundary
"the system deteriorates regardless of initial conditions", which contradicts the basin picture it
describes. Figure 1 (Right) is described once as a trajectory and once as part of the left panel.
