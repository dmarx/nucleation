---
number: 978
status: Read
formerly:
- NOTE-tmpjq49q
paper: LIT-1260
title: 'Crutchfield and Shalizi — Thermodynamic depth of causal states'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from arXiv:cond-mat/9808147v1 (13 August 1998, the only
    arXiv version, titled "Thermodynamic Depth of Causal States: When
    Paddling around in Occam's Pool Shallowness Is a Virtue"), text
    extracted with pdftotext. Read: Sections I–VIII, with VII A–C and
    their proofs, both footnotes, the transition matrices (23)–(26) and the
    references. The figures were read from captions, the extracted edge
    labels and the text. Equations with arrows over S were partly garbled,
    and were reconstructed from the surrounding prose. The published
    version (Phys. Rev. E 59:275–283, 1999, under a different title) was
    not compared, and may correct some of the errors listed below. Every
    number in the logistic-map example was recomputed in the scratchpad.
    So was the counterexample to the claim that v < C_μ.
date: '2026-10-20'
summary: >-
  The rate at which Lloyd and Pagels' thermodynamic depth grows (the dive)
  is the entropy rate of whatever macrostate process it is computed over.
  So depth measures randomness. Lumping or splitting macrostates sets it to
  any value from zero up. The paper proposes the causal states as the
  macrostates. Among partitions of the past that predict the future as well
  as the past does, they are the coarsest, with the least statistical
  complexity and the least dive ([THEORY-756](../theory.d/THEORY-756.md)). Several errors are
  noted. One stated entropy rate is in fact a single-symbol entropy, a
  footnote makes prescience vacuous, and a strict inequality fails in
  general. The result survives. The "objectivity" is relative to the
  measuring instrument, as the paper's own logistic-map example shows.
---
<!-- inactive-ok-file: THEORY-157 THEORY-257 — Proposed; readings this note connects to, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-1126 — Deferred; the authors' later treatment, registered unread -->
# NOTE-978: Crutchfield and Shalizi — Thermodynamic depth of causal states

## Contribution

It shows that thermodynamic depth's average growth rate is a plain
entropy rate, so depth does not separate structure from randomness. It
locates the failure in the unconstrained choice of macrostates. It then
proposes a fix: compute depth over the causal states. It proves that these
are the coarsest states that predict the observed future as well as the
whole past does, so that no equally predictive choice has smaller entropy
or smaller dive.

## Key insight

A complexity measure defined over "the macrostates" has no value until the
macrostates are fixed. Fixed by convenience, it can be driven to zero by
lumping and to anything by splitting. Constraining the choice by
minimality alone is useless, because one state is minimal. Constraining it
by predictive sufficiency first, and minimality second, selects one
partition: the causal states. Shallowness then becomes a virtue (the
arXiv title) rather than a symptom of a lumped description.

## Assumptions

- A stationary (time-translation-invariant) process over a finite alphabet
  A of measured values. This is a finite-precision instrument applied to an
  unobserved microscopic process.
- Rival state sets R are partitions of the observed past, "determinable
  from observed sequences", using "only the past history of observables".
- Prescience is equality of the future's conditional entropy given the
  states, H[S→|R̂] = H[S→|S]. Footnote 2 replaces it, when infinite, by the
  per-symbol limit of H[S→^L|R]/L. That replacement is wrong (see
  Limitations).
- The section VII results need only a probability measure over the causal
  states, not a finite ε-machine.

## Key results

- **Depth (9)–(11).** Lloyd and Pagels' L-depth averaged over macrostates
  is D_L = H[S_{−L+1}, …, S_{−1} | S_0]: the uncertainty of the
  (L − 1)-step history given the present macrostate.
- **Dive (12)–(22).** v ≡ lim_{L→∞}(D_L − D_{L−1})
  = lim H[S_{−L+1} | S_{−L+2}, …, S_0] = h_μ (reverse-time entropy rate).
  For a stationary process this equals the forward rate, so v = h_μ, the
  entropy rate of the macrostate process. Also v ≤ H[S_0] (18). Re-derived
  here; correct.
- **What the choice of macrostates does (Section V).** The paper shows five
  things.
  - Lumping all states into one gives depth 0.
  - Treating one state as n equiprobable degenerate states adds a term
    proportional to log n. Repeating this, the depth can be made "as large
    as we like".
  - Coarse-graining the observables does not settle the choice, since the
    link between instrument and process is "often obscure".
  - Three examples show the effect.
    - **Fig. 1:** an IID uniform three-symbol chain. Here
      v = log₂ 3 although the process is purely random.
    - **Fig. 2:** a three-state hidden chain whose output is a fair coin.
      The hidden states and the observables both deepen at 1 bit per step.
      "Rube Goldberg" automata with ever more states give the same
      observed process.
    - **Fig. 3:** the logistic map x ↦ 4x(1 − x) observed through a binary
      partition at x̂ (the largest pre-image of 1/2), which is not
      generating. The three hidden states have entropy rate 1 bit, higher
      than that of the observables. Through a generating partition there
      is a single state.
- **The proposal (Section VI).** Redefine depth and dive over the causal
  states, the classes of pasts with the same conditional distribution of
  futures (27). The dive becomes the entropy rate of the causal-state
  process, h_μ^S = H[S′|S], and v ≤ C_μ = H[S]. On the three examples:
  - Fig. 1 → one causal state, v = C_μ = 0.
  - Fig. 2 → one causal state, v = C_μ = 0.
  - Fig. 3 → countably many causal states, indexed by the number of a's
    since the last b, with v ≈ 0.677867 and C_μ ≈ 2.71147 bits. Both
    figures were recomputed here: 0.6778672 and 2.7114687.
- **Optimality (Section VII).**
  - **A.** H[S→|R] ≥ H[S→|S] for every partition R of the past.
  - **B.** Every prescient rival R̂ refines the causal states, so S = g(R̂)
    and C_μ = H[S] ≤ H[R̂].
  - **C.** H[R̂′|R̂] ≥ H[S′|S], read as "nothing as prescient as an
    ε-machine has a smaller dive". The proof uses unifilarity,
    H[S′|S, S] = 0, and that (S′, S) is a function of (R̂′, R̂).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The dive of thermodynamic depth is the macrostate process's entropy rate, so depth measures randomness | strong | (12)–(22), re-derived |
| C2 | By choice of macrostates the depth can be given any value from 0 up | strong in substance | lumping and n-fold splitting arguments, Section V. Any real value follows by splitting with unequal weights, which the paper does not spell out |
| C3 | Lloyd and Pagels' examples get their intended results by choosing macrostates suited to them, from outside the definition | moderate | Section V. Asserted against the 1988 paper, which is not in this record |
| C4 | No partition of the past predicts the future better than the causal states | strong | VII A |
| C5 | Every equally predictive partition refines the causal states, so they have least statistical complexity | strong under prescience at every finite L. Fails under footnote 2's normalization | VII B. The "mixing increases uncertainty" step is informal, and is made rigorous in [THEORY-756](../theory.d/THEORY-756.md) |
| C6 | No equally predictive partition has a smaller dive | the result is true; the proof as written has a gap | VII C. See Limitations |
| C7 | v < C_μ whenever the observed process has any past–future mutual information | false in general | Section VI, citing Eq. (106) of Feldman and Crutchfield. See Limitations |
| C8 | Redefined over causal states, depth is "objective" (published title) and its ambiguities are removed | overstated | the logistic-map example shows dependence on the measuring partition |

## Concepts

- **Thermodynamic L-depth of a state s**: H[S_{−L+1}, …, S_{−1}, S_0 = s | s].
  It is the information needed to identify the trajectory given that it
  ended in s (Lloyd and Pagels).
- **Dive**: the asymptotic growth rate of depth, lim (D_L − D_{L−1}). The
  paper's coinage.
- **Causal state**: a class of pasts with the same conditional distribution
  of futures, (27). **ε-machine**: the causal states with their labelled
  transitions.
- **Statistical complexity C_μ**: H[S], the entropy of the causal-state
  distribution.
- **Prescient rival R̂**: a partition of the past with
  H[S→|R̂] = H[S→|S].
- **Occam's pool**: the set of all partitions of the past that are
  candidate state sets.
- **Unifilar ("deterministic")**: the current state and the next symbol fix
  the next state.

## Connections

It argues against Lloyd and Pagels (1988), not held in this record, and
Landauer's 1988 commentary. It builds on Crutchfield and Young (1989) and
Crutchfield (1994) for causal states, and on Feldman and Crutchfield's
spin-chain paper for C_μ and E. Its section VII is the predictive analogue
of the classical fact that a minimal sufficient statistic is a function of
every sufficient one. The authors restate the optimality results for the
memoryless case in [LIT-1240](../literature.d/LIT-1240.md) ([NOTE-976](NOTE-976.md)). The full treatment is in
their "Computational Mechanics" ([LIT-1126](../literature.d/LIT-1126.md), unread).

## Bearing on the record

- **[CLAIM-152](../claims.d/CLAIM-152.md).** Strong support, and a second parameter. The causal states
  remove the arbitrariness only after two things are fixed. One is the
  target, the whole future of the observables. The other is the
  instrument, the alphabet A that defines "the observables". The paper's
  logistic map gives two ε-machines for one dynamical system: through a
  generating partition, one state with C_μ = 0; through the partition at
  x̂, countably many states with C_μ ≈ 2.71 bits. The paper concedes "the
  measurement dependency of both randomness and complexity" in Section V,
  and calls the redefined depth objective. Both hold only once the
  instrument is fixed. Recommended as a note on [CLAIM-152](../claims.d/CLAIM-152.md): sufficiency
  individuates relative to a target, and the target is relative to an
  instrument.
- **[THEORY-157](../theory.d/THEORY-157.md).** The causal-state map is the minimal sufficient statistic
  of the past for the future, and VII B is the classical "minimal
  sufficient is a function of every sufficient statistic". The record's
  proof ([THEORY-756](../theory.d/THEORY-756.md)) goes through the conditional independence of the
  future and the past given S, the Markov-category form of predictive
  sufficiency. Nothing here bears on [THEORY-157](../theory.d/THEORY-157.md)'s promote_when.
- **[QUESTION-220](../questions.d/QUESTION-220.md).** Section VII B is a nesting result at one budget
  only. All equally predictive partitions lie above the causal states in
  the refinement order, so the causal states are the bottom of the
  prescient part of Occam's pool. The paper has no trade-off parameter
  and nothing on partial prediction, so it says nothing about nesting
  across budgets. A Lloyd–Pagels-style depth defined over the IB optima at
  finite β would be a natural object for that question. This is not in
  the paper.
- **[QUESTION-217](../questions.d/QUESTION-217.md).** Section VII B fixes the refinement order's
  relation to prediction: among states that keep all predictive
  information, refinement only adds entropy (C_μ) and entropy rate (dive).
- **[THEORY-257](../theory.d/THEORY-257.md) and [NOTE-791](NOTE-791.md).** Dynamical independence asks that a coarse
  variable's own past predict its future as well as the microscopic past
  does. The causal states are the minimal states that make the observed
  process's own past fully predictive. The two notions differ in which
  past is conditioned on (the micro past or the macro past). [NOTE-791](NOTE-791.md)
  already names Shalizi and Moore's causal states as a neighbour.
- **[QUESTION-218](../questions.d/QUESTION-218.md).** A candidate unit with a built-in criterion:
  the classes of histories, not subsets of variables.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Fig. 1's depth.** The text says D_L = L log₂ 3. Under (11), D_L
  conditions on S_0 and covers L − 1 symbols, so D_L = (L − 1) log₂ 3 and
  D_1 = 0. The dive is unaffected.
- **The logistic-map dive, 0.811, is wrong.** The text gives the
  observables' dive as "v ≈ 0.811 bits per step". That is
  h(1/4) = 0.8113 = H[S_0], the single-symbol entropy. Pr(b) = 1/4, from the
  hidden stationary distribution (1/4, 1/2, 1/4) recomputed here from
  (25)–(26). It is not the entropy rate. Block-entropy differences of the
  observed process converge to 0.677867, the figure the paper later gives
  for the causal-state dive. So in this example the redefined dive equals
  the observed dive rather than lowering it. The paper's point that the
  hidden states (1 bit per step) are "worse" than the observables survives
  with the correct number.
- **The redefined dive is still a randomness rate.** For any ε-machine,
  unifilarity and prescience give
  h_μ^S = H[S′|S] = h_μ − H[next symbol | S, S′]. Here h_μ is the
  observed entropy rate. The second term is the part of each symbol that
  the state transition does not record. This identity is the record's,
  from the paper's (36)–(41). So the new dive is the observed entropy rate
  minus what the causal states forget. It vanishes for IID processes, the
  paper's examples, and it equals h_μ whenever distinct symbols lead to
  distinct successor states, as in the logistic-map example. The
  redefinition removes the arbitrariness of the macrostates. It does not
  make dive a measure of structure, in the way C_μ is one.
- **Footnote 2 makes prescience vacuous.** If H[S→|R] is infinite, the
  footnote compares rivals by lim H[S→^L|R]/L. But for any R with finite
  entropy, H[S→^L] − H[R] ≤ H[S→^L|R] ≤ H[S→^L]. So that limit is h_μ for
  every such R, the one-state partition included. Under the footnote every
  finite-entropy partition is "prescient", and VII B fails. The repair is
  to require H[S→^L|R̂] = H[S→^L|S] for every finite L, which is how the
  authors state it in [LIT-1240](../literature.d/LIT-1240.md), Section III.
- **The proof of VII C has a gap.** It proves H[R̂′|R̂] ≥ H[S′|S]. The
  rival's dive is its entropy rate, and that equals H[R̂′|R̂] only if the
  rival's state process is Markov. Otherwise the rate can be smaller. The
  conclusion still holds, by a shorter argument. The causal-state sequence
  is a symbol-by-symbol function of the rival's sequence, so its block
  entropies, and hence its entropy rate, are no larger ([THEORY-756](../theory.d/THEORY-756.md)).
- **C7 is false in general.** Take two causal states, 0 and 1, and four
  symbols. From 0 the process emits a (to 0) or c (to 1); from 1 it emits
  b (to 0) or d (to 1); each with probability 1/2. Then the two states
  have different futures. The state sequence is IID, so
  v = H[S′|S] = 1 bit = C_μ, while the excess entropy is E = 1 bit
  (computed here from block entropies). The cited identity
  C_μ = E + R h_μ holds for order-R spin chains whose causal states are
  the R-blocks. There E > 0 does give v < C_μ, but that is not the
  general case.
- **VII B's "mixing can only increase uncertainty"** is the right idea,
  stated informally. It needs strict concavity, positive probability of
  both parts, and an "almost surely" (the uniqueness qualification the
  authors add in [LIT-1240](../literature.d/LIT-1240.md)'s footnote 3).
- **Lloyd and Pagels are paraphrased, not checked here.** C3 rests on
  page-cited readings of a paper this record does not hold.
- **Total depth is set aside** as "most likely" incalculable. The proposal
  redefines the dive, not a finite depth.

## Open questions

- Is there a dive-like rate over causal states that vanishes for both
  periodic and IID processes and is positive for structured ones? h_μ^S is
  zero for IID and for periodic processes, and it equals h_μ for the
  logistic map. Is it ever a useful measure of structure apart from C_μ?
- How do the causal states, C_μ and h_μ^S change as the measuring
  partition is refined, from non-generating to generating? The paper shows
  two points of that path. The question is [QUESTION-220](../questions.d/QUESTION-220.md)'s, asked of
  the instrument rather than the encoder.
