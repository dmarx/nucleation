---
number: 924
status: Read
formerly:
- NOTE-tmpzuj15
paper: LIT-1115
title: Fagin, Lotem & Naor — Optimal aggregation algorithms for middleware
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full 2026-10-15 from the authors' arXiv preprint, arXiv cs/0204046v1
    (22 April 2002, posted by Moni Naor; the only version), arxiv.org/pdf/cs/0204046v1,
    39 PDF pages (an unnumbered title page and pages 1–38). Its title page says
    "Extended abstract appeared in Proc. Twentieth ACM Symposium on Principles of
    Database Systems, 2001 (PODS 2001), pp. 102–113", and the arXiv comment says
    "41 pages. Preliminary version appeared in ACM PODS 2001". So the copy read
    is the full version, not the PODS extended abstract the LIT is registered as.
    It matches the outline of the JCSS 2003 journal paper (66(4), 614–656) but is
    not its typeset text; the journal version could not be compared, and the PODS
    abstract was not read. What that means for the record: every theorem cited below
    is from the full version; the PODS abstract may state fewer of them or state
    them differently, and the journal text may correct the preprint (see the Table
    1 discrepancy below). Other places looked for both versions: Unpaywall reports
    the PODS paper closed and the JCSS paper bronze (open archive) at sciencedirect.com/science/article/pii/S0022000003000266/pdf,
    which returned 403 to this environment; the ACM DL PDF of the PODS paper (dl.acm.org/doi/pdf/10.1145/375551.375567)
    also returned 403. Text extracted with pdftotext -layout. Pages 10 (Theorem
    6.1 and its proof) and 36 (Table 1) were also checked as rendered page images,
    because the extraction breaks fractions. Read: Sections 1–12 entire, every theorem,
    corollary, example and proof, Table 1 and all footnotes; nothing skipped. The
    preprint has no reference list, and every citation is printed as "[?]" (38 times),
    so which work a citation points to is inferred from the names in the text. Fagin's
    own 1996/1999 paper (LIT-1108), which proves the cost bound for Fagin's
    Algorithm, could not be obtained; what is said below about that bound is this
    paper's account of it. Every quotation below was checked by script against the
    extracted text, with whitespace normalised.
date: '2026-10-15'
summary: >-
  Given m lists of the same N objects, each sorted by one attribute's grade, and
  a monotone function combining the grades, the threshold algorithm (TA) reads the
  lists in parallel, random-accesses each newly seen object's other grades, and
  stops once k seen objects score at least the combined score of the last grades
  read. It is correct for every monotone combining function, needs constant buffers,
  and is instance optimal among correct algorithms that make no "wild guesses":
  on every database its cost is within a constant factor of any such algorithm's,
  the factor being m + m(m−1)c_R/c_S, which is best possible when the combining
  function is strict (conjunction-like). Without the no-wild-guesses restriction
  no algorithm is instance optimal, and the counterexample is a two-list conjunction
  whose target sits in the middle of both lists, which any algorithm must search
  linearly. Fagin's Algorithm's sublinear cost O(N^((m−1)/m) k^(1/m)) is cited from
  Fagin, not proved here, and holds only when the lists' orderings are probabilistically
  independent. The model prices queries over a given set of single-attribute sorted
  lists. It does not price building or keeping the lists, choosing an arrangement,
  or any computation beyond accesses.
---

# NOTE-924: Fagin, Lotem & Naor — Optimal aggregation algorithms for middleware

## Contribution

The paper takes the top-k problem over graded data held by subsystems that
each return objects sorted by one attribute (an image system's colour score,
a search engine's relevance for one term). It analyses the threshold
algorithm, TA, which it says was found independently by at least three
groups (Nepal and Ramakrishna, who published first; Güntzer, Balke and
Kiessling; and the authors). It introduces instance optimality as the
measure: TA is shown to be within a constant of the best correct algorithm
on every database, not only in the worst case or on average. It adds
variants for approximate answers (TA_θ), for lists that allow no sorted
access (TA_Z), for systems where random access is impossible (NRA) or
expensive (CA), and lower bounds on the optimality ratio, summarised in
Table 1. The comparison point throughout is Fagin's Algorithm, FA, from
Fagin's earlier paper.

## Key insight

TA keeps a threshold τ = t(x̲1, …, x̲m), the combined score of the last
grade read in each list. By monotonicity, no unseen object can score more
than τ, so once k seen objects reach τ the answer is known. The authors
call this the knowledge-based program "Halt as soon as you know you have
seen the top k answers." Instance optimality follows from the same
fact: any correct algorithm that stops earlier could be fooled by an
unseen object placed just below where it stopped, with grade τ in every
list. The paper puts it as "the cost of an instance optimal algorithm is
essentially the cost of the shortest proof."

## Assumptions

- **Data.** N objects, each with m grades in [0, 1]; m lists L1, …, Lm,
  each holding every object once, sorted by descending grade on one
  attribute. Ties are allowed unless the "distinctness property" is
  assumed.
- **Access model.** Sorted access reads the next entry from the top of
  one list. Random access asks for one given object's grade in one list,
  in one step. With s sorted and r random accesses the "middleware cost"
  is s·c_S + r·c_R, for positive constants c_S and c_R. "We are taking
  into account only access costs, and ignoring internal computation
  costs." Building or maintaining the lists is not priced at all.
- **Aggregation.** t is monotone: "t(x1 , . . . , xm ) ≤ t(x′1 , . . . ,
  x′m ) whenever xi ≤ x′i for every i." Some results need more. t is
  *strict* if t = 1 exactly when every argument is 1 ("Intuitively,
  strictness means that the aggregation function is representing some
  notion of conjunction"; min and average are strict, max is not). t is
  *strictly monotone* if raising every argument strictly raises t. t is
  *strictly monotone in each argument* if raising any one argument raises
  t (average yes, min no). The authors flag that strict monotonicity is
  not the same as being strict and monotone.
- **k and m are treated as constants**, so factors in m and the additive
  constant in k are absorbed into the optimality ratio (Section 6.1).
- **Sorted access in lockstep** is not needed. The results hold "as long
  as the rates of sorted access of the lists are within constant
  multiples of each other" (footnote 6).
- **No probability model** for TA's results. FA's cost bound needs one:
  "the orderings in the sorted lists are probabilistically independent".
  The paper does not define that model ("We shall not discuss the
  probability model here, including the notion of “independence”, since
  it is off track").

## Key results

Notation: c_R/c_S is the cost of one random access relative to one sorted
access.

- **FA, as this paper reports it (Section 3; proved in Fagin's paper, not
  here).** FA reads all lists in parallel until at least k objects have been
  seen in every list, then random-accesses every object seen and returns the
  k best. It is correct for monotone t. "If there are N objects in the
  database, and if the orderings in the sorted lists are probabilistically
  independent, then the middleware cost of FA is O(N (m−1)/m k1/m ), with
  arbitrarily high probability" (in the extraction the exponents lose their
  superscripts: O(N^((m−1)/m) k^(1/m))). Its optimality: "Fagin shows that
  his algorithm is optimal with high probability in the worst case if the
  aggregation function is strict (so that, intuitively, we are dealing with
  a notion of conjunction), and if the orderings in the sorted lists are
  probabilistically independent." FA's access pattern does not depend on
  t at all, so it is not optimal for every monotone t: for max, a simple
  algorithm makes at most mk sorted accesses and no random ones. FA's
  buffers grow without bound with N.
- **Theorem 4.1.** For monotone t, TA correctly finds the top k answers.
  TA never makes more sorted accesses than FA on any database, and costs at
  most a constant times FA's.
- **Theorem 4.2.** TA needs only buffers whose size does not depend on N.
  The price is up to m − 1 random accesses for every object seen under
  sorted access, even if already seen.
- **Instance optimality (Section 5).** B is instance optimal over a class
  of algorithms A and a class of databases D if B ∈ A and for every A ∈ A
  and D ∈ D, cost(B, D) ≤ c·cost(A, D) + c′. "We refer to c as the
  optimality ratio." Against a nondeterministic algorithm, the comparison
  is with the cheapest branch, which the authors read as the shortest
  proof that the answer is right. The definition "is formally the same
  definition as is used in competitive analysis", except that B must
  belong to A and the cost is a performance cost.
- **Wild guesses.** An algorithm "makes wild guesses if it does random
  access to find the grade of some object R in some list before the
  algorithm has seen R under sorted access." Neither FA nor TA does.
- **Theorem 6.1.** For monotone t, over all databases, TA is instance
  optimal among all correct algorithms that make no wild guesses. The
  proof shows TA halts by depth a + k if the rival sees a distinct
  objects, giving optimality ratio at most m + m(m − 1)c_R/c_S. It holds
  whether or not t is strict (footnote 9).
- **Corollary 6.2 with Theorem 9.1.** If t is also strict, TA's
  optimality ratio is exactly m + m(m − 1)c_R/c_S, and no deterministic
  algorithm has a lower one. With c_R = 0 the ratio is m, also best
  possible for strict t. For max (not strict) TA stops after k rounds,
  ratio m. With c_S = 0, TA is far from instance optimal. **Discrepancy:**
  Table 1 of the preprint (page 36) prints both the TA upper bound and the
  Theorem 9.1 lower bound as m + ((m−1)m/2)·c_R/c_S, half the random-access
  term of the theorem statements. The proofs (Theorem 6.1's count of
  (a + k)m(m − 1) random accesses; Theorem 9.1's ψ = (dm − 1)c_S +
  (dm − 1)(m − 1)c_R against d·c_S + (m − 1)c_R) give m + m(m − 1)c_R/c_S.
  The journal version was not compared.
- **Example 6.3 and Theorem 6.4.** Two lists of 2n + 1 objects, t = min,
  k = 1. In L1 objects 1, …, n + 1 have grade 1 and the rest 0; L2 holds
  the objects in reverse order, with n + 1, …, 2n + 1 at grade 1. Only
  object n + 1 has grade 1 in both. An algorithm that guesses object
  n + 1 and random-accesses it twice can halt, but "at least n + 1 sorted
  accesses would be required" by any algorithm that does not guess. With
  the ordering of L1 drawn uniformly at random and L2 its reverse, any
  deterministic algorithm's expected number of accesses before it even sees
  the winner is at least n + 1. Hence "There is no deterministic algorithm
  (or even probabilistic algorithm that never makes a mistake) that is
  instance optimal" over all correct algorithms for min with two
  arguments. "The heart of this example ... is the fact that there may be
  multiple objects with the same grade in some list."
- **Theorem 6.5.** If t is strictly monotone and every list has distinct
  grades, TA is instance optimal over all correct algorithms, wild guesses
  allowed, with ratio at most c·m², c = max{c_R/c_S, c_S/c_R}. Theorem 9.2
  gives a lower bound of ((m − 2)/2)·c_R/c_S for one strictly monotone t,
  t = min(x1 + x2, x3, …, xm), so the ratio here must depend on c_R/c_S
  for some t.
- **Section 6.1.** The dependence of the ratio on m is "inevitable" for
  strict t without wild guesses (Corollary 6.2), and for some t under
  distinctness (Theorem 9.2).
- **Theorems 6.6, 6.7, 6.9.** TA_θ (halt when k objects reach τ/θ) finds
  a θ-approximation and is instance optimal among non-guessing
  approximation algorithms. Under distinctness with guessing allowed, no
  approximation algorithm for min is instance optimal. Stopping TA early
  gives the current list with guarantee θ = τ/β.
- **Theorems 7.1, Corollary 7.2, Example 7.3.** With sorted access to only
  m′ of the m lists, TA_Z is instance optimal without wild guesses, ratio
  m′ + m′(m − 1)c_R/c_S, tight for strict t. The analogue of Theorem 6.5
  fails.
- **Theorem 8.5, Corollary 8.6, Theorem 9.5.** With no random access, NRA
  (tracking a lower bound W and upper bound B for each seen object) finds
  the top k objects, without grades, and is instance optimal among
  algorithms making no random access, ratio m, tight for strict t. It
  needs unbounded buffers and up to Ω(d²m) bookkeeping updates.
- **Theorems 8.9, 8.10, 9.4.** CA runs NRA and every h = ⌊c_R/c_S⌋ steps
  fetches all missing grades of the viable object with the highest B. Under
  distinctness and t strictly monotone in each argument, its ratio is at
  most 4m + k, independent of c_R/c_S; for min, at most 5m; the lower
  bound for min is m/2. Choosing which object to random-access by B is
  necessary: delaying TA's random accesses instead can be worse by a factor
  3(h − 2).
- **Related work.** Nepal and Ramakrishna's version assumes in effect that
  t is min. Güntzer, Balke and Kiessling's Quick-Combine heuristic for
  choosing the next list is not instance optimal; list-choice heuristics
  can save at most a factor m in sorted accesses. Footnote 17 corrects
  their reading of Fagin's result: "the only probabilistic assumption in
  [?] is that the orderings given by the sorted lists are probabilistically
  independent", not a uniform distribution of grades.

## Bearing on the record

**On [CLAIM-310](../claims.d/CLAIM-310.md) and [THEORY-358](../theory.d/THEORY-358.md) (feature against conjunction).**

- **What corresponds, as far as the model goes.** A query on one attribute
  is a read from the top of one sorted list: with m = 1 the threshold is
  the last grade read, so TA halts after k sorted accesses whatever N is.
  That is a reading from the definition of TA; the paper states the
  related fact for max ("TA halts after k rounds of sorted access"). A
  query on a conjunction of attributes has no list sorted by it. The cost
  depends on how deep the per-feature lists must be read before the
  threshold argument closes, and that depth depends on the data.
- **The structure of Treisman's conjunction display is the paper's
  hardest case.** In Treisman and Gelade's Experiment I each distractor
  carries exactly one of the target's two features (green Xs share its
  colour, brown Ts its shape), and the target alone carries both. With 0/1
  grades and min, this is Example 6.3 and the database family of Theorem
  6.4: every object high in one list is low in the other, and the one
  object high in both sits within a block of ties. No algorithm that does
  not guess can see it before about half the objects have been read, and
  on the theorem's random family (L1's order drawn uniformly, L2 its
  reverse) even algorithms that may guess need at least n + 1 accesses in
  expectation. So in this model a conjunction of features held
  separately by the distractors costs time linear in the number of items,
  while a single feature costs time independent of it. The direction of
  [THEORY-358](../theory.d/THEORY-358.md)'s contrast is reproduced by an access-cost argument with no
  appeal to attention or binding.
- **The sublinear bound does not apply to such displays.** FA's
  O(N^((m−1)/m) k^(1/m)), √(Nk) for two lists, needs the lists' orderings
  to be probabilistically independent. Treisman's displays are built to be
  maximally dependent the other way: being high on colour predicts being
  low on shape. The cost of a conjunctive query over feature-sorted lists
  is therefore not one number. It ranges from about k when the
  features are positively correlated and the target heads both lists (the
  record's reading, not a theorem here), through about √(Nk) for two
  independent lists (Fagin's bound as reported), to about N/2 in the
  anti-correlated family of Theorem 6.4. Which one holds is a property of how the features co-occur
  in the collection, not of the query alone. [CLAIM-310](../claims.d/CLAIM-310.md) says the cheapest
  arrangement depends on what is searched for and on what stands out
  within a bin; this adds that, for a fixed arrangement, the cost of a
  conjunctive query depends on the joint distribution of the attributes.
  That is an addition the claim does not now state, not a contradiction.
- **What it does not say about the slopes.** It says nothing about
  milliseconds, about the 1:2 ratio of present to absent slopes (the
  absent case is not analysed in the paper), about practice, or about
  whether vision has anything like sorted access. Treating parallel
  feature maps as lists that can be read from the top is the record's
  analogy, not the paper's. The linear lower bound is a count of accesses
  under a stated access model; human search being linear is a measured
  result that could have other causes, including the similarity account
  ([LIT-1081](../literature.d/LIT-1081.md), Unavailable). The paper neither supports nor weakens the
  feature-integration reading of [THEORY-358](../theory.d/THEORY-358.md). At most it shows that linear
  cost for this display structure is forced for any procedure that can
  only read feature-sorted lists and look up an item it has already found.
- **Bins are outside the model.** TA prices queries over m given sorted
  lists. It does not price a partition into bins, choosing which lists to
  keep, or a list sorted by the conjunction itself (which would make the
  conjunctive query cost k). So it does not bear on [CLAIM-310](../claims.d/CLAIM-310.md)'s parts 1–2
  (one arrangement, bin budget) except by showing that the access cost of
  a query over a fixed arrangement depends on the query's form. Over the
  same lists, max (a disjunction) costs at most mk sorted accesses; a
  strict t can cost about N.

**On [CLAIM-309](../claims.d/CLAIM-309.md).** Every correctness and optimality result here needs a
monotone t. A preference that rises and then falls with one ingredient,
which [CLAIM-309](../claims.d/CLAIM-309.md) says the smoothie line describes, is not monotone in that
ingredient. TA's threshold is then no bound on unseen objects, and none of
these algorithms applies. That is consistent with [CLAIM-309](../claims.d/CLAIM-309.md)'s separation of
preference over a ratio from a discriminability, and adds nothing more to
it.

**On [QUESTION-114](../questions.d/QUESTION-114.md).** It is a cost model for one part of the trade: the
cost of answering a top-k query from stored single-attribute orders, with
sorted (sequential) and random access priced separately, as disk
sequential and random reads are. It has no build cost, no upkeep, no
space term and no choice of which orders to store, so it is not the joint
model the question asks for. It prices what an arrangement costs to
query, given the arrangement.

**On [THEORY-348](../theory.d/THEORY-348.md).** Instance optimality is, by the paper's own statement,
formally the definition of competitive analysis with the algorithm
required to belong to the class it is compared against and with cost a
resource used rather than solution quality. Both are per-instance ratios
with an additive constant. They differ in what the rival knows: in
rent-or-buy the rival knows the future request sequence; here the rival is
any correct algorithm on the same database, and against the best
nondeterministic one the cost is the length of the shortest proof that the
answer is right. As in [THEORY-348](../theory.d/THEORY-348.md), the guaranteed ratio grows with the
number of options. Here it grows with the number of lists: m + m(m − 1)
c_R/c_S, quadratic in m when random access costs anything, and tight for
strict t.

## Limitations

- Access costs only. Computing grades, and building or maintaining the
  sorted lists, are not counted.
- k and m are constants. For many lists the ratio is large: with
  c_R = c_S and m = 10 it is 100.
- Instance optimality is relative to a class. Allowing wild guesses, or
  queries of the form "Which object has the ith largest grade in list j, and what is its grade in list j?", destroys it unless grades
  are distinct and t strictly monotone.
- Fagin's Algorithm's probabilistic bound is cited, not proved, and its
  probability model is not described.
- No experiments. The preprint's Table 1 halves the random-access term
  that the theorems state.
