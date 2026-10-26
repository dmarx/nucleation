---
status: Read
paper: LIT-tmp01if4
title: 'Musat, Pimentel, Zucchet and Hofmann — Invariant learning dynamics of transformers in inductive reasoning tasks'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Read in full from the arXiv copy (arXiv:2607.11875v2, 14 July 2026,
    fetched from arxiv.org/pdf/2607.11875 on 2026-10-26), text extracted
    with pdftotext. v1 was not compared. Read: the abstract, §§1–6, and
    Appendices A (assumptions, the proof of Theorem 1 in six steps, the
    circuit-folding sketch A.4, the FFN and LayerNorm extension A.5), B
    (arbitrary relations), C (the geometry of the basis), D (training
    details, the ablation table, the proofs of Theorems 2 and 3), E (the
    competing-heads setup) and F (circuit detection, Algorithm 1, the two
    discovered circuits). The figures (1–7) were read from their captions
    and the text that describes them; the phase diagram of Fig. 4 and the
    coefficient curves of Figs. 3 and 6–7 were not seen as images. The
    gradient-confinement argument, the token and position commutants, and
    the dependence of confinement on the optimizer were checked by the
    record (THEORY-tmpdxhxm).
date: '2026-10-26'
summary: >-
  For a class of "block-list" next-token tasks that includes associative
  recall, k-hop induction and in-context n-grams, population gradient
  descent keeps an attention-only transformer's merged key–query and
  output weights in a subspace fixed by the data's token-relabelling and
  position-shift symmetries, whose coordinates are elementary actions
  ("attend to the previous position", "read the token retrieved by head
  1"). On it, a saturated in-weights circuit suppresses the in-context
  circuit's gradient by the fraction of data it does not solve, burstiness
  multiplies that gradient, initialization decides which of several
  induction circuits wins, and projecting a trained model onto the
  coordinates recovers its circuit, with "aiding" directions a head-level
  analysis would miss.
---
<!-- inactive-ok-file: THEORY-783 THEORY-tmpq4l9j CLAIM-367 CLAIM-263 CLAIM-tmpwr001 CASE-tmplcm41 THEORY-802 — Proposed; accounts and claims this reading bears on, cited as open, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-tmpe7b5o — Deferred; a work registered from the same exchange, cited as open -->

# NOTE-tmpcuw4h: Musat, Pimentel, Zucchet and Hofmann — Invariant learning dynamics of transformers in inductive reasoning tasks

## Contribution

It gives one theory of training dynamics for a family of inductive tasks
that earlier work treated one task at a time. Under its assumptions the
training trajectory of an attention-only transformer never leaves a
subspace of the key–query and output weights, the "Invariant Manifold of
Inductive Reasoning" (IMIR), fixed by the symmetries of the data. Each
coordinate of that subspace is one elementary action of one head, so the
dynamics of every component are tracked at once rather than one stage at
a time with the rest frozen. With it the paper proves how data statistics
set the competition between in-context and in-weights learning, shows
initialization choosing among competing induction circuits, and finds
circuits in trained models below the level of whole heads.

## Key insight

What gradient descent can build is limited by what the data cannot tell
apart. If relabelling the associated token pairs, or shifting every
block's position, leaves the data distribution unchanged, then the
expected gradient at a symmetric point is itself symmetric, and training
that starts symmetric stays so. The symmetric matrices are few: for
tokens, "match the same token" (I) and "match its partner" (C); for
positions, "match position j back" (powers of M). Composed through the
heads' write subspaces, these are the whole alphabet of reasoning circuits
for the class. A circuit is then a small set of coordinates, and circuits
interact by sharing coordinates or by contending for the same layers.

## Assumptions

- **Data** (Assumptions 1–3). Common tokens are correlated only through a
  set R of symmetric, balanced, non-overlapping pairs, and the
  distribution is unchanged under any permutation that fixes rare tokens
  and preserves R. Each block carries an independent, marginally uniform
  positional offset. Rare-token embeddings are resampled for every
  sequence ("lexinvariance"), with the common tokens' mean and second
  moment.
- **Architecture** (Assumptions 4–6). Attention only. Token and sinusoidal
  position embeddings orthonormal, equal-norm and centred. The merged
  product W = W_Qᵀ W_K is the learnable attention parameter. Each head's
  output–value map is a **fixed** isometry onto a write subspace
  orthogonal to the residual stream entering its layer and to the other
  heads' write subspaces, which needs a residual width d = Θ(H^L).
- **Dynamics.** Population (expected) gradient, gradient descent or flow.
  Learnable value maps (A.4) are "a sketch rather than a proven claim". The
  FFN and LayerNorm extension (A.5) is argued in the same way, with the
  FFN weights constrained to a matching structure.
- **Experiments.** Vanilla SGD on the simplified architecture for §§4.2
  and 4.3 (width 128 and 256, 16 common tokens), with fr = 0.9 in §4.2's
  main run (D.1) and fr = 1 in §4.3 (E.1). §5 uses AdamW at width 1024 on
  two-hop induction (F.1). §4.3 projects the weights onto a
  seven-dimensional sub-manifold after every step.

## Key results

- **Theorem 1 (gradient confinement) and Corollary 1 (invariant
  manifold).** Let S be the transformers with W^(ℓ,h) ∈ span(W_ℓ) and
  W̄ ∈ span(W̄), where W_ℓ = V_{1:ℓ−1}(T ∪ P)V_{ℓ−1:1}, T = {I^(t), C},
  P = {I^(p), M, …, M^{k−1}}, and V_{1:ℓ} collects products of at most one
  write map per layer. Then W ∈ S ⇒ E[∇_W L(W)] ∈ S, so a trajectory that
  starts in S stays there. *Holds when:* Assumptions 1–6 and population
  gradient descent. The paper does "not prove the stronger property that
  the IMIR is attractive; we only show this empirically".
- **The basis is the commutant.** The proof shows attention scores are
  invariant under the token rotation E^(t) and the offset rotation E^(p),
  so the loss is invariant and the population gradient commutes with
  both. Cross-concept blocks vanish because shifting every offset by π
  sends E^(p) to −E^(p). Within tokens the commuting matrices are
  c₁11ᵀ + c₂I + c₃C, and centring removes 11ᵀ. Within positions they are
  polynomials of degree < k in M. Appendix B generalizes: for any relation
  R, the token selection set is the commutant of Aut(V, R), with one
  basis matrix per orbit of Aut(V, R) on V × V.
- **Size.** The IMIR of a two-layer single-head model is 28-dimensional
  (4 + 16 + 8). Of a five-layer one, 1428-dimensional (Table 2).
- **Four directions carry the two-layer bigram model** (§4.2, Fig. 6).
  α (layer-1 attends to the previous position, ∝ M), β (layer-2 matches
  the query token to what layer 1 retrieved) and γ (the readout of the
  retrieved label) form the induction head. δ (W̄ ∝ C) is in-weights
  learning. Ablating all but (α, β, γ) keeps ICL accuracy at 0.75 against
  0.77 unablated, and destroys IWL. δ alone gives IWL 0.99 and ICL 0.01.
  Removing any one of α, β, γ destroys ICL (Table 1).
- **Theorem 2 (in-weights learning starves in-context learning).** With a
  saturated IWL circuit of logit scale δ,
  E[∇_ICL L(W + W_IWL)] = (fr + (1 − fr)fv) E[∇_ICL L(W)]
  + O(|V|e^{−δ} + |V|^{−1}). *Holds when:* the saturated-IWL,
  large-vocabulary limit, and the disjointness assumption (A4) that no
  distractor block carries the query's canonical partner. Without (A4)
  the error is O(|V|^{−1} + n fc/|V^c|), which "does not vanish in the
  orthonormal idealization" (Remark 1). Checked here as a decomposition
  of the data into the three parts in [THEORY-tmpvqsx2](../theory.d/THEORY-tmpvqsx2.md).
- **Theorem 3 (burstiness).** With burstiness b, in the
  distractor-dominated limit n → ∞ at fixed b,
  E_{D(b)}[∇_ICL L(W)] = b E_{D(1)}[∇_ICL L(W)](1 + O(b/n)), in the
  all-rare regime.
- **The induction head is a winning ticket.** Training only α, β, γ, δ,
  projecting back after every SGD step, gives dynamics that "closely match
  those of the unconstrained network" (Fig. 3, right).
- **Initialization picks the induction circuit** (§4.3). A three-layer
  single-head model has three possible induction circuits, on layers
  (1, 2), (1, 3) and (2, 3). Varying the initial strengths of β and β″
  over several thousand seeds, each winner was found by causal ablation.
  "Each circuit wins when its own units start large" fails: the (1, 3)
  circuit benefits from a large β, which is not in it, and the (1, 2)
  circuit needs a large β″, which is not in it either. The boundaries are
  "very sharp" between the (2, 3) circuit and each of the others, and not
  between (1, 2) and (1, 3), "because the red and green circuits are
  cooperative: both share α". [THEORY-tmpq4l9j](../theory.d/THEORY-tmpq4l9j.md).
- **Circuit detection** (§5, App. F). Greedy backward elimination of IMIR
  directions in two trained five-layer two-hop models recovers the four
  canonical units plus "aiding" directions. In C₁, the trained model
  scores 0.938, the full IMIR projection 0.953, the recovered seven units
  0.922 and the four canonical units alone 0.594. In C₂ the figures are
  0.906, 0.906, 0.844 and 0.719.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under Assumptions 1–6, population gradient descent keeps the key–query and output weights in span(W_ℓ), span(W̄) | strong | Theorem 1 with a six-step proof; re-derived in general form in [THEORY-tmpdxhxm](../theory.d/THEORY-tmpdxhxm.md) |
| C2 | The IMIR is attractive: trained weights align with it from generic initializations | weak | Fig. 3 bottom left and §5's projections; explicitly not proved |
| C3 | The result extends to learnable value maps, and to FFNs and LayerNorm | weak for value maps, moderate for FFN and LN | A.4 is a sketch by the authors' own account; A.5 argues the same commutation step for constrained FFN weights |
| C4 | A saturated IWL circuit scales the ICL gradient by fr + (1 − fr)fv | strong, in the stated limit | Theorem 2, proof in D.4, under (A4) |
| C5 | Burstiness multiplies the ICL gradient by b | strong, in the stated limit | Theorem 3, proof in D.5 |
| C6 | IWL emerges first and delays the induction head | moderate | one SGD run (seed 0, fr = 0.9), Fig. 3; at fr = 0.9 Theorem 2's factor is 0.9 |
| C7 | (α, β, γ) implement ICL and δ implements IWL | strong | ablations, Table 1 |
| C8 | Initialization decides the winning induction circuit, with sharp boundaries between competing circuits and soft ones between cooperating circuits that share a unit | moderate for the phase diagram, weak for the mechanism | several thousand seeds in projected training, Fig. 4; the "circuit battle" reading is offered as an interpretation the learning curves "appear to support" |
| C9 | Projecting onto the IMIR detects circuits below head granularity, including aiding directions | moderate | two trained models, Tables 2–3 |

## Concepts

- **Block-list task**: predict the next token from a list of blocks of at
  most k tokens, of which the last precedes the target and the others may
  or may not be relevant.
- **Selection matrices**: I^(t) and C on tokens (self and partner), I^(p)
  and M^j on positions (same position and j back).
- **Writing basis, action basis**: a layer's write maps with the identity;
  products of at most one write map per earlier layer. A basis weight
  reads, at one position, what a subset of earlier heads wrote, applies a
  selection matrix, and matches it against what another subset wrote at
  another position.
- **Rare tokens, burstiness, within-class variability**: fr, b and fv,
  after Chan et al. (2022). Polysemy is modelled as fv, the frequency
  with which a common token's next token is not its canonical partner.
- **Circuit unit**: one IMIR coordinate with a named role (α, β, γ, δ).
- **Aiding direction**: an IMIR coordinate that survives elimination but
  is part of no canonical induction template.

## Connections

It builds on Bietti et al.'s associative-memory view and Nichani et al.'s
disentangled residual stream, from which Assumption 6 comes, and on Chan
et al. (2022) and Reddy (2024) for the data dependence of in-context
learning. Theorems 2 and 3 are offered as the mechanistic account where
understanding had been "limited to phenomenological models" such as
Reddy's three-parameter one. Its circuit-competition
questions come from Singh et al.'s "strategy coopetition" and from
grokking as subnetwork competition. Theorem 1 is the same kind of result
as the invariant manifolds of loss of plasticity (Joudaki et al.) and of
the lottery ticket (Zhang et al. 2021). It cites Olsson et al. 2022
([LIT-tmpe7b5o](../literature.d/LIT-tmpe7b5o.md)) for induction heads, and Musat et al.'s own earlier
two-head analysis. Its basis is compared to D-RASP decompilation
variables.

## Bearing on the record

- **[QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md).** This is the strongest comparator the question
  has. It already does three things the question's construction proposes,
  in a setting where they are theorems.
  - *A feature allocation over components, with overlap.* An IMIR
    coordinate is an elementary action of one head, and a circuit is a
    set of coordinates. In §4.3 the (1, 2) and (1, 3) circuits share α, so
    one coordinate takes part in two circuits. The coordinates are fixed
    by the data's symmetry group, not inferred by an Indian buffet prior.
    So in this class the free symmetries that the question's second
    condition worries about (rescaling, splitting, basis) are removed by
    construction: Assumption 5 removes the key–query gauge "by fiat", and
    the commutant fixes the basis.
  - *Development.* The coordinates' trajectories are the dynamics, which
    is the question's temporal prior made exact: with the population
    gradient, the next state on the IMIR is a function of the current
    coordinates and the data statistics.
  - *Coupling between features and circuit interaction.* §4.3's sharp and
    soft boundaries are the record's sharpest instance of what the
    question calls "overlapping circuit formation". Sharing a coordinate
    made two circuits cooperate. Needing the same layers for different
    roles made them compete. Under C8's weak support that is an
    interpretation, but it is a falsifiable one.
  The consequence for the question's prospective test: in this task
  class, a coupled feature–circuit model fitted to early checkpoints has
  to beat the IMIR's own reduced dynamics, which predicts the winner from
  initialization by running a seven-coordinate ODE. That is a far stronger
  baseline than the question's "simpler checkpoint-level state-space
  models", and the question could name it.
- **[THEORY-253](../theory.d/THEORY-253.md), [THEORY-783](../theory.d/THEORY-783.md), [QUESTION-193](../questions.d/QUESTION-193.md).** Two points.
  - *A third source of sequential onset.* Theorem 2 and C6 put IWL first
    and ICL later under vanilla SGD. The cause is neither [THEORY-783](../theory.d/THEORY-783.md)'s
    competition for coordinate signs nor dependency between skills. It is
    redundancy: two circuits that solve overlapping parts of the data, so
    the one that saturates first removes the other's gradient on the part
    it solves. [THEORY-783](../theory.d/THEORY-783.md)'s refutation clause, "orthogonal skills under
    plain gradient descent start one after another", is not met: δ and
    (α, β, γ) occupy orthogonal coordinates, but their losses are not
    separate per-skill terms as in the Geometry model, so they are not
    independent skills. The ICL delay in the actual run (fr = 0.9, factor
    0.9) also owes much to α, β, γ being a three-factor product starting
    small, which is a small-initialization plateau. [THEORY-tmpvqsx2](../theory.d/THEORY-tmpvqsx2.md).
  - *Confinement depends on the optimizer.* Theorem 1 is about gradient
    descent. The record checked whether an elementwise optimizer keeps it
    ([THEORY-tmpdxhxm](../theory.d/THEORY-tmpdxhxm.md)). Sign descent keeps the gradient in the IMIR only if
    the IMIR's basis matrices are aligned with the parameter coordinates
    (one-hot embeddings, coordinate-aligned write subspaces). With random
    orthonormal embeddings or write maps, sign(G) leaves the subspace
    (relative residual 0.69 for the token block, 0.62 for a position plane
    embedded in an 8-d stream), while G itself stays in it to 10⁻⁹. That is
    [THEORY-253](../theory.d/THEORY-253.md)'s rotated quadratic again: whether an adaptive optimizer
    changes the dynamics depends on how the relevant directions sit
    against the coordinates. The paper's §5 trains with AdamW and still
    finds the projection faithful (0.953 against 0.938), so the departure
    may be small in practice; the paper does not discuss it.
- **[THEORY-802](../theory.d/THEORY-802.md), [CLAIM-263](../claims.d/CLAIM-263.md).** [THEORY-802](../theory.d/THEORY-802.md) says the mediating direction is
  fixed only relative to a chosen decomposition into units. Here the
  decomposition is chosen by the data's symmetry group: the commutant of
  Aut(V, R) and of the offset shifts. That is a third kind of answer,
  beside Makelov et al.'s privileged components and Wu et al.'s
  conjectured plurality: the units are the operators the task's
  symmetries allow. It holds only inside Assumptions 1–6, and says nothing
  about trained models outside them.
- **[CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md).** The aiding directions are a case of the claim in a
  network. In C₁ the four canonical units alone score 0.594, and with
  three aiding units 0.922. The circuit is not the set of canonical
  units; it depends on how further units are composed with them. That is
  the same kind of point the claim makes about perspectives and features.
- **[CLAIM-367](../claims.d/CLAIM-367.md).** The governance of training here is in the data
  statistics (fr, fv, b) and the initialization, not in anything the
  network does. Theorems 2 and 3 are clean cases of conditions of
  training that belong to the data–optimizer–network system.
- **[CASE-tmplcm41](../cases.d/CASE-tmplcm41.md).** Its condition that the temporal prior must not
  condition on θ_s is met trivially on the IMIR, where the state is the
  coordinates themselves. Its symmetry condition has the answer above.
- No instruction for machine-learning practice is drawn here. The paper's
  §6 suggestions for pruning and constrained training are the
  anthology's, and this work carries the anthology-candidate flag.

## Limitations

- **Idealized architecture.** Fixed orthogonal output–value maps with
  exponentially wide residual streams, merged key–query, orthonormal
  embeddings, no learnable embeddings, and sinusoidal positions with
  random block offsets. The extension to learnable value maps is a sketch.
- **Population gradients.** Minibatch SGD gradients are not invariant
  except in expectation, so confinement holds on average. The theorem
  says nothing about Adam or AdamW, which §5 uses (see Bearing).
- **Invariance, not attraction.** Trajectories that start off the IMIR
  are not proved to approach it.
- **One run behind C6.** The §4.2 training is a single seed at fr = 0.9.
  Theorem 2's suppression there is only to 0.9 of the IWL-free gradient.
  The appendix figures for other data regimes were not seen as images.
- **Projected training in §4.3.** The competition is studied on the
  seven-coordinate sub-manifold with every other coordinate zeroed, and
  only two initial strengths are varied.
- **An inconsistency between §5 and F.3.** §5 says the aiding directions
  "marginally increase the accuracy". F.3 says removing them drops
  accuracy "from ∼ 0.92 down to ∼ 0.6 … which is much more than a slight
  refinement".
- **Notation.** Theorem 2's proof sketch writes the IWL-solved fraction as
  "fc(1 − fv)" with fc undefined there; D.4 gives (1 − fr)(1 − fv).

## Open questions

- Is the IMIR attractive, and from what initializations?
- Under Adam with non-aligned bases, how far does training leave the IMIR,
  and does the departure change which circuit wins?
- Can the winning circuit be predicted from the seven-coordinate ODE alone,
  which would make §4.3 a derivation rather than a scan?
- Which other task classes have a symmetry group whose commutant is small?
  The paper asks this itself.
