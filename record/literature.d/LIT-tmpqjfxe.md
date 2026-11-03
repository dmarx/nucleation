---
status: Active
status_note: >-
  read 2026-11-03 ([NOTE-tmpagiju](../notes.d/NOTE-tmpagiju.md), Skimmed: main text in full,
  appendices not read), from arXiv v1; worth reading for the geometry
  of persona space in three open-weight models, the Assistant at one
  end of a pre-existing first axis, and for the finding that within a
  conversation the persona's position follows the latest user message,
  which bears on any episode-level model of personas ([CLAIM-tmphbnqm](../claims.d/CLAIM-tmphbnqm.md),
  [QUESTION-tmpildq9](../questions.d/QUESTION-tmpildq9.md)).
title: 'The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models'
version: 2
history:
- version: 1
  date: '2026-11-02'
  note: >-
    Filed, not read. Citation checked against the arXiv API on 2026-11-02
    (v1 submitted 2026-01-15); the PMLR page also resolves. The summary
    says why it is here, not what it shows.
- version: 2
  date: '2026-11-03'
  note: >-
    Read from arXiv:2601.10387v1 (15 January 2026): §§1–9 in full;
    appendices A–G not read, so the NOTE is Skimmed (NOTE-tmpagiju).
    The PMLR version was not compared. Status set from the reading:
    Active. The summary is replaced by one from the text. The
    registration's summary held. Two THEORYs are filed from it
    (THEORY-tmple55n Active, THEORY-tmprb3rb Proposed).
tags:
- representation-learning
- self
- anthology-candidate
date: '2026-11-02'
published: '2026-01-15'
arxiv: '2601.10387'
first_author: 'Lu'
keywords:
- 'assistant axis'
- 'default persona'
- 'persona drift'
implementations: []
summary: >-
  Lu, Gallagher, Michala, Fish and Lindsey (2026), arXiv:2601.10387.
  Activation vectors for 275 prompted roles in Gemma 2 27B, Qwen 3 32B
  and Llama 3.3 70B span a low-dimensional persona space whose first
  component, shared across models, runs from fantastical roles to
  Assistant-like ones, with the default Assistant at its extreme; the
  Assistant Axis, the default minus the role mean, aligns with it and
  is largely present in base models. Steering along it modulates
  role-taking and persona-based jailbreaks. In synthetic multi-turn
  conversations the persona's position follows the latest user
  message, drifting away in therapy-like and AI-philosophy talk;
  clamping the projection (activation capping) cuts harmful responses
  to persona jailbreaks by about 60% without measured capability loss.
---
<!-- inactive-ok-file: NOTE-tmpagiju — Proposed, Open, Deferred, Unfetched, Unavailable or new; cited as open -->
<!-- inactive-ok-file: THEORY-tmprb3rb — Proposed or Open; a THEORY filed from this reading and the question it bears on, cited as open -->

# LIT-tmpqjfxe: The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models

Lu, C., Gallagher, J., Michala, J., Fish, K., Lindsey, J. (2026). The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models. *arXiv preprint; PMLR v306*. arXiv:2601.10387.

Read on 2026-11-03, main text in full ([NOTE-tmpagiju](../notes.d/NOTE-tmpagiju.md), Skimmed; [THEORY-tmple55n](../theory.d/THEORY-tmple55n.md), [THEORY-tmprb3rb](../theory.d/THEORY-tmprb3rb.md)).

## Key takeaways

- Persona space is low-dimensional (4–19 PCs for 70%); PC1 loadings agree
  across models (r > 0.92), with the Assistant at one end.
- The axis is largely inherited from pre-training; post-training adds its
  AI-assistant associations.
- Within a conversation the position is predicted by the latest user
  message (R² 0.53–0.77), not by the previous position (R² 0.10).
- Activation capping is practice, the anthology's.

## Standing in the record

A direction along which the default Assistant persona is situated and stabilized; bears on what post-training installs ([TERM-072](../terms.d/TERM-072.md)'s note of 2026-10-22, [NOTE-1069](../notes.d/NOTE-1069.md)).
