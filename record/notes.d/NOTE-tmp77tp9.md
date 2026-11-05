---
status: Read
paper: 'LIT-tmpepjt3'
title: 'Douglas et al. — Self-assembly of DNA into nanoscale three-dimensional shapes'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read on 2026-11-05 from the NIH author manuscript in PubMed Central
    (PMC2688462, NIHMS105924), fetched as JATS XML through NCBI
    E-utilities and converted to text. Read in full: the abstract, all of
    the main text, the captions of Figs 1–4, acknowledgements, author
    contributions and references. The manuscript has no section headings,
    so results are cited by paragraph topic and figure. Not read: the
    figure images (captions only), and the Supplementary Information
    (Notes S1 and S2: scaffold preparation, strand diagrams, six-helix
    bundle robustness, the icosahedron gel and probably the per-target
    yields), whose PMC copy sat behind a reCAPTCHA page and whose Europe
    PMC archive held only an empty image.
date: '2026-11-05'
summary: >-
  Origami extended to multilayer 3D solids on a honeycomb lattice, with
  design rules and a one-pot fold at 7–44 % of scaffold in monomer, but
  only with week-long ramps at about 16 mM MgCl2 and low NaCl; short
  ramps, low Mg2+ or high Na+ give grossly misshapen products, while flat
  and six-helix-bundle origami fold in 72 minutes. Mechanisms, kinetic
  traps included, are conjecture; the Supplementary Information unread.
---
<!-- inactive-ok-file: CLAIM-184 CLAIM-478 CLAIM-557 CLAIM-566 CLAIM-567 CLAIM-569 CLAIM-570 CLAIM-571 CLAIM-572 CLAIM-574 CLAIM-581 CLAIM-583 CLAIM-591 CLAIM-592 CLAIM-tmp7y162 THEORY-1398 THEORY-tmp500wn THEORY-tmp8xe45 NOTE-tmpwxm2p — Proposed, Unavailable, Skimmed or new; cited from the reading of Douglas et al. (2009) as open -->

# NOTE-tmp77tp9: Douglas et al. — Self-assembly of DNA into nanoscale three-dimensional shapes

## Contribution

A general design grammar for custom 3D origami: helices stacked as
"pleated layers of helices constrained to a honeycomb lattice", with rules
for crossover spacing and staple length, and a design order from carving
the shape to threading the sequence (caDNAno is introduced here and
described in its reference 21). Five shapes were folded and imaged, a
sixth shown by gel. The paper gives the first evidence that multilayer
folding is far slower than flat or six-helix-bundle folding, names three
determinants of it (ramp time, divalent and monovalent cations), and
shows hierarchical assembly from separately folded monomers.

## Key insight

A multilayer design that is perfectly specified can still be hard to
reach: with every strand present and the same temperatures crossed, what
decides whether it folds is how long the ramp spends and the cation
balance, and the authors can only conjecture why: "Presumably,
multilayered structures must traverse more difficult kinetic traps,
perhaps due in part to the larger density of crossovers".

## Assumptions

- **B-form geometry** (2.0 nm diameter, 0.34 nm rise, 21 base pairs per
  two turns) holds well enough that the ±120° pleats form as designed.
- **Gel band brightness under ethidium bromide** measures the scaffold
  fraction in monomer, and the purified leading band stands for the
  well-folded population.
- **Negative-stain TEM of gel-purified particles** represents the shapes
  in solution.
- **Mechanisms** (cation roles, GC content, traps) are hypotheses, not
  tested.

## Key results

- **Geometry (Fig. 1).** Helix m+1 "has a preferred attachment angle to
  helix m of ±120 degrees"; staple crossovers are "spaced apart at
  intervals of 7 base pairs", which "maintains the local crossover density
  along any helix-helix interface at roughly one per 21 base pairs";
  staples are "between 18 and 49 bases inclusive, with an average between
  30 and 42".
- **Design cost.** Manual design "was very time consuming and
  error-prone"; with caDNAno a novice can produce sequences "within a
  day", and the cycle can take "as little as two weeks".
- **Protocol.** 10 nM scaffold, "50 nM of every oligonucleotide staple
  strand", 16 mM MgCl2, "cooled from 80°C to 60°C over the course of 80
  minutes and then cooled from 60°C to 24°C over the course of 173 hours".
- **Yield.** "The fraction of scaffold strands that were incorporated into
  monomeric species after folding varied from 7% to 44% for these targets
  as estimated by ethidium-bromide fluorescence intensity." Which target
  gave which is not in the main text.
- **Ramp series (Fig. 3b).** The fast ramp is "1.2 h: 95°C to 20°C at 1.6
  min/°C"; the slow ramps run 3 to 173 h over 80 to 24 °C. Every ramp
  crosses the same temperatures; only the time spent changes.
- **Three determinants (Fig. 3).** Short ramps, low MgCl2 or high NaCl
  "yielded a slowly migrating species" and "grossly misshapen objects". "In
  contrast, week-long thermal annealing at higher concentrations of MgCl2
  combined with low concentrations of NaCl yielded a fast-migrating
  species" of well-folded particles, with multimer and aggregate bands.
  Mg2+ was varied "from 0 to 30 mM"; "Excess NaCl inhibits proper
  folding".
- **One cation, two effects.** "Divalent cations thus appear to accelerate
  the rate of proper folding and increase the amount of undesired
  aggregation while monovalent cations appear to decelerate the rate of
  proper folding and decrease the amount of undesired aggregation."
- **Complexity.** "Many of the structures require week-long thermal ramps
  for proper folding, even under idealized divalent- and
  monovalent-cation concentrations", while "the Rothemund flat origami and
  these simpler nanotube structures could be folded with 72 minute ramps".
  The comparison is categorical; how yield scales with complexity is not
  measured.
- **Same shape, two scaffolds (genie bottle).** The bottle "takes up only
  4500 base pairs"; on a 7308-base M13 variant and on the "4733-base
  forward strand" of pEGFP-N1, "Folding of the same shape under identical
  conditions gave superior yield with the M13-based scaffold sequence."
  The GC content (43 % against 53 %) "could explain" it; "Systematic
  studies will be required". Length and the dangling tail differ too.
- **What the gel tells.** "increasing agarose-gel mobility correlated with
  improvement of quality of folding as observed by transmission electron
  microscopy, suggesting that correctly folded structures tend to be more
  compact than misfolded versions." Band position ranks only within a
  condition: at 4 mM Mg2+ even the fastest band was grossly defective.
- **What TEM tells.** Particles "generally were observed to be monodisperse
  with a homogenous shape"; helix-gap estimates "may originate in part from
  staining artifacts"; for the icosahedra, many particles "have missing
  struts, due either to incomplete folding or to particle flattening and
  collapse".
- **Hierarchical assembly (Fig. 4).** Polymers of the stacked cross from
  purified monomers and connector staples; heterotrimeric icosahedra from
  three monomers made by cyclic permutation of one scaffold sequence, with
  "two completely different sets of staple strands" beyond the first.
- **Outlook.** "Improvements in the rate and yield of folding will be
  critical"; the authors propose "folding with formamide dilution instead
  of thermal ramps to decrease thermal damage to the DNA".

## Concepts

- **Honeycomb-pleated origami**; the ±120° angle set by crossover
  register; crossover density about one per 21 base pairs.
- **Scaffold path**; staple-crossover planes every 7 base pairs.
- **Thermal-annealing ramp**, its length as the varied quantity.
- **Divalent against monovalent cations**; misfolding against aggregation
  against multimerization.
- **Gel mobility as compactness**; effective helix diameter in TEM.
- **Hierarchical (two-step) assembly** with connector staples; cyclic
  permutation of a scaffold to make distinct monomers.

## Connections

It extends Rothemund's flat method ([LIT-tmp5gf89](../literature.d/LIT-tmp5gf89.md), [NOTE-tmp8kyp2](NOTE-tmp8kyp2.md)), using a
fivefold staple excess against Rothemund's hundredfold and a week-long
ramp against about two hours. Sobczak's thesis ([LIT-tmpwddcn](../literature.d/LIT-tmpwddcn.md),
[NOTE-tmpwxm2p](NOTE-tmpwxm2p.md)), from the same lineage, re-examines the week-long
protocols, finds them spending about 20 h in the productive window
([THEORY-tmp500wn](../theory.d/THEORY-tmp500wn.md)), and makes 3D folding fast and isothermal. Schneider et
al. ([LIT-tmp7v945](../literature.d/LIT-tmp7v945.md), [NOTE-tmpqi66a](NOTE-tmpqi66a.md)), Dunn et al. ([LIT-tmpqku12](../literature.d/LIT-tmpqku12.md)) and
Dannenberg et al. ([LIT-tmpdyrnb](../literature.d/LIT-tmpdyrnb.md)) resolve folding pathways that this paper
treats as a black box. Wagenbauer et al. ([LIT-tmpduceb](../literature.d/LIT-tmpduceb.md), [NOTE-tmpmw05j](NOTE-tmpmw05j.md))
measure what its assay misses: gel mobility and TEM averages hide missing
staples. Marras et al. ([LIT-tmp11aw1](../literature.d/LIT-tmp11aw1.md)) supply the reconfiguration this
paper lacks, and Majikes et al. 2020 ([LIT-tmp0hqya](../literature.d/LIT-tmp0hqya.md)) the fold
thermodynamics it never measures. The kinetic traps it conjectures are
what the held simulation, [LIT-2081](../literature.d/LIT-2081.md) ([NOTE-1561](NOTE-1561.md), [THEORY-1398](../theory.d/THEORY-1398.md)), addresses;
its hypotheses (crossover density, confined interlayer folding) anticipate
interior-geometry traps. Its honeycomb lattice is the frame of the
logic-gated barrel of Douglas, Bachelet and Church 2012 ([LIT-tmpqorwy](../literature.d/LIT-tmpqorwy.md)).

## Bearing on the record

- **A's characterization.** That the method was extended to elaborate 3D
  shapes by Douglas and colleagues in 2009: supported ("Here we extend this
  method to building custom three-dimensional shapes"). "including
  multilayer helix bundles": A's paraphrase; the paper speaks of pleated
  honeycomb layers and "multilayered structures", and of helix bundles only
  for its six-helix struts and the simpler nanotube; the substance is
  supported. "and composite structures": loosely supported (two-domain
  crosses, polymers, heterotrimeric icosahedra); the word is A's. A's
  account of the process (mix, apply a temperature program) matches the
  paper's "one-pot reaction, after rapid heating followed by slow
  cooling", but A omits the week-long anneal, the 7–44 % yields and the
  cation dependence, which are the paper's main kinetic findings.
- **[CLAIM-567](../claims.d/CLAIM-567.md) (feasible, reachable, reliably reached): supports.** The
  designs are feasible and reachable, reliability poor, and the same
  design is not reached under 1.2 h ramps, at 4 mM Mg2+ or at high Na+.
- **[CLAIM-571](../claims.d/CLAIM-571.md) and [CLAIM-581](../claims.d/CLAIM-581.md): consistent, not bearing on peak cost.**
  Reaching needs a week, holding survives 24 h at 30–50 °C or a gel on
  ice; but all ramps share one peak, so the cost that differs is time,
  the additive case in which [CLAIM-581](../claims.d/CLAIM-581.md) says no tree exists (suggestive
  only).
- **[CLAIM-569](../claims.d/CLAIM-569.md): supports the construct ≫ maintain gap qualitatively**;
  transition: nothing. **[CLAIM-566](../claims.d/CLAIM-566.md): supports the example**: assembly at a
  yield, persistence through purification and incubation, nothing
  regenerates.
- **[CLAIM-583](../claims.d/CLAIM-583.md): qualified support.** The bottle on two scaffolds is not a
  clean same-complex comparison: staples, length and tail differ.
- **[CLAIM-tmp7y162](../claims.d/CLAIM-tmp7y162.md) (non-monotone resource): roughly supports the
  time-widens part** (longer ramps help at fixed Mg2+), and adds a
  non-thermal case: Mg2+ too low fails, more raises proper folding and
  aggregation alike. That a usable Mg2+ window exists is the reader's
  inference; no upper failure point within 0–30 mM is named.
- **[CLAIM-557](../claims.d/CLAIM-557.md), [CLAIM-574](../claims.d/CLAIM-574.md), [CLAIM-570](../claims.d/CLAIM-570.md), [CLAIM-592](../claims.d/CLAIM-592.md): illustrative.** The gel
  separates by compactness only within a condition; TEM refines it but
  cannot tell incomplete folding from staining collapse. [CLAIM-572](../claims.d/CLAIM-572.md) and
  [QUESTION-374](../questions.d/QUESTION-374.md): weak, the gel run both assays and purifies.
- **[CLAIM-591](../claims.d/CLAIM-591.md), [CLAIM-184](../claims.d/CLAIM-184.md), [CLAIM-478](../claims.d/CLAIM-478.md), [CLAIM-025](../claims.d/CLAIM-025.md), [QUESTION-388](../questions.d/QUESTION-388.md), [TERM-070](../terms.d/TERM-070.md):
  nothing**; no conversion between products, no mechanism, no
  reconfiguration. [QUESTION-380](../questions.d/QUESTION-380.md): only loosely, hierarchical assembly from
  pre-folded "well-behaved" monomers as a fold-small-first strategy.
- Filed: [THEORY-tmp8xe45](../theory.d/THEORY-tmp8xe45.md). No instruction for machine-learning practice.

## Limitations

- **Per-target yields, defect statistics and six-helix-bundle data** are
  in the unread Supplementary Information or in reference 21.
- **Yield is a band fraction**; quality judged by eye, with no defect
  criterion or count.
- **No melting curves, folding temperatures or isothermal runs**; only
  ramp length is varied, so time and temperature profile are not
  separated.
- **All mechanisms are hypotheses**; the scaffold comparison is
  confounded by length and tail.
- **TEM samples only gel-purified monomers**, not the population that
  failed.
