---
status: Skimmed
paper: 'LIT-tmpxq623'
title: 'Bulatov — A dichotomy theorem for nonuniform CSPs'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read in part on 2026-11-05 from arXiv v2, https://arxiv.org/pdf/1703.03021v2,
    101 pp., extracted with pdftotext -layout. Read closely: the abstract,
    contents, §1 Introduction (pp. 3–5), §2.1 on CSP, universal algebra and
    the Dichotomy Conjecture (pp. 5–8, with Theorems 1–4), §2.2 on bounded
    width and few subpowers (pp. 8–10), the opening of §3.1 and §3.2
    (separating congruences, quasi-centralizers, decomposition,
    block-minimality; pp. 10–14), and the notation paragraph of §4.1 (p.
    19). Skipped: the rest of §3.2 (the algorithm) and all of Part II
    (§§4–10, pp. 17–100, the proofs). No proof was checked. The whole text
    was searched for "Galois", "reconfigur", "connectivity", "Pol(",
    "cyclic", "Taylor" and "Siggers". Quotes checked by string match
    against the extracted text. Page numbers are arXiv v2's.
date: '2026-11-05'
summary: >-
  Bulatov proves the CSP dichotomy for finite domains: every CSP(Γ) over a
  finite constraint language on a finite set is in P or NP-complete, P
  exactly when the polymorphisms include a weak near-unanimity operation.
  The new part is the algorithm, which combines local consistency, a new
  non-local condition (block-minimality) and the few-subpowers algorithm.
  Read: the introduction and §§2–3.2's opening; the ~80 pages of proof were
  not read.
---
<!-- inactive-ok-file: THEORY-tmp99dad NOTE-tmp0p9z8 THEORY-604 CLAIM-tmp9jvpb CLAIM-tmpal9mc CASE-tmpb5t9j CLAIM-tmpuxuo4 — Proposed, or Proposed and new; cited from the reading of Bulatov (2017) as open -->

# NOTE-tmpa8w32: Bulatov — A dichotomy theorem for nonuniform CSPs

## Contribution

A polynomial-time algorithm for CSP(A) whenever A is a finite idempotent
algebra with a weak near-unanimity (WNU) term operation. With the hardness
result already known (Bulatov, Jeavons and Krokhin), this proves the
Feder–Vardi Dichotomy Conjecture for finite-domain nonuniform CSPs. It
also shows the algorithm depends only on the algebra (Theorem 2), so the
two senses of tractability for CSP(A), one algorithm per language or one
for all, coincide.

## Key insight

The complexity of a fixed-language CSP is governed by the operations that
preserve its relations, its polymorphisms. Jeavons et al. "were the first
to observe that higher order symmetries of constraint languages called
polymorphisms play a significant role" (p. 6): more polymorphisms means
an easier problem, by Theorem 3's reductions. The dividing line is a
single identity, the existence of a WNU.

## Assumptions

- **Finite domain.** A is a finite set; the constraint language is "a set —
  not necessarily finite — of relations over A" (§2.1), relations given
  as lists of tuples. Theorem 1 is stated for finite Γ.
- **Nonuniform.** The language is fixed and the instances vary; complexity
  is of the family CSP(Γ), not of any one instance.
- **Decision only**: whether a solution exists. Counting, optimisation and
  quantified variants are named in §1 and set aside.
- **Idempotent reduction.** Languages are reduced to idempotent algebras
  (all constant relations added), from [26].

## Key results

- **Theorem 1 (p. 4).** "For any finite constraint language Γ over a finite
  set the problem CSP(Γ) is either solvable in polynomial time or is
  NP-complete."
- **The new part (p. 4).** "The hardness part of the conjecture has been
  known for long time. Therefore the main achievement of this paper is a
  polynomial time algorithm for problems satisfying the tractability
  condition."
- **Theorem 3 (p. 6, from Jeavons et al.).** For Γ finite, "if every
  polymorphism of ∆ is also a polymorphism of Γ, then CSP(Γ) is polynomial
  time reducible to CSP(∆)", in fact by a log-space reduction.
- **Theorem 4 (p. 8).** For a finite idempotent algebra A, the following
  are equivalent: CSP(A) is solvable in polynomial time; "A has a weak
  near-unanimity term operation"; "every algebra from HS(A) has a
  nontrivial term operation". "Otherwise CSP(A) is NP-complete." The
  hardness is credited to [26] and the equivalence of the last two to
  [25] and [54].
- **Uniformity (p. 7).** "One of the implications of our results is that
  these two types of tractability are equivalent."
- **Two algorithm families (p. 8).** "there are only two standard types of
  algorithms solving the CSP": local propagation (bounded width) and the
  few-subpowers generalisation of Gaussian elimination. The new algorithm
  combines them through block-minimality.

## Concepts

- **CSP(Γ)**, nonuniform CSP: constraints drawn from a fixed language Γ.
- **Polymorphism**: an operation f on A with f applied coordinatewise to
  tuples of R landing in R; "A polymorphism of a constraint language Γ is
  an operation that is a polymorphism of every R ∈ Γ" (p. 6).
- **Inv(F)**: "the set of all relations invariant with respect to all
  operations from" F (p. 7); CSP(A) is the class of CSP(Γ) with Γ ⊆ Inv(F).
- **Weak near-unanimity operation**: w(y,x,…,x) = w(x,y,x,…,x) = ⋯ =
  w(x,…,x,y) (p. 6).
- **Block-minimality, separating congruences, quasi-centralizer** (§3).
- **Notation trap**: in this paper Pol(A) is the set of *polynomials* of
  the algebra, not its polymorphisms ("The set of all polynomials (unary
  polynomials) of A is denoted by Pol(A)", p. 19).

## Connections

Builds on Jeavons et al. (polymorphisms), Bulatov, Jeavons and Krokhin
(the algebraic conjecture and its hardness half), Maróti and McKenzie
(WNU terms), and the bounded-width and few-subpowers algorithms. Zhuk's
independent proof (LIT-tmp13cly, NOTE-tmp0p9z8) appeared at the same
time with a different algorithm, and notes that Bulatov's handles infinite
constraint languages over a finite domain.

## Bearing on the record

- **The pasted synthesis on resource-bounded realizability** (Response 3
  §4). Verdict:
  - **Right**: "The finite-domain CSP dichotomy theorem, proved
    independently by Andrei Bulatov and Dmitriy Zhuk, characterizes a
    division between polynomial-time-solvable and NP-complete fixed
    constraint languages using algebraic conditions." Fixed languages,
    finite domain, P against NP-complete, an algebraic criterion. The
    condition in both papers is a weak near-unanimity polymorphism.
  - **The Pol–Inv connection.** A's Γ ⊆ Inv(F) ⟺ F ⊆ Pol(Γ) is the standard
    one and follows at once from the paper's definitions (each side says
    every f in F preserves every R in Γ). Neither this paper nor Zhuk's
    states it as a Galois connection; Bulatov uses Inv(F) and Theorem 3.
    Calling it a Galois connection is the field's naming, not the paper's.
    Theorem 3 is what A's "deeply connected to computational complexity"
    refers to, unnamed.
  - **Overstated**: "classifying computational systems through their
    constraint-preserving algebra", and "what computational powers do those
    operations support?" The theorem classifies decision problems over
    fixed finite languages, not systems. Polymorphisms are operations
    applied coordinatewise to the tuples of the relations, not operations a
    system performs or powers it has.
  - **Missing**: the theorem holds for finite domains only (Zhuk, §10.4,
    shows how infinite domains change it). One fixed object, one crease
    pattern or one organization, is a single instance of constant size and
    has no complexity in this sense. Applying the dichotomy to A's
    continuous configuration spaces would first need a finite-domain
    language.
  - **Silent on connectivity.** The paper says nothing about solution-space
    connectivity, reconfiguration or reachability between solutions. Its
    one "as-connectivity" (p. 32) concerns the graph of an algebra, a false
    friend. A's own closing question, whether "the algebra of a constraint
    language" could "predict something about the complexity of navigating
    its solution space", is open relative to this paper; for Boolean
    languages Gopalan et al. are the work that addresses it.
- **THEORY-604, THEORY-729 and NOTE-141 (Corfield; adjunctions into an
  opposite).** Qualifies. Pol–Inv is an instance of the construction
  NOTE-141 traces Corfield's six Galois-connection dualities to: a relation
  between two sets (here "f preserves R") induces an antitone Galois
  connection between their power sets, restricting to a dual isomorphism
  on the closed sets (THEORY-729's fixed points, here clones and relational
  clones). The identification is the reader's; neither Bulatov nor
  Corfield makes it. It supports A's "another Galois connection" as order
  theory and adds nothing about complexity.
- **LIT-tmpj5g19 and NOTE-tmpd0dln (rigid foldability NP-hard).** Qualifies:
  that hardness result concerns continuous crease angles, not a
  finite-domain constraint language, so the dichotomy does not apply to it
  directly.
- **CLAIM-tmp9jvpb, CLAIM-tmpal9mc and CASE-tmpb5t9j (feasibility against
  reachability).** The dichotomy concerns feasibility, the first of
  CLAIM-tmp9jvpb's three properties, and never reachability.
- **CLAIM-347 and CLAIM-tmpuxuo4 (the compatibility complex).** Unrelated:
  the complex is of one fixed organization; the dichotomy concerns the cost
  of deciding satisfiability across a family.
- Filed: THEORY-tmp99dad.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- The proof is very long (Part II, about 80 pages); v2 records a patched
  gap in the proof of Lemma 46. Not checked here.
- The Meta-problem, recognising whether a language meets the condition, is
  "not quite trivial" (p. 5) and set aside.
- Zhuk (§10.1) notes that both algorithms depend exponentially on the
  domain size; a "truly polynomial" algorithm for CSP-WNU is open.
- Decision only; finite domains only.
