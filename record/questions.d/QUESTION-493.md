---
number: 493
status: Open
formerly:
- QUESTION-tmpo8ddc
title: 'What does it take for a learning system to know something, as distinct from storing the information, believing it, or producing the right answer, and where in a system that samples, adapts at test time, uses a verifier or calls a tool does the knowing sit?'
version: 1
tags:
- epistemology
- representation-learning
- cognition
date: '2026-11-19'
line:
- learned-structure
summary: >-
  The owner's, at U33 of the exchange "Topological protection explained"
  (2026-11-19): "so what does it mean for a learning system to 'know'
  something?" The owner had set the belief and knowledge distinction aside
  in the exchange of 2026-10-24 ([TERM-079](../terms.d/TERM-079.md) says "Nothing here defines
  knowledge", and the curation entry of that date left Gettier
  unregistered for that reason). U33 reopens it. A73 proposed an
  operational account, Proposed here as candidate answers: "Knowledge is
  a truth-connected epistemic capacity sustained by an agent's or
  organization's structure". The record holds what a system has against
  what it can deploy ([CLAIM-296](../claims.d/CLAIM-296.md)), grounding as a relation ([CLAIM-413](../claims.d/CLAIM-413.md)) and
  coverage against delivered success ([CLAIM-697](../claims.d/CLAIM-697.md)).
---
<!-- inactive-ok-file: CLAIM-519 CLAIM-697 CLAIM-754 TERM-079 TERM-131 THEORY-1737 THEORY-438 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CASE-408 CASE-416 CASE-399 CASE-413 CASE-414 CASE-403 CLAIM-1142 CLAIM-1086 CLAIM-1028 CLAIM-1100 CLAIM-1092 CLAIM-1059 CLAIM-1109 — Proposed; filed by the lead run of 2026-11-23 -->

# QUESTION-493: What does it take for a learning system to know something, as distinct from storing the information, believing it, or producing the right answer, and where in a system that samples, adapts at test time, uses a verifier or calls a tool does the knowing sit?

## Why it is a question

The owner, at U33 of the exchange "Topological protection explained"
(https://chatgpt.com/share/6afe6dd0-9d78-83ea-9782-f55680665dcf):

> so what does it mean for a learning system to "know" something?

[TERM-079](../terms.d/TERM-079.md) defines a belief of a process and explicitly leaves knowledge
undefined, after the owner set the distinction aside on 2026-10-24. The
exchange had just characterized learning as a change in a costed
repertoire ([CLAIM-754](../claims.d/CLAIM-754.md), [TERM-131](../terms.d/TERM-131.md)), which raises the question of
which changes are knowledge.

## A73's candidate answer (A's; Proposed)

- **Four things kept apart**: stored information, belief, a correct
  answer, knowledge. "learning changes a system's organization, but not
  every change in organization constitutes knowledge."
- **Criteria**: truth, counterfactual reliability over a declared family
  of cases, and grounding, "knowledge must be connected appropriately to
  what makes it correct"; responsiveness to correction as a diagnostic,
  not a condition.
- **Possession, accessibility, manifestation**: a capacity costly to
  exercise is still possessed; "a fact buried in a gigantic database and
  inaccessible to every permitted retrieval procedure should not
  automatically count". This is [CLAIM-296](../claims.d/CLAIM-296.md)'s has-against-deploys applied to
  knowing.
- **Where it sits**: one correct answer in many samples is generative
  reach, not knowledge, [CLAIM-697](../claims.d/CLAIM-697.md)'s coverage against delivery; knowledge
  may belong to the composite of generator and verifier or of model and
  tool.
- **Understanding as developmental value**: a memorized table f(2)=4,
  f(3)=9, f(4)=16 and the rule x² agree now and part when the target
  becomes x²+c, which the rule-learner acquires cheaply. [CLAIM-519](../claims.d/CLAIM-519.md) says why
  only change tells them apart.
- **Four tests**: reliability over a declared family; intervention on
  spurious cues; a changed fact with valid corrective evidence;
  intervention on the supposed mechanism. A's caution: "we should not
  confuse the ability to provide a plausible verbal explanation with
  evidence that the explanation describes the computation".

## What the record has that A73 did not use

[THEORY-1024](../theory.d/THEORY-1024.md): where causal tracing localizes a fact in a language model
barely predicts where editing it succeeds, which bears directly on the
fourth test. [THEORY-1737](../theory.d/THEORY-1737.md): memory agents fail to act on the latest of
conflicting facts, the third test. [THEORY-438](../theory.d/THEORY-438.md): understanding as stable
tracking under structure-preserving perturbation. A73 also called
[CLAIM-519](../claims.d/CLAIM-519.md) Active; it is Proposed.

## What would answer it

A definition of knowledge of a process, as a sibling of [TERM-079](../terms.d/TERM-079.md), whose
tests could be run on a model and which says whether knowing belongs to
the weights or to the declared system.

## Note of 2026-11-19: follow-up turns of "Topological protection explained"
ChatGPT (A84) ranks this question foundational and the first to pursue, as "what constitutes learning, knowledge, and understanding in a historically organized system". Its candidate: "Could knowledge be characterized by the organization of an epistemic capacity, rather than by a particular representation or isolated judgment?", with the questions "Can knowledge be latent but practically inaccessible? Can knowing reside in a distributed system? When does reliable success cease to be accidental? Does understanding necessarily entail greater future learnability?" A next advance without an experiment: "Construct cases that distinguish reliable performance from non-accidental epistemic competence".

## Note of 2026-11-19: Brown and colleagues, read
Background ([NOTE-2160](../notes.d/NOTE-2160.md)): Brown and colleagues read closed-book answers as knowledge absorbed in the parameters and few-shot gains on those tasks as adapting to format, so zero-shot performance understates what the system has: possession apart from accessibility, an analogy for the question's distinction, not evidence.

## Note of 2026-11-23: cases that separate the four things, and understanding

[LEAD-001](../leads.d/LEAD-001.md) filed nine cases and their verdicts against A73's candidate
answer. [CLAIM-1142](../claims.d/CLAIM-1142.md) collects eight separations among stored
information, belief, correct output, knowledge and understanding. The
candidate holds on every case, with two findings:

- **Reliability over a family as declared is not enough.** A classifier
  reading a watermark ([CASE-416](../cases.d/CASE-416.md)) and a model whose stale source was
  made true again by a reappointment ([CASE-399](../cases.d/CASE-399.md)) are reliable there
  and do not know. A73's grounding criterion, and its second and third
  tests, catch both. Whether grounding is then a further condition or
  reliability over a family closed under interventions on the truthmaker
  is filed as alternatives: [CLAIM-1086](../claims.d/CLAIM-1086.md) (the assistant's lean) and
  [CLAIM-1028](../claims.d/CLAIM-1028.md).
- **Possession and where it sits.** A fact a probe decodes and the model
  never uses ([CASE-408](../cases.d/CASE-408.md)) is stored, not known; one the model uses
  under one cue ([CASE-413](../cases.d/CASE-413.md)) is known relative to the declared
  procedures and budget ([CLAIM-1100](../claims.d/CLAIM-1100.md)). A generator filtered by an exact
  verifier ([CASE-414](../cases.d/CASE-414.md)) knows as a composite under a budget, and
  neither part does ([CLAIM-1109](../claims.d/CLAIM-1109.md)).

A84's question whether understanding "necessarily entails greater future
learnability" turns on a frozen exact rule ([CASE-403](../cases.d/CASE-403.md)): on
[CLAIM-1092](../claims.d/CLAIM-1092.md) (the assistant's lean, understanding as stable tracking,
[THEORY-438](../theory.d/THEORY-438.md)) no; on [CLAIM-1059](../claims.d/CLAIM-1059.md) (understanding as developmental value,
A73) yes. On every learner the two agree. No status change.

## Note of 2026-11-27: shortcut learning

<!-- inactive-ok-block: CLAIM-1406 CLAIM-1372 — new; filed when the owner asked for the record's account of shortcut learning -->

The owner asked for the record's account of shortcut learning, noting that the record does not use the term. It is this question's, in its own words. [CASE-416](../cases.d/CASE-416.md), the watermark-reading classifier, is the canonical shortcut. [CLAIM-1086](../claims.d/CLAIM-1086.md) and [CLAIM-1028](../claims.d/CLAIM-1028.md) share its diagnosis, an intervention that separates the cue from what makes the answer true. [CLAIM-1406](../claims.d/CLAIM-1406.md) joins that definition to the order in which networks learn ([THEORY-279](../theory.d/THEORY-279.md), [THEORY-759](../theory.d/THEORY-759.md)) to say why shortcuts arise, and [CLAIM-1372](../claims.d/CLAIM-1372.md) reads sycophancy as one. The reading is [LEAD-286](../leads.d/LEAD-286.md).

