---
status: Active
status_note: >-
  read in full 2026-10-24 ([NOTE-tmpat2ia](../notes.d/NOTE-tmpat2ia.md)) from arXiv v2 (17 June 2020);
  worth reading for one clean theorem, one general lemma and a hypothesis
  with evidence. The theorem: where players can signal n bits before the
  result is settled, every pattern of wins and losses among 2ⁿ strategies,
  a cycle through all of them included, is realized. The lemma: Nash
  clusters are weakly ordered by population performance, and beating a
  population that contains a whole cluster lifts a strategy above it.
  The hypothesis, that real games are shaped like a spinning top, with cycles thickest
  at middling strength, rests on sampled empirical games. The abstract says
  it is proved and the body says it is not. The random-game theorem's proof
  is defective, and the fixed-memory fictitious play result needs a
  replacement rule it does not state.
title: 'Real World Games Look Like Spinning Tops'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Filed and read 2026-10-24, at the lead's request in the owner's inquiry
    into how the record stands on multi-agent learning. Citation checked
    against the arXiv listing (v1 20 April 2020, v2 17 June 2020) and the
    NeurIPS 2020 proceedings index, which lists it under the same title;
    NeurIPS papers carry no DOI in Crossref. The arXiv v2 PDF is still
    marked "Preprint". Read in full from arXiv:2004.09468v2, a 27-page PDF
    under arXiv's non-exclusive distribution licence, extracted by
    pdftotext: sections 1–7 and supplementary sections A–L, every proof
    followed. Theorem 4 was checked against supp_text.tex in the v2
    source. The reference list was skimmed. The proceedings version was
    not compared. `published:` is v1's date under ADR-002.
tags:
- game-theory
- learning-theory
- anthology-candidate
date: '2026-10-24'
published: '2020-04-20'
arxiv: '2004.09468'
url: 'https://proceedings.neurips.cc/paper_files/paper/2020/hash/ca172e964907a97d5ebd876bfdd4adbd-Abstract.html'
first_author: 'Czarnecki'
keywords:
- 'Games of Skill'
- 'spinning top geometry'
- 'non-transitivity'
- 'n-bit communicative games'
- 'Nash clustering'
- 'relative population performance'
- 'population-based training'
- 'empirical game theory'
implementations: []
summary: >-
  Czarnecki, Gidel, Tracey, Tuyls, Omidshafiei, Balduzzi & Jaderberg
  (NeurIPS 2020). Games in which players can signal n bits before the
  outcome is settled contain every win–loss pattern on 2ⁿ strategies, so
  cycles of length 2ⁿ (Go: at least 2¹⁰⁰⁰). Nash clustering orders a game's
  strategies into clusters weakly ordered by population performance.
  Empirical games sampled from small board games and the AlphaStar league
  show cluster size peaking at middling strength, the "spinning top", and
  population-based training converges once the population is large
  enough.
---
<!-- inactive-ok-file: NOTE-tmpat2ia THEORY-tmp2ela3 THEORY-tmpq0hjk THEORY-tmp5k950 — filed from this reading, named -->

# LIT-tmp42ace: Real World Games Look Like Spinning Tops

Czarnecki, Gidel, Tracey, Tuyls, Omidshafiei, Balduzzi & Jaderberg (2020),
*Advances in Neural Information Processing Systems 33* (NeurIPS 2020) —
arXiv:2004.09468

## Key takeaways

*From the reading, [NOTE-tmpat2ia](../notes.d/NOTE-tmpat2ia.md). Page numbers are arXiv v2's.*

- **Long cycles are generic where play can signal.** If each player can
  transmit n bits before a win or loss becomes unattainable, every
  antisymmetric win–loss pattern among ⌊2ⁿ⌋ strategies is realized by pure
  strategies that announce an identity and then throw or take the game
  (Theorem 1; [THEORY-tmp2ela3](../theory.d/THEORY-tmp2ela3.md)). Go is at least about 1000-bit
  communicative, and Tic-Tac-Toe 5.58-bit. The theorem is ordinal: it is
  about the sign of the outcome.
- **Nash clusters.** Repeatedly peel off the support of a Nash of what
  remains. Earlier clusters are weakly ahead of later ones in relative
  population performance, and a strategy beating every member of a
  population containing a whole cluster lies in an earlier cluster
  (Theorems 2 and 3; [THEORY-tmpq0hjk](../theory.d/THEORY-tmpq0hjk.md)). Both hold in every finite
  symmetric zero-sum game, not only in Games of Skill.
- **The spinning top is a hypothesis.** "Naturally, the above does not
  prove that real world games follow the Games of Skill geometry" (p. 6),
  against the abstract's "We prove the existence of this geometry". The
  evidence is about 1000 sampled search agents per game in eight small
  board games, plus AlphaStar's league. The authors say the league
  shows "AlphaStar induced game geometry" (p. 18) ([THEORY-tmp5k950](../theory.d/THEORY-tmp5k950.md)).
- **Population size.** With a pessimistic oracle, populations below a
  critical size cycle, and above it they converge to the strongest
  strategies. In the disc game no size helps, and in an Elo game size 1
  suffices.
- **Defects.** Proposition 3 needs a replacement rule it does not state.
  The reader built a three-layer game in which replacing the newest member
  cycles forever and replacing the oldest converges. Theorem 4's proof
  computes the wrong variance (σ²/m⁴ for what is σ²/(2m²) at most) and
  treats a selected quantity as zero-mean.

## Why this is here

Filed 2026-10-24 for the record's cycles line. Theorem 1 says when cycles
are unavoidable: whenever parties can condition on who they face before
the outcome is fixed. That bears on [CLAIM-tmpuxcp6](../claims.d/CLAIM-tmpuxcp6.md) and [TERM-077](../terms.d/TERM-077.md). Nash
clustering is a cardinal layering of a cyclic record, and Theorem 3 is a
condition for escaping a cycle ([NOTE-tmpat2ia](../notes.d/NOTE-tmpat2ia.md)). It carries
`anthology-candidate` because its subject is training agents for games.
It is filed for understanding, not as an instruction for practice.
