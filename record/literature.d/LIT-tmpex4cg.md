---
status: Active
status_note: 'read in full 2026-10-02 ([NOTE-tmpjvb5a](../notes.d/NOTE-tmpjvb5a.md)); worth reading as the paper that introduced the evolutionarily stable strategy and showed that "limited war" in animal contests can be favoured by individual selection. It is not the source of the Hawk–Dove game or of owner–intruder conventions, though morality-as-cooperation cites it for both: its strategies are Mouse, Hawk, Bully, Retaliator and Prober-Retaliator, its contestants are symmetric, and its "Retaliator is an ESS" ties with Mouse, so it fails the paper''s own second ESS condition. What it does ground for MAC''s contest domains is restraint backed by retaliation, and, informally, retreat before a visibly superior opponent and honest signals of formidability.'
title: 'The Logic of Animal Conflict'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (the Nature typeset pages 15–18, as a PDF in a course
    library at the Centre for Energy Research, Budapest,
    public.ek-cer.hu/~szabo/EGT20/library/maynard_n73.pdf; text extracted
    with PyMuPDF). I read the whole article, Table 1 and the references.
    OCR misread some table digits (e.g. "SO.O" for 80.0); values used
    below were checked against the prose, which quotes several of them.
    The issue date, 2 November 1973, is printed on each page; Crossref
    gives November 1973. Not held in the Anthology of the SOTA (grep of
    its literature.d for the DOI, the title and "Maynard Smith": nothing),
    nor already in this record. Filed for the lineage of
    morality-as-cooperation (ADR-018).
tags:
- natural-sciences
- game-theory
- mathematics
date: '2026-10-02'
published: '1973-11-02'
doi: '10.1038/246015a0'
first_author: 'Maynard Smith'
keywords:
- 'evolutionarily stable strategy'
- 'animal conflict'
- 'limited war'
- 'retaliation'
- 'war of attrition'
- 'game theory'
implementations: []
summary: >-
  Maynard Smith & Price (1973), DOI-10.1038/246015a0. Why do animals with
  dangerous weapons fight conventionally? A simulation of five strategies
  (Mouse, Hawk, Bully, Retaliator, Prober-Retaliator) shows Hawk is not an
  evolutionarily stable strategy while Retaliator nearly is, so "limited
  war" can be favoured by individual selection. In a pure war of
  attrition no fixed persistence is stable; the ESS is an exponential
  mixture. There is no Hawk–Dove game and no ownership asymmetry here.
---

<!-- inactive-ok-file: LIT-tmpcsgn6 — Proposed: Curry 2016, the statement of morality-as-cooperation filed in the same batch; cited for which sources it credits for each domain -->

# LIT-tmpex4cg: The Logic of Animal Conflict

J. Maynard Smith and G. R. Price (1973), *Nature 246 (5427): 15–18, 2 November 1973* — DOI-10.1038/246015a0

## Key takeaways

- Conventional, non-injurious fighting can be favoured by individual selection, without group selection: in a population of retaliators an escalating "Hawk" does worse than a strategy that fights conventionally and retaliates (Table 1).
- The evolutionarily stable strategy (ESS) is defined: a strategy I such that E_I(I) > E_I(J) for all J, or, if equal, E_J(I) > E_J(J) (p. 17).
- In a contest decided by persistence alone, no pure strategy is stable; the ESS is a persistence cost drawn from p(x) = (1/v)exp(−x/v), so a stable population is polymorphic or individually variable (p. 17).

## Standing in the record

Filed on 2026-10-02 at the owner's request, as one of the evolutionary
sources of morality-as-cooperation. The lineage paragraph of [NOTE-034](../notes.d/NOTE-034.md)
credits "hawk–dove contests (Maynard Smith & Price)", the concept list there
glosses hawkish and dovish traits with the same citation, and Curry 2016
([LIT-tmpcsgn6](LIT-tmpcsgn6.md)) writes that "animal conflicts are modelled … as nonzero-sum
hawk–dove games … (Maynard Smith & Price, 1973)".

[NOTE-tmpjvb5a](../notes.d/NOTE-tmpjvb5a.md) is the close reading of 2026-10-02, and it placed the work:
**Active**, with a correction the MAC literature needs. This paper has no
Hawk–Dove game. Its passive strategy is "Mouse"; the word "dove" does not
occur. Its contestants have "identical fighting prowess", so it does not
model display of formidability followed by deference, and it has no
owner–intruder asymmetry, so it does not ground possession. What it does
show is that restraint is stable only when backed by retaliation
("contestants should respond to an 'escalated' attack by escalating in
return"). In its informal "Real Animals" section it argues that
conventional fighting carries information about prowess, so an animal
facing a much superior opponent "will frequently retreat", and that an
unfakeable sign of recklessness (musth in elephants) can pay. That is the
seed of MAC's hawkish-display and dovish-deference domains, not their
model. MAC's possession domain rests, in Curry 2016, on Maynard Smith
(1982) and Gintis (2007), neither in the record.

The stability claim also needs care. Table 1 gives Mouse 29.0 against
Retaliator, the same as Retaliator against itself, and Retaliator 29.0
against Mouse, the same as Mouse against itself. By the second condition
the paper itself states, Retaliator is therefore not an ESS: Mouse can
drift in. The authors say "Retaliator is an ESS since no other strategy
does better, though Mouse does equally well". A comment by Gale & Eaves,
Nature 254:463 (1975), DOI-10.1038/254463b0, re-examined the analysis; it
was not read here.

Hamilton's Part II ([LIT-tmpfgxhl](LIT-tmpfgxhl.md), §6) explains restraint between
relatives by relatedness. This paper explains it between non-relatives by
retaliation, and says excessively dangerous weapons "would be opposed by
kin selection". Axelrod & Hamilton ([LIT-tmp6z0ji](LIT-tmp6z0ji.md)) take the ESS concept from
here.

**Topic.** `natural-sciences` first: it is about animal behaviour.
`mathematics` for the evolutionary game theory, the "mathematical
frameworks applied to other fields" of that word's blurb. Not
`probabilistic-modeling`, whose blurb is Bayesian inference and
statistical models; not `moral-psychology`, since the paper is not about
morality (its one human analogy is "fair and foul blows … in boxing").

**Anthology.** No instruction for machine-learning practice; not held
there.
