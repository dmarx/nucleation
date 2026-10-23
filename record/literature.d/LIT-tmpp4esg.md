---
status: Unavailable
status_note: 'registered 2026-10-23 from Crossref, not read: a lawful copy exists but this client could not fetch it, so this failed on access, not availability. OpenAlex lists the paper as closed, with no repository copy. The publisher (ScienceDirect) is paywalled. Two course-page copies were found: Frieze''s INFONET reading list at math.cmu.edu and a Bowdoin course page (tildesites.bowdoin.edu, ~mirfan/files/3210). Both failed TLS certificate verification from this client, and a second fetcher got HTTP 503 from both. An author upload on ResearchGate (Monderer''s) was not tried, and Unpaywall was skipped because it requires an email address. Its central lemma, that a finite game has the finite improvement property exactly when it has a generalized ordinal potential, is held only as later papers restate it: Duersch, Oechssler and Schipper (arXiv 1003.4274) attribute it to Lemma 2.5, and Candogan et al. (LIT-tmp7pue2) restate its equilibrium results. The record''s own proof of the finite case is in THEORY-tmpj4ciq. Filed because the record is renaming "ascendancy" to "potential" in this paper''s sense. It stays Unavailable until a copy is supplied, not on merit; either course copy, fetched by hand, would clear it.'
title: 'Potential Games'
version: 1
history:
- version: 1
  date: '2026-10-23'
  note: >-
    Registered, not read. Details checked against Crossref (DOI
    10.1006/game.1996.0044: Games and Economic Behavior 14(1):124–143, May
    1996, Monderer and Shapley). `published:` is the first of the issue
    month, Crossref giving no day. No duplicate was found in literature.d
    by title, DOI or author.
tags:
- game-theory
- mathematics
date: '2026-10-23'
published: '1996-05-01'
doi: '10.1006/game.1996.0044'
first_author: 'Monderer'
keywords:
- 'potential games'
- 'exact potential'
- 'weighted potential'
- 'ordinal potential'
- 'generalized ordinal potential'
- 'finite improvement property'
- 'congestion games'
implementations: []
summary: >-
  Monderer & Shapley (1996), Games and Economic Behavior 14:124–143. The
  paper defines exact, weighted, ordinal and generalized ordinal
  potentials for games in strategic form, and it is reported (Lemma 2.5,
  per Duersch et al.) to show that a finite game has the finite
  improvement property exactly when it has a generalized ordinal
  potential. Unread: no lawful copy was reached by this client.
extended_by:
- LIT-tmp7pue2
---
<!-- inactive-ok-file: THEORY-tmpj4ciq LIT-tmp7pue2 — Proposed or draft; filed in this batch -->
<!-- inactive-ok-file: TERM-tmp8gbrt CLAIM-tmpz8lli QUESTION-tmpsqwu5 — Proposed or Open; the term, claim and question whose vocabulary this paper supplies, cited as open -->

# LIT-tmpp4esg: Potential Games

Dov Monderer and Lloyd S. Shapley (1996), *Games and Economic Behavior*
14(1):124–143, DOI-10.1006/game.1996.0044

## Key takeaways

*Registered, not read.* What follows comes from papers that restate it.
None of it is checked against the paper.

- **Four kinds of potential.** An *exact* potential is a real function φ
  on strategy profiles whose change, when one player deviates, equals that
  player's change in payoff. Candogan et al. (LIT-tmp7pue2, Definition
  2.1, p. 6) give this definition and credit it to this paper. A
  *weighted* potential matches each player's payoff change up to a
  positive player-specific weight. An *ordinal* potential matches its
  sign. A *generalized ordinal* potential need only rise whenever the
  deviating player's payoff strictly rises. Every restatement read gives
  each of these as a real-valued function.
- **The finite improvement property (FIP).** An improvement path is a
  sequence of profiles in which each step is a strict unilateral
  improvement by the player who moves. A game has the FIP if every such
  path is finite. Duersch, Oechssler and Schipper (arXiv 1003.4274,
  p. 18 of the arXiv PDF) report: "Monderer and Shapley (1996, Lemma 2.5)
  show that a finite strategic game has no strict improvement cycle (what
  they call the finite improvement property) if and only if it is a
  generalized ordinal potential game." Biggar and Shames (arXiv 2502.03546,
  p. 18) report it more weakly: "Monderer and Shapley (1996b) show that
  ordinal potential games satisfy the ‘finite improvement property’". The
  lemma's exact wording, number and page are therefore not confirmed.
- **Equilibria and dynamics.** Candogan et al. restate as their Theorem
  5.2, citing this paper, that a potential game has the same equilibria as
  the game in which every player's payoff is the potential, and so has a
  pure Nash equilibrium (p. 22). They also say that fictitious play and
  best-response dynamics "converges in potential games", citing this paper
  among others (p. 23).

## Standing in the record

Filed on 2026-10-23 at the owner's request, as the source of the formal
sense of "potential" that the record is adopting for "an ordering prevails
in the negotiation among a system's perspectives" (TERM-tmp8gbrt,
CLAIM-tmpz8lli, QUESTION-tmpsqwu5). THEORY-tmpj4ciq states the
FIP equivalence for finite games and proves it in the record, so the
result does not wait on this copy. Its attribution, wording and numbering
do.
