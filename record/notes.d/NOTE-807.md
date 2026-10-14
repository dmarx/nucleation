---
number: 807
status: Read
formerly:
- NOTE-tmps7nin
paper: LIT-954
title: 'Gokhale — The semantic landscape paradigm for neural networks'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from arXiv (2307.09550v1, 18 July 2023, the only
    version), text extracted with pdftotext: all five sections, the four
    schematic figures' captions and the references. The paper has no
    appendix, no experiment and no proof.
date: '2026-10-14'
summary: >-
  A conceptual proposal with no experiment and no proof. Training is
  pictured as a walk on a graph of "heuristic models" (internal
  algorithms), ranked by a fallibility F. A critical dataset size for
  grokking and emergence with scale are each argued to be graph
  connectivity thresholds, and power-law scaling in time, data and size
  is derived from an assumed trap model of activated hops. The
  percolation is asserted, not shown, and the scaling laws rest on
  chosen assumptions.
---
<!-- inactive-ok-file: THEORY-181 THEORY-039 — Proposed; the record's account of a critical training fraction and its caution about phases, compared, not leaned on -->

# NOTE-807: Gokhale — The semantic landscape paradigm for neural networks

## Contribution

The paper offers a vocabulary, not a result. It proposes to describe a
network's training as a trajectory over a graph whose nodes are the
algorithms ("heuristic models") the network's weights can implement,
with a landscape over them given by how wrong each one is. It then
argues, by analogy with percolation and with Bouchaud's trap model for
glasses, that grokking's critical dataset size, emergence with scale and
neural scaling laws can each be described in that vocabulary. Nothing in
the paper is measured or proved.

## Key insight

Coarse-grain from weights to the algorithms they implement, and the
questions "when does a capability appear?" become questions about a
graph: is a good node reachable from the current one (connectivity, set
by data), does it exist at all (node count, set by size), and how long do
the hops take (barrier statistics). A threshold is then a connectivity
threshold, and a power law is the statistics of waiting times.

## Assumptions

- **Conjecture C1.** For every network there is at least one function
  mapping subsets of its parameters to well-formed formulas in some
  formal language. The paper cites interpretability findings (induction
  heads, modular-addition circuits, concept neurons, quanta) as support.
  It is not stated precisely enough to be tested: the language, the map
  and the subsets are unspecified.
- **Fallibility** F(M_H) = Σ_{x∈I} D_KL(P_GT(y|x) ‖ P_H(y|x)), summed over
  *all* possible inputs, not the training or test sets (eq. 1).
- **Arrhenius transition times**, τ_ij = τ⁰_ij·exp(β(F_j − F_i)), with β
  independent of data size D and parameter count N; only τ⁰ depends on
  them (eq. 3).
- **For grokking:** the average degree of the graph is proportional to D.
- **For emergence with scale:** N sets which nodes exist, and D ≫ D_c.
- **For scaling laws (the semantic trap model):** barriers ΔF are
  exponentially distributed, ρ(ΔF) = βρ₀·exp(−βμΔF) (eq. 4); fallibility
  after N_b barrier crossings is F ∝ 1/N_b; traversal rate
  γ(D) = γ_∞·D/(D + D_k); hop distance ℓ(N) = ℓ₀·N^(−1/d_f) + ℓ_∞;
  sub-graph exploration is anomalous diffusion with exponent α.

## Key results

These are arguments, and the paper's "we show" means "we describe".

- **Grokking (§3.1).** If D is below a critical D_c, the graph is
  disconnected and the memorising node cannot reach the generalising one,
  so no amount of training generalises. Called "a percolation transition
  on the graph of heuristic models". Taking the grokking rate
  proportional to the excess degree, λ_g ∝ (D − D_c), gives grokking time
  t_g ∝ 1/(D − D_c), which the paper says agrees with Liu et al. (2022b).
  Also predicted: a transient rise in test loss during grokking, read as
  a barrier crossing.
- **Emergence with scale (§3.2).** Small N removes nodes the network
  cannot formulate, and with them their edges. Past some N a path to low
  F opens: "a percolation transition with increasing N".
- **Trap model in time (§4.1, eq. 6).** Exponential barriers give a
  waiting-time density ψ(τ) = ψ₀·τ₀^μ·τ^(−(1+μ)) (eq. 5) and
  t(N_b) ∝ τ₀·N_b^(1/μ); with F ∝ 1/N_b,
  F(S) = (S₀/S)^μ in training steps S. *Holds when:* μ < 1 and the
  assumptions above.
- **Size and data (eqs. 7–8).** As D → ∞, F(N) = (N₀/N)^(μ/(d_f·α)); as
  N → ∞, F(D) = (D₀/D)^μ. *Holds when:* D_c ≪ D ≪ D_k and
  N_c ≪ N ≪ (ℓ₀/ℓ_∞)^(d_f). The data and time exponents are equal, as in
  Michaud et al.'s quantization model.
- **Fit to LLMs (§4.2).** Matching Kaplan et al.'s data exponent gives
  μ ≈ 0.1, which the paper compares with a glassy-dynamics exponent of
  about 0.144.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A network's computation can be coarse-grained to algorithms in a formal language | weak | conjecture, with interpretability case studies cited |
| C2 | Grokking's critical dataset size is a connectivity threshold on the graph of algorithms | weak | informal argument, Fig. 2 schematic |
| C3 | Grokking time scales as 1/(D − D_c) | weak | follows from an assumed rate λ_g ∝ (D − D_c) |
| C4 | Emergence with scale is the appearance, with N, of a node that connects to low-F models | weak | informal argument, Fig. 3 schematic |
| C5 | Exponentially distributed barriers and F ∝ 1/N_b give power laws in time, data and size, with equal time and data exponents | moderate (as a derivation from its assumptions) | eqs. 4–8, by standard trap-model results |

## Concepts

- **Heuristic model M_H.** An algorithm in the network's internal formal
  language that fixes a conditional distribution P_H(y|x) for every input.
- **Fallibility F.** Summed KL divergence from the ground truth over all
  possible inputs: Ftrain + Ftest + Funseen.
- **Semantic landscape.** F as a function over heuristic models; local
  minima are traps, and moving between them needs crossing "semantic
  barriers".
- **Percolation (as used here).** The graph of reachable models becoming
  connected between the current and a good node. No percolation model,
  lattice or exponent is specified.
- **Semantic trap model.** Bouchaud's trap model with each hop lowering F
  predictably (by about 1/N_b²) instead of resampling it.

## Connections

It borrows Bouchaud's trap model (1992) and the anomalous-diffusion
results of Bouchaud and Georges (1990). It sets itself beside Michaud et
al.'s quantization model and claims to derive that model's ordering
hypothesis, on average, from F ∝ 1/N_b. Its grokking account cites Power
et al. ([LIT-341](../literature.d/LIT-341.md)) for the critical data size and
Liu et al. ([LIT-858](../literature.d/LIT-858.md)) for the time scaling.
Against Schaeffer et al., it argues that emergence must be judged by
inspecting representations, not by any loss metric.

## Bearing on the record

- **[QUESTION-039](../questions.d/QUESTION-039.md).** The LIT registered it
  as "one framework in which grokking, emergence with scale and scaling
  laws are the same kind of event". The paper does not say that. It puts
  them in one *vocabulary* but treats them as two kinds of event:
  thresholds (grokking's D_c and emergence with N) are connectivity
  changes of the graph, while scaling laws come from waiting-time
  statistics on a graph assumed already connected (§4: "we will therefore
  assume that D as well as N are both sufficiently large, such that the
  graph of heuristic models is always connected"). If anything it is a
  vote for "several", with a common language.
- **No THEORY is filed.** The paper's claims are a conjecture (C1),
  informal arguments without a specified graph or percolation model
  (C2, C4), a scaling that follows from an assumed rate (C3), and a
  derivation whose output depends on chosen inputs (C5: F ∝ 1/N_b,
  exponential barriers, ℓ(N), γ(D)). None is something the record could
  state as found. The trap-model derivation is the one piece with
  content, and it shows only that such assumptions *can* yield the
  observed exponents.
- **[THEORY-181](../theory.d/THEORY-181.md)** holds a concrete account of a
  critical training fraction for grokking: the same-answer equations of
  the training set pin the representation. That is a mechanism with a
  measured threshold. Gokhale's "the graph disconnects below D_c" is
  compatible with it but adds nothing it does not already say more
  precisely.
- **[THEORY-039](../theory.d/THEORY-039.md)** says the later phases differ in
  kind. Gokhale's account of a transient rise in test loss during
  grokking as a barrier crossing is a proposal about one such phase,
  untested here.
- No instruction for machine-learning practice; nothing for the
  anthology beyond the `anthology-candidate` flag the LIT carries.

## Limitations

- No experiments, no simulations, no proofs. Every figure is a schematic.
- "Percolation" is used for any loss of connectivity. Genuine percolation
  has critical exponents, and the paper's grokking time 1/(D − D_c) is
  not derived from one; it is the assumed rate inverted.
- The paper says (§5.3) that its threshold and power-law predictions
  "do not rely on particular choices of transition rates", but the
  exponent μ in F(D) and F(S) comes from the Arrhenius rates and the
  exponential barrier distribution. It concedes this for the data
  exponent in the next sentence.
- §4.2 says that with no barriers the scaling is independent of μ, and
  recovers 1/D and 1/√N for ballistic motion on a 2D graph. Read against
  eqs. 7–8, which carry μ in both exponents, this amounts to setting
  μ = 1 for the barrier-free case. That step is not derived.
- Fallibility is defined over all possible inputs and so cannot be
  measured. The bridge to test loss is qualitative ("if the training data
  quality is good").

## Open questions

- Can any trained network's sequence of internal algorithms be mapped
  onto a graph whose connectivity threshold predicts a measured D_c? The
  modular-addition circuits are the obvious test bed; [THEORY-181](../theory.d/THEORY-181.md)'s
  equation-counting threshold is the rival to beat.
- Is the trap model's equality of data and time exponents observed? A
  scaling study reporting both on the same models would test it, though
  the quantization model predicts the same equality.
