---
status: Read
paper: 'LIT-tmpmefe6'
title: 'Chalupka, Eberhardt and Perona — Causal feature learning: an overview'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from the publisher's PDF (Springer, 28
    pages, Behaviormetrika 44:137–164) as posted on Frederick
    Eberhardt's Caltech publications page
    (https://www.its.caltech.edu/~fehardt/papers/CEP2017.pdf), text
    extracted with pdftotext -layout. Read: the abstract, §§1–4, the
    mathematical appendix (§5, Lemma 8 and the proof of the causal
    coarsening theorem), the captions of Figures 1–10, the notes and
    the references. The figures are diagrams and scatter plots, read
    from their captions; no number was taken from a chart, and the
    generative probability table of Figure 4 is an image, so the toy's
    numbers were not checked against it. Checked: the algebra of eqs.
    (1), (5)–(6) and (10), where two slips were found (below). Algorithms 1 and 2 were read from the text
    that describes them; their pseudocode boxes did not survive
    extraction. The UAI 2015 paper and the El Niño paper it reviews were
    not read; the 2016 paper whose theorem it restates is NOTE-tmpiw2bv.
date: '2026-10-29'
summary: >-
  A macro cause is a class of micro states with the same P(effect |
  man(state)); a macro intervention is any manipulation into the class,
  which is unambiguous by construction. The causal coarsening theorem
  makes the causal partition a coarsening of the observational one
  except on a null set, so one experiment per observational class finds
  it. No distribution over interventions enters the definitions. The
  example is a one-dimensional toy, and two displayed equations carry
  slips.
---
<!-- inactive-ok-file: THEORY-787 — Proposed; the causal thesis this reading bears on, cited as open -->
<!-- inactive-ok-file: QUESTION-204 QUESTION-115 QUESTION-252 — Open; the questions this reading bears on, cited as open -->

# NOTE-tmpbrnim: Chalupka, Eberhardt and Perona — Causal feature learning: an overview

## Contribution

An invited review of causal feature learning (CFL). It gathers the
definitions of the UAI 2015 and AISTATS 2016 papers into one framework,
works them on a toy with a confounder, restates and proves the causal
coarsening theorem for causes and effects, and lists what CFL assumes
and cannot yet do.

## Key insight

A macro variable is a partition of micro states, and it is a causal
variable only if every micro state in a cell has the same effect under
manipulation. Then "do(macro = c)" means "set the micro state to any
member of c", and nothing about which member is chosen matters, so no
distribution over realizers is needed. The observational partition,
which can be learned from passive data, is generically finer than this
causal partition, so experiments are needed only to merge its cells.

## Assumptions

- Micro cause H (hue) and micro effect E (eda), possibly confounded by a
  hidden lat: p(hue, eda) = Σ_lat p(eda | hue, lat) p(hue | lat) p(lat)
  (eq. 1, as it should read).
- A micro manipulation man(hue = h) sets hue without touching lat or eda:
  P(eda | man(h)) = Σ_l P(eda | h, l)P(l) (eq. 2).
- Macro variables are discrete with manageable cardinality (§3.1); the
  micro system is acyclic (§4.2); the macro–micro relation is
  constitutive, not causal (§4.1).
- For the theorem: discrete I, J, H, the joint parametrized freely by
  P(J | H, I), P(I | H), P(H), with Lebesgue measure on the parameters.
- Coarse observational partitions arise from equal fundamental
  parameters, not from coincidental algebraic cancellation (§2.3); the
  authors call this assuming that "there exist causal macrovariables in
  nature".

## Key results

- **Definitions.** Observational partition (Def. 1): h₁ ~ h₂ iff
  p(e | h₁) = p(e | h₂) for all e; e₁ ~ e₂ iff p(e₁ | h) = p(e₂ | h) for
  all h. Fundamental causal partition (Def. 3): the same with man(h).
  Fundamental cause C and effect S are the class labels (Def. 4). A
  macro intervention do(X = x) is man(hue = h) for some h with X(h) = x
  (Def. 5).
- **Toy.** Four hue bands with constant p(eda | hue); P(E = 1 | H) = 1,
  1/3, 0, 4/5 observationally. Manipulating one representative per band
  (hues 36, 100, 195, 320; 25 trials each) gives 22/25, 1/25, 6/25, 23/25
  against ground truth 0.83, 0.1, 0.1, 0.83, so bands merge into "Red"
  (the cause) and drop "Warm" (a confounded correlate).
- **Causal coarsening theorem (Theorem 7, §5).** Among joints with a
  fixed causal partition and a fixed confounding partition P_{P(hue |
  lat)}, those whose causal partition of H, or of E, is not a coarsening
  of the observational one have Lebesgue measure zero. The proof fixes
  P(J | H, I) and P(I | H) and shows the violating set of P(H) is the
  zero set of a non-trivial polynomial (Okamoto 1973), then integrates.
- **Unknown cardinality (§3.3).** Over-cluster and merge. For effect
  clusters the likelihood vectors are normalized first, because two
  clusters of one observational class but of different sizes have
  proportional, not equal, vectors.
- **Open problems (§4.2).** Learning without experiments, continuous
  macrovariables (no coarsening theorem for uncountable partitions), and
  cyclic micro systems.
- **§4.3.** "There is a sense in which the occurrence of macrovariables
  is a measure zero event"; temperature is "a little bit 'fuzzy around
  the edges'" because some micro states in a macrostate have different
  effects.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Causal macrovariables are the classes of equal P(effect \| man(micro)) | definition | Defs. 3–5 |
| C2 | The causal partition generically coarsens the observational partition, for cause and effect | strong, as a genericity result | Theorem 7 with proof; measure-zero, not a bound |
| C3 | One experiment per observational class suffices to find the causal partition | strong, given C2 and exact estimates | follows from C2; toy with 25 trials per class |
| C4 | CFL recovers known structure on complex data (neural simulation, El Niño) | moderate | reported from the cited papers, not shown here |
| C5 | Hoel et al. (2013) lose the interventional/observational distinction | weak | one sentence, no computation |
| C6 | Macrovariables are task-specific: the partition depends on the chosen output space | moderate | argument (§1.3) |

## Concepts

- **Ambiguous manipulation** (Spirtes and Scheines 2004): total
  cholesterol, whose effect depends on its LDL/HDL split.
- **Observational, causal and confounding partitions**: partitions of
  the cause space by p(e | h), p(e | man(h)) and p(h | lat).
- **Constitutive versus causal** macro–micro relation (§4.1), against
  psychometric latent variables.

## Connections

It builds on computational mechanics (Shalizi and Crutchfield, LIT-1126),
whose causal states group histories by equal conditional futures; CFL
replaces conditioning with manipulation. Its macro cause of a single
cause variable is the optimum of the causal information bottleneck at
full weight on control (LIT-1802, THEORY-1125). Eberhardt and Lee
(LIT-tmpr2bnp, NOTE-tmp0q96y) recommend it against effective information
(LIT-1038). The two-sided theorem and the sufficiency results are in
LIT-tmplfiq6 (NOTE-tmpiw2bv). Rubenstein et al. (LIT-1334) and Beckers
and Halpern (LIT-1316) cite it as learned macro variables.

## Bearing on the record

- **QUESTION-204, second half.** The question asks for an independent
  interventionist test of which level the effects track, "such as
  realization insensitivity under changes of realizer". CFL's causal
  partition is that test, stated exactly: two micro states share a macro
  state iff manipulating to either has the same effect. It is
  independent of EI-type choices: it uses only point manipulations, so
  no distribution over interventions, uniform or otherwise, enters. The
  record's derivation (THEORY-tmpyfcov) shows that the coarse-grainings
  at which EI under one common distribution ties the micro are exactly
  CFL's partitions and their refinements, for every such distribution.
  So the causal criterion and the test agree on which coarse-grainings
  lose nothing. Hoel's EI, scored uniformly at each level, does not agree
  (NOTE-tmp0q96y's (13), (14) and note 6). The overview itself computes
  nothing on Hoel's systems.
- **THEORY-787.** CFL delivers a verdict on a system, but not the verdict
  THEORY-787 wants. On a transition matrix its causal partition is the
  coarsest description with unambiguous manipulations; the micro
  description is never worse, only finer. It supports "the macro is the
  proportionate level" where micro rows are exactly equal, as in Hoel's
  (11), and gives the micro on the others. It does not support "causation
  emerges at the macro". It also needs exact equality: §§3.3 and 4.3
  merge by a distance threshold and concede fuzzy edges.
- **QUESTION-115.** For the macrostate criterion, CFL is a further
  candidate that disagrees with EI on one system: on Eberhardt and Lee's
  (14) EI picks {x₁, x₂}, {x₃} and CFL the micro. It also lets cause and
  effect be partitioned differently, which EI's shared partition does
  not.
- **QUESTION-252.** CFL separates two sufficiency conditions:
  observational (the observational partition) and interventional (the
  causal partition). The coarsening theorem says the interventional one
  generically holds wherever the observational one does, and the toy's
  "Warm" variable shows the converse failing: a partition sufficient for
  prediction that is not causal. It is a configuration where predictive
  sufficiency for a target holds and the causal reading fails, and
  "macrovariables are task-specific" (§1.3) is a declared-target
  condition.

## Limitations

- **Eq. (1) slip.** It prints p(eda | hue, lat)p(eda | lat)p(lat); the
  middle factor must be p(hue | lat).
- **Eqs. (5)–(6) slip.** The step from Σ_lat P(eda | h, lat)P(lat | h) to
  Σ_lat P(lat)(P(eda | h₁, lat)P(h₁ | lat) − …) drops the factors 1/P(h₁)
  and 1/P(h₂) of Bayes's rule, so the equivalence holds only when
  P(h₁) = P(h₂). The appendix's eq. (10) keeps them.
- Lemma 8 writes P(T | …) for P(J | …) twice; a notational slip.
- The theorem conditions on fixed causal and confounding partitions;
  the 2016 paper conditions on fixed observational partitions
  (NOTE-tmpiw2bv). The acknowledgements thank a reviewer "for pointing
  out an error in our original theorem" without saying what it was.
- The theorem is about measure, and §2.3 concedes that equal parameters
  carry the same measure as coincidental cancellation; the argument
  that macro structure is not coincidental is an assumption about
  nature.
- No measure of how much a near-causal merge loses.

## Open questions

- Is there a graded version of the causal partition that does not bring
  back an intervention distribution? THEORY-tmpyfcov says the amount of
  loss depends on one.
- What does the causal partition of a whole transition matrix look like
  when cause and effect must share one partition, as in Hoel's set-up?
