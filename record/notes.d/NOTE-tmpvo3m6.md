---
status: Read
paper: 'LIT-tmpq33qh'
title: 'Ay and Polani — Information flows in causal networks'
version: 1
history:
- version: 1
  date: '2026-10-17'
  note: >-
    Read in full from the authors' preprint dated 12 May 2006, the copy in
    the University of Hertfordshire repository (UHRA eprint 162,
    902104.pdf), 15 pp.: §§1–8, Examples 1–6, Theorems 1–2, Propositions
    1 and 3, Corollaries 1–2, references. Nothing skipped. Extracted with
    pdftotext; ligatures (fi, fl) and some symbols were lost and
    reconstructed from context, and the figures were read from their
    labels and the prose. I recomputed Examples 3–6 with a script that
    implements the paper's definitions on the stated networks
    (checks/ay_massey.py in the session scratchpad). The journal version
    (Advances in Complex Systems 11(1), 2008) was not compared.
date: '2026-10-17'
summary: >-
  In a finite causal Bayesian network, X_B is causally independent of X_A
  imposing X_S if setting x_A after setting x_S leaves X_B's
  post-interventional distribution unchanged. For every model on a DAG
  this holds iff every directed path from A to B meets S (ud-separation,
  Theorem 2). Information flow I(X_A → X_B | X̂_S) is conditional mutual
  information with interventional probabilities in place of observational
  ones, zero under causal independence. Examples show it can differ from
  conditional mutual information and from transfer entropy in either
  direction. Example 6's one bit holds at k = 1, by the reading's check.
---

# NOTE-tmpvo3m6: Ay and Polani — Information flows in causal networks

## Contribution

Before this paper, "information flow" in complex systems was measured with
mutual-information variants, transfer entropy among them, which are
correlational. After it, there is an information-theoretic measure of
causal effect: the deviation from causal independence, defined through
Pearl's interventions, with a graphical criterion for when it must vanish.
It is to ud-separation what conditional mutual information is to
d-separation.

## Key insight

Mutual information measures how far observational conditioning departs
from independence. Replace every observational conditional with an
interventional one, the same formula then measures how far setting a
variable departs from making no difference. A tracer injected into a
river, but computed for the unperturbed system.

## Assumptions

- **A causal Bayesian network** (§3): a DAG on finitely many nodes, finite
  state sets, and a known mechanism p_v(x_v | x_pa(v)) at every node. The
  joint is the product (Eq. 1).
- **Interventions by truncated factorization** (Eq. 2): setting X_C = x_C
  removes the factors of the nodes in C. Defined for every x_C, observed
  or not.
- **Positivity** for the converse of Prop. 3: every x_S has p(x_S) > 0.
- **Nothing about estimation.** The quantities need the mechanisms, not
  only data. Continuous nodes are expected to work, not shown (§1).

## Key results

- **Prop. 1.** d-separation implies ud-separation (directed paths are
  all head-to-tail).
- **Theorem 2.** B ud-separated from A by S ⇔ for every G-causal model,
  X_B ⫫ X_A | X̂_S. "If" by a copying construction along an unblocked
  directed path; "only if" by splitting the nodes into those reachable
  from A avoiding S and the rest.
- **Corollary 1.** Observational independence for every model implies
  causal independence for every model.
- **Information flow (§5).** I(X_A → X_B | x̂_S) = Σ p(x_A | x̂_S)
  p(x_B | x̂_A, x̂_S) log[p(x_B | x̂_A, x̂_S) / Σ_{x′_A} p(x′_A | x̂_S)
  p(x_B | x̂′_A, x̂_S)], averaged over the observational p(x_S). With S
  empty it is the total causal effect; with S the rest of V, the direct
  effect.
- **Prop. 3, Corollary 2.** Causal independence ⇒ zero flow, ⇔ under
  positivity. Positive flow ⇒ a directed path from A to B avoiding S.
- **Example 3 (diamond W → X, Y → Z, Z = X ⊕ Y).** I(X:Y) = 1 but
  I(X → Y) = 0; I(W:Z | Y) = 0 but I(W → Z | Ŷ) = 1. *Checked:* all six
  values reproduce.
- **Example 4 (channel splitting).** I(X → Z | Ŷ) = H(X₁), and I(X → Z) =
  H(X). *Checked* with a non-uniform p_X: 0.8813 = H(X₁), and 1.5710 =
  H(X).
- **Example 5 (mediated flow).** Case 1: I(X:Z | Y) = 0 and I(X → Z | Ŷ) =
  1. Case 2, the same joint distribution with a different mechanism for
  x ≠ y: I(X → Z | Ŷ) ≈ 0.31. *Checked:* 0.3113 = h(3/4) − 1/2.
- **§6.** For one Markov chain, I(X_[i,j] → X_[k,l]) = I(X_[i,j] : X_[k,l]).
- **Example 6 (information exchange).** Two binary chains that copy each
  other's state, from ½[(0,1) + (1,0)], against two chains that each
  invert their own state, with the same observations. Transfer entropy
  I(Y_[1,k] : X_{k+1} | X_[1,k]) is zero in both. The paper says flow
  I(Y_[1,k] → X_{k+1} | X̂_[1,k]) is one bit in the first case and zero in
  the second. *Checked, with a qualification:* the first case gives one
  bit at k = 1, but zero for k = 2 and 3. Imposing all of X_[1,k] fixes
  Y_k = x_{k−1}, so the source carries no variation into X_{k+1} = Y_k.
  Imposing only X_k gives one bit at every k. The second case is zero
  either way. The contrast the example draws survives at k = 1 or with
  X_k alone imposed. The calculation is mine; the paper states no k.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | ud-separation characterizes causal independence over all models on a DAG | strong | Theorem 2, proved |
| C2 | Information flow is zero under causal independence, and iff under positivity | strong | Prop. 3, from properties of relative entropy |
| C3 | Flow and conditional mutual information differ in both directions | strong | Examples 3 and 5; checked |
| C4 | Transfer entropy can be zero where there is information flow, and cannot tell apart observationally equivalent systems that flow distinguishes | moderate | Example 6; checked at k = 1 only, see Key results |
| C5 | For a single Markov chain, flow between time windows equals mutual information | moderate | §6, "a small calculation", not shown |
| C6 | Imposing intermediate nodes can increase as well as decrease flow, as synergy can be positive or negative | moderate | Examples 3–4; the synergy link is analogy |
| C7 | The measure has an "unambiguous causal interpretation" useful in physics, synchronization, games and perception–action loops | speculative | §7, programmatic |

## Concepts

- **ud-separation** — every directed path from A to B goes through S
  (Def. 1).
- **Causal effect A → B imposing x_{C∖A}** — p(x_B | x̂_A, x̂_{C∖A}),
  summing out the unintervened nodes (§3, Step 2).
- **Causal independence X_B ⫫ X_A | X̂_S** — Eq. 4.
- **Information flow I(X_A → X_B | X̂_S)** — §5.

## Connections

- **Builds on** Pearl (2000) for interventions and Verma and Pearl's
  d-separation theorem, which Theorem 2 mirrors. It cites Schreiber (2000,
  [LIT-tmpz9o5z](../literature.d/LIT-tmpz9o5z.md)) for transfer entropy and Shaw and Matsumoto–Tsuda for
  time-window mutual information.
- **When flow equals transfer entropy.** Transfer entropy is
  I(Y_[1,k] : X_{k+1} | X_[1,k]) and flow is
  I(Y_[1,k] → X_{k+1} | X̂_[1,k]). The two formulas are term-by-term the
  same if p(y_[1,k] | x̂_[1,k]) = p(y_[1,k] | x_[1,k]) and
  p(x_{k+1} | ŷ_[1,k], x̂_[1,k]) = p(x_{k+1} | y_[1,k], x_[1,k]) for every
  value, with every observed configuration of positive probability. So
  they agree when conditioning on the pasts is as good as setting them,
  which is a back-door condition, and when the data visit every
  configuration. They diverge through confounding, through determinism or
  missing support, which is Example 6, and because setting X's past
  changes Y's past, which it does in Example 6 for k ≥ 2. This is my
  reading of the definitions, not a result in the paper.
- **[THEORY-tmp4g68i](../theory.d/THEORY-tmp4g68i.md) (Eichler and Didelez).** Both are interventional, by
  truncated factorization or by intervention indicators. Eichler and
  Didelez give conditions under which an effect is identified from
  observational time series; Ay and Polani assume the mechanisms are known
  and do not address identification. Their Theorem 2 is the DAG analogue
  of "a missing Granger edge means no effect": no unblocked directed path
  means no flow. My connection.
- **[CLAIM-tmp6nu4a](../claims.d/CLAIM-tmp6nu4a.md).** Its counterexample gives zero transfer entropy and
  a nonzero effect of a(t) on b(t + 1). In this paper's terms, for a
  discrete analogue (the paper's networks are finite), with the
  process unrolled as a DAG, the flow I(a(t) → b(t + 1)) is positive
  through the path a(t) → b(t) → b(t + 1), since nothing is imposed.
  Example 6 is another case of the same gap. My connection.
- **[CLAIM-tmpa4kr6](../claims.d/CLAIM-tmpa4kr6.md).** Flow is defined for nodes with their own
  mechanisms. A macro variable that is a deterministic function of its
  micro variables at the same time has no separate mechanism to replace
  without replacing theirs, so flow from it is not defined in the paper's
  sense unless the macro variable is added as a child node. Then setting
  it cuts it from its parents and affects only its own children. My
  inference.
- **[TERM-tmpq0ms2](../terms.d/TERM-tmpq0ms2.md) (Granger causality).** Granger causality and transfer
  entropy are observational and measure prediction. Flow is the
  interventional counterpart and needs a causal model.

## Bearing on the record

- Filed as [THEORY-tmpkovi2](../theory.d/THEORY-tmpkovi2.md).
- For [CLAIM-tmpu9ivq](../claims.d/CLAIM-tmpu9ivq.md) and [TERM-tmpj9z04](../terms.d/TERM-tmpj9z04.md): transfer entropy does not
  measure causal information flow in this paper's sense. The two coincide
  under the conditions in Connections and diverge otherwise.
- **For the Anthology of the SOTA:** no instruction for ML practice.

## Limitations

- Every example is a small deterministic binary network, where positivity
  fails and observational quantities are degenerate. The gap from
  transfer entropy is shown where transfer entropy is weakest.
- The measure needs the mechanisms. Nothing here says how to estimate it
  from data, or when it is identified. Eichler and Didelez's
  identification results are the piece that would be needed.
- Example 6's claim needs the qualification in Key results.
- §6's identity is asserted after "a small calculation".
- The averaging over the observational p(x_S) mixes regimes. It weights
  interventional quantities by observational frequencies, which the
  paper does not discuss.

## Open questions

- Estimation and identification of information flow from observational
  data, by combining it with back-door criteria such as Eichler and
  Didelez's.
- The relation between flow and partial-information-decomposition atoms
  of transfer entropy, which C6 gestures at.
