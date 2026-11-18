---
status: Read
paper: 'LIT-tmpdc2rl'
title: 'Zhu — Orientation, not magnitude: the causal structure of task-vector interference'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 from arXiv:2608.11797v1 (12 August 2026), from
    https://arxiv.org/pdf/2608.11797v1, text by pdftotext: §§1–8, the
    references and Appendix A (definitions). Appendices B–L (freeze log,
    replications, regrowth, SurgeryV2, NLL, templates) were skipped. v3,
    from https://arxiv.org/pdf/2608.11797v3, was skimmed: the abstract,
    the introduction, Figure 1, §4.2 and the §6 paragraph on collapse,
    with a search for the k = 6 result; its collapse experiments
    (Appendices J and M) were not read. Status Read for v1; v3 is
    Skimmed. The filer rechecked every quotation below against both
    downloaded texts. One reader's quotation, "make interference worse",
    is "makes interference worse" in the text and is quoted so here.
date: '2026-11-15'
summary: >-
  An exact layerwise ledger of the non-additive part of a two-task-vector
  LoRA merge in Qwen2.5 and Llama-3.2 at the final prompt token: about
  65–70% of its flux is transport of the existing term, amplified in late
  blocks; erased early it is rebuilt; erased along its own direction it
  reduces output non-additivity, and norm-matched wrong directions raise
  it. Templates suppress its expression in two-vector merges. v3 adds
  that it is a bystander in merge collapse.
---
<!-- inactive-ok-file: THEORY-107 CLAIM-498 THEORY-264 — Proposed; held entries this reading bears on or touches -->

# NOTE-tmpsyjfz: Zhu — Orientation, not magnitude: the causal structure of task-vector interference

## Contribution

An exact layerwise account of where the interaction between two merged
task vectors lives in a language model's forward pass, separating what
each block newly generates from what it carries forward, and the first
activation-level causal intervention on that interaction, with
norm-matched controls. All predictions were preregistered: 46 in v1, 81
in v3. It also shows that naive bf16 estimates of local generation are
mostly rounding roughness.

## Key insight

The interaction of two task vectors is not made anew at each layer. It is
mostly carried and amplified from earlier blocks, and the forward pass
rebuilds it when it is removed early. Its causal effect on how
non-additive the output is depends on its direction: a displacement of the
same norm in another direction does the opposite. v3 then limits what that
effect is about: removing the term does not repair a merge that has
collapsed.

## Assumptions

- One base model, two LoRA task vectors of rank 16, norm-matched, merged
  additively: θ0 + α∆A + β∆B.
- Measurements at the final prompt token only; the primary estimand is the
  first generated token's distribution, and output non-additivity R is a
  Jensen–Shannon interaction ratio.
- Interventions above λ = 1 are off-manifold; the claim is
  "direction-mediation under intervention, not natural mediation" (§5).
- Core results on Qwen2.5-1.5B with two task pairs, code + safety
  and code + math; Llama-3.2-1B and Qwen2.5-7B are reduced replications.

## Key results

- **The cross-term** (§3.1–3.2, Eq. 1). Four forward passes give
  Iℓ = h^AB_ℓ − h^A0_ℓ − h^0B_ℓ + h^00_ℓ, which "is everything
  non-additive that has accumulated before block ℓ", taken at "the final
  prompt token".
- **Transport** (abstract, §4.2). The flux is "dominated by amplifying
  transport of the existing cross-term", "∼65–70% in both model
  families": "transport carries ∼69% of the layerwise flux" on Qwen, with
  ∥Tℓ∥/∥Iℓ∥ = 1.08 per late block; on Llama "transport share 65%, late
  gain 1.14".
- **Not arithmetic accumulation** (§4.2). The observed final norm is "2.6×
  even the coherent bound", so summing local generations cannot produce
  it.
- **Regrowth** (§5). "erase at depth 3 or 8 and the network rebuilds the
  cross-term essentially exactly—final-boundary ρ = 1.00/0.99, direction
  cosine to" the original about 0.99; ρ = 0.94 erasing at 14 and 0.84 at
  20. The abstract reads the carried direction as an attractor of the
  forward pass; the regrowth window the author had preregistered was
  "falsified from above".
- **Direction specificity** (§5, Table 2). "the sign of the effect is
  decided by direction alone". Erasure removes "roughly 19% of expressed
  interference" at λ = 1 on code prompts, almost all of it from late
  erasures. Wrong-pair and coefficient-mismatch patches have negative
  effect: "an equally large, equally structured displacement in the wrong
  direction makes interference worse". The effect is "proportional to the
  displacement's projection on the erasure direction".
- **The central contrast** (abstract, §5). "task pairs whose local
  cross-term generation differs by at most 1.9× differ by 14×–337× in
  causally removable interference"; the middle figure is "inflated by a
  near-zero denominator".
- **Expression gating** (§6). An instruction wrapper increases local
  generation (3/3 seeds), yet the same erasure finds "a 13× mean ratio"
  less to remove. The mechanism is "denominator-driven": the wrapper
  inflates the main-effect divergence while the absolute interaction does
  not shrink.
- **Behaviour is not moved** (§5). "Erasure controls the non-additivity of
  the output distribution, not expert-likeness of behavior"; an NLL
  endpoint moves "±0.002 with inconsistent sign".
- **Cross-task linearity** (§7). Replicating Zhou et al. (2024),
  "layerwise linearity cosines are 0.93–0.98 across every family".
- **v3, collapse** (abstract, §6). "where merging actually collapses, the
  cross-term is a bystander, not the carrier: ... removing it entirely
  repairs none of the collapse (every preregistered repair gate failed)".
  "collapse rides in the marginal displacements".
- **v3, task count** (§6). "six task vectors rather than two raise R under
  the same template from 0.003 to 0.82", so suppression by a template is
  "a property of two-vector merges, not a law".
- **v3, methods** (§6). Of task arithmetic, trimming, TIES and DARE, "No
  method reduces R"; "TIES roughly doubles it" while giving the best
  behaviour in the small-scale cell, an inversion that "does not reproduce
  at 7B".

## Concepts

Factorial ledger; cumulative cross-term; local generation versus transport
versus mismatch; cross-term erasure; norm-matched controls; regrowth ratio
ρ; attractor of the forward pass; expression gating; the magnitude
fallacy; carrier versus bystander (v3).

## Bearing on the record

- **[THEORY-107](../theory.d/THEORY-107.md) (interference in parameter coordinates)**: qualifies, does
  not test. The paper does not compare sign with scale in coordinates.
  Its interference is the activation cross-term, and it argues that more
  of it measured at the output does not mean a worse merge. v3's audit
  finds TIES roughly doubling R while behaving best at small scale. That
  fits [THEORY-107](../theory.d/THEORY-107.md)'s caution that TIES's gain is not shown to come from
  resolving conflicts, but it is not evidence about sign.
- **[QUESTION-318](../questions.d/QUESTION-318.md) (layerwise linearity outside image classification)**:
  direct, partial evidence for the layerwise half. In LoRA merges of Qwen
  and Llama language models from one base, cosines are 0.93–0.98. The
  construction is a task-arithmetic sum, not an interpolation between two
  endpoints; only the final token is read; and the measure is a cosine,
  not [THEORY-111](../theory.d/THEORY-111.md)'s test of proportionality. The averaging half is not
  answered, though v3's six-vector merges are many-model sums with a
  growing interaction.
- **[CLAIM-498](../claims.d/CLAIM-498.md) (averaging weights averages features)**: consistent in
  spirit, since the residual is small, but the paper's point is that the
  residual is causally effective for output non-additivity. It measures
  no soup or SWA average, and the claim's defeater is not addressed.
- **[CLAIM-407](../claims.d/CLAIM-407.md) (closed coarse-graining need not preserve interventional
  responses)**: an analogy only. A format-wrapped output measure hides an
  internal interaction, and v3 has a quantity causally effective for one
  estimand and inert for another. No closure is constructed and no Γ
  computed.
- **[THEORY-264](../theory.d/THEORY-264.md) (demonstration and instruction use different heads)**:
  adjacent. Both find a presentation format changing what is expressed;
  nothing here is about heads.

## Connections

- **OrthoMerge ([NOTE-tmpy669h](NOTE-tmpy669h.md))** also locates the loss in directions that
  cancel, but in the Lie algebra of the update, not in activations, and
  repairs it by restoring magnitude.
- **OSRM ([NOTE-tmpf8m60](NOTE-tmpf8m60.md))** treats interference as first-order and
  layer-local, task 2's update acting on task 1's input. This paper finds
  most of the cross-term's flux is carried from earlier layers. The two
  are compatible; they address different stages.

## Limitations

- Single-author preprint, not peer-reviewed.
- LoRA only; two core task pairs and one wrapper family; the 13× figure is
  scoped to Qwen2.5-1.5B.
- The causal estimand is first-token non-additivity; recovery of behaviour
  by erasure was tested and failed.
- v3 substantially reframes the paper, and the v3 collapse experiments
  were not read.
- The appendices were not read.
