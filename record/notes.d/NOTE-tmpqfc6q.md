---
status: Read
paper: LIT-tmpd12l0
title: 'A. baumannii PmrB oxidative-stress response memory'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the bioRxiv full-text PDF of the v1 preprint
    (10.64898/2026.04.08.717352, 6.8 MB), downloaded 2026-10-09. The main
    text through the Materials and Methods was read page by page (Abstract,
    Introduction, all eight Results subsections, Discussion, Methods);
    figures were read as rendered in the PDF. The supplementary appendix
    (Figs. S1--S16, datasets S1--S3, Tables S2--S3) is cited throughout and
    was not opened, so claims resting on appendix-only panels are flagged as
    such. The reference list was skimmed, not followed. This is an unrefereed
    preprint and is read as one.
date: '2026-10-09'
summary: >-
  An unrefereed bioRxiv preprint arguing that the PmrA/PmrB two-component
  system in Acinetobacter baumannii senses sublethal oxidative stress through
  a periplasmic histidine box coordinating a nickel cofactor, activates
  iron-sulfur repair and peroxide-scavenging genes, holds a redox-gated
  conformational switch (from simulation), and retains a 30--90 min "response
  memory" that primes cross-protection against lethal peroxide and
  antimicrobial peptides and is required for virulence in mice and
  hypervirulence in a clinical isolate.
---


# NOTE-tmpqfc6q: A. baumannii PmrB oxidative-stress response memory

## Contribution

The paper proposes that a two-component signal transduction system does three
things not previously ascribed to one together: senses oxidative stress
through a metal cofactor, and specifically a nickel cofactor held by a
histidine box in the sensor's periplasmic domain; converts single-electron
oxidation of that nickel into a conformational change that transduces the
signal; and encodes a short-lived "response memory" whereby a sublethal
priming dose keeps the pathway active after the stimulus is gone, so the cell
survives a later lethal dose of peroxide or antimicrobial peptide. It ties all
three to virulence in a mouse lung model and to hypervirulence in a clinically
isolated carbapenem-resistant strain. If it holds up, the nickel-on-histidines
oxidative sensor would be a new sensing chemistry for this protein family, and
the "response memory" would be a concrete molecular case of signal priming in
a bacterial pathogen.

## Key insight

A sensor kinase can be turned into a redox detector by hanging a redox-active
metal (Ni2+/Ni3+) on a cluster of histidines in its sensing domain: oxidation
of the metal by reactive oxygen species reshapes the domain and flips the
pathway on, and the pathway then stays on long enough (tens of minutes) to act
as a memory of a stress the cell has already seen. The single thing to retain
is the proposed mechanism "sublethal ROS oxidises a nickel cofactor on a
histidine box, which switches the sensor and primes defence for a short
window" -- and that this chain is assembled from binding assays, reporters and
simulation rather than observed end to end.

## Assumptions

- **A. baumannii lacks the conventional defences.** The whole motivation
  rests on the stated absence of RpoS, Nif and Suf homologs (Appendix dataset
  S1, not inspected here), with the Isc system as the sole Fe-S assembly
  machinery.
- **Reporter and binding assays stand in for transcription.** Gene regulation
  is argued from luciferase fusions, putative PmrA-box motifs, and EMSA, not
  from direct measurement of the native transcripts across conditions.
- **Simulation stands in for conformational measurement.** The redox switch
  and the metal pocket come from AlphaFold3 (with Fe2+ substituted for Ni2+,
  since AlphaFold3 lacks a Ni2+ ligand) and from MD with bonded metal models,
  not from an experimental structure of Ni2+/Ni3+-PmrB.
- **Finite, defined conditions.** Metal-specificity and sensing experiments
  use M9 minimal medium stripped of metal cations; the physiological Ni2+ pool
  available to PmrB in the host is not measured.

## Key results

- **PmrA/PmrB is required for oxidative-stress survival.** *pmrA*/*pmrB*/double
  nulls fail to grow under H2O2 with no defect absent stress; plasmid copies
  rescue, empty vector does not; same pattern under the NO generator spermine
  NONOate (Appendix). *oxyR* inactivation does not impair H2O2 survival,
  unlike *pmrA*. (Fig. 1B--C, Appendix Fig. S3.)
- **The effect runs through the Fenton reaction.** Ferrous chelator DP and
  ferric/ferrous chelator DFO restore the *pmrA* mutant under H2O2; thiourea
  (HO· scavenger) restores growth; streptonigrin (kills by cytoplasmic free
  Fe2+) plus H2O2 kills more, and DFO removes the WT/*pmrA* difference.
  (Fig. 1D--G.)
- **PmrA directly activates named defence genes.** Putative PmrA boxes, ~6-fold
  H2O2-induced (colistin-not-induced) luciferase from the *hscB-hscA-fdx*
  (Isc) promoter, and EMSA with competition, repeated for *ftnA* (ferritin),
  *ahpF1* (peroxidase) and *katE* (catalase); *katG* is a negative control not
  bound by PmrA. Inactivating *ahpF1*/*hscA*/*ftnA*/*katE* reduces H2O2
  survival. OxyR and PmrA are argued to be independent (OxyR represses *ahpF1*
  basally; PmrA acts only under stress). (Fig. 2.)
- **Periplasmic domain senses oxidative stress; TM domain senses colistin.** A
  periplasmic-deletion variant (PmrB1, Δ70--130) loses H2O2 survival but keeps
  colistin resistance; a TM1-deletion variant (PmrB2, Δ23--29) keeps H2O2 but
  loses colistin; both still localise to the inner membrane. (Fig. 3B--D.)
- **Four conserved histidines are required for sensing, not for colistin.**
  Ala substitution of any or all of His86/89/90/92 lowers H2O2 survival but
  not colistin resistance; a neighbouring Ser88Ala control still rescues;
  *hscA*/*ahpF1* induction is lost in the quadruple mutant (Appendix). The
  histidines are *Acinetobacter*-specific; Salmonella/Pseudomonas PmrB (no
  histidine box) cannot restore H2O2 resistance but can restore colistin
  resistance. (Fig. 3E--F, Appendix Figs. S6--S8.)
- **Nickel is the cofactor.** Ni2+ (not Co2+/Mn2+/Zn2+) supplementation raises
  *hscB-hscA-fdx* and *ahpF1* induction and raises H2O2 resistance in WT but
  not the *pmrB* null; ICP-MS and a fluorescent dye detect Ni2+ on WT purified
  periplasmic domain (aa 30--140) but not on the histidine-box mutant or BSA.
  AlphaFold3 models His89/90/92 as direct metal binders, His86 as a stabiliser.
  (Fig. 4.)
- **Oxidation is modelled as a conformational switch.** MD (apo/Ni2+/Ni3+,
  100 ns): Ni3+ raises periplasmic-domain RMSD to ~5.5 Å (~40% above apo/Ni2+
  ~4 Å) while keeping low binding-site RMSD; PCA has Ni3+ PC1 capturing 49.0%
  of variance (vs 38.3% Ni2+, 30.4% apo) with a directed initial→final path;
  differential contact maps show loop displacement at ~75--85 and expansion
  between ~70--75 and ~90--130 with compaction at ~30--50 and ~55--78, the
  histidine box at the near-zero boundary. Read as a redox-driven switch that
  preserves the coordination shell. (Fig. 5.)
- **Response memory.** Sublethal H2O2 (1--10 µM, 1 h) raises oxidative-defence
  and AMP-resistance genes (*pmrC*, *naxD*) and improves later survival to
  30 mM H2O2 and 3 µg/mL colistin, PmrA-dependent, OxyR-independent, abolished
  in the histidine-box mutant. Priming persists 30--90 min after signal
  removal; CFU counts are unchanged over that window, offered as evidence the
  decay is not dilution by division. (Figs. 6--7, Appendix Figs. S11--S14.)
- **Virulence and clinical relevance.** Intratracheal mouse infection: *pmrB*
  mutant → less lung inflammation, fewer neutrophils (Ly6gCre;R26LSL-Tomato
  reporter), lower lung CFU; WT PmrB restores, the histidine-box mutant does
  not. Priming raises *pmrC* and LL-37 survival PmrA-dependently; survival in
  J774A.1 macrophages needs *pmrA*/*pmrB* and the histidine box. The histidine
  box is present in hypervirulent CRAB A0062 and absent in low-virulence
  A0075; A0075 is killed by 30 mM H2O2 while A0062 resists up to 120 mM;
  *pmrB* disruption in A0062 removes priming-dependent survival. (Figs. 8--9.)

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | PmrA/PmrB, not OxyR/RpoS, is the principal regulator of oxidative-stress defence in *A. baumannii*, acting by lowering Fenton-reaction damage | moderate | knockout/complementation + chelator/scavenger epistasis (Figs. 1--2); genetic/pharmacological, not a direct ROS measurement |
| C2 | PmrA directly activates *hscB-hscA-fdx*, *ftnA*, *ahpF1*, *katE* under oxidative stress | moderate | reporters + EMSA with competition (Fig. 2); in-vitro binding and fusions, not native-transcript profiling |
| C3 | Four periplasmic histidines (His86/89/90/92) are required for oxidative but not colistin sensing | moderate-to-strong | domain and point mutants, cross-species swaps (Fig. 3, Appendix) |
| C4 | PmrB uses a Ni2+ cofactor on the histidine box to sense oxidative stress | moderate | Ni2+-specific induction/survival, ICP-MS/dye on purified domain, AlphaFold3 model (Fig. 4); cofactor identity rests on correlative detection + modelling, no holo structure |
| C5 | Single-electron oxidation Ni2+→Ni3+ drives a directional conformational switch of PmrB | weak-to-moderate | MD + PCA + contact maps (Fig. 5); entirely in silico |
| C6 | Sublethal ROS leaves a 30--90 min PmrA/histidine-box-dependent "response memory" that primes cross-protection, not explained by growth dilution | moderate | priming reporters/survival + CFU control (Figs. 6--7) |
| C7 | Oxidative sensing via the histidine box is required for virulence in mice and for hypervirulence in clinical CRAB | moderate | mouse burden/inflammation + two clinical isolates + one insertional mutant (Figs. 8--9); small clinical sample |

## Method

Bacterial genetics in *A. baumannii* ATCC 17978 (λ-Red/FLP chromosomal
deletions, plasmid complementation in trans, 3xFLAG tagging); luciferase
reporter fusions in defined M9 medium with/without metal cations; EMSA with
purified PmrA and competitor DNA; purification of the PmrB periplasmic domain
for ICP-MS and fluorescent Ni2+ detection; subcellular fractionation via NADH
for localisation; structure prediction with AlphaFold3 (Fe2+ as Ni2+ proxy);
MD of apo/Ni2+/Ni3+ PmrB with bonded metal models (RMSD, RMSF, SASA, radius of
gyration, PCA, differential contact maps); priming/memory assays (sublethal
H2O2 then lethal H2O2 or colistin, with CFU controls); intratracheal mouse
infection with neutrophil-reporter imaging; macrophage (J774A.1) survival; and
assays on clinical isolates A0062 (hypervirulent CRAB) and A0075
(low-virulence).

## Concepts

- **response memory** -- a signalling state that stays "on" after the initiating
  signal is removed, priming a stronger response to a later signal; here a
  30--90 min window following sublethal ROS.
- **histidine box** -- four conserved periplasmic histidines (His86/89/90/92)
  of *Acinetobacter* PmrB, proposed to coordinate the nickel cofactor.
- **standard (sublethal) priming dose** -- 1--10 µM H2O2, said to match
  bloodstream/airway ROS levels at initial infection sites.

## Connections

The paper positions PmrA/PmrB against the canonical OxyR/RpoS oxidative-stress
regulators and against Salmonella/Pseudomonas PmrB (which confer colistin
resistance but, lacking the histidine box, no oxidative sensing). It likens
the proposed Ni-on-histidines redox switch to the Fe2+-on-histidines sensing
of *Bacillus* PerR, and the "response memory" to IFN-γ priming of mammalian
immune cells. Machine-readable lineage belongs on the LIT, not here.

## Bearing on the record

- **[THEORY-136](../theory.d/THEORY-136.md)** (Active) is the entry this reading most directly touches.
  [THEORY-136](../theory.d/THEORY-136.md) holds that a lasting or abrupt change is weak evidence for a
  system with alternative stable states, and that only hysteresis,
  initial-state dependence, or a lasting shift after a temporary disturbance
  with slow return excluded comes close to showing one. The paper's "response
  memory" is precisely a lasting-shift-after-temporary-disturbance claim, and
  it supplies one control [THEORY-136](../theory.d/THEORY-136.md) asks for -- CFU unchanged over the memory
  window, excluding dilution-by-division -- while not demonstrating bistability
  or true hysteresis (no initial-state-dependence test, no dose loop). So it is
  a biological instance that meets [THEORY-136](../theory.d/THEORY-136.md)'s bar only partway: evidence of a
  persistent response, not yet of an alternative stable state.
- **[THEORY-058](../theory.d/THEORY-058.md)** (Proposed) -- mental disorders maintained by self-reinforcing
  loops that let them outlast their triggers -- is a looser analogue: a
  response that outlasts its cause through pathway-internal dynamics rather
  than a sustained driver. The connection is conceptual, cross-domain, and does
  not change that THEORY.
- **[THEORY-130](../theory.d/THEORY-130.md)** (coral bleaching as breakdown of a host-symbiont exchange
  under oxidative stress) shares the vocabulary of oxidative stress in a
  host-associated organism but concerns a different system and mechanism; no
  real bearing.
- **No THEORY is filed from this reading.** The claim one would state -- that a
  bacterial TCS encodes an oxidative-stress memory via a nickel-histidine
  switch -- rests on a single unrefereed preprint whose mechanism is assembled
  from reporters, correlative metal detection and simulation, and is exactly
  the kind of persistence claim [THEORY-136](../theory.d/THEORY-136.md) counsels holding at arm's length.
- No instruction for machine-learning practice; nothing for the anthology.
  AlphaFold3, MD and PCA appear only as analysis tools.

## Limitations

- **Mechanism not observed end to end.** No holo structure of Ni2+- or
  Ni3+-PmrB; the cofactor identity is correlative (ICP-MS, dye) plus an
  AlphaFold3 model that substitutes Fe2+ for Ni2+; the redox switch is wholly
  in silico (100 ns MD, single system each).
- **Regulation inferred from reporters and in-vitro binding,** not native
  transcript measurement across the regulon.
- **Short and narrow memory evidence.** 30--90 min window; no
  initial-state-dependence or reversibility/hysteresis experiment; the
  dilution control addresses only one alternative explanation.
- **Thin clinical base.** Two clinical isolates and one insertional mutant
  underwrite the hypervirulence-determinant claim; histidine-box
  presence/absence is correlated with virulence across a tiny sample.
- **Unrefereed.** Not peer reviewed; figures read as rendered in the PDF;
  appendix figures and datasets S1--S3 underpinning several statements
  (absence of RpoS/Nif/Suf, metal specificity, localisation) were not opened.

## Open questions

- A holo structure (or spectroscopy) of Ni-bound PmrB and a direct redox
  measurement of the Ni2+→Ni3+ transition in the protein -- would convert C4--C5
  from correlative/computational to shown.
- A hysteresis or initial-state-dependence experiment on the response memory --
  would decide whether it is bistability (an alternative stable state, in
  [THEORY-136](../theory.d/THEORY-136.md)'s sense) or slow relaxation.
- Native-transcript profiling of the PmrA regulon under graded ROS -- would
  test C2 beyond reporters and EMSA.
- Whether the histidine box is a general virulence determinant across clinical
  *Acinetobacter* -- needs more than two isolates.
