---
status: Read
paper: LIT-tmpvpm24
title: Kirsh — The intelligent use of space
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the publisher's typeset article (Artificial
    Intelligence 73 (1995) 31–68, 38 pages, page range and "Received September 1992;
    revised June 1993" printed on the first page), as scanned and posted by the
    author on his own UCSD pages (adrenaline.ucsd.edu/kirsh/Articles/Space/intelligent_useof_space.pdf,
    linked from adrenaline.ucsd.edu/kirsh/publications.html). The scan is image-only,
    so the text was taken by OCR (pdftoppm at 300 dpi, tesseract 5.3.4); the formulas
    on pp. 42, 52 and 56, which OCR garbles, were checked against the page images.
    Kirsh's HTML web version on the same site (Articles/Space/AIJ1.html, "in a slightly
    revised form appeared in Artficial Intelligence 1995" [sic]) was also read in
    full and compared: it is the pre-publication text, it has none of the published
    footnotes (among them the oracle footnote 8 and the Tarjan footnote 9 quoted
    below), and its Tetris timings differ (mental rotation 1000–1800 ms and physical
    200 ms, against the published 700–1500 ms and 150 ms). Everything stated below
    is from the published scan. Read: all six sections, all footnotes, all figure
    captions, Table 1 and the reference list; nothing skipped. The figures themselves
    were seen only as OCR residue and captions. Kirsh and Maglio (LIT-tmp5hdul),
    Hutchins's cockpit paper (LIT-tmpn2s1p), Tarjan 1985 and Lansdale 1991, which
    the paper cites, were not read for this note, so what it says of them is its
    account. Every quotation below was checked against the OCR text by script, with
    whitespace normalised, line-end hyphenation joined and typographic quotes and
    dashes folded to plain ones; the one quotation from the HTML version was checked
    against that text; quoted formulas (b^n, 2^n, O(2^(2^n)), O(n^2), b^d, a(b^d))
    are written in plain notation and were checked against the page images, and
    the list (4)–(6), which runs over a page break, was checked item by item.
date: '2026-10-15'
summary: >-
  A classification, from video of cooks, assemblers and baggers, informal observation
  and the Tetris studies, of how people arrange things around them to cut the time
  and memory a task needs: arrangements that simplify choice (hide or highlight
  affordances, eliminate decisions, offload heuristic properties), arrangements
  that simplify perception (clustering, regions, marking, the vernier effect), and
  spatial dynamics that save internal computation (Tetris rotation, self-cueing).
  It frames the savings in search-complexity terms and links informational structuring
  to amortized computation in a footnote, but says the savings cannot in general
  be meaningfully quantified and offers no cost model, no measurements beyond the
  cited Tetris timings, and no case of an arrangement failing under a deadline.
  Its agents are experts arranging their own workspace in the medium and short term;
  long-term, pre-built environments are set aside.
---

# NOTE-tmplm202: Kirsh — The intelligent use of space

## Contribution

Planning research had studied the temporal order of actions and left "questions of where to lay down instruments, ingredients, work-in-progress, and the like" for later. The paper offers "the beginning of a principled classification of some of the ways space is intelligently used", in three categories: "spatial arrangements that simplify choice; spatial arrangements that simplify perception; and spatial dynamics that simplify internal computation." Its data are "videos of cooking, assembly and packing, everyday observations in supermarkets, workshops and playrooms, and experimental studies of subjects playing Tetris". Its scope is "interactive processes in the medium and short term: on how agents set up their workplace for particular tasks, and how they continuously manage that workplace."

## Key insight

Space is "a resource that must be managed, much like time, memory, and energy." An arrangement does informational work when it changes what an agent perceives as possible, notices, or can read off, without changing what is physically possible. Such work is defined against an oracle: "An action that structures the environment in a purely informational way achieves nothing that could not equally well be achieved by asking an oracle." An arrangement is an oracle that answers slowly, so the useful arrangements are those that make the answer cheap to read: footnote 8 says that oracles "provide answers in unit time whereas agents who must recover relevant information from an informationally structured environment may take considerably longer. This suggests that it is desirable to structure environments in ways that make relevant information most explicit."

## Assumptions

Stated as four tenets (§2):

1. "The agents we observe are experts, or near experts, at their tasks, despite these tasks often being everyday tasks."
2. Experts find enough information locally to choose "without having to plan on-line, using conscious analytical processes."
3. "Experts help to ensure that they have enough information locally by partially jigging or informationally structuring the environment as they go along." This is the paper's focus.
4. Workspaces "are pre-structured in important ways to help compensate for limitations in processing power and memory."

Further:

- **Time scales.** Hammond's long-term "stabilizations" (restoring an environment to known states) are set aside. The paper studies medium-term structuring ("readying of the workplace" for a particular order) and short-term structuring during "the cognitively demanding phase".
- **Informational versus physical jigging.** The distinction "is between planting information in the environment to reduce the perceived degrees of freedom, and planting physical impediments or constraints in the environment to reduce the physical degrees of freedom an agent actually has." The paper is "concerned primarily" with the informational kind.
- **Affordance** is "a dispositional property of a situation defined by a set of objects organized in a set arrangement, relativized to the action repertoire of a given agent. Agents perceive an affordance, when they register that one of their possible actions is feasible in a situation." The "perceived action set" is the set registered as feasible, and arrangement biases it.
- **Evidence** is observational and anecdotal ("From informal observation", "anecdotal reports suggest", one example "supplied by one reviewer of this paper"). The only measurements are the Tetris timings, cited from Kirsh and Maglio.

## Key results

The paper has no theorems. Its results are a taxonomy, illustrative complexity arguments, and Table 1.

**The taxonomy, with its examples.**

*§3. Using space to simplify choice.* "Prima facie, choice is the product of search—visual search for the actions that are currently available, and mental search of the desirability of those available actions. Arrangements which reduce either type of search, simplify the computational burden of agents." Cues and constraints can "(1) reduce the average fan-out of actions perceived as available at decision points; (2) eliminate the need for previously necessary decisions; (3) add new heuristic properties to simplify ranking the desirability of actions."

- §3.2, reducing perceived actions, by hiding affordances or highlighting them.
  - Case 1, production lines hide affordances: the kitchen with washing by the sink and cutting by the board. Stations create a task frame; "The virtue of spatially decomposing the task is that one need not consult a plan, except at the very highest level, to know what to do." An unwet item beside the sink "carries a 'wash me' label."
  - Case 2, cueing blocked actions: a door jam, rags on hot pipes, a plug in the garbage disposal, a fully set table. "Some spatial arrangements say 'Don't do X'. They cue a prohibition." "The absence of a knife is a less good cue than the presence of a pair of oven mits."
  - Case 3, drawing attention to affordances. Obvious things to do: grocery baggers' buffer-zone clusters, in which "Clustering highlights the functional category of items; size highlights urgency; and centrality highlights what is next to be used." Opportunistic things to do: carpenters' scrap wood, flower arrangers' twigs and ferns. The trade-off: "The more that is retained the more cluttered the space, with the result that the very opportunities that might be found go unnoticed."
- §3.3, eliminating decisions: the tailor traces a paper mock-up and flips it for the mirror pattern. "The key technique in eliminating decisions shown here is to substitute compliance for choice."
- §3.4, offloading heuristic properties.
  - The salad maker's rows of slices: "estimation of length is easier and more reliable than estimation of area or volume. By using length to encode number she created a cue or signal in the world which she could accurately track."
  - Case 4, encoding the temporal order of actions: the alternator laid out in a line. "The obvious virtue of encoding orderings in the world is to offload memory." Also the Lansdale and Malone material on memory for location, and the Macintosh icons.
  - Case 5, encoding where to place it: the desk laid out flat as "the data set for a simple assemblage program"; experts "'logic program' with the environment."

*§4. Spatial arrangements that simplify perception*: "to make it possible to notice properties or categories that were not noticed before, to make it easier to find relevant items, to make it easier for the visual system to track items."

- §4.1, clustering to categorize: washed and unwashed tomatoes, the baggers' side groups, card hands.
- §4.2, other Gestalt groupings: similarity, good continuation, surroundedness (bicycle parts on a sheet of newspaper), and notional regions. The Pengi-like "Blockhead" tower copier would need more visual markers for each additional tower; dividing the space into goal, resource and target regions with a known order lets it copy arbitrarily many towers with the original markers: "by creating external regions it is possible to keep memory demands within psychologically realistic limits."
- §4.3, symbolic marking: spoons kept on their pans' lids, and the knife laid on the measured half of a butter stick. "Markers are a form of reminder. But with a twist": they signal that there is something to notice "but not what that is."
- §4.4, clustering to sharpen perceptual acuity: jigsaw piles, and the "vernier effect", by which grouping similar pieces makes fine differences visible.

*§5. Saving internal computation*: "A third way an embodied agent can enlist the world is to pass off computation."

- Analog computation: striking a bundle of spaghetti to sort it, and the tailor's flip.
- §5.1, high-speed offloading in Tetris: "mental rotation of tetrazoids takes between 700 and 1500 ms; physical rotation can take place in 150 ms". "Computational steps are not actually eliminated; they are offloaded from the agent to the world." The mechanism is "a version of just in time inventory control, only here, the inventory is informational."
- §5.2, externalizing representations: Chambers and Reisberg's ambiguous figures, and self-cueing by shuffling Scrabble tiles.

**Cost and complexity framing.**

- **Ways to reduce the complexity of choice (§2.4).** Revise the problem space to reduce branching, to eliminate decision points, or to expose constraints; or "(4) improve search knowledge through chunking, caching, and so on; (5) speed up the creation of a problem space representation; (6) speed up the actual low level computation of search and heuristic evaluation." "Because there are external counterparts to most of these ways we would expect it possible to generate similar complexity analyses. It should not matter whether the change in the agent's computational task comes from modifying the world to simplify choice, or modifying the internal representation of the world to simplify choice. Yet, in practice, complexity analyses have limited significance."
- **A heuristic strong enough to pick one action at each choice point** reduces search "exponentially, from b^n to n" (Fig. 2(a)).
- **No quantitative estimate.** "The actual reduction in computation achieved by the various methods I shall discuss does not, in general, lend itself to meaningful quantitative estimation." A real estimate for the salad cue would need "a cost-benefit analysis comparing the time lost by physically lining up the items, versus the savings in improved layout performance." "What is interesting about the examples, then, is not how much they reduce computation—for that we cannot meaningfully estimate—but how easily they reduce it."
- **Amortization, in two places.**
  - Footnote 9, on self-adjusting data structures, which the paper calls "a more formal model of the benefits of informational structuring": "Tarjan has made an effort to quantify the value of self adjusting data structures under the rubric of amortized computation. His analysis relies on a cost-benefit evaluation: if the average expected benefit of having a data structure with nice properties exceeds the average cost of putting it into that form the self-adjusting algorithm is worth the effort."
  - §3.4, scope as the condition for amortization. A heuristic cue "normally applies to many choice points." Of the salad rows: "Accordingly, the set-up costs could be amortized over the whole task. By contrast, in leaving a plug in the sink, or in placing the next item to be bagged close by, the cost of set-up must be paid off by the savings in the next few actions."
- **Assembly order (Case 4).** Knowing the order turns "a doubly exponential problem" into an exponential one: with two placements per piece, 2^n placements to search with the order known, against O(2^(2^n)) when selection and placement must be solved together. With a forced placement, assembly is constant time given the order, and "if the agent must find an ordering, the problem is O(n^2) ... because at each step the agent must try out the remaining pieces."
- **Perceptual cost (§4).** Standard accounts treat it as a constant factor, so "they may increase the cost of a search from b^d to a(b^d)." But "In absolute time, as opposed to asymptotic time, however, if there is a way to more readily determine the action affordances at a choice point, or the applicability of a heuristic, the agent will have more time to make a choice."
- **Hierarchical grouping (§4.4).** "If the agent can create a hierarchical classification, visual search can be reduced from O(N) to O(log N). Hence coarse grouping is a useful preprocessing technique."
- **Descriptive complexity (§6).** "Preprocessing the world saves processing the representation of the world. Put another way, the greater our understanding of the organization we maintain outside, the less we have to memorize." A good cue "reduces the descriptive complexity of that state to a few bits."

**On arrangements that reduce search or retrieval time.**

- **External partitioning** "makes it easier: to keep track of where things are; to notice their relevant affordances." "If I can't find the garlic, I am not likely to think of rubbing it on the salad bowl—I miss some available actions."
- **Clustering against overestimated memory for location.** "Clustering helps solve these problems because it is harder to lose big things than little ones ... memory for location, as was mentioned before, is regularly overestimated. It is harder to remember where a pen is, than its color."
- **Linear order.** "If all parts are in a line, you know where to look." But "the longer the line of pieces, the more likely the pieces are to be kicked out of order", so many parts are better kept in compact groups.
- **Arbitrary locations are badly recalled.** As arrangements grow complex they "depend more on an agent's ability to remember how things were laid out at set-up time." Lansdale's subjects recalled icon locations poorly because "different locations were arbitrary: there was no meaning to them", and experiments that let subjects use an encoding strategy "showed that having a preexisting system was tremendously helpful." Footnote 11 leaves open whether the poor recall was "due to subjects not having themselves determined the shape or size of the matrix".
- **Diminishing returns.** "as the visual search involved in finding the next piece becomes more complex, the virtue of structuring items is reduced."
- **Explicit labels can cost more search than layout** (Fig. 7(b)): labelled pieces get "stored in a pile. This leads to more visual search during assembly and more computation to ensure the right edges are connected."
- **Readying the workplace** before the high-tempo phase: the short-order cook "arranges items so that the work that has to be done in the high tempo phases of cooking is both simplified and reduced."

**Table 1** (capacity improved; what has been reduced; mechanism):

| Capacity improved | What has been reduced | Mechanism |
|---|---|---|
| Recall | probability of an error in prospective memory | reminders |
| Visual search | time complexity of search; descriptive complexity of environment; probability of an error | use known orderings such as chunks or alphabets |
| Perceptual acuity | granularity of perception; micro-categorization | vernier effect |
| Reasoning | time complexity of planning | cue next action through a known ordering |
| Execution | probability of capture error | maximize cue separation |

## Bearing on the record

**On [QUESTION-tmp1mkzc](../questions.d/QUESTION-tmp1mkzc.md): the paper makes the join to amortized computation in 1995, but only as an analogy in a footnote, and it does not support a single trade.**

- **Kirsh already ties informational structuring to Tarjan's amortized complexity.** Footnote 9 says it, and §3.4 says it in the record's terms: set-up paid once, recovered over the choice points the cue serves, "amortized over the whole task" when the cue's scope is wide and "paid off by the savings in the next few actions" when it is narrow. That is the question's "expected reuse covers it" condition, stated for arrangements. The question asks whether anyone has joined the two literatures. Kirsh draws the link from the offloading side to algorithmic amortization (Tarjan), not to amortized inference, which postdates the paper.
- **The amortization he cites is not memoization.** Tarjan's self-adjusting structures spread the cost of keeping a structure in good shape over a sequence of operations. Kirsh's analogy is to continual small rearrangement ("making local changes in a data structure as we go along"), not to computing a result once and storing it. The question's candidate unification ("storing a result where reading it back is cheap is memoization") is narrower than what Kirsh classifies.
- **The taxonomy holds at least three trades, not one.**
  - Precomputed results left in the world: the salad rows, the ordered alternator parts, the desk layout. These fit the question's precompute-and-store model.
  - Maintained structure that makes later search cheap: clusters, regions, marking. Here the gain is in search cost, O(N) to O(log N), not in a stored answer.
  - Just-in-time offloading (Tetris): "Computational steps are not actually eliminated; they are offloaded from the agent to the world", done at the moment of use on a faster substrate, with nothing stored for later.

  The third is not amortization at all. The first two differ in what is reused, a result or an index.
- **Retrieval cost and failure.** Kirsh's oracle definition says what a purely informational arrangement can at best do, and footnote 8 says it will be slower than the oracle. So retrieval cost is part of the trade, as the question supposes. The paper names three ways the stored structure goes bad:
  - disturbance: lines "kicked out of order";
  - clutter: retained by-products hide the opportunities they were kept for;
  - timing: "A few hundred milliseconds later, and a given rotation will fail to carry useful information".

  These are the paper's nearest things to the question's staleness. It does not treat a stored result that has become wrong for the query.
- **No cost model.** It does not supply the cost model the owner expected to have been formalized. It says the savings cannot "in general" be meaningfully quantified, sketches only worst-case search counts, and leaves the salad cue's cost-benefit as an empirical matter it does not carry out. Of the question's five terms (precompute cost, storage and upkeep, retrieval cost, staleness, expected reuse), it names precompute cost and expected reuse in §3.4, upkeep and retrieval cost informally, and none quantitatively.

**On [CASE-tmp9qlz6](../cases.d/CASE-tmp9qlz6.md): it supports the case's environmental and training counterfactuals and explains why retrieval failed, but it does not cover the case's setting.**

- **"I miss some available actions."** The garlic sentence is the case in one line: an item that cannot be found does not enter the perceived action set. It is close to the medic's "If I can't find it, it isn't there", read as a claim about the perceived action set, not inventory.
- **Memory for location.** The paper says such memory "is regularly overestimated", and that arbitrary locations are poorly recalled while a meaningful "preexisting system was tremendously helpful". This bears on two of A17's counterfactuals, the labelled compartment and the standard layout. The EMT's position (knew the drug was stocked, could not recall where) is the pattern the Lansdale material describes. Kirsh reports it second-hand, not as his own finding.
- **What it does not cover.** Kirsh's agents are experts who arrange their own workspace. A med box is a long-term, pre-built environment (tenet 4, Hammond's scale), which the paper explicitly sets aside. The arranger and the retriever there are different people. Footnote 11 leaves open whether laying out the array oneself is what makes locations memorable.
- **No deadline failures.** The paper has no case of an arrangement failing under a deadline, and no data on retrieval time in such settings.

**On [TERM-tmp5f7cu](../terms.d/TERM-tmp5f7cu.md): it supports the term's separation of presence from timely deployment, and the 2026-10-15 note's point that retrieval can be done before the request.**

- **Perceived versus physical availability.** Kirsh separates the perceived action set from physical feasibility: informational jigging changes the former, physical jigging the latter. α lies past both, at deployment in time. His affordance is a dispositional property that may go unregistered, which matches the term's contrast with affordance.
- **Absolute time counts.** §4 says that perceptual and retrieval costs vanish from asymptotic analyses but matter "in absolute time" because they leave "more time to make a choice". That is the deadline in α, stated as a gap in the standard analysis.
- **Retrieval before the request.** The short-order cook readies the workplace so that work in the high-tempo phase is "simplified and reduced". This is the same move as Hutchins's low-workload speed bugs, which Kirsh cites ([19]). It supports making explicit, if the term is revised, that α can be raised by work done before the request and left in the environment.
- **An inversion.** Footnote 8 bounds the best such arrangement by an oracle answering in unit time. The term's environment argument e is where Kirsh's whole taxonomy would sit, and the paper gives no way to measure how much a given arrangement raises α.

**On [LIT-tmpvpm24](../literature.d/LIT-tmpvpm24.md)'s summary.** The registered summary ("How people arrange items in their workspace to simplify choice, perception and internal computation") is accurate. Two refinements:

- The third category is "spatial dynamics", not arrangements, and its leading case (Tetris rotation) is offloading at the moment of use, not arrangement.
- The paper is a classification with illustrative complexity arguments, not an empirical study. Its one quantitative result, the Tetris timings, is cited from Kirsh and Maglio ([LIT-tmp5hdul](../literature.d/LIT-tmp5hdul.md)).
