---
status: Read
paper: LIT-tmpoi6js
title: Gupta, Mumick & Subrahmanian — Maintaining views incrementally
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the ACM's typeset PDF of the SIGMOD '93 paper
    (pp. 157–166, 10 pages, headed "Extended Abstract", with the ACM copying notice
    and "SIGMOD /5/93/Washington, DC,USA" on the first page; PDF creator "ACM",
    producer "Sony Electronic Publishing Services", a scan with an OCR layer; 976,672
    bytes, sha256 a1c710ba…ceb15), as posted on the reading list of Columbia University's
    "Ph.D. Candidacy Exam in Database Systems" (2015 list) at https://www.cs.columbia.edu/~gravano/Qual/Papers/13%20-%20Maintaining%20Views%20Incrementally.pdf,
    which answered 200. This is a course-hosted copy of the publisher's version,
    not an author's copy. Other places looked, all 2026-10-15: Unpaywall (closed,
    no OA location, no repository copy); OpenAlex (closed, any_repository_has_fulltext
    false, its only location the DOI landing page); Semantic Scholar (openAccessPdf
    points to dl.acm.org, status CLOSED); the ACM Digital Library (403, per the
    coordinator; not retried); CiteSeerX, whose site and API now redirect to web.archive.org,
    which is unreachable from this environment; web searches for author and course
    copies, which found the Columbia copy and a ResearchGate page (not used). The
    full version, Gupta, Mumick and Subrahmanian, "Maintaining views incrementally",
    TR 921214-19-TM, AT&T Bell Labs, 1992 [GMS92], which holds the proofs and the
    full DRed algorithm, was not found and not read. Text extracted with pdftotext,
    whose reading order interleaves the two columns, and again with PyMuPDF, taking
    words column by column in reading order (gms93_cols.txt), which quotations were
    checked against; the OCR layer splits words and garbles symbols (ν superscripts,
    Δ, ⊎, ¬), so every definition, algorithm, lemma and theorem was read from page
    images rendered at 120 dpi, and formulas below are transcribed from the images.
    Read: abstract, all eight sections, Algorithms 4.1 and 6.1, Definitions 3.1,
    3.2, 4.1 and 6.1, Lemmas 4.1, 6.1 and 6.2, Theorems 4.1, 6.1, 6.2 and 7.1, all
    examples, the footnotes and the reference list. Nothing skipped. Every quotation
    below was checked by script against the extracted text with all whitespace removed
    (the OCR splits words with spaces) and curly quotes straightened; those the
    OCR garbles were checked against the page images and are marked (page image),
    as are the first-page lines quoted in this history; the PDF producer is from
    the file's metadata and the reading-list title from the Columbia page itself.
    Quotations of the record were checked against the record's files.
date: '2026-10-15'
summary: >-
  Two algorithms compute the changes to a stored derived relation (a view) from
  changes to the base relations, without recomputing it. Counting stores, for each
  derived tuple, the number of its derivations and propagates signed counts through
  delta rules stratum by stratum; it is stated correct for nonrecursive Datalog
  or SQL views with stratified negation and aggregation, under set or duplicate
  semantics, and is argued to cost little beyond evaluating the view. DRed (delete
  and rederive), for recursive views under set semantics only, deletes an overestimate
  of what a deletion invalidates, puts back those tuples that still have a derivation
  from what remains, then adds what insertions derive; it is stated to yield exactly
  the tuples derivable from the new base. The paper is an extended abstract: the
  theorems are stated without proof (proofs are referred to a 1992 AT&T report),
  cost claims are argued, not measured, and there are no experiments.
---

# NOTE-tmpgv5ap: Gupta, Mumick & Subrahmanian — Maintaining views incrementally

## Contribution

A view is a derived (idb) relation defined over stored (edb) relations; materializing it stores its extent. The paper gives two incremental view maintenance algorithms, which "use the view definition to produce rules that compute the changes to the view using the changes made to the base relations and the old materialized views". It assigns them domains: "we are proposing the counting algorithm for nonrecursive views, and the DRed algorithm for recursive views, as we believe each is better than the other on the specified domain". It claims to be the first to handle aggregation in incremental maintenance, and the first to do so for recursive views.

## Key insight

A derived fact should be removed when its last derivation is removed, not when one of its derivations is. For nonrecursive views, the number of derivations is finite and can be counted during ordinary evaluation, so storing a single integer per tuple suffices: a deletion subtracts the derivations it destroys, and the tuple goes when its count reaches zero. "Note that we store only the number of derivations, not the derivations themselves." For recursive views counts can be infinite or uncomputable, so DRed keeps no count: it deletes everything that any deleted fact touched, then asks of each deleted tuple whether it can still be derived from what is left, and restores those that can.

## Assumptions

- **Language.** Datalog "extended with stratified negation [VG86, ABW88], and stratified aggregation [Mum91]", which the authors say maps to a class of recursive SQL queries and back. Negation must be safe and stratified (Section 6.1); "Nonrecursive programs are always stratified."
- **Strata.** Definition 3.1: collapse each strongly connected component of the dependency graph to a node; a topological sort gives stratum numbers (SN), with base predicates at 0; a rule's RSN is the SN of its head.
- **Counts.** count(t) is "the number of distinct derivations of tuple t", taken from the multiplicity under duplicate semantics as defined in [Mum91] (positive programs) and [MS93a] (stratified negation). Deletions carry negative counts, insertions positive. ⊎ adds counts and drops a tuple whose count becomes 0; a join multiplies counts.
- **Changes** are insertions and deletions of base tuples (an update is a deletion plus an insertion). DRed is also said to handle insertion and deletion of rules.
- **DRed needs set semantics**: "Only set semantics can be used for this algorithm."
- **Incrementality is a heuristic.** "We stress that the above is only a heuristic. For example, if an entire base relation is deleted, it may be cheaper to recompute a view that depends on the deleted relation (if the new view will quickly evaluate to an empty relation) than to compute the changes to the view." Neither algorithm decides when to recompute instead.

## Key results

**Counting (Section 4, Algorithm 4.1).**
- *Delta rules (Definition 4.1).* For each rule r: p :- s_1 & … & s_n, n delta rules Δ_i(r): Δ(p) :- s_1^ν & … & s_{i−1}^ν & Δ(s_i) & s_{i+1} & … & s_n, where s^ν is the relation after the change. Subgoals before position i use new values and those after use old values, so each changed derivation is counted once (page image, p. 160).
- *Algorithm 4.1.* Input: a nonrecursive program, the stored materializations of its derived relations, and the changes to its base relations. Process rules in increasing RSN; for each rule compute Δ(P) from its delta rules and set P^ν = P ⊎ Δ(P). Output: the changes to the derived relations.
- *Lemma 4.1.* If the deleted base tuples Δ⁻ are a subset of the edb E, the algorithm derives Δ(t) with count at least −count(t): no more derivations of a tuple are deleted than it had.
- *Theorem 4.1.* If t has count(t) derivations over E and count(t^ν) over the changed edb E^ν, Algorithm 4.1 derives Δ(t) with count count(t^ν) − count(t). Stated without proof.
- *Set semantics (Section 5.1).* With the optional statement Δ(P) = set(P^ν) − set(P), only changes in set membership are passed up, and counts in stratum i + 1 are computed as if every lower-stratum tuple had count 0 or 1. Example: p(a) has 20 derivations, 10 are deleted, nothing propagates beyond stratum 1. The abstract's optimality claim is in these terms: "The algorithm is optimal in that it computes exactly those view tuples that are inserted or deleted." No proof of optimality is given.
- *Cost (argued, Section 5).* Under duplicate semantics the algorithm needs no extra work, since systems already track duplicates; ⊎ with negative counts is multiset difference, executable "in time O(n)log(n) or O(n)" in the size of the operands (page image, p. 161). Under set semantics, counting duplicates can piggyback on duplicate elimination, and since select, join, project and union each derive one tuple per derivation, "tracking counts for a nonrecursive view is almost as efficient as evaluating the nonrecursive view." No measurement supports this.
- *Negation (Section 6.1, Definition 6.1, Theorem 6.1).* For a negated subgoal ¬q, Δ(Q̄) holds t with count 1 if t ∈ Δ(Q) and t ∉ Q ⊎ Δ(Q) (t left Q, so ¬q became true), and count −1 if t ∈ Δ(Q) and t ∉ Q (t entered Q, so ¬q became false); Lemma 6.1, (¬q)^ν = ¬(q^ν). "Algorithm 4.1 works correctly in the presence of negated subgoals." (page image, p. 163). Stated without proof.
- *Aggregation (Section 6.2, Algorithm 6.1, Theorem 6.2).* For a GROUPBY subgoal, each group whose members changed has its old aggregate tuple deleted (count −1) and its new one inserted (count 1) if they differ. The paper says the new value can be computed from the old tuple and Δ(U) "for each of the aggregate functions MIN, MAX, COUNT, SUM, and for any other incrementally computable function"; otherwise the group is recomputed from U. Theorem 6.2: Algorithm 4.1 works correctly with aggregate subgoals. Stated without proof. (Not noted in the paper: deleting the current minimum or maximum of a group cannot be handled from the old value and Δ(U) alone; that case needs the group's remaining tuples.)

**Counting on recursive views** is set aside: recursive queries "may have infinite counts associated with them", and "computing counts for recursive views is expensive and furthermore counting may not terminate on some views" (Section 8).

**DRed (Section 7).** For recursive views with set semantics, stratum by stratum.
1. *Overestimate deletions.* For each rule, Δ⁻-rules δ⁻(p) :- s_1 & … & s_{i−1} & δ⁻(s_i) & s_{i+1} & … & s_n over the old relations, applied until the set of potentially deleted tuples stops changing; remove δ⁻(p) from P. This is what semi-naive deletion does: "Alternative derivations of t are not considered. Semi-naive therefore computes an overestimate of the tuples that actually need to be deleted."
2. *Rederive.* δ⁺(p) :- δ⁻(p) & s_1^ν & … & s_n^ν: a deleted tuple is put back if it has a derivation from the current (reduced) relations, iterated until no more are put back.
3. *Insert.* Δ⁺-rules Δ⁺(p) :- s_1^ν & … & s_{i−1}^ν & Δ⁺(s_i) & s_{i+1}^ν & … & s_n^ν, iterated to fixpoint.
- *Theorem 7.1.* With Δ⁻ and Δ⁺ the base tuples deleted and inserted, "The new derived view computed by the DRed algorithm contains tuple t if and only if t has a derivation in the database E^ν = (E − Δ⁻) ∪ Δ⁺." (page image, p. 165). Stated here without proof: "This three step process is formalized as an algorithm, and proved correct, in [GMS92]."
- *Extensions asserted, not shown:* stratified negation and aggregation in recursive views ("The details of the algorithm are given in [GMS92]"), and changes to rules.
- *Comparisons, asserted:* the Propagation/Filtration algorithm of Harrison and Dietrich "can be worse that our rederivation algorithm by an order of magnitude (examples in full paper)" (sic); DRed "can be used for nonrecursive views also but it is less efficient than counting". Neither is measured here.

**Worked examples** (hop and tri_hop over link; only_tri_hop with negation; min_cost_hop with MIN) show the delta computations; they illustrate and do not test.

## Bearing on the record

**On [QUESTION-105](../questions.d/QUESTION-105.md): for one family of revisions, the paper names two retained states and they are not provenance.**

- The family is narrow and fixed: insertions and deletions of base facts (and, for DRed, of rules) under a fixed program, with the new view defined as everything derivable from the new base (Theorem 7.1). There is no choice in the revision and no inconsistency to resolve, so nothing like AGM's selection function ([THEORY-353](../theory.d/THEORY-353.md)) is needed. In the terms of Hansson's survey as [QUESTION-105](../questions.d/QUESTION-105.md) reports it ([THEORY-347](../theory.d/THEORY-347.md)), the edb is the base, the part "held in their own right", and the view is the derived part; the paper's revision is base revision with derived facts dropped when their support goes.
- For that family, what must be retained beyond the base, the rules and the materialized view? Counting: one integer per derived tuple, its number of derivations, sufficient for nonrecursive programs (Theorem 4.1). Not the derivations, not which premises support what. DRed: nothing more; the support check is redone at revision time by rederivation from the current database. So the paper gives two points on [QUESTION-105](../questions.d/QUESTION-105.md)'s spectrum, both short of a justification graph: a count, and nothing plus recomputation.
- The count fails where dependencies are cyclic: counts can be infinite and counting "may not terminate", so for recursive programs the paper falls back to overdelete and rederive. That narrows [QUESTION-105](../questions.d/QUESTION-105.md) in a useful way: a cheap summary of support (how many derivations) suffices only when support is acyclic. The record's arguments are not guaranteed acyclic, so for them the paper's own answer is to recheck support from what remains, not to store it. That a count is unsound under cycles is the record's inference from the paper's two reasons (infinite counts, non-termination); the paper does not discuss self-supporting cycles explicitly.
- Defeated alternatives play no part: a deleted derived tuple is not kept, and nothing records why it went.

**On [CLAIM-303](../claims.d/CLAIM-303.md)'s dependency-tracking term: the paper shows where the tracking cost can sit, and leaves its size unmeasured.**

- [CLAIM-303](../claims.d/CLAIM-303.md) charges dependency tracking as part of filing. Counting puts the cost at derivation time (one integer per tuple, argued to be nearly free for nonrecursive views); DRed puts it at revision time (an overestimate, which can be large, then a rederivation). Neither is measured here, and the paper's comparisons of the two and with other algorithms are assertions.
- The paper also states [CLAIM-303](../claims.d/CLAIM-303.md)'s refresh trade at the level of one change: incremental maintenance is "only a heuristic", and recomputing can be cheaper when a change is large. It gives no rule for choosing.
- Correctness here means the view equals what the new base derives. A view that is maintained this way cannot go stale, so [CLAIM-303](../claims.d/CLAIM-303.md)'s added term, the cost of reusing an obsolete argument, does not arise: the paper is about removing staleness on every change, not pricing it.

## Limitations

- Extended abstract. No proofs of Lemma 4.1, Theorems 4.1, 6.1, 6.2, 7.1, nor of the optimality claim; DRed with negation and aggregation is only described as existing in [GMS92].
- No experiments and no complexity bounds beyond the O(n log n) multiset difference; efficiency claims are argued.
- Counting is for nonrecursive views; DRed is for set semantics only.
- Aggregate maintenance for MIN and MAX under deletion is stated more broadly than the method supports.
- Changes are to base facts (and rules), with a fixed program; there is no notion of retracting a derived conclusion directly.

## Open questions

- How large is DRed's overestimate in practice relative to the true deletions, and when does it exceed recomputation?
- For a record of arguments with cyclic support, is there a retained summary between a count (unsound under cycles) and full rederivation, for example per-stratum counts or well-founded support?
- Can the record's revisions be put in the paper's form, a base of held claims and a fixed set of inference rules, closely enough for Theorem 7.1's semantics to apply?
