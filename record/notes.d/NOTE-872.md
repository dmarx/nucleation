---
number: 872
status: Read
formerly:
- NOTE-tmpmcwoo
paper: LIT-1057
title: Kirsh — Adapting the environment instead of oneself
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from a scan of the published article (Adaptive Behavior
    4(3/4), pp. 415–452, 38 pp., "© 1996 The Massachusetts Institute of Technology"
    printed on the first page), posted by the author on his own laboratory server
    at UCSD (interactivity.ucsd.edu/articles/Adaptive/Adapting_env_00.pdf; Kirsh's
    "Articles" directory, linked from his home page). The scan is image-only, so
    the text was extracted by OCR (pdftoppm at 300 dpi, tesseract). The same directory
    holds the author's HTML version (Final-Single.html), which has the same argument
    and figures but no footnotes and some pre-copyedit wording ("three sections"
    for "five major sections", "Bedau, this issue" for Fletcher, Zwick and Bedau);
    it was used to cross-check OCR errors, and the published scan is the text quoted.
    Read: all six sections, all nine footnotes, Figures 1–7 (Figure 3, the decision
    tree, checked on the page image), the references and the author note. Nothing
    skipped. The PhilArchive copy (philpapers.org/archive/KIRATE.pdf, which Unpaywall
    lists as a submittedVersion) was refused by Cloudflare (HTTP 403), so whether
    it is an author's deposit was not checked, and it was not used. Also looked,
    all 2026-10-15: Unpaywall and OpenAlex (green OA, PhilArchive as the only location);
    the Internet Archive (no capture of the PhilArchive PDF or of the old adrenaline.ucsd.edu
    article path); Semantic Scholar (rate-limited, 429); a web search, which found
    the UCSD copy. Every quotation below was checked by script against the OCR text
    with whitespace and quotation marks normalised; footnote 3, where the OCR misreads
    one word ("Jater"), and the copyright line, which the OCR garbles, were checked
    against the page images, and the two phrases quoted from the HTML version against
    its text. The arithmetic on Figure 3 under Key results is this reading's, not
    the paper's.
date: '2026-10-15'
summary: >-
  A conceptual paper. It models a task as a directed graph of states and actions
  with a cost metric on transitions, and classifies how an agent can improve its
  payoff by actions external to the task: pruning hard initial states, routine maintenance,
  scouting ahead, tools (which change the graph), and actions that make a space
  more "cognitively congenial" (which leave the graph intact and reduce mental operations).
  It names amortization once, as a parenthetical gloss on chimps leaving nut-cracking
  stones in place, and gives an investment rule for maintenance (future benefit
  against present cost times an "interest factor" for risk) in words only. There
  is no cost model with reuse frequency, retrieval cost or staleness; mental cost
  lies outside the graph, and the paper says there is "no general theory" of congeniality.
  The empirical figures are unpublished pilot results.
---

# NOTE-872: Kirsh — Adapting the environment instead of oneself

## Contribution

Kirsh asks how a creature already allocating its time optimally among tasks
can do better. His answer (the "Superoptimality principle") is that only the
payoff function of some task can change, and that the creature can change it
itself by actions outside the task. To make "outside the task" precise he
takes Simon's well-defined task environment, a directed graph, and gives
three criteria for which actions are internal to it. He then sorts
environment-redesigning actions into two families: those that change the
graph's topology or metric, and those that change its cognitive congeniality
while leaving the graph as it is.

## Key insight

Much behaviour that looks like part of doing a task is better read as
changing the task: refusing hard cases, keeping things where they are
expected, looking before acting, making a tool, or arranging the workspace so
that perception replaces computation. The first four change what the agent
can do or what it costs physically; the last changes only how much thinking
the same moves require, and for that the state-space formalism has no place.

## Assumptions

- **The task model.** "Formally, a task can be represented as a directed
  graph, in which the nodes of the graph denote choice points (i.e., possible
  states), the links represent transitions or actions, and a privileged set
  of states represents the possible ways of completing the task." Following
  Simon (1973), a well-defined task environment has an initial state, an
  operational goal condition, discrete choice points, a finite feasible
  action set at each, a consequence function, and "a metric that specifies
  for each state the cost required to reach the next state (or possibly the
  goal), as measured in steps, energy, reliability, or time." Costs are
  per-transition physical costs; there is no term for the cost of deciding,
  remembering or finding.
- **Action selection** is two filters (Elster): repertoire to feasible set,
  feasible set to choice set by a decision rule such as maximize expected
  return.
- **A creature in equilibrium.** The superoptimality argument assumes the
  creature already allocates time optimally (marginal returns equal across
  tasks) and has completed learning; physiology and behavioural strategies
  are fixed on the time scale considered.
- **Task-internal versus task-external** is fixed by three criteria
  (measurable effect on performance, not too general, not too specific),
  which Kirsh calls "both necessary and sufficient" as formal criteria while
  granting they are hard to apply.
- **Superoptimal** means raising the expected value of the current task
  without lowering returns elsewhere, "or else if any lowering of returns it
  causes in other tasks is more than offset by gains in this one."
- Redesign is impermanent: "the environment has been forcibly changed and may
  be expected to return gradually to its original state on the creature's
  death."

## Key results

The paper proves nothing and reports no published experiment. Its results
are a classification and a few worked or piloted examples.

- **Where "amortize" appears.** Once, in the introduction, among three
  examples of economic explanations of environment modification ("standard
  inventory control principles" for storing food, "investment analysis" for
  building a nest): "because good nutcracking stones take time to find, it is
  better to leave them where they will be most useful for everyone concerned
  than to discard them in arbitrary ways (amortize the cost of search)." It
  is not developed. The next sentences use the example to show that such
  principles rank behaviour only for one task: "leaving around a nutcracking
  stone is desirable for the task of nutcracking, but it may not be a good
  tactic overall because it may have a side effect of cueing predators."
  The case is a shared resource (useful "for everyone concerned"), and the
  thing left in place is a tool, not a computed result. Tarjan and amortized
  analysis are not cited; the word does not recur.
- **Four topology-changing strategies (section 4).** "Just say no" prunes
  hard initial states, improving average and worst-case performance
  (Figure 1, a schematic density of case difficulty); "Selectivity is an
  important component of competence." Routine maintenance keeps the
  environment out of states that create extra work (Figure 2, schematic).
  Scouting ahead changes the expected goodness, and so the "distance",
  between states. Tools add nodes, refine states, add shortcuts
  (macro-operators) and change the probability of reaching states.
- **Maintenance makes search unnecessary, and decays.** From Hammond,
  Converse and Grass (1995): when resources reside in appointed places, "it
  will not be necessary systematically to search the work space to find the
  items one requires." But "Entropy teaches us that objects tend to scatter",
  and "A certain state of the environment must be maintained or enforced, by
  the agent itself, by some automatic mechanism, or by other members of the
  agent's group." Upkeep is named as a cost; its rate is not modelled.
  Storing nuts is the same case: "It is better to pay the storage costs and
  the up-front labor costs to build an in-house inventory."
- **The investment rule, and the interest factor.** Whether to do A now when
  its results are needed later "depends on whether the expected benefits to
  be collected some time in the future outweigh the current costs multiplied
  by some interest factor to compensate for risk." Footnote 3 says what the
  risk is: "there is uncertainty about whether I will actually use the
  results of A later, whether the changes I cause by doing A now will still
  be present later, and whether I will even be alive later to enjoy the
  benefits." Kirsh then adds that labour cost varies over time, so that
  "there is risk not only on the benefits side but also on the labor" side,
  and concludes that a creature should do maintenance whenever it has spare
  time and "it should engage in more maintenance actions if it is uncertain
  of when it might next get the chance." No formula, rate or numbers are
  given. The interest factor multiplies present cost rather than discounting
  future benefit; the two are equivalent for a single comparison, and the
  paper does not distinguish them.
- **A second rationale for maintenance** ("artificial intelligence
  principles"): practised skills handle familiar cases fast, and maintenance
  biases the distribution of cases toward the familiar, so that on-line
  reasoning is needed less often.
- **Value of information (Figure 3).** Citing Howard (1966), a lion choosing
  a flank: on prior probabilities the left flank is worth 4.5 (0.3 × 10 for a
  big animal + 0.3 × 5 for a little one + 0.4 × 0) and the right 3.5; after
  scouting, each flank is worth 5, so "any information-gathering activity
  that costs less than 0.5 is worth undertaking." In the tree as drawn the
  flank is chosen before the scouted outcome is resolved, and the 0.5 comes
  from replacing the prior (0.3, 0.3, 0.4) with (1/3, 1/3, 1/3), which is
  not the prior's expectation. So the figure is not a value-of-information
  calculation in Howard's sense, where the gain comes from choosing after
  observing. Footnote 4 confirms the reading the tree implies: "The values
  0.33 for large, small, and no animal are by no means necessary", and
  scouting may also reduce the chance of missing, changing them to perhaps
  0.4, 0.4, 0.2. Kirsh's scouting is modelled as changing outcome
  probabilities, that is, as a change to the graph's metric. The commuting
  example (looking at the highway merge before choosing a route) is the
  standard decision-after-observation case and is given in words only.
- **Cognitive congeniality (section 5).** Some task-external actions "leave
  the state space formally intact but that reduce the number and cost of
  mental operations needed for task success." Tic-tac-toe and the game of 15
  share a state space and differ in congeniality. Kirsh assumes that "a class
  of actions exists that may improve task performance and that lies outside a
  state-space formalism", and says of congeniality "To date, there is no general
  theory to report". Mental cost, including the cost of reading back what the
  environment holds, has no place in the graph.
- **Complementary actions and external encoding.** Pointing and moving
  coins while counting: error rates of more than 50 percent untouched, about
  35 percent with pointing, "nearly 20 percent" with free movement (pilot
  studies, footnote 6; no sample sizes). Finding the longest of 20 sticks
  without manipulating them: "they took more than 55 percent more time and
  made more than three times as many errors" (pilot; no sample size). A
  discard pile records the state of the algorithm, "an algorithm that is
  being executed partly in the world and partly in the creature's head."
  Card players sort their hands to encode plan fragments, and "This savings
  will reappear every time a change in intentions is made": the one place the
  paper ties a saving to the number of later uses, without a model. A child
  of 18 months rotating a puzzle back to its familiar orientation (one
  observation) is read as bringing the world into line with stored memory.
- **Conclusion.** Both families "have the effect of altering the average task
  complexity of performance."

## Bearing on the record

**On [QUESTION-095](../questions.d/QUESTION-095.md): the paper names the trade and the risks a cost model
would need, and models none of them.**

- **The single "amortize" is a gloss.** It is one parenthetical, about a tool
  left where others will need it, used as an example of an economic
  explanation that is valid only within one task. The record's filing
  ([LIT-1057](../literature.d/LIT-1057.md): "leaving tools in place to amortize the cost of search, named
  and not modelled") is accurate. What is left in place is an object that
  saves search, so the example belongs to the second of the question's four
  strategies (maintain structure that makes search cheap) more than to the
  first (precompute and leave a result).
- **The question's note attributes the Tarjan citation to Kirsh.** That is
  Kirsh 1995 ([LIT-1076](../literature.d/LIT-1076.md)). This paper does not cite Tarjan or amortized
  analysis and does not try to quantify savings.
- **The environment model cannot hold retrieval cost.** The graph's metric
  prices physical transitions: steps, energy, reliability, time. The actions
  that matter most to the question (external encoding, layouts that let
  perception replace computation, reading a result back) are in section 5,
  which Kirsh places outside the formalism. A cost model in which retrieval
  is a kind of computation would have to supply what he says is missing.
- **The interest factor is the closest thing to a cost model, and its
  footnote lists three of the question's terms.** Footnote 3's risks are
  whether the result will be used (expected reuse, though as a probability of
  any use, not a frequency), whether the change "will still be present later"
  (persistence of the store; with "objects tend to scatter", the upkeep
  cost), and survival of the user. It has no term for whether a stored result
  is still right for the query (staleness in the question's sense; here it is
  only whether the stored thing survives), no retrieval or search cost on
  read-back, no query predictability, and nothing on erosion of the internal
  route. All of it is verbal.
- **Time-varying labour cost is the cockpit's rationale.** Kirsh's
  complication, that A cannot always be done "at the last minute ... without
  incurring potentially exorbitant costs", so it should be done when labour is
  cheap and more of it when the next chance is uncertain, is the reason the
  speed bugs are set 25–30 minutes out at low workload ([LIT-1066](../literature.d/LIT-1066.md)). This is
  the paper's most usable contribution to the question: precomputation pays
  not only through reuse but because the cost of the same work differs by
  when it is done.
- **The value-of-information treatment does not help the defer-and-re-read
  strategy.** Figure 3 changes outcome probabilities rather than conditioning
  a choice on what is observed, so it does not give a price for looking again
  at the moment of use (Ballard, [LIT-1075](../literature.d/LIT-1075.md)). The commuting example does,
  in words.
- **Reuse appears once,** in the card-sorting remark that the saving recurs
  with every change of intention. Nothing makes the value of a layout scale
  with the number of later reads.
- On the question's second note, whether anyone has joined distributed
  cognition and amortized inference: this paper does not. It sits wholly on
  the distributed-cognition side and its economics are investment and
  inventory analogies.

**On [CASE-085](../cases.d/CASE-085.md): it gives the case's environmental counterfactual a
rationale and an upkeep cost, and nothing on search failure or stopping.**

- Routine maintenance, after Hammond et al., is the case's "labelled
  compartment" and "standard layout" counterfactuals: when items are in their
  appointed places, systematic search of the workspace is unnecessary. Kirsh
  adds that the arrangement decays ("objects tend to scatter") and must be
  enforced by the agent, a mechanism, or the group, which matches the case's
  point that the failure need not be the individual's.
- The case separates knowing the drug is present from knowing where it is.
  Kirsh's maintenance argument concerns where things are, not whether the
  agent remembers where; his second rationale (maintenance keeps cases
  familiar so practised skill applies) is the nearer fit to a check of the
  unit that did not leave the location retrievable under load.
- The paper has no search cost on the agent's side, no deadline and no
  stopping rule, so it says nothing about the paramedic's switch or the
  maxim "If I can't find it, it isn't there." The nearest strategy, "just say
  no" (declining a hard case), is about entering a task, not abandoning a
  search within one, and the case should not be read as an instance of it.

## Limitations

- Conceptual: no theorem, no fitted model, no published experiment. The
  numbers are from unreported pilot studies without sample sizes, and the
  child's puzzle is one observation.
- The cost metric is physical; cognitive cost is outside the formalism by the
  paper's own account.
- The economics (investment, interest factor, inventory) are analogies
  without formulas.
- Figure 3's value-of-information example does not compute value of
  information in Howard's sense (see Key results).
- Fixed time budget and equilibrium assumptions; nothing on learning, on
  costs that change as a store is used, or on populations.
