---
status: Read
paper: LIT-tmp8hsmf
title: 'Learning to (Learn at Test Time)'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from the arXiv v4 PDF (31 Aug 2025, 33 pp.). Sections 1–5 read
    in full, with the proofs of Theorems 1 and 2 followed, the dual-form
    derivation of §2.5 checked for the linear case, and Tables 1–2. The
    appendices (the dual form for nonlinear f, the Nadaraya–Watson
    background, experiment details and the full Books results) were looked
    over, not read. Perplexity curves are read from the text's statements,
    not from the plots.
date: '2026-10-09'
summary: >-
  Recasts a sequence-modelling layer as a learner trained on the sequence
  it reads: hidden state as inner-model weights, update as a gradient step
  on a learned self-supervised loss. Proves that the linear, batch-GD case
  is linear attention and that a Nadaraya–Watson inner learner is softmax
  attention; shows TTT-Linear and TTT-MLP use long context better than
  Mamba at up to 1.3B parameters.
---

<!-- inactive-ok-file: THEORY-tmpllqzv — Proposed; the account this reading supports -->

# NOTE-tmpchl3b: Learning to (Learn at Test Time)

## Contribution

A general framework in which any learner (a model and an optimiser, or a
nonparametric method) induces a sequence-modelling layer, by treating the
sequence so far as the learner's training set. Within it, the authors
prove that linear attention and softmax self-attention are two particular
learners, and build two new layers, TTT-Linear and TTT-MLP, whose inner
models are a linear map and a two-layer MLP updated by mini-batch gradient
descent. The authors note the linear-hidden-state case was already
DeltaNet's; their addition is the framework for arbitrary inner models.

## Key insight

The difference between a layer that "remembers the context" and one that
"learns from the context" is a difference of learner, not of kind. Self-
attention is a nonparametric learner: its training step appends the token
to a list, and its prediction smooths over the list. A TTT layer is a
parametric learner: its training step compresses the token into weights.
Both are learning on the context at test time.

## Assumptions

- Autoregressive sequence layer, one token at a time; hidden state W_t of
  fixed size for parametric learners.
- Inner loss: multi-view reconstruction ‖f(θ_K x_t; W) − θ_V x_t‖², with
  θ_K, θ_V, θ_Q low-rank projections learned in the outer loop.
- Theorem 1: f(x) = Wx, batch gradient descent (all gradients taken at
  W₀), η = 1/2, W₀ = 0, and linear attention in its simplest form (no
  normaliser, no feature map).
- Theorem 2: Nadaraya–Watson with kernel κ(x, x′) ∝ exp((θ_K x)ᵀθ_Q x′)
  and labels θ_V x_s.
- Experiments: Pile (2k, 8k) and Books3 (1k–32k), 125M–1.3B parameters,
  Chinchilla recipe as in the Mamba paper, Llama tokenizer, mostly the
  Mamba backbone.

## Key results

- **Theorem 1.** ∇ℓ(W₀; x_t) = −2(θ_V x_t)(θ_K x_t)ᵀ; with batch GD and
  η = 1/2, W_t = Σ_{s≤t} (θ_V x_s)(θ_K x_s)ᵀ and z_t = W_t θ_Q x_t, linear
  attention. Checked.
- **Theorem 2.** Substituting the kernel and labels into the
  Nadaraya–Watson estimator gives softmax attention. Checked; the proof is
  a substitution.
- **Table 1** (125M, Pile): linear attention 15.91 → improved 15.23 → TTT
  equivalence 15.23 → learnable W₀ 15.27 → LN and residual in f 14.05 →
  mini-batch TTT 12.35 → learnable η 11.99 → Mamba backbone 11.09.
- **Figure 7.** Smaller inner mini-batch b improves perplexity (more
  inner steps); b = 16 chosen for speed.
- **§3.1–3.2.** At 2k context TTT-Linear, Mamba and Transformer are
  comparable; at 8k (Pile) and 32k (Books) both TTT layers beat Mamba; the
  advantage widens with context. Transformer finetuned for long context is
  the strongest baseline at 32k but costs more FLOPs.
- **Figure 2 (right).** Perplexity by token index keeps falling to 32k
  for TTT layers and the Transformer, plateaus after 16k for Mamba.
- **§3.3.** Per-token latency roughly constant in context for TTT and
  Mamba, linear for the Transformer; TTT-MLP's memory I/O remains a
  problem.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A TTT layer with linear inner model and batch GD is linear attention | strong (proof) | Theorem 1, checked |
| C2 | Softmax self-attention is a TTT layer whose inner learner is Nadaraya–Watson kernel regression | strong (proof) | Theorem 2, checked |
| C3 | Mini-batch inner updates and LN/residual in f account for most of the gain over linear attention | moderate | Table 1, one size |
| C4 | TTT layers use long context better than Mamba at these scales | moderate | Figures 2, 10, 11; four sizes, two datasets |
| C5 | The advantage grows with context length beyond what was tested | weak | extrapolation in §5 |
| C6 | Human learning is more like TTT's inner loop than like i.i.d. training | not supported | a motivation in §5, not argued |

## Method

The TTT layer: for each token, take a gradient step of the inner model on
the reconstruction loss, then predict with the updated weights. For
throughput, gradients within a mini-batch of b tokens are all taken at the
last weights of the previous mini-batch and accumulated by cumulative sum;
the "dual form" computes the end-of-batch weights and all outputs by
matrix products without materialising per-token gradients. The outer loop
trains everything else by ordinary next-token prediction.

## Concepts

- **TTT layer**: a sequence layer whose state is a learner's internal
  storage, whose update rule is the learner's train step and whose output
  rule is its predict step.
- **inner loop / outer loop**: training W on the sequence (per sequence,
  at test time too) / training θ on the dataset.
- **training, label and test views**: θ_K x, θ_V x, θ_Q x.
- **parametric / nonparametric learner**: compresses data into W / keeps
  the data (here, the context) and predicts from it directly.
- **dual form**: the matmul formulation within a mini-batch.

## Connections

The TTT idea is Sun et al. (2020) for vision; the autoregressive version
for video is the closest predecessor. TTT layers are fast-weight
programmers in Schmidhuber's sense, and DeltaNet is TTT-Linear with
b = 1 and no LN or residual. Theorem 1 is the identity that von Oswald et
al. (LIT-tmp2vilw) use in the other direction, through Schlag et al.
(2021): linear attention computes a gradient-step update. Akyürek et al.
(LIT-tmp686hl) use "test-time training" for something else: a temporary
LoRA update of the language model's own weights on the demonstrations.

## Bearing on the record

- **THEORY-tmpllqzv.** Theorems 1 and 2 are the second source of that
  account. In a TTT layer the boundary between "the context" and "the
  interpreter's parameters" is drawn by the authors' choice of learner:
  the same sequence is a list the layer stores (attention) or a training
  set the layer compresses into weights (TTT), and in the linear case the
  two give identical outputs. What differs is the state kept and its
  size, not whether learning occurs.
- The inner weights W are per-sequence and discarded; the outer
  parameters persist. So in this architecture "changing the interpreter"
  splits in two: a per-sequence change that is learning and yet as
  transient as a context, and a persistent change made only in training.
- No instruction for practice is drawn here; the architectural claims
  are the anthology's to weigh (`anthology-candidate`).

## Limitations

- Theorem 1 holds only for batch gradient descent from W₀ = 0 with the
  simplest linear attention; the proposed layers use mini-batch updates,
  learned W₀ and LN, and are not equivalent to attention.
- Scales up to 1.3B parameters and 32k context; no hybrid architectures.
- No clean scaling-law fit; comparisons are by connected points.
- Wall-clock cost of TTT-MLP is unresolved, as the authors say.

## Open questions

- For which inner learners other than these two does an attention-like
  closed form exist?
- What does an inner model of fixed size lose relative to storing the
  context, and can it be stated as a rate–distortion trade-off over the
  sequence? The paper frames the hidden state as a compression heuristic
  but does not measure what is lost.
