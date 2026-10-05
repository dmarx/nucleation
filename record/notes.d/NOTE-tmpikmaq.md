---
status: Read
paper: LIT-tmpsyl6j
title: 'Experimentation by Industrial Selection'
version: 1
history:
- version: 1
  date: '2026-10-05'
  note: >-
    Read in full: the publisher's PDF from ANU Open Research, printed
    pp. 1008–1019, footnotes and references, and the notice page. Figures 1
    and 2 read from rendered page images; the percentages below are read
    off plotted curves and are approximate. The extracted text renders σ as
    "j" and "=" as "5".
date: '2026-10-05'
summary: >-
  Uses the antiarrhythmic drug disaster and a modified Zollman bandit model
  to show that industry can bias a scientific community of honest Bayesian
  agents by funding those whose methods already favour its product, given
  methodological diversity, merit-based influence and turnover. A
  merit-based independent funder makes this worse; one that discounts
  industry-funded work counteracts it. Integrity safeguards do not touch
  the mechanism.
---
<!-- inactive-ok-file: LIT-tmpyzyje — Deferred; cited for context or as the source of this reading, nothing here rests on its being settled -->
<!-- inactive-ok-file: THEORY-tmpm45lu — Proposed; cited for context or as the source of this reading, nothing here rests on its being settled -->
<!-- inactive-ok-file: THEORY-tmpgo526 — Proposed; cited for context or as the source of this reading, nothing here rests on its being settled -->
<!-- inactive-ok-file: THEORY-tmpqnfk9 — Proposed; cited for context or as the source of this reading, nothing here rests on its being settled -->
<!-- inactive-ok-file: THEORY-tmpv9j17 — Proposed; cited for context or as the source of this reading, nothing here rests on its being settled -->

# NOTE-tmpikmaq: Experimentation by Industrial Selection

## Contribution

It separates two ways industry can bias science. The familiar one corrupts
individuals through conflicts of interest. The one this paper names,
industrial selection, changes which methods prosper in a community while
leaving every individual's judgment untouched, and it shows the second in
a model built so that funding cannot affect any agent's beliefs.

## Key insight

A funder does not need to change anyone's mind. Where researchers
honestly disagree about how to measure success, funding the ones whose
measure favours your product makes them more productive and more likely
to train the next generation, so the community drifts toward their method.

## Assumptions

- Agents are "(myopically) rational Bayesian agents" whose beliefs and
  choices are "unquestionably unaffected" by funding (p. 1012).
- Methodological bias: each agent's measured success rates are drawn
  around the true rates with variance σ², standing for different metrics
  of "success" (p. 1013).
- Productivity varies (50–100 trials a round, uniform) and sets influence
  and training.
- Turnover: with probability 0.02 a round one agent leaves; the newcomer
  takes another agent's method with probability proportional to that
  agent's productivity (a Moran process) (p. 1013, n. 5).
- Industry funds anyone whose measured success for the drug exceeds its
  true rate by more than T, adding F trials a round (p. 1015). No
  treatment is in fact better than the drug.

## Key results

- **Diversity alone** lowers reliability. Read from Figure 1, with no
  industry the share of agents on the superior act falls from about 95%
  at σ² = 0 to about 64% at σ² = 0.06.
- **Industry** lowers it further: at σ² = 0.04 about 64% with F = 20 and
  about 46% with F = 100. Without diversity there is no effect: "If there
  is no methodological diversity to begin with, then industrial selection
  does not occur" (p. 1015).
- **Two channels**: the funded agent influences peers more now and trains
  more newcomers later (p. 1015).
- **Independent funding** (Figure 2): with no NSF funding about 56%; a
  meritocratic NSF, which counts industry-funded trials, about 48–49%; a
  selective NSF, which does not, about 77–81%.
- **The case**: in the antiarrhythmic drug story, funded researchers' views
  did not change with funding, and industry "simply chose not to fund"
  those who held unfavourable views (p. 1011).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Industry funding can bias a community without corrupting any individual | moderate | an existence result in a simulation, plus one historical case |
| C2 | Methodological diversity, merit-based influence and selective funding are sufficient for the effect | moderate | the model, at a few parameter settings |
| C3 | Without methodological diversity the effect does not occur | moderate | the model |
| C4 | A merit-based independent funder worsens it, and one that discounts industry-funded work counteracts it | moderate | Figure 2, one parameter setting |
| C5 | The results hold across dense and sparse networks | weak | asserted in footnote 4, no data shown |
| C6 | Conflicts of interest were not the primary cause of the antiarrhythmic disaster | weak | the authors' reading of a historical account (Moore 1995) |

## Method

Agent-based simulation of 20-agent communities in Zollman's (2010) bandit
model: each round agents perform the action they think better as many
times as their productivity, update by Bayes's rule on their own and
neighbours' results, and turn over. Figure 1 uses pA = .5, pB = .45,
T = 0.03 and F = 0, 20, 100 across values of σ²; Figure 2 uses T = 0.04,
F = 20, an NSF productivity threshold of 75, and a σ² value missing from
the caption. The number of runs, run length or convergence criterion, the
network used for the figures, and the units of NSF funding are not
reported.

## Concepts

- **industrial selection** — bias produced because "it was because of the
  views researchers antecedently held that industry contracted them in
  the first place" (p. 1012), not because funding changed them.
- **methodological bias** — an agent's systematic deviation in measured
  success, from its choice of metric.
- **meritocratic and selective funding policies** — an independent funder
  counting, or not counting, industry-funded trials toward its
  productivity threshold.

## Connections

It builds on Zollman's model ([LIT-tmpkqfje](../literature.d/LIT-tmpkqfje.md), read in [NOTE-tmp8fh62](NOTE-tmp8fh62.md)) and
cites the authors' own 2015 paper ([LIT-tmpyzyje](../literature.d/LIT-tmpyzyje.md), unread). Its turnover
dynamic is borrowed from evolutionary biology, as the authors note.

- **The Zollman effect ([THEORY-tmpgo526](../theory.d/THEORY-tmpgo526.md)).** There, sparse communication
  protects a community's reliability when evidence is scarce. Here the
  qualitative result is said to hold on "both dense and sparse
  communication networks" (n. 4), so network structure offers no
  defence against industrial selection. That rests on a footnote, with no
  data.
- **Transient diversity ([THEORY-tmpqnfk9](../theory.d/THEORY-tmpqnfk9.md)).** That account treats
  diversity in what members pursue as what protects a learning group.
  Here diversity in how members measure success is what a funder exploits,
  and it lowers reliability even without a funder. The two are different
  kinds of diversity, of belief and of method. The contrast is the
  record's; the paper does not discuss it.
- **Longino ([THEORY-tmpv9j17](../theory.d/THEORY-tmpv9j17.md)).** In the case the paper describes, venues
  for criticism existed ("conferences with dissenters regularly
  occurred") and the FDA oversaw the process, yet the community was
  steered. Funding gave some researchers more influence through
  productivity, which bears on Longino's tempered equality of
  intellectual authority. The paper does not cite Longino; the reading is
  the record's.

## Bearing on the record

Source of [THEORY-tmpm45lu](../theory.d/THEORY-tmpm45lu.md). For the owner's essay:

- **§8.2** (Longino, Ostrom, epistemic networks). It shows that an
  epistemic network meeting the usual integrity safeguards can still be
  steered from outside, and that the remedy is at the community level:
  how an independent funder counts merit.
- **§6.4** (alien interests). The record reads industrial selection as an
  outside interest reshaping a community's practices without capturing
  any member, a case of the essay's institutional niche construction. The
  paper does not use those terms.

## Limitations

One historical case, read from a secondary history, and a small
simulation at a handful of parameter values, with the run count and the
network unreported and one figure caption incomplete. The robustness claim
for network structure is a footnote. The model's agents never change
their method, so the paper does not show what happens when researchers
adapt to funders.

## Open questions

Whether the effect survives agents who revise their methods in light of
evidence; how large methodological diversity is in real fields; whether a
selective funding policy is feasible, which the authors concede "might
face opposition".
