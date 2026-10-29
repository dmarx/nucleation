---
number: 1021
status: Proposed
formerly:
- THEORY-tmp52c5a
promote_when: >-
  A comparison of attribution patching against exhaustive activation
  patching across node types and depths in more than one model family and
  task, reporting agreement (rank correlation or verified recall of the
  top effects) separately for head-level activations, MLP neurons, whole
  layer outputs and residual streams, and by distance from the metric. It
  is confirmed if head-level and late nodes agree well while residual
  streams and early layers agree badly, and if the large disagreements are
  concentrated in saturated nonlinearities and effects that need several
  features at once. It is refuted if residual-stream estimates agree about
  as well as head-level ones, or if the main disagreements lie elsewhere.
  More single-task demonstrations in GPT-2 Small cannot settle it, nor can
  comparisons that test only fine-grained nodes.
title: 'In transformer language models, attribution patching agrees well with activation patching for small patches of single heads and their queries, keys, values and attention patterns, for nodes late in a circuit relative to the metric, and for circuits that route information through attention, and agrees badly for large patches such as whole residual streams, for the first MLP layer and the early layers of deep circuits, where nonlinearities move out of saturation, and where an effect needs several features at once, as Nanda proposes'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Proposed from NOTE-1201. Its evidence is one task (IOI) in
    one model (GPT-2 Small), shown in plots this reading did not see, and
    the rest is offered by the author as "wild speculations, with some
    limited empirical backing". The mathematical core is THEORY-1023,
    Active.
tags:
- representation-learning
- causality
date: '2026-10-27'
source:
- LIT-1581
extends:
- THEORY-1023
summary: >-
  Nanda (2023), [LIT-1581](../literature.d/LIT-1581.md), read in [NOTE-1201](../notes.d/NOTE-1201.md). The post's map of
  where the first-order estimate can be trusted. The record holds it from
  one task in the post, from the mathematics of the estimate
  ([THEORY-1023](THEORY-1023.md)), and in part from Kramár et al.'s test on Pythia
  ([THEORY-996](THEORY-996.md)), which found misses behind saturated attention, as this
  predicts, and tested no residual-stream nodes.
---
# THEORY-1021: In transformer language models, attribution patching agrees well with activation patching for small patches of single heads and their queries, keys, values and attention patterns, for nodes late in a circuit relative to the metric, and for circuits that route information through attention, and agrees badly for large patches such as whole residual streams, for the first MLP layer and the early layers of deep circuits, where nonlinearities move out of saturation, and where an effect needs several features at once, as Nanda proposes

## Source

Nanda (2023), [LIT-1581](../literature.d/LIT-1581.md), read in full in [NOTE-1201](../notes.d/NOTE-1201.md): Does This Work
In Practice, Does This Make Any Sense, and My Guesses for Where
Attribution Patching Works.

## What is asserted

From the experiments: on IOI in GPT-2 Small, the estimate is "a bad
approximation for 'big' activations like residual stream patching and for
MLP0, a good approximation for all other layer outputs, head outputs, and
more zoomed in head activations". From the author's guesses: it works
"towards the end of circuits", for "circuits to do with routing
information", for "incremental changes in key activations" and for
"small, targeted patches", and badly for "MLP heavy circuits", "early
layers of circuits with many layers composing", "contexts with
multi-variable dependence", attention weights "very close to zero or one",
and "when we patch a 'big' activation".

## What the record holds toward it

- **The mathematics** ([THEORY-1023](THEORY-1023.md)): the estimate's error is second
  order in patch size, it vanishes in saturation, it cannot see
  interactions, and through LayerNorm it ignores the component along the
  residual stream. Those are reasons to expect the pattern, not
  measurements of it.
- **One task in the post**, IOI in GPT-2 Small, with scatter plots not
  seen here. The post states no agreement figure.
- **Kramár et al. ([THEORY-996](THEORY-996.md))**, on Pythia 410M to 12B: misses
  concentrated behind saturated attention and in nodes whose direct and
  indirect effects cancel. The first is predicted here. The second is not
  among the post's failure cases; the post treats cancellation in backup
  heads as a source of false positives. Only fine-grained nodes (heads'
  queries, keys, values and outputs, and neurons) were tested, so the
  residual-stream half is untouched.
- **MLP0** is explained in the post by its acting "as an extended
  embedding", with discrete structure. That is a conjecture.

## Why it stays Proposed

One model and one task for the measured part, and none of the rest
measured, as the author says. The one systematic test held agrees on
saturation, adds a failure mode the post does not name, and does not test
large patches.

## What would confirm or reject it

The promote_when above.
