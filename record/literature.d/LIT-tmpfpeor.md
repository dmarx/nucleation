---
status: Active
status_note: >-
  read in full 2026-11-06 ([NOTE-tmp2gykh](../notes.d/NOTE-tmp2gykh.md)) from the arXiv preprint, v1;
  worth reading as a compact, numerically checked case of what a weak loss
  does to an integrable soliton: it does not break up but shrinks along its
  family of shapes, at a rate fixed by an energy balance, exponentially
  under linear damping and algebraically under viscous, Landau,
  boundary-layer and friction losses, and to zero in a finite time under
  radiation, where in fact it turns into an envelope soliton. Filed as the
  read neighbour of Kivshar & Malomed (1989), [LIT-tmpzah9i](LIT-tmpzah9i.md), for damped
  solitons. Its limits: one equation, Benjamin–Ono, with the KdV laws
  quoted from the literature, not derived; no gain or supply; no NLS.
title: 'Decay of Benjamin–Ono solitons under the influence of dissipation'
version: 1
history:
- version: 1
  date: '2026-11-06'
  note: >-
    Registered and read on 2026-11-06 at the owner's suggestion that
    soliton dynamics bear on the record's questions of individuation and
    persistence (works chosen by the assistant), as a stand-in for Kivshar
    & Malomed (1989), LIT-tmpzah9i, which was not reached. Citation checked
    against Crossref (no mailto): Roger H. Grimshaw, Noel F. Smyth and Yury
    A. Stepanyants, Wave Motion 78, 98–115, doi:10.1016/j.wavemoti.2018.01.005,
    issued April 2018 with no day. The earliest exact date is the arXiv v1
    of 2018-01-27, which is `published:`. Copy from arxiv.org,
    arXiv:1801.09088v1, the preprint "submitted to Elsevier", text by
    pdftotext; its pages were not compared with the published version.
tags:
- natural-sciences
- mathematics
- complex-systems
date: '2026-11-06'
published: '2018-01-27'
arxiv: '1801.09088'
doi: '10.1016/j.wavemoti.2018.01.005'
first_author: 'Grimshaw'
keywords:
- 'Benjamin-Ono equation'
- 'soliton decay'
- 'adiabatic perturbation theory'
- 'dissipation'
- 'trailing shelf'
- 'terminal decay'
implementations: []
summary: >-
  Grimshaw, Smyth & Stepanyants (2018). Adds six kinds of weak loss to the
  integrable Benjamin–Ono equation and finds, by an energy balance that is
  the condition for removing secular terms, how its soliton decays: it
  stays a soliton whose amplitude slides down the family, as A0 e^(−t/τ)
  under linear (Rayleigh) damping, twice as fast as a linear wave,
  algebraically, A0/(1 + t/τ)^p, under viscous, Landau, laminar
  boundary-layer and Chezy losses, and as A0(1 − t/τ), terminally, under
  radiation into large-scale dispersion. Where the loss does not conserve
  mass a shelf forms behind the soliton and the adiabatic picture
  eventually fails; under Landau damping the decaying soliton is exact.
  Checked against direct numerics. The KdV laws are quoted from earlier
  work, not derived.
---
<!-- inactive-ok-file: LIT-tmpzah9i THEORY-tmpu2r6o — Unavailable or Proposed; cited from the reading of Grimshaw, Smyth & Stepanyants (2018) as open -->

# LIT-tmpfpeor: Decay of Benjamin–Ono solitons under the influence of dissipation

Grimshaw, R. H., Smyth, N. F. & Stepanyants, Y. A. (2018). Decay of Benjamin–Ono solitons under the influence of dissipation. *Wave Motion* 78: 98–115. doi:10.1016/j.wavemoti.2018.01.005. [ARXIV-1801.09088](https://arxiv.org/abs/1801.09088).

## Key takeaways

*From the reading, [NOTE-tmp2gykh](../notes.d/NOTE-tmp2gykh.md). Section numbers are the preprint's.*

- **Shrink, not break up** (§1): under weak loss "the basic structure of the
  solitary wave remains the same, but its primary parameter A, which
  determines its amplitude, speed and width, is no longer a constant, but
  is a slowly varying function of time".
- **The decay laws** (§8, Table): Rayleigh A0 e^(−t/τ), τ = 1/2δ; Reynolds
  A0/√(1 + t/τ); Landau A0/(1 + t/τ); laminar boundary layer
  A0/(1 + t/τ)²; Chezy A0/(1 + t/τ); radiative A0(1 − t/τ).
- **KdV, quoted, not derived** (§§4, 5, 7): Landau A0(1 + t/τ)^−2, boundary
  layer A0(1 + t/τ)^−4, radiative A0(1 − t/τ)², each cited to earlier work
  (Ott & Sudan 1969 and 1970; Grimshaw 2001; Grimshaw, He & Ostrovsky 1998
  and Grimshaw, Ostrovsky, Shrira & Stepanyants 1998).
- **The shelf** (§§1, 2, 6): with mass not conserved "the solution u(x, t)
  cannot be just a BO soliton, but must contain a non-solitonic part (a
  trailing wave)".
- **Radiative decay is not the end** (§7): the soliton "does not completely
  disappear, but transforms into an envelope soliton".

## Standing in the record

Filed as the read neighbour of Kivshar & Malomed (1989), [LIT-tmpzah9i](LIT-tmpzah9i.md), for
the review's central method, the adiabatic treatment of a weakly damped
soliton, in one equation. It does not cite the review and carries none of
its NLS, kink or collision results. Filed from it: [THEORY-tmpu2r6o](../theory.d/THEORY-tmpu2r6o.md). It bears
on the record's line on persistence as a sharp case of a structure held by
an internal balance with no supply, which under loss runs down smoothly,
with no threshold collapse, and can look intact for many decay times while
doing so.
