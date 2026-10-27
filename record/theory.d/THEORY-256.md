---
number: 256
status: Active
formerly:
- THEORY-tmpbx1ck
title: "When a sequence generator's latent dynamics factor as a tensor product, its predictive state embeds losslessly and linearly in orthogonal per-factor subspaces of total dimension Σ(d_n − 1); 4-layer GPT-2-style transformers trained by next-token prediction on five Mess3 and Bloch Walk factors settle near that dimension, in per-factor subspaces that are linearly independent and approximately orthogonal in their leading components, and under the token noise tested reach it first even when noise makes it lossy"
version: 3
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted from Proposed to Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-256.yaml, batch 019, ADR-047).
    The theorem is re-derived in the note of 2026-10-19 below. The
    empirical clauses rest on one study, LIT-986, which NOTE-758 read in
    full, and whose numbers are stated in its text. Under ADR-047 v3 that
    suffices once the title claims no more than was measured. So "small
    transformers ... on such processes" now names the architecture and the
    five factors tested; "approximately orthogonal subspaces" now says what
    was shown, linear independence and approximate orthogonality in the
    leading components; and the noise clause names the construction
    tested. The promote_when asked for a replication. It moves, unchanged,
    to QUESTION-157.
- version: 3
  date: '2026-10-20'
  note: >-
    The narrowing-loss sweep (batch 070, ADR-047 v4) filed THEORY-808,
    Proposed, to carry what the narrowing dropped. This entry's status,
    title and claims are unchanged; a dated note says what moved.
tags:
- representation-learning
- probabilistic-modeling
date: '2026-10-14'
source:
- LIT-986
summary: >-
  Shai et al. (2026), [LIT-986](../literature.d/LIT-986.md), read in [NOTE-758](../notes.d/NOTE-758.md). The lossless
  embedding is an elementary theorem (Prop. 2.2, Thm 2.3, App. A). The
  rest is experiment on five synthetic factors: about 10 effective
  dimensions against 242 for the joint state, approximate orthogonality in
  the first two components, and under token noise a collapse to the
  factored form before expansion. It does not show that the preference is
  architectural rather than a feature of training, a question the paper
  leaves open, and it varies neither the objective nor the data domain.
extended_by:
- THEORY-808
bears_on:
- QUESTION-060
---
<!-- inactive-ok-file: THEORY-808 — Proposed; the wider claim this entry's narrowing dropped, filed beside it and cited as open -->
<!-- inactive-ok-file: THEORY-274 — Proposed; accounts on the same question, open -->

# THEORY-256: When a sequence generator's latent dynamics factor as a tensor product, its predictive state embeds losslessly and linearly in orthogonal per-factor subspaces of total dimension Σ(d_n − 1); 4-layer GPT-2-style transformers trained by next-token prediction on five Mess3 and Bloch Walk factors settle near that dimension, in per-factor subspaces that are linearly independent and approximately orthogonal in their leading components, and under the token noise tested reach it first even when noise makes it lossy

## Source

Shai, Amdahl-Culleton, Christensen et al. (2026), [LIT-986](../literature.d/LIT-986.md), read in
[NOTE-758](../notes.d/NOTE-758.md): Proposition 2.2, Theorem 2.3, App. A.3–A.5 for the theory;
§§4.1–4.4, App. C.2–C.4, D.1–D.6 and H for the experiments.

## What was actually shown

**The theory.** For a generalized hidden Markov model whose token-labelled
operators are tensor products, T^(x) = ⊗_n T_n^(x), a product predictive
vector stays a product after every token (Prop. 2.2, eq. 11). The set of
product states has intrinsic dimension Σ_n(d_n − 1), and an explicit linear
map, partial traces followed by orthogonal per-factor embeddings, carries it
invertibly into a direct sum (Thm 2.3; eq. 13, 17). Off that manifold the
map loses the total correlation D[η ‖ ⊗η_n] (eq. 16). Dependency chains
between factors are covered, since only the operators must factor.

**The experiments.** Three Mess3 and two Bloch Walk factors, 432 product
tokens, a 4-layer GPT-2-style transformer (d_model 120, also 480):

- independent and chained factors: effective dimension at 95% variance
  falls to about 10–11, against 242 for the joint state, even at
  d_model = 480; each factor's belief is linearly recoverable;
- vary-one subspaces: per-factor dimensions sum to 14 against a union of
  12, and pairwise overlaps fall in the first two components only;
- token noise ε from 0.001 to 0.5: activations collapse to about 10
  dimensions within hundreds of steps for every ε, then expand under
  continued training, the more so the larger ε;
- RNNs and LSTMs: closer to factored than joint, but less sharply.

What could have come out otherwise: a model with ample width could have
used the joint representation, which the objective never penalizes, or
gone straight to it when factoring was lossy. Neither happened.

## What this does not say

- **Not that the architecture is the cause.** The paper names an
  "inductive bias of the architecture" but its own appendix (D.4) leaves
  open whether the effect comes from "training dynamics or inductive
  bias". Optimizer, initialization and width were not varied to separate
  them.
- **Not that cheapness beats the objective.** Under heavy noise the
  converged representation leaves the factored form (App. D.5, Fig. 12).
  Cheapness predicts what training reaches first; the objective still acts
  later.
- **Not orthogonality, strictly.** Dimension additivity shows linear
  independence of the factor subspaces; the overlap metric gives
  approximate orthogonality in two components per factor.
- **Not natural data.** Five small known processes, factors fixed by a
  product token code; whether factors are found in data without such
  structure is untested.
- **Not a measured fidelity cost.** The loss gap between factored and
  joint representations at each ε is argued from the construction, not
  reported for the trained models.

## Connections

- **[QUESTION-060](../questions.d/QUESTION-060.md).** An answer in part: a family with known relevant
  variables in which the learned variables coincide with them when
  factoring is lossless, and in which, when it is lossy, the variables
  reached first are the cheap ones rather than the objective's optimum. It
  varies the data, not the objective or the architecture, so it does not
  apportion the two the question names.
- **[THEORY-206](THEORY-206.md).** On the representational side, products of many inputs
  are costly for a shallow network; here a tensor product of beliefs is
  replaced by a sum, a case of the same cheapness shaping what is kept.
- **[THEORY-197](THEORY-197.md).** The contrasting case: there the objective fixes what is
  kept against a formal match; here the training path holds a
  representation the objective does not favour.
- **[THEORY-274](THEORY-274.md).** A second case in which what training reaches is not
  fixed by the objective's optimum alone.

## Note of 2026-10-19: the theorem, re-derived, and the narrowing

Written for the promotion audit's batch 019 ([ADR-047](../decisions.d/ADR-047.md)). It is also in
record/promotion-audit/decisions/THEORY-256.yaml.

Tokens are tuples x = (x_1, …, x_N), and the operators factor:
T^(x) = ⊗_n T_n^(x_n).

1. **Products stay products.** If η = ⊗_n η_n, then
   η T^(x) = ⊗_n (η_n T_n^(x_n)). The normaliser factors too:
   (⊗_n a_n)(⊗_n 1_n) = Π_n (a_n 1_n). So the updated predictive vector is
   ⊗_n η_n′, with η_n′ = η_n T_n^(x_n) / (η_n T_n^(x_n) 1_n). The start is
   a product as well: Σ_x T^(x) = ⊗_n Σ_{x_n} T_n^(x_n), whose stationary
   vector is ⊗_n π_n. By induction every predictive state is a product.
2. **Dimension.** Each factor lies in the affine hyperplane η_n 1_n = 1 of
   ℝ^{d_n}, of dimension d_n − 1. A product state is fixed by its factors.
3. **The embedding.** The partial trace η ↦ η_n contracts every other
   factor with its all-ones vector. It is linear, and it returns η_n
   exactly on product states. Coordinatise each hyperplane by an
   orthonormal basis of its direction space. The map to the direct sum of
   these coordinates is affine, injective on product states, and lands in
   mutually orthogonal blocks of total dimension Σ_n (d_n − 1). Off the
   product set the partial traces drop the correlations between factors,
   which is the loss the paper measures as total correlation.

The empirical clauses rest on [LIT-986](../literature.d/LIT-986.md) alone, which [NOTE-758](../notes.d/NOTE-758.md) read in full.
Its figures were read only through their captions, but the numbers these
clauses use are stated in the text: about 10–11 effective dimensions
against 242, per-factor dimensions summing to 14 against a union of 12,
and collapse to about 10 dimensions under every noise level. Under
[ADR-047](../decisions.d/ADR-047.md) v3 that one study carries a title that claims no more than it
measured. The title now names the architecture, the five factors, what
the subspace measurements show, and the noise construction. The
replication the promote_when asked for moves, unchanged, to
[QUESTION-157](../questions.d/QUESTION-157.md).

## Note of 2026-10-20: the wider claim, filed Proposed

Under [ADR-047](../decisions.d/ADR-047.md) v4 the narrowing-loss sweep (batch 070) filed [THEORY-808](THEORY-808.md)
as Proposed, extending this entry. It carries the general reading this
entry's title carried before batch 019 narrowed it: that transformers
trained by next-token prediction on factored processes in general learn
factored, approximately orthogonal belief representations of about the
factored dimension, and reach them first when factoring is lossy, as Shai et
al. present it. The architectural-bias reading ([NOTE-758](../notes.d/NOTE-758.md), C5) and
persistence at convergence under strong noise, which Fig. 12 contradicts,
are left out of it. This entry is its evidence and is not changed by the
filing.
