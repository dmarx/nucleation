---
number: 902
status: Read
formerly:
- NOTE-tmpxc25d
paper: LIT-1089
title: Piatetsky-Shapiro — The optimal selection of secondary indices is NP-complete
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full from the scan SIGMOD itself serves openly: sigmodrecord.org's page
    for the January 1983 issue (sigmodrecord.org/issues/sigmod-record-january-1983)
    links the paper's PDF through a download counter (sigmodrecord.org/?smd_process_download=1&download_id=11929),
    which redirects to sigmodrecord.org/publications/sigmodRecord/8301/pdfs/984523.984530.pdf.
    It is a 4-page scan of the typescript (dated "31 May 1982"), printed pages 72–75,
    with an OCR text layer. Text extracted with pdftotext -layout. The OCR letter-spaces
    the abstract and garbles subscripts and a few words ("seconaary", "reauctng"),
    so all four pages were also read as page images; the Schkolnik bound, which
    the text layer gives as "O(2 M ) logM)", reads O(2^(M^.5) log M) on the image.
    Read: everything, abstract, introduction, the transformation, the proof, the
    remark on off-line updates, and the nine references. Nothing skipped. None of
    the works it cites was read, so what it says of Schkolnik, Hammer and Chan,
    and the others is its account of them. Every quotation below was checked against
    the extracted text by script, with whitespace normalised.
date: '2026-10-15'
summary: >-
  For one relation, a known mix of equality queries and updates, single-attribute
  secondary indexes, and a fixed upkeep charge per index on each update, choosing
  the index set that minimizes average transaction cost is NP-hard: minimum set
  cover reduces to it, each subset becoming an attribute and each element a query
  that any one of its attributes' indexes can answer. The paper calls the problem
  NP-complete but states only the optimization version, and the proof is a sketch
  of about half a page. Storage is not in the model; the only price of an index
  is upkeep on updates. A variant with off-line updates under an update-cost budget
  is asserted NP-complete without proof. The paper does not cite or discuss Comer
  1978.
---

# NOTE-902: Piatetsky-Shapiro — The optimal selection of secondary indices is NP-complete

## Contribution

A short note proving that the index-selection problem in the form the 1970s literature had posed it, choose secondary indexes for a file to minimize expected transaction cost under known frequencies, is intractable in general. Its stated purpose is to redirect effort: the result "will probably skew the further effort in this area toward heuristic algorithms, rather than algoritms attempting to find the optimal solution."

## Key insight

When a query can be answered by any one of several indexes, and each index costs something to keep, choosing indexes is choosing a cover. Queries are the elements to be covered, attributes are the sets, and an index pays for itself as soon as it rescues one query from a sequential scan. So the cheapest index set is the smallest set of attributes that reaches every query, which is minimum set cover.

## Assumptions

The general problem as posed in the introduction: given "1. Relation (file) and list of its attributes", "2. Frequencies of transactions of each type", and "3. Distribution of values of each attribute : i.e. selectivity and any other statistics considered by query optimizer", "we want to select the set of indices which minimizes the average transaction cost." Transaction types are equivalence classes: "2 Transactions have the same type if their cost estimates are the same for each possible set of indices".

The instance built in the reduction, which is all the proof covers:

- **One relation** R with N attributes A_1 … A_N, one per subset S_i of the set-cover instance.
- **Workload.** Only queries and updates, "there are no deletions or insertions." Queries are conjunctions of equality predicates, listing all attributes. Each element of S becomes a query whose condition has one predicate A_i = value for each subset S_i containing it. Updates: for each subset S_i one of its points is chosen and made an update on A_i, updates falling on the same point being merged, so that there is "exactly ONE update" for each attribute. Frequencies are left implicit ("trivially abstracted from the actual counts").
- **Data.** "All attributes have the same selectivity, which is equal to 1 / N R", NR the number of tuples, so one tuple matches any equality predicate and at most one index is used per query.
- **Indexes.** "We are considering only single - attribute indices ( with such a low selectivity multiattribute indices have no advantages)." Only secondary indexes; the file's own order (clustering) is not a choice in the model.
- **Costs, in records accessed.** A query costs NR by sequential scan and 1 through an index; output cost is ignored as the same under every index set. An update costs its condition's evaluation (as for a query), plus a data-record cost ignored as constant, plus "COST_INDEX_UPDATE * (Number of updated attributes)". The upkeep charge is assumed "the same for all indices and is less than the difference between the cost of sequential scan and the cost of the indexed access."
- **No storage cost and no space limit.** An index's only price is upkeep on updates. No build cost.
- **Objective.** "Find the set of indices which minimizes the average cost of database use (hereafter The COST) under the given Transaction frequency distribution."

## Key results

- **The problem stated.** It is given only as an optimization problem (the QUESTION line above). No decision version (is there an index set of cost at most B?) is written down. Membership in NP is argued as: "Clearly, the problem of optimal selection of secondary indices for a file is in NP, since the transaction cost estimation function runs in time which is at most polynomial in the number of attributes." Strictly, what is shown is that the optimization problem is NP-hard and its natural decision version is NP-complete.
- **Source problem.** MINIMUM SET COVER (Garey and Johnson 1979; Karp 1972): a collection C of N subsets of a finite set S and an integer K ≤ |C|; does C contain a cover of S of size K or less?
- **The proof.** "adding new index increases The COST by COST_INDEX_UPDATE"; if some query moves from a sequential scan to the new index, "The COST is decreased by at least COST_SEQ__ACCESS - COST_IND_ACCESS which is more than COST_INDEX_UPDATE". Hence an optimal set reaches every query, and among sets that do, all queries cost the same, so the optimum "is the collection with the minimal numbcr of attribules such that the union of corresponding subsets of S is equal to S" (OCR spellings kept; the page image reads "number of attributes"). Comparing the size of the optimal index set with K answers the set-cover question. The argument is a sketch; it is sound for the constructed instance, given that each attribute carries exactly one update so that each index adds the same upkeep. (The text says "less than K" where at most K is meant.)
- **Theorem (as titled).** Optimal selection of secondary indices to minimize average transaction cost under a known transaction frequency distribution is NP-complete. *Holds when:* the number of attributes N and the number of transaction types grow with the input; queries may be conjunctions over several attributes; each index has a positive upkeep cost smaller than the saving of one indexed query over a scan. The hardness is already present with single-attribute indexes, equal selectivities, uniform upkeep and no storage term.
- **Variant, unproved.** With "updates are made off-line", minimize query cost "under the condition that the cost of updates does not exceed certain constant": "This problem is also NP-complete" and "The proof is similar and also uses reduction of". No proof is given.
- **Prior algorithms, as it reports them.** Schkolnik (1975) solves the problem in O(2^(√M) log M) for M domains (exponent read from the page image). Hammer and Chan (1976) give a polynomial heuristic "not guaranteed to find the optimal solution or to be within some percentage of the optimal solution."
- **On Comer 1978.** Nothing. Comer is not cited, and the paper does not mention any earlier hardness result for index selection. It presents itself as the first proof that the cost-minimizing problem is NP-complete. So this paper cannot confirm or refute the secondary account's description of Comer.

## Bearing on the record

**On [QUESTION-114](../questions.d/QUESTION-114.md): the joint trade can be stated exactly, and it is NP-hard in general, but only as attributes and query types grow.**

- This is the workload-based hardness result the question wanted from Comer. It has a known transaction mix, per-query savings, and a per-index upkeep charge, and minimizes their frequency-weighted sum. The secondary account's description of it, a reduction from set cover, is correct.
- It narrows the question's framing on one point. The question prices each further index "in space and upkeep". This paper prices it in upkeep only; storage is absent. Hardness does not need the space term, but it does need some per-index price: with no upkeep and no budget, indexing every attribute is optimal and the problem is trivial. The off-line variant puts the price in a budget instead, and is asserted, not proved, hard.
- It does not cover organizing ahead in the sense of sorting. Only secondary indexes are chosen; the file's one physical order, which is what a sorted collection is, is not a decision variable, and build cost is not counted. So for whether sorting is amortized search it supplies the cost model's shape (upkeep against per-query savings under a mix) but not the clustering choice, which Finkelstein et al. 1988 ([LIT-1084](../literature.d/LIT-1084.md)) include.
- Does the hardness bite a builder sorting LEGO bricks into bins? The features it uses are: many candidate attributes (one per subset), many query types (one per element), queries that can be served by any of several attributes, and a fixed price per maintained index. A builder's query mix (a red 2×4 brick, any slope) does have the multi-attribute, any-of-several shape. But NP-hardness is a statement about growth: with a handful of attributes (colour, shape, size, set) the 2^N candidate sets are few, and even Schkolnik's 1975 algorithm is fast. The result says no exact method scales with the number of attributes and query types; it does not say a builder's actual choice is hard. It also says nothing about bins as a physical partition, which is one clustering choice per collection rather than a set of secondary indexes, and its 1/NR selectivity (every predicate picks one record) is far from a colour predicate that picks a tenth of the bricks.
- Against Finkelstein et al. 1988 ([LIT-1084](../literature.d/LIT-1084.md)): consistent. This paper predicted that effort would turn to heuristics, and DBDSGN is that turn, with the optimizer's own cost estimates, a clustering choice, and a storage term that this paper lacks. This paper gives the reason heuristics are used; it does not evaluate them.
- Against Harinarayan et al. 1996 ([LIT-1094](../literature.d/LIT-1094.md)): the two hardness results have the same structure, a precomputed structure answers a set of queries and the choice is a covering problem, but Harinarayan et al. bound the number of views and prove the greedy rule reaches at least 63% of the optimal benefit. This paper gives no approximation result and notes that the known heuristic had none. The set-cover reduction does not by itself transfer a guarantee to the cost objective, since the cost includes a large term the same for every cover.
- On Comer 1978 ([LIT-1086](../literature.d/LIT-1086.md)): this paper does not mention it. The record should cite this paper, not Comer, for workload-based index selection being NP-complete, and leave the description of Comer's own result as the secondary account's, unverified.
