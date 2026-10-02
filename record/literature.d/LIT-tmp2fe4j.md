---
status: Active
status_note: 'read in full 2026-10-02 ([NOTE-tmpeo3wn](../notes.d/NOTE-tmpeo3wn.md)), from arXiv v1, the only arXiv version; the published J. Chem. Phys. text was not reached. Worth reading as the founding paper of the "dissipation-driven" programme and as a clean worked use of a macrostate fluctuation relation: the heat a replicator must release is bounded below by how fast it copies and how durable the copy is, not by the copying itself. The general bound (Eq. 6) is a coarse-grained second law and is sound; the numbers for E. coli and RNA rest on an argued, not derived, upper bound on the reverse probability (Eq. 7). It draws no line between living and non-living replicators, and says so: "self" is a classification an observer supplies.'
title: 'Statistical physics of self-replication'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (arXiv:1209.1179 v1, 6 Sep 2012, the only arXiv version,
    5 pp., text extracted with PyMuPDF): the whole text, Eqs. (1)–(8),
    Fig. 1 and the 20 references. I re-derived Eq. (6) from Eq. (5) and
    recomputed the paper's numerical estimates (the 75 n_pep irreversibility
    term, the factor-of-three comparison with the measured 220 n_pep, and
    the RNA and DNA heat bounds). The published version (J. Chem. Phys.
    139(12):121923, 2013, CC BY 3.0) was not seen: the publisher returned
    HTTP 403 to every request, and no other copy of the version of record
    was found. Not held in the Anthology of the SOTA: a grep of its
    literature.d for the DOI, the arXiv id, "England" and "self-replication"
    found nothing. `published:` is the arXiv v1 date.
tags:
- thermodynamics
- natural-sciences
- complex-systems
- individuation
date: '2026-10-02'
published: '2012-09-06'
arxiv: '1209.1179'
doi: '10.1063/1.4818538'
first_author: 'England'
keywords:
- 'self-replication'
- 'entropy production'
- 'microscopic reversibility'
- 'coarse-graining'
- 'heat bound'
- 'bacterial cell division'
- 'RNA replicator'
- 'origin of life'
implementations: []
summary: >-
  England (2012; J. Chem. Phys. 2013), arXiv:1209.1179. For a system in a
  heat bath obeying detailed balance, a transition between coarse-grained
  ensembles I → II obeys β⟨ΔQ⟩ + ln π(II→I) + ΔS_int ≥ 0 (Eq. 6), a second
  law stated for macrostates. Applied to self-replication, the reverse
  probability is small when the copy is durable and made fast, so the heat
  released per copy is bounded below by about 2n ln(n τ_decay/τ_div) − ΔS_int
  (Eq. 8). The author's estimates put E. coli within a factor of three of
  this bound and a self-replicating RNA near it. The "self" in
  self-replication is an observer's classification of microstates, not a
  physical given.
---

<!-- inactive-ok-file: THEORY-030 — Proposed; named as the account of Landauer's scope this paper's bound is compared with, not leaned on -->
<!-- inactive-ok-file: LIT-328 — Deferred: Landauer 1961 is unread; named because the paper compares its bound with it, not leaned on -->

# LIT-tmp2fe4j: Statistical physics of self-replication

Jeremy L. England (2013), *The Journal of Chemical Physics* 139(12):121923
(online 21 August 2013; CC BY 3.0); first posted as arXiv:1209.1179, v1 6
September 2012 (physics.bio-ph), the version read.

The brief's citation (J. Chem. Phys. 139(12):121923, 2013) is correct.

## Key takeaways

- **A second law for macrostates (Eq. 6).** If the dynamics obey detailed
  balance in a bath (no external driving), then for any two ensembles I and
  II defined by an observer's classification of microstates, β⟨ΔQ⟩ ≥ −ln
  π(II→I) − ΔS_int. The heat released must pay for the internal entropy
  change *and* for how unlikely the return trip is.
- **Replication is priced by speed and durability.** For a replicator whose
  copies decay with lifetime τ (peptide-bond hydrolysis, RNA backbone
  hydrolysis) and which divides in time τ_div, the reverse probability is
  about the probability that a copy falls apart within τ_div. The heat bound
  grows with ln(τ/τ_div): a more durable or faster copy costs more heat.
- **Worked estimates.** E. coli releases 220 n_pep k_BT per division against
  an irreversibility term of about 75 n_pep, so less than three times the
  bound. The bound for a ligase-type RNA replicator (about 7 kcal/mol)
  sits near the measured reaction enthalpy (about 10 kcal/mol), and the
  same reaction in DNA would need about 16 kcal/mol, more than it releases.
  The author offers this as a reason RNA, not DNA, would come first.
- **No physical "self".** "Self-replication is something that happens
  relative to an observer": the count of copies exists only once a
  classification scheme assigns one to each microstate.

## Standing in the record

Filed on 2026-10-02 at the owner's request, as part of filling out the
record's coverage of dissipative structures and of the "life as
dissipation" literature. No anthology topic holds it, and it carries no
instruction for machine-learning practice.

[NOTE-tmpeo3wn](../notes.d/NOTE-tmpeo3wn.md) is the close reading of 2026-10-02, and it placed the work:
**Active**. Its general result is a correct coarse-grained second law; the
paper itself says it is closely related to the Landauer bound and holds for
time-symmetrically driven systems too. The replication numbers depend on an
upper bound for the reverse probability that is argued from biology (the
most likely way back is one copy hydrolysing), not derived.

Where it bears on what the record holds:

- **Landauer, Bennett and Still.** The paper's own comparison is with
  Landauer, whose paper the record holds unread ([LIT-328](LIT-328.md)). The record's
  account of Landauer's scope, [THEORY-030](../theory.d/THEORY-030.md), read from Bennett ([LIT-360](LIT-360.md)), says
  copying onto a blank register has no minimum cost. England's bound does
  not contradict that. What it prices is not the copy but the finite-time
  irreversibility of making a durable copy quickly: as τ_div grows, the
  irreversibility term falls away. Still et al. ([LIT-327](LIT-327.md)) price the
  nonpredictive part of a driven system's memory; England prices statistical
  irreversibility between macrostates. Both are second-law bounds over
  averages, and neither is per operation.
- **The demarcation question ([LIT-192](LIT-192.md)).** Nahas & Sachs report a dispute
  over whether teleological systems can be told apart from dissipative
  structures ([NOTE-094](../notes.d/NOTE-094.md)). This paper takes the deflationary side: the
  replicating "self" is an observer's coarse-graining, and the bound
  applies to any replicator with a reliable population model. It draws no
  line between a cell and a non-living replicator. The record's other
  readings that make individuality observer- or model-relative are the
  Wilson & Barker survey ([LIT-168](LIT-168.md)) and Levin's "Self" bounded by what it
  can measure and change ([LIT-439](LIT-439.md)); England's coarse-graining is the
  statistical-mechanics version of that move.
- **"What Lives?" ([LIT-211](LIT-211.md)).** Its "Dissipative Self-Organizing Systems"
  cluster of definitions ([NOTE-109](../notes.d/NOTE-109.md)) is the side of the definitional
  landscape this paper speaks for, but the paper defines no life.

Its sequel, Perunov, Marsland & England (2016), [LIT-tmp7ay36](LIT-tmp7ay36.md), on "dissipative
adaptation", is filed beside it in this batch and drops self-replication altogether.
