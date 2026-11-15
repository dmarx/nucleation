---
status: Read
paper: 'LIT-tmpbynva'
title: 'Reisizadeh et al. — Hidden-state leakage in model unlearning'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 by a delegated reader from arXiv:2609.36612v1,
    https://arxiv.org/pdf/2609.36612v1 (18 pp.), text by pdftotext: the
    abstract, §1 with §1.1 Contributions, §2.2 (Theorem 1), §§3.1–3.2
    (probing method and results) and §5 Conclusion. Skimmed: §2.1, Lemma 1
    and §4 (PARS). Not read: the appendices, and the values in Figures 4–6
    beyond the prose. The filer rechecked every quotation below against a
    fresh text extraction of the same PDF; all were found.
date: '2026-11-15'
summary: >-
  Output-level unlearning can leave forget-set content in hidden states:
  in a Gaussian model the output's leakage and the representation's
  information are set by separate quantities, and per-layer probe
  decoders trained on part of the forget set recover held-out forget
  content after six unlearning methods whose outputs show near-zero
  leakage.
---

# NOTE-tmpa1b4b: Reisizadeh et al. — Hidden-state leakage in model unlearning

## Contribution

An argument and evidence that unlearning judged at the output can be an
"illusion of forgetting": the model stops emitting forget-set content
while its hidden states still carry it. And a method, PARS, that
suppresses what probe decoders can extract.

## Key insight

What the output reveals and what the representation holds are governed
by different parts of the model. The decoder can be made blind to a
direction that still carries the information, so output-level tests
measure the decoder, not the knowledge.

## Assumptions

- Theorem 1 models the representation with Gaussian noise independent of
  (C, S).
- The probe is a decoder head per layer, "initialized from the unlearned
  model's decoder parameters", trained on an 80% split of the forget QA
  set and evaluated on the other 20% (§3.1).
- Models of 1B–7B parameters; benchmarks TOFU, MUSE-News and WMDP-Bio.

## Key results

- **Theorem 1** (§2.2): I(S; R) is bounded below by ½ log(1 + N(µS)/τ²),
  a property of the backbone, and I(S; Z | C) above by ε² Var(µS), with ε
  a property of the decoder. "Since these two quantities are
  independently controlled, one can simultaneously achieve I(S; Z | C) = 0
  and I(S; R) ≥ M for any M > 0 by setting ε = 0". "Suppressing sensitive
  outputs is not the same as erasing sensitive knowledge."
- **TOFU** (§3.2): "almost all unlearning methods exhibit more sensitive
  information leakage under ES metric in their hidden states than at the
  output level".
- **MUSE-News** (§3.2): "all methods appear successful under output-level
  evaluation, with near-zero verbatim leakage; however, probe decoders
  still recover significant verbatim information from hidden states
  across multiple layers."
- **Table 1**: for an item whose answer is 2005, the probe at layer 28
  returns 2005 for NPO, SAM and SimNPO while the outputs give other years
  (as the reader reports the table).
- **PARS** (§1.1): on TOFU it "achieves perfect forgetting under the
  Entailment Score", and on MUSE-News it "reduces post-relearning VerbMem
  by 61%" relative to SAM.

## Concepts

- **Output suppression vs representational erasure**: the paper's central
  distinction.
- **Generative probe decoder**: a per-layer head trained to generate the
  forget-set answer from that layer's hidden state.
- **Illusion of forgetting**: output-level success with hidden-state
  leakage.

## Bearing on the record

- **[CLAIM-407](../claims.d/CLAIM-407.md)**: the clearest formal analogue in the batch, in shape only.
  A quantity at the output carries no information about S while the
  internal state does, and an intervention, a trained probe or
  relearning, exposes it. The claim concerns coarse-grainings and
  intervention kernels, not decoders, so this is not an instance.
- **[TERM-064](../terms.d/TERM-064.md)**: legibility to the output channel near zero, legibility to
  a trained readout at layer ℓ high: one distinction, present, illegible
  to one observer and legible to another.
- **[THEORY-846](../theory.d/THEORY-846.md)**: why a trained readout can extract what the output
  cannot.
- **[QUESTION-010](../questions.d/QUESTION-010.md)**: loosely. The across-layer leakage curves (Fig. 2) show
  information present mid-stack and suppressed at the end.

## Connections

Lu et al. (2025), [LIT-tmpokxet](../literature.d/LIT-tmpokxet.md), [NOTE-tmpsiphf](NOTE-tmpsiphf.md), name a discovery-versus-induction
limit for strong probes; it applies here too, since the probe is trained
on forget-set answers. Neither paper separates the two.

## Limitations

A preprint. Small models. The probe-versus-relearning confound above.
Theorem 1 is a stylized Gaussian model. The appendices were not read.
