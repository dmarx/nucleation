---
number: 875
status: Read
formerly:
- NOTE-tmpoczb2
paper: LIT-1074
title: Dasgupta, Schulz, Goodman & Gershman — Remembrance of inferences past
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the publisher's typeset PDF of the version of
    record (Cognition 178 (2018) 67–81, 15 pp., Elsevier-generated PDF with the
    DOI, received/accepted dates and page furniture), posted by the last author
    on his lab's publication page: gershmanlab.com/pubs/Dasgupta18_remembrance.pdf,
    linked from gershmanlab.com/pubs.html. Unpaywall and OpenAlex list the work
    as bronze open access at the publisher (doi.org/10.1016/j.cognition.2018.04.017)
    with no repository PDF; ScienceDirect refused direct requests from this environment
    (HTTP 403). The bioRxiv preprint (10.1101/137190) and the CogSci 2017 paper
    "Amortized hypothesis generation", which the article names as its preliminary
    version, were not used. Text extracted with pdftotext, raw and layout modes.
    Read: abstract, introduction, Section 2 (Monte Carlo sampling, amortized inference,
    the two strategies, adaptive amortization), Experiments 1–3 with all reported
    statistics, the general discussion and related work, future directions, Appendix
    A (the two reuse schemes as equations) and the reference list. Figures were
    read from their captions and the text that reports them; the plotted values
    were not read off the figures. The online supplementary material and data were
    not consulted. Gershman and Goodman (2014) was not read, so what this note says
    of it is what this paper says. Every quotation below was checked against the
    extracted text by script, with whitespace normalised and typographic ligatures
    expanded; three that run across a column break, a figure or a page footer were
    checked in their parts. Quotations of the record's own entries were checked
    against those files.
date: '2026-10-15'
summary: >-
  In three online experiments (N = 84, 80 and 100, before exclusions), a sub- or
  superadditivity bias induced in a first probability judgment carried over into
  a second, always-packed judgment about the same scene distribution, and errors
  on the two queries were correlated trial by trial (r ≈ 0.34–0.67). The carry-over
  appeared only when the second query shared part of its hypothesis space with the
  first, which rules out simple numerical anchoring; it was larger when cognitive
  load fell on the first query, which the authors' simulations read as reuse of
  a summary statistic rather than of the stored samples; and with a new cue it appeared
  (for subadditivity only, and weakly) when the cue's posterior was similar to the
  first. The paper defines amortization as reuse of past computation bought at a
  cost in bias, and itself places it in the time-for-space trade. It measures no
  response times, so the speed benefit is assumed, not shown; efficiency is shown
  only by better secondary-task accuracy on reusable trials; and it gives no account
  of when reuse pays.
---
<!-- inactive-ok-file: CLAIM-295 CLAIM-303 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# NOTE-875: Dasgupta, Schulz, Goodman & Gershman — Remembrance of inferences past

## Contribution

The paper takes the sampling account of human probability judgment from Dasgupta, Schulz and Gershman (2017), in which people approximate a posterior with a small number of MCMC samples whose starting points bias the answer, and asks whether the sampler is memoryless. Its answer is that it is not: computation done for one query is reused for the next, and the bias of the first answer is reused with it. It offers two concrete reuse schemes, sample reuse and summary reuse, and uses cognitive load and query overlap to discriminate them. The experimental tool is the unpacking effect: listing typical exemplars ("a chair, a computer, or any other object beginning with C") raises the judged probability (subadditivity), listing atypical ones lowers it (superadditivity), and the authors look for these effects in a second query that is always asked in packed form.

## Key insight

If an inference engine keeps something from answering one query and uses it on the next, then whatever was wrong with the first answer travels too, so reuse can be detected by its errors. The paper puts the trade in its own words: "An inference engine may gain efficiency by incurring some amount of bias due to reuse of past computations—a strategy we will refer to as amortized inference (Gershman & Goodman, 2014; Stuhlmüller, Taylor, & Goodman, 2013)." What is kept is a choice along a memory–flexibility line: keeping every sample lets any later query on the same distribution use them, at a high memory cost; keeping only a summary number is cheap to store but usable only when the later query can be built from it.

## Assumptions

- **Definition of amortized inference.** Two levels. The working definition is the sentence above: reuse of past computation that gains efficiency at a cost in bias. The general framework (Section 2.2, Fig. 2) is parameter sharing: "In the standard, memoryless framework, an inference engine inverts a generative model P(d,h) over hypothesis h and data d to compute a recognition model Qθ(h|d) parametrized by θ." Memoryless inference uses separate parameters for each query; "In the amortized framework, parameters are shared across queries. The parameters are selected to accurately approximate not just a single query, but a distribution of queries." With unbounded resources each query gets its own parameters and the framework reduces to the memoryless one; "Under bounded resources, a finite number of parameters must be shared between multiple queries, leading to memory effects: the answer to one query affects the answer to other, similar queries." The learned recognition model (Helmholtz machine, variational inference, footnote 1) is cited as the machine-learning lineage and general form; it is not what the experiments test.
- **The two tested strategies are both forms of storing results, not of learning an inference mapping.** Sample-based amortization pools the N1 samples from Q1 with the N2 new samples for Q2 (Appendix A: the Q2 estimate is computed "over all N1 + N2 equally weighted samples"). Summary-based amortization keeps one number from Q1 and composes it with a fresh estimate of the remainder: for Q1 "C" and Q2 "C or R", P(C or R) ≈ P̂(C from Q1's samples) + P̂(R from N2 new samples). "Under this scheme, only the final product of the computation carried out for Q1 is reused in the calculations for Q2." Summary reuse "is only applicable to problems where the answer to Q2 can be expressed as the composition of the answer to Q1 and another (putatively simpler) computation." The authors do not claim either is what the brain does: "We do not claim that either extreme is plausible", they are endpoints chosen because they make different predictions.
- **The sampler.** MCMC over an LDA model fitted to hand-labelled object co-occurrences in natural scenes (Greene, 2013); unpacked exemplars initialise the chain; about 230 samples per query, an estimate taken from Dasgupta et al. (2017). Cognitive load is assumed to reduce the number of samples. The "true" probabilities against which errors are scored are the MCMC model run to convergence.
- **Memory and reuse decisions are not modelled.** Storage and retrieval are free in the simulations. KL divergence is used only to choose similar and dissimilar cues for Experiment 3; the authors say it "cannot be part of the algorithmic machinery used by humans to assess similarity", and how people decide to reuse is left "to future research".
- **Participants and task.** Amazon Mechanical Turk, $0.50 plus $0.10 per on-time response, 20 s per query, slider from 0 to 100, cue object named, query about objects starting with a letter. Participants were not told that consecutive queries were related. One-sided tests for sub- and superadditivity. Sample sizes fixed before data collection.

## Key results

**Experiment 1** (N = 84, 6 excluded, 78 analysed; 6 query pairs each). Q1 framed packed, typical-unpacked or atypical-unpacked at random; Q2 always packed, same cue, a disjunction of Q1's letter and another ("W or F").

- Q1 replicated both effects: typical-unpacked 59.35 vs packed 49.67, t(77) = 4.03, p < 0.001; atypical-unpacked 31.42 vs 49.67, t(77) = −6.44, p < 0.001.
- Carry-over to Q2: after atypical unpacking, Q2 estimates were lower (46.38 vs 56.83; t(77) = 5.08, p < 0.001). The simple comparison for subadditivity was not significant (58.47 vs 56.83; t(77) = 0.72, p = 0.4); the mixed-effects regression found both (subadditivity 4.39 ± 1.14, t(606.40) = 3.83, p < 0.001; superadditivity −7.86 ± 1.21, t(610.41) = −6.50, p < 0.0001). Per-participant effect sizes: superadditivity > 0 (t(77) = 5.07, p < 0.001), subadditivity not (t(77) = −0.42, p > 0.6).
- Errors (response minus model truth) on Q1 and Q2 correlated: r = 0.67 aggregated, r = 0.55 averaged within participants; individual Q1 effect size correlated with Q2 for atypical (r = 0.35) and typical (r = 0.21) unpacking.

**Experiment 2** (N = 80, no exclusions reported). Adds two manipulations. Overlap: half the Q2 queries shared Q1's letter ("C or R"), half did not ("T or R"), so that a carry-over in the no-overlap case would indicate numerical anchoring rather than reuse. Cognitive load: three digits shown before the query on half the trials at Q1, half at Q2, with a same/different probe afterwards.

- Partial-overlap Q1 and Q2 both showed sub- and superadditivity (Q2: t(79) = 2.44, p < 0.01 and t(79) = −1.93, p < 0.05; regression 5.37 ± 1.34 and −4.92 ± 1.34).
- No overlap: no condition differed from zero under either load placement.
- Partial overlap, load at Q2: only subadditivity was significant (t(38) = 2.14, p < 0.05). Partial overlap, load at Q1: both (subadditive t(38) = 4.18; superadditive t(46) = −1.89; both p < 0.05). Average amortization effect size d = 0.8 for partial overlap with load at Q1, 0.56 for partial overlap with load at Q2, 0.42 for no overlap with load at Q1, none for no overlap with load at Q2. (The text reports d = 0.42 for the no-overlap, load-at-Q1 cell while also reporting no condition there different from zero.)
- Regression interaction: with load at Q2, subadditivity 5.25 ± 2.12 (p < 0.05), superadditivity −3.19 ± 2.17 (p = 0.17); with load at Q1, 5.83 ± 2.25 (p < 0.05) and −6.86 ± 2.21 (p < 0.01). By the simulations of Fig. 3, a larger carry-over under load at Q1 is the summary-based signature (fewer Q1 samples make a more biased summary), whereas sample-based reuse predicts a larger carry-over under load at Q2 (fewer fresh samples to dilute the stored biased ones).
- Secondary task: with load at Q2, probe accuracy was higher on partial-overlap than no-overlap trials (t(36) = 3.16, p < 0.05), read as resources freed by reuse. The authors add that this "cannot be explained by simply initializing the chain for Q2 where the chain for Q1 ended". This is the paper's only evidence of an efficiency gain.
- Partial-overlap Q2 errors correlated with Q1 errors more strongly than no-overlap (0.41 vs 0.15, t(79) = −2.1, p < 0.05). Overall error correlation r = 0.41.

**Experiment 3** (N = 100, 7 excluded, 93 analysed; 3 query pairs). Q2 uses a new cue and the same single letter as Q1 (full overlap), always packed. The new cue was similar (KL < 0.1 from Q1's posterior, e.g. Rug → Curtain 0.080) or dissimilar (KL > 8.5, e.g. Rug → Car 8.658).

- Q2 showed subadditivity carry-over (regression 5.21 ± 1.90, p < 0.05) but not superadditivity (−2.49 ± 1.91, p = 0.19).
- Similar cues: subadditivity t(47) = 3.30, p < 0.01; superadditivity t(48) = 0.54, p = 0.59. Dissimilar cues: neither (t(49) = 1.31, p = 0.19; t(47) = −0.27, p = 0.79). Similar vs dissimilar subadditivity difference only marginal (t(36) = 1.83, p = 0.07); effect size d = 0.17 vs d = 0.11.
- The authors conclude "that reuse is at least partially sensitive to similarity", and note the atypical (superadditive) answers were "not detectably being reused" when the cue changed.

**The bias cost.** "While reuse increases computational efficiency, it can cause errors in two ways." First, reuse across similar but not identical queries blurs the distributions together: "This is analogous to interference effects in memory." Second, "the answer to the first query might itself have been inaccurate or biased, so its reuse will propagate that inaccuracy to the second query's answer." The experiments test only the second. Neither is staleness in the sense of a world that changed after the computation. The general discussion frames the bias as rational: "this error may be a natural consequence of a resource-bounded system that optimally balances accuracy and efficiency", and claims that reuse inside a Monte Carlo scheme preserves "asymptotic exactness while improving efficiency in the finite-sample regime". No optimality is shown.

**What it says about memory, storage and the time–space trade.** It does not use the words cache, memoization or offloading, and nothing in it concerns storage outside the head. Its statements:

- Memoryless inference "forgoes the opportunity to reuse computations across queries, thus reducing time complexity (but possibly increasing space complexity)" (the sentence as printed attaches "reducing time complexity" to the memoryless engine; the sense of the passage is that reuse would reduce time and may cost space).
- Sample reuse "is expensive, because each sample must be stored in memory"; reusing all samples "is very intensive in its use of memory – in this aspect they are similar to exemplar models of categorization".
- "Summary-based amortization gives up some flexibility (compared to reusing the raw samples generated by past inferences), in order to gain memory-efficiency."
- Against Dougherty's memory-retrieval models of hypothesis generation: "The present paper asserts a more direct role for memory within a sampling framework, by controlling the trade-off between computation and flexibility."
- The reinforcement-learning analogy: model-free algorithms store reward estimates "in a look-up table or function approximator", so "model-free algorithms trade time for space, much in the same way that amortized inference uses memory to reduce the cost of approximate inference", and mixing model-free values into model-based search occupies "a middle ground in the time-space trade-off", analogous to summary reuse.
- Open questions it lists: "What objective function is being optimized by amortization? How are the computational trade-offs managed algorithmically? What are the contributions of different memory mechanisms (episodic, semantic, procedural, etc.)?"

**What it says Gershman & Goodman (2014) established.** Very little. It cites Gershman and Goodman (2014, "Amortized inference in probabilistic reasoning", CogSci 2014, pp. 517–522) twice: as a source of the term (with Stuhlmüller, Taylor and Goodman 2013) in the definition quoted above, and in the general discussion: "Building on earlier results (Gershman & Goodman, 2014), our findings support the existence of a sophisticated inference engine that adaptively exploits past computations." It does not say what those earlier results were, what task they used, or what they showed.

## Bearing on the record

**On [QUESTION-095](../questions.d/QUESTION-095.md): the paper joins the two ideas for internal memory, in so many words, and says nothing about the environment.**

- It treats amortized inference as a time-for-space trade and puts it beside a look-up table in reinforcement learning. Its summary-based scheme is memoization of a sub-result: Q1's answer is stored as one number and reused when Q2 can be decomposed into Q1 plus a remainder. So the owner's point, that keeping a result where it can be cheaply had again is a kind of amortized computation, is the paper's own framing, for results kept in the reasoner's memory.
- It does not cover the other two cases in the question. Nothing concerns results left in the world, read back by perception, or found by search in a record. Retrieval is free in its models; there is no retrieval cost, storage upkeep or search. Whether the speed bugs and filed arguments are the same trade is not addressed, and the paper does not join the amortized-inference and distributed-cognition literatures.
- It supplies two of the question's cost terms only qualitatively: memory cost (samples dear, summary cheap) and an error cost (propagated bias, interference between similar queries). It gives no break-even condition, no measure of expected reuse, and says itself that the objective amortization optimizes is unknown. Experiment 3 shows reuse is somewhat selective by similarity of the query, which is an empirical sign that reuse is gated by expected applicability, but the effect is marginal (p = 0.07) and the mechanism is left open.
- The failure mode it names is not the question's "staleness". Its reused result is wrong because it was approximated badly when computed, or because it is applied to a different but similar query. A result that was right and has since gone out of date does not appear. The record's cost model would need both terms, and they differ: one is fixed at computation time, the other grows with elapsed time.

**On [CLAIM-303](../claims.d/CLAIM-303.md): consistent, does not test it.**

- The paper's trade is the claim's trade at the scale of one reasoner: computation done once is reused at a cost in error. Its first error type, reuse "between two dissimilar distributions", matches the claim's warning that reusing the wrong filed result can cost more than recomputing; the paper's own words are that amortization "is not always useful" for that reason.
- It does not measure the cost side. No response times were recorded, and the only efficiency evidence is better probe accuracy on reusable trials (t(36) = 3.16). It has nothing on filing, indexing, dependency tracking or refresh, and no reuse count. It is not evidence for the break-even condition or for recurrence as evidence of reuse.

**On [CLAIM-295](../claims.d/CLAIM-295.md): the sample-versus-summary contrast is a clean instance of the claim's distinction, in a small domain.**

- The summary is a function of the samples, so keeping it in place of the samples adds no information and narrows what can be answered: it serves only queries composable from Q1's answer. The samples serve any query on the same distribution. That is the claim's "wider family of decisions for which what is kept suffices", bought here with memory. The paper calls the difference flexibility against memory-efficiency, and its Experiment 2 evidence, read through its simulations, favours the cheaper, narrower summary.
- Reuse at all is the computational value: stored Q1 computation lets Q2 be answered with less fresh work, without new information. The paper shows this only as freed capacity on a secondary task.
- It does not bear on the claim's thesis about justificatory history. Nothing is kept about how an answer was reached, and the paper's reuse spreads error rather than enabling its targeted correction; a reasoner holding only the summary cannot tell that Q1's answer was biased by its unpacking.

**On [LIT-1074](../literature.d/LIT-1074.md) as filed.** The filed summary says reuse "speeds inference and biases it toward earlier answers". Speed is assumed, not measured. And the bias is not a pull toward earlier answers as numbers: the no-overlap condition in Experiment 2 was built to rule out exactly that (numerical anchoring), and found no carry-over. What carries over is the error of the earlier computation, and only where its result is usable for the later query. The entry's keyword "memory" is right; the paper does not use "caching" or "offloading".
