---
status: Active
status_note: 'read 2026-10-23 ([NOTE-tmpajajy](../notes.d/NOTE-tmpajajy.md)): in full, from the published version on a University of Kentucky course reading list, checked against the authors'' manuscript on Gratch''s USC page. Worth reading as the worked computational case of appraisal as a continuous process over the agent''s causal interpretation, with an explicit arbitration rule. Appraisal is a single, fast, parallel mapping from that interpretation to appraisal variables. Its dynamics come from the slower perception, inference and action that change the interpretation, and from coping, which alters beliefs, desires and intentions and so drives reappraisal. Appraisal frames, one per proposition, compete for the coping response. The winner is the most recently accessed frame with the highest mood-adjusted intensity, and intensity is a decision-theoretic product of likelihood and utility. That is arbitration on a common currency among concerns, not a negotiation among perspectives.'
title: 'EMA: A process model of appraisal dynamics'
version: 1
history:
- version: 1
  date: '2026-10-23'
  note: >-
    Read in full: §§1–5 of the published version (Cognitive Systems
    Research 10(1):70–90), from the PDF on Stephen Ware's University of
    Kentucky reading list (cs.uky.edu/~sgware/reading). The authors'
    manuscript, posted on Jonathan Gratch's USC ICT page, was also
    downloaded and every quotation was found in it as well. OpenAlex
    lists the article as closed (Elsevier). Details checked against
    Crossref (DOI 10.1016/j.cogsys.2008.03.005): Stacy C. Marsella and
    Jonathan Gratch, Cognitive Systems Research 10(1):70–90, March 2009
    (online 5 July 2008, per the article). `published:` is the first of
    the issue month. Page numbers are the journal's. All quotations were
    checked by script against the extracted text. References not read.
tags:
- emotion-and-affect
- cognition
- agency
date: '2026-10-23'
published: '2009-03-01'
doi: '10.1016/j.cogsys.2008.03.005'
url: 'https://people.ict.usc.edu/gratch/public_html/papers/COGSYS-RS-EMOTION-2008-6.pdf'
first_author: 'Marsella'
keywords:
- 'EMA'
- 'appraisal dynamics'
- 'causal interpretation'
- 'appraisal frame'
- 'coping'
- 'reappraisal'
- 'mood'
- 'computational model of emotion'
implementations: []
summary: >-
  Marsella & Gratch (2009), Cognitive Systems Research 10(1):70–90. EMA
  (EMotion and Adaptation), after Smith and Lazarus. Appraisal is one
  fast, parallel, automatic process over the agent's causal
  interpretation, a decision-theoretic plan representation of its
  beliefs, desires, intentions and plans. Emotional dynamics come from
  the time course of the perception, inference and action that change
  that interpretation, so no multi-level appraisal is needed. Each
  proposition gets an appraisal frame. Frames compete for coping, and
  the most recently accessed one with the highest mood-adjusted intensity
  wins. Coping changes the world or the agent's beliefs, desires and
  intentions, which drives reappraisal. Illustrated with an actor's
  reaction to a pigeon.
---
<!-- inactive-ok-file: CLAIM-tmpz8lli TERM-tmp8gbrt — Proposed; the proposal this work bears on -->
<!-- inactive-ok-file: LIT-550 — Unavailable, unread; Lazarus's Emotion and Adaptation, which EMA is named after and follows -->

# LIT-tmpd2jcs: EMA: A process model of appraisal dynamics

Stacy C. Marsella & Jonathan Gratch (2009), *Cognitive Systems Research*
10(1):70–90 — DOI-10.1016/j.cogsys.2008.03.005

## Key takeaways

- **One appraisal process, many inference processes** (pp. 71–74). The
  authors reject multi-level appraisal (Scherer's sequential checks,
  Smith and Kirby's two processes) as confusing appraisal with inference.
  "We distinguish between the construction of this representation, which
  may be slow and sequential, and its appraisal, which is fast, parallel
  and automatic" (p. 71).
- **A cycle of appraisal, coping and reappraisal** (p. 76), following
  Lazarus ([LIT-550](LIT-550.md)): "we assume a cyclical relationship between
  appraisal, coping and re-appraisal." Inference changes the
  interpretation, and "they indirectly trigger automatic reappraisal"
  (p. 76).
- **The causal interpretation** (pp. 77–79). A blackboard holding the
  agent's working memory, built on decision-theoretic planning: states,
  actions, causal links, beliefs, intentions, probabilities and
  utilities. "Utilities represent the preference agents' have for
  states" (p. 79). Appraisals "do not change the causal interpretation
  but provide a continuously updated "affective summary" of its contents"
  (p. 80).
- **Appraisal variables** (p. 80). Relevance, perspective, desirability,
  likelihood, expectedness, causal attribution, controllability and
  changeability, computed per proposition. "Perspective" is whose
  utilities are used, the agent's own or another agent's as the agent
  represents them; the paper uses only the agent's own.
- **Arbitration** (pp. 81–82). EMA "maintains multiple appraisal frames
  (one for each proposition in the causal interpretation) each of which
  are labeled with a specific emotion type and intensity, and each
  competing to determine the agent's coping response" (p. 81). The winner
  is "the most recently accessed appraisal frame with the highest
  mood-adjusted intensity" (p. 81). Mood, an aggregate of frames by
  emotion label, "bleeds over" into appraisal (p. 81). Intensity comes
  from "a decision-theoretic calculus" of likelihood times utility
  (p. 84).
- **Coping** (pp. 82–83). Strategies that work "in the reverse direction
  of the appraisal that motivates them" (p. 82) act on attention, belief
  (shift responsibility, wishful thinking), desire (distancing, positive
  reinterpretation) and intention (planning, procrastination,
  resignation, avoidance). "EMA proposes strategies in parallel but adopts
  them sequentially. A set of preferences resolves ties" (p. 83).
- **Limits** (pp. 87–88). Some predictions miss, such as anger at the
  bird's injury where the video suggests concern for it. Time courses
  are "free parameters that allow us considerable latitude in fitting our
  model to data" (p. 88).

## Standing in the record

Filed on 2026-10-23 for the record's proposal that appraisal is the
negotiation among an organization's perspectives ([CLAIM-tmpz8lli](../claims.d/CLAIM-tmpz8lli.md),
[TERM-tmp8gbrt](../terms.d/TERM-tmp8gbrt.md)). EMA is the clearest working model of appraisal as a
continuous process with explicit arbitration among concurrent
evaluations. Its arbitration is winner-take-all on one scalar,
mood-adjusted intensity, so it presupposes the common currency that the
proposal treats as an achievement. Its competitors are evaluations of
propositions, not rankings held by perspectives. Coping that lowers a
desire's utility is the one place where the ordering itself is revised.
The bearing is set out in [NOTE-tmpajajy](../notes.d/NOTE-tmpajajy.md).

Not flagged for the Anthology of the SOTA: EMA is an architecture for
virtual humans and carries no instruction for machine-learning practice.
Whether the anthology wants it as a computational model of emotion for
agents is the anthology's question.
