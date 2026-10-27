---
status: Read
paper: LIT-tmpt2u54
title: 'Chan, Garriga-Alonso, Goldowsky-Dill, Greenblatt et al. — Causal scrubbing: Appendix'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full on 2026-10-27: the post fetched from the Alignment
    Forum's own API (post kcZZAsEjwrbczxN2i, postedAt 2022-12-03, about
    5,900 words) and converted from its HTML body to text. Read: §1 (more
    on hypotheses), §2 (the metric), §3 (zero and mean ablation), §4
    (unimportant inputs and isomorphic hypotheses), §5 (the alternative
    formalism, Lemma 1, Theorem 2 and Fun Fact 3, with proofs), §6
    (polysemanticity), §7 (a false hypothesis approved), §8 (adversarial
    validation) and all four footnotes. Its diagrams are images, read
    from captions and text only. Theorem 2 was checked numerically and the
    §7 example's arithmetic re-computed (record script, 2026-10-27).
date: '2026-10-27'
summary: >-
  The appendix the main post defers to. It defines % loss recovered
  against a label-shuffled baseline. It gives three reasons to prefer
  resampling ablation to zero or mean ablation. It proves that the
  algorithm's sampled inputs are the maximum-entropy distribution that
  keeps every interpretation node's inputs jointly as on the data, which
  the record re-checked. It explains superposition as monosemantic terms
  plus a resampled interference term, and builds a false hypothesis that
  scores ten times the model's own expected score.
---
<!-- inactive-ok-file: THEORY-802 CLAIM-454 — Proposed; the account and claim this reading bears on, cited as open -->

# NOTE-tmpymmuh: Chan, Garriga-Alonso, Goldowsky-Dill, Greenblatt et al. — Causal scrubbing: Appendix

## Contribution

It supplies what the main post ([LIT-1549](../literature.d/LIT-1549.md), [NOTE-1168](NOTE-1168.md)) states without
detail: the metric, the argument for resampling, the rules for grouping
unimportant inputs, and a characterization of the distribution the
algorithm samples from. It adds a treatment of polysemantic activations
and a second constructed case in which a false hypothesis passes.

## Key insight

A scrubbed run assumes as little as possible beyond the hypothesis.
The sampled inputs keep the joint distribution of each interpretation
node's inputs as on the data. Subject to that, they are as random as
they can be (maximum entropy). Everything a hypothesis does not claim is
treated as independent. So a hypothesis can gain by omission whenever
the model's performance depends on a correlation it leaves out.

## Assumptions

- **What is explained.** E_{x∼D}[f(x)], with no distinction between the
  part of the graph that is "model" and the part that is "metric" (§1.1).
- **Extensional rewrites.** Any f′ equal to f on every input may be
  explained instead (§1.2). The authors note trivial rewrites, such as a
  lookup table, and say the method checks faithfulness, not whether an
  interpretation is mechanistic.
- **For §5.** An isomorphic treeified hypothesis (G_T, I_T, c_T), so that
  every node of I_T has a datum, and a finite input space for the
  uniqueness step.

## Key results

- **The metric (§2.1).** % loss recovered = (E_scrubbed − E_randomized) /
  (E_model − E_randomized) × 100%. E_randomized is the loss with labels
  and outputs shuffled, which is higher than a calibrated guess. "It is
  not very meaningful as a fraction"; it can exceed 100% or be negative.
  Expectations are compared rather than full distributions, so as not to
  have to explain noise (§2.2).
- **Against zero and mean ablation (§3).** Both take the model off
  distribution, since the mean need not lie on the activation manifold.
  Both can move measured performance either way, by an off-distribution
  bias that helps or hurts depending on the subdistribution. And both
  remove variation the model may rely on: a model trained with dropout
  that falls back from M2 to M3 looks unaffected by mean-ablating M2 and
  suffers under resampling.
- **Grouping unimportant inputs (§4).** Sampling unimportant activations
  more independently makes a hypothesis more specific, because it permits
  more swaps. The default is one random datum for all the unimportant
  parents of a node. Sampling every node separately is ill-defined, since
  rewrites change the set of nodes. A hypothesis can be made an
  isomorphism by merging unimportant parents and adding unit-valued
  nodes to I.
- **Lemma 1 and Theorem 2 (§5).** For every node u of I_T, the datum the
  algorithm assigns to u is distributed as D, by induction from the root.
  So the scrubbed inputs to u have the same joint distribution as u's
  inputs on a consistent input (x, …, x). Theorem 2: the joint
  distribution of the scrubbed top-level inputs is the maximum-entropy
  distribution on Xⁿ subject to those constraints, unique for finite X.
  The proof moves a cut up through the tree, using H(X, Z) = H(Y, Z) −
  I(X; Z | Y) + H(X) − H(Y) for Y a function of X and the conditional
  independence of a node's inputs and the rest of the cut given its
  output. Fun Fact 3 decomposes the entropy into the output's entropy
  plus the information each node discards.
- **Superposition (§6).** For ỹ = (cx₁ + dx₂)² + e explaining
  y = ax₁² + bx₂², rewrite ỹ = c²x₁² + d²x₂² + 2cd x₁x₂ + e and resample
  the interference term 2cd x₁x₂. The scrubbed loss matches when the
  interference is unstructured. Splitting the term in two and resampling
  the halves independently lowers its variance and so understates the
  interference cost (§6.1). The authors: "this isn't a solution to
  finding a monosemantic basis".
- **A false hypothesis approved (§7).** Guess the last bit of a hash.
  EASY scores +2 or −1, HARD +10 or −20, "I don't know" 0. A model that
  cannot hash guesses on EASY (expected 0.5) and abstains on HARD
  (guessing would expect −5): mean 0.25. The hypothesis "on HARD the
  model outputs the correct answer" lets HARD inputs be replaced half the
  time by EASY inputs on which the model happens to guess right. The
  scrubbed score is 2.625 (record arithmetic), "even though the
  explanation is wrong".
- **Adversarial validation (§8, credited largely to ARC).** Checking
  explanations so as to reject every false one is "probably NP-hard". The
  proposed weaker check lets an adversary add structure (a `join` of
  hypotheses, defined swap-wise or graph-wise) and asks whether the score
  moves. Rewrites that make the two graphs incompatible are unsolved:
  "ARC has worked on basically this problem for a while and hasn't yet
  solved it".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Each node's datum is distributed as D, so each node's scrubbed inputs are jointly distributed as on the data | demonstrated | Lemma 1's proof |
| C2 | The scrubbed inputs are the unique maximum-entropy distribution subject to C1's constraints | demonstrated, and checked by the record ([THEORY-tmpgikxe](../theory.d/THEORY-tmpgikxe.md)) | Theorem 2's proof; record check |
| C3 | Zero and mean ablation test "this component doesn't matter" less faithfully than resampling | argued with toy examples | §3 |
| C4 | A superposed model can be explained as monosemantic terms plus a resampled interference term when the interference is unstructured | argued in a toy | §6 |
| C5 | A false hypothesis can score far above the model by routing inputs to cases where the model is right | demonstrated in a constructed case | §7, arithmetic re-computed |
| C6 | An adversary adding structure would catch the counterexamples given | proposed | §8; not run, and incomplete by the authors' account |

## Concepts

- **Randomized loss**: the loss with the model's outputs shuffled across
  inputs; the 0% point of the metric.
- **Isomorphic hypothesis**: one whose correspondence is a bijection,
  reached by merging unimportant parents and adding unit nodes.
- **f-consistent and scrubbed random variables**: the values of I_T's
  wires on (x, …, x) and on the algorithm's sampled inputs.
- **join**: the hypothesis permitting exactly the swaps both of two
  hypotheses permit.

## Connections

It is the appendix of [LIT-1549](../literature.d/LIT-1549.md). §4.1 points to the paren post
([LIT-tmpnbrst](../literature.d/LIT-tmpnbrst.md)) for a case where grouping matters, and that post's
Experiments 3c and 3d are §6.1's mechanism in a real model
([THEORY-tmpnu6ih](../theory.d/THEORY-tmpnu6ih.md)). §6 refers to Redwood's own polysemanticity toy-model
paper, not registered. §1.1 counts the IOI circuit ([LIT-1540](../literature.d/LIT-1540.md)), the
modular-addition analysis ([LIT-345](../literature.d/LIT-345.md)), induction circuits ([LIT-1534](../literature.d/LIT-1534.md)) and
curve detectors (Cammarata et al., not registered) as explanations of
this form.

## Bearing on the record

- **[THEORY-978](../theory.d/THEORY-978.md).** Theorem 2 is the general form of what the account
  derives at one node. The scrubbed distribution depends on the
  hypothesis only through the equivalence classes each node induces, and
  it is the least committal distribution consistent with them. Two
  hypotheses that induce the same classes everywhere define the same
  constraints and so the same distribution, the same score. That is
  [THEORY-978](../theory.d/THEORY-978.md)'s tie, now a consequence of the theorem.
- **[THEORY-802](../theory.d/THEORY-802.md) and [QUESTION-234](../questions.d/QUESTION-234.md).** Rewrites of G (§1.2, a subspace and its
  complement) are how a change of basis enters a hypothesis. The method
  takes the decomposition as given, as [NOTE-1168](NOTE-1168.md) says.
- **[CLAIM-454](../claims.d/CLAIM-454.md) and [QUESTION-274](../questions.d/QUESTION-274.md).** §6's treatment of superposition explains
  a model by a monosemantic reformulation the experimenter supplies. The
  score tests the reformulation, not that the units are the model's.
- **Resampling ablation ([LIT-1547](../literature.d/LIT-1547.md), [LIT-1531](../literature.d/LIT-1531.md)).** §3 is the full form of the
  argument those works adopt. Its examples are toys, and no measured
  comparison of the three ablations is given.

No instruction for machine-learning practice is recorded here
(`anthology-candidate`).

## Limitations

- **The theory is about the sampled distribution, not the score.** Nothing
  bounds how far a false hypothesis's score can sit from the model's;
  §7 shows that it can sit far above it.
- **The ablation argument is illustrative.** §3's three problems are made
  with a two-dimensional picture, an invented regression and a dropout
  toy.
- **Errors and slips.**
  - Lemma 1 states that the scrubbed inputs to u are distributed as "the
    product distribution of f-consistent inputs to u". The proof shows,
    and Theorem 2 uses, equality with their *joint* distribution. A
    product would discard exactly the correlations the lemma preserves.
  - §2.1 says "in both of these results posts" the baseline is the
    randomized loss. The induction post's 0% is the induction heads run
    on another sequence ([NOTE-tmpt6p3g](NOTE-tmpt6p3g.md)).
  - The §5 example of a cut is a figure only, so the induction's base and
    step are stated without a worked instance.
- **Uniqueness assumes a finite input space,** which the authors note is
  true on computers.

## Open questions

- Is there a bound, under the adversarial scheme, on how far the score
  of a false hypothesis can exceed the model's?
- Is the maximum-entropy characterization the right null for *what a
  hypothesis leaves unsaid*, or would a distribution matching more of
  the data's correlations make a fairer test? The authors choose
  independence deliberately (§4.1, footnote 4).
