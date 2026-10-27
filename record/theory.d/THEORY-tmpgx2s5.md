---
status: Active
title: 'In Claude 3.5 Haiku, on the prompt "Fact: the capital of the state containing Dallas is", which it completes with "Austin", an attribution graph shows Dallas features activating Texas features that, with "say a capital" features, promote Austin, beside a direct edge from Dallas to "say Austin"; inhibiting the Dallas features lowers the Texas features and leaves "say a capital" largely intact, and replacing the Texas features with those of California, Georgia, British Columbia, China or the Byzantine Empire makes the model name that place''s capital'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmpl4x31. One case study, read in full (the
    section Introductory Example: Multi-step Reasoning with its two
    validation subsections); the title claims no more than it measured, on
    one prompt and its five analogues, and nothing in the record
    contradicts it (ADR-047 v3). The article's general statement that the
    model routinely reasons in several steps is the Proposed
    THEORY-tmpfralg.
tags:
- representation-learning
- cognition
date: '2026-10-26'
source:
- LIT-tmpjvwet
extended_by:
- THEORY-tmpfralg
summary: >-
  Lindsey et al. (2025), LIT-tmpjvwet, read in NOTE-tmpl4x31. A two-hop
  intermediate, measured by intervention on one prompt. The evidence that
  counts is the change of output under the swaps; the graph itself is of
  the replacement model. It does not say how often the model reasons in
  two steps, nor that the shortcut path is weak.
---
<!-- inactive-ok-file: THEORY-tmpfralg — Proposed; the wider thesis, cited as open -->
# THEORY-tmpgx2s5: In Claude 3.5 Haiku, on the prompt "Fact: the capital of the state containing Dallas is", which it completes with "Austin", an attribution graph shows Dallas features activating Texas features that, with "say a capital" features, promote Austin, beside a direct edge from Dallas to "say Austin"; inhibiting the Dallas features lowers the Texas features and leaves "say a capital" largely intact, and replacing the Texas features with those of California, Georgia, British Columbia, China or the Byzantine Empire makes the model name that place's capital

## Source

Lindsey et al. (2025), *On the Biology of a Large Language Model*,
Transformer Circuits Thread, LIT-tmpjvwet, read in NOTE-tmpl4x31: the
section "Introductory Example: Multi-step Reasoning", with "Validation with
Inhibition Experiments" and "Swapping Alternative Features". The method is
LIT-tmpsuo6l.

## What was actually shown

**The graph.** With a 30M-feature cross-layer transcoder, the pruned graph
for "Austin" contains supernodes the authors labelled from feature
visualizations: Dallas, Texas (Texas-related features "not specific to a
particular city"), capital (including multilingual capital features), say
a capital, and say Austin. Paths: Dallas → Texas; capital → say a capital;
Texas and say a capital → Austin, directly and via say Austin; and Dallas →
say Austin directly.

**Inhibition.** Clamping each supernode to a negative multiple of its
activation in the model: inhibiting Dallas lowers Texas and say Austin and
leaves say a capital largely unaffected, and the model outputs other state
capitals; inhibiting capital lowers say a capital and say Austin and leaves
Texas largely unchanged, and the model gives non-capital completions.

**Swaps.** Texas features inhibited and features from an analogous prompt
injected: from "Oakland", the model outputs Sacramento; from "Savannah",
Atlanta; from "Vancouver" (province), Victoria; from "Shanghai" (country),
Beijing; from "Thessaloniki" (empire), Constantinople. The non-state swaps
needed larger injections.

**What could have come out otherwise.** The graph could have shown only the
shortcut, with no Texas step. Inhibiting Dallas could have left Texas
intact. Swapping the Texas features could have left "Austin" in place,
which is what a completion carried by the shortcut alone would do.

## What this does not say

- **Not that the model usually reasons in two steps.** One prompt and its
  analogues, chosen from the prompts where the method gave a clear graph.
- **Not that the shortcut is negligible.** Both paths are present; the
  article does not measure their shares of the output.
- **Not that "Texas" is a single representation.** It is a hand-made group
  of several features, each with other facets (one is about law and
  government in Texas).
- **Not about the model's attention.** Why the "Dallas" information
  reaches the final position is not shown.
