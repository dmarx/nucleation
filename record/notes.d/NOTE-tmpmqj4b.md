---
status: Read
paper: 'LIT-tmpujl75'
title: 'Ito et al. — On the complexity of reconfiguration problems'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read on 2026-11-05 from the publisher's PDF posted on co-author Erik
    Demaine's page
    (https://erikdemaine.org/papers/NPReconfiguration_TCS/paper.pdf,
    linked from https://erikdemaine.org/papers/NPReconfiguration_TCS/),
    12 pages, the article-in-press layout with the TCS article history,
    extracted with pdftotext -layout. ScienceDirect's PDF
    (https://www.sciencedirect.com/science/article/pii/S0304397510006961/pdf)
    returned HTTP 403 with a robot check; not retried. Read in full: the
    abstract, §1, §2.1 (Theorem 1 and proof), §2.2 (Theorem 2, sketched),
    §3 (Propositions 1 and 2, Theorem 3), §4.1 (Theorems 4 and 5), the
    statements of §4.2 (Theorem 6 with proof, Lemma 3, Theorem 7) and §5.
    Skimmed: the matching-reconfiguration algorithm (Lemmas 1–2,
    Corollary 1) and the proofs of Lemmas 3–4 and Theorem 7. Quotes were
    checked by string match against the extracted text. The paper is
    probably, not certainly, the one the pasted synthesis on
    resource-bounded realizability cites.
date: '2026-11-05'
summary: >-
  Defines a reconfiguration problem as reachability between two feasible
  solutions through feasible solutions under a symmetric polynomial
  adjacency. Reconfiguration of any NP search problem is in PSPACE; for
  power supply, independent set, clique, vertex cover, set cover and 0–1
  integer programming it is PSPACE-complete; for matroid bases and
  matchings it is in P. Optimising the worst intermediate objective is
  inapproximable for maxmin clique, strongly NP-hard for minmax power
  supply, and 2-approximable in linear time for minmax set cover.
---
<!-- inactive-ok-file: THEORY-tmp57bxg CLAIM-tmpbi4ca TERM-tmp2ysyt CLAIM-tmp9jvpb CLAIM-tmpal9mc CLAIM-tmppzkl3 NOTE-tmpec4ov — Proposed, Skimmed or new; cited from the reading of Ito et al. (2011) as open -->

# NOTE-tmpmqj4b: Ito et al. — On the complexity of reconfiguration problems

## Contribution

Individual reconfiguration results existed (satisfiability, by Gopalan et
al.; sliding puzzles; colourings). This paper sets out reconfiguration
problems in general for any search problem with an adjacency on its
solutions, proves PSPACE membership for every NP search problem, extends
NP-hardness reductions to PSPACE-hardness for a family of classic
problems, finds polynomial cases among problems in P, and opens a new
class: optimising the worst intermediate state along the path.

## Key insight

Finding a feasible solution and moving between two feasible solutions
through feasible ones are different problems, and the second is usually
harder by a whole class: NP-complete search tends to give PSPACE-complete
reconfiguration. When a path must exist anyway, the question becomes how
bad the worst state along it must be.

## Assumptions

- Feasibility checkable in polynomial time; the adjacency symmetric and
  polynomially testable, usually a symmetric difference of size one.
- Decision problems only: "Note that power supply reconfiguration, as well
  as any reconfiguration problem" "defined in this paper, does not ask for
  an actual reconfiguration sequence."
- Worst-case complexity, with no average-case statement.

## Key results

- **Abstract**: "Reconfiguration problems arise when we wish to find a
  step-by-step transformation" between two feasible solutions with all
  intermediate results feasible. "We demonstrate that a host of
  reconfiguration problems derived from" "NP-complete problems are
  PSPACE-complete, while some are also NP-hard to approximate."
- **§1, motivation**: "Reconfiguration problems also model questions of
  evolvability" (genotypes above a fitness threshold, adjacent by single
  mutation); CSP reconfiguration may "yield insights into the structure of
  the solution space".
- **§1, thresholds**: clique reconfiguration moves one node at a time
  "without ever going through a clique of size" less than k − 1.
- **§2.1, Theorem 1**: "Theorem 1. Power supply reconfiguration is
  PSPACE-complete." Membership holds generally: "any reconfiguration
  version of a problem S in NP, can be solved in" polynomial space.
  Hardness by reduction from satisfiability reconfiguration (Gopalan et
  al.).
- **§2.2, Theorem 2**: "Theorem 2. The following problems are
  PSPACE-complete: independent set reconfiguration, clique
  reconfiguration," vertex cover, set cover and integer programming
  reconfiguration; independent set and vertex cover "remain
  PSPACE-complete even for planar graphs of maximum" degree 3.
- **§3, Propositions 1 and 2**: for matroid bases B0, Bt within weight k,
  "Then, there always exists a sequence of |B0 \ Bt | (= |Bt \ B0 |)
  exchanges that transforms one into" the other within the bound; matching
  reconfiguration is in P.
- **§3, Theorem 3**: "Theorem 3 ([3]). Satisfiability reconfiguration for
  linear, Horn, dual Horn and 2-literal clauses are all in P", quoted from
  Gopalan et al.
- **§4, the worst intermediate state**: "we try to optimize the worst
  objective among all configurations in the reconfiguration sequence".
  "Theorem 4. Maxmin clique reconfiguration cannot be approximated within
  any constant factor unless P = NP"; Theorem 5: maxmin maxsat
  reconfiguration is not approximable within 15/16 unless P = NP.
- **§4.2**: "Theorem 6. There is a linear-time 2-approximation algorithm
  for minmax set cover reconfiguration": add Ct \ C0 to C0, then delete
  C0 \ Ct, at cost ω(C0 ∪ Ct) ≤ 2 max{ω(C0), ω(Ct)}. "Lemma 3. Minmax
  power supply reconfiguration is strongly NP-hard", even with two supply
  vertices; Theorem 7 gives a linear-time 2-approximation in that case.
- **§5, open**: "Are the problems in Section 4 PSPACE-hard to approximate
  (not just NP-hard)?"

## Concepts

- **Reconfiguration problem for S and A** (§1): given an instance and
  feasible y0, yt, is there a sequence of feasible solutions from y0 to yt
  with consecutive ones adjacent under A?
- **Threshold reconfiguration**: intermediates must keep the objective
  within a bound, as k − 1 for clique.
- **Maxmin and minmax reconfiguration** (§4): choose the sequence to
  maximise the worst (least) or minimise the worst (greatest) objective
  along it.
- **Power supply problem**: supply and demand vertices in a bipartite
  graph; each demand served by one adjacent supply within its capacity; a
  move reassigns one demand vertex.

## Connections

It builds on Gopalan et al. ([LIT-tmpxpw0i](../literature.d/LIT-tmpxpw0i.md), read in [NOTE-tmpec4ov](NOTE-tmpec4ov.md)) for
satisfiability reconfiguration, both its PSPACE-completeness, the base of
Theorem 1's reduction, and its polynomial cases, quoted as Theorem 3; on
Hearn and Demaine's constraint logic and the sliding-block puzzles; and on
Savitch's theorem for membership. Its §1 links reconfiguration of
satisfying assignments to the clustering of random-SAT solution spaces
behind survey propagation. The ISAAC 2008 extended abstract is the same
work in short form.

## Bearing on the record

- **A's characterization (the pasted synthesis on resource-bounded
  realizability).** A cites "complexity-theoretic reconfiguration
  problems" to ScienceDirect only; this paper is the probable referent,
  not a certain one. A quotes no sentence of it; A's sentence about it is
  A's paraphrase.
  - **Right**: reconfiguration problems make finding a valid state and
    navigating between valid states precise, and the complexities differ:
    NP-complete search gives PSPACE-complete reconfiguration, and some
    problems in P give reconfiguration in P.
  - **Qualified**: that the complexity "can differ dramatically even for
    closely related constraint systems" is better supported by Gopalan et
    al., whose dichotomy across Boolean constraint languages this paper
    quotes as Theorem 3. This paper's examples are whole problem families,
    and it shows no case where finding is hard and navigating easy.
  - **Missing: §4 is A's bottleneck.** A defines the minimal bottleneck
    resource of a transition as the infimum over paths of the supremum of
    the resource along the path. The worst intermediate state of §4's
    minmax problems is that B*, with cost as the resource, posed as a
    computational problem; maxmin problems are its mirror. The paper shows
    that computing it is hard in some cases (strongly NP-hard for minmax
    power supply; no constant-factor approximation for maxmin clique unless
    P = NP) and 2-approximable in others (minmax set cover).
- **[CLAIM-tmpbi4ca](../claims.d/CLAIM-tmpbi4ca.md)** (the threshold for reaching a target is the least,
  over admissible paths, of the peak requirement): supports and extends.
  The claim's threshold is exactly §4's minmax objective. The paper adds
  what the claim is silent on: computing the threshold can be strongly
  NP-hard, or inapproximable.
- **[TERM-tmp2ysyt](../terms.d/TERM-tmp2ysyt.md)** (reconfiguration slack): supports, with a bound in one
  case. Theorem 6's path through C0 ∪ Ct shows that in set-cover
  reconfiguration the threshold is at most twice the larger endpoint cost,
  so the slack is at most that cost. The power supply problem, reassigning
  one customer at a time without any customer losing supply, is a literal
  instance of reallocating committed resources while keeping commitments,
  as the term's definition has it, and is PSPACE-complete in general
  (Theorem 1); the reader's inference, as the paper does not discuss
  organisations.
- **[CLAIM-tmp9jvpb](../claims.d/CLAIM-tmp9jvpb.md)** (feasible, reachable and reliably reachable are three
  properties): supports. Reconfiguration is exactly the feasible against
  reachable distinction, and deciding reachability is PSPACE-complete for
  many families.
- **[CLAIM-tmpal9mc](../claims.d/CLAIM-tmpal9mc.md)** (four failure modes): qualifies. Telling no path from
  a path above the ceiling is itself a hard computational question.
- **[CLAIM-tmppzkl3](../claims.d/CLAIM-tmppzkl3.md)** (the threshold is stable under error in the resource
  function): unrelated in substance. Stability under estimation error does
  not make the threshold easy to compute, and Theorems 4–5 and Lemma 3 say
  it is not, in general.
- **[CLAIM-347](../claims.d/CLAIM-347.md)** (the compatibility complex): unrelated directly; this
  paper concerns paths among solutions, not which demands are jointly
  satisfiable.
- Filed: [THEORY-tmp57bxg](../theory.d/THEORY-tmp57bxg.md). No instruction for machine-learning practice.

## Limitations

- Most PSPACE-hardness results are proof sketches (§2.2).
- Decision only: whether a path exists, not how long it is or how to build
  it.
- No continuous or physical setting; adjacency is combinatorial.
- The authors leave open (§5): weighted matching reconfiguration, TSP
  reconfiguration, better approximation and lower bounds for minmax power
  supply, and whether the §4 problems are PSPACE-hard to approximate.

## Open questions

- Are the maxmin and minmax problems of §4 PSPACE-hard to approximate?
- For which families does the worst intermediate state stay within a
  constant factor of the worse endpoint, as for set cover?
