---
status: Read
paper: 'LIT-tmp7xp5z'
title: 'Nickel, Rosasco and Poggio — Holographic embeddings of knowledge graphs'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read in full on 2026-11-15 from arXiv:1510.04935v2,
    https://arxiv.org/pdf/1510.04935, 7 pages, text by pdftotext: the
    compositional models, HolE, the associative-memory section, the
    experiments, Table 2 and the conclusion. Not read: the supplementary
    material, with the further relational-learning benchmarks and the
    figure on the similarity component, which is not part of the arXiv
    PDF; the AAAI version of record was not compared. The filer rechecked
    every quote below against the downloaded text; all were found, some
    only in the layout extraction, where the two columns interleave them.
date: '2026-11-15'
summary: >-
  HolE scores a knowledge-graph triple through the circular correlation of
  subject and object embeddings, a compressed tensor product with O(d)
  memory and O(d log d) time, non-commutative so it can model asymmetric
  relations. Its authors read it as Plate's holographic associative memory
  with the storage learned by SGD, so that it generalizes rather than
  memorizes. Reimplemented baselines under one protocol; best filtered MRR
  on WN18 and FB15k, mixed on FB15k Hits@10.
---
<!-- inactive-ok-file: CLAIM-182 — a Proposed claim, cited as an analogy or as having no bearing -->

# NOTE-tmpmehz3: Nickel, Rosasco and Poggio — Holographic embeddings of knowledge graphs

## Contribution

A link-prediction model, HolE, that keeps the rich pairwise interactions
of a tensor-product model at about the parameter cost of TransE, and an
explicit tie between relational embedding learning and holographic
associative memory.

## Key insight

The full tensor product of two d-dimensional embeddings has d² terms;
circular correlation sums them in fixed partitions to d, losing little,
because learning places the features into those partitions. Correlation,
unlike convolution, is not symmetric in its arguments, which a directed
relation needs.

## Assumptions

- A logistic link on the triple score, trained by a pairwise ranking loss
  with corrupted negatives, under an open-world assumption with local
  negative sampling.
- The partition of interactions is fixed in advance by the operator;
  learning adapts the embeddings to it.
- The associative-memory reading is an analogy: HolE is trained by SGD,
  not written Hebbian-style.

## Key results

- **Model** (Eq. 9): Pr(φp(s, o) = 1 | Θ) = σ(rpᵀ(es ⋆ eo)).
- **Compression** (§HolE, Table 1a): "circular correlation can be
  interpreted as a compression of the tensor product"; O(d) memory and
  O(d log d) runtime by FFT against O(d²) for both.
- **Non-commutativity**: "Correlation, unlike convolution, is not
  commutative ... Non-commutativity is necessary to model asymmetric
  relations". One component, [a ⋆ b]_0, is the dot product.
- **Memory analogy** (§Associative memory): "we can interpret eq. (15) as
  adapting the 'memory' eo, such that the retrieval of the observed facts
  is improved"; the difference from associative memory "is that it does
  not only memorize, but it generalizes in a well defined way". Clean-up
  is an argmax over items (Eq. 13).
- **WN18, filtered** (Table 2a): MRR HolE 0.938, RESCAL 0.890, TransE
  0.495; Hits@1 93.0, 84.2, 11.3.
- **FB15k, filtered** (Table 2a): MRR HolE 0.524, TransE 0.463; Hits@10
  HolE 73.9, TransE 74.9.
- **Countries, AUC-PR** (Table 2b): S1 0.997 for HolE and RESCAL; S2 0.772
  against 0.745; S3 0.697 against 0.650.
- **Protocol**: all models reimplemented with one loss and optimizer
  (AdaGrad SGD, ranking loss), which the authors say improved TransE's and
  RESCAL's results significantly over the published numbers.

## Concepts

Knowledge-graph embedding and link prediction; circular correlation as a
compressed tensor product; non-commutative composition for asymmetric
relations; holographic associative memory; filtered MRR and Hits@k.

## Connections

- **Plate (1995)**, LIT-tmpq18t6: HolE is built on HRR. Shared: storage by
  convolution and retrieval by correlation, the compressed-outer-product
  reading, O(d log d) by FFT, and clean-up by nearest item (Plate's
  clean-up memory, HolE's argmax). Not shared: HolE composes by
  correlation rather than convolution, for non-commutativity, and learns
  its embeddings rather than storing given ones, which its authors credit
  for its generalization.

## Bearing on the record

- **A's characterization**: that HolE "uses circular correlation to model
  interactions among subject, relation, and object embeddings" is loose
  but fair (correlation joins subject and object; the relation enters by a
  dot product). "Competitive link-prediction performance" understates the
  paper's claim to outperform, which holds on filtered MRR and is mixed on
  FB15k Hits@10.
- **THEORY-272 (Hopfield)**: HolE draws the line between memorizing
  (associative memory, given embeddings, Hebbian storage) and learning
  (adapted embeddings that generalize). Content-addressable memory sits on
  the first side; no contradiction.
- **THEORY-1036 (superposition capacity)**: d² interactions packed into d
  components by a fixed, designed partition, with no capacity analysis.
  "More than d things in d dimensions" is shared; the model is not.
- **CLAIM-182**: interpretive, as under Plate: the relation vector reads
  one relation out of a compressed pair representation. HolE adds that
  where things go is learned.
- **LIT-232 (Knowledge Sheaves), THEORY-299**: the record's held
  knowledge-graph reading covers coboundary-type scores such as TransE;
  HolE is of the bilinear, compressed-tensor family, outside that account.

## Limitations

- The supplementary benchmarks were not read.
- WN18 and FB15k only; later critiques of those benchmarks were not read.
- The baselines are the authors' reimplementations.
- arXiv v2 only; the AAAI text may differ slightly.
