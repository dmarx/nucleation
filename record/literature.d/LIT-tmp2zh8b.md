---
status: Active
status_note: 'read in full 2026-10-03 ([NOTE-tmpgl8bl](../notes.d/NOTE-tmpgl8bl.md)), from the authors'' own deposit of the accepted text. Worth reading as the standard organizational definition of minimal agency, and as the clearest statement that an agent is not the same thing as an individual. Individuality is one of three conditions, with interactional asymmetry and normativity; it is a precondition for the other two and is not sufficient for agency. The generative definition: an agent is an autonomous organization that adaptively regulates its coupling with its environment and contributes to sustaining itself as a consequence. The paper rejects statistical and energetic measures of asymmetry as sufficient, and says systems optimising an externally fixed function should not be treated as models of agency.'
title: 'Defining Agency: Individuality, Normativity, Asymmetry, and Spatio-temporality in Action'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full: the authors' version 1.0 (July 2009), deposited by
    Barandiaran at barandiaran.net/textos/defining_agency (PDF, 14 pp.,
    "Opened Access", with a CC BY-SA notice on Figure 1). I read §§1–6,
    Table 1, Figure 1, the footnotes and the reference list. The published
    pagination (Adaptive Behavior 17(5):367–386) was not seen, so no page
    numbers below are the journal's; quotations are from the deposit. A
    PhilPapers copy (BARDAI-6) returned a Cloudflare bot challenge and was
    not used. `published:` is the online date Crossref gives (23 September
    2009); the print issue is October 2009. Not held in the Anthology of
    the SOTA: a grep of its literature.d for "Barandiaran", the title and
    the DOI found nothing.
tags:
- agency
- individuation
- cognition
- complex-systems
- natural-sciences
date: '2026-10-03'
published: '2009-09-23'
doi: '10.1177/1059712309343819'
url: 'http://barandiaran.net/textos/defining_agency'
first_author: 'Barandiaran'
keywords:
- 'agency'
- 'individuality'
- 'interactional asymmetry'
- 'normativity'
- 'autonomy'
- 'sense-making'
- 'minimal agency'
- 'spatio-temporality'
implementations: []
summary: >-
  Barandiaran, Di Paolo & Rohde (2009), Adaptive Behavior 17(5):367–386.
  Three conditions are jointly necessary and sufficient for minimal
  agency: the system defines its own individuality, it is the active
  source of modulations of its coupling with the environment
  (interactional asymmetry), and it regulates that coupling by norms it
  generates (normativity). Generatively, an agent is an open autonomous
  system (a precarious network of mutually enabling processes) that
  adaptively modulates its coupling so as to maintain some of its
  constituent processes. Minimal life satisfies this; life is sufficient
  for agency but not necessary.
---
<!-- inactive-ok-file: LIT-536 — Deferred, unread; named for the autonomy tradition it systematises, not leaned on -->

# LIT-tmp2zh8b: Defining Agency: Individuality, Normativity, Asymmetry, and Spatio-temporality in Action

Xabier E. Barandiaran, Ezequiel Di Paolo and Marieke Rohde (2009),
*Adaptive Behavior* 17(5):367–386, special issue on agency (eds. Rohde and
Ikegami).

The brief's citation (Adaptive Behavior 17(5), 2009) is correct.

## Key takeaways

- **Three conditions, not one.** Individuality (the system distinguishes
  itself from its environment, without an observer doing it), interactional
  asymmetry (it is the active source of modulations of its coupling) and
  normativity (it regulates that coupling against norms it generates). Each
  is necessary; none, and no pair, is sufficient (§2.4, Table 1).
- **Individuality is a precondition, not agency.** A kitten warmed by its
  mother is an individual whose norm is met, but the mother drives the
  coupling, so it is not acting. A person with Parkinson's tremor is an
  individual and the source of the movement, but the movement answers to no
  norm (Table 1).
- **Asymmetry is modulation, not causation.** Energetic and statistical
  (correlational) criteria each fail on clear cases: the gliding bird and
  the diver versus the faller. Asymmetry is defined instead as the system
  changing a subset p of the constraints Q on an otherwise symmetrical
  coupling, Δp = H_T(S) (Eqs. 1–3).
- **The generative definition (§4).** S is an agent for a coupling C with
  environment E iff S is an open autonomous system (a network in which
  every process depends on and enables another, and would run down in
  isolation) and S modulates C adaptively, that is, so as to maintain some
  of its own processes. Autonomy here is Varela's, not personal autonomy.
- **Consequences for models (§6).** Sensorimotor coupling alone is too weak
  for agency, and "systems that only satisfy constraints or norms imposed
  from outside (e.g. optimization according to an externally fixed
  function) should not be treated as models of agency".

## Standing in the record

Filed on 2026-10-03 at the owner's request, in the batch on agency, self
and control, as the record's organizational definition of what an agent
is. No anthology topic holds it; it names robotics and AI as consumers of
the definition but carries no instruction for machine-learning practice.

**Agent versus individual.** The record keeps agent, individual, self and
person apart (`agency`, `individuation`, `self`, `personhood`, [ADR-024](../decisions.d/ADR-024.md)).
This paper argues for the first cut from inside one theory: individuality
is a condition on agency, and agency adds asymmetry and self-generated
norms. It is tagged `agency` first and `individuation` second for that
reason. It is not tagged `self` or `self-governance`. Its "self" is the
*autos* of an autonomous organization, and its "autonomy" is
organizational (Varela 1979), not the personal autonomy of Christman's
survey [LIT-297](LIT-297.md) or the self-endorsement of the self-determination theory
filings [LIT-559](LIT-559.md) and [LIT-560](LIT-560.md). The words coincide; the subjects do not.

Where it bears on what the record holds:

- **Biological Autonomy ([LIT-536](LIT-536.md)).** The acknowledgments thank Alvaro
  Moreno, and §§3–4 rest on the autonomy tradition that book later
  systematises (its chapter 4 is "Agency"). The paper's autonomy is wider
  than the book's metabolic one: "we do not restrict or reduce autonomy to
  the domain of metabolism", and component processes may be neural,
  sensorimotor or social.
- **Friston, "Life as we know it" ([LIT-526](LIT-526.md)).** Two of the paper's moves
  bear directly on the Markov-blanket account of the lifelike. It rejects
  statistical measures of influence as sufficient for asymmetry, and it
  requires that individuality be self-defined by an organization rather
  than drawn by an observer, which is the regress argument from Jonas in
  §2.1. [LIT-526](LIT-526.md) individuates by a conditional-independence partition chosen
  by spectral clustering. Bruineberg et al. ([LIT-tmpxq8pk](LIT-tmpxq8pk.md)) borrow this
  paper's term "interactional asymmetry" to describe the arrow structure a
  Friston blanket assumes. The paper predates [LIT-526](LIT-526.md) and does not discuss
  it.
- **Organizational closure.** The definition's statement 1.1 (each process
  depends on and enables another) is the operational closure that
  Montévil & Mossio ([LIT-tmpksq6n](LIT-tmpksq6n.md)) make formal as closure of constraints,
  and its normativity is the one Mossio, Saborido & Moreno ([LIT-tmp9gfzl](LIT-tmp9gfzl.md))
  ground functions in; the paper cites "Mossio et al. 2009" for it.
- **Participatory sense-making ([LIT-tmp9mw46](LIT-tmp9mw46.md)).** Its "sense-making" is the
  same notion, from the same group: a deviation from a self-generated norm
  makes an event significant for the agent.
</content>
</invoke>
