---
status: Read
paper: LIT-tmpi20ed
title: 'Kang et al. — Prompt-Activation Duality (GCAD)'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 by a delegated reader from
    https://arxiv.org/pdf/2605.10664 (v3, "arXiv:2605.10664v3 [cs.CL] 10
    Nov 2026", NeurIPS 2026), text extracted with pdftotext. Read in
    full: §§1–7. Appendices read: B.3–B.4, C, F, G, the Llama tables of E,
    H (part), K, L, M, N, O, P, Q, S, U and V. Skimmed or skipped: A, D
    (beyond per-trait tables), I, J, R (Table 29 only), T, W and the
    checklist. The v1 PDF was not read. The filer string-matched every
    quotation below.
date: '2026-11-15'
summary: >-
  Residual-stream persona steering degrades coherence over multi-turn
  dialogue while system prompting does not. A 2×2 cache-isolation test
  shows steered cache states to be one cause, with injection itself the
  larger. GCAD derives a steering vector from the system prompt's cropped
  contribution to attention and gates it per token. It keeps trait
  expression with little coherence drift on Qwen2.5-7B (point estimates,
  one judge) and on Llama-3.1-8B. The title's "duality" is not stated in
  the body.
---

<!-- inactive-ok-file: THEORY-1334 — Proposed; the persona-direction THEORY the reading bears on, no note filed -->

# NOTE-tmp80eb1: Kang et al. — Prompt-Activation Duality (GCAD)

## Contribution

1. **A failure mode named and tested.** KV-cache contamination under
   residual steering is identified and tested with a 2×2 cache-isolation
   experiment.
2. **A steering signal derived from the system prompt's contribution to
   self-attention.** It is cropped to the system-prompt source tokens and
   gated per token by query–key compatibility.
3. **Multi-turn persona-steering evidence** against residual baselines
   that are layer-matched, norm-matched and swept.

## Key insight

A steering vector added to every token's residual state is written into
the KV cache, and every later token reads it again. A local intervention
thus becomes a persistent change to the context. A system prompt, by
contrast, influences later tokens through attention to a fixed span, and
only where it is relevant. Steering that enters where a prompt's
influence enters, and as selectively, persists without compounding.

## Assumptions

- **A localizable cause.** The behaviour can be elicited by a localizable
  text span, a system prompt, and the model complies with it at
  extraction. The v3 abstract narrows the method to "prompt-localizable
  behaviors".
- **A linearization.** The residual decomposition is LN-free: "omitting
  layer normalization for analytical clarity" (§3.3.1).
- **A linear trait.** A trait is carried by a linear direction.
- **The judge.** An LLM judge's 0–100 coherence score measures
  degradation; there is no human evaluation.

## Key results

- **The failure** (§1, §3.2). "Since prompt-only control remains stable
  under the same protocol (Figure 1), the problem is not long context
  alone." "A likely mechanism is KV-cache contamination". The no-steering
  baseline drifts only −5.4 over 5 turns (App. G).
- **The 2×2 test** (§5.4, Table 3; App. N). Qwen2.5-7B, 7 traits, 5
  conversations each, 6 turns, mean of 3 judges.

  | Condition | Trait | Coherence | Loop rate |
  |---|---|---|---|
  | Inject, steered cache (standard) | 68.6 | 36.1 | 0.129 |
  | Inject, clean cache | 55.4 | 51.2 | 0.014 |
  | Steered cache only, no inject | 17.4 | 81.7 | 0.029 |
  | No steering | 12.7 | 84.1 | 0.014 |
  | GCAD | 89.0 | 73.6 | 0.010 |

  Clean minus standard: +15.0 coherence [+12.9, +17.1] and −13.1 trait
  [−17.4, −8.7]. The authors: "so steered cache states are one cause of
  the collapse", and "The trait thus needs a steered cache, and removing
  the steering afterwards discards the trait along with the damage."
- **The headline** (Table 1, Qwen2.5-7B, 15-trait average). Coherence
  drift from turn 1 to turn 10 is −18.6 for residual steering and −1.9
  for GCAD. Turn-10 trait expression is 78.0 against 93.1. The results
  come from one judge (gpt-4.1-mini) and one question seed, as point
  estimates.
- **Llama-3.1-8B** (App. E): drift −26.5 against −0.2.
- **Controls** (Table 2). Against a layer-matched, summed-L2-matched
  residual baseline over 8 traits, GCAD gains +5.8 trait and +17.0
  coherence. Against the best swept residual layer (2 traits), it gains
  +40.8 trait, and the coherence difference, −3.4, has an interval
  spanning 0. "GCAD injects less than standard steering (L2 of 39.5
  versus 52.8 per position)".
- **Ablations** (Table 4): cropping and gating mainly protect trait
  expression; coherence is roughly flat across them.
- **Single turn** (AxBench, App. R): GCAD scores 0.445, below prompting
  (0.731).

## Concepts

- **Persona vectors** and **residual-stream steering**.
- **The residual decomposition** into embedding, attention and MLP terms,
  and the **attention decomposition over source tokens**.
- **Cropped attention delta**: the system-prompt part of attention's
  output.
- **Query–key gate.**
- **KV-cache contamination**: a steered (dirty) cache against a clean one.
- **Trait–coherence frontier.**

## Connections

It builds on Chen et al.'s persona vectors ([LIT-1998](../literature.d/LIT-1998.md), [NOTE-1524](NOTE-1524.md)): their
extraction pipeline, rubrics and judge prompts. It is related to
in-context vectors, prefix tuning, AxBench and ReFT, none of which the
record holds.

## Bearing on the record

- **[LIT-1998](../literature.d/LIT-1998.md) / [NOTE-1524](NOTE-1524.md)** (Persona Vectors). This paper reports the
  multi-turn coherence cost of Chen et al.'s layer-20 steering, with an
  average drift of −18.6 on Qwen2.5-7B. It also decomposes their vector into
  trait-bearing (attention) and other components. No note filed: this
  qualifies the steering use, not their monitoring account.
- **[THEORY-1334](../theory.d/THEORY-1334.md)** (prompting and finetuning persona shifts are mediated by
  the same linear directions). This paper argues that a residual persona
  vector mixes the prompt-mediated attention component with
  response-content components. That complicates "the same direction" as
  the mediator of a prompt's effect, but it has no finetuning evidence
  and does not meet that entry's promote_when. No note filed; the
  bearing is recorded here.
- **[QUESTION-443](../questions.d/QUESTION-443.md)** (does a chat model's persona position follow the latest
  user message?). Under residual steering, persona state is carried
  forward through cached steered states: trait drops 13 points when the
  cache is cleaned. This is weak, indirect evidence that history adds to
  the current input, and only in a steered model. No note filed.
- **[LIT-1991](../literature.d/LIT-1991.md) / [THEORY-1339](../theory.d/THEORY-1339.md)** (the Assistant Axis, multi-turn persona
  drift). An adjacent dynamic, but here the drift is induced by the
  intervention, not by user messages.

## Limitations

- **The headline is thin.** It comes from one model, one judge and one
  question seed, with three samples per group and no interval on
  Table 1.
- **The cache test explains the level of coherence more than its drift.**
  Pooled cross-turn drift is not reduced by cleaning (−10.6 clean against
  −6.8 steered).
- **Injection itself is the larger cause.** With a clean cache, coherence
  is still far below no steering (51.2 against 84.1).
- **"Duality" is not a result.**
- **Coverage is partial**: the cache test covers 7 of 15 traits, and the
  layer-matched control 8.
- **On AxBench, GCAD trails prompting.**
- **Calibration is needed per model**: "Model-level calibration remains
  necessary" (App. S).

## Open questions

- Would a steering method that writes nothing into the cache, steering
  only the current token's output while keeping states clean, keep the
  trait? The 2×2 test suggests not ("The trait thus needs a steered
  cache"). If so, multi-turn trait expression is carried partly by the
  context itself.
