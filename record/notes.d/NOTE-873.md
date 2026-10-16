---
number: 873
status: Read
formerly:
- NOTE-tmpmd0yp
paper: LIT-1071
title: Lieder & Griffiths — Resource-rational analysis
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read on 2026-10-15 from the publisher's typeset PDF of the whole BBS treatment
    (Behavioral and Brain Sciences 43, e1: 1–60; target article, 25 commentaries
    e2–e26, Authors' Response e27, references), posted by the Griffiths lab on its
    publications page (cocosci.princeton.edu/publications.php, "(pdf)" link to cocosci.princeton.edu/papers/lieder_resource.pdf;
    60 pp., sha256 6c61b43d…3680). The PDF carries a Cambridge Core download stamp
    (Welch Medical Library, 11 Mar 2020); it is the version of record, not a preprint.
    Where else I looked, 2026-10-15: Unpaywall (is_oa false, no location); OpenAlex
    (closed; an MPG.PuRe handle 21.11116/0000-0006-FA0D-3, submitted version, whose
    landing page pure.mpg.de/pubman/item/item_3247494 returned 403); Semantic Scholar
    (its openAccessPdf, doi 10.31234/osf.io/nuedj, is Theriault et al.'s commentary
    e26, not the target; the arXiv id it lists, 1905.05176, is Moreira et al.'s
    commentary e17); re.is.mpg.de (proxy 502). Text extracted with pdftotext; Equations
    1–4 are garbled by extraction and were checked against a page image of p. 5.
    Read in full: the target article (pp. 1–16, all sections, Boxes 1 and 2, Figures
    1–4 captions) and the Authors' Response (pp. 45–51, R1–R7). Also read in full
    four commentaries that touch the reading question: Bates, Sims & Jacobs (e3),
    Dimov (e8), Dingemanse (e9) and Ma & Woodford (e15). The other 21 commentaries
    were not read; the whole PDF was searched by keyword (amortiz, cach, memoiz,
    offload, reus, precomput, prosthes, stale, lookup, extended mind, external memory)
    and every hit was read in context. The cited primary studies (Dasgupta et al.
    2018, Howes et al. 2016, Huys et al. 2015, Keramati et al. 2016, Milli et al.
    2017/2019) were not read; what is said about them here is this article's account.
    Every quotation of the source below was checked against the extracted text by
    script, with whitespace, hyphenation and quote marks normalised; one ("propose
    that people never have to directly solve … defined in Equation 3") is split
    by a column break in the extraction and was checked against the page image of
    p. 5. The phrase "incorrectly reusing an obsolete argument" is quoted from CLAIM-303,
    not from the paper.
date: '2026-10-15'
summary: >-
  Resource rationality defines the right cognitive mechanism as the one, among those
  a brain can execute, that maximizes expected utility of its result minus the expected
  opportunity cost of the time and resources it uses (Eq. 3), averaged over the
  environments consistent with what is known (Eq. 4); resource-rational analysis
  is a five-step iterate-and-refine method for deriving process models from that
  objective. The objective is per episode. It has no separate terms for storing
  a result, retrieving it later, or its going stale: the value of what a computation
  leaves behind is folded into the utility of the episode's result, and the cost
  of finding the heuristic in the first place is assigned to evolution and learning
  and left out. Reuse appears only in the review, qualitatively: habits as reused
  action sequences, Dasgupta et al. 2018's memorized hypotheses, Howes et al. 2016's
  memorize-or-look-up trade, and "cognitive prostheses". The framework is offered
  as a methodological device, not a claim that people are optimal.
---
<!-- inactive-ok-file: CLAIM-303 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# NOTE-873: Lieder & Griffiths — Resource-rational analysis

## Contribution

A synthesis and a method. The authors name "the rational use of limited resources" as the principle common to bounded-rational economics (Simon, Sims's rational inattention, Gabaix's sparse max), efficient neural coding, efficient-communication accounts in linguistics, and recent psychology, and they take Russell and Horvitz's bounded optimality from AI as its formal statement. They then turn Anderson's six-step rational analysis (Box 1) into a five-step resource-rational analysis (Box 2) that derives algorithm-level process models instead of optimal behaviour. Most of the article (sections 4–5) reviews prior work recast in this frame. Section 6 lists the limits. The Response insists the optimality assumption is "a methodological device to efficiently search through the endless space of possible mechanisms", not a substantive claim.

## Key insight

Charge computation to the objective, and optimize the mechanism rather than the behaviour. Classical rational models (Eq. 1) pick the action with the highest expected utility and treat computing it as free. Resource rationality picks the heuristic whose result is worth the most net of the time and resources spent producing it, so the mechanisms it favours are cheap, approximate and biased, and many classic biases fall out as the price of that frugality. The optimization is done "by evolution, cognitive development, and life-long learning", not by the person at decision time.

## Assumptions

- **The formal definitions, as printed.**
  - Eq. 1 (classical): a* = argmax_a ∫ u(o)·p(o|a) do.
  - Eq. 2 (bounded optimality, lifetime): m* = argmax_{m ∈ M_B} E_{P(T, l_T | E, A_t = m(l_t))}[u(l_T)], where M_B is "the set of biologically feasible minds", T the agent's unknown lifetime, l_t = (S_0, …, S_t) its life history, A_t = m(l_t) the action chosen, and u scores whole life histories.
  - Eq. 3 (resource-rational heuristic, known environment): h*(s_0, B, E) = argmax_{h ∈ H_B} E_{P(result | s_0, h, E, B)}[u(result)] − E_{t_h, ρ, λ | h, s_0, B, E}[cost(t_h, ρ, λ)], where H_B is "the set of heuristics that brain B can execute", s_0 = (o, b_0) the observed initial world state and the initial belief state, and cost(t_h, ρ, λ) is a random variable denoting "the total opportunity cost of investing the cognitive resources ρ used or blocked by the heuristic h for the duration t_h of its execution, when the agent's cognitive opportunity cost per quantum of cognitive resources and unit time is λ".
  - Eq. 4 (boundedly resource-rational, limited information i): h*(s_0, B, i) = argmax_{h ∈ H_B} E_{E|i}[ E_{P(result | s_0, h, E, B)}[u(result)] − E_{t_h, ρ, λ | h, s_0, B, E}[cost(t_h, ρ, λ)] ], the same trade averaged over environments consistent with information "obtained about the environment through direct experience, indirect experience, and evolutionary adaptation".
- **Episodes.** Eq. 3 follows from Eq. 2 only "if we assume that life can be partitioned into a sequence of episodes". The cost term is the link between episodes: "the time and cognitive resources expended on any decision or inference (current episode) take away from a person's budget for later ones (future episodes)." In the Response (R3) the authors add that the utility in Eq. 3 scores the resulting belief state too: "the intermediate belief state following a single decision or judgment is valuable because it can inform future decisions", and b should "include all aspects of the agent's internal state that might impact its future decisions."
- **The architecture is fixed and given.** M_B includes "a limited set of elementary operations … limited processing speed … and potentially other constraints, such as limited working memory". The Figure 1 caption: "For the purpose of deriving a resource-rational mechanism these constraints are assumed to be fixed. … Sufficiently large changes may warrant the resource-rational analysis to be redone."
- **The optimization is not done in the head.** The authors "propose that people never have to directly solve the constrained optimization problem defined in Equation 3"; "for most of our decisions the problem of finding a good decision mechanism has already been solved by evolution …, learning, and cognitive development". The cost of that search is not in Eq. 3 or 4. The authors concede that adaptation is itself bounded, so "even a resource-rational mind might have to rely on heuristics for choosing heuristics".
- **Hard constraints are a special case.** Response R3: a model with a fixed budget (their example, utility-weighted sampling with a fixed number of samples) is "just a special case of Equation 3 … where the cost of computation is constant across all heuristics."
- **No commitment on the cost's currency.** Response R4: RRA specifies "the terms of the tradeoff between utility and computational costs but not the kinds of computations or the way that those costs are denominated." Response R3: "there truly are different types of cognitive constraints. For instance, time constraints are conceptually different from limited working memory capacity."
- **Individual agent facing nature.** The Response (R6) accepts that the target article treats single minds and problems "generated by nature", and calls extension to interacting agents and language an open frontier without doing it.

## Key results

- **The five steps (Box 2), verbatim:**
  1. "Start with a computational-level (i.e., functional) description of an aspect of cognition formulated as a problem and its solution."
  2. "Posit which class of algorithms the mind's computational architecture might use to approximately solve this problem, the cost of the computational resources used by these algorithms, and the utility of more accurately approximating the correct solution."
  3. "Find the algorithm in this class that optimally trades off resources and approximation accuracy (Equation 3 or 4)."
  4. "Evaluate the predictions of the resulting rational process model against empirical data."
  5. "Refine the computational-level theory (step 1) or assumed computational architecture and its constraints (step 2) to address significant discrepancies, derive a refined resource-rational model, and then reiterate or stop if the model's assumptions are already sufficiently realistic."
  The box adds that the analysis "may stop in step 5 even when human performance substantially deviates from the resource-rational predictions as long as reasonable attempts have been made to model the constraints accurately". Section 6 calls step 5 "a double-edged sword": constraints postulated carelessly can overfit, so fitted constraints should be judged by out-of-sample prediction and measured independently.
- **The review's numbers are reports of others' work.** People's planning reached "about 86% of the best possible trade-off between decision quality and time cost and agreed with the bounded-optimal strategy about 55% of the time" (Callaway et al. 2018a; Lieder et al. 2017). Vul et al. 2014: deciding on a single sample is bounded-optimal "when it takes at most three times as long to execute the action as to simulate it". Icard & Goodman 2015: "it is often resource-rational to ignore all but the one to three most relevant variables."
- **On reuse of past computation (all qualitative, all citations to other work):**
  - Habits (4.4): "Reusing previously successful action sequences allows people to save substantial amounts of time-consuming and error-prone computation; therefore, the principle of resource rationality in Equation 3 can be applied to determine under which circumstances it is rational to rely on habits." Huys et al. 2015 is described as trading "planning cost savings attained by reusing previous action sequences against the resulting decrease in decision quality"; Keramati et al. 2016 as finding people "adaptively integrate planning and habits according to how much time is available".
  - Amortized inference (5.1.3), one sentence: "once people have generated a hypothesis in this way they memorize it and later retrieve it to more efficiently reason about related questions in the future (Dasgupta et al. 2018)." The cited title in the reference list is "Remembrance of inferences past: Amortization in human hypothesis generation". The word "amortization" appears in the target article only in that reference.
  - Memory (5.1.1): Anderson & Milson 1989 is read as "an optimal memory storage mechanism" that "presorts memories optimally by exploiting how the probability that a previously encountered piece of information will be needed again depends on the frequency, recency, and pattern of its previous occurrences", with "a resource-rational stopping rule that trades off the cost of continued memory search against its expected benefits".
  - Head versus world (5.1.1): "Howes et al. (2016) found that bounded optimality can predict how many items a person chooses to commit to memory from the cost of misremembering, their working memory capacity, and how long it takes to look up forgotten information." This is the only place the target article sets internal storage against retrieval from the environment.
  - A repertoire has a cost: "Being equipped with a different heuristic for each and every situation would be prohibitively expensive (Houston & McNamara 1999) − not least because of the difficulty of selecting between them (Milli et al. 2017; 2019)." This motivates Eq. 4; it is not a term in it.
  - Chunking and hierarchical action representations are named as future applications: chunking "as a bounded-optimal mechanism for representing information in memory to reduce the cost of memory maintenance while increasing recall performance".
- **On offloading to the environment.** The target article mentions it once, as an intervention: resource constraints "could be addressed through cognitive training or cognitive prostheses like navigation systems or decision-support systems". It does not model it. Dingemanse (e9) does: language is "a culturally evolved store of habits – routinely deployable resources – that help outsource computation", and interaction is "an interactively scaffolded form of cognitive offloading (Risko & Gilbert 2016)", citing Hutchins 1995. He says the authors do not discuss "material symbols of metacognition that augment and distribute our cognitive processes". The Response (R6) agrees this is "a particularly rich territory" and does not extend the formalism.
- **On storage as a cost.** Bates, Sims & Jacobs (e3) treat working memory as a channel, "sending a message to his or her future self", and note that a policy stored as "a lookup table specifying the optimal move for every board configuration" exceeds finite capacity, so capacity-limited learners store compressed policies that generalize better. The Response (R3) answers that channel capacity covers representational constraints but "not all constraints are about representation".
- **On timescale and change.** Ma & Woodford (e15): "Resource-rational models are often non-committal about the timescales over which the optimization occurs", and how well-adapted a mechanism can be "is even more important if the statistics of the environment are changing". Nothing in the target or Response addresses a stored result becoming wrong as the world changes.

## Bearing on the record

**[QUESTION-095](../questions.d/QUESTION-095.md).** The paper supplies the general objective the question needs, utility of a result minus the opportunity cost of producing it, and its review groups reuse of past computation (habits, memorized inferences, Anderson's need-probability memory, memorize-or-look-up) under that one objective. So it supports the question's premise that precomputation, memory and retrieval are all cost-benefit trades over the same currency, opportunity cost of time and resources. It does not give the cost model the question asks for. Eq. 3 is per episode. Precompute cost for a later episode, storage and upkeep, retrieval cost and staleness are not separate terms. The value of a kept result enters only through u(result), which by the Response values the belief state for future decisions. Retrieval is just another heuristic in H_B with its own t_h. Storage could be read as resources ρ "blocked" over time, but ρ is charged only for the heuristic's duration t_h; that reading is mine, not the paper's. The search for h* itself, the best case of amortization (paid once, by evolution and learning, reused every episode), is left out of the objective on purpose. Staleness has no term. The nearest things are Eq. 4's averaging over possible environments, which is robustness to not knowing the environment, not decay over time, and the remark that the analysis may need "to be redone" if constraints change. On whether anyone has joined distributed cognition and resource rationality: the target article has not. Dingemanse's commentary names the join (Hutchins 1995, Risko & Gilbert 2016, offloading) as an open frontier, and the authors accept it without doing it. The paper is a frame to hang an answer on, not the answer. The formal amortization is in Dasgupta et al. 2018 ([LIT-1074](../literature.d/LIT-1074.md)) and Gershman & Goodman 2014. The head-versus-world trade is in Howes et al. 2016, which is not registered and should be if the question is pursued.

**[CLAIM-303](../claims.d/CLAIM-303.md).** The claim's break-even F + n(c_a + u) < n·c_r is an instance of the form Eq. 3 licenses, a net of benefit and cost, but summed over n uses rather than taken per episode. The paper neither supports nor tests the claim's application to a record. Two points narrow it. First, the paper's position that the expensive search for a mechanism is done once, offline, and its cost left out of the per-use objective is the same move as treating F as sunk; the claim keeps F and so is more complete on that point. Second, the claim's staleness term (the cost of "incorrectly reusing an obsolete argument") has no counterpart in Eqs. 2–4, so the paper gives no support to that part. Its stance on habits (reuse saves computation at "the resulting decrease in decision quality") is the closest it comes, and it is qualitative and from Huys et al. Nothing here bears on the claim's second-occurrence point, that recurrence is evidence of reuse; Anderson & Milson's need probability from "frequency, recency, and pattern of … previous occurrences" is a cited example of exactly that inference, and could be read for it.

## Note of 2026-10-15: Howes et al. 2016, read

This reading called Howes et al. 2016 ([LIT-1062](../literature.d/LIT-1062.md)) "the head-versus-world trade", following the source's description. The task has no look-up: names are seen once and cannot be revisited, and the choice is how long a list to take per trial. There is no parametric model; the prediction for each person is the list length with the best reward rate in their own measured data. Capacity and look-up time are not parameters, and raising the cost of misremembering did not change choices. It is a trade of memory load against reward rate, not of memory against the world.
