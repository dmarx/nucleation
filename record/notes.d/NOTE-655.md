---
number: 655
status: Read
formerly:
- NOTE-tmpavdpk
paper: 'LIT-854'
title: 'Irreversibility in bacterial regulatory networks'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the CC BY version of record at PubMed Central
    (PMC11352831, HTML): abstract, introduction, results, discussion,
    Materials and Methods, every equation followed. The Supplementary
    Text (nodes without irreversibility, necessity of positive circuits,
    asynchronous preservation, periodic-attractor motifs, alternative
    rule formulations, comparison with adaptive evolution, the
    transcription-weighted attractor analysis) and Tables S1–S3 read
    from the arXiv copy (2409.04513v1, which carries the supplement).
    Figures read from their captions, not inspected as images. The
    HillCube differential-equation analysis (fig. S7) read in outline
    only. The code and data deposits (Zenodo, GitHub, Dryad) were not
    opened, and nothing was re-run.
date: '2026-10-09'
summary: >-
  In an ensemble of sign-consistent Boolean rules on the 87-gene core of
  the E. coli regulatory network, 51 genes admit a transient knockout or
  overexpression that leaves the network in a different attractor; only
  genes that reach a positive circuit can, and the likelihood grows with
  the weighted number of paths to one. Transitions run from small basins
  to large. The comparison with evolved crp-knockout strains supports the
  network's sign structure strongly and its irreversibility predictions
  only weakly; no transient perturbation was done in cells.
---

<!-- inactive-ok-file: THEORY-178 — Proposed; the finding this reading produces, filed with it -->
<!-- inactive-ok-file: THEORY-058 — Proposed; named as a neighbouring self-maintaining-loop account -->

# NOTE-655: Irreversibility in bacterial regulatory networks

## Contribution

Bistable switches in bacteria were known one circuit at a time (the lac and
mar operons, sporulation, *Caulobacter* stalking), and each is thrown by an
environmental cue. This paper asks the question for a whole reconstructed
regulatory network and for genetic rather than environmental perturbation:
can switching one gene off or on for a while, and then restoring it, leave
the rest of the network in a lasting new state? Across an ensemble of
plausible Boolean rules it finds that this is common in the core of the
*E. coli* network, says which genes can do it (those that reach a positive
circuit), and gives a structural predictor of how likely it is. It ends
with a concrete experiment nobody has yet run.

## Key insight

A transient perturbation is remembered when it flips a positive circuit
that then holds itself in the new state after the cause is gone. So the
ability of a gene to cause irreversibility is a matter of where it sits:
it must reach a strongly connected component that contains a positive
circuit, and the more independent routes it has to such components the
likelier it is to flip one. Genotype then fixes a set of possible
expression states, not one, and history picks among them.

## Assumptions

- **The network is RegulonDB's union of potential interactions**, with
  polarity taken as known and presence allowed to vary by condition. Edges
  of dual or unknown sign (148) are dropped.
- **Boolean, synchronous, deterministic dynamics**, x_u^{t+1} = B_u(x^t),
  with three consistency constraints: each rule uses exactly the gene's
  regulators, each regulator is essential, and each enters with its sign
  (monotone in each input). Autorepression is silenced when the gene is off,
  to exclude artefactual oscillation; this breaks essentiality for some
  edges. phoB, the only core gene with no input, is given a self-loop.
- **Rule ensemble.** Rules are sums of products built left to right over
  the inputs, sorted by their out-degree (ascending: "diffuse control";
  descending: "concentrated control"), joining consecutive inputs by
  ×( with probability r, + with probability (1 − r)s, × with probability
  (1 − r)(1 − s). M = 20 realizations per non-unique (r, s) setting, on
  grids along s = 1, r = 0 and r = 1 − s.
- **The perturbation protocol.** From the first recorded point of each
  attractor 𝒜, one gene is clamped (1 → 0 for knockout, 0 → 1 for
  overexpression), the network runs to a new attractor, the clamp is
  released at the first point reached on it, and the network runs to a
  final attractor 𝒜′. Irreversible means 𝒜′ ≠ 𝒜. Every attractor counts
  equally unless stated (basin weighting is a robustness check).
- **Only the core matters.** Genes outside the 87-gene core cannot affect
  core genes and change reversibly downstream, so they are trimmed. The
  largest origon is taken to stand for the whole network: Table S1 shows the
  other large origons' cores overlap it almost entirely.

The setting is narrower than the title. "Irreversibility" is a change of
attractor in a deterministic model, permanent by construction. Real cells
are noisy and divide; the authors expect "temporarily irreversible but
long-lived" changes, and how long they last is left to experiment.

## Key results

- **Network reduction.** 1859 genes and 5119 edges; the phoB origon has
  1406 genes; its core has 87 genes and 290 edges. The number of
  consistent rule sets is at least ∏_u 2^{k_u⁺ − 1}, about 10^61.
- **Attractor counts.** The geometric mean is about 10² attractors under
  concentrated control and 10³ under diffuse control, largest at
  intermediate nestedness. Of attractors, 42.2% are fixed points, 24.4%
  period 2, 1.1% period 3, 27.9% period 4, 4.4% longer.
- **Who can be irreversible** (Fig. 5). 51 core genes admit an irreversible
  perturbation for some rules; every gene influencing a positive circuit
  does. The 36 that never do are 32 leaves and 4 genes (metJ, pdhR, argP,
  nac) whose only output is an autorepressive leaf. The ensemble estimate
  is within about 0.1 of its limit (RMSD between independent ensembles of
  10 realizations, fig. S2).
- **Structure predicts propensity** (Fig. 6). With path weight
  ω(H) = ∏_{i=2}^{ℓ} (k⁺_{H_i})^{−1} and K_u the sum over paths from u
  into strongly connected components with a positive circuit,
  p̂_u = aK_u^b explains 55–62% of the variance in irreversibility
  probability; b = 0.68 ± 0.09 (diffuse), 0.93 ± 0.14 (concentrated).
  The weight is the probability of a path transmitting a change if each
  input is equally likely to flip its target and changes are independent.
- **Conditions.** Necessary: some gene other than the perturbed one has
  changed by the time the clamp is released. Sufficient: the released state
  lies outside 𝒜's basin. Both checked in the simulations.
- **Basin direction** (fig. S4). Weighting each starting attractor by its
  basin keeps the pattern (R² > 0.91 against unweighted) but roughly halves
  the rate; initial basins average about one-eighth the size of final ones.
- **Rule dependence** (Fig. 7). For hns, stpA, crp, rcsB, leuO, bglJ, rhaR,
  rhaS irreversibility varies monotonically with rule bias, and knockout
  and overexpression irreversibility are anticorrelated: a gene is more
  irreversible under the perturbation applicable in more attractors.
  Hubs upstream of many components (phoB, cra, fis) lose irreversibility at
  intermediate nestedness, genes inside large components (fnr, fur, fliZ,
  gadX) gain it.
- **Transition types** (Supplementary Text). 49.0% of irreversible
  transitions are between fixed points, 31.7% between partial fixed points
  differing on their fixed genes, 2.2% fixed point to partial fixed point,
  17.1% between partial fixed points with different fixed sets. In every
  case the attractors differ on a gene fixed in at least one of them. At
  least 67.9% of transitions keep their initial and final attractors under
  asynchronous updating.
- **Evolved crp-knockout strains** (Fig. 8, Tables S2–S3; RNA-seq,
  GEO GSE152214). The predicted sign of change, minus the polarity of the
  shortest path from crp, matches the observed log fold change (relative to
  the mean shift) for 10 of 11 genes with |ln| > 0.5 in batch and 33 of 42
  in chemostat; average precision 0.99 and 0.85, each P < 0.01 by
  shuffling the predicted signs (25,000 shuffles). Among strongly changed
  genes, irreversible responders matched the predicted sign 8 of 9 times
  and reversible genes 2 of 2 in batch, 28 of 34 against 5 of 8 in
  chemostat; P = 0.03 for both conditions together.
- **Candidates** (figs. S5–S7). Weighting attractors by their similarity
  to 16 observed instances of crp downregulation in public RNA-seq points
  to self-activating genes positively regulated by crp. Candidates: zraR,
  melR, rhaRS. A HillCube model of the motif gives a bistable range that
  widens with self-activation strength and Hill coefficient.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In the model, transient single-gene perturbations of the *E. coli* core network often leave it in a different attractor | strong for the model ensemble | simulations over the rule ensemble, Fig. 5, with convergence check fig. S2 |
| C2 | Only genes that can reach a strongly connected component containing a positive circuit can cause irreversibility | strong (argument plus simulation) | Supplementary Text, with Thomas's rule that positive circuits are necessary for multiple fixed points (ref. 38) |
| C3 | Propensity rises with the weighted number of paths to such components | moderate | power-law fit, R² 0.55–0.62, Fig. 6 |
| C4 | Irreversible transitions run from small basins to large | moderate | basin-weighted re-analysis, fig. S4 |
| C5 | The conclusions hold under asynchronous updating and in continuous models | weak to moderate | fixed points are preserved (cited); partial fixed points preserved in at least 46.3% of cases by a sufficient condition; one continuous motif |
| C6 | The signed network predicts the direction of expression change after adaptive evolution to a crp knockout | moderate | sign concordance, Fig. 8B, P < 0.01 in each condition |
| C7 | Genes that respond irreversibly to a transient crp knockout are those that change in adaptive evolution to a permanent one | weak | counts of 9 and 2 (batch), 34 and 8 (chemostat), P = 0.03 jointly |
| C8 | Transient crp knockdown will cause lasting expression changes in zraR, melR or rhaRS in cells | untested | a prediction; no experiment reported |

## Method

Trim the RegulonDB network to the core of its largest origon by repeatedly
deleting genes with no outgoing edges. Sample rule sets with the (r, s)
algorithm and two input orderings. Find all attractors of each rule set
with a SAT-based method (BoolNet in R). From each attractor, clamp each gene
off and on, run to an attractor, release, run to the final attractor, and
record whether it changed and which genes differ. Average over attractors
weighted by how often each gene is on (eq. 4). Relate the averages to path
counts into positive-circuit components, then compare predicted signs and
irreversible-responder sets with RNA-seq of evolved strains by permutation
tests.

## Concepts

- **irreversible perturbation**: a transient knockout or overexpression
  after whose removal the network reaches an attractor different from its
  starting one.
- **irreversible response gene**: a gene whose state differs between the
  initial and the final attractor.
- **origon**: the subnetwork reachable from a root gene with no inputs
  other than itself.
- **core network**: what remains of an origon after recursively removing
  genes with no outgoing edges.
- **positive circuit**: a directed cycle whose product of edge signs is
  positive (an even number of repressions).
- **canalization depth**: the expected number of input states needed to
  fix a rule's output; the paper's measure of nestedness.
- **rule bias**: the probability that a rule outputs 1.
- **concentrated / diffuse control**: input orderings in which the
  regulator with the largest / smallest out-degree tends to canalize.
- **partial fixed point**: a periodic attractor in which some genes are
  constant.

## Connections

The necessity of positive circuits for multiple stable states is René
Thomas's rule, cited (ref. 38) rather than proved anew; the Supplementary
Text adapts it to partial fixed points. The rule ensembles relate to random
Boolean networks with bias (Kauffman's line, refs. 29–30) and to
threshold networks (ref. 31), and the paper says how each corresponds to an
(r, s) setting. The irreversibility argument is the bacterial counterpart of
eukaryotic cell-fate commitment, without chromatin marks. Steering between
attractors is the network-control programme of the senior author's group
(refs. 49–51). The evolution data are from an earlier adaptive-laboratory-
evolution study of crp knockouts (ref. 41).

## Bearing on the record

- **[THEORY-136](../theory.d/THEORY-136.md).** That standard says a lasting shift after a temporary
  disturbance, with slow return excluded, is among the few kinds of evidence
  that come close to showing alternative stable states, and that positive
  feedback must be strong to produce them. This paper defines irreversibility
  as exactly that kind of shift, predicts it across a whole regulatory
  network, and its continuous model agrees that self-activation must be
  strong and switch-like. But by that standard it has not yet shown it: the
  evidence is models, and the one data comparison is evolution under a
  permanent knockout, which is not a temporary disturbance. Its proposed
  CRISPRi experiment is the kind [THEORY-136](../theory.d/THEORY-136.md) asks for, and the authors' own
  caveat (noise turns permanent into long-lived) is [THEORY-136](../theory.d/THEORY-136.md)'s
  slow-return confound.
- **It produces [THEORY-178](../theory.d/THEORY-178.md)**: that regulation alone can make a
  bacterium's expression state depend on its history, with positive circuits
  necessary, filed Proposed with that experiment as its promotion condition.
- **[THEORY-058](../theory.d/THEORY-058.md)** (disorders as self-maintaining symptom loops) and
  the record's ecological alternative-state works ([LIT-726](../literature.d/LIT-726.md), [THEORY-132](../theory.d/THEORY-132.md))
  share the mechanism: a strongly connected positive loop that outlasts its
  trigger. This is my connection, not the paper's; it adds a molecular case
  and changes none of them.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **No transient perturbation was done in cells.** C1–C5 are about the
  model ensemble; C8 is a proposal.
- **The data comparison tests something else.** C6 tests the signed
  network's prediction of the direction of change after a permanent
  knockout and evolution, which needs no multistability. C7 is the only
  test touching irreversibility, and it is weak: 68 of the 86 other core
  genes are irreversible responders to crp knockout, so the reversible
  comparison groups are tiny (2 genes in batch, 8 in chemostat), and in
  batch the reversible genes matched at a higher rate (2 of 2 against 8 of
  9). The paper's own statement that evolving after a permanent knockout is
  "akin to" releasing a transient one is an intuition, not an argument.
- **The p-value formula as printed**, P = 1 − N_exc/N_samp with N_exc the
  number of shuffles exceeding the observed statistic, would give a large P
  for an extreme observation; it reads as a slip for N_exc/N_samp, and the
  reported values are consistent with the latter.
- **The necessary and sufficient conditions are close to definitional.**
  "Some other gene changed while clamped" and "the released state is outside
  the original basin" restate irreversibility in a deterministic map rather
  than give a structural test; the structural content is in C2 and C3.
- **Synchronous updates** produce many period-2 and period-4 attractors;
  about a third of transitions are not shown to survive asynchronous
  updating.
- **Equal weighting of attractors**, most of which may never be visited by
  a cell; the basin and transcription-weighted analyses address this only
  partly.
- **The rule family is restricted** to nested sums of products built in one
  input order; the true rules are unknown, and RegulonDB's network is a
  union over conditions.

## Open questions

- Does a transient crp knockdown, released, leave zraR, melR or rhaRS on
  for many generations in cells, with the environment held fixed and slow
  return ruled out? That experiment would settle C8 and [THEORY-178](../theory.d/THEORY-178.md).
- How long do the predicted states last under noise and division? A
  stochastic model of transcription and translation mapped from the Boolean
  transitions would give lifetimes.
- Is the small-to-large basin direction a general property of such
  networks or of this rule ensemble?
- Would a direct comparison, transient perturbation against permanent
  perturbation plus evolution in the same strain, support the paper's
  "akin to" link between them?
