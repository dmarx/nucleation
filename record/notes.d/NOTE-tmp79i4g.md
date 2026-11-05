---
status: Read
paper: 'LIT-tmpairr7'
title: 'Ni et al. — Cooperativity, entropy, and effective concentration in DNA origami self-replication'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read on 2026-11-05 from the PubMed Central copy of the version of
    record (https://pmc.ncbi.nlm.nih.gov/articles/PMC13189100/, CC BY-NC
    4.0), fetched as JATS XML from Europe PMC's REST service and converted
    to text; no obstacle was met. Read in full: abstract, Introduction,
    Results, Discussion, Materials and Methods, the figure captions and the
    reference list. Not read: the supplementary materials (supplementary
    text, figs. S1-S14, tables S1-S11, among them fig. S7, which defines
    the replication rate, and table S11 of entropies), which are not in the
    XML, and the figure images, so figures are known only from their
    captions.
date: '2026-11-05'
summary: >-
  In a cross-tile self-replication cycle, a seed of origami tiles recruits
  supplied monomer tiles, whose tethered horizontal sticky ends, at an
  effective concentration raised from about 1 nM to about 0.8 mM, melt
  about 50 °C higher than in solution; UV fixes them and heating separates
  daughter from parent. A two-state model with three entropy terms, fitted
  once, predicts the melting of 1- to 4-tile assemblies to about 2 °C.
  Replication rates fall from about 1.9 per cycle for dimers to 1.6 for
  tetramers, and tetramers barely separate before the tiles unravel.
---
<!-- inactive-ok-file: THEORY-tmpnu25d THEORY-1398 THEORY-412 CLAIM-566 CLAIM-569 CLAIM-571 CLAIM-591 CLAIM-581 CLAIM-567 CLAIM-583 CLAIM-557 CLAIM-574 CLAIM-570 CLAIM-592 CLAIM-572 CLAIM-478 CLAIM-184 CLAIM-185 CASE-tmpu0s44 — Proposed or new; cited from the reading of Ni et al. (2026) as open -->

# NOTE-tmp79i4g: Ni et al. — Cooperativity, entropy, and effective concentration in DNA origami self-replication

## Contribution

A two-state model for binding between DNA origami tiles, with three
measurable entropy terms, fitted once by FRET and one gel set and then
used to predict the melting of other assemblies. It quantifies
cooperativity as effective concentration, uses it as a design rule (each
step of a replication cycle melts in its own temperature window), and
predicts an upper limit on the melting temperature of an N-tile string,
which sets how large a pattern could be replicated without the template
holding its product.

## Key insight

A template works by raising effective concentration: once the first few
bonds have paid the translational entropy, the rest bind at a local
concentration a million times higher, so weak bonds that would melt far
below the working temperature form on the template. Cooperativity here
sets the windows that make the replication cycle possible; it does not
maintain anything.

## Assumptions

- **Two-state binding**, open or closed, intermediates ignored; the
  authors flag this for large N ("partial binding and branching become
  more probable").
- **Nearest-neighbour thermodynamics** for each sticky end, corrected by
  one tether entropy ΔSp; rotational and flexibility entropies from
  small-angle geometry or fitted.
- **Independent steps**: vertical binding v and horizontal linking h
  succeed independently (Eq. 1: dimer yield v²h, trimer v³h², tetramer
  v⁴h³).
- **Equilibrium melting** throughout; no kinetics and no hysteresis are
  reported.

## Key results

- **The cycle (Results; Methods).** Vertical ends "have a melting
  temperature of ~20°C at 1 nM"; with eight of them a monomer binds the
  seed at about 45 °C. Horizontal ends melt at about −5 °C in solution but,
  held on the seed at "an effective concentration of ~1 mM", at about
  18 °C. UV "permanently binds the horizontal sticky ends"; "The dimers
  separate at ~50°C, and we have two dimers for every original parent
  seed". Each cycle cools "at a rate of 1.5 C/hour" from 50 to 18 °C (about
  21 h), then UV at 366 nm for 20 min, and "The sample is then split to
  repeat the cycle". Next-generation monomers are supplied: "In the
  presence of second-generation monomers, the FG dimers will act as
  parents", whose "offspring will be duplicates of the original parent
  seeds".
- **Replication yield (Fig. 1D).** "about 1.9 replication rate for dimers
  reducing to 1.6 for tetramers", where "the rate is 2 for a full yield and
  1 for no growth". The fit puts v near 1 and h near 0.8, "a limited
  horizontal binding, likely due to weak hybridization and additional
  photo crosslinking reaction". Linear, L-shaped and square patterns were
  copied: "Templated self-replication of two-dimensional (2D) tile
  patterns seems to work well."
- **Effective concentration (Fig. 3).** About 1 nM unbound; bound at about
  5.6 nm, about 0.8 mM, "around a million fold increase resulting in a
  shift in melting temperature of ~50°C". The FRET fit gives about 0.2 mM
  (the text's "0.2 nM" conflicts with the caption and looks like a typo).
- **Entropies by three routes.** Global fit ΔSp = −8.5R, ΔSr = −16.5R,
  ΔSv = −19.0R; geometric estimate −8.9R, −13.0R, −14.2R; oxDNA −8.1R,
  −11.9R, −12.6R. "with a single experimental measurement, the determined
  entropies can effectively predict the melting curves of other
  variations."
- **Size: practice against theory (Fig. 5D; Eq. 15).** "We found that we
  could barely separate tetramers before the DNA origami cross-tiles
  started unraveling." In the model the string's Tm rises with N to an
  upper limit, and the authors conclude the "theoretical feasibility of
  self-replicating a large and even infinity N-mer"; the design rule is
  that "we want to design the sticky ends such that monomer tiles can bind
  above 20°C, while the N-mer tile unbinds below 50°C." The Discussion
  adds that the length distribution of a 1D chain decays exponentially,
  "suggesting a theoretical prohibition of a 1D infinity-mer", in some
  tension with the infinite-N sentence.
- **What each probe can tell apart.** In AFM, "The daughters are attached
  with gold nanoparticles to distinguish from the parents": parent and
  daughter are the same pattern, told apart only by an added label. In
  FRET, "FRET pairs confined between the two dimer tiles can exchange
  energy even when they are not hybridized", so at 4 bp hybridization and
  confined adjacency are not separated. Gels are run at the binding
  temperature, from 2 h at 50 °C to 6 h at 10 °C.

## Concepts

- **Effective concentration**: the local concentration of a tethered
  partner, about 1/(gL³).
- **Cooperativity as entropy paid once**: "the translational entropy
  penalty is paid only once when the first several bonds form".
- **Template-product inhibition**: a product bound too strongly to its
  template to be released.
- **Non-overlapping melting windows**: the design condition for cycling
  through several steps.
- **Photo-crosslinking** (CNVK) as an irreversible fixing step.

## Connections

The tiles are scaffolded origami made as in Rothemund (2006),
LIT-tmp5gf89. Majikes et al. (2020), LIT-tmp0hqya, Dannenberg et al.
(2015), LIT-tmpdyrnb, and Dunn et al. (2015), LIT-tmpqku12, invoke
cooperativity within one origami through loop entropy or effective
concentration; this paper carries the same reasoning one level up,
between origami, and quantifies it. As in Wagenbauer et al. (2014),
LIT-tmpduceb, yield is read from gel quantification. It is the only work
of this branch with a cycle that multiplies structure and with a
deliberately irreversible step. The held simulation of DeLuca et al.
(LIT-2081, NOTE-1561, THEORY-1398) is about folding one origami; the two
meet only where tiles unravel near the separation temperature. The
methods follow H. Ni's NYU thesis (2024). Earlier DNA origami
self-replication work it cites (He et al. 2017, on exponential growth
and selection; Zhou et al. 2021, on mutations) is not held.

## Bearing on the record

- **A's characterization.** The title, the 2026 date and the link are
  right, and that it "examines cooperative binding in self-replicating DNA
  origami motifs" is supported ("We test our model with self-replication
  of DNA origami motifs of increasing sizes"), though much of the evidence
  is melting of assemblies outside a replication run. "molecular
  machinery" is A's paraphrase: the paper has none, and only cites such
  work. That self-replication "in a supplied chemical environment" does not
  by itself establish reciprocal maintenance of constraints is A's
  inference, consistent with the text, which never discusses closure; but
  what is supplied is more than chemical: a thermal program, UV, fresh
  monomers and the splitting of samples. A's further proposals, a reaction
  network for endogenous regeneration and a staged programme of damage
  and replacement, are A's own.
- **CLAIM-566 (assemble, persist, regenerate).** Supports, and refines:
  assembly is measured (per-cycle yield, v and h); persistence is
  engineered by the covalent crosslink and not measured over a horizon;
  regeneration after turnover is absent. What is shown is a fourth thing,
  multiplication: more copies of a pattern from fresh parts, restoring no
  one of them.
- **TERM-070 (closure of constraints).** An instance of non-closure: the
  template constrains the assembly of its daughters and survives the
  cycle, but dependence runs one way, from parent to daughter, and every
  enabling condition is set by the experimenter (the reader's reading, not
  the paper's words).
- **CLAIM-569 (construct, maintain, transition).** Supports: making a copy
  (cooling, UV) and keeping it (covalent, nearly free) cost differently,
  and moving out of the template complex (about 50 °C) is bounded above by
  the tile's own destruction.
- **CLAIM-571 (threshold against holding requirement).** Supports:
  separation needs a peak of about 50 °C, unlike the 18 °C hold at which
  the complex forms, and there is a window only while that peak stays
  below unravelling.
- **CLAIM-591 (directed costs).** An instance: the crosslink makes a bond
  reversible at 18 °C one-way, which is what lets heating separate
  daughters without undoing them.
- **CLAIM-581 (peak-cost ultrametric).** Qualifies: temperature acts as a
  peak cost, but each cycle also spends about 21 h of cooling, an additive
  cost the paper does not compare.
- **CLAIM-567 (feasible, reachable, reliable).** Supports: large N is
  feasible in the model; separation is reached only to tetramers, and
  per-cycle reliability falls from 1.9 to 1.6.
- **CLAIM-583**: leaves open; 7, 8 or 9 bp ends change costs, not
  compatibility.
- **CLAIM-557, CLAIM-574 (observing budgets).** An instance: parent and
  daughter are indistinguishable in AFM until gold labels are added, and
  FRET at 4 bp cannot tell hybridized from confined. **CLAIM-570,
  CLAIM-592, CLAIM-572, QUESTION-374**: none directly.
- **CLAIM-480 (eliminated degrees of freedom leave constraints).**
  Supports by analogy: tethering removes translational freedom and leaves
  a new effective coupling, raising the horizontal ends' Tm from −5 to
  18 °C.
- **CLAIM-478 (scale separation makes constraints).** An analogue in
  temperature, not time: separated melting windows are the design
  condition.
- **CLAIM-185 and CLAIM-184.** A physical instance of persistence as
  anchor: the fixed seed persists across cycles and further structure
  grows on it; entrenchment appears only as template-product inhibition.
- **QUESTION-380**: bears; the template is a small compatible structure
  that makes the next assembly likely, though the paper does not speak of
  nucleation. **QUESTION-388**: programmable, not self-governing; the cycle
  and the sticky ends are set from outside. **CLAIM-025, QUESTION-090,
  QUESTION-tmpg0j9y**: none.
- **CASE-tmpu0s44**: partial; binding strength and size vary at fixed tile
  geometry, with yield and melting measured, but not allocation at fixed
  total, and no kinetic traps; like the case, it leaves regeneration out.
- **LIT-515 and NOTE-419 (England, the statistical physics of
  self-replication).** A direct referent for England's bound relating a
  replicator's heat release to how fast it copies and how durable the copy
  is: copies made durable by crosslinking under an imposed thermal cycle,
  the non-living, externally driven case. THEORY-412 and THEORY-679 are
  adjacent.
- Filed: THEORY-tmpnu25d. No instruction for machine-learning practice.

## Limitations

- **The replication data are one figure** (Fig. 1D, with standard
  deviations), and the rate's definition is in fig. S7, not read; the
  number of cycles is not stated in the main text.
- **The model is untested beyond tetramers**; the N = 512 curves are
  extrapolation, and the Discussion itself rules out an infinite 1D chain.
- **No kinetics, no hysteresis, no misfolded or trapped products**, and no
  measurement of daughters persisting or degrading over time.
- A typo: "Ceff=0.2 nM" in the text against "0.2 mM" in the caption.

## Open questions

- Does the model's Tm(N) hold for pentamers and beyond, where partial
  binding and branching enter?
- Would a cycle in which some member regenerates another's enabling
  condition, rather than the experimenter, be buildable from these parts?
