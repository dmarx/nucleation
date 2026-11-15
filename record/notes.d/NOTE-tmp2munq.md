---
status: Read
paper: LIT-tmpxroua
title: 'Ramsauer et al. — Hopfield networks is all you need'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 from arXiv:2008.02217v3 (28 April 2021), from
    arxiv.org/pdf/2008.02217v3, text by pdftotext (which reported an xref
    error and rebuilt the file; the text is complete). Read in full: the
    main text, §§1–5 (pp. 1–10): the energy, the update rule, Theorems 1–5,
    metastable states, the identity with attention, the three Hopfield
    layers, the experiments and the conclusion. Skipped: the roughly
    90-page appendix, with the proofs (A1–A9 and their lemmas), the BERT
    operating-class figures (A.5.1.4) and the experimental details; the
    theorems are carried as stated. The reader's draft was turned into this
    note by the filer, who rechecked every quote below against the
    downloaded text; all were found.
date: '2026-11-15'
summary: >-
  A continuous modern Hopfield network with energy −lse(β, Xᵀξ) + ½ξᵀξ +
  const and update ξ ← X softmax(βXᵀξ), proved to converge to stationary
  points, to store exponentially many random patterns on a sphere and to
  retrieve a well-separated pattern in one step; one update through learned
  projections at β = 1/√d_k is softmax attention. The record's first
  Hopfield derivation of attention, beside the SDM one ([NOTE-242](NOTE-242.md)).
---
<!-- inactive-ok-file: THEORY-1030 — Proposed; the FFN-memory reading this one bears on by construction, cited as open -->

# NOTE-tmp2munq: Ramsauer et al. — Hopfield networks is all you need

## Contribution

A continuous-state generalization of the exponential-interaction dense
associative memory (Demircigil et al.), with an energy, an update rule
and proofs of convergence, capacity and one-step retrieval. Its update rule
is, for one step and under a choice of projections and β, the attention
operation of transformers, which lets the authors read attention heads as
retrieving one pattern, an average of a few, or an average of all. They
package the rule as three layers (Hopfield, HopfieldPooling, HopfieldLayer).

## Key insight

Softmax attention is one step of energy descent in an associative memory
whose stored patterns are the keys: the query is the state, and the
softmax weights say how many stored patterns the step lands near.

## Assumptions

- Stored patterns lie on a sphere of radius M; the capacity theorem
  assumes random patterns, and one-step retrieval assumes well-separated
  ones (separation ∆i large).
- The identity with attention is for a single update, with projections
  W_K, W_Q, W_V, β = 1/√d_k and a transpose convention; the model's own
  dynamics iterate, a transformer layer takes one step.

## Key results

- **Energy and update** (§2, Eq. 3): "ξ new = f (ξ) = Xp = Xsoftmax(βX T ξ)"
  (extraction spacing kept).
- **Convergence** (Theorems 1–2): "The update rule Eq. (3) converges
  globally", to "stationary points (local minima or saddle points)", by
  the concave–convex procedure.
- **Capacity** (Theorem 3): with probability 1 − p, "the number of random
  patterns that can be stored is" at least √p c^((d−1)/4); proved "for
  c ≥ 3.1546" at d = 20 and "c ≥ 1.3718" at d = 75 (p = 0.001).
- **One-step retrieval** (Theorems 4–5): the distance after one update "is
  exponentially small in the separation ∆i".
- **Attention** (§2, Eq. 10): "The Hopfield network update rule is the
  attention mechanism used in transformer and BERT models"; "In the
  transformer self-attention R = Y", with W_K W_V replaced by W_V.
- **Abstract**: "The new update rule is equivalent to the attention
  mechanism used in transformers."
- **BERT heads** (§4): "the attention heads of transformer and BERT models
  are predominantly in metastable states"; averaging over very many
  patterns "is abundant in lower layers", and near-single-pattern
  retrieval "is predominant in the last layers".
- **HopfieldLayer** (§3): with learned stored patterns it "can substitute a
  fully connected layer"; following Krotov and Hopfield (2020), the
  patterns "can be interpreted as weights from the state (query) to hidden
  neurons that have a softmax activation function".
- **Classical capacity, cited** (§1): for the standard model with Hebbian
  storage, Cd/log(d) random patterns (McEliece et al., 1987), and, "allowing
  small retrieval errors, the storage capacity is about 0.138d (Crisanti
  et al., 1986; Hertz et al., 1991; Torres et al., 2002)".
- **Applications** (§4, Table 1): DeepRC reaches an AUC of 0.832 ± 0.022 on
  real immune repertoires; new state of the art reported on several
  multiple-instance and drug-design benchmarks.

## Concepts

- **Modern Hopfield network** — here, the authors' continuous model with
  log-sum-exp energy, not Krotov and Hopfield's polynomial or Demircigil's
  binary one.
- **Metastable state** — a fixed point near an average of a subset of the
  stored patterns.
- **Separation ∆i** — how far pattern i stands, in dot product, from the
  others; it sets one-step retrieval.
- **β** — inverse temperature; at large β retrieval is of single patterns,
  at small β of the global average.

## Connections

- **[LIT-269](../literature.d/LIT-269.md), [NOTE-242](NOTE-242.md), [THEORY-697](../theory.d/THEORY-697.md)** (attention as sparse distributed
  memory): a parallel derivation of attention from an associative memory.
  [NOTE-242](NOTE-242.md) compares its trained-β pattern with this paper's BERT analysis
  and says the record held no Ramsauer paper; this reading fills that gap.
- **[LIT-918](../literature.d/LIT-918.md), [THEORY-272](../theory.d/THEORY-272.md)** (Hopfield 1982): the ancestor model, with the
  quadratic energy this paper replaces by an exponential one. It does not
  restate or test Hopfield's simulations.
- **[LIT-tmpp9nhx](../literature.d/LIT-tmpp9nhx.md)** (Schlag, Irie and Schmidhuber): cites this paper for the
  Hopfield reading of attention and treats softmax attention as the
  infinite-capacity end of the memory scale linear attention sits on.
- **[LIT-tmpi44jr](../literature.d/LIT-tmpi44jr.md)** (Ravfogel et al.): a memory of facts in trained
  weights or embeddings, where this one is a memory of the context.

## Bearing on the record

- **[QUESTION-201](../questions.d/QUESTION-201.md)**: a lead, not an answer. The introduction cites a
  large-N capacity of "about 0.138d" for Hebbian storage allowing small
  retrieval errors, and Cd/log(d) for error-free recall. Both are other
  authors' results, unread here; they agree with [THEORY-272](../theory.d/THEORY-272.md)'s small-N
  0.15N and say where the large-N answer is to be read (Crisanti et al.
  1986; Hertz et al. 1991; McEliece et al. 1987).
- **[THEORY-272](../theory.d/THEORY-272.md)**: no change. Context only.
- **[THEORY-1030](../theory.d/THEORY-1030.md)**: by construction only. The HopfieldLayer is a
  softmax-normalized version of the memory form FF(x) = f(x·Kᵀ)·V that
  [THEORY-1030](../theory.d/THEORY-1030.md) reads into trained FFN units. That the form can serve as a
  memory is shown; that trained FFN units use it so is not touched.
- **[NOTE-242](NOTE-242.md)**: its sentence that the record holds no Ramsauer paper is now
  out of date.
- **[THEORY-1011](../theory.d/THEORY-1011.md), [THEORY-1024](../theory.d/THEORY-1024.md), [THEORY-021](../theory.d/THEORY-021.md), [THEORY-1036](../theory.d/THEORY-1036.md), [QUESTION-275](../questions.d/QUESTION-275.md),
  [CLAIM-407](../claims.d/CLAIM-407.md)**: no bearing. Storage here is of separated patterns, not of
  features in superposition or of facts in weights.

## Limitations

- The proofs were not checked here.
- The capacity and retrieval results are for random or well-separated
  patterns on a sphere, not for trained keys.
- The identity says what one attention step computes. It does not show
  that trained transformers' keys act as stored attractors.
- The BERT classification is descriptive, and its 0.90 softmax-mass
  threshold and class boundaries are the authors' choices.
- The venue is unconfirmed (see [LIT-tmpxroua](../literature.d/LIT-tmpxroua.md)).
