---
status: Open
title: 'When an organization that must act acceptably in every circumstance it cannot yet exclude learns which circumstance holds only from what its own committing actions reveal, how much must it observe before it commits, and is what only commitment would reveal lost to it?'
version: 1
tags:
- control-theory
- agency
- information-theory
date: '2026-11-14'
line:
- will-organization
summary: >-
  Raised by the reading review of 2026-11-14 (by topic, part C,
  control-theory). CLAIM-535 gives the one-step condition for a policy
  acceptable in every circumstance an organization cannot tell apart,
  and CLAIM-572 the cheapest split of one budget between observing and
  acting; both exclude the case where acting is itself observing. Two
  readings in force that no line used state that case for controllers: a
  policy that must stay safe under every model it has not ruled out
  cannot use the evidence its committing action produces, and forfeits
  about ½e^{−β} of the value only commitment reaches when what it can
  learn beforehand is bounded by β (THEORY-1254); where a conservative
  experiment is safe under every plausible model and repeatable, acting
  on the lower end of an anytime confidence sequence is safe and
  approaches the oracle, while certainty equivalence is unsafe with
  probability ½ however much data it has (THEORY-1256). The wording is
  the assistant's; adopting it is the owner's call.
---

# QUESTION-tmppyelk: When an organization that must act acceptably in every circumstance it cannot yet exclude learns which circumstance holds only from what its own committing actions reveal, how much must it observe before it commits, and is what only commitment would reveal lost to it?

## Why it is a question

CLAIM-535 holds that an organization acting on what it observes has a
policy acceptable in every circumstance exactly when, for each
observation, the circumstances it cannot tell apart share an acceptable
action. It is one step: it says nothing about learning, and it sets
aside "active sensing and dual control". CLAIM-572 prices observation
against response from one budget and excludes the case where "an action
also observes". In organizations that case is common: a commitment (a
launch, a hire, a reorganization) is often the only way to find out
which circumstance holds.

Two readings state it for controllers:
- **What safety costs** (THEORY-1254). A policy that must keep every
  model it has not ruled out safe cannot commit before it has excluded
  the models under which commitment is unsafe, and it cannot use what
  the commitment itself would show. If what it can learn beforehand is
  bounded by β nats, it forfeits at least about ½e^{−β} of the value
  only commitment reaches; acting at risk α needs about log(1/(2α))
  nats first.
- **When it can be paid** (THEORY-1256). Where a conservative
  experiment is safe under every plausible model, can be repeated from
  a common state and keeps informing, acting on the lower end of an
  anytime confidence sequence stays safe and approaches the oracle. A
  certainty-equivalent policy, acting on its best estimate, is unsafe
  half the time however much it has seen.

## What would count as an answer

- For a kind of organization the record holds, whether its commitments
  are of the first kind (no safe, repeatable, informative trial short of
  committing) or the second, and what that implies for CLAIM-535's
  policy: acceptable in every circumstance it cannot exclude, and so
  never committing where only commitment informs, or acceptable at a
  stated risk.
- Or an argument that CLAIM-535's "every circumstance" requirement is
  the organizational counterpart of the readings' uniform safety, so
  their bound carries over, or that it is not.

## What it does not ask

Whether the readings' controllers model organizations in general. Their
results are for one parametric model class with a per-model bound on
the probability of violation; a budget on cumulative violations is a
different criterion (THEORY-1254, "What this does not say").
