---
number: 893
status: Read
formerly:
- NOTE-tmp6n3s5
paper: LIT-1096
title: Karlin, Manasse, Rudolph & Sleator — Competitive snoopy caching
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full 2026-10-15 from a scan of the published Algorithmica article (Springer-Verlag
    copyright line on the first page, running heads, pages 79–119, "Received October
    28, 1986; revised May 30, 1987") that MIT course 6.896 (Spring 2004) posts among
    its reading handouts, at courses.csail.mit.edu/6.896/spring04/class/www/handouts/papers/snoopy-cache.pdf.
    It is the publisher's typeset version scanned for a course reading list, not
    an author-posted copy; the coordinator's brief names course pages as an allowed
    source, and the record should judge that on its own terms. No author or repository
    copy was found: Unpaywall and OpenAlex report the article closed with no repository
    full text, Semantic Scholar gives no open-access PDF, Sleator's CMU papers page
    (www.cs.cmu.edu/~sleator/papers/) and Karlin's UW page (homes.cs.washington.edu/~karlin/)
    do not list it, guessed paths on Sleator's page returned 404, and a scholar.archive.org
    search for the title returned no result. The FOCS 1986 version was not needed
    and not read. The scan is 21 sheets, the first page alone and the rest two pages
    to a sheet, rotated; it has no text layer. Every page was rendered at 300 dpi,
    rotated, split and OCR'd with tesseract, and every page was also read as an
    image, since the OCR does not carry the formulas. Read: Sections 1–10, Appendices
    A–D and the references; nothing skipped. The proofs of Theorems 4.1, 5.4, 6.1,
    8.1 and D.1 were followed case by case; the decentralized bus protocols of Appendices
    A and B were read for content, not checked. Formulas below were transcribed
    from the page images. Every quotation was checked by script against the OCR
    text, with whitespace normalised; four differ from it only where tesseract misread
    a letter ("teplicated", "tead", "¢-competitive", "Dus cycle") and were confirmed
    against the page images. A search of the OCR text for rent, rental, buy and
    ski found none. Sleator and Tarjan 1985 (LIT-1093, NOTE-903) is held
    and read; the follow-up by Karlin, Manasse, McGeoch and Owicki on randomized
    algorithms was located on the same course page but not read.
date: '2026-10-15'
summary: >-
  For a shared-bus multiprocessor whose caches can either keep a replicated block
  (and pay one bus cycle for every write to it) or drop it (and pay p to fetch it
  again if it is read), the paper gives counter-based on-line algorithms whose total
  bus cost on every request sequence is at most twice that of the best off-line
  algorithm, and proves that no deterministic on-line algorithm can guarantee better
  than 2. The rule is: drop a copy once the writes it has caused since it was last
  read have cost as much as refetching it. With a third option (reading or writing
  through without fetching) the lower bound rises to 3, and the algorithm given
  is 3-competitive ignoring writebacks, 4 counting them; with associative caches
  the bound becomes the paging ratio. The paper never names rent-or-buy or ski rental;
  its rent is upkeep paid on an idle copy, and its purchase is the refetch after
  dropping, the reverse orientation of building a bin. Costs are fixed constants,
  the guarantees are worst case only, and the authors call the practical significance
  "unclear".
---

# NOTE-893: Karlin, Manasse, Rudolph & Sleator — Competitive snoopy caching

## Contribution

Snoopy-cache multiprocessors must choose a block retention strategy. The
paper states the tradeoff: "if a block is replicated, then the system must pay
the cost of updating all copies following a write to that block; if a block is
dropped from a processor's cache, then the system must pay for the
processor's next request to read a variable in that block." The two standard
designs each fail badly on some sequence: exclusive-write by a factor of
(n − 1)p, pack-rat by an unbounded factor. The paper defines a family of
models (direct-mapped, associative, general, block and limited block snoopy
caching, and multibus networks), gives an on-line retention algorithm for
each, and proves each is within a constant factor of the off-line optimum on
every sequence, with lower bounds showing several constants are the best
possible. It defines the terms: an on-line algorithm "is c-competitive (or
simply competitive) if its cumulative cost on any sequence (plus a constant)
is within a factor of c of the cost of the optimal off-line algorithm on the
same sequence", and "If c is the smallest possible such constant for any
on-line algorithm, then the algorithm is said to be strongly c-competitive".
It credits Sleator and Tarjan for the method: "Sleator and Tarjan [ST] showed
that move-to-front is a competitive algorithm for maintaining a linear search
list." Counter-based schemes were not new ("Like the strategies of [RS2], our
algorithms keep counters"). What is new is the competitive analysis.

## Key insight

Switch state when what you have overpaid for staying equals the price of
switching. The paper's own statement: "The principle used to devise these
schemes is roughly the following: the change from a state A to a state A' is
made when the cost of making the change equals the extra cost incurred due to
being in state A instead of A'." Then neither the on-line algorithm's waiting
nor its switching can cost more than the off-line optimum has to pay on the
same stretch, so the total is within 2. The lower bound shows the balance is
forced: "if an on-line algorithm does not spend nearly equal amounts reading
and writing, then an off-line algorithm can beat it by more than a factor of
2." The authors "were guided by the constraint that the cost of reading and
writing must be balanced."

## Assumptions

- **Costs are bus cycles, fixed and known.** Fetching or writing back a block
  costs p, "the number of bus cycles needed to read a block";
  a broadcast update of one variable costs 1; dropping a block, a local update
  and a supply from one's own cache cost 0. Nothing else is counted: not
  processor time, not cache contention, not latency.
- **Requests are a sequence**, READ_i(v) and WRITE_i(v), served one at a time;
  "the bus serializes all communication." Bus arbitration is assumed solved.
- **Coherence is never relaxed.** A replicated block must be updated or
  invalidated on every write; a stale read is not an option with a price, it
  is excluded.
- **On-line means local control**: after a request by processor i, no other
  cache acts until the request completes or cache i takes a costly action.
- **The comparison is worst case over sequences**, against an off-line
  algorithm that sees the whole sequence. No probabilistic model of requests.
  The authors' reason: "Without prior knowledge of the structure of the
  sequence of operations, a scheme that is competitive is more attractive than
  one that is not."
- **Deterministic algorithms only.** All lower bounds are for deterministic
  on-line algorithms.
- Constants k in the theorems depend only on the initial cache states and
  vanish when caches start empty (or as stated per theorem).

## Key results

Notation: p is the cost of moving a block; C_A(σ) is algorithm A's cost on
sequence σ; opt is the off-line optimum.

- **Theorem 3.1 (lower bound 2).** In any model without Supplythrough and
  Updatethrough, with at least two caches, for any on-line algorithm A there is
  an infinite sequence σ with C_A(σ(n)) ≥ n and C_A(σ(n)) ≥ 2·C_opt(σ(n)) for
  infinitely many n, and C_A(σ(n)) + p ≥ 2·C_opt(σ(n)) for all n. The
  adversary uses two caches and one block replicated in both: it issues
  WRITE_1(B) while cache 2 still holds B, and READ_2(B) as soon as A has
  dropped it. Each write costs A 1 and each read after the first costs p. The
  off-line H looks ahead p requests: "After each read, H chooses to make B
  unique to cache 1 if and only if the read is followed by at least p
  consecutive writes." Between two reads with k writes, A pays k + p and H pays
  min(k, p), and 2·min(k, p) ≤ k + p. This is the rent-or-buy argument,
  complete, inside a cache-coherence proof.
- **Theorem 3.2 (no best on-line algorithm).** For any on-line A there is an
  on-line G with C_G(τ) ≤ C_A(τ) + 2p for every τ, yet for every N some σ has
  C_A(σ) ≥ N and 2·C_G(σ) ≤ C_A(σ). "Here we show in a strong sense that there
  is no such thing."
- **Theorem 3.3 (lower bound 3 with a third option).** If Supplythrough and
  Updatethrough are allowed (serve a request over the bus without taking the
  block), then for any on-line A, C_A(σ(n)) ≥ 3·C_opt(σ(n)) for infinitely many
  n.
- **Theorem 4.1 (direct-mapped, dsc).** For any σ and any on-line or off-line
  A, C_dsc(σ) ≤ 2·C_A(σ) + k: dsc is strongly 2-competitive. The algorithm keeps
  a count w[i, B] in 0..p for each cached block; a write to a replicated block
  decrements the count in one other cache holding it ("Each other cache
  containing the block is partially guilty of causing this bus cycle"), and
  "When the counter reaches zero the block is dropped." A fetch sets the count
  to p; a read may raise it to anything in w..p, and which other cache is
  charged is free: "amortized analysis of the algorithm is insensitive to these
  choices, so other criteria must be used to make them." Proof by a potential
  function, case by case. Theorem 4.2 splits the bound: fetch costs of dsc are
  at most A's fetch plus update costs, and dsc's update plus writeback costs
  are at most the same.
- **Theorems 5.1–5.4 (associative caches = paging + snoopy caching).**
  Theorem 5.1 is Sleator and Tarjan's paging lower bound, F_A(σ) ≥
  (n_A/(n_A − n_min + 1))·F_min(σ). Theorem 5.2 (proofs in Appendix C, new
  potential-function proofs) shows FWF, FIFO and LRU meet it up to an additive
  k. Theorem 5.3: any on-line associative snoopy algorithm with caches of size
  n_A against opt with n_opt has arbitrarily long σ with C_A(σ) ≥
  max(n_A/(n_A − n_opt + 1), 2)·C_opt(σ). Theorem 5.4: algorithm scwf (FIFO for
  room, dsc counters for writes) has FBC_scwf ≤ (n_scwf/(n_scwf − n_A + 1))·
  (FBC_A + UC_A) + k1 and UC_scwf ≤ FBC_A + UC_A + k2; its corollary makes it
  (1 + 2·[n_scwf/(n_scwf − n_A + 1)])-competitive.
- **Theorem 6.1 (general snoopy caching, gsc).** With the read-through and
  write-through options, C'_gsc(σ) ≤ 3·C'_A(σ) + k counting all costs except
  writebacks, so gsc is strongly 3-competitive by Theorem 3.3; counting
  writebacks (WBC_gsc ≤ ⅓·C'_gsc), gsc is 4-competitive. Whether it is strongly
  competitive with writebacks counted is left open.
- **Theorems 7.1 and 8.1 (block and limited block snoopy caching).** Caches
  that can grab a block broadcast on the bus; algorithms bsc and lbsc make a
  block unique only after p uninterrupted writes by one processor. Both are
  strongly 2-competitive: C ≤ 2·C_A + k.
- **Theorem 9.1 and Corollary 9.1 (multibus).** With gateways joining block
  snoopy caching buses in a tree per block, there is an on-line algorithm whose
  cost on each bus is at most twice that of any algorithm using the same
  trees, including on a d-dimensional n-cube of buses.
- **Remarks (Section 10).** "A problem very closely related to those described
  in this paper is that of deciding where to keep files in a distributed file
  system." "We have not yet transformed our skill into a general theory of
  competitiveness." And: "The practical significance of these results is
  unclear." The only evidence they cite that competitive analysis predicts
  practice better than average-case analysis is Bentley and McGeoch's
  move-to-front measurements, attributed to locality of reference.

## Where the rent-or-buy structure is

The record's LIT entry describes the paper as the origin of "when to stop
paying per use and pay once". That is right in substance and wrong in two
details of orientation.

- **The two prices.** A cache j holding a copy of a block that another
  processor i keeps writing pays, through the bus, 1 per write to keep its copy
  current. That is the rent. Dropping the copy costs nothing now; the price
  comes later, p to fetch the block again if j reads it. That is the purchase.
  The paper says so in its own terms: "Voluntarily dropping a block is
  advantageous only if that block becomes unique to a single cache."
- **The rule.** dsc's counter starts at p when j fetches the block and falls by
  one per write charged to j; at zero, j drops the block. So j drops the copy
  exactly when the rent paid since its last use equals the purchase price. The
  lower-bound adversary (Theorem 3.1) then reads at once, forcing the purchase:
  the pattern of every ski-rental lower bound.
- **What is rented and what is bought.** The rent here is upkeep on an idle
  copy, and the purchase is reacquiring what was let go. The decision is when
  to stop maintaining, not when to build. The abstract structure is symmetric
  (a cost per period of staying in one state, a fixed cost of switching), and
  the paper states it in that symmetric form (the state-change principle
  quoted above). But a reader who wants "when does a new bin pay?" is applying
  the principle in the mirror direction from the paper's instance.
- **The name.** The paper never says rent, buy, ski or rental (checked by
  search of the OCR text and by reading). It contains the argument and the
  2-competitive bound with its matching lower bound, applied to cache blocks.
  The record should cite it as the first competitive analysis of the
  rent-or-buy decision, not as the source of the name.

## The principle, stated precisely

Two states, S (cheap to enter, costs r per request of a certain kind while in
it) and S′ (costs nothing per such request, but costs P once to switch into).
Requests arrive one at a time; their number is unknown and may be chosen by an
adversary. On-line rule: stay in S until the requests seen since the last
reset have cost P in total, then switch. Then on every sequence the on-line
cost is at most 2 times the off-line optimum plus a constant (Theorem 4.1,
C ≤ 2·C_A + k), and no deterministic on-line rule guarantees a factor below 2
(Theorem 3.1). In the paper r = 1, P = p, and a reset is a read by the
dropping cache. Two conditions matter and are easy to lose:

- **Exactly two options.** With a third (Supplythrough: serve a read without
  taking the block), the deterministic lower bound rises to 3 (Theorem 3.3),
  and the algorithm given costs 3 or 4 times the optimum. More choices cost
  more competitiveness.
- **Fixed, known prices.** r and P are constants the algorithm knows. The
  bound is about uncertainty in the sequence only, not in the costs.

## Bearing on the record

**On [QUESTION-114](../questions.d/QUESTION-114.md).** The attribution holds, with the corrections above:
the paper is the competitive analysis of a rent-or-buy decision, unnamed,
oriented toward dropping a maintained copy; its general principle is stated
for any state change. It is not a cost model of indexing or sorting; it says
nothing about which partition to build, and has no space budget beyond cache
size in Section 5. With Sleator and Tarjan it gives the question two
worst-case results that fit together: reorganizing at the moment of use, when
that is free, is within 2 of the best (move-to-front); and a costly one-time
reorganization should be made when the extra cost of not having made it
reaches its price, also within 2. Neither needs a model of future use, which
is what makes them usable where expected reuse is unknown.

**(a) The LEGO bin ([CASE-094](../cases.d/CASE-094.md), [CLAIM-307](../claims.d/CLAIM-307.md)).** Mapped in the mirror
direction: the rent is the extra search each time the brick is wanted in the
mixed bin (on [CLAIM-307](../claims.d/CLAIM-307.md)'s model about m/(c+1) items, against a near-zero
search in its own bin); the purchase is the cost of making the bin. Rule: keep
searching the mixed bin until the extra search spent on this kind adds up to
the cost of a bin, then make one. That is within 2 of a builder who knew how
often the brick would be wanted. Three limits:

- The rule triggers on accumulated cost of use, not on copies or evidence. So
  it agrees with [CLAIM-307](../claims.d/CLAIM-307.md) that "very few of but use often" is the cell
  where a bin pays, and adds that use, observed as it happens, is enough to
  decide it with a worst-case guarantee. Copy count enters only through the
  rent per use: few copies means a high rent per search, so the threshold is
  reached after fewer searches.
- [CASE-094](../cases.d/CASE-094.md)'s practice, setting a brick aside when it is found, makes the
  purchase nearly free (the search is already paid). When P is about 0 the rule
  says switch at once, which is the case's practice; the 2-competitive bound
  matters only when making the bin costs real work, such as re-sorting a bin.
- The rent per search is not a constant: it falls as copies are added and
  rises as the bin grows. The paper's bound assumes fixed prices; with drifting
  prices the cumulative-cost rule still makes sense but this paper does not
  prove its ratio. And a builder's choice is rarely binary (search, bin, bin by
  colour, set aside on finding): Theorem 3.3 is a warning that each further
  option raises the best guaranteed ratio.

**(b) [CLAIM-303](../claims.d/CLAIM-303.md).** The claim's condition, file when n > F/(c_r − c_a − u),
needs the number of uses n in advance. Rent-or-buy gives the worst-case answer
without it: file once the reconstructions already done have cost F more than
reading a filed copy would have, that is after about F/(c_r − c_a) uses; on
every sequence this costs at most twice what filing with hindsight would, and,
by the argument of Theorem 3.1 transposed, no deterministic rule guarantees
better. The transposition is this note's, not the paper's. Consequences for the claim:

- **It narrows "recurrence is evidence of reuse, not the criterion".** Under
  worst-case evaluation, counting recurrences, weighted by what each
  reconstruction cost, is the criterion, and is optimal among deterministic
  rules. The claim's position holds only where there is a distribution over
  reuse to exploit; this paper does not cover that case.
- **It locates the second-occurrence rule ([ADR-032](../decisions.d/ADR-032.md)).** Filing at the second
  occurrence is the rent-or-buy rule exactly when filing costs about one
  reconstruction. If filing costs many reconstructions, the rule files too
  early, and an item never used again costs F against about 2c_r, a ratio
  that grows without bound as F/c_r grows; if filing is much cheaper than a reconstruction, waiting for
  the second occurrence wastes one reconstruction. This makes the claim's
  "can fail in both directions" precise.
- **It also gives the retirement rule.** The paper's own instance is the
  reverse decision: keep a copy and pay to keep it current, or drop it and pay
  to reacquire it. For a filed argument whose dependencies keep changing, the
  same reasoning says retire it (by status) once its upkeep since it was last
  used has cost as much as reconstructing it.
- **What it does not cover.** A11's staleness term, reusing an obsolete
  argument, has no counterpart: coherence is enforced at a price, never
  risked. The threshold also needs F and c_r known, and the
  record's costs are estimates.

**(c) [QUESTION-095](../questions.d/QUESTION-095.md).** Snoopy caching is a model of copies left where they are
cheap to read, kept current at a price per change, and dropped when that price
outruns the cost of fetching again. So it prices the upkeep term that Sleator
and Tarjan's paging model lacks, and gives a worst-case rule for when keeping a
result readable stops paying. It does not price computation: the copies are
copies of stored data, so nothing in it is a precomputed answer, and it has no
phases, so it does not capture the cockpit's move of work to a low-load period.
Its staleness is handled by forbidding stale reads, which is the opposite of the
reused-inference case, where staleness is the price accepted.

**Relation to Sleator and Tarjan 1985 ([LIT-1093](../literature.d/LIT-1093.md)).** This paper takes its
method from that one, quotes its paging lower bound as Theorem 5.1, adds new
potential-function proofs that FIFO, FWF and LRU meet it (Appendix C), and
combines paging with the snoopy counters for associative caches (Theorems
5.3, 5.4). It names the property that Sleator and Tarjan proved for
move-to-front "competitive". The two papers' 2s have different sources:
move-to-front's comes from an amortized comparison of list positions; dsc's
from balancing a per-use cost against a one-time cost.
