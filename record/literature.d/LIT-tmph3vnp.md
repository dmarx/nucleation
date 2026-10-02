---
status: Active
status_note: 'read in full 2026-10-01 ([NOTE-tmprnrsd](../notes.d/NOTE-tmprnrsd.md)), from the authors'' preprint (CRCC Technical Report 49, March 1991) that Chalmers posts; the published text was not seen. Worth reading as the clearest short statement of the Fluid Analogies Research Group''s case against hand-coded representations, and as the most accessible description of Copycat. It is an argument, not a result: its two arguments against a separate "representation module" are informal and good, its case studies (BACON, SME) are fair as far as they go, and the evidence it offers for Copycat is a description of the architecture and one worked problem, with nothing measured in the paper itself.'
title: 'High-level perception, representation, and analogy: A critique of artificial intelligence methodology'
version: 1
history:
- version: 1
  date: '2026-10-01'
  note: >-
    Read in full: the preprint posted by Chalmers at
    https://consc.net/papers/highlevel.pdf (CRCC Technical Report 49,
    Center for Research on Concepts and Cognition, Indiana University,
    March 1991, "To appear in Journal of Experimental and Theoretical
    Artificial Intelligence"; 36 pp.; text extracted with PyMuPDF). I read
    the abstract, §§1–5 and the reference list. Figure 1 (SME's
    representations of the solar system and the atom) survived extraction
    as labels and was read from them; Figures 2–3 (Copycat structures, a
    piece of the Slipnet) survived only as labels. The published version,
    JETAI 4(3):185–211 (Taylor & Francis), was not seen, so differences
    between preprint and print are unknown. Citation verified against
    Crossref (https://api.crossref.org/works/10.1080/09528139208953747):
    authors David J. Chalmers, Robert M. French, Douglas R. Hofstadter;
    volume 4, issue 3, pp. 185–211; issued July 1992, month only, so
    `published:` is the first of the month. Every detail in the brief
    checked out. Not held in the Anthology of the SOTA: a grep of its
    record for "Hofstadter", "Copycat", "Chalmers" with the title, and the
    DOI found nothing.
tags:
- cognition
- complex-systems
- philosophy-of-science
date: '2026-10-01'
published: '1992-07-01'
doi: '10.1080/09528139208953747'
first_author: 'Chalmers'
keywords:
- 'high-level perception'
- 'representation'
- 'analogy'
- 'representation module'
- 'BACON'
- 'Structure-Mapping Engine'
- 'Copycat'
- 'microdomains'
implementations: []
summary: >-
  Chalmers, French & Hofstadter (1992), DOI-10.1080/09528139208953747.
  Traditional AI hands its programs representations built by people who
  already know the answer, so models like BACON (Kepler's third law) and
  the Structure-Mapping Engine (atom and solar system) skip the hard part,
  high-level perception: deciding what is relevant and how to organise it.
  Nor can the gap be filled later by a separate "representation module",
  because analogy shapes perception and the task decides which
  representation is right. Copycat, in a microdomain of letter strings,
  is offered as an architecture that builds representations and mappings
  together.
---
<!-- inactive-ok-file: LIT-tmphpjjx — Deferred, unreachable full text; Hofstadter's "Is there an 'I' in AI?", named as a neighbour, not leaned on -->
<!-- inactive-ok-file: LIT-tmpqepho — Deferred, no lawful full text; Minsky's The Society of Mind, named as a neighbouring architecture, not leaned on -->
<!-- inactive-ok-file: LIT-tmpsfaz3 — Deferred, closed access; Mitchell & Hofstadter's Copycat paper, named as the program's primary description, not leaned on -->

# LIT-tmph3vnp: High-level perception, representation, and analogy: A critique of artificial intelligence methodology

David J. Chalmers, Robert M. French, Douglas R. Hofstadter (1992), *Journal
of Experimental & Theoretical Artificial Intelligence 4(3):185–211; preprint
CRCC Technical Report 49, Indiana University, March 1991* —
DOI-10.1080/09528139208953747

## Key takeaways

- A model that is given its representations ready-made has been given the
  answer: the "20–20 hindsight" charge against BACON and SME.
- Representation-building cannot be split off into a front-end module,
  because analogy-making is part of perception and the right representation
  depends on the task in hand.
- Copycat is the group's demonstration that perception and mapping can be
  run together, by many small stochastic agents biased by a network of
  concepts.

## Standing in the record

Filed on 2026-10-01 at the owner's request for Douglas Hofstadter's work,
and the Fluid Analogies Research Group's programme in particular.
[NOTE-tmprnrsd](../notes.d/NOTE-tmprnrsd.md) is the close reading, and it placed the work: **Active**. It
is the group's methodological manifesto in one paper: why a theory of
cognition must start from the system building its own representations, and
why analogy is a perceptual process rather than a special-purpose reasoning
tool. It argues; it does not measure.

Its bearing on the record:

- **Copycat.** §4 is the most accessible account of Copycat, and it cites
  the Physica D paper ([LIT-tmpsfaz3](LIT-tmpsfaz3.md), filed beside it) for the details. Read
  together, this paper is the argument and that one the program. The
  emergence claim — "higher-level understanding emerges" from many local,
  parallel processes, under top-down bias from the Slipnet — is why it
  carries `complex-systems`, and it bears on the record's emergence
  readings ([LIT-141](LIT-141.md), [LIT-150](LIT-150.md)) as an engineered instance, not a theory.
- **Minsky.** Frames ([LIT-tmpf92fs](LIT-tmpf92fs.md)) are among the representational formats
  the paper names ("frames and scripts"), and its "data do not come
  prepackaged as slots and fillers" is aimed at that tradition: the critique
  is not that frames are the wrong format but that a format leaves the
  filling unexplained. Copycat's many small agents also stand near Minsky's
  society of agents ([LIT-tmpqepho](LIT-tmpqepho.md)), though the paper does not cite it.
- **Scientific discovery.** The BACON section and the closing reading of
  Copycat's re-perception as a "scientific revolution" in a microdomain are
  claims about how discovery works, read against Kuhn. That is why it
  carries `philosophy-of-science`: someone browsing that topic for
  computational models of discovery should find this critique of them.
- **Understanding in present AI.** The paper's 1992 "meaning barrier" is the
  ancestor of the record's question whether deep networks understand
  ([LIT-131](LIT-131.md)) and of Hofstadter's 2026 essay ([LIT-tmphpjjx](LIT-tmphpjjx.md)). Its §2 names
  connectionist models with context-dependent distributed representations
  as "a step in the right direction", which a reader of today's learned
  representations will want to set against its demand that perception and
  task interact.
- **Boundary.** The paper carries a methodological instruction for AI
  modelling: do not hand-code representations; build perception into the
  model. It is aimed at symbolic cognitive modelling, not machine-learning
  practice. The nearest anthology topic, `analysis-and-evaluation` ("which
  comparisons are unsound"), would hold only its charge that BACON's and
  SME's successes are artefacts of pre-built inputs, and that charge is
  about cognitive models, not learned ones. It is not tagged
  `anthology-candidate`.
