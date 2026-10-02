---
status: Active
status_note: 'read in full 2026-10-02 ([NOTE-tmpbwfxo](../notes.d/NOTE-tmpbwfxo.md)), from arXiv v1, the only arXiv version; the published Physical Review X text was not reached. Worth reading as the origin of "dissipative adaptation": the claim that driven matter tends towards states whose formation absorbed and dissipated work reliably, with no replication needed. Read it as a heuristic argument with two toy models, not a theorem. Its exact content is a rearranged macrostate fluctuation relation; the step to "adaptation" holds two terms fixed that it does not show can be held fixed in a many-body system, and the simulation it reports was not shown. It deliberately erases the line between living and non-living organization.'
title: 'Statistical Physics of Adaptation'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (arXiv:1412.1875 v1, 5 Dec 2014, the only arXiv version,
    24 pp., text extracted with PyMuPDF): the whole text, Eqs. (1)–(13),
    Figs. 1–4 and the 12 references. I checked the derivation of Eq. (8)
    from Eq. (3) and recomputed the two hopping-model results, Eqs.
    (10)–(13). The published version (Phys. Rev. X 6(2):021036, published
    16 June 2016, CC BY 3.0) was not seen: the publisher returned HTTP 403
    to every request. The arXiv record carries the journal reference, but
    the PRX text may differ from the 2014 preprint in content as well as
    form; this reading is of the preprint. Not held in the Anthology of the
    SOTA: a grep of its literature.d for the DOI, the arXiv id, "Perunov",
    "England" and "dissipat" found nothing on it. `published:` is the arXiv
    v1 date.
tags:
- thermodynamics
- natural-sciences
- complex-systems
- individuation
date: '2026-10-02'
published: '2014-12-05'
arxiv: '1412.1875'
doi: '10.1103/PhysRevX.6.021036'
first_author: 'Perunov'
keywords:
- 'dissipative adaptation'
- 'driven self-organization'
- 'fluctuation theorem'
- 'Crooks relation'
- 'entropy production'
- 'nonequilibrium statistical mechanics'
- 'resonance'
- 'adaptation without replication'
implementations: []
summary: >-
  Perunov, Marsland & England (2014; Phys. Rev. X 2016), arXiv:1412.1875.
  Starting from a fluctuation relation between coarse-grained macrostates,
  the paper writes the log-odds of two outcomes of a driven system as an
  internal-entropy term, a reversal-probability term and Ψ − Φ, the mean
  heat minus a fluctuation correction (Eq. 8). Holding the first two
  fixed, the more likely outcome is the one whose formation absorbed and
  dissipated work from the drive more reliably. It calls such outcomes
  "adapted" and argues the tendency needs no self-replication. Two
  single-particle hopping models illustrate the dissipation and fluctuation
  terms (Eqs. 10–13); the many-body case is a plausibility argument.
---

<!-- inactive-ok-file: THEORY-026 — Proposed; named as the account whose notion of an efficient, predictive driven system this paper's "adapted" system is contrasted with, not leaned on -->

# LIT-tmp7ay36: Statistical Physics of Adaptation

Nikolai Perunov, Robert A. Marsland III and Jeremy L. England (2016),
*Physical Review X* 6(2):021036 (published 16 June 2016; CC BY 3.0);
first posted as arXiv:1412.1875, v1 5 December 2014 (physics.bio-ph), the
version read.

The brief's citation (Phys. Rev. X 6(2):021036, 2016) is correct. The
arXiv preprint lists the authors as "Nikolai Perunov, Robert Marsland, and
Jeremy England"; Crossref has Perunov, Marsland, England.

## Key takeaways

- **An exact relation, rearranged.** For two outcomes II and III of a
  system prepared in I and driven by a field λ(t), the log ratio of their
  forward probabilities equals the difference in internal entropy, plus the
  log ratio of their reversal probabilities, plus ΔΨ − ΔΦ. Ψ is the mean
  heat released (in k_BT) and Φ corrects for its fluctuations, so Ψ − Φ =
  −ln⟨e^{−βΔQ}⟩ (Eqs. 6–8). The authors call this "a generalization of the
  Helmholtz free energy" for driven, finite-time evolution.
- **Dissipative adaptation, the interpretive claim.** All else equal (same
  internal entropy, same reversal probability), the likelier outcome is the
  one reached by paths that absorbed more work from the drive and
  dissipated it more reliably. Such states have "dynamical response
  properties" tuned to the drive, as a resonant oscillator is tuned to its
  forcing frequency, and the paper calls them "better adapted".
- **No replication needed.** "The adaptation we predict is expected to take
  place independent of whether or not there is anything in the system that
  can copy itself." Self-replication is offered as one especially good way
  to keep absorbing work while changing shape. "Well-adapted" structures
  "that did not have parents" (sand dunes, snowflakes, hurricanes, active
  filament bundles) are proposed as test cases.
- **What is shown.** Two three-state and two-state hopping models with
  oscillating energies and barriers. In one, drift is reliably accompanied
  by dissipation, with r_max(2→1)/r(2→3) = exp(ΔΨ) (Eq. 12). In the other,
  fluctuations in entropy production slow the forward rate, ln r ≃ −Φ
  (Eq. 13).

## Standing in the record

Filed on 2026-10-02 at the owner's request, as part of filling out the
record's coverage of dissipative structures and the "life as dissipation"
literature. No anthology topic holds it. It carries no instruction for
machine-learning practice: its "learns" is in scare quotes, and it is about
driven matter, not learning systems.

[NOTE-tmpbwfxo](../notes.d/NOTE-tmpbwfxo.md) is the close reading of 2026-10-02, and it placed the work:
**Active**. It is the paper the phrase "dissipative adaptation" comes from,
and it is cited far more widely than the evidence it gives. Its exact part
is a rearrangement of England's macrostate relation for a driven system.
The "tendency towards adaptation" depends on holding the internal-entropy
and reversal terms fixed. The paper shows that this can be done only in a
contrived single-particle landscape, and argues that some of the ∼10²⁵
directions of a many-body phase space "should" behave the same way. The
simulation of a driven chemical mixture is reported in one paragraph
"rather than shown here".

Where it bears on what the record holds:

- **The predecessor.** England 2013, [LIT-tmp2fe4j](LIT-tmp2fe4j.md), supplies the
  macrostate relation (its Eq. 6) and the bound on replication heat that
  this paper's Discussion invokes for Darwinian competition.
- **Still et al. ([LIT-327](LIT-327.md)) and [THEORY-026](../theory.d/THEORY-026.md).** Both papers study a system
  driven by a fixed external protocol with no feedback, and both read
  dissipation as a record of the drive. They use "adapted" in opposite
  directions. In [THEORY-026](../theory.d/THEORY-026.md) a system matched to its drive is one whose
  memory is predictive, and it *wastes less* work. Here a system matched to
  its drive is one that *absorbs and dissipates more* work, reliably. The
  two are not in contradiction. Still prices the dissipation of a given
  system over a protocol; this paper asks which macrostate a stochastic
  evolution is likely to reach. But the record should not merge the two
  senses, and a claim that "adapted systems dissipate more" or "adapted
  systems dissipate less" needs to say which one it means.
- **The demarcation question ([LIT-192](LIT-192.md), [NOTE-094](../notes.d/NOTE-094.md)).** The paper is the
  sharpest statement in the record of the view that there is no principled
  line between living adaptation and the self-organization of dissipative
  structures. It calls it "somewhat arbitrary how we have decided to draw a
  line around a whale". Its stated aim is a notion of adaptation that does
  not need "to decide in advance on a physical definition of where one
  replicator ends, and another begins". This is the claim Nahas & Sachs's
  candle-flame dispute is about, made from the physics side. The paper
  does not engage the philosophical side (autopoiesis, closure, Deacon).
- **Self-organization in the record.** The primitive metabolic cycles of
  [LIT-036](LIT-036.md) are self-organized states of a chemically driven system. This
  paper's claim predicts that such states should be the ones that absorb
  and dissipate the chemical drive reliably. [LIT-036](LIT-036.md) does not compute
  dissipation, so the prediction is untested there.
- **"What Lives?" ([LIT-211](LIT-211.md)).** This paper is a paradigm member of the
  "Dissipative Self-Organizing Systems" view of life ([NOTE-109](../notes.d/NOTE-109.md)), though it
  defines adaptation, not life.

The paper cites the record's neighbours on entropy-production principles
(Martyushev 2010, as a contrast: maximising Ψ alone "is not predicted to
correspond to a likely outcome") and on fluctuation theorems (Crooks 1999,
Jarzynski 1997, 2006; Hatano–Sasa 2001). Those are being filed in parallel
in this batch.
