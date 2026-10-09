---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmpqfc6q](../notes.d/NOTE-tmpqfc6q.md)) from the bioRxiv full-text PDF of the v1 preprint. An unrefereed preprint: worth keeping as a clean biological instance of the ``memory from a temporary signal'''' pattern that THEORY-136 sets the evidential bar for, and as a self-contained worked example of a two-component signalling system (PmrA/PmrB) that is claimed to sense oxidative stress through a histidine box with a nickel cofactor, to hold a redox-gated conformational switch, and to retain a 30--90 minute ``response memory'''' after the stimulus is removed. Read for what it shows, not for what a manuscript might use it for; its central memory and virulence claims rest on this single unreviewed study.'
title: 'A sensor of oxidative stress confers virulence via response memory in Acinetobacter baumannii'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full on 2026-10-09 (NOTE-tmpqfc6q) from the bioRxiv full-text
    PDF (27 pp. main text through Materials and Methods; figures as rendered
    in the PDF, supplementary appendix figures/datasets referenced but not
    opened). Identity verified before reading: Crossref
    (api.crossref.org/works/10.64898/2026.04.08.717352) returns the work
    with publisher "openRxiv", institution "bioRxiv", type posted-content,
    posted 2026-04-09, licence CC-BY 4.0; the bioRxiv API
    (api.biorxiv.org/details/biorxiv/10.64898/2026.04.08.717352) returns the
    same record (version 1, category microbiology, corresponding author Jinki
    Yeom); doi.org/10.64898/2026.04.08.717352 resolves (302). The DOI prefix
    is 10.64898, not bioRxiv's historical 10.1101: openRxiv now registers
    bioRxiv DOIs under its own prefix, and 10.64898/2026.04.08.717352 is what
    resolves. `published:` is 2026-04-09, the posted date. Not held in the
    Anthology of the SOTA: a grep of its record/ (clone of 2026-10-09, commit
    d8b5ba5, which may be stale) for the authors, the DOI and the title found
    nothing.
tags:
- natural-sciences
- complex-systems
date: '2026-10-09'
published: '2026-04-09'
doi: '10.64898/2026.04.08.717352'
first_author: 'Ngo'
keywords:
- 'two-component system'
- 'PmrA/PmrB'
- 'oxidative stress sensing'
- 'response memory'
- 'nickel cofactor'
- 'histidine box'
- 'Acinetobacter baumannii'
- 'virulence'
- 'antimicrobial peptide resistance'
implementations: []
summary: >-
  Ngo et al. (2026), bioRxiv 10.64898/2026.04.08.717352 (preprint, not peer
  reviewed). Reports that the PmrB sensor of the PmrA/PmrB two-component
  system in Acinetobacter baumannii detects sublethal oxidative stress via
  four periplasmic histidine residues coordinating a nickel cofactor; PmrA
  then activates iron-sulfur repair, a ferritin, a catalase and a
  peroxidase. The sensor is claimed to stay active 30--90 min after the
  stimulus is removed (a "response memory"), priming cross-protection
  against lethal peroxide and antimicrobial peptides, and the histidine box
  is reported necessary for virulence in mice and for hypervirulence in a
  clinical carbapenem-resistant isolate.
---


# LIT-tmpd12l0: A sensor of oxidative stress confers virulence via response memory in Acinetobacter baumannii

Hoan Van Ngo, Seung Hyeon Kim, Hongseok Ha, Sangwoo Kang, Donghyuk Shin,
Matthias Gunzer, Kiwook Kim, Jinki Yeom (2026), *bioRxiv* — DOI
10.64898/2026.04.08.717352 (v1, posted 9 April 2026, CC-BY 4.0). **An
unrefereed preprint.**

## Key takeaways

- **A two-component system is cast as an oxidative-stress sensor.** The paper
  argues that *A. baumannii*, which lacks RpoS, Nif and Suf homologs, defends
  against peroxide and nitric-oxide stress through the PmrA/PmrB TCS rather
  than through the usual regulators. The support is genetic and reporter-based:
  *pmrA*/*pmrB* nulls fail to grow under H2O2, plasmid-borne copies rescue,
  and iron chelators (DP, DFO) and a hydroxyl-radical scavenger (thiourea)
  restore the mutant, placing the effect on the Fenton reaction. OxyR
  inactivation does not phenocopy, so the two pathways are presented as
  independent.
- **PmrA is placed directly upstream of concrete defence genes.** Putative
  PmrA boxes, luciferase reporters induced by H2O2 (but not by colistin), and
  EMSA binding (competed out by unlabelled promoter) are given for the
  *hscB-hscA-fdx* Isc operon, the ferritin *ftnA*, the peroxidase *ahpF1* and
  the catalase *katE*; *katG* is a stated negative control. This is a
  promoter-binding and reporter argument, not direct in-vivo transcription
  across the regulon.
- **The sensing chemistry is the novel claim: a nickel cofactor on a histidine
  box.** Four conserved periplasmic histidines (His86/89/90/92), specific to
  *Acinetobacter*, are required for H2O2 survival but not colistin resistance;
  Ni2+ (not Co2+/Mn2+/Zn2+) supplementation boosts the response; ICP-MS and a
  fluorescent dye detect Ni2+ on wild-type but not histidine-substituted
  purified periplasmic domain; AlphaFold3 (with Fe2+ as a Ni2+ proxy) models
  the histidines forming a metal pocket. This is presented as the first report
  of a TCS sensor using a Ni2+ cofactor with multiple histidines for oxidative
  sensing.
- **A redox switch is argued from simulation, not measured conformations.**
  Molecular-dynamics runs (apo, Ni2+, Ni3+, 100 ns) report that oxidising the
  bound nickel to Ni3+ expands the periplasmic domain (RMSD ~5.5 Å vs ~4 Å)
  while keeping tight local histidine-box geometry; PCA and differential
  contact maps are read as a dominant, directional conformational transition.
  The switch is a computational inference.
- **"Response memory" is the headline concept.** Priming with sublethal H2O2
  (1--10 µM) is reported to raise both oxidative-defence and antimicrobial-
  peptide-resistance genes and to improve later survival to 30 mM H2O2 and to
  colistin, PmrA- and histidine-box-dependent and OxyR-independent. The effect
  is said to last 30--90 min after signal removal, with CFU counts offered to
  rule out dilution by division as the explanation for its decay.
- **Host and clinical claims.** Intratracheally infected mice show less lung
  inflammation, fewer neutrophils and lower bacterial burden with the *pmrB*
  mutant and with the histidine-box substitution; the histidine box is present
  in a hypervirulent carbapenem-resistant clinical isolate (A0062) and absent
  in a low-virulence one (A0075), and *pmrB* disruption in A0062 reduces
  priming-dependent survival.

The record's reading of what is shown versus asserted, and the reasons for
caution, are in [NOTE-tmpqfc6q](../notes.d/NOTE-tmpqfc6q.md). In short: the mechanistic chain (Ni2+ binding →
oxidation → conformational switch → signalling) is assembled from binding
assays, reporters and simulation rather than observed end to end, and the
central "memory" and virulence claims rest on this one unrefereed study.

## Standing in the record

Filed on 2026-10-09 at the owner's request, who asked for this preprint to be
registered and read, with no stated context. It is read on its own merits.
Because it is an unrefereed bioRxiv preprint, the reading separates what the
experiments show from what the authors claim, and treats the mechanism and the
host/clinical conclusions as not yet independently established.

The reading bears on [THEORY-136](../theory.d/THEORY-136.md), the record's statement that a lasting change
after a temporary disturbance is only weak evidence for a system with
alternative stable states unless hysteresis, initial-state dependence or a
lasting shift with slow return excluded is shown. This paper's "response
memory" is exactly such a lasting-shift claim, and it supplies the
dilution-excluding control [THEORY-136](../theory.d/THEORY-136.md) asks for (CFU unchanged over the memory
window) while stopping short of demonstrating true bistability. No THEORY is
filed from this reading: the account is a single unrefereed study, and the
claim it would state is the one [THEORY-136](../theory.d/THEORY-136.md) counsels holding at arm's length.

Not held in the Anthology of the SOTA. The paper uses AlphaFold3, MD and PCA
as tools but makes no machine-learning-practice claim, so it carries no
`anthology-candidate` flag.
