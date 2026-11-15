---
status: Read
paper: LIT-tmpp9nhx
title: 'Schlag, Irie and Schmidhuber — Linear transformers are fast weight programmers'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 from arXiv:2102.11174v3 (9 June 2021), from
    arxiv.org/pdf/2102.11174v3, text by pdftotext: §§1–6, the whole main
    text, with Tables 1–3. Skipped: appendices A–F (the derivations of the
    update rule and normalisation in A.1–A.2, the comparison with Peng et
    al.'s gated rule in B, the DPFP code, learning curves, and the
    translation and language-model setups). The extraction garbles some
    equations; Eqs. 20–28 were read from the reflowed text. The reader's
    draft was turned into this note by the filer, who rechecked every quote
    below against the downloaded text; all were found (one, "the modern
    Hopfield network", is split in the extraction by a footnote mark). The
    gradient-step reading of Eq. 24 under Bearing on the record is the
    filer's arithmetic, not the paper's. The filer also added §6.1.2,
    which the reader's draft left out: the synthetic comparison of update
    rules is set within capacity, so the delta rule's synthetic advantage
    is in reassigning keys, not past the d_dot load.
date: '2026-11-15'
summary: >-
  Linear attention, with or without a kernel φ, is an outer-product fast
  weight programmer apart from normalisation: a fast weight matrix summing
  v ⊗ φ(k), read by the query. Hence at most d_dot associations without
  crosstalk, shown on synthetic retrieval, and a delta-rule write
  W ← W + β(v − v̄) ⊗ φ(k) with a learned rate β, which helps on
  WikiText-103 in an overcapacity regime. Defines the delta-rule layer
  QUESTION-159 asks about.
---
<!-- inactive-ok-file: THEORY-1030 — Proposed; the FFN-memory reading this one shares only an algebraic form with, cited as open -->

# NOTE-tmpss2fb: Schlag, Irie and Schmidhuber — Linear transformers are fast weight programmers

## Contribution

It makes explicit, and reviews from Katharopoulos et al. (2020) and Ba et
al. (2016), that linear attention is a fast weight programmer of the early
1990s: a slow net emits keys and values, each step adds their outer
product to a fast weight matrix, and the query reads it. From that view it
draws a capacity limit, proposes a delta-rule write with a learned
write-strength, sum normalisation, and a deterministic feature map (DPFP)
that raises the key dimension d_dot.

## Key insight

Linear attention is a memory written during the forward pass, one outer
product per token, and like any such memory it fills up: past d_dot
associations the keys cannot be orthogonal and retrieval interferes. A
memory that can overwrite what a key already holds does better there.

## Assumptions

- Causal attention with the softmax removed, or replaced by a kernel
  φ(k)ᵀφ(q). Softmax attention itself is not covered; the paper treats it
  as a memory whose capacity is infinite.
- Retrieval by one matrix–vector read, with interference whenever keys
  are not orthogonal.

## Key results

- **The plain identity** (§3.1, Eqs. 10–11): W(i) = W(i−1) + v(i) ⊗ k(i),
  y(i) = W(i) q(i); with softmax removed, self-attention matches the FWP
  of Eqs. 1–3 "where the activation function σ is the identity function
  and without query projection".
- **With a kernel** (§3.2, Eqs. 17–19): adding the normaliser z(i) =
  z(i−1) + φ(k(i)) gives "a Fast Weight Programmer (Sec. 2) with
  normalisation. Hence, the core of linear Transformer variants are outer
  product-based Fast Weight Programmers."
- **The claim in brief** (§1): "the formal equivalence of this family of
  linear Transformers and the Fast Weight Controllers" of 1991–93, "apart
  from normalisation".
- **Capacity** (§4.1): "With keys embedded in a ddot space, there cannot be
  more than ddot orthogonal vectors. That is, storing more than ddot
  associations will result in a retrieval error." Tied to Smolensky's
  tensor-product crosstalk.
- **On synthetic retrieval** (§6.1.1, Fig. 2): "Linear-Attention begins to
  accumulate errors with 60 or more associations" at d_dot = 64; DPFP-1/2/3
  degrade near 128, 256 and 384. "Softmax attention is outperforming all"
  feature maps, "although it struggles to fully converge with more than 500
  keys".
- **Softmax as the limit** (§5.3, FAVOR+): with m random features the
  memory's capacity is still limited, "and equals the infinite capacity of
  the softmax memory only when m goes to infinity".
- **The delta rule** (§4.2, Eqs. 20–25): v̄(i) = W(i−1)φ(k(i)) is the value
  the memory now pairs with k(i); β(i) = σ(W_β x(i)); W(i) = W(i−1) +
  β(i)(v(i) − v̄(i)) ⊗ φ(k(i)) (Eq. 24); y(i) = W(i)φ(q(i)). It "is
  effectively a delta rule with a dynamic learning rate", after Widrow and
  Hoff (1960). W(0) = 0.
- **Update rules compared** (§6.1.2): keys sampled with replacement, so
  a key is reassigned and "the model is required to update its finite size
  memory"; the setting "does not exceed the capacity of DPFP-1", and the
  result is said to be "independent of the capacity regime" (Appendix D.2,
  unread). The delta rule with normalisation is compared with the sum rule
  and two earlier rules; the plot values were not read.
- **Language modelling** (§6.3, Table 2, WikiText-103, small
  configuration, overcapacity): test perplexity 38.3 → 35.5 for the Linear
  Transformer and 39.6 → 37.2 for the Performer when the sum rule becomes
  the delta rule; softmax Transformer 34.1. The Performer's capacity was
  matched to the Linear Transformer's "even though this limits
  performance".
- **Translation** (§6.2, Table 1, WMT14 En–De): DPFP beats the Linear
  Transformer and Performer at small d_dot; the standard Transformer has
  27.7 test BLEU.

## Concepts

- **Fast weight programmer (FWP)** — a slow net that writes, at each step,
  the weights of a fast net, here by outer products of generated keys and
  values.
- **d_dot** — the dimension of the key feature space φ(k); the number of
  orthogonal keys, so the capacity.
- **Overcapacity regime** — sequence length L exceeding d_dot.
- **Write-strength β** — the model-generated rate at which a new value
  replaces the one currently stored under its key.
- **DPFP** — deterministic parameter-free projection, a feature map with
  d_dot = 2·d_key·ν.

## Connections

- **LIT-tmpxroua** (Ramsauer et al.): cited in §1, the Transformer's
  self-attention "was recently connected to the modern Hopfield network
  (Ramsauer et al., 2021)". Together they place linear and softmax
  attention on one scale of memory capacity.
- **LIT-918** (Hopfield 1982): placed among the outer-product memories of
  Hebb, Kohonen and Palm whose authors "described pre-wired rules to
  associate given patterns"; FWPs learn which patterns to write. The
  d_dot limit is the same kind of crosstalk limit as Hopfield's, derived
  for orthogonal-key reads, not for attractor recall.
- **LIT-792, NOTE-621** (von Oswald et al.) and **LIT-801, NOTE-620** (TTT):
  both use the identity this paper makes explicit; NOTE-621 says it rests
  on this paper.

## Bearing on the record

- **QUESTION-159**: the bearing that matters. The question asks whether an
  exact train-then-predict identity holds "for further sequence-layer
  classes such as delta-rule or mini-batch inner updates". This paper
  defines the delta-rule layer (Eqs. 20–25). It does not state such an
  identity, and the appendix derivations (A.1) were not read. By the
  filer's arithmetic, not the paper's: with v̄(i) = W(i−1)φ(k(i)), the
  increment in Eq. 24 is −β(i) times the gradient in W of
  ½‖v(i) − Wφ(k(i))‖² at W(i−1), so the unnormalised layer's output
  y(i) = W(i)φ(q(i)) is the prediction at φ(q(i)) of a linear model
  trained from zero by one online gradient step per context token, with
  the learned rates β(i). That is a train-then-predict description by
  construction, sequential rather than one batch step, and the normalised
  version (Eqs. 27–28) is not covered by it. Whether that counts as the
  "exact identity of this kind" QUESTION-159 asks for is the owner's call.
- **THEORY-169**: the identity it holds for unnormalized linear attention
  is the one this paper reviews, apart from the batch-gradient framing.
- **THEORY-1030**: algebraic kinship, no evidence. Geva et al.'s memory is
  held in trained weights; this one is written from the context's
  activations and discarded after the sequence. Both are sums of key–value
  outer products, and evidence about one says nothing of the other.
- **THEORY-272**: context only, as under Connections.
- **THEORY-021, THEORY-1036**: indirect at most. The overcapacity regime is
  where crosstalk appears, but the paper does not speak of superposition.
- **THEORY-1011, THEORY-1024, QUESTION-275, CLAIM-407**: no bearing.

## Limitations

- The capacity limit is argued intuitively, by appeal to Smolensky, and
  shown on toy retrieval; it is not proved for trained linear Transformers.
- The language-model results are from 40M- and 90M-parameter models in a
  configuration chosen to be overcapacity.
- The equivalence says what linear attention computes, not what trained
  models store.
- The venue is from the PDF footer only (see LIT-tmpp9nhx).
