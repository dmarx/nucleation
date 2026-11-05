---
status: Read
paper: 'LIT-tmp11aw1'
title: 'Marras et al. — Programmable motion of DNA origami mechanisms'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read on 2026-11-05 from the PubMed Central HTML article page of the
    version of record (https://pmc.ncbi.nlm.nih.gov/articles/PMC4311804/),
    PMC's XML carrying no body for this article; text converted from the
    HTML. Read in full: the Significance statement, abstract, introduction,
    Mechanism Design, Simple Motion (sliders, hinges), Complex Motion
    (crank–slider, Bennett linkage, projection kinematics), Actuation, the
    closing paragraph, Materials and Methods, and every figure caption
    (Figs. 1–6). Not read: the reference list; the Supporting Information
    (Figs. S1–S9, the projection-kinematics derivation, energy-landscape
    details, locking-strand designs), which PMC served behind a JavaScript
    download interstitial that was treated as a bot check and not retried;
    Movies S1–S3 and Dataset S1. Anything resting on the SI is marked
    unread below. Section names are the paper's.
date: '2026-11-05'
summary: >-
  DNA origami sliders and hinges built from stiff bundles joined only by
  single-stranded scaffold move in one designed degree of freedom whose
  range and stiffness the connection lengths set; TEM fluctuations,
  Boltzmann-inverted, give the force or torque to hold each configuration.
  A crank–slider and a Bennett linkage follow their rigid-body paths; the
  linkage's higher-energy compacted state, rarely occupied unaided, is held
  by locking staples or closing strands and released by strand
  displacement, each move in about a minute. TEM on a surface, small
  samples, misfolds excluded, SI unread.
---
<!-- inactive-ok-file: THEORY-tmp1799q THEORY-1398 CLAIM-567 CLAIM-569 CLAIM-571 CLAIM-591 CLAIM-583 CLAIM-581 CLAIM-566 CLAIM-557 CLAIM-574 CLAIM-570 CLAIM-592 CLAIM-478 CASE-206 CASE-201 THEORY-1406 THEORY-1374 THEORY-1390 THEORY-1405 THEORY-1415 THEORY-1417 CASE-208 THEORY-1420 — Proposed or new; cited from the reading of Marras et al. (2015) as open -->

# NOTE-tmpjeolx: Marras et al. — Programmable motion of DNA origami mechanisms

## Contribution

The paper carries the vocabulary of macroscopic machine design (links,
joints, motion paths, degrees of freedom) into DNA origami. Stiff
double-stranded bundles serve as links, and joints are made by connecting
them only through single-stranded scaffold, so that the joint's motion is
set by the length and placement of those connections. It builds a slider
(a 30-helix tube around a 6-helix bundle) and a hinge (two 18-helix arms),
measures their thermal motion, composes them into a crank–slider and a
Bennett linkage, and actuates the linkage after folding with added
strands. It is, among the works read for this batch, the one with designed
and reversible reconfiguration.

## Key insight

A configuration of a compliant DNA mechanism has two separable costs: the
cost of visiting it, which thermal motion may pay for nothing, and the cost
of holding it, which the thermal ensemble itself measures. The linkage's
compacted bundle is visited thermally but "is a higher energy state",
"Adopting this higher energy state requires performing work" (Actuation),
and that work is supplied by bound strands, added either at folding or
afterwards.

## Assumptions

- **The grid ensemble is the solution ensemble.** The landscapes assume
  Boltzmann weighting on TEM-measured distributions; the authors
  acknowledge that "surface deposition and staining may affect the
  configuration seen on the grid" (Methods).
- **Rigid links, idealized joints.** A 4-helix bundle's persistence length
  of 740 nm against links of about 35 nm is taken to make a 16-helix link
  rigid; the authors concede the "hinge axes are not ideally
  constrained".
- **Projection kinematics** assumes that a planar pair of links lies flat on
  the grid, and works only "Because the full geometry and motion path are
  known" (Complex Motion).
- **Fluorescence quenching** stands for the bundled state.
- **Conditioned on correct folding.** "Misfolded structures were omitted
  from the motion analysis"; "Only well-folded structures were included in
  the analysis."

## Key results

- **Range set by connection length (Simple Motion; Fig. 2).** Slider 1
  (49- and 28-nt connections) "revealed a range of thermal motion of 14.0
  nm" (n = 275); slider 2 (86- and 96-nt) "resulted in a range of motion of
  29.2 nm" (n = 251). The longer connections "also occasionally caused the
  outer tube to fold apart from the inner 6 hb" (Fig. S2, unread); no
  misfold fraction is given.
- **Holding curves (Figs. 2E–F, 3E–F).** "The energy landscape was
  differentiated to determine the force required to hold each joint at any
  specific length." Slider 1 behaves as "a linear spring with a stiffness
  of 0.42 pN/nm"; slider 2 is nonlinear, "0.07 pN/nm at smaller extensions
  and 0.21 pN/nm for longer extensions". Hinge 1 acts approximately as "a
  linear torsional spring with a stiffness" of 25 pN-nm/rad rising to 45 at
  the ends; hinge 2 about 70 pN-nm/rad at the ends, flexible between. The
  derivation is in the SI, unread.
- **Hinge angles (Fig. 3).** "Joint angles varied from 11° to 147° with an
  average of 79.7° for hinge 1" (n = 918); hinge 2 11–131°, mean 62°
  (n = 248).
- **Composite mechanisms (Figs. 4–5).** The crank–slider (n = 56) follows
  its prediction "with some fluctuation about the ideally constrained
  motion path"; the Bennett linkage (n = 52) "closely follows the expected
  motion path for its rigid-body counterpart".
- **The compacted state, unaided (Complex Motion; Fig. 6B).** "Only a small
  fraction of the mechanisms was observed in the closed bundle
  configuration, likely due to electrostatic repulsions": 9.9% bundled.
- **Fixed at folding (Fig. 5D–E).** With added locking staples (Fig. S5,
  unread), "Eighty-one percent of the linkages were successfully held in
  the expanded configuration and 93% in the compacted configuration. These
  results represent upper bounds because surface deposition may force
  nearly expanded or nearly compacted mechanisms into their respective
  extreme configuration."
- **Switched after folding (Actuation; Methods).** "Sixty staples were
  designed to present ssDNA overhangs", bridged by closing strands that
  zipper the linkage shut, each with "5-nt toeholds to allow for their
  subsequent removal via toehold-mediated strand displacement". Closing
  strands at "twofold excess (110 nM) compared with the total number of
  connections", opening strands at "20-fold excess compared with the
  closing strands (2 μM)", linkage at 1.9 nM. Bundled fractions: "9.9% in
  the unconstrained case, 93.1% in the compacted structures, and 10.0% in
  the expanded structures".
- **Timing (Fig. 6E–F).** "Closing actuation occurred on a timescale of"
  t1/2,c = 55 s, expanding t1/2,e = 49 s, both "double-exponential". The
  authors guess that expansion is fast "perhaps because the process is
  accelerated by electrostatic repulsion driving toward a lower energy
  configuration".
- **Construction (Methods).** Scaffold 20 nM, each staple 200 nM, 18–20 mM
  MgCl2; "initial heating to 65 °C to melt all interactions and then slow
  cooling to 25 °C over the timescale of 2 d"; gel purification. No
  melting curves, hysteresis or yields in the main text.
- **Limits of observation (Complex Motion; Methods).** "It is difficult to
  verify 3D motion by typical imaging methods such as TEM or atomic force
  microscopy (AFM)"; below β′ of 45° the links overlap and the projected
  angles cannot be measured; repeat-measurement error 2.5° and 0.95 nm.
  The bulk fluorescence assay tells only closed from not closed.

## Concepts

- **Kinematic mechanism**: links and joints (revolute, prismatic) with a
  designed number of degrees of freedom and a motion path.
- **Compliant single-stranded connections**: joints whose motion is set by
  entropic elasticity, sterics and electrostatics of ssDNA.
- **Boltzmann-inverted energy landscape**, differentiated to a holding
  force or torque.
- **Locking staples**, added at folding to fix a configuration;
  **closing strands** that bridge overhangs to zipper a structure shut;
  **toehold-mediated strand displacement** to remove them.
- **Projection kinematics**: inferring a 3D state from a 2D projection by a
  known motion path.
- **Bennett linkage**: a spatial four-bar linkage with one degree of
  freedom, here with equal links, going from an open frame to a compact
  bundle.

## Connections

It builds on Castro's group's earlier origami design work and on
macroscopic mechanism theory. In the held record, the nearest construction
is Hopkins's freedom and constraint topologies for flexures ([THEORY-1406](../theory.d/THEORY-1406.md),
[THEORY-1374](../theory.d/THEORY-1374.md), [THEORY-1390](../theory.d/THEORY-1390.md)): these DNA joints are flexure-like mechanisms
whose freedom is set by placing compliant constraints, and locking staples
add constraint to remove the freedom. The slider's steric stop resembles
the contact-stopped second state of [THEORY-1405](../theory.d/THEORY-1405.md); strand-driven switching
can be set against the externally actuated origami of [THEORY-1415](../theory.d/THEORY-1415.md),
[THEORY-1417](../theory.d/THEORY-1417.md) and [CASE-208](../cases.d/CASE-208.md); the Boltzmann-inverted landscapes are
one-dimensional instances of the landscapes of [THEORY-1420](../theory.d/THEORY-1420.md); and the
Bennett linkage's compact bundle against open frame is the deployable
contrast of [CASE-201](../cases.d/CASE-201.md). Same group as the held DeLuca et al. simulation,
[LIT-2081](../literature.d/LIT-2081.md) ([NOTE-1561](NOTE-1561.md), [THEORY-1398](../theory.d/THEORY-1398.md)); the slider-2 misfold, the tube folding
apart from the inner bundle, is a design-dependent fold failure, but the
paper offers no folding mechanism and does not bear on that account.
Within this batch it is the dynamic counterpart to Rothemund (2006)'s
static shapes, and its exclusion of misfolded particles leaves to
Wagenbauer, Wachauf and Dietz (2014) the question of how good the folded
objects are.

## Bearing on the record

- **[CLAIM-567](../claims.d/CLAIM-567.md) (feasible, reachable, reliably reached): supports, with a
  concrete triple.** The bundled state is feasible (the locked bundle holds
  at 93%), reachable (9.9% of free linkages visit it thermally) and
  reliably reached only with closing strands (93.1%). The authors call the
  grid fractions upper bounds.
- **[CLAIM-571](../claims.d/CLAIM-571.md) (reaching threshold need not equal holding requirement):
  qualifies, in the reverse direction.** Here the target is cheap to reach,
  by thermal visits at no input cost, and dear to hold. No threshold over
  the path is measured. Compare [CASE-206](../cases.d/CASE-206.md), where passage costs more than
  either end.
- **[CLAIM-569](../claims.d/CLAIM-569.md) (construct, maintain, transition): supports.** Construction
  is a two-day anneal at tenfold staple excess and gel purification;
  maintenance is bound strands or locking staples against electrostatic
  repulsion, with holding curves in pN or pN·nm/rad for the joints;
  transition is about a minute of strand addition or displacement at stated
  excesses. None fixes another, but they are not put on one scale.
- **[CLAIM-591](../claims.d/CLAIM-591.md) (directed moves): supports qualitatively.** Closing and
  opening are different one-way chemical moves, with different inputs (2×
  bridging strands, then 20× displacing strands) and rates (55 s and 49 s):
  the configuration returns but the reagent state does not. One cycle only.
- **[CLAIM-583](../claims.d/CLAIM-583.md) and [CLAIM-581](../claims.d/CLAIM-581.md): leave open.** The two sliders differ in
  connection lengths, so in compatibility, not only in moves or costs; the
  paper shows thermal (barrier-type) and consumed (additive) costs side by
  side but does not test an ultrametric.
- **[CLAIM-566](../claims.d/CLAIM-566.md): consistent.** Locked or actuated structures persist and
  nothing regenerates them; no persistence horizon is measured.
- **[CLAIM-557](../claims.d/CLAIM-557.md), [CLAIM-574](../claims.d/CLAIM-574.md), [CLAIM-570](../claims.d/CLAIM-570.md), [CLAIM-592](../claims.d/CLAIM-592.md) and [QUESTION-374](../questions.d/QUESTION-374.md):
  illustration only.** TEM projection (costly, static, per particle),
  projection kinematics (model-dependent, blind below 45°) and bulk
  fluorescence (cheap, real-time, closed or not) separate different
  things, but no budgeted comparison is made.
- **[CLAIM-478](../claims.d/CLAIM-478.md): weak illustration, of stiffness rather than time.** Stiff
  links act as rigid constraints, so a compliant ssDNA network moves along
  a rigid-body path.
- Filed: [THEORY-tmp1799q](../theory.d/THEORY-tmp1799q.md). No instruction for machine-learning practice;
  nothing for the anthology.

## Limitations

- **The SI was not read**: the landscape derivation, the locking-strand
  designs (Fig. S5), the misfold images (Fig. S2) and the gel (Fig. S8)
  are unseen.
- **Surface statistics.** All conformational fractions come from
  negative-stain TEM, which the authors say may push near-extreme
  mechanisms into the extremes.
- **Small samples** for the mechanisms (56 and 52); misfolded particles
  excluded; no yields.
- **One actuation cycle**; cycling, fatigue and waste accumulation untested.
- **No thermal, cation or melting data**, so temperature as a
  reconfiguration resource is not addressed.
- **The electrostatic account of fast expansion** is the authors' guess
  ("perhaps").
