---
status: Proposed
promote_when: >-
  A sample of deployed conversations, coded blind for the referent of the
  agent's "I", that finds uses which require the model (beyond the
  conversation) and uses which require the conversation (within it), with
  the choice predicted by context; and self-descriptions elicited under
  regeneration, the role-play paper's own method, showing which conception
  of itself a fine-tuned assistant character enacts and how stable it is
  across conversations. It would be refuted if real uses fixed one referent
  across contexts, for instance the per-conversation instance, as
  Goldstein and Lederman's account (LIT-206) predicts, or if products with
  memory across conversations, which both papers set aside, brought back a
  single persisting referent. The papers' invented dialogues and the
  twenty-questions illustration cannot settle it: they are described, not
  sampled.
title: "What a chat agent's 'I' refers to is fixed by the context of use, not by the system: the agent role-plays characters that carry the self-conception the corpus and the conversation give them, and its uses of 'I' can pick out the model, present in many simultaneous instances, or the single conversation, none of them the self by nature"
version: 1
tags:
- self
- individuation
- philosophy-of-language
date: '2026-10-16'
source:
- LIT-466
- LIT-460
summary: >-
  Shanahan (2025), [LIT-466](../literature.d/LIT-466.md), read in [NOTE-376](../notes.d/NOTE-376.md), with Shanahan, McDonell and
  Reynolds (2023), [LIT-460](../literature.d/LIT-460.md), read for the self in [NOTE-370](../notes.d/NOTE-370.md). The candidate
  sites of an LLM's "I", and the fact that a conversation-bound self is
  literally a transcript and a program, are solid. That both the model and
  the conversation are legitimate referents rests on two invented usages.
  It does not say that there is "no-one at home" or that no candidate is a
  self, which the papers assert without a criterion, and its subject is a
  2024-vintage chat agent without tools or memory across conversations.
supports:
- CLAIM-029
---
<!-- inactive-ok-file: THEORY-tmp60gbs THEORY-tmp9v34q THEORY-tmpv3v56 THEORY-tmpyw2hy — Proposed; filed in the same batch and named as a rival, a parallel or a contrast, not leaned on -->
<!-- inactive-ok-file: THEORY-023 THEORY-173 CLAIM-029 — Proposed; named as a neighbouring account, nothing here rests on its being settled -->

# THEORY-tmpb08ha: What a chat agent's 'I' refers to is fixed by the context of use, not by the system: the agent role-plays characters that carry the self-conception the corpus and the conversation give them, and its uses of 'I' can pick out the model, present in many simultaneous instances, or the single conversation, none of them the self by nature

## Source

Shanahan (2025), "Palatable Conceptions of Disembodied Being",
arXiv:2503.16348 (v3), [LIT-466](../literature.d/LIT-466.md), read in [NOTE-376](../notes.d/NOTE-376.md). Shanahan, McDonell and
Reynolds (2023), "Role play with large language models", *Nature* 623:
493–498, [LIT-460](../literature.d/LIT-460.md), read for the self in [NOTE-370](../notes.d/NOTE-370.md), which also records where
the arXiv version differs.

## What was actually shown

**Role play ([LIT-460](../literature.d/LIT-460.md)).** A dialogue agent can be seen as playing one
character, or as "a superposition of simulacra within a multiverse of
possible characters". The simulator, the base model with sampling and an
interface, "contains multitudes"; simulacra "only come into being when the
simulator is run". A character that says "I" carries the self-conception
the corpus and the conversation give it: each simulacrum has "its own
theory of selfhood consistent with the dialogue prompt and the
conversation", and the superposition narrows as the conversation rules
theories out (pp. 497–498). Candidate sites a character might protect are
the hardware and, on a "substrate neutral" theory, the computational
process; many concurrent instances make "the picture more complicated".
[NOTE-370](../notes.d/NOTE-370.md) rates the framing moderate as a description.

**Candidate referents ([LIT-466](../literature.d/LIT-466.md) §5.1).** When an LLM says "I", the referent
might be the model (architecture plus weights), the deployed process, all
its concurrent instances, one instance, or the model plus one
conversation's suspended state.

**Two conceptions (§5.2).** "I am still learning" must refer beyond the
conversation; "I did not say that", of another window, must refer within
one. So one self is the model, "manifest as multiple, simultaneous
instances", and the other is tied to a conversation, which "flickers into
being with each user interaction, and lies dormant in the gaps". "We (the
users and the LLMs) can legitimately slip from one usage to another." The
two usages are invented, not sampled.

**What a conversation self is (§5.3).** It "is literally the combination of
a piece of text (the conversation transcript) and a computer program", so
it can be "arbitrarily edited, copied, and merged" and continued by a
different model. Instances "have no access to each other's memories or
experiences". [NOTE-376](../notes.d/NOTE-376.md) rates this strong as a description of how chat
systems work.

**What could have come out otherwise.** Usage could have fixed one referent,
so that every use of "I" read as the instance, or as the model. The two
invented examples are offered to show it does not; whether real usage
behaves so is untested.

## What this does not say

- **That there is "no-one at home".** The role-play paper says so of
  self-preservation talk, and that the simulator has no beliefs, goals or
  agency "not even simulated versions". The reading rates both weak:
  asserted from the framing, with no criterion for having an attitude.
  Birch ([LIT-111](../literature.d/LIT-111.md)) replies that role play "does not rule out a conscious
  'actor'". This account is about reference, and it does not bear on
  [THEORY-023](THEORY-023.md).
- **That no candidate is a self.** Shanahan's no-self conclusion, that
  "there is nothing enduring, essential, or substantial" to underpin
  selfhood for such a system (§6.1), is asserted as the upshot without
  testing each candidate against a criterion. His extension to human
  selves (§6.2) is an assertion, and the 2025 paper says it aims at
  "poetic truth", not literal truth (§3).
- **What makes such an agent the same over time.** The role-play paper calls
  the criteria "far from clear" and cites one work on personal identity,
  Perry's anthology. Neither paper adopts a criterion.
- **Anything about agents with tools or memory across conversations.** The
  2025 paper restricts itself to an early-2024 chat agent (fn. 1). Memory
  across conversations could restore a single persisting referent or add a
  third conception.
- **Which conception a deployed assistant in fact enacts.** That is
  testable by regeneration and is not done.
- **That selfhood is agency.** The papers' sites of a self are the bearers
  Goldstein and Lederman make agents; [ADR-024](../decisions.d/ADR-024.md) keeps the two apart, and
  picking out the same bearer is not the claim that self is agent.

## Connections

- **The rival view, not filed as a THEORY.** Goldstein and Lederman
  ([LIT-206](../literature.d/LIT-206.md), [NOTE-138](../notes.d/NOTE-138.md)) make the per-conversation instance the bearer of
  beliefs and desires and find no work for a model agent. Shanahan's
  conversation self picks out their instance; his model self is the bearer
  they reject. They also argue that role play is incompatible with
  attributing belief, and [NOTE-370](../notes.d/NOTE-370.md) finds that version in the published text.
- **Floridi** ([THEORY-tmpv3v56](THEORY-tmpv3v56.md)). Letting context fix which "I" is meant is
  the level-of-abstraction move, as [NOTE-376](../notes.d/NOTE-376.md) observes; it is not cited.
- **Dennett** ([THEORY-tmpyw2hy](THEORY-tmpyw2hy.md)). A simulacrum has a fictional character's
  indeterminacy; Dennett would count a coherent one a self, and the
  role-play paper counts it no one. Dennett's "Where Am I?" ([LIT-405](../literature.d/LIT-405.md)) asks
  §5.1's question of a human split across brain, body and duplicate.
- **Branching and counting.** The §5.3 operations, copy, merge, edit and
  restore, are the cases of Parfit ([THEORY-tmp60gbs](THEORY-tmp60gbs.md)) and Lewis
  ([THEORY-tmp9v34q](THEORY-tmp9v34q.md)) made routine. Shanahan uses them to show that
  intuitions about integrity fail, not to decide what matters.
- **The record's own claim.** [CLAIM-029](../claims.d/CLAIM-029.md) holds that a language model's
  response to a context is functionally a parameterized pragmatic frame,
  and grounds on [LIT-460](../literature.d/LIT-460.md) and on this account, for the role-play
  framing stated above.
- **[THEORY-173](THEORY-173.md)** treats large models as a cultural technology rather than
  agents and calls the simulator account compatible from the other side.
