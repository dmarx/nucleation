---
number: 649
status: Read
formerly:
- NOTE-tmpusmlj
paper: 'LIT-848'
title: 'Large AI models are cultural and social technologies'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the authors' accepted version: the Science galley
    of 25 February 2025 (4 pp., two- and three-column layout, line
    numbers), posted by Henry Farrell on henryfarrell.net; text extracted
    with pdftotext and read whole, including the 15 references and the
    acknowledgement. The version of record (Science 387(6739):1153–1156)
    was not seen. The galley's reference list carries copy errors: ref. 2
    prefixes Hayek (1945) with "Yiu, E. Kosoy, A. Gopnik"; ref. 7 (Goldin
    and Katz, QJE 113) has "(year)"; ref. 15 gives Nat. Hum. Behav. as
    vol. 11, where the 2023 volume is 7. Simon, Scott, Davies, Chiang and
    the other cited works were not read.
date: '2026-10-09'
summary: >-
  Argues that large models are a cultural and social technology, not
  intelligent agents: lossy, uninvertible summaries of human-produced
  corpora that, like prices and bureaucratic categories, allow the
  information to be reorganized at scale. The argument is by analogy and
  classification; no evidence is offered that could have come out
  otherwise. It names one mechanism (fitting the training distribution on
  average makes models worst where data are rare, which may homogenize
  culture) and leaves both it and its remedy untested.
---
<!-- inactive-ok-file: THEORY-023 — Proposed; named as an adjacent account, not leaned on -->
<!-- inactive-ok-file: THEORY-173 — Proposed; the account this reading files, not settled -->

# NOTE-649: Large AI models are cultural and social technologies

## Contribution

A short, programmatic reclassification by a political scientist, a
developmental psychologist, a statistician and a sociologist. Its own
citations point to Gopnik's work on imitation and innovation (ref. 5, Yiu,
Kosoy and Gopnik 2024, not read) as a prior source for the cultural half.
Here the view is stated in Science, joined to the older idea that markets, bureaucracies
and democracies are information-processing technologies (Simon, Hayek,
Scott), and turned into a research agenda for the social sciences. It adds no
new evidence.

## Key insight

Ask what a large model is the way one asks what a price is. A price
compresses what countless people know, want and do into a number that is
lossy and cannot be inverted, yet lets strangers coordinate, and it then
shapes what they know and do. A large model does the same for text and
images, with one addition: it lets people operate on the compressed culture,
restating, condensing and recombining it. On this view an LLM is a social
institution made of other people's work, not a mind. Its agent-like
interface is a storytelling convention, like Anansi or a market treated as
"wanting" something.

## Assumptions

- **Agency is a capacity to find truth in a changing world**: perceiving
  and acting on it, building and revising models of it as evidence
  accumulates, designing novel goals. Large models "simply sample and
  generate text and images" and have "no conception of truth and falsity".
  The paper does not defend this characterisation against views on which
  in-context inference or RLHF-trained models count as agents in some
  degree.
- **Large models are taken as they are deployed now** (pretrained,
  RLHF-tuned, prompted by people). Agentive systems, robotics and possible
  future AGI are set aside, explicitly, as a different question.
- **The analogy carries the argument.** Features shared with print,
  markets and bureaucracies (abstraction, scale, lossy representation,
  distributive struggle) are taken to predict the kinds of effects. No
  criterion is given for when the analogy would fail.

## Key results

No theorems or experiments. The paper's propositions, as stated:

- **Classification.** Large models "combine the features of cultural and
  social technologies in a new way": they summarize "unmanageably large
  and complex bodies of human-generated information", like catalogues,
  search and Wikipedia, and they "reorganize and reconstruct
  representations or 'simulations'" at scale, like markets, states and
  bureaucracies.
- **Lossiness.** Market prices, government statistics and bureaucratic
  categories are "lossy (i.e., incomplete, selective, and uninvertible)
  but useful representations", and large models are "'lossy JPEGs' of the
  data corpora on which they have been trained".
- **Scaling.** Large models "are fundamentally different from intelligent
  agents and 'scaling' won't change this"; hallucination is "endemic".
- **The distributional mechanism.** Models are built to reproduce
  sequence probabilities "on average", so they are "most accurate in
  situations most commonly found in their training data and least accurate
  in situations which were rare in data or entirely novel", which "might"
  worsen homogenization.
- **Producer–distributor tension.** Producers and distributors of
  information need each other and have opposed incentives; the speed and
  centralized ownership of large models sharpen the tension.
- **Institutions.** The institutions that tempered earlier technologies
  (editors, peer review, libel law, election law, deposit insurance, the
  SEC) did not emerge by themselves but "resulted from concerted and
  sustained efforts".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Large models are better understood as a cultural and social technology than as intelligent agents | weak (argument by analogy) | the whole paper; no test proposed |
| C2 | Large models, like prices and bureaucratic statistics, are lossy and uninvertible but useful representations of what they summarize | moderate as description | the analogy, and the training objective (estimating a distribution over sequences) |
| C3 | Hallucination is endemic and scaling will not make large models agents | weak | asserted |
| C4 | Because models fit their training distribution on average, they are least accurate on rare or novel cases, and this may homogenize culture | moderate for the first half (follows from the objective); weak for the second (stated as a possibility) | informal argument |
| C5 | Ecologies of diversified models might preserve or recombine perspectives | speculative | citations to the authors' and others' position papers |
| C6 | The countervailing institutions of earlier technologies were made by sustained effort, not emergent | moderate as history | asserted, with examples |

## Concepts

- **cultural technology**: a means by which humans access information other
  humans have created (pictures, writing, print, video, search).
- **social technology**: an institution, after Simon's "artificial systems
  of human society", that processes information to enable large-scale
  coordination (markets, bureaucracies, democracies).
- **lossy representation**: incomplete, selective and uninvertible, yet
  useful; a price, an election result, GDP, a bureaucratic category, a
  large model.
- **Large Models**: the paper's term for current large language, vision and
  multimodal models, distinguished from "more agentive systems".

## Connections

- **Shanahan, McDonell & Reynolds ([LIT-460](../literature.d/LIT-460.md)).** Both deny that the model is
  an agent with beliefs and goals, and both account for the appearance of
  one through fiction. [LIT-460](../literature.d/LIT-460.md) does it from inside the model (a simulator
  role-plays characters, "no-one at home"); this paper does it from the
  culture (stories have always used illustrative agents, and chatbots are
  their successor). The paper does not cite Shanahan. The two are
  compatible: role play is a mechanism by which a lossy summary of
  storytelling produces a storytelling device.
- **[THEORY-023](../theory.d/THEORY-023.md).** That account says behavioural evidence cannot settle AI
  consciousness because the system mimics human output. This paper moves
  the same fact (the output is other people's) from an epistemic obstacle
  to an ontological classification: the system is the others' output,
  reorganized.
- **Hayek, Simon, Scott.** The social-technology half is a compressed
  restatement of Hayek's price as a summary of dispersed knowledge, Scott's
  legibility, and Simon's artificial systems; nothing new is added to them.

## Bearing on the record

- Files [THEORY-173](../theory.d/THEORY-173.md), Proposed: large models are cultural and social
  technologies, lossy summaries of human-produced corpora, rather than
  agents. The record held no statement of this view; the selfhood cluster
  ([LIT-460](../literature.d/LIT-460.md), [LIT-465](../literature.d/LIT-465.md), [LIT-466](../literature.d/LIT-466.md)) argues about what, if anything, is a self in
  the system, and this paper is the rival that declines that question.
- **On repeated reconstruction.** C4 is a mechanism for contraction toward
  the common: a model that fits the average reproduces typical material
  better than rare material, so a culture that routes its production
  through such models drifts toward its own modes. That is a hypothesis
  about cultural transmission with a model in the loop; the paper does not
  model or measure it.
- **On models as instruments.** If a model is a lossy summary of a
  corpus, then what it judges or prefers is a property of that summary, not
  of any community of speakers. The paper does not draw this consequence;
  it is mine.
- The paper's suggestions for AI practice ("thinking in this way might
  reshape AI practice") are programmatic, not instructions, which is why
  the LIT carries `anthology-candidate` rather than being sent across.

## Limitations

- A Policy Forum of about 3,500 words. The case against agency is
  asserted from a definition of agency the paper chooses, and scaling's
  irrelevance is stated, not shown.
- No criterion is offered by which the classification could turn out
  wrong, for instance a capacity whose presence would make a large model an
  agent rather than a technology.
- The homogenization mechanism and its remedy are both hedged with
  "might" and "may"; nothing is measured.
- The analogy cuts both ways and the paper does not weigh it: markets and
  bureaucracies are also routinely modelled as agents in economics and
  organization theory, so "treating it as an agent" is not obviously a
  mistake for them either.
- The accepted version's reference list has copy errors (see the history
  note); the published version may differ.

## Open questions

- What observation would distinguish "a social technology that looks like
  an agent" from "an agent built from a social technology"? The paper's
  framing needs one to be more than a choice of description.
- Does routing cultural production through large models measurably narrow
  the distribution of what is produced (C4), and do diversified ensembles
  (C5) undo it? A study of iterated generation with and without such
  ensembles would test both.
