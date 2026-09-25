---
status: Skimmed
paper: LIT-tmp4zlq9
title: 'The relativity of causal knowledge'
version: 1
date: '2026-09-25'
summary: >-
  The paper argues that SCMs are imperfect, subjective models embedded in a network of subjects. It formalizes "relative causal knowledge": SCMs form a functor category whose observational and interventional measures are convex spaces, and a network sheaf and cosheaf over these spaces carries causal knowledge between subjects consistently with interventions.
---

<!-- inactive-ok-file: LIT-tmp4zlq9 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmpe99kk: The relativity of causal knowledge

## Contribution

Motivated by the limits of purely predictive AI and by Grothendieck's relational turn in mathematics, the authors propose that structural causal models are imperfect, subjective representations that exist inside networks of relationships. Using category theory, they arrange SCMs into a functor category and show that observational and interventional probability measures form convex structures, so that non-intervened SCMs can be encoded as convex spaces of measures. Using sheaf theory, they then build a network sheaf and cosheaf of causal knowledge. These transfer knowledge across the network while respecting interventional consistency and each subject's perspective, which yields a formal definition of relative causal knowledge.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Motivation (§1): the authors cite Pearl's ladder of causation and Richens & Everitt's result that robustness to distribution shift requires an approximate causal model. They start "where Richens and Everitt end", by formalizing a subject's dependence on its relationships. Philosophical anchors are manipulability theories, causal pluralism and actor-network theory. "Relativity" is explicitly distinguished from relativism.
- Examples of "subjects": collaborating agentic-AI systems, but also resolutions of study, pollution sensors and bank trading books.
- Construction (§2–4): SCMs, interventions and α-abstractions form a category, and the measures form objects of a category of convex spaces (CS_prob). Network sheaves (first-order cellular sheaves) and cosheaves then move knowledge along edges via restriction and extension maps that encode "perspective".
- Discussion (§5): the programme is openly unfinished. There is no learning theory yet ((co)sheaf inference and discovery). No cohomology exists because CS_prob is not Abelian. A Hodge-like theory is needed for diffusion and spectral tools.
- There are no experiments. The paper is a formal position and definitions paper.

## Open questions

- Anthology fit (the survey's question): it is not `analysis-and-evaluation`. It proposes no evaluation method and no practice, and its AI motivation is framing for a mathematical definition. It belongs in the reading list under probabilistic-modeling (causal models), with mathematics as secondary.
- A deeper reading should check §2–3 for what the convexity result actually buys, and whether the sheaf construction does anything that multi-agent causal-abstraction work cannot already do.
