---
status: Read
paper: LIT-tmpzusyw
title: 'Velarde and others 2026 — Emergence of Fibrations, Compression, and Symmetry Breaking in Artificial Neural Networks'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://arxiv.org/pdf/2609.01768 (HTTP 200, 6.0 MB PDF, v1 of
    1 Sep 2026), fetched 2026-11-19. Kind of copy (step 5): arXiv preprint,
    the authors' own upload. No obstacle. Text extracted with pdftotext
    -layout to dl/text.txt (also dl/text_raw.txt without layout). Read:
    abstract; Main (hierarchy of symmetries, Fig. 1); Results 2.1
    (synchronization, synchronized learning, Theorem 1, compression rule)
    and 2.2 (emergence, synchrony and data regularity, compression in
    MLP/CNN/Transformer, fibration symmetry breaking); Discussion; Methods
    4.1 (definitions), 4.4 (fibration on weighted graphs, Eq. 14-15),
    4.9.2-4.9.3 (end), 4.10-4.11 (Theorem 1 proof and the stability-of-
    covers paragraph), 4.14 (datasets, Tables 1-3), 4.15 (balanced-colouring
    algorithm with tolerance), 4.16 (threshold search), 4.21 (fibers refine
    class-conditional synchrony clusters), 4.22 (loss-landscape hierarchy).
    Skipped or only glanced: Methods 4.2-4.3 (base construction, lifting),
    4.5-4.9.1 (weighted input trees, synchronization proofs, quasi-
    synchronization bound, flavored opfibrations), 4.12-4.13
    (sums/convolutions/gates/attention, compression rules per architecture),
    4.17-4.20 (pruning, orthogonal regularization, continual-learning
    details), 4.23 (low rank); supplementary video S1 not seen.
date: '2026-11-19'
---
<!-- inactive-ok-file: CASE-tmpsjjgx CLAIM-tmpj540o — Proposed; cited in this filing of 2026-11-19 -->

# NOTE-tmp0z3qi: Velarde and others 2026 — Emergence of Fibrations, Compression, and Symmetry Breaking in Artificial Neural Networks

## Contribution

Velarde, Parra, Hashemi and Makse (arXiv 2609.01768, v1, 1 September 2026) carry graph fibrations (isomorphic input trees), opfibrations (isomorphic output trees) and their intersection, which they call coverings, from binary graphs to weighted feed-forward networks. Two units are in one fiber when, for every fiber colour of the previous layer, their summed incoming weights from that colour are equal (Eq. 14); this is a balanced colouring computed layer by layer from the input, where every input coordinate starts with its own colour. They prove that fibers synchronize activity for every input, that (flavoured) opfibers synchronize backpropagated error, and that the two together make weight updates equal. From this, Theorem 1 says that under gradient descent the covering partition can only coarsen. They then report that, with a tolerance, quasi-covers grow during training in an MLP (MNIST), a CNN (ImageNet) and an LSTM agent (Atari Beam Rider), and use them to compress networks, a transformer included. They also propose a continual-learning method that compresses covers and adds fresh units.

## Key results

- **Fibers synchronize activity** (Results 2.1, p. 5; Methods 4.4, Eq. 15): "two nodes in the same fiber synchronize their activity (hi = hj ) for any input x to the network". With a tolerance εfib these are "quasi-fibers", and the synchrony error is bounded in proportion to εfib (p. 6).
- **Covers can only merge under GD** (Theorem 1, p. 7; proof Methods 4.11): "Under the dynamic of GD, the covering partition Cℓcov (t + 1) is a coarsening of Cℓcov (t)." The authors gloss it: "once multiple nodes join a cover, they cannot exit".
- **Stability under SGD is cited, not proved** (p. 7; Methods 4.11.3): "Any parameter set that is invariant under GD becomes a stable attractor under stochastic GD for sufficiently large learning rates [32]." Reference 32 is Chen, Kunin, Yamamura and Ganguli's "Stochastic collapse" (NeurIPS 2023).
- **Emergence in training** (Results 2.2, pp. 8–9; Fig. 2d, Fig. 3a, c, e): "at the start of learning, all nodes form trivial (single-node) fibers. As learning progresses, the nodes start to partition into multi-node covers". Fibers are larger in later layers and opfibers in earlier ones. In the LSTM agent, quasi-covers "first grow in size, i.e., unique nodes decrease, but these approximate symmetries break upon further training" (p. 9).
- **Exact fibers need a tolerance in practice** (Methods 4.15, p. 38): "Given that these conditions are impossible to satisfy exactly for continuous weights, we transform Eq. (21) into a set of inequality constraints parameterized by a tolerance". Fibers are found by complete-linkage agglomerative clustering of the colour-summed weight rows, with a distance threshold ε.
- **Automorphisms are not seen** (Main, p. 4): automorphism symmetry "is so restrictive that we have never observed it in our trained networks."
- **Compression** (Results 2.2, p. 10): a three-layer MLP on MNIST compressed "down to 17% of the original network size with no change in loss or accuracy". The German–English transformer goes to 70% at zero loss tolerance and to 18% at εLoss = 0.45 (p. 10). For the transformer "We only tested fibration compression" (p. 10), and no emergence-over-training curve is shown for it.
- **Fibers and data regularity** (Results 2.2, p. 9; Methods 4.21, p. 44): class-conditional synchrony clusters "are a coarsening of the partitioning into fibers". Fibers match synchrony clusters under random inputs at small thresholds ("matching score=1", Fig. 10a).
- **Plasticity** (Results 2.2, p. 11): "The emergence of sym- metry induces parameter tying, which reduces the degrees of freedom" (hyphen as in the PDF). This is offered as the explanation of loss of plasticity. Fibration Symmetry Breaking (compress to the covering base, then "Sprout" fresh random units) beats Continual Backpropagation beyond task 1,500 on continual ImageNet (Fig. 3g).

## Assumptions

- Layered networks with weighted sums followed by a pointwise nonlinearity (Eq. 1). Other architectures are handled by treating sums, gates and attention as hypergraphs (Methods 4.12, not read in detail).
- Fibers are computed with every input coordinate in its own colour (Methods 4.4: "starts in the input layer, ℓ = 0, with all nodes (d0 nodes) having distinct colors"). So fibers are defined relative to the whole input space, not to the data.
- Theorem 1 is for plain gradient descent on exact covers. The MLP experiments used Adam (Table 1), the CNN used SGD with momentum, and all empirical covers are quasi-covers at a chosen tolerance.
- Stability under SGD is imported from reference 32 on the condition of "a sufficiently large learning constant" (Methods 4.11.3).

## Concepts

- **Fibration / opfibration / covering symmetry**: units with isomorphic input trees, output trees, or both. On weighted layered graphs these are in-balanced, out-balanced, and in- and out-balanced colourings (Methods 4.1). Hierarchy: fiber, opfiber ≥ cover ≥ orbit.
- **Quasi-fiber**: a fiber up to tolerance εfib (from Boldi, Leifer and Makse's quasifibrations, ref. 30).
- **Synchronized learning**: equal weight updates across a fiber-to-opfiber block (Eq. 5).
- **Fibration compression and lifting**: merge each colour into a base graph, summing over source colours and averaging over target colours (Eq. 6). Lifting is the inverse.
- **Fibration Symmetry Breaking (FSB)**: prune to the covering base, then sprout new random units.

## Bearing on the record

- **QUESTION-tmpex36a** — leaves open, and narrows it. This is the evidence that balanced partitions of units (quasi-fibers and quasi-covers) form during ordinary training without symmetry in the data forcing them, on MNIST, ImageNet and Atari. That is the form the question takes after CLAIM-tmpj540o: learned rather than forced. But the paper has no relational or rule task, no measure of role abstraction or of invariance to relabelling, and its fibers are computed with every input coordinate a separate colour. So they are input-independent redundancies (synchronized "for any input x"), not a quotient of inputs. The paper's closest object to a data-relative quotient is the class-conditional synchrony clusters, which are coarser than fibers (Methods 4.21). The question's proposed measurement, approximate balanced colourings with a tolerance, is what the paper's algorithm (Methods 4.15) does, with code at github.com/MakseLab.
- **CLAIM-tmpj540o** — leaves open, compatible. The claim shows that data symmetry cannot force unit partitions when the vocabulary exceeds the width. This paper offers a different mechanism, cover persistence under GD plus an SGD-attractor argument, by which partitions arise with no data symmetry at all. It does not test the claim and gives no independent evidence for its derivation. It reports that automorphisms (permutation symmetries) are "never observed" in trained networks, which fits the claim's point that permutation actions are not where the structure comes from.
- **THEORY-1065** — supports its scope and extends its use. On binary graphs the fiber partition is a balanced colouring (Methods 4.1: "fibers are in-balanced colorings, opfibers are out-balanced colorings"). Synchrony "for any input" is the feed-forward analogue of a robust polydiagonal. Two cautions carry over from THEORY-1065: invariance is not stability, and the paper's stability claim rests on reference 32, not on its own proof. The weighted generalization (equal colour sums, Eq. 14) is a weighted balance condition, which THEORY-1065's 2003 source does not cover: that account notes it says nothing about weighted or multiple arrows.
- **THEORY-1059** — supports, by application. Fibration compression to a base graph that "performs the identical forward computation" (p. 4) is the quotient network run on the synchronous subspace. The paper adds the loss-preservation bound for quasi-fibers (Eq. 7, not checked).
- **TERM-062, QUESTION-tmpcb0bf, CASE-tmpsjjgx** — no direct bearing.

## Limitations

- Theorem 1 says exact covers persist once formed. It does not say how they form from random weights, where exact covers are absent (the paper cites the Erdős–Rényi asymmetry theorem). Emergence is shown only empirically, at chosen tolerances.
- In the parts read I found no baseline giving the number of quasi-covers expected at the same tolerance for untrained, shuffled-label or norm-matched random weights. So how much of the growth is structure, and how much is shrinking or concentrating weights passing a fixed cosine threshold, is not separated. (Methods 4.15 normalizes the colour-summed rows, which removes scale but not concentration.)
- The theory is for GD, while the MLP was trained with Adam. The SGD-stability claim is borrowed from reference 32.
- For transformers only post-hoc compression is shown, not emergence during training. The abstract's "emergence of covering symmetries across ... transformer networks" is therefore wider than the evidence shown in the main text.
- Table 1 gives the ImageNet CNN 2 output nodes against 1,000 classes, which is not explained in the parts read.
- Results are from one group, on one preprint, not peer reviewed as of v1.
