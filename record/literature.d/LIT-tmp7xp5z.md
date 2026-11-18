---
status: Active
status_note: >-
  read in full 2026-11-15 ([NOTE-tmpmehz3](../notes.d/NOTE-tmpmehz3.md)) from arXiv:1510.04935v2, from
  arxiv.org; the supplementary material, with the further benchmarks, is
  not part of the arXiv PDF and was not read. Worth reading here as the
  learned descendant of Plate's holographic reduced representations,
  [LIT-tmpq18t6](LIT-tmpq18t6.md): a knowledge-graph embedding that scores a triple through
  circular correlation, a compressed tensor product, and that its authors
  set apart from associative memory because it learns its embeddings and
  so generalizes.
title: 'Holographic Embeddings of Knowledge Graphs'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted continuation
    of the ChatGPT exchange "Explain String Theory", in A's turn on wave
    optics and holography as models for learning in neural networks.
    Citation checked against the arXiv API and Crossref (no mailto):
    Maximilian Nickel, Lorenzo Rosasco and Tomaso Poggio; Proceedings of
    the AAAI Conference on Artificial Intelligence 30(1), 2016 (AAAI-16),
    doi:10.1609/aaai.v30i1.10314, issued 2016-03-02. `published:` is the
    arXiv v1 date, 2015-10-16; v2 is dated 2015-12-07 and is the copy
    read. No email address was sent to any service.
tags:
- representation-learning
- information-retrieval
- anthology-candidate
date: '2026-11-15'
published: '2015-10-16'
arxiv: '1510.04935'
doi: '10.1609/aaai.v30i1.10314'
first_author: 'Nickel'
keywords:
- 'knowledge graphs'
- 'holographic embeddings'
- 'circular correlation'
- 'link prediction'
- 'associative memory'
- 'compositional representations'
implementations: []
summary: >-
  Nickel, Rosasco & Poggio (2016), AAAI-16. HolE scores a knowledge-graph
  triple as σ(r_pᵀ(e_s ⋆ e_o)) with circular correlation ⋆, which
  compresses the subject–object tensor product into d components at O(d)
  memory and O(d log d) time and, being non-commutative, models asymmetric
  relations. With all models reimplemented under one loss and optimizer it
  gives the best filtered MRR on WN18 and FB15k. Built explicitly on
  Plate's HRR, [LIT-tmpq18t6](LIT-tmpq18t6.md). A called it "competitive"; the paper claims to
  outperform, which holds on MRR and is mixed on FB15k Hits@10.
---
<!-- inactive-ok-file: CLAIM-182 THEORY-tmpcw54z — Proposed or Skimmed entries of this filing; and a Proposed claim, cited as an analogy or as having no bearing -->

# LIT-tmp7xp5z: Holographic Embeddings of Knowledge Graphs

Nickel, M., Rosasco, L. & Poggio, T. (2016). Holographic Embeddings of Knowledge Graphs. *Proceedings of the AAAI Conference on Artificial Intelligence* 30(1). arXiv:1510.04935. doi:10.1609/aaai.v30i1.10314.

## Key takeaways

*From the reading, [NOTE-tmpmehz3](../notes.d/NOTE-tmpmehz3.md); the account is [THEORY-tmpcw54z](../theory.d/THEORY-tmpcw54z.md).*

- **The model** (Eq. 9): Pr(φp(s, o) = 1 | Θ) = σ(rpᵀ(es ⋆ eo)), with
  [a ⋆ b]_k = Σ_i a_i b_(k+i mod d).
- **Compression**: "circular correlation can be interpreted as a
  compression of the tensor product", O(d) memory and O(d log d) time
  against O(d²) for RESCAL's tensor product.
- **Asymmetry**: "Correlation, unlike convolution, is not commutative ...
  Non-commutativity is necessary to model asymmetric relations".
- **Memory and learning**: the difference from associative memory "is
  that it does not only memorize, but it generalizes in a well defined
  way".
- **Results** (Table 2a, filtered MRR): WN18, HolE 0.938 against RESCAL
  0.890 and TransE 0.495; FB15k, HolE 0.524 against TransE 0.463, though
  TransE leads on Hits@10 (74.9 against 73.9).

## Standing in the record

Filed with the optics and holography batch of 2026-11-15. A's description,
circular correlation modelling interactions among subject, relation and
object with "competitive" link prediction, is fair but loose: correlation
combines subject and object, and the relation enters by a dot product; and
the paper claims more than competitiveness. The baselines are the authors'
reimplementations.

Its neighbour in the record is Knowledge Sheaves, [LIT-232](LIT-232.md), whose
coboundary account ([THEORY-299](../theory.d/THEORY-299.md)) covers the translational family (TransE,
TransR, RotatE); HolE is a bilinear, compressed-tensor model of a
different family. Its bearing on [CLAIM-182](../claims.d/CLAIM-182.md) is the one drawn under Plate,
[LIT-tmpq18t6](LIT-tmpq18t6.md): the relation vector acts as a key reading one relation from
a compressed representation; HolE adds that the store is learned, not
written.
