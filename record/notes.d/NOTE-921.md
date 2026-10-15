---
number: 921
status: Read
formerly:
- NOTE-tmpxpujb
paper: LIT-1116
title: 'Halevy — Answering queries using views: a survey'
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full from the publisher's typeset PDF (The VLDB Journal 10: 270–294
    (2001), DOI 10.1007/s007780100054, 25 pp., Springer-Verlag 2001; the journal
    header and page range are printed on the first page), hosted as a reading for
    the Columbia University Ph.D. candidacy exam in database systems (www.cs.columbia.edu/~gravano/Qual/Papers/halevy01.pdf,
    linked from the exam's reading-list page www.cs.columbia.edu/~gravano/Qual/),
    fetched 2026-10-15. It is a course-hosted copy of the published article. Also
    fetched, not read in full: the author's preprint (42 pp., by "Alon Y. Levy",
    University of Washington) on the Waterloo CS 740 course page (cs.uwaterloo.ca/~david/cs740/answering-queries-using-views.pdf),
    an earlier version whose introduction lacks the published sentence on "the maximal
    set of tuples". Unpaywall and OpenAlex report the article closed; Springer's
    PDF link returned an HTML page; the UW CSE 544 course copy (courses.cs.washington.edu/courses/cse544/11wi/papers/view-survey.pdf)
    is behind a UW login; the Oregon State course copy returned 404; the UPenn CIS
    650 file (seas.upenn.edu/~zives/03s/cis650/aquv.pdf) is lecture slides, not
    the paper; homes.cs.washington.edu/~alon/ is an empty directory. Text extracted
    with pdftotext; the extraction loses ⊑ and ≠, so Definition 1 and the open-world
    certain-answers sentence on p. 287 were read from page images. Read: §§1–9,
    every example, Tables 1–2, Figs. 3–5, footnotes. The reference list (153 entries)
    was scanned for the works cited in §7, not read entry by entry. The survey reports
    results proved elsewhere (Abiteboul and Duschka 1998; Duschka, Genesereth and
    Levy 2000; Grahne and Mendelzon 1999; Rajaraman, Sagiv and Ullman 1995) that
    were not read here, so those results are stated as this survey states them.
    Every quotation below was checked by script against the extracted text, whitespace,
    Unicode ligatures and line-end hyphenation normalised.
date: '2026-10-15'
summary: >-
  A survey that separates two problems of answering queries from stored views: finding
  an equivalent rewriting, which query optimization needs, and finding a maximally-contained
  rewriting or all certain answers, which data integration needs when sources are
  incomplete. Its theoretical findings, mostly reported from other papers: an equivalent
  conjunctive rewriting exists only if one exists no longer than the query, so finding
  one is NP-complete in the size of the query and view definitions, and checking
  a candidate is itself NP-complete; the inverse-rules algorithm builds the maximally-contained
  rewriting, as a possibly recursive datalog program, in time polynomial in the
  query and views; and finding all certain answers is polynomial in the size of
  the stored data in many open-world cases, but co-NP-hard in that size under the
  closed-world assumption even for conjunctive views and queries, or open-world
  with union in the views or ≠ in the query. Choosing which views to store is left
  as the next problem; cost-based choice among rewritings is described for practical
  optimizers, without guarantees.
---

# NOTE-921: Halevy — Answering queries using views: a survey

## Contribution

The survey gathers the work on using precomputed views to answer queries
into one framework, organized by a taxonomy (Fig. 3). The main split is by
output. Query optimization and physical data independence need an
equivalent rewriting turned into a cheapest execution plan, so the
reasoning is logical and cost-based, with views assumed complete and few.
Data integration needs a query over the sources that is equivalent to the
query or, more often, maximally contained in it, with many views that may
be incomplete. A further question, finding all answers derivable from the
view extensions (the certain answers), is distinct from finding a
rewriting and can be harder. The survey covers System-R style and
transformational optimizers (§5), the bucket, inverse-rules and MiniCon
algorithms (§6), the theory of completeness and complexity (§7), and
extensions to OQL, access patterns, semi-structured data and description
logics (§8).

## Key insight

Reuse of stored results has three levels, each with its own cost. Is a
stored view usable at all for a query? Can the query be rewritten exactly
from the views, or only partly? And given the stored contents, which
answers are certain? The first two are reasoning over the definitions and
cost a search in the size of the query and views; the third is reasoning
over the stored data and can cost a search in its size. "Hence, the
challenge is not only to detect when a view is logically usable for
answering a query, but also to make a judicious cost-based decision on
when to use the available views."

## Assumptions

- **Mostly select-project-join (conjunctive) queries and views** under set
  semantics, with arithmetic comparisons as a variant, datalog for the
  data-integration algorithms, and extensions surveyed in §5.3 and §8.
- **Definitions are given.** Every view comes with a definition over the
  same schema as the query. That is what makes usability decidable.
- **Two readings of the stored contents.** Closed world: each view's
  extension is exactly its definition applied to the database (the case
  for materialized views in optimization). Open world: an extension may
  miss tuples (the case for autonomous sources). Definition 4 defines
  certain answers under each.
- **Maximal containment is relative to a rewriting language** (Definition
  3). A maximally-contained rewriting in one language may miss certain
  answers that a more expressive language would get.
- **Not covered**, as the survey says: incremental maintenance of views,
  selection of views to materialize, automated index selection.

## Key results

As reported in the survey; sources in brackets.

- **When a view is usable (§4).** For a select-project-join view to be part
  of an equivalent rewriting, there must be a mapping from its tables to
  the query's (many-to-one under set semantics, one-to-one under bag
  semantics), it must apply the query's predicates or weaker ones on the
  mapped attributes, and it must not project out attributes the query
  still needs. A view with a stronger predicate can serve only a contained
  rewriting.
- **Size bound and NP (§7.1) [LMSS95].** Without comparison predicates, if
  the query has n subgoals, an equivalent conjunctive rewriting exists only
  if one with at most n subgoals exists. "An immediate corollary of the
  bound on the size of the rewriting is that the problem of finding an
  equivalent rewriting of a query using a set of views is in NP, because it
  suffices to guess a rewriting and check its correctness." Footnote 7:
  "Note that checking the correctness of a rewriting is NP-complete;
  however, the guess of a rewriting can be extended to a guess for
  containment mappings showing the equivalence of the rewriting and of the
  query." Hardness has two independent reasons, the ways to map one view
  into the query and the ways to combine the mappings of several views.
- **Access patterns (§8.2) [RSU95].** With binding-pattern limits the bound
  becomes n + v (v the query's variables) and equivalent rewriting stays
  NP-complete. For maximally-contained rewritings there may be no bound on
  length; a recursive datalog rewriting then suffices [DL97].
- **Bucket algorithm (§6.2).** Checking whether a view belongs in a
  subgoal's bucket is polynomial when predicates are arithmetic
  comparisons. The containment test on each candidate is Π2p-complete,
  "though only in the size of the query and the view definition, and hence
  quite efficient in practice". Without comparisons in the query it returns
  the maximally-contained union of conjunctive queries.
- **Inverse rules (§6.3) [DG97a, DGL00].** One Skolemized rule per view
  subgoal; with the query, they form a datalog program that is the
  maximally-contained rewriting, even for recursive queries. "Furthermore,
  the algorithm produces the maximally-contained rewriting in time that is
  polynomial in the size of the query and the views. Note that the
  algorithm does not tell us whether the maximally-contained rewriting is
  equivalent to the original query, which would contradict the fact that
  the problem of finding an equivalent rewriting is NP-complete [LMSS95]
  (see Sect. 7)." Evaluating the rules recomputes the base relations and
  loses the joins the views had already done, unless unfolded.
- **MiniCon (§6.4) [PL00].** Builds per-view descriptions of which query
  subgoals a view must cover together, and in experiments outperforms
  inverse rules, which outperform the bucket algorithm, scaling to hundreds
  of views of common query shapes. No complexity guarantee is reported.
- **Recursive rewritings (§7.2).** With functional dependencies,
  access-pattern limits, unions in views or description-logic hierarchies,
  no non-recursive rewriting may be maximally contained; Example 4 shows a
  chain of conjunctive rewritings each adding answers.
- **Certain answers (§7.3) [AD98, GM99a].** Open world: polynomial in the
  size of the view extensions "in many practical cases"; but "the problem
  becomes coNP-hard (in the size of the view extensions!) as soon as we
  allow union in the language for defining the views", or ≠ in the query.
  Closed world: co-NP-hard even for conjunctive views and query without
  comparisons, by reduction from 3-colourability (Example 5). With views
  all complete or all possibly containing incorrect tuples, and no
  comparisons, polynomial; otherwise co-NP-hard. Relative containment
  (certain answers of one query always within another's) is Π2p-complete
  for conjunctive queries and views [MLF00].
- **Regular path queries (§8.3) [CGLV99, CGLV00a].** Rewriting is in
  2EXPTIME; certain answers are co-NP-complete in data complexity.
- **Open problem the survey names (§9).** "I believe that the next
  challenge is selecting which views to materialize in the first place."
  And for searching over candidate view sets: "In this context it is
  important to be able to reuse the results of the computation from the
  previous state in the search space."

## Bearing on the record

**On [CLAIM-303](../claims.d/CLAIM-303.md) and [CLAIM-308](../claims.d/CLAIM-308.md), and the owner's point that reusing a stored
answer for a new question requires recognizing that it covers it.** The
survey sharpens the point in three ways and narrows it in one.

- **Recognition is graded, and the grades cost differently.** Whether a
  stored answer covers the new question exactly (an equivalent rewriting)
  is NP-complete to decide for conjunctive queries, and even checking a
  proposed reuse is NP-complete. But extracting everything the stored
  answers do give, as a maximally-contained rewriting, is polynomial in
  the size of the query and view definitions for conjunctive views
  (inverse rules), at the price of not knowing whether it is everything. In
  [CLAIM-303](../claims.d/CLAIM-303.md)'s terms, c_a splits: partial reuse can be recognized cheaply,
  while certifying that a stored answer settles the question costs a hard
  search. The asymmetry is the survey's own: the polynomial algorithm
  "does not tell us whether the maximally-contained rewriting is
  equivalent".
- **Two different sizes.** Rewriting costs are in the size of the question
  and the stored items' definitions. Certain-answer costs are in the size
  of the stored contents, and there the closed-world case, the one that
  matches materialized results, is co-NP-hard even for conjunctive
  queries. For a filed argument, the definition is its statement of what
  it answers and the contents are the argument. [CLAIM-303](../claims.d/CLAIM-303.md)'s c_a, read this
  way, has a definition-matching term and possibly a content term, with
  different growth.
- **Recognition presupposes definitions.** Every result here assumes each
  stored view carries a definition in the query's own language. A filed
  argument whose question is not stated cannot be matched at all. The
  record's practice of filing a CLAIM with its QUESTION is the analogue of
  a view definition; that is the record's reading, not the survey's.
- **For [CLAIM-308](../claims.d/CLAIM-308.md).** The rent-or-buy bound ([THEORY-348](../theory.d/THEORY-348.md)) needs a fixed,
  known per-use cost. Here per-use recognition cost depends on the
  question and on the set of stored items (the bucket algorithm's
  Cartesian product grows with the number of relevant views). [CLAIM-308](../claims.d/CLAIM-308.md)
  already leaves drifting costs outside; this is one concrete mechanism of
  drift. It does not affect the bound where recognition is cheap or
  constant, as when a stored item is reused only for the identical
  question.
- **What it does not say.** These are worst-case results for formal query
  languages with stated definitions. They do not say recognition is
  expensive in practice (the survey calls the Π2p test "quite efficient in
  practice" because queries are small, and MiniCon scales to hundreds of
  views), and they say nothing about arguments in natural language, where
  coverage is not even a decidable relation without a formal semantics.
  Nor do they price the cost of a wrong recognition, which [CLAIM-303](../claims.d/CLAIM-303.md)'s
  staleness term is about; the survey's views are always correct by
  definition under the closed world, or merely incomplete under the open
  world.

**On [QUESTION-114](../questions.d/QUESTION-114.md).** The survey places the decision the record has been
reading about (which answers to store: Harinarayan et al. [LIT-1094](../literature.d/LIT-1094.md), Gupta
[LIT-1091](../literature.d/LIT-1091.md)) downstream of this one: in warehouse and web-site design "the
first step in determining the utility of a choice of views is to ensure
that the views are sufficient for answering the queries", which is a
rewriting problem. So a joint cost model for stored answers would need
three terms the record's readings have not combined: the recognition cost
priced here, the storage and upkeep priced by the view-selection papers,
and the per-query saving. The survey names view selection as "the next
challenge" and supplies no such model.

## Limitations

- A survey: most theorems are reported, with conditions abbreviated; the
  primary proofs (AD98, DGL00, GM99a, RSU95) were not read.
- No new results, no experiments of its own.
- The statement of the two sources of hardness differs from LMSS95's own
  ([LIT-1100](../literature.d/LIT-1100.md)), where the second source is deciding which query literals
  are redundant, not combining the mappings of several views.
- Cost-based optimizers are described without guarantees; the cost of
  finding rewritings in practice is reported only through the cited
  experiments.

## Connections

Builds on Levy et al. 1995 ([LIT-1100](../literature.d/LIT-1100.md)), cited as LMSS95, and on Chandra
and Merlin 1977 ([LIT-1111](../literature.d/LIT-1111.md)) with Sagiv and Yannakakis 1981 for
containment. It names Harinarayan, Rajaraman and Ullman 1996 ([LIT-1094](../literature.d/LIT-1094.md)) and
Gupta 1997 ([LIT-1091](../literature.d/LIT-1091.md)) among the view-selection works it sets aside, and
Chaudhuri and Narasayya's index tool ([LIT-1083](../literature.d/LIT-1083.md) is their 1997 paper; the
survey cites 1998 papers) among automated index selection.
