---
number: 819
status: Read
formerly:
- NOTE-tmpyx2db
paper: LIT-918
title: 'Hopfield — Neural networks and physical systems with emergent collective computational abilities'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the five page images of the PNAS scan in PubMed
    Central (PMC346238, pnas00447-0135 to -0139), viewed at double size
    column by column: abstract, every section, Eqs. 1–13, Figs. 1–2 and
    the 32 references. PMC's PDF link returned a captcha page to this
    client, so the page images on the PMC article page were used instead.
    The paper has no theorems; the one derivation is the energy argument
    (Eqs. 7–8), and the capacity, basin and merging results are Monte
    Carlo simulations at N = 30 and N = 100.
date: '2026-10-14'
summary: >-
  With symmetric couplings, asynchronous threshold updates descend an
  energy function, so Hebbian outer-product storage makes random patterns
  attractors: a cue a few bits off settles into the nearest one. In
  simulations at N = 30 and 100, recall degrades severely near 0.15N
  patterns, memories closer than about a tenth of N fuse, and overload
  makes every memory irretrievable unless old ones are forgotten.
---
<!-- inactive-ok-file: CLAIM-179 CLAIM-180 CLAIM-182 — Proposed; open, and cited as open: the theses of the nucleating-argument line are under test, not settled -->

# NOTE-819: Hopfield — Neural networks and physical systems with emergent collective computational abilities

## Contribution

The paper shows that a content-addressable memory can be a collective
property of many simple units rather than of designed circuitry. A
network of two-state threshold units with Hebbian couplings, updated
asynchronously, has the stored patterns as stable points of its flow, and
a partial or noisy starting state flows to the stored pattern nearest it.
For symmetric couplings it gives an energy function that the dynamics
never increase, which ties the model to Ising spin systems. The rest is
simulation of what the memory can and cannot do: capacity, basins,
merging, categorisation, familiarity and short sequences.

## Key insight

Memory as a flow in state space. "Any physical system whose dynamics in
phase space is dominated by a substantial number of locally stable states
to which it is attracted can therefore be regarded as a general
content-addressable memory" (p. 2554). Retrieval is not a lookup but
settling: the information stored is the set of attractors, a starting
point near one is a partial knowledge of it, and the dynamics supply the
rest.

## Assumptions

- **Units.** Vᵢ ∈ {0, 1}, with a fixed threshold Uᵢ (taken as 0 unless
  stated). Couplings Tᵢⱼ, with Tᵢᵢ = 0 and Tᵢⱼ = 0 for unconnected units.
- **Asynchronous dynamics.** Each unit re-evaluates at random times with
  mean rate W: Vᵢ → 1 if Σⱼ≠ᵢ TᵢⱼVⱼ > Uᵢ, Vᵢ → 0 if < Uᵢ (Eq. 1). No global
  clock, which Hopfield defends as the biologically plausible case.
- **Storage.** Tᵢⱼ = Σₛ (2Vᵢˢ − 1)(2Vⱼˢ − 1), with Tᵢᵢ = 0 (Eq. 2), assumed
  to have been produced by Hebbian experience (Eq. 6).
- **Random memories.** The capacity results assume stored patterns with
  independent random bits, justified as what efficient preprocessing
  would produce. Correlated memories are treated separately (Eqs. 11–12).
- **Symmetry for the energy argument only.** Eqs. 7–8 need Tᵢⱼ = Tⱼᵢ. The
  simulations with random asymmetric Tᵢⱼ are an empirical check, with an
  informal argument that the asymmetric part acts like a finite
  temperature.
- **Small N.** All numbers come from N = 30 and N = 100, which the paper
  itself calls "slightly small" against the 100–10,000 cells it takes as
  typical of cortical circuits.

## Key results

- **Pseudo-orthogonality (Eqs. 3–4).** With pattern s′ in place,
  Σⱼ TᵢⱼVⱼˢ′ = Hᵢˢ′ has mean ≈ (2Vᵢˢ′ − 1)N/2: positive where the bit is 1,
  negative where it is 0. "Except for the noise coming from the s ≠ s′
  terms, the stored state would always be stable." *Holds when:* random,
  uncorrelated patterns.
- **Nonlinearity makes choices (p. 2555).** A linear associative net given
  0.6 S₁ + 0.4 S₂ returns "a generally meaningless mixed output
  0.6 O₁ + 0.4 O₂"; this model "will generate the output O₁" with high
  probability.
- **Energy (Eqs. 7–8).** For Tᵢⱼ = Tⱼᵢ, E = −½ Σᵢ≠ⱼ TᵢⱼVᵢVⱼ and
  ΔE = −ΔVᵢ Σⱼ≠ᵢ TᵢⱼVⱼ, so every update lowers E or leaves it: "State
  changes will continue until a least (local) E is reached." The case is
  "isomorphic with an Ising model", and a random symmetric T is a spin
  glass with many stable states. *Holds when:* symmetric couplings,
  asynchronous updates. This is the paper's one derivation.
- **Asymmetric random couplings (p. 2556).** Tᵢⱼ uniform in [−1, 1],
  N = 30: no ergodic wandering; within about 4/W the state settles, most
  often to a stable state. Of 50 random starts on one matrix, all ended in
  "one of two or three end states". Simple cycles and chaotic wandering
  near one state also occur, with ln M = −Σ pᵢ ln pᵢ giving M = 25
  (Eq. 9). "The flow in phase space produced by this model algorithm has
  the properties necessary for a physical content-addressable memory
  whether or not Tᵢⱼ is symmetric."
- **Capacity (pp. 2556–2557, Fig. 2).** "About 0.15 N states can be
  simultaneously remembered before error in recall is severe." At
  N = 100: n = 5, stored states almost always stable and exactly
  recallable; n = 15, about half evolve to stable states with fewer than 5
  errors, and the rest to states "quite different from the starting
  points". The crosstalk has rms σ = [(n − 1)N/2]^½, approximately
  Gaussian for large nN, so a single bit errs with
  P = (2πσ²)^−½ ∫_{N/2}^∞ e^{−x²/2σ²} dx (Eq. 10). At n = 10, N = 100,
  P = 0.0091 and the chance of a perfect 100-bit state is
  e^−0.91 ≈ 0.40; the simulation gave 0.6. Half the memories well
  retained at n = 0.15N "is expected to be true for all large N". A
  choice of thresholds equivalent to ±1 units doubles storage at a given
  accuracy.
- **Where random starts end (p. 2557).** N = 30, n = 5 (10 nominal stable
  states, counting complements): about 85% of trials end in assigned
  memories, 10% "in stable states of no obvious meaning", and 5% in stable
  states very near assigned memories. The ten assigned states differ in
  likelihood by a factor of 20.
- **Basins (p. 2557).** N = 30, n = 5, starting states made by random
  modification of a memory: for a distance ≤ 5 from the nearest memory,
  that memory is reached more than 90% of the time; beyond, the
  probability "fell off smoothly, dropping to a level of 0.2 (2 times
  random chance) for a distance of 12". "The phase space flow is
  apparently dominated by attractors which are the nominally assigned
  memories", and "the system responds to an ambiguous starting state by a
  statistical choice between the memory states it most resembles".
- **Clipped couplings (p. 2557).** Replacing Tᵢⱼ by its sign: at N = 100,
  n = 9 gives errors like the ordinary rule at n = 12. Analytically the
  signal-to-noise ratio falls by (2/π)^½ and the number of memories at
  fixed error by 2/π. Maximal information at N = 100 is near n = 13,
  about N(N/8) bits, against the N(N/2) a symmetric matrix can hold.
- **Overload and forgetting (p. 2557).** "The addition of new memories
  beyond the capacity overloads the system and makes all memory states
  irretrievable unless there is a provision for forgetting old memories."
  If Tᵢⱼ saturates at 0, ±1, ±2, ±3, only recent memories stay stable, and
  "Memories from the distant past are no longer stable."
- **One-way synapses (p. 2557).** With Tⱼᵢ = 0 whenever Tᵢⱼ ≠ 0, stable
  minima persist; the signal-to-noise ratio falls by 1/√2. Failure is
  "soft": error rises slowly as synapses fail.
- **Merging (p. 2557).** Two random memories at N = 100 lie 50 ± 5 apart.
  With seven random memories and an eighth placed 30, 20 or 10 from one
  of them: at 30 both were usually stable; at 20 the minima were usually
  distinct but displaced; at 10 "the minima were often fused". "Memories
  too close to each other are confused and tend to merge."
- **Unfamiliarity (pp. 2557–2558).** The all-zero state is always stable.
  At threshold 0 it lies high in energy and seldom occurs. A uniform
  threshold makes it a likely end state, reached "by any initial state
  that does not resemble adequately closely one of the assigned memories",
  and so "represents positive recognition that the starting state is not
  familiar". At N = 100, n = 500 (overload by 25), no stored state is
  stable, but familiar and unfamiliar starts are still told apart most of
  the time by the initial processing rate, faster for unfamiliar states.
- **Correlated memories and completion (p. 2558).** A partial new state
  stored on k < N units (Eq. 11) is completed on the rest by the sign of
  Σⱼ CᵢⱼXⱼ, the mean correlations of the other memories (Eq. 12).
- **Sequences (p. 2558).** Adding A Σₛ (2Vᵢˢ⁺¹ − 1)(2Vⱼˢ − 1) (Eq. 13)
  moves the state from Vₛ toward Vₛ₊₁, but "sequences longer than four
  states proved impossible to generate, and even these were not
  faithfully followed".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | With symmetric couplings and asynchronous updates, the dynamics never raise E, so the state ends at a local minimum | strong | derivation, Eqs. 7–8 |
| C2 | Hebbian outer-product storage makes random patterns attractors whose basins return a cue a few bits away | moderate | simulation at N = 30, n = 5, p. 2557 |
| C3 | Recall degrades severely near 0.15N stored patterns, and this scaling holds for large N | moderate | simulation at N = 30 and 100, with the Gaussian crosstalk estimate of Eq. 10 |
| C4 | Loading past capacity makes all memories irretrievable unless old ones are forgotten | weak | stated, with saturating synapses as a forgetting mechanism; no figure |
| C5 | Memories closer than about a tenth of N fuse | moderate | one simulation design at N = 100, p. 2557 |
| C6 | The memory properties survive asymmetric couplings, clipping and one-way synapses, degrading softly | moderate | simulations, with signal-to-noise factors derived for clipping and one-way synapses |
| C7 | With a threshold, a cue resembling no memory falls to a distinct state that signals unfamiliarity | weak | simulation described, no figures |

## Concepts

- **Content-addressable memory.** A memory that returns a whole stored
  item from "any subpart of sufficient size" or a corrupted version of it.
- **Nominally assigned memories.** The patterns written by Eq. 2; whether
  each is in fact stable is what the simulations test.
- **Stable states of no obvious meaning.** End states that are not
  assigned memories, the later literature's spurious states. They occur
  here at a low load (n = 5, N = 30), not only past capacity.
- **Familiarity.** Recognising that a cue resembles no stored memory,
  read either from a dedicated end state (with a threshold) or from the
  initial rate of processing (under overload).

## Connections

Hopfield sets the model against the perceptron (feed-forward, synchronous,
intractable with back-coupling) and the linear associative nets of
Cooper, Kohonen, Anderson and Longuet-Higgins, and against Little and
Shaw's synchronous model. The storage rule is theirs (refs. 15, 16); the
attractor dynamics and the energy function are what this paper adds.
Kanerva's report ([LIT-921](../literature.d/LIT-921.md)) sets sparse distributed memory beside it, citing
Keeler (1988) that the two have the same capacity per storage element,
and puts the 0.15N figure at a bit fidelity of 0.995. Bricken and
Pehlevan's critical distance ([LIT-269](../literature.d/LIT-269.md), read in [NOTE-242](NOTE-242.md)) is the SDM
counterpart of the basin results here.

## Bearing on the record

- **[CLAIM-180](../claims.d/CLAIM-180.md) is supported in its picture of retrieval, with three
  corrections.**
  - **Supported.** The basin result is the dynamical form the claim
    describes: from within about 5 bits of 30 the nearest memory is
    retrieved more than 90% of the time, and by 12 bits the chance is 0.2.
    An ambiguous cue is resolved "by a statistical choice between the
    memory states it most resembles", which is the claim's silent
    redefinition: a cue near two memories may settle into the wrong one.
  - **Corrected: merging comes from closeness, not from load.** The claim
    puts "merged and confused ideas" under capacity. The paper separates
    two failures. Memories closer than about a tenth of N fuse at any
    load. Past capacity, retrieval fails for all memories at once, not by
    merging. "Many near-duplicate statements" names the first failure,
    and that is the one the paper shows best.
  - **Corrected: spurious states are not a symptom of overload.** At
    n = 5, N = 30, far below capacity, 10% of random starts end in "stable
    states of no obvious meaning". The claim, and the takeaways on [LIT-918](../literature.d/LIT-918.md)
    before this reading, tie them to a load past 0.15N.
  - **Not in the paper: "taken for new".** The network never treats a cue
    as new. A cue far from every memory settles somewhere else, or, with
    a threshold, into a state that signals unfamiliarity. The record's
    analogue of re-derivation as though new is closer to the second:
    failing to recognise, not storing a duplicate. Whether a duplicate is
    then written is outside the model.
  - **Codes are outside the model.** The paper has no addresses. The
    claim's contrast between content and code needs Kanerva's RAM limit
    ([LIT-921](../literature.d/LIT-921.md)), not Hopfield.
- **[CLAIM-179](../claims.d/CLAIM-179.md) (flooding).** [LIT-918](../literature.d/LIT-918.md)'s standing says the capacity limit
  bears on flooding because stored items "interfere and spurious ones
  appear". The paper's statement is stronger and different: overload
  "makes all memory states irretrievable unless there is a provision for
  forgetting old memories", and with saturating synapses the recent are
  kept and the distant past is lost. Read across, a record past its load
  would lose access to its old entries rather than blur them, unless it
  forgets. The record's design (retire by status, never delete) is a
  provision against forgetting, so the analogy, if it holds at all, cuts
  the other way. This is analogy, and the paper offers nothing about
  records.
- **[CLAIM-182](../claims.d/CLAIM-182.md).** Nothing direct. The model shows what storage without
  addressing can do, not what addressing adds.
- **Filed from this reading:** [THEORY-272](../theory.d/THEORY-272.md), the attractor account
  with its capacity, basin and merging limits, held to the simulation
  sizes the paper used.
- **Anthology.** The `anthology-candidate` flag stays: the paper is a
  neural-network model and the anthology already holds Kanerva's family.
  It carries no instruction for machine-learning practice.

## Limitations

- Every quantitative result is from simulations at N = 30 or 100, with no
  error bars and, for several (clipping, merging, familiarity), no figure.
- The 0.15N figure is the load at which about half the memories are well
  retained, not a sharp threshold, and the paper's "expected to be true
  for all large N" rests on the Gaussian estimate, not on a proof.
- The energy argument holds only for symmetric couplings; the asymmetric
  case rests on simulations and an informal finite-temperature argument.
- The biological interpretation (firing-rate thresholds, Hebbian
  synapses, delays folded into 1/W) is offered as motivation, not tested.

## Open questions

- How the basin radius scales with N and load is not given here; only one
  basin curve, at N = 30, n = 5, is reported.
- Whether the factor-of-20 spread in how often each memory is reached
  reflects basin size, and what sets it, is not examined.
- The sequence result (at most four states) is left as a failure; whether
  it is a limit of Eq. 13 or of the model is open in the paper.
