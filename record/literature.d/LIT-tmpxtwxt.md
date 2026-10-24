---
status: Active
status_note: >-
  read in full 2026-10-24 (NOTE-tmp7qq6n) from the published article as
  posted on Sergiu Hart's homepage; worth reading as the theorem that
  correlated equilibrium is reachable by simple adaptive play: if every
  player switches from its last action to each alternative with
  probability proportional to its positive regret for not having made that
  switch in the past, the empirical joint distribution of play converges
  almost surely to the set of correlated equilibria. No device, no
  forecasts and no best replies are needed; the common history is the
  correlating device. The limits matter: convergence is to the set, not to
  a point; correlated equilibria that are interior and not pure Nash
  cannot be the limit of the empirical distribution; and the players must
  observe one another's past play.
title: 'A Simple Adaptive Procedure Leading to Correlated Equilibrium'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Filed and read 2026-10-24 for the owner's question how the record
    stands on multi-agent reinforcement learning, for its bearing on
    THEORY-414. Citation checked against Crossref
    (doi:10.1111/1468-0262.00153): Sergiu Hart and Andreu Mas-Colell,
    Econometrica 68(5):1127–1150, September 2000 (Crossref gives only the
    month). Read in full from the typeset article as posted on the first
    author's homepage (www.ma.huji.ac.il/hart/papers/adapt.pdf, fetched
    over http; the https certificate did not match the host), 24 pp.,
    extracted by pdftotext. Unpaywall lists the Universitat Pompeu Fabra
    working paper (econ-papers.upf.edu, paper 200, CC BY-NC-ND) as the open
    copy; its file links returned nothing to this client and it was not
    needed. Footnote 1 dates the paper "October 1998 (minor corrections:
    June 1999). Previous versions: February 1998; November 1997; December
    1996; March 1996 (handout)". `published:` is the earliest of these,
    March 1996, without a day (ADR-002: the earlier date when unsure); the
    journal issue is September 2000. A grep of record/literature.d for the
    DOI, "Mas-Colell", "regret" and the title found nothing.
tags:
- game-theory
- learning-theory
- anthology-candidate
date: '2026-10-24'
published: '1996-03-01'
doi: '10.1111/1468-0262.00153'
url: 'http://www.ma.huji.ac.il/hart/papers/adapt.pdf'
first_author: 'Hart'
keywords:
- 'adaptive procedure'
- 'correlated equilibrium'
- 'no regret'
- 'regret-matching'
- 'simple strategies'
- 'Blackwell approachability'
implementations: []
summary: >-
  Hart & Mas-Colell (Econometrica 2000; handout 1996). Regret matching: each
  period a player who last played j switches to k with probability
  R_t(j, k)/μ, the positive part of its average gain had it played k
  whenever it played j, and otherwise repeats j. If all players do so, the
  empirical distribution of play converges almost surely to the set of
  correlated equilibria. The proof runs through Blackwell's approachability
  theorem; regrets vanish exactly when the empirical distribution
  approaches the correlated-equilibrium set. Inertia, a positive probability
  of repeating, is needed for the result.
---
<!-- inactive-ok-file: NOTE-tmp7qq6n THEORY-tmpri5hl THEORY-414 — filed from this reading, or Proposed and named -->

# LIT-tmpxtwxt: A Simple Adaptive Procedure Leading to Correlated Equilibrium

Hart, S. & Mas-Colell, A. (2000). A simple adaptive procedure leading to
correlated equilibrium. *Econometrica* 68(5): 1127–1150.
doi:10.1111/1468-0262.00153.

## Key takeaways

*From the reading, NOTE-tmp7qq6n. Page numbers are the journal's.*

- **Regret matching.** A player's regret R_t(j, k) is the positive part of
  how much better its average payoff would have been had it played k every
  time it played j. Next period it switches from its last action j to k
  with probability R_t(j, k)/μ, and otherwise repeats j (Eq. 2.2, p. 1130).
- **The theorem.** If every player does this, the empirical distribution
  of play converges almost surely to the set of correlated equilibria
  (Main Theorem, p. 1131; THEORY-tmpri5hl).
- **Regret and correlated equilibrium are the same condition.** All
  conditional regrets tend to zero exactly when the empirical distribution
  approaches the correlated-equilibrium set (Proposition, pp. 1133–1134).
- **The device is the history.** "In our procedure, as in most others,
  there is a natural coordination device: the common history, observed by
  all players" (p. 1129).
- **Limits.** Convergence is to a set and need not be to a point; interior
  correlated equilibria that are not pure Nash equilibria cannot be the
  limit of the empirical distribution (p. 1132); and without inertia the
  result fails (p. 1141).

## Why this is here

Filed 2026-10-24 when the owner asked how the record stands on multi-agent
reinforcement learning. THEORY-414 reads institutions as correlated
equilibria that the players represent as rules. This paper shows how a
correlated equilibrium can be reached with no device and no representation
at all, which bears on which half of THEORY-414 does the work. It carries
`anthology-candidate` because regret matching underlies counterfactual
regret minimization in game-playing AI. It carries no instruction for ML
practice.
