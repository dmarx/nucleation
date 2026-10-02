---
status: Active
status_note: 'read in full 2026-10-02 ([NOTE-tmp7prgu](../notes.d/NOTE-tmp7prgu.md)); worth reading as the short, authoritative account of the Belousov–Zhabotinsky reaction by the chemist who named half of it: discovery, the core mechanism (autocatalytic HBrO₂ inhibited by Br⁻), the Oregonator and its known defects, closed versus open-reactor dynamics, and target and spiral waves. Chosen over Zaikin & Zhabotinsky (1970) because it is openly readable and covers the 1970 waves paper; it is a short encyclopedia review with no new results.'
title: 'Belousov-Zhabotinsky reaction'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (the Scholarpedia article as served on 2026-10-02,
    http://www.scholarpedia.org/article/Belousov-Zhabotinsky_reaction,
    revision #91050, "last modified on 21 October 2011", its four sections
    and the 38 references; the five figures were read from their captions
    only). The page credits Anatol M. Zhabotinsky as author and lists
    later contributors (E. M. Izhikevich, T. Denninger, B. Bronner, R. J.
    Field); it was reviewed by R. J. Field and an anonymous referee and
    "Accepted on: 2007-09-11", which is used as `published:` because
    Crossref gives the year only. Chosen as the BZ entry in place of the
    request's two primary candidates. Zaikin & Zhabotinsky, "Concentration
    Wave Propagation in Two-dimensional Liquid-phase Self-oscillating
    System", Nature 225(5232):535–537, February 1970 (DOI
    10.1038/225535b0, authors A. N. Zaikin and A. M. Zhabotinsky, as the
    request has them) is paywalled, and only its first paragraph was
    visible. Zhabotinsky (1964) is in Russian in Biofizika 9:306–311 and
    was not reached. This review is by the same author, open, refereed by
    the "F" of the FKN mechanism, and summarizes both. Not held in the
    Anthology of the SOTA: a grep of its literature.d, notes.d and
    theory.d for "Zhabotinsky", "Belousov" and both DOIs found nothing.
tags:
- natural-sciences
- complex-systems
date: '2026-10-02'
published: '2007-09-11'
doi: '10.4249/scholarpedia.1435'
first_author: 'Zhabotinsky'
keywords:
- 'Belousov-Zhabotinsky reaction'
- 'chemical oscillations'
- 'Oregonator'
- 'excitability'
- 'chemical waves'
- 'spiral waves'
- 'CSTR'
implementations: []
summary: >-
  Zhabotinsky (2007), Scholarpedia 2(9):1435. BZ reactions are
  metal-ion-catalysed oxidations of organic reductants by bromate in
  acid. The core loop is autocatalytic oxidation of the catalyst via
  HBrO₂, switched off by bromide, which the oxidized catalyst regenerates
  from bromomalonic acid. Closed, stirred, it can run "up to several
  thousand" cycles; only in a continuous-flow reactor do oscillations
  continue indefinitely, and there bursting and chaos appear. Unstirred
  thin layers support target and spiral waves (Zaikin & Zhabotinsky
  1970). The Oregonator is qualitatively right and quantitatively not.
---
<!-- inactive-ok-file: LIT-tmpd737a — Deferred, no lawful full text; Nicolis & Prigogine, cited only as the review's source for the far-from-equilibrium condition on oscillation -->

# LIT-tmpoej2u: Belousov-Zhabotinsky reaction

Anatol M. Zhabotinsky (2007), *Scholarpedia 2(9):1435 (revision #91050, last modified 21 October 2011)* — DOI-10.4249/scholarpedia.1435

## Key takeaways

- The BZ reaction made homogeneous chemical oscillation respectable. Before it, chemists read the detailed-balance argument, which forbids oscillation near equilibrium, as forbidding oscillation in any closed homogeneous system, and blamed observed oscillations on heterogeneity or error.
- The oscillation is a relaxation cycle. Autocatalytic production of HBrO₂ oxidizes the catalyst (Ce³⁺ → Ce⁴⁺). Br⁻ inhibits that autocatalysis, and Br⁻ is produced when Ce⁴⁺ is reduced by malonic and bromomalonic acid. Phase-resetting by injected Br⁻, Ag⁺ and Ce⁴⁺ confirms the scheme.
- Closed, it oscillates for up to thousands of cycles and then stops; open (CSTR), it oscillates indefinitely and shows bursting and chaos. Unstirred, it propagates trigger waves that form target patterns and, when broken, spirals and scroll waves.

## Standing in the record

Filed on 2026-10-02 at the owner's request, as the Belousov–Zhabotinsky entry
among the canonical systems of the dissipative-structure programme. The
request offered Zhabotinsky (1964) or Zaikin & Zhabotinsky (1970). Neither was
readable, so this review by Zhabotinsky, which covers both, stands in.

It bears on the record's coverage in three ways.

- **What makes BZ a dissipative structure, and when.** The review's split
  between closed and open systems is the useful point. A closed BZ mixture
  oscillates on its way to equilibrium: a long transient, not a steady
  state. Only the continuous-flow reactor holds it permanently away from
  equilibrium, which is Prigogine's condition ([LIT-tmp452jw](LIT-tmp452jw.md)). Cross and
  Hohenberg ([LIT-tmpht8ga](LIT-tmpht8ga.md), §X.B.5) make the same point for patterns: closed
  experiments "run down in finite time", and open gel reactors were the fix.
- **The demarcation question in [LIT-192](LIT-192.md).** BZ is the cleanest case of a
  chemical system with behaviour organisms are often singled out for:
  rhythm, excitability, self-propagating signals, entrainment of slower
  pacemakers by faster ones. It does this with no closure of constraints and
  nothing that maintains itself; fed reagents, it simply runs. That supports
  the view [NOTE-094](../notes.d/NOTE-094.md) records, that dissipative self-organization cannot be the
  demarcating property, and it makes BZ the natural foil for any account
  that tries to make it one.
- **[LIT-211](LIT-211.md)'s "Dissipative Self-Organizing Systems" cluster.** BZ satisfies
  thermodynamic-organizational definitions of life of that kind about as
  well as a candle flame does. It is the standard counter-example such
  definitions must exclude.

The review's first paragraph credits Nicolis and Prigogine ([LIT-tmpd737a](LIT-tmpd737a.md)) with
the far-from-equilibrium condition on oscillation.

No instruction for machine-learning practice. The anthology does not hold it.
