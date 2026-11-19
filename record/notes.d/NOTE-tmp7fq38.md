---
status: Read
paper: LIT-tmpexypk
title: 'Driscoll, Shenoy and Sussillo — Flexible multitask computation in recurrent networks utilizes shared dynamical motifs'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader from Nature Neuroscience, doi
    10.1038/s41593-024-01668-6 (CC BY 4.0), through the Europe PMC full-text
    interface for PMC11239504 (ADR-101); the date from Crossref: all of the
    text, methods and figure captions; Supplementary Table 1 not in the XML;
    plotted values not read. Running notes on the branch
    claude/readers/task-composition (ADR-108). Quotations rechecked by the
    filer by script against the downloaded text.
date: '2026-11-19'
summary: >-
  Shared dynamical motifs in multitask RNNs; transfer by training only a
  rule input, fast when the needed motif was learned before; lesions of
  motif clusters, on trained networks only. No matched comparison of
  organizations; no intervention on the transferred motif.
---
<!-- inactive-ok-file: LEAD-tmphfbq0 CLAIM-756 CLAIM-754 THEORY-tmpf6s7m THEORY-tmppm9la — Proposed or newly filed; entries this reading bears on -->

# NOTE-tmp7fq38: Driscoll, Shenoy and Sussillo — Flexible multitask computation in recurrent networks utilizes shared dynamical motifs

## Contribution

A mechanistic unit, the dynamical motif, "the high-dimensional nonlinear
dynamics around a fixed point skeleton that implements computation for a
specified input" (Results), and a two-stage account of learning: slow
learning of motifs, then fast recombination through an input vector.

## Key results

1. **Transfer protocol.** "all network connections were held fixed except
   for the rule input weights of the held-out task" (Methods).
2. **With and without the motif** (Fig. 6b, five networks per arm).
   "Pre-training on this minimal set with relevant motifs achieved similar
   speed and proficiency as pre-training on all tasks", whereas
   "pre-training on tasks lacking the anti motif (orange) or no
   pre-training (green) resulted in significantly slower learning or
   failure to learn MemoryAnti entirely". No test is named and no
   threshold numbers are given.
3. **New motif through the input alone.** "Despite slow and variable
   learning, networks pre-trained on tasks lacking the anti motif were
   still able to learn the new dynamical motif by modifying the rule input
   vector".
4. **Limit of reuse.** "The fast learning benefit was smaller, and the
   long-term cost was negative for tasks with unique dynamical motifs"
   (Methods); "rapid learning was not as successful in the context of
   novel tasks with unique dynamical motifs" (Results).
5. **Lesions** on one trained network: "A lesion to one cluster (Fig. 3a,
   unit cluster c) only impacted performance on tasks that included a
   delayed response"; the authors note "limitations in our approach to
   link clusters of units directly to dynamical motifs".
6. **Robustness.** "A total of 144 networks were trained, each with
   different hyperparameters"; unit-aligned clusters depend on the
   activation function.

## Assumptions

Fixed points of piecewise-constant inputs are the task's skeleton; a smooth
fixed-point bridge under rule-input interpolation means a motif is shared.

## Concepts

Dynamical motif; fixed-point skeleton; rule-input interpolation; task
variance clusters; transfer by training only an input.

## Bearing on the record

- **LEAD-tmphfbq0**, partial: (a) learning curves with and without the
  relevant prior learning; not (b), since arms differ in pretraining data;
  not (c) for the saving, since lesions are on trained networks and no
  motif is removed before transfer. The composition is a recombination of
  modules, not h after a shared g. A testbed for (c), the reader's
  suggestion: lesion the anti-stimulus cluster before training the new
  rule input; networks and code are public.
- **CLAIM-756**, corroborates its premise: an earlier acquisition (the
  anti motif) lowers the cost of a later one; no first-stage cost
  accounting.
- **CLAIM-754**, an empirical instance of an interface-relative
  developmental frontier: with learning confined to one input vector, what
  is reachable depends on motifs held, and tasks needing new motifs fall
  behind full plasticity.
- **CLAIM-596**, parallel: a rate comparison of a later acquisition; the
  blue and orange arms both hold the memory motif, isolating the anti
  motif.
- **THEORY-tmpf6s7m** (Papadimitriou and Jurafsky), the closest design
  parallel: frozen recurrent weights, only an input trained, sources with
  and without the needed structure.
- **THEORY-tmppm9la** (Anguita and colleagues), parallel: an input-only
  regime forces reuse and loses when the new task's features do not
  overlap.
- **QUESTION-039**, background: slow acquisition of motifs, then fast
  recombination, two kinds of acquisition.
- **TERM-117**, analogy; **THEORY-1287**, background on what lesions show.

## Limitations

Simplified networks; 3–5 seeds and no sample-size calculation; lesions on
one network; no numbers for transfer speed in the text.
