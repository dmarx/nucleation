---
status: Read
paper: LIT-tmp3cyf2
title: 'Chen, Kunin, Yamamura and Ganguli — Stochastic Collapse: How Gradient Noise Attracts SGD Dynamics Towards Simpler Subnetworks'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader from arXiv 2306.04251v3
    (2024-05-29; v1 2023-06-07), which carries the NeurIPS 2023 footer.
    Main text, appendices A to D, G, H and J and the figure captions read
    in full; the proof algebra of appendices E, F and I skimmed. The
    extraction garbles the mathematics; the reader's reading of equation 6
    is marked as such. The filer rechecked the quotations by script
    against the downloaded text.
date: '2026-11-19'
summary: >-
  Sets where a hidden neuron vanishes, or two neurons in a layer are
  identical, are invariant under SGD; both are fixed sets of reflection
  symmetries of the parameterization. For a continuous model of SGD the
  authors give a sufficient condition for such a set to attract, a
  competition between curvature and gradient noise that can hold at
  saddles and maxima, and report clusters of near-identical neurons in
  trained VGG and ResNet networks, growing with learning rate. In a linear
  teacher-student model the collapse keeps weak modes from being learned.
---
<!-- inactive-ok-file: THEORY-tmpz825j THEORY-781 CLAIM-tmpj540o CLAIM-tmp8ljvp THEORY-tmpgjb4y — Proposed; entries this reading bears on -->

# NOTE-tmpsybfr: Chen, Kunin, Yamamura and Ganguli — Stochastic Collapse: How Gradient Noise Attracts SGD Dynamics Towards Simpler Subnetworks

## Contribution

It names the invariant sets that every feed-forward network has, derives
them from symmetry, and gives a rigorous sufficient condition, for the
stochastic-gradient-flow model, for noise to make them attracting. It
links the result to a simplicity bias and to learning-rate schedules.

## Key results

1. **Invariant sets (p. 1).** "We introduce invariant sets as subsets of
   parameter space that, once entered, trap SGD", "one for vanishing
   neurons and the other for identical neurons". An invariant set is
   left by no minibatch update (Def. 3.1).
2. **From symmetry (Thm 3.1, p. 4).** An "affine subspace A = {θ ∈ Rd |Qθ
   = θ} is an invariant set if" the loss is approximately Q-symmetric
   around it; "In general, any translational symmetry should generate
   invariant sets" (App. B.3).
3. **Curvature against noise (p. 2).** The condition for attraction
   "reveals a competition between the loss landscape's curvature around
   an invariant set and the noise introduced by stochastic gradients".
   "the collapsing condition can still be satisfied with negative
   curvature" (p. 5), and "the learning rate to batch size ratio
   determines the maximum attainable steepness for an invariant set to be
   attractive" (p. 5).
4. **Only sufficient in high dimensions (p. 6).** "Nonetheless, we can
   derive a sufficient condition:" (Thm 4.2). "Identifying the necessary
   conditions for stochastic attractivity of general affine invariant
   sets is an important goal for future work" (p. 10). In the
   two-neuron toy, "An increase in the learning rate accelerates the
   collapsing process until reaching a critical threshold, beyond which
   the collapsing ceases" (App. G).
5. **A continuous model (p. 5).** "Although this SDE cannot be
   interpreted as the continuous-time limit of SGD, it matches the first
   and second moments of the SGD process."
6. **In trained networks (p. 7).** Clustering "reveals multiple large
   clusters of many neurons with near identical incoming and outgoing
   parameters after training", with neurons counted identical when
   within "10% of their norms"; "we replace ReLU with GELU activation in
   all our experiments below." "increased learning rates typically
   intensify the stochastic attraction to invariant sets by reducing the
   number of independent neurons", while "changes in batch size produce
   complex shifts" (p. 8).
7. **Generalization (pp. 9–10).** Collapse "effectively governs the
   minimum learnable singular mode, serving as a natural mechanism to
   prevent overfitting"; "even after the training loss plateaus, further
   extended training with a large learning rate η will continue to drive
   stochastic collapse of small singular modes"; and "the repulsive
   escape will take longer the closer it starts from the invariant set".

## Assumptions

The stochastic-gradient-flow approximation, often with label noise;
affine invariant sets only ("exploring the possibility of curved
invariant sets" is future work); data symmetry not studied; the
propositions do not cover neurons with residual connections; deep
experiments used momentum and weight decay 0.0005, neither varied.

## Concepts

Invariant set of SGD; sign and permutation invariant sets; stochastic
attractivity; rate of attractivity; stochastic gradient flow; fraction of
independent neurons; vanishing neurons.

## Bearing on the record

- **Velarde and colleagues' citation ([THEORY-tmpz825j](../theory.d/THEORY-tmpz825j.md)).** They cite this
  paper for "Any parameter set that is invariant under GD becomes a
  stable attractor under stochastic GD for sufficiently large learning
  rates". The paper does not say that. Its sets must be invariant under
  every minibatch update, not full-batch descent; attraction is a
  sufficient condition weighing curvature against noise, not guaranteed
  in high dimensions; in its toy, collapse stops above a critical
  learning rate; and the analysis is of the continuous model. It covers
  vanishing and pairwise identical neurons, not covers in general.
- **[THEORY-781](../theory.d/THEORY-781.md) and [QUESTION-206](../questions.d/QUESTION-206.md).** An independent, rigorous sufficient
  condition for noise making symmetric subspaces attract, at saddles too,
  with evidence in deep networks; no deep-network threshold tested, no
  control that removes the symmetry.
- **The fibration hunch ([QUESTION-tmpex36a](../questions.d/QUESTION-tmpex36a.md)) and [CLAIM-tmpj540o](../claims.d/CLAIM-tmpj540o.md).** A route
  to learned unit partitions with no data symmetry: the architecture's
  permutation symmetry plus noise. The partitions are copies, not
  quotients by relabelling.
- **Plasticity and overconsolidation.** Not discussed by the authors.
  Collapsed units can never be separated by gradients, and near-collapsed
  ones escape slowly, which parallels dead units and falling rank in
  plasticity loss ([THEORY-tmpgjb4y](../theory.d/THEORY-tmpgjb4y.md)) and gives overconsolidation
  ([CLAIM-tmp8ljvp](../claims.d/CLAIM-tmp8ljvp.md)) a candidate mechanism. An analogy, not evidence.

## Limitations

The proofs of appendices E, F and I were not checked line by line;
equation 6's form is the reader's reading. Figures read through their
captions. The proceedings version was not compared.
