---
status: Active
status_note: 'read 2026-10-02 ([NOTE-tmpg7iyq](../notes.d/NOTE-tmpg7iyq.md); §§5, 8.3–8.4, 9.2 and 11 skimmed); worth reading as the systematic reference for stochastic thermodynamics as of 2012: first law, heat and stochastic entropy along single trajectories of Markovian systems coupled to baths, every known fluctuation theorem derived from one master theorem with a conjugate dynamics, dissipation as distinguishability of forward and reverse paths, Sagawa–Ueda feedback, the NESS fluctuation–dissipation theorem and efficiency of molecular machines. It is the framework in which the record''s thermodynamics-of-prediction and thermodynamics-of-learning results ([LIT-327](LIT-327.md), [LIT-308](LIT-308.md)) are stated. Read it as a review: the derivations are its own and concise, the case studies are reported.'
title: 'Stochastic thermodynamics, fluctuation theorems and molecular machines'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read (arXiv 1205.4176 v1, 18 May 2012, the only arXiv version, 105 pp.
    including 602 references, from the arXiv PDF; text extracted with
    PyMuPDF, which drops most displayed equations' bodies but keeps their
    numbers). Read closely: §1 (introduction, scope, complementary
    reviews), §2 (Langevin dynamics, first law, stochastic entropy), §3
    (classification of fluctuation theorems, Jarzynski, Bochkov–Kuzovlev,
    Crooks, entropy-production theorems, Hatano–Sasa), §4 (conjugate
    dynamics and the master theorem), §6 (master-equation dynamics), §7
    (optimal protocols, time's arrow, measurement and feedback), §§8.1–8.2
    (the NESS fluctuation–dissipation theorem), §§9.1, 9.3–9.4
    (biomolecules, free-energy recovery, enzymes and motors), §10
    (isothermal machines) and §12 (concluding perspective). Skimmed: §5
    (experimental and numerical case studies), §§8.3–8.4, §9.2 and §11
    (heat engines). References were consulted, not read through. The
    Reports on Progress in Physics version of record (75(12):126001,
    online 20 November 2012) was not seen. Not held in the Anthology of the
    SOTA: a grep of its literature.d for "Seifert", the DOI and the arXiv id
    found nothing; the nucleation record holds Seifert only as coauthor of
    LIT-308. `published:` is the arXiv v1 date. Filed with the critics of
    Prigogine's extremum principles and the fluctuation theorems, at the
    owner's request to fill out the record's coverage of dissipative
    structures.
tags:
- thermodynamics
- natural-sciences
- information-theory
date: '2026-10-02'
published: '2012-05-18'
doi: '10.1088/0034-4885/75/12/126001'
arxiv: '1205.4176'
first_author: 'Seifert'
keywords:
- 'stochastic thermodynamics'
- 'fluctuation theorems'
- 'stochastic entropy'
- 'entropy production'
- 'nonequilibrium steady state'
- 'feedback'
- 'molecular motors'
- 'efficiency at maximum power'
implementations: []
summary: >-
  Seifert (2012), DOI-10.1088/0034-4885/75/12/126001. A 105-page review of
  stochastic thermodynamics. Work, heat and a stochastic system entropy
  s = −ln p(x(τ),τ) are defined along single trajectories of Markovian
  systems coupled to baths, and every known integral, detailed and Crooks
  fluctuation theorem is derived from one master theorem by choosing a
  conjugate dynamics. Further results: dissipation bounds forward–reverse
  distinguishability (⟨w⟩ − ΔF ≥ D[p‖p_eq]), Sagawa–Ueda feedback
  relations, a NESS fluctuation–dissipation theorem in terms of entropy
  production, and a cycle-based theory of efficiency at maximum power for
  molecular machines.
---
<!-- inactive-ok-file: THEORY-026 — Proposed; named as the account this reading bears on, not leaned on -->
<!-- inactive-ok-file: THEORY-030 — Proposed; named as the account this reading bears on, not leaned on -->

# LIT-tmpcfjz8: Stochastic thermodynamics, fluctuation theorems and molecular machines

Udo Seifert (2012), *Reports on Progress in Physics 75(12), 126001* — DOI-10.1088/0034-4885/75/12/126001 (preprint arXiv:1205.4176, 18 May 2012)

## Standing in the record

Filed on 2026-10-02 with the critics of Prigogine's extremum principles, the
maximum-entropy-production literature and the fluctuation theorems, at the
owner's request to fill out the record's coverage of dissipative
structures. The anthology does not hold it.

[NOTE-tmpg7iyq](../notes.d/NOTE-tmpg7iyq.md) is the reading of 2026-10-02, and it placed the work:
**Active**. Most of it was read closely, and the experimental survey and
the heat-engine section were skimmed. It is the reference for the framework
the record's thermodynamics-of-computation papers work in. Goldt and
Seifert's learning bound ([LIT-308](LIT-308.md)) is a stochastic-thermodynamics result in
this sense, built on Horowitz's subsystem second law ([NOTE-296](../notes.d/NOTE-296.md)). Still et
al.'s nonpredictive-dissipation identity ([LIT-327](LIT-327.md)) is stated with the same
nonequilibrium free energy, which [LIT-327](LIT-327.md) takes from other sources. It derives
Jarzynski's equality ([LIT-tmp47vbz](LIT-tmp47vbz.md)) and Crooks's theorem ([LIT-tmpc4996](LIT-tmpc4996.md)) as
special cases of one master theorem.

Its bearing on [THEORY-026](../theory.d/THEORY-026.md) is twofold, and neither part is support for the
account's claim.

- **Framework.** It states the bound ⟨w⟩ − ΔF ≥ D[p(x_t)‖p_eq(x_t)] (Eq.
  150, from Vaikuntanathan and Jarzynski, in units with T = 1). For a fixed
  protocol started in equilibrium, that is the statement that [LIT-327](LIT-327.md)'s
  protocol-level dissipation ⟨W_ex⟩ − F^add is nonnegative. [NOTE-tmpg7iyq](../notes.d/NOTE-tmpg7iyq.md)
  explains the match.
- **Scope.** It does not address the per-step nostalgia under a non-Markov
  drive, which is what [THEORY-026](../theory.d/THEORY-026.md)'s promotion condition asks for.

It also frames [THEORY-030](../theory.d/THEORY-030.md)'s subject: §7.3 states that work extracted by
feedback is paid back by erasure "according to Landauer's principle", and
reports the colloidal experiment in which erasure heat approaches the
Landauer bound for slow cycles.

On Prigogine's programme it is the modern descendant, not a defence. Seifert
notes (§1.1) that "stochastic thermodynamics" revives a name the Brussels
school used in the mid-1980s at the ensemble level for chemical systems. In
a footnote to §6.1 he points to Polettini 2011 "for a relation to the
minimum entropy production principle", and otherwise says nothing on
extremum principles. Its linear-response section (§10.4) recovers Onsager
symmetry from the cycle representation, and its efficiency results are
stated beyond linear response.
