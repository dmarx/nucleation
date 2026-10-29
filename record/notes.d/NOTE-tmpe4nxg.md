---
status: Read
paper: 'LIT-1126'
title: 'Shalizi and Crutchfield — Computational mechanics'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from arXiv's own copy, v2 of 19 June 2000
    (https://arxiv.org/pdf/cond-mat/9907176, 29 pages), text extracted
    with pdftotext; the two-column layout scrambles the order of some
    equations, which were reassembled from the proofs. Read: §§I–VII,
    Appendices A–G, the 131 references and the glossary. The proofs of
    Lemmas 1–8, Theorems 1–6 and Theorem 7 (App. F) were followed step by
    step and found sound. The journal version (J. Stat. Phys. 104, 2001)
    was not compared; OpenAlex lists no free copy of it. The PDF's date
    line, "November 26, 2024", is a LaTeX \today artifact of arXiv's
    rebuild, not the paper's date.
date: '2026-10-29'
summary: >-
  For a discrete-valued, discrete-time stationary process whose joint
  distribution is known, the causal states (classes of pasts with the
  same distribution over the whole future) are as predictive as the full
  past, are the minimal and, up to measure zero, the unique such states,
  and have the least stochastic transitions; their entropy Cµ bounds the
  excess entropy from above. Minimality holds only for predicting the
  entire future: for any finite horizon a coarser state set can be as
  predictive and simpler. The paper proves these; it does not show how to
  estimate causal states from data.
---
<!-- inactive-ok-file: CLAIM-327 — Proposed; the claim this reading bears on, cited as open -->

# NOTE-tmpe4nxg: Shalizi and Crutchfield — Computational mechanics

## Contribution

It supplies the proofs that computational mechanics had lacked. Causal
states had been defined in 1989 and used since; this paper proves that
they are maximally prescient (Theorem 1), minimal among equally prescient
states (Theorem 2), unique among minimal ones up to measure zero
(Theorem 3, new here), and minimally stochastic (Theorem 4). It adds the
bounds E ≤ Cµ (Theorem 5) and a control theorem (Theorem 6). The
introduction places the approach against algebraic, algorithmic and
Dennett's error-tolerant accounts of pattern.

## Key insight

A pattern in a process is a partition of its histories used for
prediction. Grouping histories by their conditional distribution of
futures loses nothing about the future, and any other partition that
also loses nothing must be a refinement of that one almost everywhere.
So the coarsest lossless partition is unique, and its entropy is the
process's memory, a quantity distinct from how much the observed past and
future share (E).

## Assumptions

Listed by the authors in §VII B:

1. The joint distribution over sequence blocks of every length is known
   exactly.
2. Values are discrete (a countable alphabet).
3. Time is discrete.
4. The process is a pure time series, without spatial extent.
5. The process is stationary.
6. Prediction uses only the process's own past.

Also: functions on histories are "sufficiently tame, measure-theoretically"
that induced distributions exist (footnote 2).

## Key results

- **Definition 5.** ε(s⃖) = {s⃖′ : P(S⃗ | s⃖) = P(S⃗ | s⃖′)}; causal states
  are the range of ε; each has a unique "morph" P(S⃗ | σ).
- **Lemma 1 (Old Country).** H[S⃗ᴸ | R] ≥ H[S⃗ᴸ | S⃖] for every effective
  state class R and every L.
- **Theorem 1.** H[S⃗ᴸ | R] ≥ H[S⃗ᴸ | S] for all R, L; causal states are
  sufficient statistics (Corollary 1).
- **Lemma 5.** ε-machines are deterministic in the automata sense: the
  current causal state and next symbol fix the next state.
- **Lemma 6.** The sequence of causal states is Markov.
- **Lemma 7 (Refinement).** Every prescient rival state is, up to a
  measure-zero set, inside one causal state.
- **Theorems 2–3.** Cµ(R̂) ≥ Cµ(S) for prescient rivals, with equality
  only for an a.e. relabelling of the causal states; causal states are
  minimal sufficient statistics (Remark 3).
- **Theorem 4.** H[R̂′ | R̂] ≥ H[S′ | S].
- **Theorem 5.** E = I[S⃗; S⃖] ≤ Cµ, with equality iff H[S | S⃗] = 0; for
  range-R spin chains Cµ = E + R hµ, and periodic processes have
  Cµ = E = log₂ p.
- **Theorem 6.** H[S] − hµ[S⃗ | R̂] ≤ Cµ, a version of Ashby's requisite
  variety; App. F gives H[S⃗] − H[S⃗ | R̂] ≤ Cµ when H[S⃗] is finite.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Causal states predict the future as well as the whole past | strong | Theorem 1 |
| C2 | No equally predictive state class has lower entropy | strong | Theorem 2, via Lemma 7 |
| C3 | The minimal predictive state class is unique up to measure zero | strong | Theorem 3 |
| C4 | Causal-state transitions are the least uncertain of any prescient states | strong | Theorem 4 |
| C5 | Excess entropy is a lower bound on stored memory, not a measure of it | strong | Theorem 5 |
| C6 | Minimality is relative to predicting the whole future | strong | Theorem 2, Remark 2 |
| C7 | Causal states are "causal" | weak | Humean succession plus conditional independence (§II E, §VII A); no interventions |

## Concepts

- **Effective state**: a cell of a partition R of the set of histories,
  via η : S⃖ → R. Occam's pool is the set of all such partitions.
- **Causal state**: a cell of the partition induced by ∼ε.
- **Morph**: a causal state's conditional distribution of futures.
- **Statistical complexity Cµ**: H[S], the entropy of the causal state.
- **Prescient rival**: an effective state class with the same H[S⃗ᴸ | ·]
  as the causal states for every L.
- **ε-machine**: the causal-state function with its labelled transition
  matrices T⁽ˢ⁾.

## Connections

The paper states its own: Crutchfield and Young 1989 for the definition;
Grassberger's "true measure complexity", which it formalizes; Rissanen's
MDL and context algorithm, from which it differs on random sources; Nerode
equivalence for finite automata; Wiener–Kolmogorov prediction; Salmon's
statistical-relevance basis, of which causal states are an instance;
Ashby for the control theorem. In the record, Rosas et al.'s "software in
the natural world" ([LIT-1306](../literature.d/LIT-1306.md)) builds its causal closure on ε-machines.

## Bearing on the record

- **[CLAIM-327](../claims.d/CLAIM-327.md).** A10 offered causal states as "the minimal history a
  collective must keep to predict its future", a candidate for the slow
  state that survives turnover, and the LIT records A10's own caution
  that they are not thereby the boundaries of a social individual. The
  reading supports the caution and adds two limits. The theorems need
  the observed process fixed in advance (alphabet and variables) and
  stationary, and the authors say it is "unclear" how to relax
  stationarity, which a collective under turnover may not have. And the
  causal states are minimal only for the whole future (Theorem 2,
  Remark 2): for a finite horizon a coarser and simpler state can be as
  predictive, so "the" slow state depends on the horizon of prediction.
  Proposed dated note below.
- **[CLAIM-152](../claims.d/CLAIM-152.md).** The causal states are a minimal sufficient statistic,
  and the paper's target is explicit: the semi-infinite future of the
  same observable. They are an instance of the claim, with the target
  fixed by construction rather than chosen.
- **[QUESTION-115](../questions.d/QUESTION-115.md).** E ≤ Cµ separates what is measurable from sequences
  (E) from the memory needed to produce them (Cµ), the same distinction
  the question draws between retention measured on observables and a
  system's state.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **No inference.** ε-machine reconstruction from finite data is
  described as "an activity about which we have said next to nothing"
  (§VII C); error statistics are future work.
- **"Causal" is thin.** By the authors' own account causality enters "in
  an extremely weak sense", Humean succession made probabilistic. Nothing
  is shown about interventions.
- **Measure-theoretic caveats** are acknowledged and deferred (footnote 2,
  §VII C).
- **Slips.** Lemma 6 is titled "Causal States Are Independent" but proves
  that they form a Markov chain. The TOC and front matter run into each
  other in the arXiv layout. No error of substance was found in the
  proofs.

## Open questions

- What is the "prediction frontier" the authors mention: the minimal
  machine for each level of prescience between the one-state machine and
  the ε-machine?
- Which, if any, of the theorems survive non-stationary processes, and
  for a collective with turnover, what plays the role of the process?
