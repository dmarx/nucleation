---
number: 95
status: Open
formerly:
- QUESTION-tmp1mkzc
title: Is leaving the result of a computation where it can be cheaply retrieved
  the same trade as amortizing the computation, and does one account of when it
  pays cover a crew's speed bugs, a record's filed arguments and a reasoner's reused
  inferences?
version: 2
history:
- version: 2
  date: '2026-11-10'
  note: >-
    Carries nucleating-argument as well, at the sweep of ADR-085's
    rule (2026-11-10): the entry takes part in that line's argument,
    through the first line of an entry it names:
    nucleating-argument, since it refines QUESTION-098. No other
    change.
tags:
- cognition
- embodied-cognition
- information-theory
date: '2026-10-15'
line:
- distributed-agency
- nucleating-argument
refines:
- QUESTION-098
summary: >-
  The owner, after reading Hutchins's cockpit paper: "amortized retrieval is actually
  a kind of amortized computation". The speed bugs are computed once at low load
  and read back as a judgement of spatial adjacency. [CLAIM-303](../claims.d/CLAIM-303.md) said filing
  moves work across time; [TERM-055](../terms.d/TERM-055.md)'s note said retrieval can be done before
  the request. This asks whether those are one trade, and which literature has formalized
  it.
---
<!-- inactive-ok-file: THEORY-tmp3jjfo THEORY-tmpgxdpz THEORY-tmpvarvt THEORY-tmpdzbq1 THEORY-tmplz597 THEORY-tmpc6xzg THEORY-tmp6v6q8 — Proposed; the readings of 2026-11-12, cited in its note -->
<!-- inactive-ok-file: CASE-tmp40vka CASE-tmp3isyl CLAIM-tmpnwq8a — Proposed; filed on 2026-11-12 from "Identify Synthesis Opportunities", cited in its note -->
<!-- inactive-ok-file: CLAIM-295 CLAIM-303 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# QUESTION-095: Is leaving the result of a computation where it can be cheaply retrieved the same trade as amortizing the computation, and does one account of when it pays cover a crew's speed bugs, a record's filed arguments and a reasoner's reused inferences?

## Why it is a question

The owner, 2026-10-15, after the cockpit reading ([LIT-1066](../literature.d/LIT-1066.md), [NOTE-867](../notes.d/NOTE-867.md)):
"the cockpit case is interesting, and I think also illustrates how
amortized retrieval is actually a kind of amortized computation. there's
probably a clearer relationship here that I imagine has likely been
clarified/formalized at some point in the 30 years since the cockpit
essay was published."

Three things the record holds look like one trade:

- **The cockpit.** Speeds computed 25–30 minutes before landing, at low
  workload, and left as bugs on the airspeed indicators, so that using
  them later is a perceptual judgement, not recall and scale reading.
- **Filing.** [CLAIM-303](../claims.d/CLAIM-303.md): filing an argument pays now against
  reconstruction later, worth it when expected reuse covers it.
  [QUESTION-098](QUESTION-098.md) asks when.
- **Availability.** [TERM-055](../terms.d/TERM-055.md)'s α starts its clock at the request; the
  note of 2026-10-15 there says work done earlier and left in the
  environment raises it.

The candidate unification: retrieval cost is computation, so storing a
result where reading it back is cheap is memoization, and its value has
the two parts [CLAIM-295](../claims.d/CLAIM-295.md) separates, informational (a result is kept)
and computational (a cheap operation replaces an expensive one). What it
costs is staleness: a reused result can be wrong for the query at hand.

Literatures that may already hold it, registered for this question and read the same day (note below):

- **Amortized inference.** Dasgupta, Schulz, Goodman and Gershman 2018
  ([LIT-1074](../literature.d/LIT-1074.md)) and Gershman and Goodman 2014 ([LIT-1056](../literature.d/LIT-1056.md)): reasoners reuse
  past inferences on related queries. The 2014 paper shows reuse faster
  and dependent on the earlier answer; the 2018 paper shows the earlier
  computation's error carried over, at a cost in bias.
- **Offloading into the world.** Kirsh and Maglio 1994 ([LIT-1054](../literature.d/LIT-1054.md)),
  Kirsh 1995 ([LIT-1076](../literature.d/LIT-1076.md)), Ballard et al. 1997 ([LIT-1075](../literature.d/LIT-1075.md)), Risko and
  Gilbert 2016 ([LIT-1059](../literature.d/LIT-1059.md)).
- **Choosing head or world by cost.** Gray and Fu 2004 ([LIT-1058](../literature.d/LIT-1058.md)),
  where people take cheaper, worse memory over dearer, perfect information
  in the world; Lieder and Griffiths 2020 ([LIT-1071](../literature.d/LIT-1071.md)), cognition as the
  optimal use of limited computation.

An answer would say whether one cost model covers the three (precompute
cost, storage and upkeep, retrieval cost, staleness risk, expected reuse),
or name where they differ. Speed bugs are read by perception, a filed
argument by search and reading, a reused inference by internal memory,
and the retrieval costs and failure modes differ. It would also say
whether anyone has already joined the distributed-cognition and
amortized-inference literatures, which is checked as part of this
reading pass.

## Note of 2026-10-15: what the eight readings found

All eight were read (NOTEs filed the same day). None of them joins the
two literatures with a cost model, and they split the proposed single
trade into four strategies, separated by when the work is done and what
is left behind:

| strategy | example | work done | what is left |
|---|---|---|---|
| precompute and leave a result | the cockpit's speed bugs ([LIT-1066](../literature.d/LIT-1066.md)) | before the request | a computed result |
| maintain structure that makes search cheap | Kirsh 1995's grouping, O(N) to O(log N) ([LIT-1076](../literature.d/LIT-1076.md)) | over the task | an arrangement |
| offload at the moment of use | Tetris rotation ([LIT-1054](../literature.d/LIT-1054.md)) | during the task, once | nothing |
| defer and re-read | Ballard et al.'s block copying ([LIT-1075](../literature.d/LIT-1075.md)) | when needed | the raw input |

Amortized inference ([LIT-1056](../literature.d/LIT-1056.md), [LIT-1074](../literature.d/LIT-1074.md)) is the first strategy
with the store inside the head, and its models give retrieval no cost.
Kirsh comes closest to the owner's point, citing Tarjan's amortized
analysis for workspace structuring, but says the savings cannot "in
general" be quantified. Lieder and Griffiths' objective ([LIT-1071](../literature.d/LIT-1071.md)) could
host the trade but is per episode, with no terms for precomputation,
storage, retrieval or staleness; it treats the cost of finding a strategy
as already paid, itself an amortization. Gray and Fu ([LIT-1058](../literature.d/LIT-1058.md)) price
only read-back: people take the cheaper route, and check finished work
from memory, even when the display is perfect. Risko and Gilbert
([LIT-1059](../literature.d/LIT-1059.md)) add that offloading erodes the internal route over time,
a cost [CLAIM-303](../claims.d/CLAIM-303.md)'s fixed reconstruction cost leaves out.

What a single account would need, from these: a term for how predictable
the later query is (the cockpit's is fixed and known; Ballard's
"cannot" be precomputed), a retrieval cost that includes search, a
staleness or bias cost on reuse, and a term for the erosion of the
alternative. The four strategies would then be regimes of one trade,
which is the owner's conjecture, stated so that it can fail.

## Note of 2026-10-15: has anyone joined them? A citation search

Citation data (OpenCitations, fourteen seed works, both literatures) found
no indexed work that cites Dasgupta et al. 2018, or Dasgupta and Gershman
2021, together with any offloading or distributed-cognition source. The
bridges that exist run through resource rationality and price cognitive
effort, not the reuse of a result. Pieces, none registered here yet:

- Gray, Sims, Fu and Schoelles 2006 (Psychological Review 113, 461–482,
  doi:10.1037/0033-295X.113.3.461): the nearest formal head-or-world cost
  model, deciding each access separately, with no precompute, reuse or
  staleness term.
- Kirsh 1996, "Adapting the environment instead of oneself" (Adaptive
  Behavior 4, 415–452, doi:10.1177/105971239600400307): the owner's
  intuition from inside distributed cognition, leaving tools in place to
  "amortize the cost of search", named and not modelled.
- Dasgupta and Gershman 2021, "Memory as a computational resource" (Trends
  in Cognitive Sciences 25, 240–251, doi:10.1016/j.tics.2020.12.008):
  memoization and amortization across domains, internal memory only, and
  none of its references is an offloading source.
- Also: Gilbert et al. 2020 on optimal reminders (single use), Russell et
  al. 1993 on the cost structure of sensemaking, and Anderson and Milson
  1989, whose need probability is the formal "expected reuse" for internal
  memory.

The search could not reach OpenAlex or Semantic Scholar, so Gershman and
Goodman 2014's citers were not checked. On what it could check, the answer
to whether this has been formalized is: in parts, not as one trade.

## Note of 2026-10-15: the three works the search found, read

- Gray, Sims, Fu and Schoelles 2006 ([LIT-1073](../literature.d/LIT-1073.md), [NOTE-868](../notes.d/NOTE-868.md)). The search
  note above says the model decides "each access separately". Each look is
  one decision, but it is valued against the whole trial, so the cost of
  forgetting and looking again is priced in ahead. It has no term for
  precomputation, reuse across trials or staleness; the paper uses
  "amortized" twice, unmodelled.
- Kirsh 1996 ([LIT-1057](../literature.d/LIT-1057.md), [NOTE-872](../notes.d/NOTE-872.md)). "Amortize" occurs once, in an
  aside; the paper's economics is a verbal rule with an "interest factor"
  for risk, one risk being that a stored change is not "still present
  later". It fits the maintained-structure strategy, not the precomputed
  result. The citation of Tarjan's amortized analysis is Kirsh 1995's.
- Dasgupta and Gershman 2021 ([LIT-1077](../literature.d/LIT-1077.md), [NOTE-865](../notes.d/NOTE-865.md)). A vocabulary for
  the first strategy with the store inside the head, retrieval nearly free.
  It adds staleness proper, values "not yet updated" after the world
  changes, beside the bias from a similar earlier query, so a cost model
  needs both.


## Note of 2026-10-15: scaling laws price two of the terms

The owner pointed to "valuation of pre-training investment (amortized
compute) vs inference time search/compute". Three works were read; the
anthology holds Kaplan et al. ([ANTH-LIT-028](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-028.md)), Hoffmann et al.
([ANTH-LIT-068](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-068.md)) and Noise Hypernetworks ([ANTH-LIT-491](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-491.md)), which are not
refiled here.

- **Jones 2021** ([LIT-1069](../literature.d/LIT-1069.md), [NOTE-884](../notes.d/NOTE-884.md)) measures the exchange
  rate within one system: on 9×9 Hex, each extra 10× of training compute
  removes about 15× of test-time search at fixed strength, down to a
  one-node search. Precomputing into the weights and computing at the
  moment of use lie on one straight log–log curve, the shape the owner's
  conjecture predicts for those two strategies. It counts no games played.
- **Sardana et al. 2024** ([LIT-1070](../literature.d/LIT-1070.md), [NOTE-881](../notes.d/NOTE-881.md)) adds expected reuse
  explicitly: minimize training plus lifetime inference compute at fixed
  quality, and with enough demand a smaller model trained longer wins (28%
  less compute at 30B quality and 10¹³ inference tokens; 34–58% in
  dollars). The dial is continuous, not file-or-not, which narrows
  [CLAIM-303](../claims.d/CLAIM-303.md)'s break-even. Demand is assumed known in advance.
- **Snell et al. 2024** ([LIT-1063](../literature.d/LIT-1063.md), [NOTE-869](../notes.d/NOTE-869.md)) spreads a larger
  model's extra pretraining over the ratio of inference to pretraining
  tokens; test-time compute wins only when that ratio is low and on
  easier questions. The larger model also pays more per inference token,
  a retrieval cost the amortized-inference readings lacked.

Of the terms listed above, these price expected reuse and per-use
(retrieval) cost. None has staleness, uncertainty about future demand or
erosion of the alternative. In all three the precomputed thing is a
cheaper computation, not a stored answer, so they are the
maintained-capacity case more than the memo-table case.

## Note of 2026-10-15: Howes et al. 2016, read

Lieder and Griffiths cited Howes et al. ([LIT-1062](../literature.d/LIT-1062.md), [NOTE-882](../notes.d/NOTE-882.md)) as a
memorize-or-look-up trade. It is not one: there is no look-up option, and
the choice is how many items to hold per trial against the reward rate.
People mostly chose the length that paid best for them (55% and 46% of
choices, against 8–17% for the neighbouring lengths). It adds a priced error cost,
which did not move behaviour, and none of the question's other terms.


## Note of 2026-11-12: a practitioner's version of the trade, from "Identify Synthesis Opportunities"

At U6 of the exchange of 2026-11-08 (https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44) the owner offered a case "illustrating how changing resource costs changes the incentive to compute on demand or learn and amortize via memory": a 2026 Reddit thread on keeping a character consistent in image generation with a reference-conditioned model instead of a trained character LoRA, and, at U7, the earlier generations of the same choice. Filed as [CASE-tmp40vka](../cases.d/CASE-tmp40vka.md), with A's proposal to measure the crossover as [CASE-tmp3isyl](../cases.d/CASE-tmp3isyl.md).

- **It adds a domain with three strategies in view**: a LoRA, work moved into weights and cheap per use, which is the scaling readings' "cheaper computation, not a stored answer"; a reference sheet, made once and interpreted at every use; and raw references, nothing kept. A16 put it as "both are forms of memory, but they move different amounts of work into each generation."
- **It adds a change in costs over time.** The scaling readings fix the technology and vary demand. The case asks how a change in per-use cost across model generations moves the break-even, which none of the readings above measures.
- **It does not settle anything.** The thread could not be read here (it redirected to a login page on 2026-11-12), and A's report of it is unverified. A: "the thread doesn't establish a controlled cost-and-quality comparison."

The assistant (Claude, in the filing session) added a staleness term the readings lack, filed as [CLAIM-tmpnwq8a](../claims.d/CLAIM-tmpnwq8a.md), Proposed: a specialization learned into weights goes stale when its base model is replaced, while what it encodes stays right, so the reader's turnover caps expected reuse. Its proposed test is a transfer arm in [CASE-tmp3isyl](../cases.d/CASE-tmp3isyl.md)'s design. The reading of IP-Adapter, its one piece of evidence so far, is still owed.

The question stays Open.

## Note of 2026-11-12: seven works on character identity, read

The works registered with CASE-tmp40vka were read; each THEORY bears on
this question.

- **Amortization across users.** The question's cases price one agent's
  own reuse: the crew's bugs, the record's filings, a reasoner's
  inferences. The reference routes amortize across agents. A module's
  maker trains once (IP-Adapter, THEORY-tmp3jjfo; InstantID,
  THEORY-tmpgxdpz, on 48 H800s; PhotoMaker, THEORY-tmpvarvt, on 8 A100s for
  two weeks), and every user pays only per use, with no per-subject
  training. A single account would need a term for who pays the fixed
  cost and over how many users it is spread. THEORY-331's lifetime
  objective is the provider's version of that.
- **The trade, in its authors' words.** Textual Inversion
  (THEORY-tmpc6xzg): "we can optimize a single pseudo-word and re-use it
  for a multitude of new generations. The baseline models, meanwhile, use
  CLIP for test-time optimization and thus require expensive optimization
  for every new creation."
- **Two costs the readings above did not price.** Storage, on the learned
  side: InstantID names "high storage demands" among the costs of
  per-subject training, and LoRA (THEORY-tmp6v6q8) shrinks it, about 35MB
  against 350GB per task on GPT-3. And erosion of what the store held
  before: DreamBooth's language drift (THEORY-tmplz597), in which the
  model "slowly forgets how to generate subjects of the same class as the
  target subject", paid for with a second loss.
- **An analogue already held.** THEORY-439 (LIT-796): for language models,
  examples used as context and the same examples used as a temporary weight
  update "are not interchangeable". It now bears on this question.

The question stays Open.
