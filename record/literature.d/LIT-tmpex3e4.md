---
status: Active
status_note: >-
  read in part 2026-11-04 (NOTE-tmp4f0ld, Skimmed) from the published PDF
  on the first author's MIT CSAIL page; worth reading as the standard
  restatement, for an AI readership, of the operations-research theory of
  partially observable Markov decision processes: the belief state as a
  sufficient statistic, control as an MDP over beliefs, the
  piecewise-linear convex finite-horizon value function, and the tiger
  problem, in which a costly, noisy information action is valued inside the
  model. Registered as the stand-in for Smallwood and Sondik (1973),
  LIT-tmp7m16t, whose core finite-horizon results it restates. Its main
  limits: enumerated rather than factored states, a known model, and exact
  solution intractable in general.
title: 'Planning and acting in partially observable stochastic domains'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Registered and read on 2026-11-04 as a stand-in for Smallwood and
    Sondik (1973), LIT-tmp7m16t, whose full text could not be found, at the
    owner's request; that paper is cited in the pasted bibliography on
    emergency readiness, written by another assistant (A) and pasted by the
    owner on 2026-11-04, which does not cite this one. Citation checked
    against Crossref (10.1016/S0004-3702(98)00023-X): Leslie Pack
    Kaelbling, Michael L. Littman and Anthony R. Cassandra, Artificial
    Intelligence 101(1–2), 99–134, journal article. Crossref gives the print
    issue as 1998-05 and no online date, so `published:` is 1998-05-01; the
    PDF gives "Received 11 October 1995; received in revised form 17
    January 1998". Not held before (no hit for the DOI, the title or
    "Kaelbling"). Copy: https://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf,
    the published typeset PDF on the first author's page, 36 pages,
    extracted with pdftotext.
tags:
- operations-research
- control-theory
- probabilistic-modeling
date: '2026-11-04'
published: '1998-05-01'
doi: '10.1016/S0004-3702(98)00023-X'
first_author: 'Kaelbling'
keywords:
- 'planning'
- 'uncertainty'
- 'partially observable Markov decision processes'
- 'belief state'
- 'witness algorithm'
implementations: []
summary: >-
  Kaelbling, Littman & Cassandra (1998). An agent that cannot observe the
  state keeps a belief state, a probability distribution over states updated
  by Bayes' rule, which is a sufficient statistic for its history; control
  then becomes an MDP over beliefs. The optimal t-step value is the upper
  surface of one linear function per policy tree, so it is piecewise-linear
  and convex, and the optimal policy partitions belief space into polyhedral
  regions. The paper adds the witness algorithm and the tiger problem, where
  with two steps to go the optimal policy only listens. It credits Smallwood
  and Sondik with the belief state's sufficiency (jointly with another work)
  and an exact direct-construction algorithm that is exponential in the
  worst case.
---
<!-- inactive-ok-file: NOTE-tmp4f0ld THEORY-tmphj1kw LIT-tmp7m16t — Skimmed, Proposed or Unavailable, and new; the reading of this work, the account filed from it, and the unread original it stands in for, cited as open -->

# LIT-tmpex3e4: Planning and acting in partially observable stochastic domains

Kaelbling, L. P., Littman, M. L. & Cassandra, A. R. (1998). Planning and acting in partially observable stochastic domains. *Artificial Intelligence* 101(1–2): 99–134. doi:10.1016/S0004-3702(98)00023-X.

## Key takeaways

*From the reading, NOTE-tmp4f0ld. Page numbers are the journal's.*

- **The belief state is a sufficient statistic** "for the past history and
  initial belief state of the agent" (§3.2, p. 106), citing Smallwood and
  Sondik among others; so the optimal policy solves an MDP over beliefs.
- **The value function.** Each policy tree's value is linear in the
  belief: "So, Vt is piecewise-linear and convex" (§4.1, p. 110). The
  infinite-horizon discounted value stays convex but may have infinitely
  many facets (§4.6, p. 118).
- **Information is valued inside the model.** "there is no distinction
  drawn between actions taken to change the state of the world and actions
  taken to gain information" (§1, p. 100). In the tiger problem (§5.2) the
  optimal two-step policy never opens a door, only listens.
- **Exact solution is expensive.** Earlier direct-construction algorithms,
  Smallwood and Sondik's among them, "still have worst-case running times
  exponential in at least one of the problem parameters" (§4.4, p. 114).

## Standing in the record

Registered as the stand-in for Smallwood and Sondik (1973), LIT-tmp7m16t,
which the pasted bibliography on emergency readiness cites and which could
not be found. It restates that paper's core finite-horizon results in the
same framework, but derives the piecewise-linear convex value function
itself and gives none of the original's own algorithm, proofs or examples.
Filed from it: THEORY-tmphj1kw. It is the standard formal reference for the
structure of CASE-153 (a hidden binary state and a costly, noisy
inspection).
