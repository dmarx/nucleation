---
number: 52
status: Skimmed
formerly:
- NOTE-tmpevggu
paper: LIT-056
title: 'Consciousness in AI: indicator properties'
version: 1
date: '2026-09-25'
summary: >-
  Assuming computational functionalism, the report derives a rubric of 14 "indicator properties" from leading neuroscientific theories of consciousness (RPT, GWT, computational HOTs, AST, PP, agency and embodiment). Applying it, the authors find that no current AI system is a strong candidate for consciousness, and that there are no obvious technical barriers to building systems that satisfy many of the indicators.
---

<!-- inactive-ok-file: LIT-056 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-052: Consciousness in AI: indicator properties

## Contribution

Whether current or near-term AI could be conscious is a question of growing scientific and public concern. The authors argue for a rigorous, empirically grounded approach: assess AI systems in detail against the best-supported neuroscientific theories of consciousness. They survey recurrent processing theory, global workspace theory, higher-order theories, predictive processing and attention schema theory, and derive computationally stated indicator properties from them. They use these to assess several recent AI systems and discuss how future systems might implement them. Their conclusion is that no current AI system is conscious, but that nothing obvious prevents building systems that satisfy the indicators.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Method (Executive Summary, §1.2): computational functionalism is adopted as a working hypothesis. The approach is "theory-heavy" rather than behavioural, because AI can be trained to mimic human behaviour. Credences depend on functional similarity, evidence for each theory, and credence in functionalism. Integrated information theory is excluded as incompatible with functionalism.
- Table 1 lists RPT-1/2, GWT-1–4, HOT-1–4, AST-1, PP-1 and AE-1/2 (agency, embodiment). Some are already met (RPT-1, algorithmic recurrence) and some arguably met (part of AE-1).
- Implementation (§3.1): most indicators could be built with standard ML methods, but combining them is untested. Prior systems have been built to implement GWT and AST.
- Case studies (§3.2): Transformer LLMs and Perceiver are assessed under GWT (attention heads as modules; whether a limited-capacity workspace and global broadcast exist). DeepMind's Adaptive Agent, a virtual-rodent controller and PaLM-E are used for agency and embodiment.
- Implications and recommendations (§4): the risks of both under- and over-attributing consciousness, and the relation between consciousness and capabilities. The authors recommend more research and urgent attention to moral and social risk, which the report itself does not address.

## Open questions

- The survey's flag: its subject is AI systems, so it may belong in the anthology. The skim suggests it is an assessment framework (a rubric), not a training practice or a model-behaviour theory. If the anthology has a topic for evaluating properties of AI systems, this is a candidate for it. Otherwise it is a reading-list note under consciousness.
- A deeper reading should check the §3.2 LLM analysis in detail, since that is the part that ages fastest. It should also check whether the later journal paper by an overlapping author group (reportedly in Trends in Cognitive Sciences, 2025; unverified) supersedes the report as the citable version.
