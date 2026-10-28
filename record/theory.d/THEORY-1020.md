---
number: 1020
status: Active
formerly:
- THEORY-tmp3gl09
title: 'In a two-layer attention-only language model, on tokens where induction helps, the standard induction circuit (queries and values from the token embedding, keys from the previous-token head) accounts for 35% of the loss its two induction heads contribute, and a hypothesis that adds three-token matching, layer 0''s average effect and three layer-0 heads acting as if they attended to the current token accounts for 86%'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Active from NOTE-1196, the reading of the induction-heads
    post in full. One study, and the title claims only what it measured,
    in one model, on its token subset and against its own baseline
    (ADR-047 v3). The baseline arithmetic (0.213 − 0.160 = 0.053) was
    checked; the percentages cannot be re-computed from what is published.
tags:
- representation-learning
- causality
date: '2026-10-27'
source:
- LIT-1579
summary: >-
  Chan, Garriga-Alonso, Goldowsky-Dill, Greenblatt, Lin et al. (2022),
  [LIT-1579](../literature.d/LIT-1579.md), read in [NOTE-1196](../notes.d/NOTE-1196.md). Percentages are of 0.053 nats, the
  loss the induction heads 1.5 and 1.6 contribute on next-token examples
  whose last token is on an induction-favouring whitelist, measured by
  causal scrubbing. The naive story's shortfall is mostly in the queries
  (51% alone) and keys (79%), not the values (90%). It does not say what
  fraction of the model's whole loss, or of its in-context learning, the
  circuit explains, nor anything about models with MLPs.
---
<!-- inactive-ok-file: THEORY-990 — Proposed; the wider thesis this bears on, cited as open -->

# THEORY-1020: In a two-layer attention-only language model, on tokens where induction helps, the standard induction circuit (queries and values from the token embedding, keys from the previous-token head) accounts for 35% of the loss its two induction heads contribute, and a hypothesis that adds three-token matching, layer 0's average effect and three layer-0 heads acting as if they attended to the current token accounts for 86%

## Source

Chan, Garriga-Alonso, Goldowsky-Dill, Greenblatt, Lin, Nitishinskaya,
Radhakrishnan, Shlegeris and Thomas (2022), *Causal scrubbing: results on
induction heads*, [LIT-1579](../literature.d/LIT-1579.md), read in full in [NOTE-1196](../notes.d/NOTE-1196.md): the
baseline, the naive hypothesis, refined hypotheses 1–4 and the bonus
hypothesis 5.

## What was actually shown

**The quantity.** On OpenWebText validation examples whose last context
token is on a whitelist chosen so that in-context repetition beats
bigrams, the model's loss is 0.160 nats. Running the two induction heads
on another sequence raises it to 0.213. A hypothesis's score is the
fraction of that 0.053 restored when every activation the hypothesis
calls unimportant is taken from the other sequence.

**The naive hypothesis.** Values only from the embedding via the
residual stream, queries likewise, and keys only from the previous-token
head 0.0. For keys, 0.0's OV reads only the previous position and its
attention pattern comes from the other sequence. Scrubbed together the
three restore 35%; separately Q 51%, K 79%, V 90%. This could have come
out near 100%, and it did not.

**The refinement, in steps.**

1. Layer 0 enters only through its OV pathway with attention taken from
   the other sequence: 62%.
2. As 1, with Q and K reading the current and two previous positions: 76%.
3. As 2, with 0.0, 0.1, 0.2 and 0.5 left unscrubbed for Q and K: 91%.
4. As 2, with heads 0.1, 0.2 and 0.5 rewritten as "identity attention"
   plus an error term taken from the other sequence: 86% (Q 97%, K 91%,
   V 97%).

A further step resamples 0.0's attention only among positions of the
same coarse "typicality" (after quote tokens or " a"/" an", or at "."
and " to"), and gives 89%.

## What this does not say

- **Not a share of the whole loss.** 35% and 86% are of the induction
  heads' 0.053-nat contribution on a filtered subset. On all tokens the
  authors say the fractions are lower and give no numbers.
- **Not comparable with the paren post's percentages.** Those are of a
  4.30-nat gap to a label-shuffled baseline ([NOTE-1195](../notes.d/NOTE-1195.md),
  [NOTE-1196](../notes.d/NOTE-1196.md)).
- **Not that 86% is the true circuit.** Leaving the layer-0 heads
  unscrubbed gives 91%. The more specific hypothesis is preferred for
  making more claims, at a cost of five points.
- **Not about larger models** or models with MLPs, and not about training.
- **Not an independent replication of the circuit's discovery.** The heads
  were picked by eye and the model is not published.

## Connections

- **[THEORY-973](THEORY-973.md).** Compatible. That account says induction heads form in
  one window and ablating them removes in-context learning in small
  attention-only models. This one says what those heads read, in one
  such model, and how far the usual diagram falls short of it.
- **[THEORY-990](THEORY-990.md).** The large-model thesis argues by analogy from the
  small-model circuit. Here the small-model circuit as drawn accounts for
  about a third of what the heads do.
- **[THEORY-978](THEORY-978.md).** The scores are partition scores. Hypothesis 4's rewrite
  is exactly the kind of rewrite of G that the account fixes when it
  compares two hypotheses.
