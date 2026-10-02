---
status: Active
status_note: 'read in full 2026-10-02 ([NOTE-tmporp14](../notes.d/NOTE-tmporp14.md)); worth reading as the short, exact critique of Dewar''s information-theoretic derivation of maximum entropy production. It shows that the 2005 derivation''s key step holds only where the constitutive relations are linear, so MaxEP far from equilibrium is not established by it, and that the 2003 claim that MaxEP yields self-organized criticality is an artefact of a mean-field expansion. Read from the authors'' submitted manuscript (Zenodo); the version of record was not seen. Its first point is checked here only on its own worked example, since Dewar 2005 itself could not be read.'
title: 'Comments on a derivation and application of the ‘maximum entropy production’ principle'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (the authors' manuscript as submitted to J. Phys. A on 15
    April 2007, 5 pp., deposited on Zenodo, record 889780, under CC BY-SA,
    found through Semantic Scholar's open-access link; text extracted with
    PyMuPDF). I read the abstract, §1 with its spin-chain example (§1.1),
    §2 and the four references. I re-derived the spin-chain partition
    function, λ(F), A(F) and the quadratic expansion of Eq. 4, and Eq. 3
    from the definitions it states. I checked the SOC argument against
    Dewar 2003 (LIT-tmpbf3wy, Eqs. 26–28), which I read. The published
    Comment (J. Phys. A: Math. Theor. 40(31):9717–9720, online 19 July
    2007) was not seen. Dewar's 2005 letter (J. Phys. A 38:L371), the
    target of §1, could not be read: no open copy was reachable.
    Not held in the Anthology of the SOTA: a grep of its literature.d for
    "Grinstein", "Linsker" and the DOI found nothing. `published:` is the
    Crossref online date; there is no arXiv version. Filed with the critics
    of Prigogine's extremum principles and the MEP literature, at the
    owner's request to fill out the record's coverage of dissipative
    structures.
tags:
- natural-sciences
- information-theory
- complex-systems
date: '2026-10-02'
published: '2007-07-19'
doi: '10.1088/1751-8113/40/31/N01'
first_author: 'Grinstein'
keywords:
- 'maximum entropy production'
- 'MaxEP'
- 'MaxEnt'
- 'Dewar'
- 'constitutive relations'
- 'fluctuation theorem'
- 'self-organized criticality'
- 'mean-field approximation'
implementations: []
summary: >-
  Grinstein & Linsker (2007), DOI-10.1088/1751-8113/40/31/N01. A Comment
  with two points. (1) Dewar's 2005 derivation of MaxEP needs a quadratic
  approximation to p(f) near f = F to hold for all f. With the fluctuation
  theorem, that forces A(F) to be constant, i.e. linear constitutive
  relations. So the "orthogonality condition" behind both maximum and
  minimum entropy production fails far from equilibrium, as an exact
  spin-chain model shows. (2) Dewar's 2003 SOC result is an artefact.
  Keeping the quartic term gives a finite flux variance at F_ext = 0.
---
<!-- inactive-ok-file: LIT-tmp9n5sf — Deferred, no lawful full text; named as the survey of the MEP literature, not leaned on -->

# LIT-tmpflluj: Comments on a derivation and application of the ‘maximum entropy production’ principle

G. Grinstein, R. Linsker (2007), *Journal of Physics A: Mathematical and Theoretical 40(31), 9717–9720* (Comment) — DOI-10.1088/1751-8113/40/31/N01

## Standing in the record

Filed on 2026-10-02 with the critics of Prigogine's extremum principles and
the maximum-entropy-production (MEP) literature, at the owner's request to
fill out the record's coverage of dissipative structures. It is the record's
statement of why the information-theoretic foundation of MEP is not
settled.

[NOTE-tmporp14](../notes.d/NOTE-tmporp14.md) is the close reading of 2026-10-02, and it placed the work:
**Active**.

- **Second point, checked in full.** It is correct against the paper it
  criticises, Dewar 2003 ([LIT-tmpbf3wy](LIT-tmpbf3wy.md)), which the record holds and has
  read. The SOC divergence there is produced by extending a quadratic
  expansion to all F.
- **First point, checked only on the authors' own model.** It concerns
  Dewar's 2005 letter, which could not be read, so the record holds it on
  the strength of the spin chain. There λ(F) = τ artanh F and A(F)F =
  τF/(1 − F²) agree only as F → 0. The record is not filing Dewar 2005
  because its text could not be reached.

Its scope is narrower than its reputation. It refutes one derivation of
MaxEP, and one application. It says the existence of far-from-equilibrium
extremal principles "has not been settled". It does not say MaxEP is false,
and it calls Dewar's MaxEP–SOC conjecture "intuitively appealing".
Kleidon's review ([LIT-tmp8wfl8](LIT-tmp8wfl8.md)) cites it as pointing out "some technical
flaws in the derivation of the linkage of MEP and SOC", which reports the
second point and leaves out the first. The survey by Martyushev and
Seleznev ([LIT-tmp9n5sf](LIT-tmp9n5sf.md)) predates it.

It bears on Prigogine's minimum principle too. The same orthogonality
condition gives both maximum and minimum dissipation in Dewar's scheme. So
the Comment's conclusion, that the condition needs linear constitutive
relations, applies to the minimum principle derived that way as well. In
the Comment's words, both derivations "do require 'the usual
near-equilibrium assumption of linear constitutive relations'", the
inner quotation being Dewar's own phrase for what he claimed to avoid.
