---
status: Active
status_note: 'read in full 2026-10-09 ([NOTE-tmpj1l5b](../notes.d/NOTE-tmpj1l5b.md)); worth reading as the first paper to test natural-language data for contextuality in the formal sense rather than the loose one, and as the paper that names the obstacle the test meets: corpus estimates of meaning selection are almost always signalling. In the sheaf-theoretic framework one hand-specified support model ({tap, box} × {pitcher, cabinet}) is possibilistically contextual (a Hardy-type failure), but its corpus probabilities are signalling, so the framework cannot judge them. Under Contextuality-by-Default the Bell-type corpus systems are noncontextual, and two noun–verb pairs read as subject–verb and verb–object (adopt/boxer, throw/pitcher) are CbD-contextual, by 1/30 and 7/30. Its own parametric bootstrap then gives those two a probability above .56 and above .08 of being noncontextual, on fractions with denominators between 3 and 30, so the contextual verdicts are not statistically secured.'
title: 'On the Quantum-like Contextuality of Ambiguous Phrases'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed at the owner's request on 2026-10-09 and read in full the same
    day (NOTE-tmpj1l5b) from the arXiv PDF (2107.14589v1, the only
    version, 6 pages, text layer extracted), compared with the ACL
    Anthology PDF (2021.semspace-1.5, 11 pages): the two text extracts
    share their vocabulary and every figure checked, apart from the
    Anthology's header. Bibliography checked against the arXiv abstract
    page (v1 submitted 19 July 2021, cs.CL, no journal reference) and the
    ACL Anthology record (Proceedings of the 2021 Workshop on Semantic
    Spaces at the Intersection of NLP, Physics, and Cognitive Science
    (SemSpace), eds. Martha Lewis and Mehrnoosh Sadrzadeh, Groningen,
    June 2021, pp. 42–52; no DOI). Crossref holds no record of it.
    `published:` is the arXiv v1 date by ADR-002's arXiv rule; the
    Anthology gives only the month, June 2021, which is earlier. Chosen
    as the Sadrzadeh-group paper that tests language data for
    contextuality; the journal follow-up and the later anaphora papers
    are named in the body, not filed. Not held in the Anthology of the
    SOTA: a grep of its record/ (clone pulled 2026-10-09, commit d8b5ba5)
    for the arXiv id, the title, Sadrzadeh and Cervantes found nothing.
tags:
- contextuality
- linguistics
- quantum-foundations
- probabilistic-modeling
- cognition
- compositionality
date: '2026-10-09'
published: '2021-07-19'
arxiv: '2107.14589'
first_author: 'Wang'
keywords:
- 'quantum-like contextuality'
- 'lexical ambiguity'
- 'sheaf-theoretic contextuality'
- 'Contextuality-by-Default'
- 'signalling'
- 'corpus frequencies'
implementations: []
summary: >-
  Wang, Sadrzadeh, Abramsky & Cervantes (2021), [ARXIV-2107.14589](https://arxiv.org/abs/2107.14589), SemSpace
  2021 (ACL Anthology, pp. 42–52). Treats each word of a two-word
  ambiguous phrase as a measurement whose outcome is the selected meaning.
  One hand-specified support model is possibilistically contextual; its
  BNC/ukWaC probabilities, like all the corpus models, are signalling.
  Under Contextuality-by-Default two subject–verb/verb–object pairs come
  out contextual, but the paper's own bootstrap leaves both plausibly
  noncontextual.
extends:
- LIT-016
- LIT-777
supports:
- CLAIM-037
---

<!-- inactive-ok-file: THEORY-013 — Proposed; cited for the data claim this reading bears on, not as settled -->

# LIT-tmp9rgb4: On the Quantum-like Contextuality of Ambiguous Phrases

Daphne Wang, Mehrnoosh Sadrzadeh, Samson Abramsky and Víctor H. Cervantes
(2021), in *Proceedings of the 2021 Workshop on Semantic Spaces at the
Intersection of NLP, Physics, and Cognitive Science (SemSpace)*, ACL
Anthology 2021.semspace-1.5, pp. 42–52 — [ARXIV-2107.14589](https://arxiv.org/abs/2107.14589)

## Key takeaways

- **The set-up.** A phrase of two ambiguous words is a bipartite
  measurement: each word is a measurement, its outcome the meaning
  selected, and a context is a pair of words in a fixed grammatical
  relation. Four words in a 2 × 2 Bell-type arrangement give a cyclic
  scenario. Supports in §5 are set by the authors' judgement;
  probabilities in §6 are relative frequencies of hand-annotated
  readings in the BNC and ukWaC.
- **Possibilistic contextuality, once, and only on hand-set supports.**
  {tap, box} × {pitcher, cabinet} is possibilistically non-signalling and
  contextual: its only global assignments are tap = box = pitcher,
  cabinet the other value, so the locally possible (tap = touch,
  pitcher = baseball player) does not extend. {coach, boxer} × {lap,
  file} is possibilistically signalling; {press, box} × {can, leaves} is
  non-signalling and noncontextual.
- **Corpus data are signalling.** Every corpus-estimated model is
  signalling, including the probabilistic version of the tap/box model,
  so the sheaf-theoretic criterion does not apply to any of them (§§6–7).
  The authors argue that non-signalling has no reason to hold for
  language: a word's selected meaning constrains its partner's.
- **Contextuality-by-Default verdicts.** The Bell-type corpus systems are
  CbD-noncontextual (a 105-constraint linear program over 2¹⁶ events for
  press/box, the Kujala–Dzhafarov cyclic inequality for the others). Two
  rank-2 systems, the same noun–verb pair read as verb–object and as
  subject–verb, are CbD-contextual: adopt/boxer by 1/30 and throw/pitcher
  by 7/30 (Dzhafarov, Kujala and Cervantes's measure).
- **The verdicts are not secured.** By parametric bootstrap the
  probability of a noncontextual system given these estimates is above
  .56 for adopt/boxer and above .08 for throw/pitcher (§8.1). The counts
  behind them are small: the printed fractions have denominators 30 and
  4 for the two adopt/boxer contexts and 10 and 3 for throw/pitcher, so
  one context may rest on as few as three or four occurrences.

## Standing in the record

Filed on 2026-10-09 at the owner's direct request, as the work by
Sadrzadeh and collaborators that tests ambiguous phrases for formal
contextuality, following Abramsky and Sadrzadeh's Semantic Unification
([LIT-841](LIT-841.md)). It is not from the manuscript bibliography: the owner asked
for it directly on 2026-10-09. It is the first data test of the record's
contextuality line ([LIT-016](LIT-016.md), [THEORY-012](../theory.d/THEORY-012.md)) on language, and the first
language case for Contextuality-by-Default ([LIT-777](LIT-777.md), [LIT-264](LIT-264.md),
[THEORY-013](../theory.d/THEORY-013.md)). [NOTE-tmpj1l5b](../notes.d/NOTE-tmpj1l5b.md) says how it bears on the manuscript's argument
on line `pragmatic-transport`.

The same programme's other papers, named here and not filed:

- **The journal follow-up.** Wang, Sadrzadeh, Abramsky and Cervantes,
  "Analysing Ambiguous Nouns and Verbs with Quantum Contextuality Tools",
  *Journal of Cognitive Science* 22(3):391–420 (2021), DOI
  10.17791/jcs.2021.22.3.391, author copy at UCL Discovery (eprint
  10146180). It was read in full for this filing. It does not test
  contextuality again. It builds 90 rank-2 noun–verb systems from the
  same corpora and measures their direct influences (signalling) instead,
  through Jones's canonical models, finding verbs with several meanings
  carry about 70% of a phrase's direct influence against about 50% for
  verbs with several senses. It carries a different result, not half of
  this one, so it is not filed separately.
- **Later work.** Lo, Sadrzadeh and Mansfield on anaphora: a BERT-based
  sheaf model of anaphoric ambiguity (EPTCS 366, 2022, arXiv 2208.05720);
  a generalised Winograd schema with crowdsourced judgements violating
  Bell–CHSH by 0.192 (EPTCS 384, 2023, arXiv 2308.16498); further
  developments with a contextual fraction of 0.096 (EPTCS 408, 2024,
  arXiv 2402.04505); and a large-scale BERT study reporting 77,118
  sheaf-contextual and 36,938,948 CbD-contextual instances
  (Proc. R. Soc. A, 2025, DOI 10.1098/rspa.2024.0399, arXiv 2412.16806).
  Wang and Sadrzadeh's causal analysis of the same phrases is EPTCS 394
  (2023, arXiv 2206.06807), and Wang's thesis covers the line
  (arXiv 2408.07402). None of these was read.
