---
number: 898
status: Read
formerly:
- NOTE-tmphbty9
paper: LIT-1084
title: Finkelstein, Schkolnick & Tiberio — Physical database design for relational
  databases
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full 2026-10-15 from the publisher's typeset article (ACM TODS 13(1),
    March 1988, pp. 91–128, 38 pp.; running heads and page numbers 91–128, the ACM
    copying notice and "0362-5915/88/0300-0091$01.50" on the first page; "Received
    February 1986; revised June 1987; accepted July 1987"). ACM serves it free (Unpaywall
    and OpenAlex: bronze, publishedVersion, at dl.acm.org/doi/pdf/10.1145/42201.42205),
    but ACM returned HTTP 403 to every request from this environment, and the Internet
    Archive's capture of that URL (snapshot 20200531131335 of the ?download=true
    form) could not be fetched (connection reset, then blocked by egress policy).
    Semantic Scholar lists only the ACM URL; OpenAlex's other location, a University
    of Tehran course copy (ece.ut.ac.ir/classpages/F84/AdvancedDatabase/Paper/DB_Paper/p91-finkelstein.pdf),
    returned 503 or a reset, with no Wayback capture; CiteSeerX (10.1.1.104.2048)
    reset the connection. The copy read is the same ACM PDF as posted by the course
    CS-460 Database Management Systems at the University of Crete, Computer Science
    Department (www.csd.uoc.gr/~hy460/pdf/p91-finkelstein.pdf, linked from the course's
    2023–2024 fall page as a reading; sha256 6b4d47f5…2c746b). Text extracted with
    pdftotext from the PDF's OCR layer. The OCR garbles formulas and some figures,
    so the formulas for the maintenance cost (p. 103), Proposition 2, the catalog-update
    count ψ_q (p. 109), ε-domination (p. 112), the maintenance difference D (p.
    119), and Figures 9 and 10 (pp. 123–124) were checked against page images rendered
    at 110 dpi. Read: all eight sections, both propositions and their proofs, Table
    I, Figures 1–10 as far as the scan shows them (the tree diagrams of Figs. 3–8
    are images whose node labels were not all legible; the text describing them
    was read), and the reference list. Nothing skipped. Works it relies on (Selinger
    et al. 1979 for the optimizer's cost formulas; Schkolnick & Tiberio 1985 for
    maintenance costs; Comer 1978 for NP-hardness) were not read, so what it says
    of them is its account. Every quotation below was checked against the extracted
    text by script, with whitespace and line-end hyphenation normalised; where the
    OCR misreads a character ("Pl" for P1, "Jl" and "53" for J1 and J3, "design-s",
    a dropped prime on ISET′), the reading was confirmed on the page image.
date: '2026-10-15'
summary: >-
  DBDSGN chooses, for each table, one clustered (ordering) index and a set of nonclustered
  indices to minimise a frequency-weighted sum of per-statement costs (access, tuple
  update, index maintenance) plus a weighted storage term, under an optional page
  limit, taking every cost from the System R optimizer's own estimates rather than
  an external model. Statement costs for any configuration are computed exactly
  from "atomic" configurations with at most one index per table (Propositions 1
  and 2), so the optimizer is consulted a linear rather than exponential number
  of times per table; with no elimination heuristics and a full search the tool
  finds the optimum, but only with respect to the optimizer's estimates. The paper
  gives one worked example and no measurement of actual execution, and its claims
  that the heuristics usually find the best solutions are not backed by reported
  data. The model is steady-state over a period: it has no term for the one-time
  cost of building an index or sorting a table, so it prices upkeep against retrieval,
  not a one-off sort against later retrievals.
---

# NOTE-898: Finkelstein, Schkolnick & Tiberio — Physical database design for relational databases

## Contribution

The paper describes DBDSGN, an experimental index-selection tool for System R built at IBM San Jose and the basis of IBM's Relational Design Tool for SQL/DS. Earlier index-selection methods, it says, each solved a restricted problem: single tables only, a narrow class of statements, maintenance cost ignored or treated as independent of access path, a primary (ordering) access path fixed in advance, or an analytic cost model separate from the optimizer's. DBDSGN tries to remove all five restrictions at once: it designs record placement and secondary indices jointly, across joins, for any statement System R accepts, with maintenance costs that depend on access paths, using the optimizer's own cost estimates obtained through a new statement, EXPLAIN, which the authors prototyped.

## Key insight

Because the System R optimizer uses exactly one access path per appearance of a table and picks the cheapest combination, the cost of a statement under any set of indices is the minimum of its costs under the subsets with at most one index per table. So a few atomic cost inquiries determine the cost of every configuration, and the design problem reduces to search over configurations with costs read from a table. Asking the optimizer, not an analytic model, guarantees that a recommended design is one the optimizer will actually use: "attempts to outsmart the optimizer are misguided."

## Assumptions

- **Workload as weighted statements.** "The expected workload during that period is characterized by a set of pairs" W = {(q_i, w_i)}, where each q_i is a query, join, update, insert or delete. The weight is "a function of" either "the frequency of execution of the statement in the period" or "system load when the statement is run (e.g., statements that can be run off-shift may be given smaller weights, and statements that require particularly fast response time may be given larger weights)". Weights must often be approximated; a performance monitor helps for existing applications.
- **Optimizer principles.** "(P1) Exactly one access path is used for each appearance of a table in the statement. (P2) The costs of all combinations using one access path per table appearance are computed, and the one with the minimal cost is chosen." P1 fails for systems with TID intersection (using two indices on one table at once), which the paper calls "DBDSGN's major limitation".
- **Costs are optimizer estimates.** "When we speak of costs in the rest of this paper, we mean the optimizer's cost estimates; actual execution costs are explicitly referenced as such." The units are whatever the optimizer uses; the paper does not define them.
- **Single-column indices** (B+-trees). Multicolumn indices are considered only if the designer names them. Hashing and links are discussed as extensions (Section 7), not implemented.
- **Statistics are a snapshot.** Catalog statistics (table and column cardinalities, pages, min/max values, index leaves and levels) describe the data at design time, or are supplied by the designer. Configurations are simulated by writing statistics into the catalog entries of empty "skeleton replicas" of the tables.
- **Static period.** The design is for "a specified time period" with a fixed workload. Redesign is suggested when "the workload on a database changes substantially", "the database has been heavily updated", or "DBMS performance has degraded". There is no model of drift within the period and no term for the cost of creating indices or reorganising a table.

## Key results

**The problem (Section 2.1).** "Given a set of tables and a set of statements, together with their expected frequencies of use, the index-selection problem involves selecting for each table -the ordering rule for the stored records (which determines the clustered index, if any), and -a set of nonclustered indices, so as to minimize the total processing cost, subject to a limit on total index space. We define the total processing cost to be the frequency weighted sum of the expected costs for executing each statement, including access, tuple update, and index maintenance costs. A weighted index space cost is also added in."

**The clustered-index constraint.** "Such a solution is not possible, since (without replication) records can be ordered only one way." A configuration has at most one clustered index per table, and no column has both a clustered and a nonclustered index. Indexing everything fails for three stated reasons: each index adds maintenance cost on every update that touches it; storage is not negligible ("Typically, a System R index utilizes from 5 to 20 percent of the space used by the table it indexes"); and "a global solution cannot generally be obtained for each table independently", because the clustering of one table changes the best clustering of another (Section 4.2: with PARTS clustered on PARTNO, clustering ORDERS on PARTNO allows a one-pass merge-scan join; with PARTS clustered elsewhere, ORDERS is better clustered on SUPPNO).

**Hardness and the goal.** "Even a restricted version of the index-selection problem is in the class of NP-hard problems [13]" (Comer 1978). The authors question optimality as a goal, since workload, frequencies, statistics and the optimizer's model are all approximations, and aim instead for "a set of reasonable designs, each of which has a relatively low performance cost", from which the designer chooses.

**The cost model, term by term.**

- Query cost: COST_q(I_1,…,I_t) = min over one access path α_j per table (an index in I_j or sequential scan ρ) of C_q(α_1,…,α_t), the optimizer's best plan cost for those paths.
- Proposition 1: "The cost of a query (single-table query or join) for a configuration is the minimum of the costs for that query taken over the atomic configurations that are subsets of the configuration." For a single table with n plausible columns there are 2n + 1 atomic configurations instead of n·2^(n−1) + 2^n configurations; for a t-table join, ∏(2n_j + 1).
- Maintenance cost (Section 3.3): for a maintenance statement q, COST_q[ISET] = min over α ∈ ISET ∪ {ρ} of [C_q(α) + Σ_{β∈ISET} U_q(β, α)], where C_q is the cost of finding and modifying the tuples through α and U_q(β, α) is the cost of updating index β when α is the access path. Proposition 2 gives the same decomposition into atomic costs.
- Maintenance depends on order: U_q(β, α) takes one of two values, for an "ordered scan" (access path ordered as β is) or an "unordered scan". "For updating a nonclustered index, the only ordered scan is the index itself." A clustered index updated after access through a nonclustered index is hit "in an unordered way, incurring a higher cost."
- Storage: each index j has memory cost m_j, "the number of pages in the index", multiplied by a designer-supplied storage weight σ "to trade off page costs versus execution costs in computing total cost of a configuration", and optionally a hard limit on total index pages.
- Total: TOTALCOST[ISET] = Σ_q w_q COST_q[ISET], with the weighted storage added. In the worked example, the weighted access and maintenance costs in Figure 10 sum to 9,646 by my arithmetic, and 9,646 plus the storage cost 449 is the printed total 10,095, so the storage weight there is 1, as the text states (σ = 1).
- Adding an index α to ISET gives an access advantage A ≥ 0 and a maintenance difference D = Σ_q w_q [Σ_{β∈ISET′} U_q(β, AP_q(ISET′)) − Σ_{β∈ISET} U_q(β, AP_q(ISET))]; "ISET′ has a better total cost than ISET only if A is greater than D." D is not just the new index's upkeep, "because the maintenance costs of other indices may have changed based on the change of some access-path choices."

**Plausibility (Section 3.4).** Only columns that appear in a statement in a way an index can serve (an ANDed predicate of the form column op X; GROUP BY or ORDER BY) are candidates for that statement, as reported by EXPLAIN REFERENCE. In the example statement, COLOR and WEIGHT inside an OR are implausible, and QONORD compared with an expression is implausible. Restricting to plausible atomic configurations is exact (criterion C1, by Propositions 1 and 2). Example: two 10-column tables have 37,748,736 configurations; for one join only 35 atomic plausible configurations need costing.

**Index elimination (Section 4), heuristic except in one case.** Index k dominates j if m_k ≤ m_j and C_i(k) ≤ C_i(j) for every statement; criteria E1–E4 remove dominated or equivalent indices. These are "valid for single-table queries. When the workload also contains maintenance statements and joins, the criteria may not be valid." Criterion E2 drops a clustered index equivalent to the nonclustered index on the same column, "because there is no advantage in keeping the tuples ordered on that column." A relaxed ε-domination (maximum weighted advantage of j over k at most ε times that of k over j, 0 ≤ ε ≤ 1) is a heuristic; it is not transitive. E5 eliminates within "basic groups" defined by each surviving clustered index. For joins, three restrictions (J1: only same-table elimination; J2: clustered indices on join columns never eliminated; J3: join-column indices never eliminate others) make elimination "good (although not necessarily valid)"; "We have done a series of experiments that show that index elimination is a good heuristic when (J1), (J2), and (J3) are followed." The experiments are not reported.

**Solution generation (Section 5).** A tree enumerates subsets of surviving indices once each, clustered first; nodes whose index set exceeds the storage limit are pruned, as are "wasteful" nodes containing an index no statement uses and none could. With full expansion and no elimination, "all configurations are considered, and the optimal index configurations are found (if we assume the costs furnished by the optimizer are the actual execution costs)." For large problems, a breadth-first beam keeps the best N after expanding L indices at a time; "We have found that choosing L = 3 usually allows DBDSGN to find the best solutions." No data are given for this. "When maintenance statements are present in the workload, the best solutions are not necessarily at the leaves of the tree."

**Validation.** One worked example (Section 6): three tables (8,000, 24,000 and 72,000 tuples), ten weighted statements including an insert, an update and two deletes, 12 plausible columns, 238 join costs requested; full expansion took "approximately 12 seconds" of CPU on an IBM 3081. The proposed design clusters PARTS on QONHAND and both ORDERS and QUOTES on SUPPNO. The heaviest per-execution maintenance cost is the delete of ORDERS by SUPPNO (146). The paper reports no comparison of the recommended designs against actual execution times or against designs chosen by people, and no study of how sensitive the choice is to the weights.

## Bearing on the record

**On [QUESTION-114](../questions.d/QUESTION-114.md): the paper supplies an exact joint cost model of the right shape for one of the four cases (the bins), but it is not an amortization model, and it does not cover precomputing answers.**

- *What it gives.* Weighted retrieval cost, weighted upkeep cost and a weighted (or capped) storage cost, summed over a declared workload, with the cost of each arrangement read from the same procedure that will do the retrieving. That is the joint model [QUESTION-095](../questions.d/QUESTION-095.md) lacked, for access paths to stored items.
- *What it lacks: the term for paying once.* The total cost contains no cost of creating an index or sorting (reorganising) a table. The design is for a fixed period, and the trade it prices is a per-period rate of query savings against a per-period rate of maintenance plus storage. [QUESTION-114](../questions.d/QUESTION-114.md)'s first bullet (Sorting N bricks takes about one pass) has no counterpart. In the paper's terms a LEGO bin pays when its weighted retrieval savings exceed its weighted upkeep and space, every period; whether the initial sort is recovered is a separate question that this model does not ask. [CLAIM-303](../claims.d/CLAIM-303.md)'s condition, worth its cost only when expected reuse covers it, fits A > D in steady state, not a one-off investment. The rent-or-buy line on the survey's list is where a build cost would enter.
- *Workload.* Workload enters as statement weights that may encode either frequency or importance (urgent statements up-weighted, off-shift ones down). So the query mix is a priced mix, not only a frequency distribution, which is closer to a builder who cares more about some searches than others.
- *Speed bugs and reused inferences are not covered.* The paper chooses access paths to data, never stored answers. Nothing in it precomputes a query result. The cockpit crew's bugs and a reused inference are materialised results; the survey's Harinarayan, Rajaraman and Ullman (1996) is the right source, not this one. A filed argument, retrieved by code or tag, is nearer this paper's case: an item with indices to it.
- *Upkeep.* New bricks arriving correspond to INSERT statements, and the paper charges index and tuple maintenance on every one, synchronously, at a cost that depends on whether the arrival is processed in the order of the arrangement. The LEGO practice of letting new bricks pile up unsorted and sorting in batches (or as found, [CASE-094](../cases.d/CASE-094.md)) is deferred maintenance, which DBDSGN does not model. Neither does it model bins drifting: statistics are a snapshot, and the remedy offered is redesign when the workload or data change substantially.

**On [CLAIM-310](../claims.d/CLAIM-310.md): support for one arrangement and the query mix, none for part 3, and the bin budget only by loose analogy.**

- *One arrangement.* Directly supported for databases: "records can be ordered only one way", one clustered index per table, everything else bought as secondary indices at a price in pages and upkeep. The parenthetical "(without replication)" names the escape, which for bricks is a second copy of the collection. The paper also shows the claim's point that the arrangement is a choice with an opportunity cost: E2 refuses to spend the table's one ordering on a column where a nonclustered index does as well.
- *Query mix.* Supported by construction: the objective is a weighted sum over statements, so the best design changes with the weights, and the worked example's statements are served by different access paths. The paper adds something the claim does not have: arrangements of separate collections interact (the best clustering of ORDERS depends on the clustering of PARTS through the join method), so collections searched together cannot be arranged one at a time.
- *Bin budget.* There is no analogue of k bins. A clustered index is a total order on one column, navigated by B+-tree in logarithmically many page reads, not a partition into k bins found by scanning their labels. The storage limit caps the number and size of secondary indices, not the coarseness of the primary arrangement. The claim's k/2 + N/(2k) has no counterpart here.
- *What the item must still be told apart by.* No counterpart, and this is where the analogy fails. Once the optimizer has narrowed by an indexed predicate, the remaining predicates are evaluated tuple by tuple over every page fetched; a database lookup has nothing like pop-out, and the cost of the residual search depends only on how many tuples and pages are touched, not on which attribute distinguishes them. The nearest thing is the paper's plausibility: some predicates (an OR across columns, a comparison with an expression) cannot be helped by any index at all under one-access-path-per-table. That is a property of the query language and the optimizer, not of perception.
- *Defeat condition.* [CLAIM-310](../claims.d/CLAIM-310.md) would be defeated by a cost model in which the cheapest arrangement does not depend on the query mix. This one depends on it by construction, so it is not a test; it is an instance in another medium.

**On whether sorting is amortized search.** The paper does not use the word or the idea. Its costs are per period, the build is free, and optimality is relative to the optimizer's estimates. It treats ordering and indexing as standing structures whose value is the weighted difference they make to each statement, against their weighted upkeep and space. That supports a narrower answer than the question proposes: the steady-state part of the LEGO trade has an exact, workload-weighted model in physical database design; the one-time part does not, in this paper.
