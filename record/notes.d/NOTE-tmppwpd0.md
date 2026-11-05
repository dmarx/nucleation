---
status: Read
paper: 'LIT-tmpbkl3k'
title: 'Majikes et al. — Complex cooperativity in DNA origami revealed via design-dependent defectivity'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read on 2026-11-05 from the PubMed Central copy of the version of
    record, https://pmc.ncbi.nlm.nih.gov/articles/PMC12907558/ (HTML; "This
    work is written by (a) US Government employee(s) and is in the public
    domain in the US"), found through Europe PMC (PMID 41693566) and
    converted to text; Europe PMC's full-text XML endpoint returned an
    error once and was not retried. Eq. 1 is an image on PMC and was read
    from the NCBI copy of it. Read in full: abstract, Introduction,
    Materials and methods, Results, Discussion, all figure captions, Eq. 1
    and the data statement; the reference list scanned. Not read: the
    figure images (no values read off plots beyond the text's), and the
    supplementary PDF (sections 1-14: per-design tables, the >30 metric
    variants, the LASSO, the control anneals, melt curves), whose PMC
    download met a proof-of-work challenge and was not retried.
date: '2026-11-05'
summary: >-
  34 designs of one 2D origami rectangle, annealed fast at 0.375 nM with
  5x staples so defects are common, imaged by liquid AFM and classed into
  four classes, give a defectivity φ of about 10 to 35, with staple-pool
  variation (±2.8) the largest uncertainty. Defectivity tracks the skew of
  the first-fold loop-entropy penalty distribution and the measured melt
  temperature; with a blocking metric, roughly equal weights collapse it
  onto one trend over 28 designs. Designs with more short folds at the
  expense of medium ones did worse. The authors read 2D origami assembly as
  funnel-like rather than path-like.
---
<!-- inactive-ok-file: THEORY-tmpcfriw THEORY-1398 CLAIM-567 CLAIM-583 CLAIM-571 CLAIM-581 CLAIM-591 CLAIM-569 CLAIM-566 CLAIM-557 CLAIM-574 CLAIM-570 CLAIM-592 CLAIM-572 CLAIM-184 CLAIM-185 CLAIM-478 CASE-tmpu0s44 LIT-tmpg98v0 — Proposed, Unavailable or new; cited from the reading of Majikes et al. (2026) as open -->

# NOTE-tmppwpd0: Majikes et al. — Complex cooperativity in DNA origami revealed via design-dependent defectivity

## Contribution

A comparative experiment of unusual breadth: 34 designs of one fixed 2D
geometry, assembled under one protocol and scored with quantified
uncertainty. The literature's named mechanisms of cooperativity are turned
into metrics computable from a caDNAno design and tested against
defectivity, giving a first empirical heuristic from design to quality.

## Key insight

Across designs of one 2D shape, aggregate properties of the whole design,
above all the distribution of loop-entropy penalties each fold would pay
if it bound first, predict how defective the product is, without tracing
any pathway. A smooth hierarchy from short through medium to long folds is
better than many short folds, which leave the long folds few routes.

## Assumptions

- **Poor anneals stand for typical ones.** "This approach is valid,
  provided the mechanisms of defect formation are the same under poor
  annealing conditions as they are under typical ones"; the check is in a
  supplementary section not read. Conditions: 0.375 nM scaffold, 5x
  staples, 80 °C to 4 °C in 45 min.
- **Defectivity from classes (Eq. 1).** φ = (1 n_well-folded + 5
  n_damaged + 15 n_ripped + 50 n_catastrophic) / n_total, the
  coefficients estimating the least number of defective staples for each
  level of visible damage; classes assigned by human analysts from liquid
  AFM.
- **Metrics from first-fold, single-step, nearest-neighbour energetics**,
  each ignoring the other staples.
- **Linear combinations only**, to limit what the authors call accidental
  p-hacking.
- **One shape**, of "nearly identical aspect ratio" across designs except
  one notched rectangle; one scaffold (M13mp18); one buffer.

## Key results

- **Four mechanisms (Fig. 1 caption)**, presented as "the primary forms of
  cooperativity in DNA origami discussed in the literature": positive
  inter-domain (a bound domain raises its neighbours' local
  concentration, reduced by loop entropy at long distance); inter-fold,
  where "the closing of one fold reduces the possible conformations
  available to the entire remaining scaffold"; "Negative inter-domain
  cooperativity, or blocking" (a second staple copy outcompetes the second
  domain at long scaffold distance); and "Base stacking cooperativity".
- **The inter-fold metric (Methods)**: "the skew of the loop entropy
  penalty distribution for each fold, assuming it was first to bind".
- **What skew means (Results).** "A large negative skew is indicative of
  many nucleation points, but a limited number of pathways leading to the
  geometrically necessary long folds." Design #1 (a hierarchy of fold
  lengths) has skew 1.0; #24, the same rotated 90° to maximize short
  folds, has skew −1.6 and "performs objectively worse": "simply
  increasing the number of short folds at the expense of medium folds
  merely creates additional kinetic traps for the topologically necessary
  long folds."
- **Order is not changed by the first fold.** "while the initial fold will
  reduce the penalty for subsequent events, it will not, on average, change
  the order in which subsequent folds occur."
- **Thermal stability (Fig. 6b).** Higher measured melt and anneal
  temperatures go with lower φ; predicted Tm, which treats each staple as
  first to bind, underestimates stability. No hysteresis values are given.
- **Combination (Fig. 7).** "roughly equivalent weights of 33%, 32%, and
  35% for Tm, entropy skew, and blocking", fitted on 28 of 34 designs (six
  with internal excess-scaffold loops excluded as steric outliers). A
  LASSO over more than 30 metric variants keeps skew and Tm but picks
  positive inter-domain cooperativity instead of blocking, which the
  authors take to mean "our overall set of metrics is in some way
  incomplete or incorrect" or needs a nonlinear combination.
- **Funnel, not path.** The collapse "supports the hypothesis that 2D
  origami is more funnel-like than path-like"; "the aggregate properties of
  event distributions in origami matter more than their precise
  propagation during assembly", which the authors put down to the weakness
  of the cooperative couplings beside hybridization.
- **Qualitative trends.** Sequence rotation keeping the excess loop on an
  edge changed nothing; an internal excess loop raised defectivity sharply
  ("catastrophic steric effects"); and "altering the seam symmetry
  consistently increased defectivity, despite our hypothesis that
  interdigitated seams should improve yield."
- **Measurement and its cost.** "yield measurements have an inverse
  relationship between their resolution and both their cost and
  throughput" (gel, then AFM or TEM, then DNA-PAINT). On a gel "only a
  significant amount of damage will shift the band", and "design
  variations can significantly shift the mobility even for well-folded
  structures": damaged #7 ran with well-folded #1 and #14. Of φ: "We equate
  the defectivity, or φ, to the average number of missing or blocked
  staples for a design", yet "use this only as a very approximate
  substitute for the number of missing or blocked staples. The primary
  utility of φ is to facilitate comparison between designs."
- **Why poor anneals.** Lowered concentration and time make outcomes
  distinguishable with fewer images: "Without this, the imaging and
  classification time would have been infeasible."
- **Uncertainty.** Staple-pool synthesis ±2.8 in φ; sample size ±0.2 to
  ±1.7; day to day ±0.1 to ±0.3. Analysts disagreed on values and agreed on
  the ordering of designs.

## Concepts

- **Defectivity φ**: a class-weighted mean standing roughly for missing
  or blocked staples per structure; useful for comparison only.
- **First-fold loop-entropy penalty distribution** and its **skew**: the
  penalty each staple's fold would pay if it closed first, over the whole
  design.
- **Blocking**: two copies of one staple each binding one of its scaffold
  sites, so that neither closes the fold (from the group's 2021 paper).
- **Funnel-like against path-like**: whether aggregate design properties
  or specific pathways decide the outcome.
- **The resolution-cost ladder** of yield measurements: migratory,
  imaging, oligomer-inclusion.

## Connections

It extends Majikes et al. (2021), whose blocked state becomes one metric
of four, and Majikes et al. (2020), LIT-tmp0hqya, whose fold-level loop
entropy it aggregates. It cites Dannenberg et al. (2015), LIT-tmpdyrnb, as
the melting model to test across designs, and Schneider, Möritz and Dietz
(2019), LIT-tmp7v945, for folding in two to three stages. Dunn et al.
(2015), LIT-tmpqku12, and Wah et al. (2016) steered one design by stability
or concentration; this paper varies the design across 34. Wagenbauer et
al. (2014), LIT-tmpduceb, is cited for oligomer-inclusion yield, and its
point that observables merge states is echoed by the gel result. Sobczak
et al. (2012), LIT-tmpg98v0, is cited for gels on one design. The review
of Cumberworth and Reinhardt (2025), LIT-tmp7dfy2, gives the loop-order
mechanism behind the skew metric and argues that blocking is rare at
typical concentrations; the two disagree there, under different
concentrations. DeLuca et al. (LIT-2081, NOTE-1561, THEORY-1398) are
cited for modelling; their global topological traps in 3D are not the
local traps for long folds found here. Rothemund (2006) is not in the
reference list.

## Bearing on the record

- **A's characterization.** "A 2026 study" and the title are supported
  (NAR 2026; preprint 2025). The pubs.rsc.org tag is wrong for this paper,
  an Oxford University Press journal; it fits the 2025 review. That the
  paper "distinguishes several positive and negative cooperative
  mechanisms" is supported with a qualification: the four are presented as
  the literature's, the paper's own result is the metrics and their test,
  and it could not separate the positive and negative inter-domain terms.
  "blocking" and "base stacking" are the paper's; "binding-site proximity"
  and "loop-mediated cooperation" are A's paraphrases of positive
  inter-domain and inter-fold cooperativity. A's sentence before it, that
  earlier folding can "obstruct a binding site, strain a loop, or create
  steric exclusion", is A's own: blocking here is competition from a second
  staple copy, and the paper's steric effect is the internal excess loop.
  A's definition of a productive nucleus, as partial organization that
  makes further compatible organization more likely, is A's own, and the
  paper qualifies it: adding short-fold nuclei in place of medium folds
  made things worse.
- **CLAIM-567 (feasible, reachable, reliably reachable).** Supports,
  empirically: 34 designs encode one feasible target, and how reliably a
  fixed protocol reaches it varies with design (φ about 10 to 35).
- **CLAIM-583 (same complex, different reach).** Qualifies: the designs
  share the target shape but not the compatibility complex, since routing,
  seams and motifs change which domains pair. Sequence rotation, which
  keeps the routing, is the nearest to the same complex, and it changed
  nothing.
- **CLAIM-571**: leaves open; melt Tm and low defectivity go together, so
  holding and reaching are correlated here, not shown to differ.
  **CLAIM-581, CLAIM-591**: none; no hysteresis values.
- **CLAIM-569 (construct, maintain, transition).** Mild support:
  concentration and time are the constructing resource the authors cut,
  and thermal stability enters the model as its own term.
- **CLAIM-566**: leaves open; assembly only.
- **CLAIM-557, CLAIM-574, CLAIM-570, CLAIM-592 (observing budgets).**
  Support, as an example: resolution rises with cost from gel to AFM to
  DNA-PAINT, and AFM classes cannot count staples. The gel is not a
  coarsening of AFM: it merges damaged with well-folded (#7 with #1 and
  #14) and splits well-folded designs by mobility, which bears on
  CLAIM-574's nesting of probe families.
- **CLAIM-572 and QUESTION-374 (one budget for observing and acting).**
  An example on the observer's side: the authors spend down concentration
  and anneal time to make outcomes distinguishable at an affordable
  imaging cost.
- **CLAIM-184 (anchors entrench).** Weak, indirect support: many
  nucleation points with few routes to the long folds raise defects.
- **CLAIM-185 (persistence as anchor).** Qualifies: more short, stable
  early folds made outcomes worse (#24); the distribution of penalties
  matters, not the number of anchors.
- **CLAIM-478 and CLAIM-480 (settled degrees of freedom as constraints).**
  Some support: inter-fold cooperativity is a closed fold constraining the
  rest of the scaffold. The paper does not frame it so.
- **QUESTION-380 (when a small compatible nucleus helps).** Directly
  relevant: not more nuclei, but a positively skewed penalty distribution,
  offered as a predictor from the constraint architecture.
- **QUESTION-tmpg0j9y**: leaves open; no fixed stock was reallocated.
  **CASE-tmpu0s44**: partly realized; a fixed target, assembly reliability
  across 34 arrangements with uncertainty, but arrangement rather than
  availability is varied, and neither time, intermediates nor persistence
  is measured.
- **CLAIM-025, QUESTION-388, TERM-070, QUESTION-090**: none.
- Filed: THEORY-tmpcfriw. No instruction for machine-learning practice.

## Limitations

- **φ is a coarse proxy**, by the authors' own account, from hand
  classification.
- **One shape**, 28 designs in the regression, linear models only; the
  LASSO and the hand-built model disagree on the inter-domain term.
- **Poor-anneal transfer** rests on a supplementary section not read.
- **No hysteresis** is quantified in the main text.
- The authors grant that the result "does not necessarily provide
  confidence that the exact metric formulations we chose will work for any
  arbitrary origami system."

## Open questions

- Does the skew metric order designs of other shapes, and 3D designs?
- Does the blocking metric earn its weight at typical concentrations,
  where the 2025 review argues blocking is rare?
- Would per-staple readout (DNA-PAINT) recover the same ordering?
