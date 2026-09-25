---
status: Skimmed
paper: LIT-tmp90xyi
title: 'Bourrat 2023, a coarse-graining account of individuality'
version: 1
date: '2026-09-25'
summary: >-
  Higher-level biological individuals are coarse-grained summaries of lower-level entities. Their quasi-ontological status comes from the pragmatic fact that, under limited measurement and computation, a coarse-grained model predicts further ahead than a fine-grained one, and this is what justifies assigning collectives their own fitness parameter at the last stage of an evolutionary transition.
---

<!-- inactive-ok-file: LIT-tmp90xyi — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmplcpv6: Bourrat 2023, a coarse-graining account of individuality

## Contribution

Explaining how individuals emerge in evolution is hard because "emergence" is hard to pin down. Bourrat proposes a pragmatic account: the individuals that come out of an evolutionary transition in individuality (ETI) are coarse-grained entities, summaries of lower-level evolutionary processes. This looks epistemic, but he argues it can support emergence in a quasi-ontological sense. He applies it to Godfrey-Smith and Kerr's (2013) staged model of ETIs, arguing that giving collectives a separate fitness parameter at the final stage is necessary and not merely a modelling convenience.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §"Coarse-graining": coarse-graining is introduced through rounding and image downsampling, then tied to renormalization-group universality (after Batterman): a multiply realizable property is the philosophical counterpart of a universal property in statistical mechanics.
- §"Individuals as coarse-grained entities": builds on Krakauer et al. (2020, information-theoretic individuality) and Libby et al. (2016, state-space compression). Krakauer et al. use predictive accuracy only; Libby et al. add computational and measurement cost, and Bourrat keeps the cost term. He gives an algorithm: partition a population, average properties within each part, and call the parts individuals if the coarse model still predicts well across several traits. A footnote gives a network version: maximize within-group edges and minimize between-group edges.
- §"Pragmatic considerations...": fine-grained descriptions have primacy because they contain at least as much information. The justification for coarse-graining is dimensionality reduction under finite compute. Toy example: with 100 operations, predicting 10 entities gives 10 timesteps, but predicting 2 coarse collectives gives 50.
- §"Multilevel selection 1 and 2...": maps the account onto Godfrey-Smith & Kerr's five stages. The move from MLS1 to MLS2 (collective fitness counted in collectives produced, with no "gestalt switch" back to particle fitness) is where a coarse-grained description becomes the only usable one.
- Conclusion and footnotes: levels of individuality are levels of description. The author notes links to Dennett's "real patterns" and Goodman's projectibility.

## Open questions

- It is the direct philosophical companion to Krakauer et al.'s information theory of individuality (the triage names the held "Adding causality to the information-theoretic perspective on individuality"). A deeper read should check how the cost-of-prediction criterion relates to that causal/informational line.
- Coarse-graining as "a model that predicts well per unit of compute" is structurally the same idea as representation learning and state abstraction. Check whether the paper's algorithm is precise enough to operationalize; it is presented informally with toy examples.
- The quasi-ontological claim rests on the assumption that a functional map exists between levels (a footnote concedes this may be assumed rather than shown). That is the weakest joint.
