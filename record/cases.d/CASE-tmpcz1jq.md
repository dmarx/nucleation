---
status: Proposed
title: 'A model trained while one chief executive held office answers with that name after a successor has left and the first is reappointed: a true belief, reliably produced from its source, whose truth does not depend on what now makes it true'
version: 1
standing: fictional
kind: thought-experiment
tags:
- epistemology
- learning-theory
- causality
date: '2026-11-23'
line:
- learned-structure
bears_on:
- QUESTION-493
draws_on:
- THEORY-1737
summary: >-
  The fourth of the set LEAD-001 asks for: a learning system's Gettier
  case. A model whose training data end while Avery runs a firm answers
  "Avery" to "Who runs the firm?". Since then Blake ran it and left, and
  Avery was reappointed last month. The answer is true, believed, and
  produced by a source that was reliable for its period; it would have
  been the same had Blake stayed. The construction is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-079 THEORY-1737 — Proposed; cited as the criterion applied and as a reading the case draws on, not relied on -->
<!-- inactive-ok-file: CASE-tmpr1f20 CLAIM-tmp5qk10 CLAIM-tmpeonjp CLAIM-tmpngm72 — Proposed; filed by the lead run of 2026-11-23 -->

# CASE-tmpcz1jq: A model trained while one chief executive held office answers with that name after a successor has left and the first is reappointed: a true belief, reliably produced from its source, whose truth does not depend on what now makes it true

## The case

A model's training data end in year 1. Throughout the data, Avery is the
chief executive of a firm, and the model answers "Avery" to every
phrasing of "Who runs the firm?", and uses it as a premise (who signs the
annual letter, whose strategy the firm follows). In year 2 Blake replaced
Avery; in year 3 Blake left and the board reappointed Avery. The model is
queried in year 3, with no retrieval.

Two variants hold the model fixed and change the world or the context:

- **Had Blake stayed**, the model would still answer "Avery", falsely.
- **Given in context** a dated, reliable news item that Blake was
  appointed in year 2, and nothing about year 3, the model still answers
  "Avery" in most samples.

## What it separates

- **True belief, reliably sourced, without knowledge.** The answer is
  true and is a belief by TERM-079's probes. The process that produced it
  (training on a period's documents) was reliable for that period. What
  makes it true now is the reappointment, and the answer does not depend
  on it: across the variants the answer is fixed while its truth varies.
- **Belief that does not respond to valid corrective evidence.** The
  second variant shows the belief is not revised by evidence that should
  revise it, so the model's being right in year 3 is not even the
  disposition of a careful updater who happened to lack news.

## Against the candidate answers

QUESTION-493's candidate (A73) gives three criteria and four tests. Truth
holds; reliability over the family of queries in the training period
holds, and over the family "present-tense queries across years" fails;
grounding fails, since the answer is not connected to what now makes it
correct. A73's third test, "a changed fact with valid corrective
evidence", is the one that shows it, and THEORY-1737 reports the
documented pattern at scale: memory agents fed conflicting facts in turn
fail to act on the latest. The case agrees with A73's verdict, not
knowledge, and adds what A73 leaves implicit: the declared family must
range over the times the truthmaker can change, not over the training
period. As in CASE-tmpr1f20, the two readings of grounding filed as
alternatives, CLAIM-tmp5qk10 and CLAIM-tmpeonjp, agree on the verdict and
differ in what does the work.

## What it can show

That truth, belief and a reliable source together do not make knowledge
in a learning system whose source has gone stale: Gettier's structure
arises from training cut-offs without any contrivance. Being fictional,
nothing about how often it occurs. One of the separations CLAIM-tmpngm72
collects.
