---
status: Read
paper: LIT-tmpdsowv
title: 'Natschläger, Bertschinger & Legenstein — At the Edge of Chaos: Real-time Computations and Self-Organized Criticality in Recurrent Neural Networks'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    From the publisher's open proceedings PDF (proceedings.nips.cc, NIPS
    17, 8 pp.), fetched 2026-11-22 without obstacle, text extracted with
    pdftotext. Read in full: abstract, §§1–7, footnotes, references;
    figures read from their captions and axis labels only. Read as a
    stand-in for Bertschinger and Natschläger (2004), LIT-2991, which
    could not be reached (ADR-114). The mean-field supplement the paper
    cites as its ref. [8] (igi.tugraz.at/tnatschl/edge-of-chaos/mean-field-supplement.pdf)
    redirects to a 404 at tugraz.at, and the old host igi-web.tugraz.at
    reset the TLS connection on 2026-11-22; it was not read. Read by a
    reader subagent; filed by a second one, which rechecked every quote
    used here against the extracted text. No email address sent.
date: '2026-11-22'
summary: >-
  Driven random threshold networks have an order-to-chaos line where a
  single flipped input bit flips on average one node (K·P_bf = 1); order
  is fading memory, chaos leaves "spurious" information about initial
  conditions in the state; a separation measure corrected for both peaks
  near the line, and so does a linear readout's performance averaged over
  many nonlinear tasks of recent inputs. A local synaptic-scaling rule
  brings networks to the line.
---
<!-- inactive-ok-file: LIT-2991 NOTE-tmpt3dxa ARG-tmp2zz6k CLAIM-809 CLAIM-814 CLAIM-850 ARG-148 ARG-128 THEORY-2041 THEORY-tmpye6xs THEORY-2158 — Unavailable, Proposed or new; the work this stands in for, the reading, the supplement and the entries it bears on -->

# NOTE-tmpi5t3r: Natschläger, Bertschinger & Legenstein — At the Edge of Chaos: Real-time Computations and Self-Organized Criticality in Recurrent Neural Networks

## Contribution

The order-to-chaos transition computed analytically for networks driven
by an input, not autonomous ones, and tied empirically to real-time
computation with a trained linear readout; a predictor of that
computational power (NM-separation, "we propose a novel complexity
measure (Sec. 4)"); and a local rule that self-organizes networks to the
transition.

## Key results

- **The critical line** (§3, Eq. 1). Following Derrida and Pomeau, two
  states under the same input; the slope α* of the Hamming-distance map
  at d = 0 decides the phase: "ordered, critical or chaotic regime if
  α* < 1, α* = 1 or α* > 1". The line α* = 1 is K·P_bf = 1, "where Pbf
  denotes the probability (averaged over the inputs and the network
  activity) that a node will change its output if a single out of its K
  input bits is flipped". §6 restates it: critical dynamics "are achieved
  if the probability Pbf that a single bit-flip in the input shows up in
  the output should on average ... be equal to 1/K".
- **Activity is not the order parameter** (§2): with weights of arbitrary
  mean, "the network activity ... can vary considerably for different
  parameters (compare Fig. 1)"; Fig. 1 shades the (µ, σ²) plane by mean
  activity a*, with the critical line drawn across it.
- **Order is fading memory; chaos pollutes the state** (§3): fading
  memory "is equivalent to the requirement that all state differences
  vanish, i.e. being in the ordered phase"; in the chaotic regime "a
  given network state xt also contains “spurious” information about the
  initial conditions and hence it is hard or even impossible to deduce
  any features of the recent input."
- **NM-separation** (§4, Eq. 2): NM_sep = s* − f* − i*, separation due to
  input differences less that due to initial states (f*) and to an
  all-dominant input drive (i*). "Note that the N M -separation peaks very
  close to the critical line." The values are numerical (fn. 4: "Hopefully
  these numerical estimates can be replaced by analytic results in the
  future").
- **Computation near the line** (§5, Fig. 3): tasks are delayed 3-bit
  parity and 50 random Boolean functions of the last 5 inputs; performance
  is MC = Σ_τ I(v, y^(τ)). "The highest performance is clearly achieved
  for parameter values close to the critical line where the phase
  transition occurs." The design is task-averaged: "the networks used here
  are not optimized for any specific task but their computational
  capabilities are assessed by evaluating them for many different tasks.
  Therefore a network that is specifically designed for a single task will
  not show a good performance in this setup."
- **Self-organized criticality** (§6, Figs. 4–5): each node estimates its
  P_bf from its margin and scales its weights toward P_bf = 1/K; networks
  started in either phase move to the line and their MC rises.
- **Conclusion as worded** (§7): the results "support the hypothesis that
  dynamics near the critical line are expected to be a general property of
  input driven dynamical systems which support complex real-time
  computations."

## Assumptions

Annealed mean-field approximation; fixed in-degree K (5 or 10), i.i.d.
Gaussian weights of mean µ and variance σ²; an i.i.d. binary input, ū + 1
with probability r, else ū, injected into every node; synchronous update;
N = 500 in the figures; a linear threshold readout trained per task;
tasks needing memory of a few steps only. The "edge of chaos" is the
damage-spreading transition of a deterministic driven map.

## Concepts

Edge of chaos; annealed approximation (Derrida–Pomeau); Hamming distance
and damage spreading; fading memory; separation property; liquid state
machine; NM-separation; bit-flip probability P_bf; synaptic scaling.

## Bearing on the record

How far it stands in for [LIT-2991](../literature.d/LIT-2991.md). It restates the article's programme
and cites it for the experimental details ("for details see [4]", §5); it
does not restate the article's own model (zero-mean weights), its
figures or its caveats, and its NM-separation and SOC rule are new to it.
The article's abstract, read from PubMed, carries the headline both share:
"only near the critical boundary can such networks perform complex
computations on time series".

- **[CLAIM-809](../claims.d/CLAIM-809.md)**: qualifies, and its strand 1 is supported. The headline
  "only near" is the universal reading the thesis rejects, but the optimum
  is task-averaged by design and no per-task optima are reported, so the
  defeater (every component maximized at the transition for every task)
  is not met ([ARG-tmp2zz6k](../arguments.d/ARG-tmp2zz6k.md)). Strand 1's mechanism is chaos polluting the
  state with initial conditions, not readout noise. The "Misattribution"
  bullet is corrected in place: these three are A's named authors.
- **[QUESTION-507](../questions.d/QUESTION-507.md), point 1**: the line K·P_bf = 1 says one flipped node
  flips on average one node in the next step, a branching ratio of one
  for perturbations (damage), not for activity, which varies along the
  line. That reading of Eq. 1 is the filer's and the reader's inference,
  not the paper's. It is a step relating the edge of chaos to branching
  criticality by the form of their order parameter, not an identification.
- **[CLAIM-850](../claims.d/CLAIM-850.md)**: a mechanism where an order–chaos edge is a branching
  condition of perturbations (same inference).
- **[CLAIM-814](../claims.d/CLAIM-814.md)**: contrast; in the scalar linear model there is no chaotic
  side, and here the cost past the edge is loss of fading memory.
- **[ARG-148](../arguments.d/ARG-148.md)**: background; the nonlinear tasks it says its case leaves
  untouched are the tasks here, but no bounded capacity is shown
  redistributed.
- **[THEORY-tmpye6xs](../theory.d/THEORY-tmpye6xs.md)**: contrast; opposite transition and opposite
  outcome (finite-window optimum subcritical there, near the order–chaos
  line here).
- **[ARG-128](../arguments.d/ARG-128.md)**: background; the edge's value that Dambre and colleagues
  carry in from Langton has its empirical support in driven networks here,
  and Langton (1990) is this paper's ref. [1] too.
- **[THEORY-2041](../theory.d/THEORY-2041.md)**: parallel; the same Derrida-style two-trajectory mean
  field, for recurrent, driven, binary networks rather than deep
  feedforward ones.
- **[THEORY-2158](../theory.d/THEORY-2158.md)**: contrast, reported to the lead (another filer's
  entry): a task-family performance, not a total capacity, so no conflict
  with Dambre's bound.
- **[QUESTION-508](../questions.d/QUESTION-508.md)** (untuned scale invariance) and **[LIT-1139](../literature.d/LIT-1139.md)** (Gross and
  Blasius): §6 is self-organization to the edge by a local adaptive rule,
  after Bornholdt and Röhl (2003), not held. Reported to the lead.

Calvet, Reulet and Rouat ([LIT-tmpahs2x](../literature.d/LIT-tmpahs2x.md), [NOTE-tmpt3dxa](NOTE-tmpt3dxa.md)), a later RBN
reservoir study read for one passage, qualify the "only near" result.

## Limitations

- The article itself ([LIT-2991](../literature.d/LIT-2991.md)) is unread beyond its abstract.
- Mean-field (annealed) theory; NM-separation is numerical; N = 500.
- "Near the line" is read off interpolated gray-scale images (Fig. 3
  caption: "an interpolation between the data points").
- One input statistic; tasks with a few steps of memory; no total
  capacity and no per-task optima, so no allocation can be read off.
- §6 says "the computational capabilities of a network depend crucially
  on having almost critical dynamics", which the task-averaged design
  shows for its average, not for every task.

Not held, cited, possibly worth registering: Langton (1990), Derrida and
Pomeau (1986), Derrida (1987), Maass, Natschläger and Markram (2002),
Jaeger and Haas (2004), Bornholdt and Röhl (2003), and the mean-field
supplement (unreachable). None is relied on here, so none is registered.
