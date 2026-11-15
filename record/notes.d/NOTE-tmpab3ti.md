---
status: Read
paper: 'LIT-tmp52idf'
title: 'Elazar et al. — Amnesic Probing'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 by a delegated reader from arXiv:2006.00995v3,
    https://arxiv.org/pdf/2006.00995v3 (15 pp.), text by pdftotext: the
    abstract, §1, §2 (method and controls), §4 (Table 1 discussion), the
    head of §5, §6 (fine-grained labels, Tables 3–4), §§7.1–7.2, §9
    Discussion and §10 Conclusions. Figures 3–4 (heatmaps) were read from
    the prose only, since their numbers are not in the text layer. Not
    compared with the TACL version. The filer rechecked every quotation
    below against a fresh text extraction of the same PDF; all were found.
date: '2026-11-15'
summary: >-
  In BERT-base, how well a linear probe decodes a property does not
  predict how much INLP removal of it hurts masked-word prediction
  (Spearman 8.5, p = 0.871, six properties), and what is removed at an
  early layer is largely re-decodable at later layers, in the unmasked
  setting.
---
<!-- inactive-ok-file: THEORY-287 THEORY-104 — Proposed; held readings cited as neighbours, nothing rests on them -->

# NOTE-tmpab3ti: Elazar et al. — Amnesic Probing

## Contribution

An interventional replacement for accuracy-based probing: remove the
property and see whether the model's behaviour changes. And evidence that
the two disagree: properties a probe decodes well need not be used.

## Key insight

Probe accuracy says that a property is encoded; it does not say that the
network uses it. Removing the property and measuring the behavioural cost
asks the second question, provided the removal is controlled against
removing as many random directions.

## Assumptions

- INLP is the removal operator: linear, first-order (§2).
- The removed directions approximate the abstract property, which §9 says
  explicitly need not hold.
- BERT-base; properties from gold-annotated corpora (PTB, OntoNotes).

## Key results

- **Non-correlation** (§4): "the probe accuracy does not correlate with
  task importance as measured by our method (Spearman correlation of 8.5,
  with a p-value of 0.871)"; "high probing performance does not entail
  this information is being used at a later part of the network." The
  correlation is over six properties.
- **Fine-grained** (§6, Table 3, masked c-pos): removal hurts the
  prediction of function words far more than content words; determiner
  Δ 65.66 and particle Δ 77.66 against noun Δ 8.65.
- **Layer-wise recoverability** (§7.1): for c-pos, non-masked, "the
  information is highly recoverable in subsequent layers when applying
  the amnesic operation on the first seven layers": the drop is "between
  5.72 and 12.69 accuracy points", while in the second part of the
  network "the drop is substantially larger: between 16.57 and 46.39". In
  the masked version "we witness an opposite trend".
- **Limits, stated** (§9): "we remove only linearly-present information";
  "we neutralize the information from certain layers, but occasionally
  observe higher probing accuracy in following layers"; and "the
  classifiers can rely on arbitrary features that happen to correlate".

## Concepts

- **Amnesic counterfactual**: the representation with the property
  removed, fed on to the rest of the network.
- **Selectivity control**: removing the same number of random directions.
- **Layer-wise recoverability**: whether the property can be decoded
  again at layers after the one where it was removed.

## Bearing on the record

- **QUESTION-010**: the nearest empirical analogue in the batch, in the
  reverse direction. Information removed at layer i is partly regenerated
  by later layers from correlates left in the representation, so a chain
  can restore what one of its steps erased. Linear erasure, one model; not
  an answer.
- **TERM-064**: "decodable" means legible to a linear probe, and
  legibility is not monotone along the network, which is THEORY-846's
  point that computation can create usable information.
- **CLAIM-407**: an analogy of shape only. Observation (probe accuracy) and
  intervention (amnesic removal) disagree, as ordinary adequacy and
  interventional response do there; it is not an instance of the claim's
  coarse-graining construction.
- **THEORY-287** (interchange intervention predicts behaviour better than
  probes) and **THEORY-104** (the best linear-readout layer lies below the
  top) are held readings of the same "intervene, don't just probe" and
  layer-wise kind.

## Connections

It uses INLP (LIT-tmp3i6ea) as its removal operator. Kumar, Tan & Sharma
(2022), LIT-tmpzdaep, NOTE-tmpqbu99, argue that amnesic probing is flawed
because it depends on a good concept classifier; §9 here concedes a milder
form of the same point.

## Limitations

Linear removal, which may remove correlates rather than the property
(§9). Six properties for the correlation. BERT-base only.
