---
status: Active
status_note: >-
  read in full 2026-10-24 ([NOTE-tmpcqwez](../notes.d/NOTE-tmpcqwez.md)) from the authors' working paper of
  October 1995, as held in Levine's Working Paper Archive; worth reading
  as the proved source of "Cross learning is the replicator dynamic": a
  single Bush–Mosteller learner with positive payoffs moves in expectation
  exactly as a population under the discrete replicator dynamic, and in the
  continuous-time limit follows the continuous replicator dynamic on any
  finite horizon. Two limits matter as much as the result. Asymptotically
  the discrete learner is absorbed in a pure strategy profile with
  probability one at every learning speed, even in matching pennies where
  the replicator dynamic cycles; and with negative payoffs a second force,
  probability matching, enters beside the replicator term.
title: 'Learning Through Reinforcement and Replicator Dynamics'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Filed and read 2026-10-24 for the owner's question how the record
    stands on multi-agent reinforcement learning. Citation checked against
    Crossref (doi:10.1006/jeth.1997.2319): Tilman Börgers and Rajiv Sarin,
    Journal of Economic Theory 77(1):1–14, November 1997 (Crossref gives
    only the month). Read in full from the working paper, "First Version:
    October 1993, This Version: October 1995", 31 pp., fetched from
    Levine's Working Paper Archive (www.dklevine.com/archive/refs4380.pdf,
    indexed by RePEc as cla:levarc:380) and extracted by pdftotext; Figure
    1 and part of Section 6 are scanned and were read from the extracted
    text where legible. The ELSE working-paper copy RePEc lists
    (ftp.repec.org/RePEc/els/esrcls/replic.pdf) could not be reached (FTP
    connection timed out). Unpaywall and OpenAlex list the journal version
    as closed, and it was not read, so differences from it are not known;
    the working paper acknowledges an associate editor and two referees,
    so it is at least a revised version. `published:` is the first
    version's month, October 1993, the earliest date any source gives
    (ADR-002), with no day; the journal issue is November 1997. A grep of
    record/literature.d for the DOI, "Börgers", "Sarin" and the title found
    nothing.
tags:
- game-theory
- learning-and-conditioning
date: '2026-10-24'
published: '1993-10-01'
doi: '10.1006/jeth.1997.2319'
url: 'http://www.dklevine.com/archive/refs4380.pdf'
first_author: 'Börgers'
keywords:
- 'Bush–Mosteller learning'
- 'Cross learning'
- 'replicator dynamics'
- 'continuous time limit'
- 'stimulus sampling'
- 'probability matching'
- 'learning and evolution'
implementations: []
summary: >-
  Börgers & Sarin (1997; working paper 1993). For two players each
  running Cross's version of Bush–Mosteller learning with payoffs in
  (0, 1), the expected change of each player's mixed strategy equals the
  discrete replicator step of a two-population biological model, and
  in the continuous-time limit the learning process converges in
  probability to the continuous (Taylor) replicator dynamic at every
  finite time. Asymptotically it does not: the discrete process is
  absorbed in a pure strategy profile with probability one for every
  learning speed. With negative payoffs the limit adds a
  probability-matching term to a replicator term in "benefits".
---
<!-- inactive-ok-file: NOTE-tmpcqwez THEORY-tmphhvqf THEORY-tmpbq2nj THEORY-tmp3oyxw CLAIM-tmp1xoac — filed from this reading or Proposed; named -->

# LIT-tmp6d9wu: Learning Through Reinforcement and Replicator Dynamics

Börgers, T. & Sarin, R. (1997). Learning through reinforcement and
replicator dynamics. *Journal of Economic Theory* 77(1): 1–14.
doi:10.1006/jeth.1997.2319. Working paper, October 1993 and October 1995.

## Key takeaways

*From the reading, [NOTE-tmpcqwez](../notes.d/NOTE-tmpcqwez.md). Page numbers are the 1995 working paper's.*

- **Expected motion is the replicator step.** In Cross's model a player
  who plays j and receives payoff U ∈ (0, 1) moves her mixed strategy a
  fraction U of the way to the vertex j. Her expected change is
  p_j(e_j U q − p U q), exactly the movement of a population in a
  biological model in which offspring equal payoffs (Propositions 1 and 3,
  pp. 8, 11).
- **The limit holds on finite horizons only.** With step size θ → 0 and
  nθ → t, the learning process converges in probability to the continuous
  Taylor replicator dynamic at t (Proposition 4, via Norman's theorem). But
  for every θ > 0 it converges with probability one to a pure strategy
  pair (Proposition 5), including matching pennies, where the replicator
  dynamic cycles ([THEORY-tmphhvqf](../theory.d/THEORY-tmphhvqf.md)).
- **A population of ideas in one mind.** Read through Estes's stimulus
  sampling, the learner is a population of stimuli, one sampled each
  period and re-programmed in proportion to the payoff. The analogy is
  individual learning with biological evolution, not imitation in a
  population (Section 4).
- **Negative payoffs add probability matching.** The limit is a
  replicator term in "benefits" plus a term that alone would equate each
  strategy's choice probability with its probability of success, which is
  "often irrational behavior" (p. 5; [THEORY-tmpbq2nj](../theory.d/THEORY-tmpbq2nj.md)).

## Why this is here

Filed 2026-10-24 when the owner asked how the record stands on multi-agent
reinforcement learning. It is the source the record's replicator reading
of authority ([CASE-tmpw4r7u](../cases.d/CASE-tmpw4r7u.md), [CLAIM-tmp1xoac](../claims.d/CLAIM-tmp1xoac.md)) and Soma et al.'s Proposition 1
([THEORY-tmp3oyxw](../theory.d/THEORY-tmp3oyxw.md)) inherit "Cross learning is the replicator dynamic" from.
Its asymptotic result is the record's lock-in worry in a single learner:
the expected dynamic can cycle or stay interior while every sample path is
absorbed in a vertex.
