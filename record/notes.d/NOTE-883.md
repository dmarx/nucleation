---
number: 883
status: Read
formerly:
- NOTE-tmpv6kkr
paper: LIT-1075
title: Ballard, Hayhoe, Pook & Rao — Deictic codes for the embodiment of cognition
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the typeset Behavioral and Brain Sciences PDF
    (BBS 20(4), the whole treatment, pp. 723–767, 45 PDF pages: target article,
    Open Peer Commentary, Authors' Response, references), posted on Dana Ballard's
    own page at the University of Texas at Austin (https://www.cs.utexas.edu/~dana/bbs.pdf,
    also served at https://www.cs.utexas.edu/users/dana/bbs.pdf). A second copy
    on Rajesh Rao's page at the University of Washington (https://homes.cs.washington.edu/~rao/deictic.pdf)
    is the same publisher file (same PDF metadata and creation date, identical extracted
    text, 48,442 words) and was not used further. Unpaywall reports the DOI closed;
    OpenAlex reports it closed but lists a CiteSeerX record (10.1.1.49.3813) and
    a University of Rochester repository record (hdl.handle.net/1802/1457, resolving
    to urresearch.rochester.edu), both as submitted versions, which were not fetched
    because the author-posted typeset copy was in hand; Semantic Scholar's API did
    not find the DOI. Text extracted with pdftotext. Read: the target article in
    full, pp. 723–742 (sections 1–5, Tables 1–7, Figures 1–17 captions, notes 1–15).
    Figures 9b and 11 carry numbers not in the running text, so the pages with them
    (pp. 732, 734) were rendered as images and read; the bar heights of Figure 9b
    given below are read off the plot and are approximate. Not read: the Open Peer
    Commentary and the Authors' Response (pp. 742–767), so nothing here reports
    the critics or the authors' replies to them. The experimental details the article
    defers to Ballard et al. (1995) and Pelz (1995) were not read, so the number
    of trials, the block count per pattern and the statistics are as the target
    article gives them, which is mostly not at all. Every quotation below was checked
    against the extracted text by script, with whitespace normalised; one quotation
    runs across a page break, where the running head and Table 7 interrupt it in
    the extraction, and was checked across the break.
date: '2026-10-15'
summary: >-
  At about a third of a second, the time scale of a saccade, the article models
  fixation as a pointer that binds a variable in a behavioural program to a place
  in the world, so that what is bound is only the task-relevant feature, fetched
  just before use. In a block-copying task subjects looked back at the model about
  1.3 times per block on average, the commonest cycle being two looks per block
  (one apparently for colour, one for position), and chose this slowest, lowest-memory
  strategy (about 3 s a block, against about 1.5 s for copying from memory) though
  told to be fast; separating model and copy by 70° cut looks to 1.0 per block,
  and one-colour patterns that could be chunked cut them to 0.7. The authors read
  this as working memory having a "carrying cost" that exceeds the cost of re-acquiring
  from the world, but that cost is inferred from the choices and never measured
  or modelled, and the evidence is one task with small samples (seven subjects for
  the main data, three for the colour-change experiment) and no statistics reported
  in the article. What is left in the world is unprocessed input, not a computed
  result, and the article argues against precomputation where the needed products
  cannot be foreseen.
---
<!-- inactive-ok-file: CLAIM-298 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# NOTE-883: Ballard, Hayhoe, Pook & Rao — Deictic codes for the embodiment of cognition

## Contribution

The article proposes an "embodiment level" of description for the brain,
at about a third of a second, between the attentive or deliberate act
(about 50 ms) and the cognitive unit task (2–3 s) (Table 1, adapted from
Newell 1990). At that level, the claim is, body movements are pointers:
"deictic" codes, after Agre and Chapman (1987) and Ullman (1984), in which
a fixation, a reach or an attentional shift binds an object in the world to
a variable in a behavioural program. It argues for this in three ways: a
computational argument that programs using few pointers are cheaper to
learn and suffice (section 2, with simulations and a teleassistance robot);
eye-tracking experiments on block copying (section 3); and a speculative
mapping onto cortex, parietal saliency maps and the basal ganglia
(section 4).

## Key insight

The pointer is the cheap thing, not the content. In a computer, changing
which object "the-bee-chasing-me" refers to costs one memory write
instead of copying every property (Table 2). "Changing gaze is analogous
to changing the memory reference in a silicon computer." The world plays
the role of memory, a fixation is the dereference, and working memory
holds only the few pointers needed at the moment. So "the necessary state
required to keep track of a complex task can be represented with just the
temporal history of a handful of pointers". People then keep little in the
head and re-read the world just in time: "Deictic representations allow
the brain to leave important information out in the world and acquire it
just before it is needed in the cognitive program. This avoids the
carrying cost of the information."

## Assumptions

- **Hierarchical time scales.** Following Newell, each level composes about
  ten operations of the level below, so levels run at geometrically slower
  rates. The embodiment level is placed at 0.3 s because "Body movements
  such as saccadic eye movements take about 200–300 milliseconds to
  generate", and "Saccadic eye movements are typically made at the rate of
  about 3 per second". "Human working memory has a natural decay constant
  of a few seconds".
- **Working memory items are pointers.** "Working memory items may be
  thought of as corresponding to computational pointers." Fixation and
  attention are one or two pointers held by the body or by attention; more
  need working memory. Its capacity is held to reflect "a balance between
  the natural decay rate of the marked items and the temporal demands of
  the task".
- **Few pointers are preferred** because, under a sequential search model
  as in reinforcement learning, the cost of finding an alternative program
  "could potentially scale as" (MV)^s, with M pointers, V visual or manual
  routines and s steps. This is a stated possibility, not a derived or
  tested bound.
- **The task's primitives are individual blocks.** The analysis of the
  copying data assumes "the individual blocks are primitives for the task",
  so that a look at the model fetches one property of one block. Patterns
  were random colours chosen to resist grouping.
- **The information is in view.** The whole account of the trade assumes
  the model stays visible and unchanged except where the experimenters
  change it. "The limited number of variables need only be a handicap if
  the entire task is to be completed from memory".
- **Cost is read from choice.** That memory is costly is inferred from
  subjects preferring slower, lower-memory strategies. No cost is measured
  independently.

## Key results

The block-copying task (section 3): a display divided into a model (the
pattern to copy), a resource (loose blocks) and a workspace (where the copy
is built). Subjects were told only to work "as quickly as possible". The
main data were collected with simulated blocks moved by a mouse on a
Macintosh, eyes tracked by a Dual Purkinje Image tracker; the authors say
the same pattern holds "with real blocks and hand movements, with as many
as 20 subjects [Pelz 1995]".

- **Re-looking rather than memorizing.** Copying the pattern as four
  memorized two-block subpatterns, "well within visual memory
  limitations", would need four looks at the model. "Instead,
  subjects sometimes made as many as 18 fixations in the model area in the
  course of copying the pattern", and "commonly made more than one fixation
  in the model area while copying a single block". The average was 1.3
  looks at the model per block (stated in the control comparisons below), consistent with the
  strategy mix that follows.
- **Strategy frequencies (Figure 9b, seven subjects).** Coding each block
  cycle by fixations: M-P-M-D (look at model, pick up, look at model again,
  drop) is "memoryless" for colour and location; P-M-D implies colour was
  remembered, M-P-D location, P-D both. The M-P-M-D "strategy is the most
  frequently used by all the subjects, far outweighing the others". Read off
  the plot, approximately: M-P-M-D about 43%, P-M-D about 28%, M-P-D about
  11%, P-D about 11%, other about 6%. "In the data, “pickup-drop” sequences
  were invariably the last one or sometimes two blocks in the sequence."
- **Time against memory (Table 7).** Per block: M-P-M-D 3 s (no items
  held), P-M-D 2.5 s (colour), M-P-D 2.0 s (offset), P-D 1.5 s (colour and
  offset). So the most used strategy is the slowest: "it is surprising that
  subjects choose minimal memory strategies in view of their temporal cost,
  especially because they have been instructed to complete the task as
  quickly as possible, and memorization saves time."
- **Raising the cost of looking.** With model and copy moved to eccentric
  positions 70° apart, "The number of eye movements decreases from an
  average of 1.3 per block to 1.0 per block." The authors: "eye movements,
  head movements, and memory load trade off against each other in a
  flexible way."
- **Control for unreliable memory and idle looks.** Two rival readings are
  raised: the eyes are idle while the hand moves, or "working memory is
  cheap but unreliable, so that subjects are checking to compensate for
  memory errors." With all blocks one colour, so that segments could be
  chunked, looks fell to "0.7 per block in the monochrome case versus 1.3
  per block in the multicolored case", and subjects copied subpatterns
  without looking. The 70° condition is also cited against unreliable
  memory: longer transit should have meant more checks, and there were
  fewer.
- **What is kept across a saccade (Figures 10, 11; three subjects).** A
  block's colour in the model was changed during a saccade on about 25% of
  model fixations. Changed before pickup (when colour is presumably being
  fetched), fixation time rose by only about 50 ms (about 400 against
  350 ms on the plot): colour seen on earlier model fixations had not been
  kept. Changed after pickup (when colour is already held and position is
  being fetched), it rose by 129 ms (about 560 against 430 ms): the held
  colour now conflicted. "in most instances subjects were not aware of the
  change", yet picked a neighbouring block of the held colour. "The
  important finding is that the information retained from prior saccades
  is determined by what is currently relevant for the task."
- **Different computation, same place.** Subjects fixate the same model
  location for colour and then for relative position: "they need to apply
  a different computation to the same image data."
- **Simulations and robot (section 2).** A reinforcement learner solved
  "pick up the green block" with two pointers (fixation and attention) and
  a 16-feature deictic representation (Table 3); Chapman's tower copy needs
  three pointers whatever the tower height; McCallum's history trees needed
  2 to 14 short-term features in highway driving. In teleassistance, the
  human's deictic signs (point, preshape, halt) took 22% of the total time
  of a door-opening task, the robot's routines the rest.
- **Neural proposal (section 4), speculative.** Pointer referents as
  81-dimensional spatiochromatic filter vectors; identification matches the
  foveal vector to stored models, location matches a remembered vector to
  every retinal location and yields a parietal "saliency map"; the basal
  ganglia hold program sequence. Supported by simulation and citation, not
  by new data.

## Bearing on the record

**On [QUESTION-095](../questions.d/QUESTION-095.md): it is the clearest case of the opposite policy to
the cockpit's, and it states the trade as a cost comparison, but it does
not give the unifying cost model the question asks for.**

- The article's trade is between holding information in working memory
  and re-acquiring it from the world when needed. Its term is "carrying
  cost": "the carrying cost of working memory is expensive compared to the
  cost of acquiring the information on-line, so that low memory strategies
  are preferred." Raising the cost of re-acquisition (70° separation)
  shifts the balance toward memory, and making memory cheaper (chunkable
  one-colour patterns) shifts it further. So the direction of the trade
  responds to both costs, as a cost account predicts.
- It is not the same trade as amortization in the sense the question
  means. What is left in the world is raw input (the model pattern), not
  the result of a computation; the costly step deferred is a fetch, and the
  computation applied to what is fetched is done anew each time. The
  article goes further and argues against precomputation where the needed
  products vary: "An obvious reason for timely, task-dependent computation
  is that its products are so varied that the brain cannot precompute
  them." The cockpit's speed bugs precompute because the later need is
  known and invariant; this task defers because, at each step, only one
  property of one block is needed. The two cases fit one ledger only if
  the ledger has a term for how predictable the later query is, which the
  question's list (precompute cost, storage and upkeep, retrieval cost,
  staleness, expected reuse) does not name directly.
- Staleness is tested here in the reverse direction: the world changed
  during a saccade, and the agent that had not memorized was mostly
  unaffected, while the one holding the colour paid 129 ms. Re-reading the
  world is a defence against staleness that memorizing is not.
- The cost model is not formal. Costs are inferred from choices; no
  utility, no fitted model, no statistics in the article. The (MV)^s
  scaling is about learning programs, not about the memory-versus-look
  choice. A reader wanting the formal version should look to Gray and Fu
  ([LIT-1058](../literature.d/LIT-1058.md)), which this article precedes.
- Neither this article nor its reference list joins the deictic account to
  amortized inference. It joins it to virtual memory: pages "brought into
  the memory from peripheral storage as required", which is demand paging,
  a caching policy, not memoization.

**On [TERM-055](../terms.d/TERM-055.md): it supports the note of 2026-10-15 that α needs the
world's retrieval cost made explicit, and it shows the policy that keeps
α high without precomputing.**

- Here the agent relies on the world's α being high (a look costs a
  saccade and a fixation, roughly a third of a second) and declines to
  raise its internal α by memorizing. When the world's retrieval cost rose,
  people memorized more. So the choice between internal and external
  sources tracks their relative retrieval cost, which is what α under the
  environment term e would have to carry.
- It does not support moving retrieval earlier. It shows people moving it
  later, to "just before it is needed". Both are compatible with α; the
  article supplies the case where deferral is preferred, under a visible,
  stable and cheaply reachable source.

**On [CLAIM-298](../claims.d/CLAIM-298.md): it bears only by analogy, and does not test the
claim.**

- Its mechanism is cue-driven retrieval: the location routine matches a
  remembered feature vector against every place in view and returns the
  best match, and the same image yields colour or position depending on
  the program step. What is extracted from an unchanged source depends on
  the query, which is the form of the claim's Retrieve(M, q).
- But the source is the visual scene, not stored knowledge; the query is
  set by the task step, not by a frame or anchor; and there is no
  judgement whose shift is measured. The colour-change result (behaviour
  altered by a change subjects did not notice) shows task context
  controlling what is kept, not a frame controlling what is reachable in
  memory. It neither supports nor weakens the claim's defeat condition.

What the article does not show: that the result generalizes beyond
block copying, which the authors argue by analogy to chess and driving
(section 5.1); that the carrying cost of memory is a measured quantity;
or any of the neural mapping in section 4, which is proposal. The
commentaries, which were not read, are where these limits would have been
pressed.
