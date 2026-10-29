---
status: Read
paper: 'LIT-tmpr2bnp'
title: 'Eberhardt and Lee — Causal emergence: when distortions in a map obscure the territory'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from the publisher's PDF (MDPI, CC BY,
    15 pages) as deposited in Caltech's repository
    (https://authors.library.caltech.edu/records/q1rr1-m4198/files/philosophies-07-00030.pdf),
    text extracted with pdftotext. The publisher's own link
    (https://www.mdpi.com/2409-9287/7/2/30/pdf) returned Access Denied to
    this client. Read: the abstract, §§1–6, Appendix A, the 11 notes and
    the 16 references. Figure 1 is a schematic, read from its caption.
    Checked by a record script on 2026-10-29: the EI of every matrix the
    paper prints in (11), (13), (14), (15) and (17), the square of (17),
    the exhaustive EI search over partitions for (14), its variant with
    first row (0.8, 0.1, 0.1), (17), (17)² and note 6's matrix, and the
    row sums of (13). Hoel 2017, the paper criticized, was not read; its
    definitions are taken as this paper restates them.
date: '2026-10-29'
summary: >-
  Under Hoel's effective information, with uniform interventions at each
  level and macro interventions as uniform averages over micro states,
  the EI-optimal coarse-graining can merge micro states whose effects
  differ widely, so the macro variable has ambiguous manipulations; and
  the EI-optimal abstraction of a two-step matrix differs from the square
  of the one-step abstraction, so abstraction and marginalization do not
  commute. Both are traced to the maximum-entropy distribution, which the
  authors call extraneous to the system. The numbers check.
---
<!-- inactive-ok-file: THEORY-787 — Proposed; the causal thesis this reading bears on, cited as open -->
<!-- inactive-ok-file: QUESTION-204 QUESTION-115 QUESTION-252 — Open; the questions this reading bears on, cited as open -->

# NOTE-tmp0q96y: Eberhardt and Lee — Causal emergence: when distortions in a map obscure the territory

## Contribution

A critique of Hoel's 2017 account of causal emergence on two desiderata
any account of multi-scale causation should meet: macro variables
without (much) ambiguity of manipulation, and abstraction that commutes
with marginalization over time. It gives numerical examples where EI
maximization fails each, and locates the cause in the maximum-entropy
intervention distribution and the averaging steps.

## Key insight

EI is mutual information under an input distribution the analyst
supplies. A uniform distribution over macro states, each realized as a
uniform average of its micro states, is a non-uniform distribution over
micro states. So which coarse-graining wins depends on that injected
distribution, not only on P(Y | do(X)). An account built on the
interventional conditionals alone, as in Chalupka et al.'s causal
feature learning, avoids both failures.

## Assumptions

- A discrete micro state space with a transition matrix read as
  P(Y | do(X)): no hidden variables, one-step transitions. No marginal
  P(X) is given.
- Hoel's set-up: cause and effect share a state space and are coarsened
  together; EI(X → Y) = I(X; Y) with X uniform (eq. 7); a macro
  intervention do(U = u) is the uniform average of do(X = x) over x ∈ u
  (eq. 8); causal emergence is a strict coarsening maximizing EI, the
  maximum being the causal capacity (eq. 10).
- Distances between rows (absolute, squared Euclidean, max and min
  component difference, symmetrized KL) to say how different two merged
  states are.

## Key results

- **Hoel's examples.** (11): micro EI "0.55", macro {1–7, 8} EI 1. The
  record's computation gives 0.544 for the micro. (13): micro EI 0.81
  (checked, 0.806), macro 1; rows sum to 1.
- **Ambiguity (§3).** The 3×3 matrix (14), rows (0.7, 0.1, 0.2),
  (0.4, 0.5, 0.1), (0, 0, 1), has micro EI 0.6787 and is maximized by
  merging x₁ and x₂, macro EI 0.6788 (checked: 0.67867 against
  0.67879), though the merged rows are at absolute distance 0.8.
  Changing the first row to (0.8, 0.1, 0.1) keeps the micro (checked:
  0.761 against 0.758), though x₁ and x₂ still look more alike than
  either does like x₃. Appendix A lists matrices on the 0.1 grid where
  the merged rows are far apart under each distance.
- **Non-commutativity (§4).** For (17), rows (0.3, 0.2, 0.5),
  (0.4, 0.1, 0.5), (0.5, 0.5, 0): A(T²) keeps all three states (EI
  0.0524), while A(T)² is the 2-state [[0.75, 0.25], [0.5, 0.5]] (EI
  0.0488). Checked exactly. "Only very specific transition probability
  matrices satisfy commutativity", which is asserted, not shown.
- **Note 6.** With rows (0, 0.2, 0.8), (0, 0, 1), (0, 0, 1), EI keeps
  x₂ and x₃ apart although their rows are identical (checked: 0.113
  against 0.052), because cause and effect must be coarsened together.
- **§5.** Causal capacity is like channel capacity, a normative quantity
  about an optimal input that the system need not use, so Hoel's is an
  account of potential, not actual, emergence. The EI-maximizing
  partition need not be unique; two incomparable maximizing partitions
  are conjectured, not found (note 11).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | EI maximization can merge micro states with very different effects | strong | (14) and Appendix A, numerical, checked |
| C2 | The EI-optimal abstraction does not commute with two-step marginalization | strong for the example | (17), checked |
| C3 | Commutativity fails for most matrices | weak | asserted, no count or proof |
| C4 | Both failures come from the maximum-entropy input distribution | moderate | argument; no computation under any other distribution |
| C5 | Causal capacity is normative: it describes potential, not actual, emergence | moderate | analogy with channel capacity and Hoel's own passage |
| C6 | Two incomparable EI-maximizing partitions can exist | weak | conjecture (note 11) |

## Concepts

- **Ambiguous manipulation** (Spirtes and Scheines): an intervention on a
  macro variable whose effect depends on which micro realization is set,
  as total cholesterol with HDL and LDL.
- **Proportional cause** (Yablo): the coarsest description of the cause
  that screens off finer ones from the effect, i.e. all of whose
  interventions are unambiguous.
- **Commutativity of abstraction and marginalization**: A(T × T) =
  A(T) × A(T), eq. (16).
- **Causal capacity**: max EI over coarsenings, eq. (10).

## Connections

It criticizes Hoel 2017 ("When the map is better than the territory",
not registered), the successor of Hoel, Albantakis and Tononi 2013
(LIT-1038, THEORY-222). The commutativity demand is credited to
Rubenstein et al. (LIT-1334) and Beckers and Halpern (LIT-1316), whose
consistency conditions are stronger; the alternative it recommends is
Chalupka, Perona and Eberhardt's causal feature learning (not
registered). It cites Rosas et al.'s "Reconciling emergences"
(LIT-1244) and Aaronson's blog post for similar concerns, and Dewhurst
2021 for the epistemic reading. The defenders' replies the record holds
are CE 2.0 (LIT-1136, NOTE-1387), which answers the uniform-intervention
criticism, and Zhang et al. (LIT-1129, NOTE-1399), which answers
ambiguity and non-commutativity with a 3×3 example. Comolatti and Hoel
2022 (LIT-tmpzfaqi) answers the same criticism by moving to other
measures.

## Bearing on the record

- **THEORY-787 and QUESTION-204.** The triage expected the published
  case that the EI advantage is an artefact of the uniform choice. The
  paper argues that, and shows two consequences of the choice, but it
  does not run the test QUESTION-204 asks for. Nowhere does it compute
  EI with one distribution over micro states at both levels. That test
  needs no example: under any single micro distribution, the macro EI is
  I(f(X); f(Y)) ≤ I(X; Y) by data processing, so the advantage cannot
  survive (THEORY-tmphfpe7). The paper supplies the diagnosis and the
  record's derivation supplies the proof. Together they meet
  THEORY-787's "in trouble if" clause for EI.
- **QUESTION-204, second half.** Example (14) is a small case of the
  disagreement the question asks about. An interventionist test of
  realization insensitivity (Yablo's proportionality, THEORY-133's) would
  keep x₁ and x₂ apart. Their effects on the macro effect variable still
  differ (0.8/0.2 against 0.9/0.1), and EI merges them. It is a
  hand-built 3×3 matrix, so by the question's own terms it cannot settle
  agreement in general. It does show that the EI-optimal level and a
  proportionality test can come apart.
- **The paper's own examples, corrected.** (13)'s merged states are
  ambiguous only for the micro effect Y. Every one of states 1–7 sends
  all its mass into the block {1–7}, so for the macro effect V, the
  variable it is scored on, the manipulation is unambiguous. The partition
  is strongly lumpable. The ambiguity charge stands on (14), not on (13).
  The commutativity example is the same kind of case: {x₁, x₂} is a
  strongly lumpable partition of (17), since both rows send 0.5 into
  each block. A(T)² equals the {x₁, x₂} coarsening of T², the same
  matrix [[0.75, 0.25], [0.5, 0.5]]. So the coarse-graining commutes with
  time evolution, as THEORY-822's lumpability guarantees, and only the
  EI argmax changes, from that partition at one step to the micro at two.
  The failure is in the selection criterion, not in the coarse-graining.
- **QUESTION-115 (A21).** A21's condition, C_*(P_ℓ^{do(a)}) = P_L^{do(ā)}
  for a declared family of interventions, is this paper's commutativity
  and ambiguity demands in one line. The paper shows that EI's family,
  uniform averages over realizers, passes coarse-grainings that fail
  both. The same answer for EI as the ΦID note of 2026-10-20 gives for Ψ:
  the criterion picks a level the admissibility condition does not
  license.
- **QUESTION-252.** One more pairwise separation: strong lumpability (D
  and M hold for the block label) does not make the EI-optimal choice
  stable under a change of time step. That is a property of EI, not one
  of the question's five conditions, so it is context, not a witness.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- The examples are found by a grid search at step 0.1 on 3×3 matrices,
  with no analytic result. The commutativity claim for "most" matrices
  is not quantified.
- The paper never computes EI under a distribution other than the
  maximum-entropy one. So C4 is argued, not shown, and the paper does not
  check whether its two failures survive another distribution.
- It reads Hoel 2017. Hoel 2013's spatial and temporal macros, and
  CE 2.0, are not addressed.
- **Errors and slips.** (11)'s micro EI is printed 0.55 where 0.544 is
  computed. Total cholesterol's components are written "LDP" once. Hoel's
  eq. (7) is criticized as notation, which is fair, and otherwise the
  restatements check.

## Open questions

- Under the system's own stationary distribution used at both levels,
  does a partition ever tie with the micro on EI without being a
  sufficient statistic of the cause for the coarse effect? A tie is the
  most a macro can get under a common distribution (THEORY-tmphfpe7).
- Does a fixed, system-given intervention family exist on which EI's
  level and a proportionality test can be compared on a system not built
  for it?
