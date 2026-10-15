---
status: Read
paper: LIT-tmpt85t0
title: Sleator & Tarjan — Amortized efficiency of list update and paging rules
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the copy on Sleator's own CMU page (https://www.cs.cmu.edu/~sleator/papers/amortized-efficiency.pdf,
    7 pp., 1,440,033 bytes). It is a scan of the published article, not a preprint:
    an Acrobat 5.0 Paper Capture file of 2002 whose pages carry the CACM running
    heads, the printed page numbers 202–208 (the footer of page 206 is misread as
    208 by the OCR), the 1985 ACM copyright line with code 0001-0782/85/0200-0202,
    the received/revised/accepted dates and ACM's copying notice. Crossref gives
    pages 202–208, February 1985. The text matches the publisher's version of record;
    OpenAlex and Unpaywall list the ACM Digital Library PDF (dl.acm.org/doi/pdf/10.1145/2786.2793)
    as open access (bronze, publishedVersion), but the ACM site returned 403 to
    a direct request from this environment, so the two were not compared page by
    page. Text extracted with pdftotext (plain and -layout). The OCR drops or garbles
    the displayed formulas (the statements of Theorems 5 and 6 are missing entirely,
    and ≤ comes out as 5), so the statements of Theorems 1, 2, 4, 5 and 6, the potential
    of Theorem 4 and Figure 1 were checked against page images rendered at 110 dpi.
    Read: all five sections, every theorem, proof, counterexample and remark, the
    figures and the reference list. Nothing skipped. Bentley and McGeoch (1982),
    Belady (1966) and Franaszek and Wagner (1974), whose results the paper reports,
    were not read, so what it says of them is its account. Every quotation of the
    paper below was checked against the extracted text by script, with whitespace
    normalised; two differ from the OCR only by its errors ("L e t A" for "Let A"
    in Theorem 3, "(1- l/c)n" for "(1 − 1/c)n" in Section 5) and were checked against
    the page images. Quotations of the record (QUESTION-tmplg07t, the LIT summary)
    were checked against those files.
date: '2026-10-15'
summary: >-
  For a list searched sequentially from the front, where reaching the i-th item
  costs i, moving each accessed item to the front costs at most twice what any other
  rule costs on the same sequence, including rules that know the whole sequence
  in advance (four times, counting move-to-front's own moves), with no probabilistic
  assumption. A fixed list sorted by access frequency, and the transpose and frequency-count
  rules, are not within any constant factor of that. Rearranging ahead of need never
  pays in this model (Theorem 3). For paging, where only a small fast memory is
  cheap, no rule that cannot see the future can do better in the worst case than
  n/(n − n_MIN + 1) times the offline optimum MIN, and LRU and FIFO attain that
  bound up to an additive n_MIN; with equal memories the ratio is the memory size.
  The model is a single linear list (or a two-level memory) with uniform items and
  access cost depending only on position; it says nothing about partitions, bins
  or search that is not a scan.
---

# NOTE-tmpy8giy: Sleator & Tarjan — Amortized efficiency of list update and paging rules

## Contribution

Earlier analyses of self-organizing lists were average-case: accesses
independent with fixed probabilities, where transpose was proved at least
as good as move-to-front and the optimum is the list sorted by decreasing
probability. Bentley and McGeoch had compared rules on arbitrary sequences,
but only against the best *static* list. This paper compares move-to-front
(MF) on an arbitrary sequence against *every* algorithm in a stated class,
including ones that rearrange the list as they go and know the future, and
does the same for paging against Belady's offline MIN. It is the paper that
started what was later called competitive analysis; the word "competitive"
is not used in that sense here (it appears once, for Bentley and McGeoch's
empirical finding that "move-to-front is competitive with frequency
count").

## Key insight

Charge each operation its cost plus the change in a potential that measures
how far MF's list is from the rival's: the number of inversions between the
two lists. When MF moves an accessed item to the front, the items it passes
that the rival also has in front of that item create inversions, and those
it passes that the rival has behind it destroy them, which pays for MF's
extra search. So MF's amortized cost per access is at most twice the
rival's, whatever the sequence. The amortization is over a worst-case
sequence: "By amortization we mean averaging the running time of an
algorithm over a worst-case sequence of executions." No probabilities enter.

## Assumptions

- **The dictionary problem on an unsorted linear list** (Section 2): access,
  insert and delete, with the item found by scanning from the front.
  "Accessing or deleting the ith item in the list costs i. Inserting a new
  item costs i + 1, where i is the size of the list before the insertion."
- **Free and paid exchanges.** "Immediately after an access or insertion of
  an item i, we allow i to be moved at no cost to any position closer to the
  front of the list; we call the exchanges used for this purpose free. Any
  other exchange, called a paid exchange, costs 1." Paid exchanges are of
  adjacent items.
- **The class compared.** "We shall only consider algorithms that solve the
  dictionary problem in the manner described above." Any algorithm A in
  that class, online or offline, with any policy of free and paid
  exchanges. So the rival is the optimal *dynamic* offline algorithm in the
  class, not the best fixed arrangement. Data structures other than a
  sequentially scanned list (hash tables, trees, bins) are outside it.
- **Initial state.** Theorems 1, 2 and 4 start from the empty set; the
  stated generalizations add a term for differing initial lists.
- **Generalized cost (Section 3).** Access to position i costs f(i), f
  nondecreasing; a paid exchange of positions i and i+1 costs
  Δf(i) = f(i+1) − f(i). No deletions. Theorem 4 needs f convex in the
  paper's sense, Δf(i) ≥ Δf(i+1); as printed this is nonincreasing
  increments, which includes f(i) = i and concave-shaped costs such as log i.
- **Paging (Section 4).** Two-level memory, uniform pages, n pages of fast
  memory; a hit costs 0, a miss costs one page fault, and the accessed page
  must be brought into fast memory. A and MIN may have different fast-memory
  sizes, n_A ≥ n_MIN.
- **No cost for maintaining bookkeeping** (counts, timestamps) is in the
  model; the paper remarks only that frequency counts cost time and space.

## Key results

- **Theorem 1.** "For any Algorithm A and any sequence of operations s
  starting with the empty set," C_MF(s) ≤ 2C_A(s) + X_A(s) − F_A(s) − m
  (formula transcribed from the page image).
  C is cost excluding paid exchanges, X the number of paid exchanges, F the
  number of free exchanges, m the number of operations. With different
  initial lists add I, the initial number of inversions, at most n(n−1)/2.
  Counting MF's own moves (gross cost T = C + F + X), T_MF(s) ≤ 4T_A(s) −
  2X_A(s) − 6F_A(s) − 2m. The conclusion states the constants: "The constant
  factor is 2 if we do not count the updating cost incurred by
  move-to-front and 4 if we do."
- **What it means, in the paper's words.** "Theorem 1 states that on any
  sequence of operations, move-to-front is to within a constant factor as
  efficient as any algorithm, including algorithms that base their behavior
  on advance knowledge of the entire sequence of operations." And: "What
  this means is that knowledge of future operations cannot significantly
  help to reduce the cost of current operations." Theorem 1 implies the
  earlier average-case result that MF is within 2 of the best fixed order.
- **A measure of a sequence's difficulty.** Define the complexity of an
  access to i as 1 plus the number of distinct items used since the last
  operation on i. "With this definition the complexity of a sequence is
  exactly the cost of move-to-front on the sequence and is within a factor
  of 2 of the cost of an optimum algorithm."
- **Theorem 2.** A rule MF(d), d ≥ 1, that moves an item at position k at
  least k/d − 1 places forward satisfies C_MF(d)(s) ≤ d(2C_A(s) + X_A(s) −
  F_A(s) − m). Moving partway to the front keeps a constant, d times worse.
- **Negative results.** Transpose and frequency count are not within any
  constant factor. For frequency count the counterexample gives cost
  Ω(mn) against MF's m + O(n²). "The same example with the insertions
  omitted shows that using a static list ordered by decreasing access
  frequency is not within a constant factor of optimal." A fixed sort by
  frequency, chosen with hindsight, can be worse than MF by a factor that
  grows with n.
- **Theorem 3 (rearranging ahead does not pay).** "Let A be an algorithm for
  a sequence s of insertions and accesses. Then there is another algorithm
  for s that is no more expensive than A and does no paid exchanges." It
  holds for any nondecreasing f, with paid exchanges charged Δf(i), and
  does not need an empty initial set. The proof postpones each paid
  exchange past the next access, where it either becomes free or costs
  nothing extra. In paging this is the known fact that premature paging
  cannot reduce faults.
- **Theorem 4 (convex cost).** If f is convex and the set starts empty,
  C_MF(s) ≤ 2C_A(s) + X_A(s) − mf(1). Potential Σ_i (f(i + x_i) − f(i)),
  x_i the number of items after i in A's list that precede it in MF's.
  Deletions are left open unless charged f(i) in a list of size i.
- **Theorem 5 (lower bound for every online pager).** "Let A be any on-line
  algorithm. Then there ure arbitrarily long sequences s such that"
  F_A(s) ≥ (n_A/(n_A − n_MIN + 1))F_MIN(s) ("ure" is the OCR's; the page
  reads "are"; formula from the page image). If n_A < n_MIN, A can be made
  to fault on every access while MIN never faults.
- **Theorem 6 (LRU attains it).** For any sequence s,
  F_LRU(s) ≤ (n_LRU/(n_LRU − n_MIN + 1))F_MIN(s) + n_MIN. "Essentially the
  same argument shows that Theorem 6 holds for FIFO." LIFO and LFU have no
  such bound. With equal memories (n_A = n_MIN = n) the ratio is n, the
  size of fast memory: "any on-line paging algorithm makes a number of
  faults in the worst case that exceeds the minimum by a factor equal to the
  size of fast memory." With more memory than the optimum: "for any
  constant factor c > 1, LRU and FIFO with fast memory size n make at most
  c times as many faults as the optimum algorithm with fast memory size
  (1 − 1/c)n."
- **Slips in the printed text.** The proof of Theorem 1 says the potential
  is used again "in the proof of Theorem 3"; it is used in Theorem 4. The
  remark after Theorem 6 refers to "the lower bound in Theorem 4"; the lower
  bound is Theorem 5. Neither affects a result.

## Bearing on the record

**On [QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md): the citation's gloss is right in spirit and wrong in
two particulars.**

- The gloss "putting the brick just used on top" is a fair picture of move-to-front if
  the collection is one pile searched from the top, one brick at a time,
  with cost equal to depth, and if putting the found brick on top costs
  nothing. Under those terms Theorem 1 holds for the pile.
- "within a constant of the best arrangement" understates it and misnames
  it. The rival is not an arrangement but the best *algorithm* in the
  class, one that may rearrange after every access and knows the whole
  future. The constant is 2, or 4 if MF's own moves are counted. Against
  the best fixed arrangement, which is what "arrangement" suggests and what
  the LIT entry's summary says ("the best arrangement chosen with
  hindsight"), the 2 was already Bentley and McGeoch's; this paper's claim
  is the stronger one.
- **It speaks against sorting once, in its model.** A static list sorted by
  frequency is not within any constant factor of optimal on sequences with
  locality, and Theorem 3 says paid rearrangement ahead of need never beats
  rearranging the item you have just found. So within a single scanned list
  the answer to whether sorting a collection is amortized search is that sorting ahead does
  not pay, and the cheap, lazy practice of [CASE-tmpd5exw](../cases.d/CASE-tmpd5exw.md) (move the item
  when it is found) is provably as good as any. That is a sharper finding
  than the question's framing, which treats sorting as a one-off payment
  against later retrievals.
- **Bins are outside the model.** Sorting LEGO into bins replaces a scan of
  one list by a choice of bin and a scan within it. That is a different
  cost function, not a position in one list, and the comparison class here
  excludes it. Nothing in the paper says when bins beat a pile, or what
  [CLAIM-tmpjmtw0](../claims.d/CLAIM-tmpjmtw0.md)'s one-partition constraint costs. Theorem 4 extends the
  result to any position cost with nonincreasing increments, which could
  model a pile where deep search is cheaper per item, but still one list.
- **Online, with nothing assumed about the future.** MF needs no
  prediction and no counts. For a builder who cannot predict the next
  brick, the result says prediction would buy at most a factor of 2 in a
  pile. The paging part says the opposite where the cheap store is small: if
  only n bricks can be kept at hand (a tray), not knowing the future can
  cost a factor of n against a planner with the same tray, and only a
  larger tray than the planner's brings it back to a constant (LRU with
  tray 2n is within 2 of a planner with tray n, up to an additive term).
- Costs not modelled: the physical cost of moving items, uniform items,
  insertions of new kinds (modelled only as appending to the end), and any
  cue that lets search skip the scan. The model has no staleness: an item's
  identity never changes.

**On [QUESTION-095](../questions.d/QUESTION-095.md): paging is the caching half, priced exactly, and nothing
more.**

- Section 4 prices what [QUESTION-095](../questions.d/QUESTION-095.md) calls leaving a result where it can be
  read cheaply, as keeping pages in a fast memory of fixed size. The cost
  counted is retrieval misses only. The bound gives the price of not knowing
  future requests (n/(n − n_MIN + 1)) and says the simplest recency rule,
  LRU, is worst-case optimal among online rules up to an additive term.
- It does not price the computation of what is cached, storage beyond a
  fixed capacity, upkeep, or staleness, and caching is forced (demand
  paging), not chosen. So it supplies one term of the joint cost model the
  question asks for, not the model. Theorem 3's "premature paging cannot
  reduce the number of page faults" is the paging form of the point that
  precomputing placement ahead of a request does not pay here, which is the
  opposite of the speed-bug case, where work is done early because later
  work is dearer. In this model nothing is dearer later.
