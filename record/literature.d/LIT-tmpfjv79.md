---
status: Active
status_note: >-
  read 2026-10-25 ([NOTE-tmpkgxba](../notes.d/NOTE-tmpkgxba.md)) in full, from the arXiv preprint v1 of 23 May 2018 (arxiv.org/pdf/1805.09247v1, 24 pp.); the ALT 2019 version (PMLR 98:529–556) was fetched and its theorem statements, footnote and contribution list compared, not read in full. Worth reading for the completed classification of finite adversarial partial-monitoring games, degenerate and duplicate actions included ([THEORY-tmpyulw1](../theory.d/THEORY-tmpyulw1.md)); for how actions that are optimal only on a boundary enter it, through the neighbourhood set and not as neighbours, and for its correction of the lower-bound proof of Bartók et al. (2014) ([THEORY-tmpwqg2f](../theory.d/THEORY-tmpwqg2f.md)); for NeighborhoodWatch2, a simpler algorithm with a high-probability √n bound; and for RelExp3 on point-locally observable games ([THEORY-tmpb4ozq](../theory.d/THEORY-tmpb4ozq.md)). Read it knowing that the arXiv text says Foster and Rakhlin and Bartók et al. "inadvertently exchanged an expectation and maximum" in their localisation argument and the published text no longer says so, though both abstracts say "correct errors in previous analyses"; that it proves only the two pieces of the classification that were missing or flawed and cites the rest; that its constants are game-dependent and can be large; and that a few small typos survive in the arXiv text.
title: 'Cleaning up the neighborhood: A full classification for adversarial partial monitoring'
version: 2
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed at the owner's request, 2026-10-25 ("register and read"), as the
    completion of Bartók et al. (LIT-tmpwpq36) that the reading of that
    paper named and did not hold. Citation checked against arXiv on
    2026-10-25: Tor Lattimore and Csaba Szepesvári, arXiv:1805.09247, v1
    submitted 23 May 2018 (the only version), cs.LG and stat.ML, 24 pages;
    `published:` is that date, per ADR-002. The published version was found
    on its PMLR page: Proceedings of the 30th International Conference on
    Algorithmic Learning Theory, PMLR 98:529–556, publication date
    2019-03-10, same title and authors. Crossref has no record of it (PMLR
    does not register DOIs), so there is no DOI. DBLP's search API and
    record page returned a bot check on 2026-10-25, and OpenAlex and
    Semantic Scholar refused for rate limits, so neither was seen. Open
    copies: arXiv, and the PMLR PDF. The summary follows the arXiv abstract.
- version: 2
  date: '2026-10-25'
  note: >-
    Read in full (NOTE-tmpkgxba), from the arXiv preprint v1, text extracted
    with pdftotext; the ALT 2019 text was compared at the level of its
    statements. Status Deferred → Active. The PMLR page is added as `url:`.
    The summary is checked against the reading and made exact: the
    classification's trivial class is "no pair of neighbouring actions", and
    what it corrects in Bartók et al. is named. THEORY-tmpyulw1 and
    THEORY-tmpwqg2f (Active, re-derived and checked numerically) and
    THEORY-tmpb4ozq (Proposed) are filed from it. `extends` and `corrects`
    name LIT-tmpwpq36.
tags:
- learning-theory
- game-theory
- anthology-candidate
date: '2026-10-25'
published: '2018-05-23'
arxiv: '1805.09247'
url: 'https://proceedings.mlr.press/v98/lattimore19a.html'
first_author: 'Lattimore'
keywords:
- 'partial monitoring'
- 'online learning'
- 'minimax regret'
- 'degenerate games'
- 'NeighborhoodWatch'
implementations: []
extends:
- LIT-tmpwpq36
corrects:
- LIT-tmpwpq36
summary: >-
  Lattimore & Szepesvári (2018; ALT 2019). Completes the classification of
  finite adversarial partial-monitoring games by minimax regret to all
  games, including the degenerate ones (with actions optimal only on a
  lower-dimensional part of the simplex) that Bartók et al. (2014) left
  open: 0 with no pair of neighbouring actions, Θ̃(√n) when locally
  observable, Θ(n^2/3) when globally but not locally observable, and Ω(n)
  otherwise. A new NeighborhoodWatch2 attains √n with high probability by
  redistributing mass onto degenerate actions in proportion to the
  neighbours they lie between. It corrects a slip in Bartók et al.'s
  T^2/3 lower-bound proof and, in the preprint's words, an exchanged
  expectation and maximum in the earlier localisation argument. A second
  algorithm, RelExp3, gives point-locally observable games an asymptotic
  √n bound free of arbitrarily large game constants, with a matching
  linear dependence on the number of feedback symbols.
---
<!-- inactive-ok-file: THEORY-tmpb4ozq — Proposed; the point-local bound, filed from this reading -->
<!-- inactive-ok-file: THEORY-tmpz3a05 — Superseded by THEORY-tmpyulw1; the classification as Bartók et al. state it, which this reading completes, nothing here rests on it -->
<!-- inactive-ok-file: CLAIM-446 — Proposed; the claim whose check variant this paper's spam game matches, named, nothing here rests on it -->
# LIT-tmpfjv79: Cleaning up the neighborhood: A full classification for adversarial partial monitoring

Lattimore, T. & Szepesvári, C. (2019). Cleaning up the neighborhood: A
full classification for adversarial partial monitoring. *Proceedings of
the 30th International Conference on Algorithmic Learning Theory*, PMLR
98: 529–556. Preprint: arXiv:1805.09247 (23 May 2018).

Read 2026-10-25 in full ([NOTE-tmpkgxba](../notes.d/NOTE-tmpkgxba.md)), from the arXiv preprint; the
published text was compared at the level of its statements. The summary
was checked against it.

## Why this is here

The owner asked on 2026-10-25 for it to be registered and read. The
reading of Bartók et al. ([LIT-tmpwpq36](LIT-tmpwpq36.md), [NOTE-tmpupizd](../notes.d/NOTE-tmpupizd.md)) left the
adversarial classification for non-degenerate games only, and named this
paper as the one that completes it and corrects the earlier analyses;
[THEORY-tmpz3a05](../theory.d/THEORY-tmpz3a05.md)'s promotion condition names it. It settles what that
reading could not: which games the classification covers, what was wrong
in the earlier proofs, and how actions that are optimal only on a
boundary count. Its spam game is the check variant of [CLAIM-446](../claims.d/CLAIM-446.md)'s
approach–avoid example, with the threshold case that the earlier
classification excluded now placed in the easy class.
