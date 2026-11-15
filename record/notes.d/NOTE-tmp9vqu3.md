---
status: Read
paper: 'LIT-tmpq18t6'
title: 'Plate — Holographic reduced representations'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 from the IEEE version as a scan with an OCR layer,
    19 pages, posted by the Redwood Center for Theoretical Neuroscience,
    https://redwood.berkeley.edu/wp-content/uploads/2020/08/Plate-HRR-IEEE-TransNN.pdf,
    text by pdftotext in flowed and layout modes. Read: Sections I–III, V,
    VIII, IX and XI, and parts of Section X and Appendices A–B. Skimmed:
    Section IV (clean-up memory) apart from its conclusion, Section VI
    (features, types and tokens) and Section VII (two machines). The
    appendix derivations were not followed. The OCR layer is noisy and
    garbles formulas, so the capacity fit of §IX is given as the reader
    transcribed it and marked as such. The filer rechecked every quote
    below against the downloaded text; all were found, the outer-product
    sentence only in the layout extraction, where the two columns
    interleave it.
date: '2026-11-15'
summary: >-
  Plate binds vectors by circular convolution, which keeps their dimension,
  so associations are items and can be bound and superposed again: fixed-
  width distributed representations of sequences, bindings and frames.
  Circular correlation decodes approximately; a separate item memory cleans
  up the noisy result. For independent random vectors the number of pairs a
  trace holds grows about linearly with the dimension, with a log factor in
  the number of candidate items. Holographic only by descent from
  convolution–correlation memories.
---
<!-- inactive-ok-file: CLAIM-182 — a Proposed claim, cited as an analogy or as having no bearing -->

# NOTE-tmp9vqu3: Plate — Holographic reduced representations

## Contribution

Earlier associative memories stored items as vectors and associations as
matrices, in different spaces, so an association could not itself be an
item. Plate gives a concrete, analysable operator for compositional
distributed representation in a fixed width: binding by circular
convolution, which keeps the dimension, so an association can be bound or
superposed again. That realizes Hinton's reduced descriptions, and the
paper analyses its inverses, its capacity and the structures it can
encode, and ties it to convolution–correlation ("holographic") memory.

## Key insight

A bound pair can live in the same space as its parts if binding is a
compressed outer product; the price is that unbinding is only
approximate, so the system needs a second memory that maps a noisy result
to the nearest stored item.

## Assumptions

- Vector elements independent, about N(0, 1/n), and items uncorrelated;
  similar or repeated items raise the error rate.
- Retrieval needs a clean-up memory holding every item, so the scheme is
  not self-sufficient.
- Decoding degrades with depth of nesting and with the number of
  superposed terms; chunking works around this soft limit.

## Key results

- **Name** (§I): "I call these holographic reduced representations
  (HRR's), since convolution and correlation based memories are closely
  related to holographic storage."
- **Convolution as compressed outer product** (§II.B): the convolution of
  two vectors "can be regarded as a compression of the outer product of
  those two vectors", summing along trans-diagonals.
- **Approximate inverse** (§II.C): "what is remarkable is that circular
  correlation ... is an approximate inverse operation of it".
- **Binding** (§V): "the binding of the value a to the variable x and the
  value b to the variable y is" x ⊛ a + y ⊛ b. "Variables can be unbound by
  convolving the binding with the approximate inverse of the variable."
- **Clean-up** (abstract, §XI): "The noisy reconstructions extracted from
  convolution memories can be cleaned up by using a separate associative
  memory"; systems "must have an error-correcting autoassociative memory to
  clean up the noisy results".
- **Exact against approximate inverse** (§VIII.C): "Unless unitary vectors
  are used, however, using the exact inverse results in a lower
  signal-to-noise ratio in the retrieved vector when the memory trace is
  noisy".
- **Capacity** (§IX): "The number of associations that can be stored in a
  convolution memory is approximately linear in the dimensionality of the
  vectors." The reader's transcription of the numerical fit, through noisy
  OCR, is n = 4.5(k + 0.7) ln(m/30q⁴), with k pairs, m candidate items and
  q the probability of one or more errors.
- **Hopfield set aside** (§IV): "Hopfield networks are probably not a good
  candidate because of their low capacity in terms of the dimension of the
  vectors being stored". Kanerva networks have "sufficient capacity" "but
  can only store binary vectors". The simulations use exhaustive
  dot-product lookup.
- **Computation** (§VIII): O(n log n) via the FFT.

## Concepts

Circular convolution binding; circular correlation and the involution as
approximate inverse; superposition by addition; clean-up (item) memory;
reduced descriptions; unitary vectors; capacity linear in dimension.
"Vector symbolic architectures" is a later name, not the paper's.

## Connections

- **Nickel, Rosasco & Poggio (2016)**, [LIT-tmp7xp5z](../literature.d/LIT-tmp7xp5z.md), build HolE on this
  paper: storage by convolution, retrieval by correlation, the
  compressed-outer-product reading and an argmax clean-up. HolE composes by
  correlation for non-commutativity and learns its embeddings.
- **Angle-multiplexed volume holography**, read through Márquez et al.
  (2023), [LIT-tmp3d5f9](../literature.d/LIT-tmp3d5f9.md): the same structure of many items superposed in one
  medium and read out by a key. Plate draws the parallel only through the
  name.

## Bearing on the record

- **A's characterization**: "circular convolution for binding, vector
  addition for superposition, and circular correlation for approximate
  retrieval", with "a cleanup memory" for noisy retrieval, holds exactly.
  "Explicitly draws on holographic memory mathematics" holds for
  convolution–correlation memories, which Plate notes had been "regarded as
  inferior to matrix style associative memories"; he does not use optical
  holography.
- **[THEORY-272](../theory.d/THEORY-272.md) (Hopfield)**: a complementary contrast. HRR is
  hetero-associative with items and associations in one space; Plate sets
  Hopfield aside as clean-up memory for its low capacity per dimension.
  Nothing here contradicts [THEORY-272](../theory.d/THEORY-272.md).
- **[THEORY-1036](../theory.d/THEORY-1036.md) (superposition capacity)**: both are capacity in
  superposition, under different models: k random bound pairs in n
  dimensions with fixed decoding here, a learned allocation in a toy model
  there. Neighbours, not the same result.
- **[QUESTION-120](../questions.d/QUESTION-120.md)**: a further random-code threshold of a different shape,
  n growing with k times log m, to set beside the distance, sparse-recovery
  and SDM thresholds that question compares.
- **[CLAIM-182](../claims.d/CLAIM-182.md)**: interpretive only. A trace holds many items superposed,
  nothing spatially separate, and each is recovered by its key (the role
  vector) followed by content-addressed clean-up. That suggests an address
  need not be a location, and also that keyed readout of a superposed store
  is noisy without a second memory. The claim is about records, so this is
  analogy, not evidence.
- **[TERM-064](../terms.d/TERM-064.md) (legibility)**: a bound filler is not recoverable from the
  trace without the right key and the clean-up memory, an instance of
  legibility relative to the observer's resources.

## Limitations

- The OCR garbles formulas, so the capacity fit is the reader's
  transcription of the approximation, not the exact inequality.
- Sections VI and VII were skimmed.
- The capacity analysis assumes random, independent vectors; learned or
  structured vectors are not analysed here.
