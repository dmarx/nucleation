---
number: 888
status: Read
formerly:
- NOTE-tmp4jlib
paper: LIT-1085
title: 'Athanassoulis et al. — Designing access methods: the RUM conjecture'
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full 2026-10-15 from the publisher's open-access PDF on OpenProceedings
    (openproceedings.org/2016/conf/edbt/paper-12.pdf; 6 pp., printed pages 461–466,
    headed "Visionary Paper"), which is the URL DataCite registers for DOI 10.5441/002/edbt.2016.42.
    The URL answered 200 with a 511,891-byte PDF on 2026-10-15 (sha256 0d1e3c2f…5d38);
    the file's internal creation date is 2019, so OpenProceedings regenerated it
    after the conference, and its first page carries the EDBT 2016 copyright line.
    Licence, printed on page 1: "Creative Commons license CC-by-nc-nd 4.0", so the
    copy is kept in the reading folder unaltered. Also checked: DataCite (title
    and seven authors as cited, year 2016, no rights field); OpenAlex (green open
    access, repository full text reported); Unpaywall (404, no record for this DataCite
    DOI). Text extracted with pdftotext, in raw and layout modes. Table 1 and Figures
    1–3 do not survive extraction, so Table 1's entries and the placement of structures
    in Figure 1 were read from page images of pages 463–464. Read: abstract, all
    six sections, the three propositions, the conjecture, Table 1 with its caption
    and footnotes, Figures 1–3, and the reference list. Nothing skipped. The paper's
    cited works (cracking, LSM, Finkelstein-style index tools) were not reread for
    this note; what it says of them is its account. Every quotation below was checked
    against the extracted text by script, whitespace normalised and line-break hyphens
    rejoined; two quotations that the extraction splits around a page footer or
    Figure 2's labels (the §3 gloss, and the sentence on the sorted column) were
    checked in their parts, and quotations with an ellipsis were checked part by
    part. Quotations of the record's own entries were checked against those entries;
    the survey's description of the paper is quoted from the reading request.
date: '2026-10-15'
summary: >-
  The paper names three per-operation overheads of an access method, each a ratio
  to the base data alone (read, update and space amplification, each minimum 1.0),
  and conjectures that bounding any two forces a lower bound on the third. Its evidence
  is three one-line propositions about extreme designs over an integer array (a
  direct-address array, an append-only log, an unindexed dense array), a placement
  of known structures on a triangle, and a table of asymptotic I/O costs; nothing
  is proved, and the formal statement does not say how large the forced bound is,
  so as worded it is close to empty. The extremes themselves show the overheads
  are not symmetric: the space-minimal design is also update-minimal, and the read-minimal
  design keeps updates at 2.0, so the clean conflicts are read against space and
  update against both. Build cost appears in the table but is outside the triangle,
  there is no workload weighting, no time or deadline, and no cost of examining
  an item other than reading it.
---

# NOTE-888: Athanassoulis et al. — Designing access methods: the RUM conjecture

## Contribution

A six-page vision paper. It proposes that every access method trades among three overheads, read (R), update (U) and memory (M), states this as a conjecture, places familiar structures on a triangle with those three as corners, and sets out a research programme for access methods whose position on the triangle can be tuned or can move with the workload. It claims no theorem: "proving the RUM Conjecture will expand on this line of research."

## Key insight

Measure every access method by how much more it reads, writes and stores than the base data it serves. Auxiliary structure is what lowers one of these, and auxiliary structure is itself something read, written and stored, so pushing one ratio to its floor of 1.0 pushes another up. The paper's own examples add a qualification it does not draw out: organizing the base data itself, with no auxiliary structure (a sorted column, data clustered under a block index), shifts cost between read and update without adding space, and "computation and knowledge about the data" can lower two overheads at once.

## Assumptions

- **Overheads are ratios to base data, per operation.** "The overheads of an access method quantify the additional data accesses to support any operation, relative to the base data." Units are amounts of data read, written or stored, not time.
- **Uniform cost of access.** Reading any block costs the same; there is a "minimum access granularity" on every medium. Nothing in the definitions depends on what the data look like, only on how much is touched.
- **Toy model for the propositions.** "an array of integers", N ≫ 1 fixed-size elements, one per block, with a workload of "point queries, updates, inserts, and deletes". "The generality of these examples lies in their simplicity."
- **No workload weighting.** The overheads belong to the method. The paper says "the optimal design depends on a multitude of factors like hardware, workload, and user expectations", but no query mix, frequency or cost function enters the definitions or the conjecture.
- **Steady state.** The three overheads are per-operation costs of an existing structure. Building it is a separate column of Table 1, not a fourth corner.

## Key results

**The three overheads, as defined in §2.**

- **Read overhead (RO), "read amplification":** "the ratio between the total amount of data read including auxiliary and base data, divided by the amount of retrieved data." B+-tree example: total data accessed, tree traversal plus base data, over "the base data intended to be read".
- **Update overhead (UO), "write amplification":** "the ratio between the size of the physical updates performed for one logical update, divided by the size of the logical update." B+-tree example: updated size of base and auxiliary data over the size of the updated base data.
- **Memory overhead (MO), "space amplification":** "the ratio between the space utilized for auxiliary and base data, divided by the space utilized for base data." B+-tree example: "the overall size of the B+ -Tree by the base data size."
- Floor: "The theoretical minimum for each overhead is to have the ratio equal to 1.0, implying that the base data is always read and updated directly and no extra bit of memory is wasted."

**The hypothesis and the three extreme designs (§2).** Stated: "Hypothesis. An access method that is optimal with respect to one of the read, update, and memory overheads, cannot achieve the optimal value for both remaining overheads." Each proposition is a one-paragraph argument, not a proof.

- **Prop. 1, minimum read.** Store each value in the block whose ID equals the value ("the relation {1, 17} is stored in an array with 17 blocks"). Every read touches only useful data. Space is unbounded, since the largest value cannot be anticipated. Changing a value empties one block and fills another. "Prop. 1 min(RO) = 1.0 ⇒ UO = 2.0 and MO → ∞".
- **Prop. 2, minimum update.** Append every update to an ever-growing log. "any reorganization of the data to reduce RO would result in an increase of UO." "Prop. 2 min(UO) = 1.0 ⇒ RO → ∞ and MO → ∞".
- **Prop. 3, minimum memory.** No auxiliary data, base data a dense array, updates in place, every selection a scan. "Prop. 3 min(MO) = 1.0 ⇒ RO = N and UO = 1.0".

Read together, the propositions do not show a three-way conflict at the extremes. Prop. 3's design is optimal on both memory and update; only read suffers. Prop. 1's design keeps update bounded at 2.0; only memory blows up. So at the corners the hypothesis holds by one overhead each time, and the pairs in real tension are read against memory (Props. 1 and 3) and update against read (Prop. 2, and the sorted column below).

**The conjecture, two wordings.**

- §1: "designing access methods that set an upper bound for two of the RUM overheads, leads to a hard lower bound for the third overhead which cannot be further reduced."
- §3, the formal statement: "The RUM Conjecture. An access method that can set an upper bound for two out of the read, update, and memory overheads, also sets a lower bound for the third overhead." Glossed: "we can choose which two overheads to prioritize and optimize for, and pay the price by having the third overhead greater than a hard lower bound."
- Abstract: "optimizing in any two areas negatively impacts the third." Section heading: "Read, Update, Memory – Optimize Two at the Expense of the Third."
- As stated in §3 the conjecture does not say the forced bound exceeds 1.0 or how it grows with the other two bounds. Every overhead is bounded below by 1.0 already, so without that the statement is trivially true. The content the authors intend is in the hypothesis and the gloss, and that content is not formalized. The summary nonetheless says "we show through the RUM Conjecture that creating the ultimate access method is infeasible"; it is shown for the three toy extremes only.

**Where structures sit (Figure 1, Table 1).**

- Figure 1 corners: read-optimized (hash, B-tree, trie, skiplist), write-optimized differential structures (LSM, PBT, MaSM, PDT), space-optimized approximate indexes (sparse index, Bloom filter, bitmap). Middle: adaptive structures (cracking, merging). These labels were read from the figure image. A tunable method is "an area" rather than a point. Placement is qualitative.
- Table 1 gives asymptotic I/O costs, not the RUM ratios, for six organizations, with columns for bulk creation cost, index size, point query, range query of size m, and insert/update/delete. B+-tree: creation O(N/B·log_{MEM/B}(N/B)), size O(N/B), point O(log_B N), update O(log_B N). Perfect hash: creation O(N), point and update O(1), range O(N/B). ZoneMaps (best case, one partition touched): creation O(N/B), size O(N/P/B), every operation O(N/P/B). Levelled LSM: creation N/A, update O(T/B·log_T(N/B)). **Sorted column**: creation as B+-tree (a sort), size O(1), point O(log₂ N), update O(N/B/2). **Unsorted column**: creation O(1), size O(1), point O(N/B/2), update O(1).
- On the sorted column: "even without any additional secondary index, maintaining a sorted column allows for searching with logarithmic cost, with the downside of having linear update cost. Hence, even without an auxiliary data structure, adding structure to the data affects read and write behavior." By the paper's own MO definition a sorted column has MO = 1.0, so sorting the base data trades read against update alone.
- Two overheads lowered at once: block-based clustered indexing "reduces both read and memory overhead by storing only a few pointers to pages", because the data are "clustered on the index attribute"; and compressed bitmaps. "In essence, we use computation and knowledge about the data in order to reduce the RUM overheads." Compression "does not affect the fundamental nature of the RUM Conjecture." Computation is a fourth resource the triangle does not count.

**Adaptive and tunable methods (§§4–5).**

- Adaptive methods (cracking, adaptive merging, adaptive indexing) "balance the read performance versus the overhead of creating an index. The incoming queries dictate which part of the index should be fully populated and tuned. The index creation overhead is amortized over a period of time, and it gradually reduces the read overhead, while increasing the update overhead, and slowly increasing the memory overhead."
- Limits claimed: they "cannot cover the whole RUM spectrum as they are designed for a particular type of hardware and application", and cracking behaves "in a dynamic manner yet are not tuneable".
- Proposals, none built or measured: B+-trees with runtime-tuned height, node size and split rule; approximate tree indexes absorbing updates in quotient filters; "Morphing access methods" that add "structure to data gradually with incoming queries, and building supporting index structures when further data reorganization becomes infeasible"; update-friendly bitmaps; logs with probabilistic filters; merge-based methods that change the number of merge trees and merge frequency with the workload. The paper also allows that one method may not cover the triangle and that several, "covering the whole space in aggregate", may.

**Build and reorganization cost.**

- Table 1's caption: "When using an additional index we (i) spend time building it, (ii) allocate space for it, and (iii) pay the cost to maintain it." Only (ii) and (iii) are RUM overheads. Building is tabulated (footnote: "Bulk loading requires sorting"; external multi-way mergesort assumed) and is not in the conjecture.
- Reorganization appears as the reason for update cost: differential structures let updates "avoid the cost of reorganizing data" at the price of reads that must merge pending updates; and in an append log "any reorganization of the data to reduce RO would result in an increase of UO". Reorganization is charged to update, not given its own term, and nowhere is it scheduled (when to reorganize) or amortized against a forecast.

**Memory hierarchy.** The triangle holds at each level separately (Figure 2), and read and update overheads at level n can be cut by holding more at level n−1, at a higher MO there. Cache-oblivious methods are said to pay larger read constants and more pointers, and to be less tunable.

## Bearing on the record

**On [QUESTION-114](../questions.d/QUESTION-114.md): the RUM triangle is a vocabulary for the question's trade, not the joint cost model it lacks.**

- The record's "organizing ahead" splits into two of the paper's three trades. Auxiliary structure, paid in space, cuts reads (Prop. 1, B+-tree, hash): the record's "every further index is paid for in space". Organizing the base data itself cuts reads at the price of update (the sorted column, O(log N) reads against O(N) updates, MO = 1.0): the record's "upkeep". The question's title names both, and the paper confirms they are distinct trades. The paper shows that sorting without bins or labels costs no memory in its sense, only upkeep.
- What the question most needs, the one-time cost of organizing set against later savings ("paid once"), is not in the triangle. Build cost is a column of Table 1, and the conjecture is silent on it. The only amortization the paper mentions is adaptive indexing's, cited, not modelled. So on whether sorting is amortized search the paper adds nothing beyond Idreos et al. 2007 ([LIT-1090](../literature.d/LIT-1090.md)), which it cites and which measured the break-even.
- There is no workload in the model. The overheads are per-operation ratios of a method. A query mix enters only as prose ("depends on ... workload"). So the paper does not give Finkelstein et al. ([LIT-1084](../literature.d/LIT-1084.md)) or Chaudhuri and Narasayya ([LIT-1083](../literature.d/LIT-1083.md)) a missing term; it sits a level above them, naming the axes their cost functions weigh.
- The survey's description, "no access method is best at once on read cost, update cost and memory; a conjecture, not a proof", is right on both halves. Two narrowings: the formal wording only asserts some lower bound on the third overhead, which every design already has, so it says less than the survey's paraphrase; and the toy extremes show conflicts between particular pairs (read–memory, update–read), not a symmetric triangle, since the memory-minimal design is also update-minimal.

**The LEGO mapping holds in outline and breaks on the cost of looking.**

- Read = items examined per brick retrieved; update = work to put a new brick away; memory = bins, labels and floor space relative to the bricks. With that mapping the paper's extremes are recognisable. An unsorted pile is Prop. 3: MO = 1, UO = 1 (toss it on), RO = N. One labelled bin per kind is Prop. 1: a brick is found with no wasted looking, but most bins sit near empty and new kinds need new bins. A tray of new bricks left to sort later is Prop. 2's differential structure: putting away is free, and every search must also check the tray. Setting a found brick aside, as in [CASE-094](../cases.d/CASE-094.md), is the paper's adaptive middle: structure added by queries, read cost falling over time.
- [CLAIM-310](../claims.d/CLAIM-310.md)'s bin budget does not map cleanly onto MO. The claim's k bins constrain which partition is realized; in RUM terms a set of bins is clustering of the base data plus a small directory (the labels), much like the paper's block-based clustered index or ZoneMaps with partition size P, and the paper says that kind of design lowers read and memory together. So, by the paper's own account, the bin budget is not mainly a memory overhead. Its cost is in [CLAIM-310](../claims.d/CLAIM-310.md)'s k/2 term, the directory scanned to find a bin, which in the paper's units is read overhead on auxiliary data. The claim's k/2 + N/(2k) is an RO for one brick, and its minimum near k = √N is a read–memory balance of the kind the triangle describes. The paper gives no such formula.
- [CLAIM-310](../claims.d/CLAIM-310.md)'s query mix has no place in the model, which has no workload term. Nothing here supports or weakens its part 2 beyond the prose that the best design "depends on ... workload".
- [CLAIM-307](../claims.d/CLAIM-307.md)'s m/(c+1) is a read overhead, items examined per item wanted. The RUM definition supports counting it so. But RUM charges every item read the same. [CLAIM-310](../claims.d/CLAIM-310.md) part 3 and [CLAIM-307](../claims.d/CLAIM-307.md)'s brick that is buried but still detectable turn on the opposite: items that stand out are found almost without examining their neighbours. Perceptual pop-out has no counterpart in the model. In data systems the nearest thing is "computation and knowledge about the data" (filters, compression), which the paper treats as outside the triangle. For the record this means RO overstates search cost when the target pops out, and the triangle cannot express [CLAIM-307](../claims.d/CLAIM-307.md)'s point that a rare item may need no bin.
- Left out entirely: deadlines and time (all costs are amounts of data, per operation), workloads and their frequencies, build cost inside the trade, when to reorganize, perception, and any guarantee. For the timing questions Karlin et al. ([LIT-1096](../literature.d/LIT-1096.md)) and Sleator and Tarjan ([LIT-1093](../literature.d/LIT-1093.md)) stay the record's sources.

## Limitations

- A conjecture with no proof and, in its formal wording, no quantitative content. The supporting propositions concern extreme designs on a toy array and are argued in a paragraph each.
- Placement of structures on the triangle is qualitative. Table 1 gives asymptotic I/O complexities, not the RUM ratios it defines, so the two cannot be compared directly.
- No experiments, no measurements, no workload model, no cost of building inside the conjecture.
- Lists of proposed tunable methods are a programme, not results.

## Open questions

- What is the forced lower bound as a function of the other two bounds? A quantified version would turn the triangle into a cost model; the paper leaves it as future work.
- With a workload and a build cost added, does the triangle reduce to the steady-state index-selection model of Finkelstein et al., or does it add something? This is [QUESTION-114](../questions.d/QUESTION-114.md)'s question asked of this paper.
- For a collection searched by eye, what replaces uniform cost per item read? A pop-out term would let the triangle price [CLAIM-310](../claims.d/CLAIM-310.md) part 3 and [CLAIM-307](../claims.d/CLAIM-307.md).
