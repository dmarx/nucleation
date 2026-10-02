---
number: 360
status: Read
formerly:
- NOTE-tmpt626p
paper: LIT-427
title: 'Selfridge — Pandemonium'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (a scan of the HMSO printing, Mechanisation of Thought
    Processes Vol. I, Session 3 Paper 6, pp. 511–531, from
    gwern.net/doc/ai/nn/1959-selfridge.pdf; PyMuPDF text, with the page
    images consulted where the OCR garbled formulas). I read the title page,
    the biographical note, the paper (pp. 513–526, figs. 1–8, Table 1) and
    the discussion: Bray, Strachey, McCarthy, MacKay, Price (written) and
    Selfridge's reply (pp. 527–531). The weight-vector and worth formulas on
    pp. 519 and 521 are unreadable in the OCR; they are paraphrased from the
    surrounding text, not transcribed. The 1988 reprint was not seen.
date: '2026-10-02'
summary: >-
  A proposal, with a preliminary Morse-code trial, for pattern recognition
  by a hierarchy of parallel "demons". Data demons hold the input,
  subdemons compute features, cognitive demons shout weighted sums, and a
  decision demon takes the loudest. It adapts by hill-climbing on the
  weights, by culling and breeding subdemons through mutation and
  "conjugation", and in principle by adapting its own control demons. The
  only result is reported in the discussion: hill-climbing "does work",
  subdemon selection "did not do what we hoped", and the best single
  subdemon was right 90% of the time.
---
<!-- inactive-ok-file: LIT-046 — Proposed; named as a neighbouring account of collective intelligence, not leaned on -->
<!-- inactive-ok-file: LIT-429 — Deferred, no lawful full text; named as the decomposition side of the bridge, not leaned on -->

# NOTE-360: Selfridge — Pandemonium

## Contribution

It gives the first explicit design for building a perceptual competence out
of many small, quasi-independent, specialised processes that run in
parallel, each anthropomorphised as a "demon". None of them has the
competence of the whole. It couples that design to learning at three
levels: weights, the feature set itself, and the control structure. The
feature set is learned by a selection-and-variation process, which is an
early statement of evolving the feature detectors and not only their
weights.

## Key insight

Do not try to specify a pattern in advance; for most human patterns
(spoken words, hand-keyed Morse) "the only adequate definition … must be in
terms of the consensus of the people who are using it" (p. 514). Instead,
build a crowd of cheap feature computers, let the categories vote by
weighted shrieks, and let a running score select both the weights and the
feature computers. The architecture is chosen for modifiability: an
assembly of quasi-independent modules is easier to change than a machine
whose parts all interact.

## Assumptions

- **Task.** Supervised pattern classification with a running score,
  meaning a monitor says when the machine errs (p. 518). Unsupervised
  operation comes later, and only after supervised training (p. 523).
- **Parallelism** is assumed natural for data handling and preferable for
  modifiability (p. 513). Simulation runs serially on an IBM 704 (p. 522
  footnote).
- **Hill-climbing landscape.** In high dimension "the interdependence of the
  components and the score is so great as to make very unlikely the
  existence of false peaks completely isolated from the main or true peak".
  This is hoped, and is called "a purely experimental question" (p. 521).
- **Anthropomorphism is vocabulary.** "Useful words to describe our notions"
  (p. 513).

## Key results

- **Idealised pandemonium** (fig. 1, p. 514). One demon per pattern
  computes similarity to the image, and the decision demon picks the
  maximum. Footnote: this is "an exact correlate" of minimum-distance
  decoding in a signal space (fig. 2). A second footnote rejects "ideal"
  pattern representatives as "unnecessarily platonic" (p. 516).
- **Amended pandemonium** (fig. 3, pp. 516–517). Computations the cognitive
  demons share go to subdemons. There are four levels: data, computational,
  cognitive and decision. Each cognitive demon's output is a weighted sum of
  subdemon outputs, and the weights are its only difference from the
  others.
- **Feature weighting** (pp. 517–521). The weight vector over all cognitive
  demons is searched to maximise the score. Two techniques are given: random
  sampling (fig. 4), and random sampling followed by small random steps that
  keep improvements (fig. 5, "a blind man trying to climb a hill"). False
  peaks (fig. 6), foot-hills and plateaux are discussed. Unicycle versus
  chess illustrate two kinds of learning difficulty.
- **Subdemon selection** (pp. 521–522). Each subdemon is given a worth that
  measures how strongly its output affects decisions (the formula is
  illegible in the scan). Low-worth subdemons are eliminated. New ones come
  from "mutated fission", random changes to a survivor's parameters after
  reduction to a canonical form so the program still runs. They also come
  from "conjugation", a continuous analogue of one of the ten non-trivial
  binary functions of two useful subdemons (Table 1).
- **Control adaptation** (p. 523). Control operations are demons too, and
  some "will be in a position to change themselves", which "raises the
  possibility of irreversible changes".
- **Evolution** (p. 523). This is natural selection on processing demons,
  and could extend to "some crowd" of pandemoniums.
- **Unsupervised operation** (p. 523). Use the margin by which one cognitive
  demon "far outshines the rest" as a proxy score.
- **Morse pandemonium** (fig. 7, pp. 524–525). Dot and dash cognitive demons
  each take a weighted sum over "some 150 computing subdemons". Data demons
  pass mark and space durations. Subdemons are built from a small, "carefully
  non-binary" vocabulary: degree of equality, of less-than and greater-than,
  of being the maximum, stored identifications, averages, tracking means,
  and the last durations identified. Planned extensions add space demons,
  then about forty character demons under a new decision demon (p. 526).
- **Results** are given only in the discussion (pp. 530–531). "Improvement
  does take place; the hill-climbing does work. The sub-demon selection …
  did not do what we hoped". The most effective single demon worked "90 per
  cent of the time". No data, test set or baseline is given.
- **Discussion.**
  - Bray proposes polynomial regression on durations; Selfridge says "it
    will not work; we have tried it", since context extends "at least 10
    letters on either side".
  - MacKay proposes "syndicated" learning: start with coupled elements to
    reduce diversity, then decouple them as competence grows. Selfridge
    calls it "an extremely accurate and good point".
  - Price distinguishes stochastic from determinate hill-climbing and asks
    about sample sizes. Selfridge does not answer this directly.
  - McCarthy: the demons' internal work as unconscious thought and their
    public shouting as conscious thought (p. 527).
  - Selfridge says speed "is so completely irrelevant to this problem" and
    hopes for parallel machines, so that a problem twice as hard needs a
    machine twice as big (p. 530).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Pandemonium can adaptively improve itself on pattern-recognition problems that cannot be specified in advance | weak (proposal) | design argument; the paper says it "does not … seem on paper to have the same kinds of inherent restrictions"; no results in the paper |
| C2 | An assembly of quasi-independent modules is easier to modify than a densely interacting machine | assertion | stated as a ground for the design (p. 513) |
| C3 | Hill-climbing on feature weights improves performance on hand-keyed Morse | weak | one sentence in the discussion ("the hill-climbing does work"); no numbers beyond the best single subdemon at 90% |
| C4 | Subdemon selection by mutation and conjugation improves the feature set | proposed; reported not to work as hoped | discussion p. 530 |
| C5 | In high-dimensional spaces, isolated false peaks are unlikely | hope | explicitly "a purely experimental question" (p. 521) |
| C6 | The machine can monitor its own performance by the unequivocality of its decisions | proposal | p. 523; conditional on prior supervised training |
| C7 | Demons' internal processing is unconscious thought; their public shouting is conscious thought | assertion (McCarthy, in discussion) | none; not taken up by Selfridge |

## Concepts

- **Demon** — a quasi-independent process at one level: data, computational
  (subdemon), cognitive, decision or control.
- **Shriek** — a cognitive demon's output, a weighted sum of subdemon
  outputs.
- **Worth** — a subdemon's influence on decisions, used to cull it.
- **Mutated fission / conjugation** — generating new subdemons by random
  parameter change, or by a binary logical function of two parents.
- **Hill-climbing, foot-hills, false peaks** — search vocabulary for feature
  weighting.

**Composition.** The whole's competence, recognition, belongs to no demon.
Each cognitive demon's competence is a weighted vote, and the decision
demon's is taking a maximum. The parts are not minded. The anthropomorphism
is declared to be vocabulary, and a subdemon is "reduce[d] … to some
canonical form" so that it can be mutated (p. 522). There is a top-level
decision demon, so it is a hierarchy with a single arbiter, not a flat
society.

## Connections

- **Minsky ([LIT-399](../literature.d/LIT-399.md), [LIT-402](../literature.d/LIT-402.md), [LIT-429](../literature.d/LIT-429.md)).** Minsky is thanked first
  (p. 526). Minsky's 1977 memo ([NOTE-344](NOTE-344.md)) has agents "just intelligent
  enough to accomplish their own specialized purposes", new agents "by
  splitting off from old ones, with only small changes", and
  perceptron-like detectors "on tap". These are Selfridge's subdemons,
  mutated fission and weighted cognitive demons, without Selfridge's
  decision demon on top. The lineage is my pairing; the memo is not read
  here as citing Selfridge.
- **Block ([LIT-407](../literature.d/LIT-407.md)).** Block's n. 19 replaces each homunculus with a
  McCulloch–Pitts "and" neuron. A pandemonium's demons are already at that
  level: a weighted sum, a maximum.
- **Schwitzgebel ([LIT-159](../literature.d/LIT-159.md), [NOTE-131](NOTE-131.md)).** Not cited. McCarthy's remark is a
  broadcast model of consciousness in one sentence. Schwitzgebel (p. 29)
  treats global-workspace and "fame" models as subsystem-driven, in his
  reply to Chalmers. McCarthy puts the conscious part in the shouting
  *between* demons, which reads more naturally as relational.
- **Collective intelligence ([LIT-046](../literature.d/LIT-046.md)).** A pandemonium is a designed collective
  whose members are mindless. Selection among a "crowd of" pandemoniums
  (p. 523) is a second, population level of the same design.

## Bearing on the record

- **For the bridge.** This is the decomposition side's starting point:
  competence assembled from parts that lack it, with mental vocabulary
  explicitly figurative. It is neutral on Schwitzgebel's C3–C5 because it
  never has minded parts. Its one consciousness claim (C7) is McCarthy's
  aside, and should be cited as that.
- **Anthology.** It carries machine-learning content: feature weighting by
  stochastic hill-climbing, and evolution of feature detectors. The LIT is
  tagged `anthology-candidate` (see its boundary paragraph).

## Limitations

- It is a proposal written in July 1958, before the runs it promises
  (p. 526). The results are three sentences in the discussion.
- There is no definition of the score beyond "how well the machine is doing
  the task", and no data set, error rates or baseline.
- The worth and weight formulas are illegible in the scan read here.
- The no-false-peaks hope in high dimension is unargued, and the author says
  so.

## Open questions

- Did the later runs promised for the November meeting, or later work, show
  subdemon selection working, or was the feature set fixed in practice?
- Does MacKay's "syndicated" coupling-then-decoupling change the picture of
  how parts become independent agents? It is the reverse of fission.

## Corrections

- none to a seeded skim (there was no seed)
- **Page range.** The paper is pp. 513–526. With the title page, the
  biography and the discussion, the item is pp. 511–531. The citations
  511–526 and 511–529 found online are each partly wrong.
