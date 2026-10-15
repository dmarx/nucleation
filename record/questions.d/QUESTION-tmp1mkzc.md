---
status: Open
title: Is leaving the result of a computation where it can be cheaply retrieved
  the same trade as amortizing the computation, and does one account of when it
  pays cover a crew's speed bugs, a record's filed arguments and a reasoner's reused
  inferences?
version: 1
tags:
- cognition
- embodied-cognition
- information-theory
date: '2026-10-15'
line: distributed-agency
refines:
- QUESTION-tmp2vbup
summary: >-
  The owner, after reading Hutchins's cockpit paper: "amortized retrieval is actually
  a kind of amortized computation". The speed bugs are computed once at low load
  and read back as a judgement of spatial adjacency. [CLAIM-tmpygqjz](../claims.d/CLAIM-tmpygqjz.md) said filing
  moves work across time; [TERM-tmp5f7cu](../terms.d/TERM-tmp5f7cu.md)'s note said retrieval can be done before
  the request. This asks whether those are one trade, and which literature has formalized
  it.
---
<!-- inactive-ok-file: LIT-tmp5hdul LIT-tmpbbd7f LIT-tmpbhj79 LIT-tmppqntw LIT-tmpt2ql7 LIT-tmptejau LIT-tmpvpm24 — Deferred; works registered unread, cited for what they would be read for, not leaned on -->
<!-- inactive-ok-file: CLAIM-tmp7t44x CLAIM-tmpygqjz — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# QUESTION-tmp1mkzc: Is leaving the result of a computation where it can be cheaply retrieved the same trade as amortizing the computation, and does one account of when it pays cover a crew's speed bugs, a record's filed arguments and a reasoner's reused inferences?

## Why it is a question

The owner, 2026-10-15, after the cockpit reading ([LIT-tmpn2s1p](../literature.d/LIT-tmpn2s1p.md), [NOTE-tmpav8gn](../notes.d/NOTE-tmpav8gn.md)):
"the cockpit case is interesting, and I think also illustrates how
amortized retrieval is actually a kind of amortized computation. there's
probably a clearer relationship here that I imagine has likely been
clarified/formalized at some point in the 30 years since the cockpit
essay was published."

Three things the record holds look like one trade:

- **The cockpit.** Speeds computed 25–30 minutes before landing, at low
  workload, and left as bugs on the airspeed indicators, so that using
  them later is a perceptual judgement, not recall and scale reading.
- **Filing.** [CLAIM-tmpygqjz](../claims.d/CLAIM-tmpygqjz.md): filing an argument pays now against
  reconstruction later, worth it when expected reuse covers it.
  [QUESTION-tmp2vbup](QUESTION-tmp2vbup.md) asks when.
- **Availability.** [TERM-tmp5f7cu](../terms.d/TERM-tmp5f7cu.md)'s α starts its clock at the request; the
  note of 2026-10-15 there says work done earlier and left in the
  environment raises it.

The candidate unification: retrieval cost is computation, so storing a
result where reading it back is cheap is memoization, and its value has
the two parts [CLAIM-tmp7t44x](../claims.d/CLAIM-tmp7t44x.md) separates, informational (a result is kept)
and computational (a cheap operation replaces an expensive one). What it
costs is staleness: a reused result can be wrong for the query at hand.

Literatures that may already hold it, registered unread for this question:

- **Amortized inference.** Dasgupta, Schulz, Goodman and Gershman 2018
  ([LIT-tmpt2ql7](../literature.d/LIT-tmpt2ql7.md)), with Gershman and Goodman 2014 to be registered once its
  citation is confirmed: reasoners reuse past inferences on related
  queries, faster and biased toward earlier answers.
- **Offloading into the world.** Kirsh and Maglio 1994 ([LIT-tmp5hdul](../literature.d/LIT-tmp5hdul.md)),
  Kirsh 1995 ([LIT-tmpvpm24](../literature.d/LIT-tmpvpm24.md)), Ballard et al. 1997 ([LIT-tmptejau](../literature.d/LIT-tmptejau.md)), Risko and
  Gilbert 2016 ([LIT-tmpbhj79](../literature.d/LIT-tmpbhj79.md)).
- **Choosing head or world by cost.** Gray and Fu 2004 ([LIT-tmpbbd7f](../literature.d/LIT-tmpbbd7f.md)),
  where people take cheaper, worse memory over dearer, perfect information
  in the world; Lieder and Griffiths 2020 ([LIT-tmppqntw](../literature.d/LIT-tmppqntw.md)), cognition as the
  optimal use of limited computation.

An answer would say whether one cost model covers the three (precompute
cost, storage and upkeep, retrieval cost, staleness risk, expected reuse),
or name where they differ. Speed bugs are read by perception, a filed
argument by search and reading, a reused inference by internal memory,
and the retrieval costs and failure modes differ. It would also say
whether anyone has already joined the distributed-cognition and
amortized-inference literatures, which is checked as part of this
reading pass.
