---
number: 891
status: Read
formerly:
- NOTE-tmp60fit
paper: LIT-1097
title: Yao — Should tables be sorted?
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the published Journal of the ACM version (28(3),
    pp. 615–628, 14 pp., ACM's scanned typeset pages with the 1981 ACM copyright
    notice; "RECEIVED JULY 1979, REVISED JUNE 1980, ACCEPTED AUGUST 1980"), as hosted
    on a University of Maryland course page (www.cs.umd.edu/users/gasarch/COURSES/858/S13/tables.pdf,
    Gasarch's CMSC 858 reading list). ACM serves this PDF free (OpenAlex and Unpaywall:
    bronze, publishedVersion, at dl.acm.org/doi/pdf/10.1145/322261.322274), but
    dl.acm.org answered 403 to direct requests and to WebFetch from this environment,
    and the Internet Archive capture of that URL (web.archive.org/web/20241126095045/…,
    listed by the Wayback availability API) could not be fetched because web.archive.org
    reset every connection. The author's own institutional version, Stanford report
    STAN-CS-79-753 (July 1979, i.stanford.edu/pub/cstr/reports/cs/tr/79/753/CS-TR-79-753.pdf),
    was also fetched and compared section by section: it has the same theorems,
    proofs, appendices and acknowledgment (including Theorem 1′), with Tarjan–Yao
    as reference [18] rather than [19]. Also looked, 2026-10-15: CiteSeerX entries
    10.1.1.138.3178 and 10.1.1.75.5573 (listed by OpenAlex; connection reset, nothing
    fetched); Semantic Scholar (openAccessPdf points to the ACM URL only). Text
    extracted with pdftotext; the JACM file is an OCR'd scan, so every theorem and
    lemma statement (Theorems 1, 1′, 2, 3, Lemmas 1, 2, Ramsey's theorem as stated)
    was checked against page images at 110 dpi. Read: the abstract, Sections 1–5,
    Appendix A (the case analysis for Theorem 2) and Appendix B (the separating-system
    construction for Lemma 2), the bibliographic note and the references. Nothing
    skipped; the arithmetic in Appendix B's final chain of inequalities was followed
    but not re-derived. Quotations below were checked by script against the extracted
    text of the JACM version or the Stanford report, whitespace-normalised; three
    that the OCR garbles ("~mprove", "m ~ oo", and a sentence broken by the page
    header on p. 622) were checked against the page images instead and are marked
    [image-checked].
date: '2026-10-15'
summary: >-
  For storing a set of n keys from a universe {1,…,m} in a table so that the membership
  query (is x in S?) is answered with the fewest worst-case adaptive probes, Yao
  proves that when the table cells may hold only keys of S or a bounded number of
  pointer symbols, sorted order with binary search (⌈lg(n+1)⌉ probes) is optimal
  once m exceeds a Ramsey-number threshold N(n, p, q), whatever the arrangement
  rule, table size or hashing scheme. The threshold is astronomically large, and
  for small universes sorted order is beaten (one probe suffices for m = 3 with
  n = 2, and for m ≤ 2n − 2 with n > 2). The optimality also fails as soon as one
  cell may hold an arbitrary value from the universe: with a single extra "directory"
  cell, two probes suffice for m ≥ 2^{16n²}. Only query cost is counted; building
  the table is free and unconstrained, so the paper says nothing about the cost
  of arranging or about trading arrangement cost against lookups.
---

# NOTE-891: Yao — Should tables be sorted?

## Contribution

Yao asks whether any storage scheme for a static set can answer membership queries in fewer worst-case probes than binary search on a sorted table, in a model whose only cost is the number of table cells read, and where both the arrangement of the keys and the adaptive search strategy are arbitrary functions. This is the problem setting later called the cell-probe model (the paper does not use that name; it speaks of "probes" and, in its bibliographic note, of "Wordwise-access models" used in earlier papers). He answers with a lower bound that holds only for huge universes and two constructions showing it fails without that condition or once cells may hold encoded information.

## Key insight

If the universe is large enough, Ramsey's theorem forces any arrangement rule to behave, on some subuniverse of 2n − 1 keys, exactly like a sorted table under one fixed permutation of positions. On that subuniverse no search strategy can do better than binary search (Lemma 1, an adversary argument). So no arrangement of the keys themselves can beat sorting for large m. The argument depends on the table holding nothing but members of S (and pointer symbols drawn from a fixed finite set): a single cell holding a value outside S can encode which of a family of partitions of the universe separates the stored keys, and then the key's position is known after reading that cell.

## Assumptions

- **Problem.** Static membership: a fixed set S of n distinct keys from the key space M = {1, 2, …, m}; queries "Is j in S?". The paper notes that its one-probe scheme answers membership without finding the key's location, so membership and retrieval differ.
- **Basic model.** A table T of exactly n cells holding the n keys. A "table structure" is any rule assigning each n-subset of M a table; a "search strategy" for key K is a sequence of probes T(i₁) = ?, T(i₂) = ?, … that is fully adaptive (each probe location may depend on K and on all previous answers). Cost c(table structure, strategy) is the number of probes in the worst case; f(n, m) is the minimum cost over all pairs. Nothing is charged for computing the probe locations or for building the table.
- **General model (Theorem 1′).** A table of q cells; each cell holds an element of S ∪ P, where P is a fixed set of p "pointer" symbols. Keys of S may be duplicated or omitted. f(n, m, p, q) is the minimum worst-case cost. Yao adds that allowing S nonunique representations "obviously will not improve the worst case cost" [image-checked], so the model covers linked lists, search trees and the usual hashing schemes. The essential restriction is that a cell cannot hold a key outside S: Theorem 3 shows the result "depends heavily on the fact that keys outside of the set S may not be present in the table."
- **Encoding model (Section 4).** A sorted table of n cells plus one extra cell (cell 0) whose content is "allowed to be any integer between 1 and m".
- **Regime.** The theorems are about fixed n with m → ∞ (word size growing), not about n → ∞ with m tied to n. Yao calls this "a word-length-independent framework (by letting m → ∞)" [image-checked].

## Key results

- **Sorted is not always optimal.** For n = 2, m = 3 a "cyclic" table answers every query in one probe, against two for a sorted table: "Thus, a sorted table is not optimal for n = 2, m = 3." For n = 2 and m ≥ 4, any table structure contains three keys stored as a permuted sorted table, so f(2, m) = 2 = ⌈lg 3⌉.
- **Lemma 1.** If a table structure stores the keys in sorted order (or under some fixed permutation), then ⌈lg(n + 1)⌉ probes are needed in the worst case by any search strategy, provided m ≥ 2n − 1 and n ≥ 2. Adversary proof by induction on n, searching for K = n.
- **Theorem 1.** For every n there is an N(n) such that f(n, m) = ⌈lg(n + 1)⌉ for all m ≥ N(n). Proof: colour each n-subset of M by which of the n! position permutations the table structure uses for it; by Ramsey's theorem with N(n) = R(2n − 1, n, n!) some 2n − 1 keys have all their n-subsets stored under one permutation; apply Lemma 1.
- **Theorem 1′.** For any n, p, q there is an N(n, p, q) such that f(n, m, p, q) = ⌈lg(n + 1)⌉ for all m ≥ N(n, p, q); the colouring has (n + p)^q classes and the threshold is R(2n − 1, n, (n + p)^q). Note what this covers: extra space (q may exceed n), pointers and duplicates do not help when the universe is large. It holds for "all common schemes such as hashing, sorted tables, and linked list structures."
- **The threshold is impractical.** "The numbers N(n) in Theorem 1 are extremely large even for moderate n. Thus the result is not too useful in practical terms." No explicit bound on N(n) is given beyond the Ramsey number.
- **Theorem 2 (when one probe suffices).** Let g(n, k) be the largest m with f(n, m) = k. Then g(n, 1) = 3 if n = 2, and g(n, 1) = 2n − 2 if n > 2. The lower bound is an explicit "apartment" assignment (rooms 1…n − 2 have a lower and an upper tenant, rooms n − 1 and n one each); the upper bound is the case analysis of Appendix A, ending in a proof that no one-probe structure exists for n = 3, m = 5. In the scheme, "the above scheme only allows one to determine in one probe whether an element is in the table, but not the location of the element (when it is in)." g(n, 2) is left open.
- **Lemma 2.** There is an n-separating system for {1, …, m} of size at most 4^{n²}·(lg m)^{n−1} (Appendix B, recursive block construction).
- **Theorem 3 (two probes with one extra cell).** There is an N′(n) such that if m ≥ N′(n), a sorted table plus one extra cell holding an arbitrary integer in [1, m] supports membership search in two probes: read cell 0 to learn which separator in the system places each stored key in a known position, then probe that position. Lemma 2 gives N′(n) = 2^{16n²}; Yao reports Tarjan's improvement to exp(cn log n), and Graham's nonconstructive bound implying a "canonical" two-probe structure whenever m ≥ exp(cn).
- **Conclusion as stated.** "The main conclusions are, roughly, that when the word size is large, sorted tables are optimal structures if only the addressing power of a random-access machine can be used, but far from optimal once arbitrary encoding of the information is allowed in the table" [image-checked; the sentence runs across pp. 621–622]. "These results are mainly of theoretical interest, although Theorem 3 suggests that there may be fast retrieval schemes in more practical situations." Both extremes, m ≈ n and m ≥ 2^{16n²}, need at most two probes; the intermediate range is open, except that "Tarjan and Yao [19] have shown that when m grows at most polynomially in n, one can retrieve in O(1) probes with a O(n)-cell table." The case m = 2^{√n} is named as open.
- **Dynamic problems are only conjectured.** Open problem (1): for sequences of INSERT, DELETE, MIN, "We conjecture that, unlike the membership problem, nonconstant lower bounds exist even if arbitrary encoding is allowed." Nothing about maintaining or building a structure is proved.

## Bearing on the record

[QUESTION-114](../questions.d/QUESTION-114.md) lists this paper as "the founding cell-probe paper: when storage in sorted order beats other arrangements for lookup". Held against the text:

- **"Founding cell-probe paper": holds, with a qualification.** It sets up the model the later literature calls cell probe (cost = cells read, arbitrary arrangement, arbitrary adaptive strategy, nothing else charged) and is the standard citation for it. The paper itself does not use the term, and it credits the membership problem to Minsky and Papert's bitwise-access "exact match" problem, with earlier wordwise-access work by Elias, Sprugnoli and Tarjan.
- **"When storage in sorted order beats other arrangements": does not hold as worded.** The main theorem is not a condition under which sorted order beats the alternatives; it says that under the restriction that cells hold only stored keys or pointer symbols, and for a universe larger than a Ramsey-number threshold, no arrangement beats sorted order (sorted order ties for best; hashing and search trees can at best match it in the worst case). The other results go the opposite way: sorted order is beaten for small universes (m ≤ 2n − 2 gives one probe), and beaten for large universes as soon as one cell may hold encoded information (two probes, Theorem 3), and, via Tarjan–Yao which it cites, when m is polynomial in n with O(n) cells. Yao's own summary is that sorted tables are optimal only if the addressing power alone is used and "far from optimal" otherwise. A faithful one-line description: "the founding cell-probe paper: sorted order is worst-case optimal for membership only for astronomically large key spaces and only if cells hold nothing but the keys; one encoded cell brings search to two probes."
- **What counts as cost: lookup only.** The cost is worst-case probes per query. Space enters only as the table size q (fixed in the basic model, arbitrary but fixed in Theorem 1′). Building the arrangement is free: a table structure is any function from sets to tables, with no charge for computing it, and the Theorem 3 directory is found by search over a separating system without regard to cost. There is no average case, no query distribution, no update cost and no count of queries.
- **Amortization: nothing.** The paper does not bear on whether sorting is amortized search, on what organising a collection costs, or on how that cost trades against later lookups. It compares lookup costs across arrangements once each arrangement exists. The only dynamic matter is the conjecture about INSERT/DELETE/MIN, which is unproved here. For [QUESTION-114](../questions.d/QUESTION-114.md) it supplies one side of the ledger, the lookup-cost floor and when sorted order attains it, and nothing on the other side. If the question needs the joint cost of building and querying, it needs other sources (the dynamic cell-probe literature, or sorting lower bounds combined with search bounds), not this one.
- **Universe size does the work.** Every result is indexed by m relative to n. The record's description omits this, but it is the paper's main point: the optimality of sorting is a large-universe, no-encoding phenomenon.
