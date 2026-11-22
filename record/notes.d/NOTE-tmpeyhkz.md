---
status: Read
paper: LIT-2462
title: 'Peng et al. Immunity 2025 on NIMA tolerance sustained by LysM CD11c maternal microchimeric cells'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read in full on 2026-11-22 for LEAD-051, from the NIH Public Access
    author manuscript (nihpa) served as JATS XML by the NCBI E-utilities
    efetch interface (db=pmc, id=12412910), a documented machine interface
    (ADR-101). Abstract, Introduction, Results, Discussion and STAR Methods
    were read; the figures themselves (S1-S7 and Figures 1-7) were not
    rendered, only their text references. Prior routes still fail on
    2026-11-22: Europe PMC REST fullTextXML HTTP 500, NCBI PMC OA service
    HTTP 404, the publisher PDF refused by this session's permission
    classifier (NOTE-1763 records the 2026-11-12 reCAPTCHA/Cloudflare/403).
date: '2026-11-22'
summary: >-
  The paper behind [THEORY-1658](../theory.d/THEORY-1658.md), read for [LEAD-051](../leads.d/LEAD-051.md). In mice, a conditional
  depletion platform (maternal-only Cre-driven diphtheria-toxin receptor)
  shows noninherited-maternal-antigen (NIMA) tolerance is sustained only by
  maternal microchimeric cells co-expressing LysM, CD11c and Vav1, and that
  depleting that subset erases the tolerance without lowering overall
  maternal microchimerism, dissociating the tolerance from the cells'
  persistence.
---

<!-- inactive-ok-file: THEORY-1658 CLAIM-659 ARG-090 — Proposed; the account, claim and argument this reading bears on -->
<!-- inactive-ok-file: CASE-tmpmkc5v — new; the comparison specified from this reading in the same change -->

# NOTE-tmpeyhkz: Peng et al. Immunity 2025 on NIMA tolerance sustained by LysM CD11c maternal microchimeric cells

## Contribution

Before this, maternal microchimeric cells (MMc) were known to be collectively
necessary for a child's tolerance of the maternal antigens it did not inherit
(NIMA), but which MMc and whether presence and function were the same thing
were open, because the cells are too rare (<1 in 10^5-10^6) and heterogeneous
to manipulate. The paper builds a platform that depletes MMc of any chosen
cell lineage in the offspring on demand (Cre-restricted diphtheria-toxin
receptor expressed only by maternal cells, depleted by diphtheria toxin), and
uses it to show NIMA tolerance is carried by one small subset (LysM+ CD11c+
Vav1+ leukocytes) and that erasing the tolerance does not erase the
microchimerism.

## Key insight

Presence and function of foreign-origin cells in a host come apart by
intervention: a small marked subset does the tolerogenic work, and the rest of
the maternal cells persist without it and without that work. Tolerance and
persistence are separately regulated.

## Key results

- **Complete MMc depletion overturns NIMA tolerance** (Results, "DT-induced
  MMc depletion overrides NIMA-specific tolerance"; Figure 2). In offspring
  whose MMc all express the receptor (via constitutive βactin-Cre), diphtheria
  toxin drives OVA+ maternal DNA below detection across tissues (Figure 1B,C)
  and collapses NIMA-2W1S-specific FOXP3+ regulatory T-cell expansion to naive
  levels; it also overturns cross-generational resiliency against
  infection-induced fetal wastage in NIMA-matched allogeneic pregnancy.
- **The capacity narrows to Vav1+ leukocytes** (Figure 3). Depleting maternal
  microchimerism in Vav1+ leukocytes/endothelial cells erases both readouts;
  depleting K14+ epithelial or Cdh5+ endothelial MMc does not. Endothelial
  (Cdh5) depletion being inert localizes the requirement to Vav1+ leukocytes.
- **Within leukocytes, LysM+ myeloid and CD11c+ dendritic cells are each
  essential; lymphocytes are not** (Figures 4-5). hCD2+ (B and T) lymphocyte
  depletion overturns neither readout (and is verified efficient, Figure 6);
  LysM-Cre and CD11c-Cre depletion each overturns both. Hence "LysM+ CD11c+
  Vav1+."
- **Tolerance is dissociated from persistence** (Results, "Persistent maternal
  microchimerism despite loss of NIMA-specific tolerance"; Figure 7).
  "loss of only the limited microchimeric cell types that promote NIMA-specific
  tolerance phenotypes does not significantly impact overall MMc levels,
  supporting a model where microchimeric cells persist autonomously, and
  through mechanisms independent from expanded NIMA-specific FOXP3+ Treg cells".

## Assumptions

- A surrogate-antigen system: maternal cells are engineered to express a model
  antigen (OVA:2W1S, or H2d treated as a surrogate NIMA) so the rare cells and
  the antigen-specific T cells can be quantified (OVA+ qPCR; I-Ab:2W1S tetramer
  enrichment). The NIMA whose tolerance is studied is this surrogate.
- The depletion handle is receptor-mediated killing by diphtheria toxin, with
  maternal-only receptor expression achieved by a three-generation breeding
  scheme; efficiency is verified by loss of OVA+ maternal DNA.
- The functional readouts are FOXP3+ Treg expansion and resiliency against
  *Listeria*-induced fetal wastage; the authors note these "require ongoing MMc
  stimulation" (Discussion).

## Concepts

- **NIMA** — noninherited maternal antigen: a maternal allele/antigen the child
  did not inherit but was exposed to developmentally, and is tolerant of.
- **Maternal microchimerism (MMc)** — maternal-origin cells persisting in the
  offspring.
- **Tolerogenic MMc subset** — as defined here, maternal cells co-expressing
  LysM, CD11c and Vav1.

## Connections

Extends the laboratory's antibody-based MMc-depletion work (refs 29, 30 in the
paper) by making depletion cell-lineage-specific and conditional. Within the
record it is the paper behind the press post read in [NOTE-1763](NOTE-1763.md) ([LIT-2428](../literature.d/LIT-2428.md)) and
the finer, same-laboratory result flagged in [NOTE-1728](NOTE-1728.md) (Kinder et al.,
[LIT-2348](../literature.d/LIT-2348.md)).

## Bearing on the record

- **[THEORY-1658](../theory.d/THEORY-1658.md)** (the account, Proposed): the reading confirms both halves of
  its promote_when verbatim — depletion of LysM+ CD11c+ (Vav1+) MMc abolishes
  NIMA-specific tolerance (Figures 3-5) and "does not diminish overall MMc
  levels, dissociating NIMA-specific tolerance from MMc persistence" (abstract;
  Figure 7). Promotion and whether to add [LIT-2462](../literature.d/LIT-2462.md) as the account's source are
  the owner's call: this reading is not independent of the press post that
  filed [THEORY-1658](../theory.d/THEORY-1658.md) (read-and-file step 8), since both report the same study.
- **[CLAIM-659](../claims.d/CLAIM-659.md)** (microchimerism bears on graded individuality): supports the
  premise it leans on — foreign-origin cells doing regulatory work in a host,
  established by intervention, not mere coexistence. The Discussion's closing
  line is apt: individuals are "constitutively chimeric ... phenotypically
  distinct microchimeric cells that defy our current immunological framework
  defining antigens based on binary self versus non-self distinction". Leaves
  gradedness of individuality untouched, as [ARG-090](../arguments.d/ARG-090.md) already holds.
- **[CLAIM-530](../claims.d/CLAIM-530.md)** and **[QUESTION-086](../questions.d/QUESTION-086.md)**: the reading supplies the concrete handles
  (identified tolerogenic subset, DTR/DT depletion, Treg and fetal-wastage
  readouts, the "ongoing stimulation" requirement, and autonomous persistence)
  that let the own-cell-vs-donor-cell comparison be specified; it is written up
  as [CASE-tmpmkc5v](../cases.d/CASE-tmpmkc5v.md).

## Limitations

- Mouse only, and the NIMA is a surrogate (engineered OVA:2W1S / H2d); the
  authors do not claim it holds in humans.
- The qPCR MMc marker is less sensitive than the depletion: after LysM+ MMc
  depletion, residual myeloid MMc were still detected in only ~30% of mice, a
  discordance the authors attribute to assay sensitivity, not to MMc regrowth.
- "Persist autonomously" is inferred from undiminished overall MMc levels after
  depleting the tolerogenic subset; the mechanism of autonomous persistence is
  explicitly left open ("how this works remains uncertain").
- Figures were read through their text descriptions only; the panels were not
  rendered.

## Open questions

- By what mechanism MMc persist independently of NIMA-specific tolerance
  (the authors' own open question).
- Whether a once-supplied, matched tolerogenic cell population (a donor source
  of the same function) sustains tolerance and responds to the same depletion
  and stimulation interventions as the host's own MMc — the comparison
  [CASE-tmpmkc5v](../cases.d/CASE-tmpmkc5v.md) specifies.
