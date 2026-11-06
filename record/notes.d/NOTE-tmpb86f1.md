---
status: Read
paper: 'LIT-tmpun6ep'
title: 'Zabusky and Porter — Soliton (Scholarpedia)'
version: 1
history:
- version: 1
  date: '2026-11-06'
  note: >-
    Read in full on 2026-11-06 from the article's HTML at
    http://www.scholarpedia.org/article/Soliton (current revision; the page
    gives "Accepted on: 2010-08-26"), converted to text. Read: the lead,
    §1 Historical development, §2 Explicit construction of the KdV
    soliton, §3 The solitary wave menagerie, §4 Applications and the figure
    captions. Not read closely: §5 MATLAB code and the reference lists.
    Read as a stand-in for Zabusky & Kruskal (1965), LIT-tmpfx0lb.
date: '2026-11-06'
summary: >-
  A solitary wave is held by a balance of nonlinearity and dispersion; a
  soliton keeps its shape at constant speed and comes out of a collision
  unchanged except for a phase shift, which in a conservative system means
  amplitude, shape and velocity are conserved. Zabusky and Kruskal named it
  in 1965 from numerical KdV solutions; inverse scattering explained it as
  integrability. Topological, dissipative and other relatives are only
  named, and in general lack the collision property.
---
<!-- inactive-ok-file: LIT-tmpfx0lb LIT-tmpzah9i LIT-tmp4mmn1 LIT-1642 THEORY-tmp68j1u CLAIM-157 TERM-088 THEORY-072 — Unavailable, Unfetched or Proposed; cited from the reading of Zabusky & Porter (2010) as open -->

# NOTE-tmpb86f1: Zabusky and Porter — Soliton (Scholarpedia)

## Contribution

An authored encyclopedia article, by the co-author of the 1965 letter that
named the soliton, giving the definition, the history and a catalogue of
related localized structures. Nothing in it is new; its value here is a
precise statement, from the source, of what a soliton's identity is.

## Key insight

A soliton is individuated by what survives interaction: two solitons pass
through each other and come out with the same amplitude, shape and
velocity, shifted only in phase. That property belongs to integrable
equations; the relatives do not in general share it.

## Assumptions

One space dimension for the definition; a conservative (non-dissipative)
system for "conserved after a collision"; integrability for the special
interaction properties. The article notes that in more dimensions "one
needs to be more nuanced" (§1).

## Key results

- **Definition** (lead): "A solitary wave is a localized "wave of
  translation" that arises from a balance between nonlinear and dispersive
  effects." A soliton "must maintain its shape when it moves at constant
  speed", and "When a soliton interacts with another soliton, it emerges
  from the "collision" unchanged except possibly for a phase shift." So
  "for a conservative (non-dissipative) system, a soliton is a solitary
  wave whose amplitude, shape, and velocity are conserved after a
  collision".
- **Collision** (Fig. 2, a two-soliton KdV run from the article's code):
  "Observe the phase shift that occurs when the two solitons collide."
- **Origin** (§1): Korteweg–de Vries work was ignored "until 1965 when
  Norman Zabusky and Martin Kruskal published their numerical solutions of
  the KdV equation (and invented the term "soliton")"; Kruskal derived KdV
  "as an asymptotic (continuum) description" of the Fermi–Pasta–Ulam
  lattice.
- **Formation from initial data** (Fig. 3): "Near-recurrence in the
  Korteweg–de Vries (KdV) equation with a single-mode (sine wave) initial
  condition"; "The red–orange streaks indicate right-propagating,
  large-amplitude solitons that arise from the initial condition." Of
  Russell's 1844 findings (§1): "A sufficiently large initial mass of water
  can produce two or more independent near-solitary waves that separate in
  time."
- **Integrability** (§1): Gardner, Greene, Kruskal and Miura "were able to
  solve the initial-value problem for the KdV equation by introducing the
  inverse scattering method"; for nonintegrable equations "analytical
  techniques typically rely on perturbative methods, asymptotic analysis,
  and/or variational approximations (Kivshar, 1989)".
- **The menagerie** (§3, named only): topological solitons "emerge because
  of topological constraints"; kinks are "The only one-dimensional
  topological solitary wave"; dissipative solitons are "Stable localized
  structures that arise in spatially extended dissipative systems";
  oscillons arise "in granular and other dissipative media"; and the
  relatives "do not in general have similar interaction properties as
  solitons".

## Concepts

Soliton against solitary wave; balance of nonlinearity and dispersion;
elastic collision with phase shift; near-recurrence; inverse scattering and
integrability; topological and dissipative relatives.

## Connections

- **For Zabusky & Kruskal (1965)**, [LIT-tmpfx0lb](../literature.d/LIT-tmpfx0lb.md), unread: restates the
  naming, the numerical origin, the elastic collision and the recurrence
  picture, in the first author's words. Does not restate the letter's
  equation parameters, figures or numbers.
- **For Kivshar & Malomed (1989)**, [LIT-tmpzah9i](../literature.d/LIT-tmpzah9i.md), unread: cites it for the
  perturbative study of nonintegrable solitary waves; carries none of its
  results.
- **Satsuma & Yajima (1974)**, [LIT-tmp4mmn1](../literature.d/LIT-tmp4mmn1.md): the count of solitons from an
  initial pulse is in Cui & Wang (2023), not here; Russell's "sufficiently
  large initial mass" is the qualitative version.
- **Dissipative solitons**: named only. [LIT-1642](../literature.d/LIT-1642.md) (Knobloch 2015,
  Unfetched), Herr et al. (2014) and Grelu & Akhmediev (2012) are the
  record's sources.
- Filed from it: [THEORY-tmp68j1u](../theory.d/THEORY-tmp68j1u.md).

## Bearing on the record

- **[TERM-088](../terms.d/TERM-088.md) (individuation)**: supports the dynamical sense with a sharp
  case. Identity is the parameter set that survives collision, "unchanged
  except possibly for a phase shift", and a soliton is dynamically
  individuated with no upkeep at all. It is not constitutive or autonomous.
- **[TERM-070](../terms.d/TERM-070.md) (closure)**: none; a soliton has no constraints producing one
  another.
- **[THEORY-072](../theory.d/THEORY-072.md), [QUESTION-085](../questions.d/QUESTION-085.md)**: a conservative soliton is neither flame nor
  organism; it persists with no flux, held by an internal balance. A case
  the flame–convection–organism line does not yet place.
- **[CLAIM-157](../claims.d/CLAIM-157.md)**: bears on its third pressure, localized structures as
  dynamical individuals, for the conservative case: the individual is
  tracked through interaction by its conserved parameters. It says nothing
  of turnover, since a lossless soliton's material does not turn over in
  any sense the claim means.
- **[QUESTION-399](../questions.d/QUESTION-399.md)**: a soliton persists without being self-maintaining.

## Limitations

An encyclopedia article; the copy read is the current revision, not
compared with the 2010 one. Relatives are named, not treated: nothing on
existence thresholds, bistability, hysteresis or topological protection.
The figures are illustrative simulations.
