---
status: Read
paper: 'LIT-tmpsa1qj'
title: 'Contextuality-by-Default 2.0'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from arXiv 1604.04799v4 (25 Oct 2016, 17 pages, the
    corrected LNCS text), extracted with pdftotext. Sections 1–6, all five
    theorems, Examples 1–3 and the reference list were read. The proof of
    Theorem 1 was followed step by step: the coupling property, sufficiency
    and the induction for necessity. Theorem 5's proof was also followed.
    Theorem 2 is proved in the companion paper (arXiv 1604.08412), which
    was also read (LIT-tmpuzf4t). The 4D Kochen–Specker incidence table on
    p. 11 came through as scattered stars and was not checked entry by
    entry. The typeset LNCS version was not compared.
date: '2026-10-09'
summary: >-
  Replaces CbD 1.0's maximal coupling of each connection by a multimaximal
  one (every subset maximally coupled). For binary variables this coupling
  exists, is unique and has an explicit staircase form (Theorem 1), so a
  noncontextual system's subsystems are noncontextual (Theorem 3) and
  partial and complete (non)contextuality coincide. Cyclic, consistently
  connected and two-copy systems are judged as before. For non-binary
  variables multimaximal couplings can fail to exist, can be non-unique,
  and are not stable under coarse-graining (Examples 1–3).
---

<!-- inactive-ok-file: THEORY-013 THEORY-014 THEORY-tmpjdnxt — Proposed; cited for what this reading adds to them -->

# NOTE-tmpy1lmh: Contextuality-by-Default 2.0

## Contribution

CbD 1.0 (LIT-777) asked whether the bunches of a system are compatible with
a maximal coupling of each connection. This paper replaces that with a
multimaximal coupling, in which every subset of a connection is maximally
coupled. It proves that for binary variables this coupling exists, is
unique and has a closed form. That gives the binary theory two properties
CbD 1.0 lacked: heredity under deleting variables, and a single verdict
instead of "partial" and "complete" ones. It also shows that the same
definition misbehaves for non-binary variables, which motivates the move to
dichotomizations.

## Key insight

For binary variables, coupling the copies of a content "as closely as
possible" has exactly one answer once every pair is required to be as
close as possible. Sort the copies by their probability of a 1. The copies
then switch from 1 to 2 one at a time, in that order, like a staircase.
With the connection couplings fixed, contextuality is the single question
whether the rows (contexts) and the columns (contents) of the system can be
marginals of one joint distribution.

## Assumptions

- A finite c-c system: each random variable R_q^c is indexed by a content q
  and a context c. Variables sharing a context are jointly distributed.
  Variables in different contexts are stochastically unrelated. All
  variables in one connection have the same set of values.
- **Binary variables** throughout the definitions and Theorems 1–4.
  Definition 3 is stated only for binary systems. Section 6 and Theorem 5
  treat arbitrary categorical variables.
- **Maximal coupling** (from Thorisson; LIT-777 Theorem 3.3): a coupling
  maximizing Pr[T¹ = … = Tᵏ], which for categorical variables is
  Σ_v min_i Pr[Rⁱ = v].

## Key results

- **Definition 1.** A coupling (T_q^1, …, T_q^k) of a connection is
  *multimaximal* if, for every subset of size m > 1,
  Pr[T_q^{i₁} = … = T_q^{i_m}] is the largest attainable among couplings
  of that subset.
- **Definitions 2–3.** A coupling of the whole system is *multimaximally
  connected* if its restriction to each connection is multimaximal. A
  binary system is noncontextual if and only if one exists.
- **Theorem 1.** For a binary connection with p_i = Pr[R_q^i = 1] sorted
  p₁ ≤ … ≤ p_k, a coupling is multimaximal if and only if its only
  nonzero masses are p₁ on 11…1, p_{l+1} − p_l on 2…21…1 (l twos, k − l
  ones) for l = 1, …, k − 1, and 1 − p_k on 22…2. Sufficiency is checked
  directly; necessity is by induction on the position of the first 1.
- **Corollary 1.** A multimaximal coupling of a binary connection exists
  and is unique.
- **Theorem 2** (proof in LIT-tmpuzf4t). For a binary connection in that
  order, a coupling is multimaximal if and only if each adjacent pair
  (T_q^i, T_q^{i+1}) is a maximal coupling.
- **Theorem 3.** In a noncontextual binary system, every subsystem
  (obtained by deleting variables) is noncontextual. The proof deletes the
  corresponding variable from the coupling; subsets of a multimaximal
  coupling stay multimaximal.
- **Properties stated in Section 4.** (a) For consistently connected
  systems, multimaximal couplings are identity couplings, so the verdict
  is the traditional one. (b) Binary systems are always completely
  (non)contextual. (c) For two-element connections, maximal and
  multimaximal coincide, so the theory of cyclic systems is unchanged.
  (d) For Kochen–Specker systems with more than two variables per
  connection (Peres-type proofs), the result "will yield different
  results" from CbD 1.0. No example is computed.
- **Theorem 4.** Every binary system has a quasi-coupling (signed masses
  summing to 1, proper bunch marginals) whose connection marginals are
  the multimaximal couplings. Among these there is one of least total
  variation, which is the measure of contextuality. The existence result
  is LIT-777's Theorem 6.1.
- **Theorem 5.** For arbitrary variables, a coupling is multimaximal if
  and only if every pair is maximally coupled. Proof: if some subset
  fails, a value v has Pr[all = v] < min_c Pr[T_q^c = v] while every pair
  attains its pairwise minimum at v. Dichotomizing at v contradicts
  Theorem 2.
- **Examples 1–3.** (1) Three 3-valued variables with masses
  (0, ½, ½), (½, 0, ½), (½, ½, 0): pairwise maximality forces three
  mutually exclusive events of probability ½ each, so no multimaximal
  coupling exists. (2) Three 6-valued variables have two distinct
  multimaximal couplings. (3) Lumping i with i′ in Example 2 gives Example
  1, so a system with a multimaximal coupling (noncontextual) becomes one
  without (contextual) under coarse-graining.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A binary connection has exactly one multimaximal coupling, of the staircase form | strong (proof) | Theorem 1, Corollary 1 |
| C2 | Noncontextuality in CbD 2.0 is hereditary for binary systems | strong (proof) | Theorem 3 |
| C3 | CbD 1.0 noncontextuality is not hereditary | asserted, no example | Section 1 |
| C4 | CbD 2.0 agrees with CbD 1.0 on cyclic systems and on any system whose connections have two variables, and with the traditional definition under consistent connectedness | strong (immediate from the definitions) | Section 4 |
| C5 | Multimaximality is equivalent to pairwise maximality for arbitrary variables | strong (proof, relying on Theorem 2) | Theorem 5 |
| C6 | For non-binary variables, multimaximal couplings may not exist, may not be unique, and can be destroyed by coarse-graining | strong (counterexamples) | Examples 1–3 |
| C7 | CbD 2.0 and 1.0 give different verdicts on Peres-type Kochen–Specker systems | asserted, not computed | Section 4 |

## Concepts

- **conteXt / conteNt.** The paper's typography for context and content.
- **connection.** All variables sharing a content. They are pairwise
  stochastically unrelated.
- **C-coupling; partially / completely C-(non)contextual.** For a property
  C of connection couplings, a system is partially noncontextual if the
  bunches are compatible with *some* combination of C-couplings, and
  completely noncontextual if they are compatible with *every* combination.
  The adjectives are new here. They coincide when C-couplings are unique.
- **multimaximal coupling.** Every subset maximally coupled (Definition 1).
  By Theorem 5, the same as every pair maximally coupled.
- **CbD 1.0 / CbD 2.0.** The authors' names for the maximal-coupling and
  multimaximal-coupling versions.

## Connections

It revises LIT-777's Definition 3.4 and keeps that paper's principles, its
linear-programming test and its Section 6 measure. Its Theorem 2 is proved
in the companion LIT-tmpuzf4t, which in turn cites this paper for the
existence and uniqueness theorem. The two papers cite each other for their
halves. Its closing proposal, to replace every non-binary variable by all
its dichotomizations, is the programme of the canonical-systems paper
LIT-tmp1kfuc. The maximal-coupling theorem is Thorisson's. The quasi-coupling
idea is credited to de Barros and Oas.

## Bearing on the record

- **LIT-777 and NOTE-600.** NOTE-600 reported from footnote 10 that the
  definition was being superseded and that the binary cyclic results were
  unchanged. This reading confirms both, from the source: for two-variable
  connections, maximal and multimaximal coincide. NOTE-600's statement
  that CbD agrees with the sheaf criterion under consistent connectedness
  also holds for 2.0, since multimaximal couplings of identically
  distributed variables are identity couplings.
- **THEORY-013.** Its source's systems (question order, matching, the
  Bruza word pairs) are binary and cyclic, so the switch to 2.0 does not
  change any verdict THEORY-013 reports.
- **THEORY-014.** Theorem 4 has that theory's shape: a signed coupling
  always exists, and classicality is having a nonnegative one. It is
  LIT-777's Theorem 6.1 applied to multimaximal couplings, so it is not a
  new instance.
- **The manuscript's claim CLAIM-tmpje74v.** The paper supports it.
  Different verdicts arise only for contents measured in more than two
  contexts. The cyclic case and the measure are unchanged. But the paper
  states the CbD 1.0 failure of heredity without an example, and it does
  not compute any system on which 1.0 and 2.0 disagree.
- It produces, with the canonical-systems paper, THEORY-tmpjdnxt.
- No instruction for machine-learning practice.

## Limitations

- Binary variables only. For non-binary ones the paper gives only problems
  and a proposal.
- The motivating claim, that CbD 1.0 noncontextuality is not hereditary,
  has no worked example.
- Theorem 2, which Theorem 5 depends on, is proved elsewhere.
- No example system is computed under both versions.

## Open questions

- A concrete inconsistently connected binary system that is
  CbD 1.0-noncontextual with a contextual subsystem would make C3 precise.
- How large the disagreement between 1.0 and 2.0 is on Peres-type
  Kochen–Specker systems with realistic inconsistent connectedness.
- Whether the dichotomization programme is "feasible", the paper's own
  closing question. LIT-tmp1kfuc answers it for a single pair of
  categorical variables.
