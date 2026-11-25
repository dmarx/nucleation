---
number: 168
status: Proposed
formerly:
- CASE-tmpa087v
title: 'Monocercomonoides'
statement: >-
  Monocercomonoides: a eukaryote that lost its mitochondrion entirely after
  the organelle's essential jobs were removed in steps, its Fe–S cluster
  assembly taken over by a bacterial-type SUF system that its relatives
  share and its glycine cleavage system lost, and kept canonical eukaryotic
  complexity
version: 4
history:
- version: 2
  date: '2026-10-27'
  note: >-
    Note of 2026-10-27 (batch 2) added from the reading of LIT-1574, which corrects the case's account of what made the organelle dispensable. The title is revised; version 1's title was 'Monocercomonoides: a eukaryote that lost its mitochondrion entirely once a bacterial Fe–S system acquired by lateral transfer replaced the organelle''s one indispensable job, and kept canonical eukaryotic complexity'.
- version: 3
  date: '2026-11-11'
  note: >-
    Bears on QUESTION-277, now that a case can carry `bears_on`
    (ADR-092); added as that decision's demonstration. Its text cites the question: As A2 put it, "losing genetic information is not equivalent to losing function, losing autonomy, or increasing integration" (QUESTION-277). No line changes
    (ADR-085). No other change.
- version: 4
  date: '2026-11-22'
  note: >-
    Note of 2026-11-22 added for LEAD-138: LIT-1567 read; its four facts hold, with refinements. No other change.
standing: documented
kind: specimen
tags:
- endosymbiosis
- individuation
date: '2026-10-27'
line: distributed-agency
reported_in:
- LIT-1567
- LIT-1574
summary: >-
  The oxymonad Monocercomonoides lacks all hallmark mitochondrial proteins; its mitochondrial iron–sulfur cluster pathway was replaced by a cytosolic SUF system taken from bacteria, and the loss was secondary ([LIT-1567](../literature.d/LIT-1567.md)). Its genome otherwise shows canonical eukaryotic complexity ([LIT-1574](../literature.d/LIT-1574.md)). Used as the negative control: loss of function dissolving an integrated compartment, not deepening dependence on it.
bears_on:
- QUESTION-277
---
<!-- inactive-ok-file: THEORY-2230 — new, filed for LEAD-138; the reading the note of 2026-11-22 reports -->

# CASE-168: Monocercomonoides

## The case

The genome of the oxymonad *Monocercomonoides* ([LIT-1567](../literature.d/LIT-1567.md)) lacks every
hallmark mitochondrial protein. The mitochondrial iron–sulfur cluster
assembly pathway, thought conserved in virtually all eukaryotes, is
replaced by a cytosolic SUF system acquired by lateral gene transfer from
bacteria. Phylogeny places the organism among mitochondriate relatives, so
the loss was secondary. It is the first eukaryote known to lack any form of
mitochondrion.

The full analysis of *M. exilis* ([LIT-1574](../literature.d/LIT-1574.md)) finds its genome as complex as
other eukaryotes', less reduced than some related metamonads', with a
canonical cytoskeleton, endomembrane system and biosynthesis. The only
apparent preadaptations for the loss were gaining SUF and losing the glycine
cleavage system.

## What it can show

- **The same process, the opposite outcome.** Loss of function deepens a
  symbiont's dependence in the other cases. Here, once a third party's
  genes replaced the compartment's essential job, the compartment itself was
  lost. As A2 put it, "losing genetic information is not equivalent to
  losing function, losing autonomy, or increasing integration"
  ([QUESTION-277](../questions.d/QUESTION-277.md)).
- **An integration that can be undone.** A partnership as old as the
  eukaryotic cell was dissolved, so integration is not a ratchet.

Documented in works the record has not read. What it shows rests on their
abstracts until they are read.

## Note of 2026-10-27 (batch 2): [LIT-1574](../literature.d/LIT-1574.md) read

Karnkowska et al. 2019 ([LIT-1574](../literature.d/LIT-1574.md), read in [NOTE-1243](../notes.d/NOTE-1243.md); [THEORY-1098](../theory.d/THEORY-1098.md))
correct the previous title's "one indispensable job":

- **SUF alone was not enough.** The SUF system replaced the mitochondrial
  ISC pathway "in all examined Preaxostyla", including relatives that kept
  a mitochondrion-related organelle.
- **A second step.** The glycine cleavage system and SHMT sit in the
  organelle of the close relative *Paratrimastix pyriformis*. Their loss
  "took place after the split from the P. pyriformis lineage" and "removed
  another essential function". The authors count both as preadaptations,
  so the title is revised.
- **What went with it.** Mitophagy is the one system "likely lost together
  with mitochondria". Peroxisomes are also gone, which is common in
  anaerobes. No compensating gene was found.
- **The origin of SUF.** Its lateral-transfer origin is [LIT-1567](../literature.d/LIT-1567.md)'s claim
  and is not argued here.
- **"First eukaryote known to lack any form of mitochondrion" stands,**
  with two caveats from the paper. FIB-SEM "could still allow for
  undetected highly reduced mitosomes", and relatives may share the
  status.
- **A substituted dependence.** The organism is a gut commensal that
  salvages its nucleotides. It lost an internal partner and depends on a
  host gut instead. This inference is the record's, not the paper's.

## Note of 2026-11-22: [LIT-1567](../literature.d/LIT-1567.md) read ([LEAD-138](../leads.d/LEAD-138.md))

Karnkowska et al. 2016 ([LIT-1567](../literature.d/LIT-1567.md)) is now read in [NOTE-2320](../notes.d/NOTE-2320.md)
([THEORY-2230](../theory.d/THEORY-2230.md)), from the in-press article on the first author's
institutional site. The case took four facts from its abstract.

- **Held.** The genome "lacks all hallmark mitochondrial proteins"
  (none of the import machinery, carriers, ISC, cardiolipin synthase or
  ERMES; Golgi proteins found as a control). The ISC pathway, "thought
  to be conserved in virtually all eukaryotic cells", is replaced by a
  cytosolic SUF system "acquired by lateral gene transfer from
  bacteria". The loss is secondary. It is "the first example of a
  eukaryote lacking any form of a mitochondrion".
- **Refined.** The secondary-loss argument rests on the free-living
  sister lineage *Paratrimastix* keeping mitochondrial homologues, and
  on all oxymonads being obligate animal symbionts, as much as on
  phylogeny. The SUF acquisition belongs to the ancestor shared with
  *Paratrimastix*, and the paper's own model (Figure 4) puts the loss
  of the organelle in a later step. That agrees with the correction
  [LIT-1574](../literature.d/LIT-1574.md) already made to the title.
- **The authors' caveat.** They "cannot exclude the possibility that a
  mitochondrion exists ... whose protein composition has been altered
  entirely", though no evidence points to one.
- **The substituted dependence.** "All known oxymonads are obligate
  animal symbionts" is now a premise from the paper. The inference
  drawn from it, that a host gut stands in for the lost internal
  partner, remains the record's.
- **Unverified.** Nothing the case takes from [LIT-1567](../literature.d/LIT-1567.md) is left
  unchecked. The supplementary tables that list the searches were not
  read.

No status changes.
