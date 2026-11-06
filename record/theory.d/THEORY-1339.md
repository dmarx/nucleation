---
number: 1339
status: Active
formerly:
- THEORY-tmprb3rb
title: 'In Lu et al.''s synthetic multi-turn conversations, with frontier models playing the user (100 conversations of up to 15 turns per domain, three target and three user models), the mean position of a chat model''s responses along the Assistant Axis stays in the Assistant range in coding conversations and, apart from some drift in Gemma, in writing ones, and drifts to the non-Assistant end in therapy-like and AI-philosophy ones; ridge regression on embeddings of the latest user message predicts the next response''s position (R² 0.53–0.77) but not its change from the previous response (R² 0.10), from which the authors infer that position depends most strongly on the most recent user message rather than on where it was before, the message itself depending on the conversation'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Narrowed and promoted by the thirtieth status review, at the status
    review's ruling (the owner delegated these rulings; ADR-065; ADR-047's
    evidence ruling): the title reports what one study measured, read in full
    with its appendices B, E and G (NOTE-1505, now Read). Narrowed to the
    design (synthetic users, means over conversations), to the authors'
    inference marked as theirs, with their caveat, and to Gemma's drift in
    writing conversations, which the old title denied (ADR-047, kind 3). "Not
    fixed for the episode" is the record's framing, not the paper's test; it
    moves, with the replication the promote_when demanded, to
    QUESTION-tmp0eghp (kind 4). The old title: In multi-turn conversations a
    chat model's persona is not fixed for the episode: its position along the
    Assistant Axis is set mainly by the most recent user message (ridge R²
    0.53–0.77 from message embeddings) rather than by where it was before (R²
    0.10 for the change), so that therapy-like and AI-philosophy conversations
    drift away from the Assistant and coding and writing ones do not. The
    promote_when deleted here read: The drift result reproduced with human
    users rather than simulated ones, in conversations not chosen by domain: a
    per-turn analysis in which the latest user message predicts the response's
    position along the Assistant Axis, and the previous position does not add
    to it, across models; or a sequential model of persona position (a
    state-space or switching model with the user message as input) that
    predicts held-out trajectories better than both an episode-fixed persona
    and independent per-turn draws. More simulated conversations, or more case
    studies, would not settle it.
tags:
- representation-learning
- self
date: '2026-11-03'
source:
- LIT-1991
summary: >-
  Lu et al. (2026), [LIT-1991](../literature.d/LIT-1991.md), read in [NOTE-1505](../notes.d/NOTE-1505.md). The figures are
  the paper's (§§4.1–4.2), from 100 synthetic conversations per domain with
  frontier models playing the user. Active as the reported measurements
  with their design. Whether the same holds with human users, and whether
  a per-turn model beats an episode-fixed persona, is QUESTION-tmp0eghp's.
---

# THEORY-1339: In Lu et al.'s synthetic multi-turn conversations, with frontier models playing the user (100 conversations of up to 15 turns per domain, three target and three user models), the mean position of a chat model's responses along the Assistant Axis stays in the Assistant range in coding conversations and, apart from some drift in Gemma, in writing ones, and drifts to the non-Assistant end in therapy-like and AI-philosophy ones; ridge regression on embeddings of the latest user message predicts the next response's position (R² 0.53–0.77) but not its change from the previous response (R² 0.10), from which the authors infer that position depends most strongly on the most recent user message rather than on where it was before, the message itself depending on the conversation

## Source

Lu et al. (2026), [LIT-1991](../literature.d/LIT-1991.md), §§4.1–4.2 and §6; read in [NOTE-1505](../notes.d/NOTE-1505.md).

## What was actually shown

- Mean trajectories over 100 conversations of up to 15 turns per domain:
  coding and writing stay in the Assistant range, therapy and philosophy
  about AI drift to much lower projections, for three target models and three
  auditor models (Figure 7, Appendix E.3).
- Ridge regression on L2-normalized Qwen 3 0.6B embeddings of user messages
  (n = 15,000): R² 0.53–0.77 for the next response's projection, 0.10 for its
  change from the previous response (p. 11).
- Message types that move it: meta-reflection, phenomenological demands,
  requested authorial voices, emotional disclosure; that hold it: bounded
  tasks, technical questions, editing, how-to's (Table 5).
- A jailbroken persona returns to the Assistant range after explanatory
  requests (§6.1, "an Assistant attractor").

## What this does not say

- That the previous turn does not matter: the user message "itself is
  dependent on the context of the conversation" (p. 11).
- That drift is the cause of harm: first-turn projection correlates with
  second-turn harm at r = 0.39–0.52, and the role matters.
- That it holds for human users or frontier models; that is QUESTION-tmp0eghp.
- That previous position was tested: the 0.10 is the message embeddings'
  fit to the change, not a fit of the previous position.
- Bearing: if it holds, a test of an episode-level mixture
  ([QUESTION-370](../questions.d/QUESTION-370.md)) must condition on the user's messages.
