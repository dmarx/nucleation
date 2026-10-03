---
status: Active
status_note: 'read in full 2026-10-03 ([NOTE-tmptji09](../notes.d/NOTE-tmptji09.md)), from the free-to-read publisher PDF. Filed in place of Kelso''s book Dynamic Patterns ([LIT-tmpghan1](LIT-tmpghan1.md)) and as the read account of the paywalled Haken–Kelso–Bunz paper ([LIT-tmpp3m1q](LIT-tmpp3m1q.md)), both Deferred. Worth reading as Kelso''s own short statement of coordination dynamics: the HKB order-parameter equation for relative phase, its stochastic and symmetry-breaking extensions, metastability as relative coordination, the generalized HKB–Kuramoto model, and the claim that one coordination dynamics holds within and between people. It is a retrospective by an author of the model, not a review, and it says so.'
title: 'The Haken–Kelso–Bunz (HKB) model: from matter to movement to mind'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full: the publisher PDF (Biological Cybernetics 115:305–322,
    18 pp.), free to read at link.springer.com (Unpaywall: bronze open
    access), §§1–7, Box 1 caption, footnotes 1–5 and the Appendix with Eqs.
    (1)–(10). Box 1's figure is not in the text layer; its caption was
    read. The references were scanned, not read item by item. Chosen as
    the substitute for Kelso 1995 under the owner's rule for books, and as
    the readable account of HKB 1985, whose only copy is behind Springer's
    paywall. Not held in the Anthology of the SOTA: a grep of its
    literature.d for "Kelso", "HKB" and "coordination dynamics" found
    nothing.
tags:
- complex-systems
- behavioral-integration
- neuroscience
- cognition
- natural-sciences
- philosophy-of-science
- embodied-cognition
date: '2026-10-03'
published: '2021-08-18'
doi: '10.1007/s00422-021-00890-w'
first_author: 'Kelso'
keywords:
- 'HKB model'
- 'coordination dynamics'
- 'relative phase'
- 'order parameter'
- 'nonequilibrium phase transition'
- 'symmetry breaking'
- 'metastability'
- 'intrinsic dynamics'
- 'functional information'
- 'Kuramoto model'
implementations: []
summary: >-
  Kelso (2021), Biological Cybernetics 115(4):305–322, a 60th-anniversary
  retrospective. HKB models bimanual coordination by the relative phase φ,
  with dφ/dt = −a sin φ − 2b sin 2φ and potential V = −a cos φ − b cos 2φ:
  both in-phase and anti-phase are stable for b/a > 1/4, and anti-phase
  loses stability below it, as observed when movement frequency rises.
  Noise, symmetry breaking (Δω) and metastability extend it; with
  Kuramoto's model it becomes a generalized HKB for many agents. The same
  dynamics is reported within a body, between people and with machines,
  and in brain activity.
extends:
- LIT-tmpp3m1q
---
<!-- inactive-ok-file: LIT-tmpp3m1q — Deferred, paywalled; HKB 1985, the paper this retrospective is about and builds on, not read -->
<!-- inactive-ok-file: LIT-tmpghan1 — Deferred, no lawful full text; Kelso's book, which this paper substitutes for, not read -->

# LIT-tmpw3fkg: The Haken–Kelso–Bunz (HKB) model: from matter to movement to mind

J. A. Scott Kelso (2021), *Biological Cybernetics* 115(4):305–322,
"60th Anniversary Retrospective" (published online 18 August 2021).

## Key takeaways

- **The model.** Relative phase φ between the two hands is the order
  parameter; dφ/dt = −a sin φ − 2b sin 2φ (Eq. 1), with potential
  V(φ) = −a cos φ − b cos 2φ (Eq. 2). For b/a > 1/4 (slow movement) both
  φ = 0 and φ = π are stable; for b/a < 1/4 (fast movement) only in-phase
  remains. The switch is a pitchfork bifurcation, and with noise (Eq. 3) a
  nonequilibrium phase transition, with critical fluctuations and critical
  slowing before it.
- **From components to collective variable.** The φ dynamics is derived from
  two coupled "hybrid" (Van der Pol–Rayleigh) oscillators (Eqs. 4–6), and
  later from excitatory–inhibitory neural populations, which the author
  takes to put the mechanism-versus-description objection "to bed".
- **Symmetry breaking and metastability.** Adding the eigenfrequency
  difference Δω (Eq. 7) tilts the potential; past a saddle-node bifurcation
  no fixed points remain but "coordination tendencies" do. This metastable
  regime is offered as the theory of von Holst's relative coordination.
- **Generality.** The same coordination dynamics is reported between limbs,
  between a limb and a stimulus, between people, between humans and other
  species, and between humans and virtual partners, which the author reads
  as evidence that coupling is informational, not only mechanical. Combined
  with Kuramoto's model it handles groups (generalized HKB, Eq. 10).
- **Brain.** Phase transitions and stability-dependent recruitment were
  found in MEG/EEG and fMRI; TMS over premotor and supplementary motor
  cortex switched anti-phase to in-phase but not the reverse, as the model
  predicts.

## Standing in the record

Filed on 2026-10-03 at the owner's request, in the coordination-dynamics
part of the agency batch, as the substitute for two works.

**Why this paper.** The brief named Kelso's *Dynamic Patterns* (1995) and
Haken, Kelso & Bunz (1985). The book has no lawful full text ([LIT-tmpghan1](LIT-tmpghan1.md)),
and the 1985 paper is behind Springer's paywall with no repository copy
([LIT-tmpp3m1q](LIT-tmpp3m1q.md)). This paper is by Kelso, is free to read at the publisher,
and gives in eighteen pages the HKB equations with their parameter regimes,
the stochastic and symmetry-breaking extensions, the metastable regime it
credits the book with naming as relative coordination ("Kelso 1995"), and
the link to Kuramoto that postdates the book. It reproduces the book's
coordination-potential figure as its Box 1 ("adapted from Kelso 1995") and
points to the book's chapter 3 for the history of HKB and chapter 8 for the
brain's rhythms. The book's contents were not seen, so what it carries
beyond this paper is not known; it stays filed as a Deferred seed because it
is the citation others reach for. Kelso's encyclopedia article
"Coordination Dynamics" (2009/2013), which this paper cites, would have been
the other candidate; no lawful copy was found to compare.

**Relation.** It `extends` HKB 1985 ([LIT-tmpp3m1q](LIT-tmpp3m1q.md)): the paper is a statement
and extension of that model, with symmetry breaking, noise, metastability and
the many-oscillator generalization, and it could not stand without it.

**Caveats for a reader.** It is a retrospective by one of the model's
authors. It says it relies on "the work and opinions of others" where it can,
but its §5 list of consensus impacts and its §6 dismissal of the mechanism
question are the author's view. The data it cites (Schöner et al. 1986;
Meyer-Lindenberg et al. 2002; Jantzen et al. 2009) are reported, not shown.

Where it bears on what the record holds:

- **Participatory sense-making ([LIT-tmp9mw46](LIT-tmp9mw46.md))** takes absolute versus
  relative coordination from Kelso 1995; this paper's metastable regime is
  the formal account of the latter.
- **Raja et al. ([LIT-tmpumhsc](LIT-tmpumhsc.md))** use coupled pendulums measured by relative
  phase, citing Haken et al. 1985 and Kelso 1995, as a system already
  explained by its own collective variable, and ask what a Markov-blanket
  partition would add. This paper is the read statement of that
  collective-variable explanation.
- **Behavioral integration.** HKB is a worked case of many degrees of
  freedom acting as one, Bernstein's problem, solved by a low-dimensional
  collective variable rather than a controller; that is why the record tags
  it `behavioral-integration`. Kelso also lists the "excitator" and
  structured-flows models as descendants.
- **Philosophy of science.** §6 takes up whether dynamical models of this
  kind explain or merely describe (Kaplan & Craver 2011; Chemero), and
  warns that "Dynamical Systems Theory" is often invoked without identified
  collective variables or control parameters.
