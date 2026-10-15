---
status: Read
paper: LIT-tmpyg066
title: Dasgupta & Gershman — Memory as a computational resource
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the publisher's typeset PDF of the version of
    record (Trends in Cognitive Sciences 25(3), March 2021, pp. 240–251; Elsevier-generated,
    12 pages, with the DOI and "© 2020 Elsevier Ltd." on the first page), posted
    by the second author on his lab's publication page: gershmanlab.com/pubs/DasguptaGershman21.pdf,
    linked from gershmanlab.com/pubs.html. Unpaywall lists the work as bronze, with
    one location, the publisher (doi.org/10.1016/j.tics.2020.12.008, "acceptedVersion",
    no PDF URL); the lab copy was used instead. Text extracted with pdftotext, raw
    and layout modes; page 249 (Outstanding Questions box and Concluding Remarks)
    was also checked against a page image, because the first Outstanding Question
    ends without a question mark in the extraction, and it does so in print too.
    Read: abstract, highlights, glossary, the introduction, "Approaches to Computational
    Reuse", Box 1 (cognitive models of reuse), the four case studies (arithmetic,
    imagery, probabilistic inference with Box 2, planning), Concluding Remarks,
    Outstanding Questions, figure captions and the reference list. Figures were
    read from their captions and the text that reports them; plotted values were
    not read off. None of the cited works was read for this note except Gershman
    and Goodman 2014 and Dasgupta et al. 2018, which have their own readings; what
    this note says of the others is what this review says. Every quotation below
    was checked against the extracted text by script, with whitespace normalised
    and typographic ligatures expanded; one, which runs across the page footer of
    p. 246, was checked in its two parts. Quotations of the record's own entries
    were checked against those files.
date: '2026-10-15'
summary: >-
  A short review arguing that memory is used to avoid redundant computation: results
  are stored and reused (memoization), either whole ("top-down") or as solutions
  to subproblems ("bottom-up"), and amortized inference and deep Q-networks are
  "distributed" memo-tables that generalize to new inputs. It illustrates this in
  mental arithmetic, mental imagery, probabilistic inference and planning, mostly
  with response times that flatten with practice and with biases that a cache explains
  (reuse of earlier inferences, choices based on stale cached values, reuse of policy
  fragments). It has equations for its examples but no cost model: the space–time
  trade-off is named, and when caching pays is listed as an outstanding question.
  Memory is internal throughout; retrieval cost is mentioned once, and offloading
  or external stores not at all.
---
<!-- inactive-ok-file: CLAIM-tmpygqjz — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# NOTE-tmp4doe6: Dasgupta & Gershman — Memory as a computational resource

## Contribution

A review that reads several literatures in cognitive science as cases of one computer-science idea: "redundant computation (which costs time) can be avoided by storing partial solutions in memory (which costs space)". It organizes reuse by Michie's memoization, adds three design issues from computer science (generalization, persistence, decomposition), and sorts cognitive models by decomposition: Logan's instance theory as "top-down" reuse of whole outputs, ACT-R and SOAR production compilation as "bottom-up" reuse of intermediate computations. Its newer claim is that neural networks extend memoization: "Recent developments in neural networks expand the scope of computational reuse with a distributed form of memoization called amortization." No new data or model; the evidence is the authors' and others' earlier studies.

## Key insight

Many cognitive skills that look like faster computation after practice are better described as computation replaced by look-up, and a learned function approximator is a look-up table that interpolates. So one frame covers arithmetic facts, practised rotations, chess positions, cached values in reinforcement learning, and recognition networks for inference; and the biases these show (reuse of a near-miss inference, choices driven by a cached value the world has since devalued) are signatures of the cache, not of the computation.

## Assumptions

- **Memory is internal.** Every store is in the head (long-term declarative memory, episodic memory, synaptic weights of a recognition or Q-network). The environment appears only as the source of queries and of samples in reinforcement learning.
- **Reuse is cheaper than recomputation.** Assumed throughout; not stated as a condition, not measured, and retrieval is not given a cost except once (Box 1, below).
- **Computer-science memoization is the reference model** (Michie 1968; Bentley 1982 for the space–time trade-off; tabulation, selective memoization and function caching for the design issues). Amortized analysis in the algorithms sense (averaging cost over a sequence of operations) is not used or cited; "amortization" here means amortized inference.
- **Response-time flattening with practice is evidence of a shift from algorithm to memory** (arithmetic, alphabet arithmetic, mental rotation), following Logan.

## Key results

The paper reports no new results. What it defines and claims:

- **Memoization.** Glossary: "storing the results of expensive function calls and returning the cached result when the same inputs occur again, in order to speed up algorithms or programs." In the text, after Michie: "Function calls are intercepted by a ‘memoizer’ that inspects a cache (the memo-table) of past function calls and their outputs. If a function has previously been called with the same inputs, then the previously computed result is reused." If the target function has not been memoized, memoized subfunctions can be intercepted as it runs.
- **Amortization.** Defined only as amortized inference. Glossary: "memoizing the process of inference, by learning a mapping from data to the parameters of the posterior distribution." Highlights: "a distributed form of memoization called amortization". Amortized inference algorithms "replace iterative computation with a fast parametrized ‘recognition model’", and "the neural network functions as a distributed memo-table, obviating the need for bottom-up iterative computation." A recognition network is "a sophisticated version of Michie’s interpolation approach to memoization, able to operate on inputs it has never seen before by generalizing from past inputs." A deep Q-network is likewise "a distributed memo-table". So amortization is memoization whose table is a learned function, which generalizes to unseen inputs; it is not defined as spreading a one-off cost over later uses.
- **Space–time trade-off.** Glossary: "where an algorithm trades increased time usage with decreased space usage and vice versa." This is the only trade the paper names.
- **Equations.** Six, all illustrative: the Fibonacci recursion [1]; Kepler's geometric interpolation f(n) ≈ √(f(n+1)f(n−1)) as an example of generalizing from a memo-table [2]; Bayes' rule [3]; the Bellman equation [4]; and in Box 2 the posterior over a state sequence [I] and its hidden-Markov recursion [II], which shows that only "the sufficient statistics of the posterior need to be stored". None of them prices storage, retrieval or reuse.
- **No cost model.** There is no expression for when reuse pays, no break-even condition, no expected-reuse or need-probability term. The question is posed as open. Outstanding Questions: "What are the costs of computations, both the time required to perform new computations, as well as the space required to cache" (printed without a question mark), "How does the brain negotiate this space–time trade-off in choosing when to cache computations?", and "What is the role of memory as a computational resource in this trade-off?", the trade-off being resource rationality's "between accuracy and computational cost".
- **Query predictability, qualitatively.** Two places. Michie saw "that a memo-table might be too rigid for some problems, particularly when the input space is vast and the probability of a repeated function call is low", and proposed interpolation. And a capacity-limited recognition network "preferentially allocates its limited capacity to answering high probability queries", which is "an automatic consequence of training the recognition network on queries drawn from the environment"; manipulating the historical query distribution shifts the bias (from Dasgupta et al. 2020, ref. 51).
- **Persistence and storage limits.** "Because there are inevitably space constraints, memoization must be selective about what it stores and when it discards information". The two extremes are a memo-table "erased after each function call" and one that "persists indefinitely". How long cached computations persist in human memory, "and in what form", is "an open question".
- **Retrieval cost.** Mentioned once, for production systems: storing intermediate computations "means that there is a very large database, placing onerous demands on storage and retrieval" (citing Tambe et al. 1990 on expensive chunks). Logan's theory is described as a race between algorithm and memory, "whereby behavioral outputs were based on the first process to complete", so retrieval has a time, but the review gives it no cost term. Search is not discussed.
- **Staleness.** Stated for planning, as an out-of-date cache: "Caching can explain why humans and other animals sometimes make decisions based on ‘stale’ information, choosing actions that bring them to previously high-value states that have been devalued". "This pattern of behavior arises if some parts of the cache have not yet been updated after other parts have been updated (inducing inconsistencies between the cached values)." "Partial cache updating is an inevitable consequence of a resource-constrained planning system that must prioritize some updates over others"; with more resources, time or incentives people update more, and offline simulation at rest supports "offline cache updating".
- **Bias and interference among reused results.** For amortized inference: "inferences are biased by recent inferences computed for other queries and that this bias depends on the overlap between the queries", explained by structure shared across posteriors in a capacity-limited network. The word "interference" is not used. For production systems, ACT-R's strengthening assumes a factorized posterior, "the cost is that such an approximation can be highly inaccurate."
- **Partial reuse.** In planning, reuse of policy fragments (Huys et al. 2015) gives "a good (albeit suboptimal) solution", and fragment reuse rises across trials, "ostensibly due to filling of the memo-table". Episodic control (Lengyel and Dayan 2007) is argued to be most valuable when experience is scarce.
- **Slip.** The planning text cites "Figure 3B" for the four-step path example; the panel is Figure 4B.

## Bearing on the record

**On [QUESTION-tmp1mkzc](../questions.d/QUESTION-tmp1mkzc.md): a vocabulary for the first strategy with the store in the head, no cost model, and nothing on the environment.**

- **Memoization and amortization.** The paper's definitions fit the question's first strategy, "precompute and leave a result", with one difference: memoization here is lazy, caching a result when it is first computed for a request, not ahead of a predicted one. The cockpit's speed bugs are computed before the request because the query is known; nothing in this paper is computed in advance for a predicted query, except perhaps offline simulation to update a cache. "Amortization" means a learned, generalizing memo-table. It does not mean amortized analysis, and the paper does not use the word in Kirsh's (Tarjan's) sense. So it does not settle whether the owner's "amortized retrieval" and "amortized computation" are one trade; it supplies the computer-science reference (Michie, memo-tables, tabulation) that a statement of the trade would cite.
- **Cost model.** None. The space–time trade-off is named, and when to cache is listed as open. For the question's terms: query predictability appears qualitatively (Michie's low probability of a repeated call; a capacity-limited network spending capacity on frequent queries); retrieval cost appears once, as "onerous demands on storage and retrieval" in production systems, and search not at all; staleness and bias both appear (next point); erosion of an internal route does not appear. The paper's own open question, how the brain negotiates the trade-off "in choosing when to cache computations", is the question's, restricted to the head.
- **Staleness and bias are both here, and they are different.** The planning section gives the question's staleness in its strict sense: a cached value that was right and that the world has since devalued, kept because updating is partial and resource-limited. The inference section gives the other failure, a reused result biased by overlap with a different query. The earlier reading of Dasgupta et al. 2018 ([LIT-tmpt2ql7](../literature.d/LIT-tmpt2ql7.md)) found only the second; this review adds the first, from the habit and devaluation literature (Daw et al. 2005, 2011; Gershman et al. 2014 on offline revaluation). So a cost model would need both terms, and this paper is a source for both, qualitatively. It also adds a remedy term the question does not list: offline cache updating, done when resources allow.
- **External memory, offloading, the environment.** Not mentioned. No reference is to offloading, distributed cognition, external representations or tools. "Environment" appears only as the world that generates queries and rewards (MDPs, temporal-difference learning, queries "drawn from the environment"), and "external world" once, in a parenthesis about hypotheses. This confirms the citation search's note in [QUESTION-tmp1mkzc](../questions.d/QUESTION-tmp1mkzc.md) ("internal memory only, and none of its references is an offloading source"). The paper does not join the two literatures.
- **What it does add for the four strategies.** Its top-down/bottom-up split (store final outputs versus store subproblem solutions) cuts across the question's table. Speed bugs are top-down (a final result); Kirsh's structured workspace is closer to bottom-up (an arrangement that makes later steps cheap), and Box 2's sufficient statistic, a running summary kept so that past data need not be retrieved, is a third pattern: keep a compressed state, not results. Ballard's defer-and-re-read is the opposite of Box 2's: it keeps no summary and re-reads the raw input. The paper does not make these comparisons.

**On [LIT-tmpyg066](../literature.d/LIT-tmpyg066.md) as filed.** The filed summary is accurate. The "Why this is here" line says the paper "states that retrieval is computation, for internal memory". It does not: it says memory replaces computation, and treats retrieval as nearly free (one mention of retrieval demands, in Box 1). The owner's conjecture that retrieval is itself computation is not in the paper. The keyword "computational resource" is the title's. The citation search's description, "memoization and amortization across domains, internal memory only", is correct.

**On [CLAIM-tmpygqjz](../claims.d/CLAIM-tmpygqjz.md).** Consistent and not a test. The paper's reuse is the claim's trade at the scale of one mind, and its stale-cache cases support the claim's warning that a kept result can cost more than recomputing; it gives no condition on expected reuse and no measure of the cost of filing or finding.
