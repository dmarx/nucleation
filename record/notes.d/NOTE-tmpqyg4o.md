---
status: Read
paper: LIT-tmp5hdul
title: Kirsh & Maglio — On distinguishing epistemic from pragmatic action
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the copy David Kirsh posts on his UCSD publications
    page (adrenaline.ucsd.edu/kirsh/publications.html, linking adrenaline.ucsd.edu/kirsh/Articles/CogsciJournal/DistinguishingEpi_prag.pdf).
    It is a scan of the published article, with the journal's running heads and
    page numbers 513–549 (37 pp.), so it is the version of record; the page lists
    it under 1995, the article itself prints 1994. Other places looked, same day:
    Unpaywall (no OA location returned); OpenAlex (bronze OA at onlinelibrary.wiley.com/doi/pdfdirect/10.1207/s15516709cog1804_1,
    plus PhilArchive/PhilPapers records KIRODE and CiteSeerX entries); the Wiley
    pdfdirect and pdf URLs (HTTP 403 from this environment); PhilArchive and PhilPapers
    archive PDFs (403); an Internet Archive capture of the Wiley URL (connection
    reset); a guessed UCSD path (404). Text extracted with pdftotext from the scan's
    OCR layer, which garbles the zoid glyphs, some figure contents and a few words;
    Figures 6, 7 and 10 were read from page images, and values read off those figures
    are marked as approximate. Read: the abstract, introduction, "Why Tetris?",
    the process model, all five epistemic uses of rotation, the translation section,
    the Discussion including the planning subsection, and the reference list. Nothing
    skipped. Every quotation of the paper below was checked against the extracted
    text by script, with whitespace and hyphenation normalised; the one that failed,
    from the Figure 7 caption, fails on OCR errors ("ond", "on episode") and was
    checked against the page image. The two quotations of the LIT entry were checked
    against the record file.
date: '2026-10-15'
summary: >-
  Kirsh and Maglio define an epistemic action as a physical action whose primary
  function is to reduce the space, time or unreliability of the agent's own mental
  computation, and argue from Tetris keystroke data that players rotate and translate
  pieces for that reason: zoids are rotated more than plan-then-act would need,
  rotation starts within a few hundred milliseconds of a zoid appearing, and a translate-to-wall
  check is used more the higher the drop. The computational saving is argued, not
  measured: physical rotation of 90° takes as little as 100 ms against an estimated
  800–1200 ms mentally (a three-player pilot), and fewer attentional probes and
  less working memory are needed. The trade is physical action in place of internal
  computation at the moment of use, not precomputation or caching; the paper explicitly
  sets it against caching and chunking accounts of skill, and mentions amortized
  complexity only in passing for everyday cases such as sorting bolts before assembly.
  It says the choice fits a Stigler-style cost–benefit model in outline but that
  such models fail in detail, because an epistemic action's value depends on the
  particular internal computation it serves.
---
<!-- inactive-ok-file: CLAIM-tmpygqjz — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# NOTE-tmpqyg4o: Kirsh & Maglio — On distinguishing epistemic from pragmatic action

## Contribution

The paper names a category of action that standard models of planning and skill leave out: action taken to change the agent's informational or computational state rather than to move the world toward the goal. It builds a classical four-phase information-processing model of Tetris (RoboTetris: bitmap, chunked encoding, placement search, motor plan), shows that this model and its interleaving variant cannot explain how often and how early players rotate pieces, and reinterprets the extra moves as epistemic. It then proposes that planners search a space whose nodes pair physical and informational state.

## Key insight

An action can pay for itself by what it does to the agent's computation, not to the board. In Tetris a rotation is cheap, fast and wholly determinate, so asking the world to rotate a shape can be quicker and less error-prone than rotating it in the head, and a well-adapted agent links attention directly to such actions. The definition: "we use the term epistemic action to designate a physical action whose primary function is to improve cognition by: 1. reducing the memory involved in mental computation, that is, space complexity; 2. reducing the number of steps involved in mental computation, that is, time complexity; 3. reducing the probability of error of mental computation, that is, unreliability." Pragmatic actions are those "whose primary function is to bring the agent closer to his or her physical goal". The Discussion restates it: epistemic actions "are not performed to advance a player to a better state in the external task environment, but rather to advance the player to a better state in his or her internal, cognitive environment."

## Assumptions

- **A classical phase model as foil.** Tetris cognition is modelled as four phases (create bitmap; encode chunks; determine placement; compute motor plan), first fully sequential, then cascaded/interleaved. The argument is that the data defeat both.
- **Uniform target orientations.** The expected-rotation baseline assumes each zoid emerges in a random orientation and is placed in each of its orientations with equal probability, so a four-orientation zoid needs 1.5 rotations on average.
- **Determinate local effects.** Tetris has "no hidden states, exogenous influences, or other agents to change the result of hitting the rotate key." The paper names this as the property that makes the strategy pay.
- **Function is inferred, not observed.** "an action can serve both epistemic and pragmatic purposes simultaneously", and the authors say it is "often hard to prove" which an action served. The clean cases are those with no plausible pragmatic reason.
- **Much of the mechanism is conjecture.** Multiple-perspective representations, the Boltzmann-machine settling account, the decision-tree model of attention and perceptual matching are offered as hypotheses "ripe for experimental testing", not tested.

## Key results

**Game parameters.** Board 10 squares wide and 30 high (as printed). Free fall from about 200 ms per square at the start to about 100 ms per square at the fastest; at medium speed one square per 150 ms, so a zoid takes about half a second to emerge. Four actions: rotate 90° counterclockwise, translate left, translate right, drop.

**Rotation counts (Figure 6).** Each zoid type is rotated more than the plan-then-act expectation (half the rotations before an orientation repeats; 1.5 for a four-orientation zoid), with 95% confidence intervals. Read off the figure, approximately: the T- and L-type zoids average about 1.7–1.75 rotations against an expected 1.5; the two-orientation zoids about 0.6–0.65 against 0.5; the square about zero. No numbers are printed, and the number of players and episodes behind the figure is not stated.

**Rotation timing (Figure 7 and text).** Histograms of rotations against time in the episode: "rotation begins in earnest by 400 to 600 ms and, on occasion, at the very outset of an episode." Some rotations come "before 100 ms", when "the zoid is not yet completely in view". The shortest interkeystroke interval is "about 75 ms" and the average "around 250 ms", so recovering from an over-rotation costs between 75 and 750 ms. Hence interleaving with false starts is "a bad strategy for a well-adapted agent", and the classical and interleaving models fail.

**Early rotation for discovery.** Rotating an emerging zoid exposes its hidden part "150 to 300 ms earlier than if they waited for it to appear naturally." Partially hidden zoids that are ambiguous in both shape and starting column are rotated more often than zoids ambiguous in shape alone, which are rotated no more than unambiguous ones. No test statistic or count is reported for this. No player interviewed had noticed that zoids start in different columns.

**Physical versus mental rotation.** "zoids can be physically rotated 90° in as few as 100 ms, whereas we estimate that it takes in the neighborhood of 800 to 1200 ms to mentally rotate a zoid 90°". The estimate comes from a Shepard–Metzler-style pilot with three players (intermediate, advanced, expert), eight presentations of each zoid pair, correct "same" trials only (Figure 10). Read off the figure, reaction time is about 0.6 s at 0°, 0.9 s at 90° and 1.2 s at 180°, linear in angle. So the 800–1200 ms figure is total reaction time, including encoding and response, not the increment for rotating; the increment is about 300 ms per 90° on the figure. The paper adds 200 ms for pressing the rotate key and still finds physical rotation faster, and notes self-priming might make repeated mental rotation faster (footnote 4). Experts did not show flat (orientation-independent) reaction times.

**Attention (Figures 11–13).** On a 4 × 4 cell model of the iconic buffer, a decision tree identifying the zoid without rotation needs up to three probes; with rotation allowed between probes, at most two, and attention can mostly stay on one cell. This is an illustration, not data.

**Translate-to-wall (Table 1, Figure 15).** In about 1% of drops the player first moves the zoid to the wall and back, read as verifying the column. Mean drop distance, ordinary vs after the routine: intermediate 13.18 vs 19.04, advanced 13.69 vs 19.33, expert 15.65 vs 20.05 squares; within each skill level the means differ by a t test at α = .05. The proportion of drops preceded by the routine rises with drop distance. The text says experts drop "when it is about 13 squares" and "about 19" after the routine, which matches the intermediate and advanced rows of the table, not the expert row.

**What cost is saved and how it is measured.** The costs named are the three in the definition: working-memory space, number of mental steps (time), and error probability. None is measured as a saving in performance. Time is argued from the physical-versus-mental rotation comparison; space from a listing of what visuo-spatial memory would have to hold during mental generate-and-test (re-oriented chunks, the target contour chunk, a record of chunks tried, a contour position marker) and from the need to refresh imagery in the iconic buffer every 200 ms; error from the translate-to-wall routine, whose use rises with drop height. The paper contains no comparison of scores or placements with and without epistemic actions. It reports that experts perform more epistemic actions, as part of a cost–benefit reading, without a table for it.

**When it pays.** The Discussion: the rationale is that "after we have subtracted the cost of time lost in performing an epistemic action, the expected epistemic or computational benefits still outweigh the expected net benefits of performing a pragmatic action." It invokes Stigler's economics of information (search until the expected gain of one more inquiry equals its cost) and says Tetris behaviour fits it in some respects: early rotation tracks how informative it is, the wall routine tracks drop height, physical rotation is cheaper than mental. But "simple economic models of costs and benefits fail because the benefits of an epistemic action depend in considerable detail on just what computations the agent is performing", unlike value-of-information in classical decision analysis, which needs nothing about the agent's reasoning. The paper gives no formal cost model. The conditions it names for payoff are: the action is fast relative to the internal computation it replaces, and its local effect is determinate.

**Framing: trade, precompute or cache?** The paper frames epistemic action as substituting physical action, and the perception of its result, for internal computation, at the time the computation is needed. It is not framed as precomputation or caching. It sets itself against caching explicitly: "Agents do not simply cache associative rules describing what to do in particular circumstances." What agents learn are "qualitatively different behavioral tricks", to "expose information early", "prime themselves", and "perform external checks". It allows that "such epistemic procedures may be cached", which is caching of the procedure, not of results. Three passages come nearer to precomputation and storage, all outside the Tetris data:
- The everyday examples: "memory-saving actions such as reminding, for example, placing a key in a shoe", and "time-saving actions such as preparing the workplace, for example, partially sorting nuts and bolts before beginning an assembly task in order to reduce later search (a similar form of complexity reduction has been studied under the rubric “amortized complexity;” Tarjan, 1985)". This is the one mention of amortization, in a parenthesis, with no development.
- The opening cites external records of intermediate results in arithmetic, and Hutchins (1990) on navigation, as the commonplace symbolic case.
- Footnote 5, on an internal fixed cost: players might "find it worthwhile to pay the fixed costs of constructing an orientation-independent representation if they know they will be facing repeated judgments concerning the same shape." This is amortization inside the head, offered as a possible artifact of test design.

The Discussion also speaks of "offloading structure to the world" and "arranging things so that the world preempts the need for certain representations, or preempts the need for making certain inferences", and concludes that an agent "ought to know how to strike a balance between internal and external computation".

## Bearing on the record

**On [QUESTION-tmp1mkzc](../questions.d/QUESTION-tmp1mkzc.md).** The paper is the founding statement of using action on the world to cut internal computation, and it states the cost dimensions the question needs (space, time, error). It does not join that to amortization. Its Tetris cases are computation done in the world at the moment of use: a rotated zoid is read within a few hundred milliseconds, nothing is stored for a later occasion, and there is no reuse count. That is the opposite end from the speed bugs, which are computed 25–30 minutes ahead and read back later. The paper's only bridge is the parenthetical analogy of sorting bolts to Tarjan's amortized complexity and the reminder examples, which are precisely the stored-result cases and are not analysed. So it names both halves of the question's candidate unification but treats them as two kinds of epistemic action, not one trade; and it frames itself against caching. Its cost–benefit passage is the nearest to an account of when it pays, and it says a general account cannot be given without modelling the particular computation an action serves. That is a reason to expect the question's single cost model (precompute, storage, retrieval, staleness, reuse) to need a process-level term the paper says economic models lack. Staleness does not arise in Tetris because the effects are determinate and the result is used at once; the paper names determinacy as a condition of payoff, which bears on staleness only by implication.

**On [TERM-tmp5f7cu](../terms.d/TERM-tmp5f7cu.md).** The paper's epistemic actions raise the operational availability of information by changing the world during the deadline, not before the request: rotation brings a zoid's hidden part into view 150–300 ms sooner, and early rotations can occur before 100 ms. That is a case the definition already covers through the environment term and procedure π (the procedure includes acting on the world). The note of 2026-10-15 about retrieval done before the request is supported only by the paper's everyday examples (key in a shoe, sorting bolts), not by its data.

**On [CLAIM-tmpygqjz](../claims.d/CLAIM-tmpygqjz.md).** Little direct bearing. The claim's break-even (F + n(c_a + u) < n·c_r) is about a result filed once and reused n times. The Tetris actions have n = 1 and no upkeep. The paper supports the general shape of the claim (an action is worth it when its cost is less than the computation it saves) and its caution that simple economic accounting is not enough, and it supplies nothing on recurrence as evidence of reuse or on staleness. Footnote 5's "fixed costs ... if they know they will be facing repeated judgments" is the only place it reasons as the claim does, and it is speculative.

**What the LIT entry's summary gets right and wrong.** The entry's summary, that players move pieces "to save internal computation" and that epistemic actions "change the world to make mental computation easier, not to advance the goal", is accurate. The registration's phrase "The founding case of offloading computation into action on the world, which is what the cockpit's speed bugs do" needs narrowing: the paper's founding case is offloading at the time of use; precomputation and storage of results for later, which is what speed bugs do, appear in the paper only as unanalysed everyday examples.
