---
status: Read
paper: LIT-tmpras8t
title: Gray, Sims, Fu & Schoelles — The soft constraints hypothesis
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full 2026-10-15 from the publisher's typeset PDF (APA, Psychological
    Review 113(3), pp. 461–482, 22 pp.; PDF metadata title doi:10.1037/0033-295X.113.3.461,
    created 2006-07-24), as posted on a University of Colorado course page, Michael
    Mozer's CSCI 3702 syllabus readings (home.cs.colorado.edu/~mozer/Teaching/syllabi/3702/readings/GraySimsSchoellesFu2006.pdf,
    which redirects to home4.cs.colorado.edu; SHA-256 9c2c7bc7…f482e8b9). This is
    a course's copy of the typeset article, accepted under the record's precedent.
    That server sends the wrong intermediate certificate, so the missing Sectigo
    intermediate (Public Server Authentication CA OV R36) was fetched from Sectigo's
    own address, checked against the system trust store, and added to the CA file;
    verification stayed on. Other places tried, all on 2026-10-15: Unpaywall (closed,
    no OA location); OpenAlex (closed; lists three CiteSeerX records and DTIC ADA459037,
    all submitted versions); CiteSeerX PDF URLs for 10.1.1.140.1121, 10.1.1.709.4258
    and 10.1.1.87.1126 (connection reset); DTIC apps.dtic.mil ADA459037 (403); Gray's
    RPI pages, homepages.rpi.edu (host not resolved) and www.rpi.edu/~grayw (proxy
    502), where the paper's footnote 3 says the model file is posted; Internet Archive
    CDX for the RPI paths (connection reset). So the authors' own copy could not
    be compared against the course copy. Text extracted with pdftotext (raw and
    layout); the layout pass was used for Table 6 and the Appendix equations, which
    the raw pass scrambles. Read: abstract, every section, all three experiments,
    the Ideal Performer analysis, the model results and discussion, the conclusions,
    Appendices A–C, the footnotes, and the reference list skimmed for cited works.
    Figures 2–6 carry their values only as plots and their page images were not
    viewed; fit statistics below are the ones the text states. The supplementary
    Lisp model file was not read. Every quotation of the paper below was checked
    against the extracted text by script, with whitespace normalised; the one other
    quotation is of QUESTION-tmp1mkzc's own note, checked against that file.
date: '2026-10-15'
summary: >-
  In a Blocks World copying task where the model pattern was hidden and opening
  it cost a lockout of 0 to 3,200 ms, people opened it less often, kept it open
  longer, and placed more blocks after the first look as the lockout rose, and the
  trend was graded down to differences of tens of milliseconds. An Ideal Performer
  Model that chooses how many blocks to encode per look (ENCODE-1 to ENCODE-8) by
  Q-learning, with the only reward being negative time and memory given by ACT-R's
  base-level activation, retrieval-threshold and latency equations, fits four measures
  from Experiment 3 with three memory parameters and one softmax noise parameter
  fitted on one of them. The authors read this as support for choosing between head
  and world by time alone, against a minimum memory hypothesis, which they concede
  no one has stated precisely enough to model. The model's only memory costs are
  encoding time, retrieval time and forgetting; it has no term for anything carried
  across trials, for a retrieved item being wrong, or for the world changing.
---

# NOTE-tmpc26wx: Gray, Sims, Fu & Schoelles — The soft constraints hypothesis

## Contribution

The paper extends Gray and Fu 2004 ([LIT-tmpbbd7f](../literature.d/LIT-tmpbbd7f.md)) from ordinal predictions to a quantitative optimal model. It sets the soft constraints hypothesis, that "the control system selects sequences of interactive routines that tend to minimize performance costs measured in time while achieving expected benefits", against the minimum memory hypothesis it attributes to Ballard and colleagues and to Wilson (2002), "that people favor strategies that minimize the use of memory." Three experiments vary the cost of looking at the pattern to be copied. An "ideal performer analysis" then joins ideal-observer analysis with Anderson's rational analysis: a task analysis fixes the steps, published estimates fix their times, ACT-R's memory equations fix encoding, retrieval and forgetting, and Q-learning finds the sequence of choices that minimizes total time. Reinforcement learning is used as an optimizer, not as a theory of how people learn: "we make no claim that the process followed by the algorithm mimics any process followed by human cognition."

## Key insight

On the memory side, the paper says, only three things are priced: "the time required to encode, the time required to retrieve an item from memory, and the probability that an encoded item can be retrieved (i.e., is not forgotten) when needed." A forgotten item costs the time spent encoding it, the time spent failing to retrieve it, and the time to go back. Once memory is priced that way, a model with no bias toward the world or the head, minimizing only expected time, reproduces how people shift from looking often to memorizing more as looking gets dearer. The conclusion is that the control system is "indifferent to information source; resources are allocated to knowledge in-the-world versus in-the-head not based on source, but based on the cost of accessing the source."

## Assumptions

- **Time is the only currency.** Benefit is defined as minimizing time: "just as costs are defined by time, benefits are defined as minimizing time. Optimizing benefits entails minimizing costs." Errors enter only as the time they waste.
- **Selection is local in the hypothesis but global within a trial in the model.** The hypothesis is stated at the "1/3 to 3 sec" level and "predicts optimal performance only in tasks where" optimizing interactive routines is congruent with the global optimum. The model, however, sets the discount γ = 1.0 "meaning that the algorithm should strive to maximize global performance rather than select actions locally greedily", over one trial.
- **The task.** Blocks World after Ballard, Hayhoe and Pelz (1995): copy an 8-block pattern (random colours, no colour more than twice, random cells of a 4 × 4 grid) from a Target Window into a Workspace Window with blocks from a Resource Window. Unlike Ballard's version, every window is covered by a gray box and only one can be open at a time. Resource and Workspace open when the cursor enters. A new random pattern each trial; 40 trials in Experiment 1, 48 in Experiments 2 and 3; analysis drops the first 10 trials.
- **The model's state and actions.** State: the number of blocks not yet placed (1–8). Action: ENCODE-k, encode k blocks on this look, then get and place them until all are placed "or a retrieval failure occurs". 36 state-action pairs. Penalty per action: the total time of its Encode and Get & Place unit tasks (Table 5).
- **Perceptual-motor side conditions are fixed from outside the data** (Appendix C): attention shift 185 ms (ACT-R default), mouse moves 150–249 ms (Fitts' law with ACT-R's a = 0.05, b = 0.10), click 150 ms (Gray & Boehm-Davis 2000), lockout 0–3,200 ms. Encoding a block is 50 ms to create a declarative memory element (DME) plus "rehearsing the element by performing two retrievals".
- **Memory is ACT-R declarative memory** (Appendix A). Base-level activation, Eqn. A-1: a_i = ln(Σ_{j=1..n} t_j^(−d)) + ε, where t_j is "the time since its jth retrieval", d the decay, and ε logistic noise; "The summation is over the entire history of retrievals of the DME." Retrieval fails if activation is below a threshold. Retrieval time, Eqn. A-2: RT_i = F·e^(−a_i); a failed retrieval uses the threshold in place of a_i, so failures "take longer than successful retrievals." Context and goal-relevance terms of full ACT-R are left out as "not relevant to the Blocks World model." Values: decay 0.5 (default); activation noise 0.28, retrieval threshold 0.325 and latency factor F 0.9, all fitted by grid search.
- **Choice among strategies is softmax over the learned utilities**, p(k) = e^(U_k/t) / Σ_j e^(U_j/t), with t = 0.491 fitted by least squares; footnote 5 converts this to choosing the faster of two strategies 1 s apart "on 88.5% of its choices."
- **The minimum memory hypothesis is not modelled.** "as far as we know, there is no version of the minimum memory hypothesis specific enough to implement as a computational model." Its literal form, ENCODE-1 always, is dismissed as trivially wrong; a capacity penalty or a bias weight are named as other readings and not built.

## Key results

- **Manipulations of access cost.** All between subjects, 16–18 per condition. Experiment 1: Target opened by holding the control key (e1-low), by the cursor entering (e1-med), or by entering plus a 1-s lockout (e1-high); estimated time differences 46 ms (low to med) and 1,000 ms (med to high). Experiment 2: a button in the Target Window of 260, 60 or 8 pixels, Fitts index of difficulty 1.7, 2.8, 6.2. Experiment 3: lockout of 0, 200, 400, 800, 1,600 or 3,200 ms, the only one modelled.
- **Behaviour (Tables 1–4).** All three experiments show significant effects of condition on all three measures (e.g. Experiment 3, F(5,104) = 11.60, 13.18 and 17.39 for accesses, first-look duration and blocks placed after the first look). Experiment 3 means, 0 to 3,200 ms: Target Window accesses per trial 5.6, 4.8, 4.5, 3.7, 3.5, 2.9; median first-look duration 1,603 to 4,634 ms; blocks correctly placed after the first look 2.00, 2.39, 2.49, 2.94, 3.11, 3.58. Linear trends account for 98%, 87% and 97% of the variance due to condition. Experiment 1's low and medium conditions (46 ms apart) did not differ significantly on any measure, but each measure moved in the predicted direction.
- **Time, not motor effort.** Lockout (no extra motor work) and Fitts difficulty (more motor work) produced the same pattern, which the authors take to mean "time is the operative factor".
- **Learned utilities (Table 6, 8 blocks left).** The best first action is ENCODE-2 at 0, 200 and 400 ms, ENCODE-3 at 800, ENCODE-5 at 1,600 and ENCODE-8 at 3,200 (ENCODE-7 within 2 ms of it). The paper calls the best-to-worst spread "on the order of 1 to 2 seconds"; by the table it runs from about 0.6 s (800 ms lockout: −29.935 against −30.560) to about 2.1 s (3,200 ms).
- **Fit.** Fitted on blocks placed after the first look: RMSE 0.092, r² = 0.969, within one standard error in five of six conditions (1.15 SE at 800 ms). Not fitted, same parameters: distribution of blocks placed after the first look, RMSE 0.034, r² 0.887–0.958 by condition; first-look duration, RMSE 0.431, r² = 0.980; visits to the Target Window, RMSE 0.397, r² = 0.970 (Monte Carlo).
- **Against the minimum memory hypothesis.** The paper concludes that "The control system is not biased to favor perceptualmotor over cognitive costs" and that "It seems improbable that a computational model employing the minimum memory hypothesis would be able to account for the same broad range of results." This is argued, not tested: the experimental data "do not rule out weaker forms of the minimum memory hypothesis", and no minimum-memory model was fitted for comparison.
- **On Ballard's result.** The authors suggest Ballard et al.'s apparent preference for re-looking may be confounded because memory for the pattern builds over the trial: "if encoding time is amortized over both early and late block placements, then end of trial events do not provide clean estimates of the time costs for encoding blocks in memory." Their own measures use the first look only, to avoid "any cumulative memory trace for the block pattern."
- **Learning time.** People "required on the order of 10 trials to fine tune their strategies"; the model trained for 100,000 trials per condition, which the authors equate with the metacognitive knowledge people bring, acquired "through experience remembering and forgetting things amortized over a lifetime of practice."

## Bearing on the record

For [QUESTION-tmp1mkzc](../questions.d/QUESTION-tmp1mkzc.md) this is the nearest formal head-or-world cost model, as the citation-search note says, and it is narrower than that note's phrase "deciding each access separately" suggests in one respect and broader in another. Each look is one decision (how many to encode), but each is valued by Q-learning against the expected time to finish the whole trial, so the cost of forgetting and having to look again is priced ahead. Within that, it covers exactly two of the terms the question's 2026-10-15 note asks for and none of the others.

- **Retrieval cost: yes, for the head.** Retrieval time depends on activation, and failure costs more than success. Retrieval from the world is a fixed cost (attention shift, mouse move, lockout) with no search term; the windows are at known places and the paper assumes attention moves "to an object at a known location."
- **Upkeep: yes, in part.** Encoding includes two rehearsal retrievals, and forgetting over the retention interval is the risk. This is the nearest thing to storage and upkeep, and it is internal only.
- **Precomputation: no.** Nothing is computed ahead of the request. What is stored is the raw input (colour and position), read just before use. In the question's table this is the fourth strategy, defer and re-read, with a choice of how much to read per look.
- **Reuse across trials: no.** Each trial's pattern is new and random, so no stored content can serve a later trial. The only thing carried across trials is the learned policy, the Q-table, which the authors liken to metacognition "amortized over a lifetime of practice"; the paper names this amortization, as it names amortized encoding within Ballard's trials, and models neither as a cost. Whether a block forgotten in one round keeps its partial activation into the next round of the same trial is not stated; the measures were chosen to avoid that case.
- **Staleness: no.** The target never changes during a trial, and a retrieval either succeeds or fails. The model has no wrong retrieval, so there is no cost for reusing a result that no longer fits the query, and no erosion of the world route over time (the question's Risko and Gilbert term).
- **Predictability of the query: fixed.** The task always asks for the same eight items in an order the performer chooses, so the question's term for how predictable the later query is does not vary here.

What it does support for the question is the paper's central move: memory and the world are priced in one currency, with no bias toward either, and the optimal mix shifts smoothly with access cost. That is the form a single cost model would take. It shows such a model can fit behaviour at the sub-second scale, for one task with one kind of stored item. It does not show that the four strategies in the question's table are regimes of one trade, because three of them involve work or structure that this model has no place for. It also narrows Gray and Fu 2004's reading in one way: there, people relied on memory even when it caused errors, while here errors cost only time and the model has no way for a retrieved item to be wrong.
