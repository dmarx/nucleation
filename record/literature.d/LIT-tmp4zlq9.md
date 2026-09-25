---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-25; not read in full
title: 'The Relativity of Causal Knowledge'
version: 1
tags:
- probabilistic-modeling
- mathematics
date: '2026-09-25'
published: '2025-03-13'
arxiv: '2503.11718'
first_author: 'D''Acunto'
keywords:
- 'structural causal models'
- 'category theory'
- 'sheaf theory'
- 'causal abstraction'
- 'relative causal knowledge'
implementations: []
summary: >-
  D'Acunto et al. (2025), [ARXIV-2503.11718](https://arxiv.org/abs/2503.11718). The paper argues that SCMs are imperfect, subjective models embedded in a network of subjects. It formalizes "relative causal knowledge": SCMs form a functor category whose observational and interventional measures are convex spaces, and a network sheaf and cosheaf over these spaces carries causal knowledge between subjects consistently with interventions.
---

# LIT-tmp4zlq9: The Relativity of Causal Knowledge

Gabriele D'Acunto, Claudio Battiloro (2025), *Conference on Uncertainty in Artificial Intelligence (UAI 2025); arXiv preprint* — [ARXIV-2503.11718](https://arxiv.org/abs/2503.11718)

## Key takeaways

- The paper argues that SCMs are imperfect, subjective models embedded in a network of subjects. It formalizes "relative causal knowledge": SCMs form a functor category whose observational and interventional measures are convex spaces, and a network sheaf and cosheaf over these spaces carries causal knowledge between subjects consistently with interventions.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

Motivated by the limits of purely predictive AI and by Grothendieck's relational turn in mathematics, the authors propose that structural causal models are imperfect, subjective representations that exist inside networks of relationships. Using category theory, they arrange SCMs into a functor category and show that observational and interventional probability measures form convex structures, so that non-intervened SCMs can be encoded as convex spaces of measures. Using sheaf theory, they then build a network sheaf and cosheaf of causal knowledge. These transfer knowledge across the network while respecting interventional consistency and each subject's perspective, which yields a formal definition of relative causal knowledge.

## Standing in the record

Filed from the survey of 2026-09-25 of work the anthology set aside as out of scope (tier B): 290 seconds of active reading over 5 sessions in the papers-feed tracker. `Deferred` because nobody has read it closely here yet, not on merit.

**Priority for a deeper reading: medium — It is a boundary item the survey asked to "read before choosing a record". The skim settles that question: reading list, not anthology. The formal core (§2–4) is still unread. Moderate owner time (t=290 s over 5 sessions).**

What a deeper reading should check:

- Anthology fit (the survey's question): it is not `analysis-and-evaluation`. It proposes no evaluation method and no practice, and its AI motivation is framing for a mathematical definition. It belongs in the reading list under probabilistic-modeling (causal models), with mathematics as secondary.
- A deeper reading should check §2–3 for what the convexity result actually buys, and whether the sheaf construction does anything that multi-agent causal-abstraction work cannot already do.

Access when seeded: I read the arXiv abstract page (v1 13 Mar 2025, v2 30 May 2025; comment "Accepted at UAI 2025. 19 pages, 2 figures") and the full v2 PDF. I read §1 (Introduction, motivation and related work), §5 (Discussion) and §6 (Conclusion), and took §2–4 by headings (Categorical SCM; Encoding causal knowledge; The network sheaf and cosheaf). I did not check the PMLR proceedings entry.
