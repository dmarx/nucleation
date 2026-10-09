---
number: 657
status: Read
formerly:
- NOTE-tmpwvklq
paper: 'LIT-853'
title: 'Bhattacharyya et al. 2023, heritable iron memory in E. coli'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the PubMed Central copy of the version of record
    (PMC10691332, fetched as Europe PMC full-text XML): Significance,
    abstract, Introduction, Results, Discussion, Methods and every figure
    caption. From the SI Appendix (Europe PMC supplementary bundle,
    pnas.2309082120.sapp.pdf): the SI Methods in full, including the
    mathematical model and the fitting procedure, the noise F-test and the
    PCA; Tables S1–S2 and Figs. S1–S11 were not examined. Fig. 4 was viewed
    as an image for the correlation statistics; Figs. 1–3 and 5 were read
    from their captions and the text only. The reference list was not read.
date: '2026-10-09'
summary: >-
  In genetically identical E. coli, a single cell's swarming potential is
  shared by its descendants for about four generations and lost by seven;
  it tracks the cell's iron status as read by a Fur-repressed reporter
  (low iron, better swarmer), iron manipulation lengthens it, and a
  three-class switching model fits the lineages only if each founding cell
  holds its class for a fixed delay before switching. The iron link is a
  correlation through a promoter reporter, and the model is fitted to two
  time points.
---

<!-- inactive-ok-file: THEORY-179 — Proposed; the finding this reading produces, filed with it -->

# NOTE-657: Bhattacharyya et al. 2023, heritable iron memory in E. coli

## Contribution

It shows, in single-cell swarm assays, that the heterogeneity in swarming
among genetically identical E. coli cells is not noise renewed each
generation: a cell's swarming class is shared by its descendants for about
four generations and dissipates by seven. It identifies the cell's iron
status, read through the Fur regulon, as the variable that carries the
state, and shows that pushing iron down or up lengthens how long the state
is kept. It adds a phenomenological model in which the state is held for a
fixed time before switching, rather than switched at a constant rate.

## Key insight

A physiological quantity that is diluted, rebuilt and regulated slowly
across divisions, here the cell's iron pool and the Fur-controlled uptake
machinery, acts as a short inherited state. It does not need a bistable
switch or an epigenetic mark: it is a slow variable, so a lineage keeps the
founder's value for a few divisions and then relaxes back to the population
distribution. Pinning the variable (chelator, added iron, a mutant that
cannot import) pins the behaviour for longer.

## Assumptions

- **Strain and conditions.** E. coli MG1655; swarm plates of 0.45% Eiken
  agar with 0.5% glucose, dried 8 h, inoculated with 4 μL and read at 30 h
  at 30 °C; swarm diameter measured by ruler as the maximum diameter.
- **Single cells by dilution to extinction.** A suspension targeted at 0.5
  cells per 4 μL; Poisson sampling puts a cell on about 40% of plates and
  more than one on about 5%, which are excluded by counting nucleation
  centres. At least 120 plates for 50 swarms per assay.
- **Generations by timing.** G4, G7 and G12 are harvest times in 96-well
  plates calibrated by CFU counts, not observed divisions; sixteen
  daughters per mother are expected at G4 and sampled singly at later
  generations.
- **Iron is read, not measured.** The biosensor is sfGFP on a plasmid
  behind the fepA promoter, which Fur represses when iron is high. It
  reports Fur derepression; plasmid copy-number variation is controlled
  only by a constitutive Ptrc-sfGFP comparison.
- **Model.** Equal proliferation rates in all three classes, so fractions
  can be modelled instead of counts.

## Key results

- **Fig. 1.** Swarm-derived colonies on moist hard agar are less circular
  and larger than planktonic ones (n = 218, Mann–Whitney P < 0.0001); about
  20% of planktonic colonies look swarm-like. Single-cell inocula show
  significantly higher coefficient of variation in swarm diameter than
  100- and 10,000-cell inocula in each of three zone-adjusted comparisons
  (F-tests), most in the outer zone.
- **Fig. 2 (about 1,700 plates).** Planktonic G0 mothers vary; the 16 G4
  daughters of each mother are homogeneous, and K-means on the column
  means gives three classes, XS, M and L; by G7 within-sibling variability
  returns. Swarm-edge mothers are uniform at G0, give one class (L) at G4
  with lower noise, and lose it by G7. Mothers from hard agar behave like
  planktonic ones (Fig. S3B).
- **Fig. 3 (about 2,400 plates).** No environmental perturbation changes
  the variability; of the plasmid-expressed genes only fepA and fur do
  (PCA over mean, SD and noise, PC1 60.06%). DFO shifts the distribution to
  better swarming, FeCl₃ to worse; neither affects ΔfepA. DFO-treated
  lineages keep their class to G7 (lost by G12); fepA overexpression keeps
  the poor-swarming class to G12, the last generation tested.
- **Fig. 4.** Reporter signal vs swarm diameter in sorted G0 cells:
  Spearman r = 0.7067, p = 8.66 × 10⁻¹⁶ (WT/PfepA-sfGFP; exponential fit
  R² = 0.5996); r = 0.1506, p = 0.14 (WT/Ptrc-sfGFP); r = 0.0507,
  p = 0.5965 (ΔfepA/PfepA-sfGFP). Five sorted mothers per strain followed:
  in WT/PfepA the G4 daughters follow the mother's reporter level, and by
  G7 they do not; ΔfepA, uniformly low in iron, keeps its class to G7.
- **SI model.** df_XS/dt = −k_{XS→M} f_XS + k_{M→XS} f_M;
  df_M/dt = k_{XS→M} f_XS − (k_{M→XS} + k_{M→L}) f_M + k_{L→M} f_L;
  df_L/dt = −k_{L→M} f_L + k_{M→L} f_M, with time in generations.
  Steady state is fixed at 52% XS, 35% M, 13% L by k_{M→XS} = 1.49 k_{XS→M}
  and k_{M→L} = 0.37 k_{L→M}. The founding cell's outgoing rates are zero
  until τ. Least-squares fit (Excel Solver) to G4 data and the G7 steady
  state gives τ_XS, τ_M ≈ 3, τ_L ≈ 4 generations, k_{XS→M} ≈ 0.4,
  k_{L→M} = 1.8 per generation.
- **SI Fig. S11.** Reporter signal correlates with biofilm (crystal violet;
  more iron, more biofilm) and with survival after 4 h at about half-MIC
  kanamycin or chloramphenicol (less iron, better survival), not in the
  controls. These are G0 measurements only.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Genetically identical planktonic E. coli cells differ in swarming potential more than population inocula reveal | strong | Fig. 1, many single-cell assays with F-tests on the coefficient of variation |
| C2 | A cell's swarming class is shared by its fourth-generation descendants and lost by the seventh, in planktonic and swarm-derived cells alike | moderate | Fig. 2, 25 mothers per condition, three harvest times only |
| C3 | Prior swarming makes the founding cells uniform good swarmers; growth on hard agar does not | moderate | Fig. 2C, E; Fig. S3B |
| C4 | Iron status is the variable that carries the state | moderate | only fepA and fur among ten genes alter variability (Fig. 3A–B); iron manipulation shifts and prolongs it (Fig. 3C–E); reporter correlation (Fig. 4E). Correlational and through a Fur reporter; no direct iron measurement |
| C5 | Daughters' swarming follows the mother's iron status at G4 | weak to moderate | Fig. 4F–G, five sorted mothers per strain |
| C6 | Constant-rate (memoryless) switching cannot reproduce the lineage data; a fixed holding delay is needed | weak | asserted from the model fit; no fit of the delay-free model is reported, and five parameters are fitted to G4 and G7 |
| C7 | Iron status also predicts biofilm formation and antibiotic survival | moderate (G0 correlation) | Fig. S11; inheritance of these was not tested |
| C8 | The memory is a bet-hedging strategy and likely widespread; "iron memory impacts all iron-controlled behaviors" | speculative | Discussion, no test |

## Method

Dilution to extinction gives single cells, which are either plated directly
on swarm agar or grown in 96-well plates to a calibrated generation and
their daughters plated singly. Swarm diameter (and, for clustering, total
pixel intensity) is the read-out; noise is the coefficient of variation,
compared by an F-test. Candidate carriers are screened by environmental and
plasmid perturbations and a PCA of mean, SD and noise. Cells are then
sorted by the Fur-reporter signal (FACS) into single wells, and each sorted
mother's own swarm, or its G4/G7 daughters' swarms, are scored against its
reporter level. The lineage data are summarised by a three-class linear
switching model with class-specific holding delays.

## Concepts

- **memory**: here, any heritable non-genetic carry-over of a cell's
  swarming potential across divisions. Used throughout as a functional
  label, not with a claim about storage and retrieval beyond persistence.
- **iron memory**: the authors' name for that carry-over once identified
  with intracellular iron status as reported by the Fur regulon.
- **conditioning**: prior swarming, which leaves cells uniformly in the
  good-swarming class. Borrowed from the vocabulary of associative
  learning; no stimulus–response association is tested.
- **decision-making**: the choice of when to start swarming and how well to
  swarm on a new surface. Not a model of choice among options.
- **SCI**: single-cell inoculum swarm assay.
- **XS, M, L**: swarm diameter under 35 mm, 35–65 mm and over 65 mm.

## Connections

It builds on the observation, from the Harshey laboratory's earlier work,
that swarm-derived cells start swarming after a shorter lag, and on the
known role of iron starvation as a swarming signal and of Fur as the
repressor of iron uptake. It places itself among bacterial memory
mechanisms that are stimulus-specific (fimbrial phase variation,
chemotaxis adaptation, the motile–sessile switch) and claims a different
kind, a state reached by several stimuli. It explicitly sets aside
bistable and toggle switches and epigenetic inheritance because the memory
lasts only a few generations, and invokes stochastic gene-expression noise
and dilution of Fe–S proteins at division instead.

## Bearing on the record

- **New THEORY.** The record held no account of non-genetic,
  multigenerational state in single bacteria from experiment. This
  reading produces [THEORY-179](../theory.d/THEORY-179.md), stating the finding (a slow
  physiological variable carries a cell's behavioural state for about four
  generations), with what the evidence does not reach.
- **Against the record's other bacterial-memory reading.** *Irreversibility
  in bacterial regulatory networks* (Zhao et al. 2024, filed the same day)
  argues from Boolean models that a transient perturbation can leave the
  E. coli regulatory network in a different self-maintaining attractor.
  This paper is the opposite case, read in cells: a heritable state that is
  not self-maintaining, decays in about seven generations, and is
  explicitly not a bistable switch. It is not evidence for that account;
  it shows that a few generations of inheritance do not by themselves
  indicate an alternative stable state. My connection, not the paper's.
- **[THEORY-136](../theory.d/THEORY-136.md)** (a persistent or abrupt change is not evidence of
  alternative stable states). The same lesson at the cellular scale: the
  persistence here is explained by a slow variable relaxing, and the
  authors reject multistability. My connection; it does not change that
  THEORY.
- **The word "memory".** Readings in the record that weigh claims of
  memory, learning or cognition in organisms without nervous systems
  should take this paper's "memory", "conditioning" and "decision-making"
  as functional labels for persistence of a physiological state. Nothing in
  it bears on learning in the sense of the `learning-and-conditioning`
  tag.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **The iron link is correlational and indirect.** No intracellular iron
  is measured; the reporter reads Fur-repressed transcription from a
  multicopy plasmid. The strongest evidence (Fig. 4E) is one strain's
  correlation over about 96 cells.
- **Inheritance rests on few founders and three time points.** 25 mothers
  per condition in Fig. 2, five sorted mothers per strain in Fig. 4, and
  only G0, G4, G7 (and G12) were sampled, so "lost by the seventh" is
  "lost at the seventh time point tested". Generations are inferred from
  timing, not observed.
- **The delay claim is weakly supported.** The model has five fitted
  parameters for data at two time points, with steady-state fractions
  imposed; the comparison with a delay-free model is asserted, not shown.
  The authors say three classes may stand in for a continuum.
- **Biofilm and antibiotic links** are single-generation correlations.
- **Some figure-level details** (the hard-agar control, the noise per
  mother, the growth/motility clustering) are in SI figures not examined
  here.
- The bet-hedging interpretation and the claim that the mechanism is
  general are not tested.

## Open questions

- Does the state follow iron itself? A direct single-cell iron measurement
  (or a chromosomal reporter of a second Fur target) correlated with swarm
  outcome would separate iron from Fur-promoter or plasmid effects.
- Is the decay a fixed holding time or a slow continuous relaxation?
  Lineages sampled at every generation, with the delay-free and delayed
  models both fitted, would decide it.
- Is swarm-edge "conditioning" more than selection of low-iron cells that
  happened to reach the edge? Tracking iron status of the same cells before
  and after swarming would answer it.
- Do biofilm propensity and antibiotic tolerance inherit on the same
  four-generation timescale?
