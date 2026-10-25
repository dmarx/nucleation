---
status: Read
paper: LIT-tmpwlnuv
title: 'DeGroot — Reaching a consensus'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Read in full from the copy the owner supplied on 2026-10-25: a JSTOR
    scan of the Journal of the American Statistical Association article
    (69(345): 118–121), five PDF pages, a JSTOR cover sheet dated 13 May
    2002 and the four printed pages. The scan has no text layer, so the
    pages were rendered with pdftoppm and read as images, and the
    displayed matrices and the theorem statements were checked on
    200-dpi crops. A tesseract pass was used only for searching. Read:
    the abstract, §§1–8 (the model, iteration, convergence, conditions
    for convergence with Theorems 1 and 2, calculation of the consensus
    with Theorem 3 and the four examples, arbitrary linear spaces,
    concluding remarks on Delphi), and the 14 references. The theorems
    are stated without proof in the paper, as standard Markov-chain
    results. They are re-derived and checked numerically in
    THEORY-tmpvqkp6.
date: '2026-10-25'
summary: >-
  A group whose members each replace their opinion, over and over, by a
  fixed weighted average of everyone's current opinions, F⁽ⁿ⁾ = PⁿF, is a
  Markov chain run on opinions. It reaches a consensus from every start
  exactly when the chain has one closed class and that class is
  aperiodic. The consensus is then a linear opinion pool whose weights
  are the chain's stationary vector, which gives members outside the
  closed class no weight. Two closed classes, or one periodic class, give
  no consensus. The weights are fixed, and nothing in the model tracks
  the truth.
---
<!-- inactive-ok-file: CLAIM-262 — Proposed; the owner's claim the construction illustrates, nothing here rests on it -->
# NOTE-tmp5sbzm: DeGroot — Reaching a consensus

## Contribution

It turns the opinion pool, a weighted average Σπᵢ Fᵢ of the members'
distributions whose weights earlier writers had no principled way to
choose, into the limit of a process. Each member chooses weights on the
others' opinions once. Iterating those averages either converges to a
common pool or does not, and Markov-chain theory says which and gives the
pool's weights. Of the three advantages the paper claims, the second and
third are the substance: "It presents simple conditions for determining
whether it is possible for the group to reach a consensus" and "When a
consensus can be reached, the weights to be used in this consensus can be
explicitly and simply calculated" (§1).

## Key insight

The weight matrix P is row-stochastic, so it "can be regarded as the
one-step transition probability matrix of a Markov chain with k states"
(§5). Repeated averaging is then the chain's n-step matrix Pⁿ applied to
the opinions. A consensus is the chain forgetting where it started, so
that every row of Pⁿ tends to the same vector π. Who ends up counting in
the consensus is decided by who is listened to, indirectly as well as
directly, and not by how much each member trusts himself or by any
member's accuracy.

## Assumptions

- k members. Each holds a subjective distribution Fᵢ for a parameter θ on
  an abstract measurable space Ω, or, in §7, a point in a fixed convex set
  of an arbitrary linear space, such as a real-valued estimate.
- Each member i fixes weights p_ij ≥ 0 with Σⱼ p_ij = 1 before seeing the
  others' opinions. The first revision is F_i1 = Σⱼ p_ij Fⱼ (2.1).
- The weights stay fixed at every stage. The justification is consistency:
  if member i "still wishes to form his subjective distribution by
  assigning the weight p_ij to the distribution of individual j—and there
  does not seem to be any basis for his changing these weights at this
  time—then in order to remain consistent with this principle he must
  again revise" (§3). Hence F⁽ⁿ⁾ = PF⁽ⁿ⁻¹⁾ = PⁿF (3.3).
- Revisions go on "indefinitely or until F⁽ⁿ⁺¹⁾ = F⁽ⁿ⁾" (§3).
- No outside information: "there is no possibility of learning whether
  the opinion of one individual is closer to the truth than that of
  another" (§8).

## Key results

- **Definition (§4).** "A consensus is reached if and only if all k
  components of F⁽ⁿ⁾ converge to the same limit as n → ∞" (4.1). From
  (3.3), "a consensus is reached if and only if there exists a vector π"
  with lim p_ij⁽ⁿ⁾ = π_j for all i, j (4.2). The common distribution is then
  Σπᵢ Fᵢ.
- **Theorem 1 (§5),** "adapted from a result given by Doob": "If there
  exists a positive integer n such that every element in at least one
  column of the matrix Pⁿ is positive, then a consensus is reached."
- **Theorem 2 (§5).** "If all the recurrent states of the Markov chain
  communicate with each other and are aperiodic, then a consensus is
  reached." This is weaker than irreducibility: transient members are
  allowed.
- **The negative cases (§5).** "On the other hand, if the states of the
  chain form at least two disjoint closed sets of communicating states or
  if the communicating states in a single closed set are periodic, then a
  consensus is not reached. These results are discussed in texts such as
  Feller [5], Karlin [6], or Parzen [10]." So the periodic case is named,
  and named as a failure.
- **Theorem 3 (§6).** "Suppose that a consensus is reached and let
  Σπᵢ Fᵢ denote the common subjective distribution that is reached in the
  consensus. Then π = (π₁, ···, π_k) is the unique stationary probability
  vector." It is found from πP = π and Σπᵢ = 1. A transient member gets
  πᵢ = 0: "no weight will be assigned in the consensus to the prior
  distribution Fᵢ of individual i."
- **Examples (§6.1).** P = [[½, ½], [¼, ¾]] gives π = (⅓, ⅔). Adding a third
  member who weights everyone ⅓, with no one weighting him, gives
  (⅓, ⅔, 0): he is transient. P = I gives no consensus. A four-member P of
  two ½-blocks gives two internal consensuses after one revision and none
  overall. "In general any individuals for whom the corresponding states
  of the Markov chain form a closed communicating, aperiodic class will
  reach a consensus among themselves."
- **Delphi (§8).** Self-weight p_ii ∈ (0, 1) and equal weights
  (1 − p_ii)/(k − 1) on the rest always lead to a consensus by Theorem 1.
  The model is offered as "a formalization of the Delphi technique, a
  formalization in which a consensus is reached."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Iterated fixed-weight averaging of opinions reaches a consensus if some power of P has a strictly positive column | strong | Theorem 1, cited from Doob, no proof given; re-derived in THEORY-tmpvqkp6 |
| C2 | It reaches one if all recurrent states communicate and are aperiodic | strong | Theorem 2, stated as "analogous", no proof; equivalent to C1 for a finite chain (re-derived, not remarked in the paper) |
| C3 | Two closed classes, or one periodic closed class, give no consensus | strong as a statement about consensus from every start; it needs that quantifier | stated, with textbook references; checked |
| C4 | When a consensus is reached its weights are the unique stationary vector, zero on transient members | strong | Theorem 3, stated as "well known"; re-derived |
| C5 | The model applies unchanged to point estimates in any convex subset of a linear space | strong | §7; the iteration is linear and convex |
| C6 | It formalizes the Delphi technique, of which it is a special case under equal weights to others | moderate | §8, argued, no data |

## Concepts

- **Consensus**: all members' opinions converge to one common limit
  (4.1). Not agreement at a finite stage, though it may happen at one, as
  in the four-member example.
- **Opinion pool**: a convex combination Σπᵢ Fᵢ of the members'
  distributions. The term is Stone's (1961), as the paper says.
- **Stationary probability vector**: π ≥ 0, Σπᵢ = 1, πP = π (§6).
- **Recurrent, transient, closed class, periodic**: the Markov-chain
  terms, used without definition and referred to Feller, Karlin and
  Parzen.

## Connections

It cites earlier work on pooling subjective probabilities: Eisenberg and
Gale (1959) and Norvig (1967) on consensus and pari-mutuel methods, Stone
(1961) on the opinion pool, Madansky (1964) on externally Bayesian groups,
Morris (1971), Winkler (1968) and Savage (1971). The Markov-chain results
are from Doob (1953), Feller (1968), Karlin (1966) and Parzen (1962).
The Delphi technique is cited through Dalkey et al. (1972). The record
reads its descendants: Golub and Jackson's naïve learning (LIT-999,
THEORY-321), which calls the same iteration DeGroot updating and takes
the stationary vector as influence; the DeGroot–Friedkin model of Jia
et al. (LIT-1146); and Friedkin, Jia and Bullo (LIT-1482), who let the
self-weights change, the possibility DeGroot names in §8 and leaves out.

## Bearing on the record

- **THEORY-tmpvqkp6** is filed from this reading: the conditions for
  consensus and the weights it uses, as DeGroot states them, re-derived.
- **THEORY-321** already uses this model through Golub and Jackson. Its
  "strongly connected" narrowing is stronger than DeGroot's Theorem 2 needs
  for a consensus to exist: one closed class plus aperiodicity suffices,
  with transient members getting zero weight. Wisdom is Golub and
  Jackson's question, not DeGroot's, so nothing in THEORY-321 changes.
- **CASE-tmpvmjgd.** Its ℓ, the left eigenvector of a row-stochastic W
  with ℓᵀW = ℓᵀ and Σℓᵢ = 1, is DeGroot's π for P = W, by the same
  equation (Theorem 3). Its discrete-time amendment, that x ← Wx settles
  only if W is aperiodic, is DeGroot's own negative statement for a
  periodic closed class (§5). Its exclusion of "a reducible W" is broader
  than needed: with one closed class and transient members, ℓ is unique,
  zero off the class, and the closure still holds (checked, in
  THEORY-tmpvqkp6). The roles differ. DeGroot's π weights the initial
  opinions in a limit. The case's ℓ weights a running coordinate that the
  coupling conserves. They are the same invariant, πPⁿF = πF.
- **CLAIM-tmpfd9lk** lists "a strongly connected population" among its
  conditions. DeGroot's condition is one closed class (with aperiodicity
  in discrete time).
- **CLAIM-262** and the owner's exchange: the U36 reply's "an emergent
  summary of who is listened to, much as in classical consensus and
  DeGroot models" is borne out. In DeGroot the weights are fixed and
  chosen, so "who is listened to" is literal, and accuracy plays no part.

The proposed edits to those entries are written for the consolidator,
not made here. No instruction for machine-learning practice, so nothing
for the anthology.

## Limitations

- **No proofs.** All three theorems are cited from the Markov-chain
  literature. The paper's contribution is the reading of opinion pooling
  as a chain, not new mathematics.
- **The "if and only if" in §4 needs a quantifier.** Convergence of every
  Pⁿ row to π is necessary for a consensus from every initial F, not from
  a given one. With P = [[0, 1], [1, 0]] the opinions never converge for
  F₁ ≠ F₂, but two members who start equal stay equal. The negative cases
  in §5 hold in the same sense: no consensus for a generic start.
- **Theorems 1 and 2 are equivalent** for a finite chain, and with the
  negative cases they make a complete characterization: a consensus from
  every start exists iff the chain has exactly one closed class and it is
  aperiodic. The paper presents them as "analogous" results and does not
  say this.
- **Fixed weights and no truth.** The weights never change, and no
  observation enters, so the model says nothing about whether the
  consensus is right. That question is Golub and Jackson's.
- **Discrete time only.** The periodic failure is a discrete-time one: in
  continuous time, ẋ = (P − I)x, a periodic P converges (checked).
- **A typo.** In §6 the normalization reads Σᵢ₌₁ⁿ πᵢ = 1 for Σᵢ₌₁ᵏ.

## Open questions

- What happens when members revise their weights after seeing how others
  move? §8 names this and leaves it. Friedkin, Jia and Bullo (LIT-1482)
  and the DeGroot–Friedkin model (LIT-1146) take it up.
- How fast is the consensus reached? The paper says nothing about rates.
  Golub and Jackson treat speed separately from correctness (THEORY-321).
