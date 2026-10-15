---
number: 886
status: Read
formerly:
- NOTE-tmpw9lhz
paper: LIT-1056
title: Gershman & Goodman — Amortized inference in probabilistic reasoning
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full from the authors' copy on the Gershman lab's publications page
    (https://gershmanlab.com/pubs/GershmanGoodman14.pdf, fetched 2026-10-15). It
    is 6 pages, with the running header "Proceedings of the 36th Annual Conference
    of the Cognitive Science Society. (2014)", and the PDF was regenerated 2018-08-27.
    The version of record is eScholarship ark:/13030/qt34j1h7k5 (escholarship.org/uc/item/34j1h7k5).
    Its PDF refused direct requests from this environment, so this copy was not
    compared with it. The page range 517–522 does not appear on the copy. It comes
    from the authors' own later citation (Dasgupta, Schulz, Goodman & Gershman 2017).
    The text was extracted with pdftotext. Extraction drops minus signs and the
    content of Figure 2's equations, so pages 2–5 were checked against page images.
    Two values depend on that check: the S2 correlation for Query E is r = −0.11,
    not 0.11, and the facilitation effect is log RT_D − log RT_E. Read: abstract,
    introduction, the formal section, both experiments with every figure, discussion,
    and the reference list. Nothing was skipped. Stuhlmüller et al. (2013), the
    machine-learning scheme this paper's reuse is modelled on, was not read, so
    what is said of it here is this paper's account. Every quotation of the paper
    below was checked against the extracted text by script, with whitespace normalised.
    One quotation runs across a figure in the extraction ("identical to the procedure
    used in Experiment 2") and was checked against the page image. Quotations of
    the record's own entries are marked as such.
date: '2026-10-15'
summary: >-
  Gershman and Goodman define amortized inference as the reuse of past inferences,
  cached as sub-computations, to answer related later queries. They report two small
  online experiments in which order alone made reuse available. When a sub-query
  came before a complex query on a five-node Bayesian network, a person's answer
  to the complex query could be predicted from their own answer to the sub-query
  (r = 0.28; r = −0.11 when the order was reversed). Answers to the complex query
  were also faster relative to a structurally matched baseline. Reuse in this paper
  is internal memory, and it is shown only through correlation and speed, within
  one task, with small effects. The paper does not measure costs. Storage cost and
  the choice of what to store are listed as open trade-offs. Bias, staleness and
  interference are not studied: reuse that may be "inaccurate" without modification,
  and interference and forgetting of stored inferences, appear only as questions.
---
<!-- inactive-ok-file: CLAIM-295 CLAIM-303 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# NOTE-886: Gershman & Goodman — Amortized inference in probabilistic reasoning

## Contribution

The paper names the problem and gives the first behavioural evidence for it. The problem is "how to flexibly reuse inferences so as to answer a variety of related queries". General-purpose inference algorithms such as belief propagation, MCMC and importance sampling are "memoryless: each query is (at least in principle) processed independently of others". So "answering the same query twice requires the same amount of computation as answer two unique queries". The authors argue that the brain faces "numerous related queries" and so should not be memoryless. They test the simplest form of reuse, which is caching a sub-inference and plugging it into a larger one.

## Key insight

Reuse leaves fingerprints that order manipulations can expose. If a stored sub-inference is plugged into a later, larger inference, two things follow. The larger answer is faster, "since retrieval of an inference is presumably faster than computing the inference from scratch". It also inherits the individual's idiosyncrasies in the sub-answer: "individual differences in the answer to a simple query should propagate to more complex queries". The two experiments test these two predictions.

## Assumptions

- **Formal setting.** A Bayesian network over x = {x_1,…,x_M}. A query is a tuple {Q, E, y}: latent variables Q, observed variables E with values y. An inference algorithm is "any function that takes as input q and returns the conditional distribution" p(x_Q | x_E = y). The amortized form considered is "caching" of "sub-computations that are invoked by multiple queries", which the paper glosses as "memoizing" (Michie, 1968). In Figure 2's example, Query 1, P(B|C), is a sub-query of Query 2, P(A|C) = Σ_B P(A|B)P(B|C).
- **The reasoner reuses only what was presented earlier.** The authors admit reuse could in principle run in the other order: "reuse could still occur if the complex query precedes the sub-query". Their test rests on a conjecture that "query order biases the complex query to be answered in different ways based on what sub-computations are available for reuse".
- **Confidence as probability.** In Experiment 1, a binary choice plus a slider were linearly rescaled to a probability, with minimum confidence mapped to 0.5. Calibration against the true posteriors (r = 0.92) was taken to justify using these as "proxies for subjects' inferences".
- **Stochastic inference.** The correlation signature requires that individual answers vary: "an element of stochasticity or individual variation (a necessity for inducing the reported correlation)". The data "do not constrain hypotheses about particular inference algorithms" beyond this and decomposability.

## Key results

- **Task.** The network is a chain of military officers: a general (root L), two captains (M, Z) and two sergeants under one captain (leaves X, Y). P(defect | superior defects) = 0.7, P(defect | superior loyal) = 0.3, P(general defects) = 0.5. There are six queries, A–F (Figure 4). Query C is P(M | X, Y). The target, Query E, is P(L | X, Y, Z). The control, Query D, has E's structure but no sub-query among the trials. In order S1 (A, B, C, D, E, F) the sub-query C comes third, before E. In order S2 (A, B, F, D, E, C) it comes sixth, after E. Only the positions of C and F differ.
- **Experiment 1 (n = 146, 73 per order, Mechanical Turk, $0.50).** Each subject's answer to C was plugged into Bayes' rule (eq. 3) to predict their answer to E. Predicted and reported E were correlated in S1 (r = 0.28, p < 0.05) but not in S2 (r = −0.11, p = 0.36). The absolute prediction error was higher in S2 than in S1, t(144) = 2.06, p < 0.05 (Figure 6B, about 0.33 against 0.41 read from the plot). In the control, C's answer plugged into D's computation gave no correlation in either order (both p > 0.05), and the prediction errors did not differ (p = 0.6). The difference between the two correlations was not itself tested.
- **Simulation (Figure 7).** A sampler that caches noisy Monte Carlo estimates reproduces the pattern: a correlation for E and about 0 for D. The E correlation falls as the number of samples rises, from about 0.85 at one sample to about 0.2 at 40. In the authors' words, "even the very small fluctuations in Monte Carlo estimates based on dozens of samples are enough to induce a strong correlation (though these small fluctuations could be quickly swamped by independent sources of response noise)".
- **Experiment 2 (134 recruited; 50 in S1 and 53 in S2 analysed).** The orders were the same and responses were speeded binary choices. Only subjects who chose "defect", the more likely answer, for Query E were analysed. The facilitation effect is log RT_D − log RT_E, with D as the structural baseline. The median facilitation was larger in S1 than in S2 (z = 2.09, p < 0.05, rank-sum test). It was greater than zero in S1 (z = 3.68, p < 0.005) but not in S2 (p = 0.16). Read from Figure 8, the medians are about 0.47 in S1 and 0.23 in S2. "We conclude that the availability of reuse facilitates the speed of inference."
- **Conclusion as stated.** "Multiple related queries are not processed independently. Specifically, queries influence each other when the answer to one query supplies a memoizable sub-computation for another query." Rational process models "need to be augmented with storage and retrieval mechanisms for reusing inferences".
- **Costs and trade-offs (Discussion, not tested).** "the memory cost of storing all inferences may be prohibitive". The trade-offs listed are: "storing more complex inferences provides greater savings in computation time, but incurs a larger memory cost; complex inferences should not be stored if they can be decomposed into simpler inferences that are already stored, and conversely simple inferences should be stored if they can be composed into larger inferences; storage of frequent inferences should be preferred to storage of rare inferences." Balancing them "may addressable via resource-rational analysis". It is not done here.
- **Staleness and interference, as questions only.** For related but non-identical queries, "it may be inaccurate to reuse a stored inference without modification". Memorylessness "guarantees that inferences will not interfere with one another", which implies reuse gives up that guarantee. The open questions are: "do stored inferences interfere with each other proactively and retroactively? Is there a temporal gradient—analogous to a forgetting function—such that older inferences are less likely to be reused?"
- **Against exemplar models.** Here the things stored are inferences, "rather than stimulus exemplars or samples from the prior", and they can be composed with freshly computed ones.

## Limitations and slips

- The samples are small, the tasks run online with one network, and the effects are modest. The order effect on correlation rests on one significant correlation and one non-significant one.
- Experiment 2 analyses only subjects who gave the more likely answer to E, which is selection on the outcome query.
- The text mislabels queries. Equation 3 and the Experiment 2 results call the target "Query F" and "RT_F", but Figure 4, the Experiment 1 analysis and the definition of RT_F as "the response time (in milliseconds) for Query E" show that the target is E. Experiment 2's procedure is said to be "identical to the procedure used in Experiment 2", which presumably means Experiment 1. None of these slips changes the design.
- No bias in the sense of a shift toward earlier answers is measured. What is shown is dependence: errors in a person's sub-answer carry into their complex answer.

## Bearing on the record

**On [QUESTION-095](../questions.d/QUESTION-095.md): the paper frames amortization as memoization, retrieval in place of recomputation. That supports the question's candidate unification for internal memory only. It supplies a partial cost list and no staleness term.**

- The paper defines amortized inference as caching ("memoizing", after Michie 1968) of "sub-computations that are invoked by multiple queries" and explains the speed gain as "retrieval of an inference is presumably faster than computing the inference from scratch". For the question's first half, this is the authors' own position: amortizing inference is keeping a computed result where reading it back is cheaper than redoing it. The paper does not separate "retrieval" from "computation" as two kinds of thing. It treats retrieval as a cheap computation that replaces an expensive one, which is the "computational" part the question attributes to [CLAIM-295](../claims.d/CLAIM-295.md).
- It does not cover the cockpit or the filed argument. Storage here is in the reasoner's memory, and nothing is said about external storage, perception or offloading. It does not join the distributed-cognition literature, and it cites none of Kirsh, Hutchins, Ballard or Gray. Joining the speed bugs to amortized inference is still the record's move.
- Its cost model is partial. It names compute saved, memory cost, decomposability and frequency of the query, in prose. It has no retrieval-cost term beyond "presumably faster" and no upkeep term. Staleness appears only as the possibility that reuse for a non-identical query "may be inaccurate", plus questions about interference and forgetting. So the paper does not supply the staleness risk that the question's unification needs. The record should look for it in Dasgupta et al. 2018 ([LIT-1074](../literature.d/LIT-1074.md)), and should not credit it to this paper.
- The question's summary says reasoners reuse past inferences "faster and biased toward earlier answers". This paper shows the first part (Experiment 2) and shows dependence on earlier answers (Experiment 1). It does not show a directional bias, and it does not use the word "bias" for the effect. The "bias" framing should be attributed to the later work.

**On [CLAIM-303](../claims.d/CLAIM-303.md): consistent with its trade, and one point bears on its rider about recurrence.**

- The paper's trade-offs have the same structure as the claim's: pay storage now against recomputation later, and store what will be reused. It states them as intuitions, with no break-even arithmetic and no estimate of reuse. It neither tests nor supports the claim's inequality.
- The claim holds that recurrence is evidence of reuse, not the criterion. The paper lists frequency as one consideration among several ("storage of frequent inferences should be preferred to storage of rare inferences"), alongside the size of the saving and whether the result composes into larger answers. That is consistent with the claim's rider: frequency is not the whole rule. But the paper gives no argument that a rare, expensive inference should be stored, which is the claim's illustration.
- The claim's distinctive term, the cost of reusing an obsolete result ("persistence can preserve errors as efficiently as valid discoveries"), has an empirical counterpart in Experiment 1. A person's error in the sub-answer propagates into the larger answer. That is error preservation through reuse, but the error is present from the start. A result that was right and later went stale is not studied.
- The evidence is about a single reasoner over minutes. It says nothing about a record's filed arguments, verification or dependency tracking.
