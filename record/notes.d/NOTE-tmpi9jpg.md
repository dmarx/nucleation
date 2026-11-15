---
status: Read
paper: LIT-tmp0q2ls
title: 'Loshchilov et al. — nGPT'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 from arXiv:2410.01131v2 (23 April 2025), from
    arxiv.org/pdf/2410.01131v2, text by pdftotext -layout. Read in full:
    §§1–5 (pp. 1–10). Read in the appendix: A.1 (SiLU rescaling), A.2
    (sign of the eigen learning rates), A.3 (comparison with ReZero), A.5
    (time per step). Skipped: A.4 (Riemannian extension), A.6–A.7 (setup,
    learning-rate sweeps), A.8 (context extrapolation) and A.9
    (ablations), apart from the main text's summary of the last two.
    Figure values are from the text, not read off the plots. The reader's
    draft was turned into this note by the filer, who rechecked every
    quote below against the downloaded text; all were found.
date: '2026-11-15'
summary: >-
  A GPT with every embedding, hidden state and weight row on the unit
  hypersphere, each residual sum replaced by a learned per-dimension step
  toward the block's normalized output and a renormalization, read as an
  optimizer step on the sphere. At 0.5B and 1B on OpenWebText it reaches
  GPT's loss in 4–20 times fewer tokens, at 60–80% more time per step. An
  architecture paper; no claim about memory or about trajectories across
  inputs.
---

# NOTE-tmpi9jpg: Loshchilov et al. — nGPT

## Contribution

An architecture with no RMSNorm or LayerNorm in which hidden states,
embeddings and weight rows all lie on one hypersphere, with learned
scaling vectors (s_qk, s_u, s_ν, s_z) putting back the magnitude
information normalization removes, and with the residual sum replaced by
an interpolation toward each block's normalized output. The authors read
each layer as two steps of a variable-metric optimizer on the sphere, an
interpretation, not a proof.

## Key insight

If the state lives on a sphere, a layer can only move it along the sphere,
and the size of each move can be a learned, per-dimension step size;
training then converges in far fewer tokens.

## Assumptions

- Two model sizes (0.5B, 1B), one corpus (OpenWebText), and a GPT
  baseline at its best learning rate. Speed is counted in tokens or
  iterations, not wall-clock time.
- The optimizer reading takes the block's output as a target point b and
  g = a − b as a gradient; that identification is stipulated.

## Key results

- **Update** (§2.2.2, Eqs. 10–11): h ← Norm(h + α_A(h_A − h)), h ←
  Norm(h + α_M(h_M − h)), with h_A = Norm(ATTN(h)) and h_M = Norm(MLP(h)).
  "We denote α as eigen learning rates (from the German word eigen,
  meaning "own," ...)". The block output is "the point suggested by the
  attention or MLP block".
- **Speed** (§3.1, Fig. 2): "Training the 0.5B and 1B nGPT models is
  approximately 4x, 10x, and 20x faster at context lengths of 1k, 4k, and
  8k tokens, respectively." At 1B and 4k, "nGPT achieves the same
  validation loss that GPT reaches only after 200k iterations", after 20k.
- **Cost** (footnote 3, A.5): "The time cost per step for nGPT is
  approximately 80% higher with 4k context length, and 60% higher with 8k
  context length."
- **Downstream** (§3.1, Fig. 3): the acceleration shows in task
  performance too, with some saturation in the longest runs.
- **Learned steps** (§3.2, Fig. 6): "the network learns to take only
  modest steps (20%-30%)"; mean α_A 0.25 at 0.5B and 0.20 at 1B, α_M 0.37
  and 0.32.
- **Conditioning** (§3.2, Figs. 4–5): GPT's attention matrices have far
  higher condition numbers and "degenerate into lower-rank matrices";
  nGPT's embeddings "are not uniformly distributed across the hypersphere"
  but cluster.
- **Sign of α** (A.2): unconstrained, "we obtain experimental results
  which are the same", since the sign can be absorbed into W_o.

## Concepts

- **Eigen learning rates** — the learned per-dimension vectors α_A, α_M
  setting how far each block moves the state.
- **LERP / SLERP** — linear and spherical interpolation; the update is
  LERP followed by renormalization, approximating SLERP.
- **Retraction** — Norm read as mapping a step back onto the sphere.

## Connections

- **LIT-792** (von Oswald et al.): nGPT cites the line on transformers as
  implicit gradient-descent meta-optimizers and claims to make that
  process explicit in its architecture. That is an analogy built in, not
  the in-context identity LIT-792 proves.
- **LIT-269, NOTE-242**: hold QK-norm (Henry et al.), which nGPT's
  normalized attention logits (Eqs. 15–16) closely resemble.

## Bearing on the record

- **No direct bearing** on THEORY-1030, THEORY-1011, THEORY-1024,
  THEORY-272, THEORY-021, THEORY-1036, QUESTION-275 or CLAIM-407. It
  makes no claim about where facts are stored, associative memory,
  superposition, circuit development or coarse-graining.
- **A's branched-flow disclaimer** holds: the paper does not mention
  branched flow, and analyses no trajectories across inputs.
- Its practical recommendation, normalize everything for faster training,
  is an instruction for machine-learning practice, which belongs to the
  Anthology (hence the anthology-candidate flag on LIT-tmp0q2ls).

## Limitations

- Two scales, one dataset, one baseline recipe; the authors note
  saturation in the longest runs and call for "larger network sizes,
  real-world datasets".
- The optimizer interpretation is a reading of the architecture; nothing
  tests whether block outputs behave like gradients of any objective.
- The speed-up is in tokens, partly offset by per-step overhead the paper
  ascribes to unfused kernels.
