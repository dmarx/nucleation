---
status: Read
paper: LIT-tmpyk46l
title: 'Goudar and colleagues — Schema formation in a neural population subspace underlies learning-to-learn in flexible sensorimotor problem-solving'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader from Nature Neuroscience, doi
    10.1038/s41593-023-01293-9, from the PMC author manuscript PMC11559441
    (the Europe PMC interface returned an error; the supplement sat behind a
    download challenge and was not read); the date from Crossref: the whole
    main text, methods and figure legends; supplement and references not
    read. Running notes on the branch claude/readers/task-composition
    (ADR-108). Quotations rechecked by the filer by script against the
    downloaded text.
date: '2026-11-19'
summary: >-
  Harlow-style learning-to-learn in an RNN, trials to criterion falling
  exponentially; a reused decision subspace; a readout perturbation that
  removes the saving. One kind of learner; the representation itself is
  not ablated.
---
<!-- inactive-ok-file: CLAIM-756 — Proposed or newly filed; entries this reading bears on -->

# NOTE-tmpk8fli: Goudar and colleagues — Schema formation in a neural population subspace underlies learning-to-learn in flexible sensorimotor problem-solving

## Key results

1. **Trials to criterion.** "The network required a few thousand trials
   to learn the first problem"; "solving the second problem took a few
   hundred trials"; then "plateauing at an average of 20 trials per
   problem"; "time constant: 47.52 ± 26.22 (mean ± s.d.); asymptote: 21.33
   ± 3.85" over 30 seeds. "Crucially, training was performed without an
   explicit meta-learning objective."
2. **Causal test.** With the readout rotated off the decision subspace
   after problem 1 and frozen, networks "learned as slowly as naive
   networks learning their first problem"; the authors conclude "impeding
   the reuse of the decision manifold adversely affects learning
   performance" (Fig. 3).
3. **Transfer to a changed structure.** From two mappings to three, "Here,
   too, we observed a substantial facilitation of learning performance
   compared to a naive network".
4. **Mechanism, analysed.** "The magnitude of the plasticity-induced
   recurrent connection weight changes explains most of the variance in
   the number of trials to learn problems"; "the accumulation of weight
   changes over problems progressively improves representational
   invariance and, therefore, learning efficiency".

## Bearing on the record

- **[LEAD-006](../leads.d/LEAD-006.md)**, partial: (a) trials to criterion with and without
  earlier learning; (c) by readout perturbation, the representation left
  intact; not (b), one kind of learner. The shared structure is the trial
  structure and response set; later rules are new stimulus mappings.
  Public code; reinitializing the subspace inside the recurrent weights is
  the reader's suggestion.
- **[CLAIM-756](../claims.d/CLAIM-756.md)**, corroborates the premise: earlier problems lower later
  problems' cost in counted trials.
- **[CLAIM-596](../claims.d/CLAIM-596.md)** and **[QUESTION-397](../questions.d/QUESTION-397.md)**, parallel: barring reuse returns
  learning to naive speed, a process measure, not an endpoint.
- **[TERM-117](../terms.d/TERM-117.md)**, parallel: the decision subspace as a productive nucleus
  against a declared comparator.
- **[CLAIM-754](../claims.d/CLAIM-754.md)**, analogy: equal criterion each problem, falling cost of
  the next; one learner over time.
- **[THEORY-1358](../theory.d/THEORY-1358.md)** (Kemp, Goodman and Tenenbaum), parallel: learning to
  learn through a schema, Bayesian there; **[THEORY-2046](../theory.d/THEORY-2046.md)** and
  **[THEORY-2019](../theory.d/THEORY-2019.md)**, contrast: learning to learn here without a
  meta-objective.

## Limitations

One architecture at 100 units; the causal test only after problem 1; no
numbers for Figs. 3c and 6a in the text; monkey data unpublished; the
earlier problems' cost not netted.
