---
status: Read
paper: LIT-tmpjg8mc
title: Howes, Duggan, Kalidindi, Tseng & Lewis — Short-term remembering as boundedly
  optimal strategy choice
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full 2026-10-15 from the text of the publisher's typeset article (Cognitive
    Science 40(5), pp. 1192–1223, 32 pp.; running heads "A. Howes et al. / Cognitive
    Science 40 (2016)" with page numbers, copyright line "Copyright © 2015 Cognitive
    Science Society, Inc."), as deposited in the University of Michigan's institutional
    repository Deep Blue (hdl.handle.net/2027.42/133633, which holds cogs12271.pdf,
    the publisher's version, and cogs12271_am.pdf, the accepted manuscript) and
    served as extracted full text by CORE's reader page for that Deep Blue record
    (core.ac.uk/reader/86638046, CORE output 86638046, data provider "Deep Blue
    Documents", oai:deepblue.lib.umich.edu:2027.42/133633). The page embeds the
    full text (89,159 characters) in its page data; it was saved as core_reader.html
    (SHA-256 05a042bb…28fe9bc92) and the text as core_fulltext.txt (SHA-256 d93aa7c3…dacd04ab).
    No PDF could be fetched, so this is CORE's text extraction of the typeset PDF,
    not a file I extracted myself: figure images are absent (Figs. 1–10 survive
    only as captions and scattered axis labels), and minus signs were lost in "optimal−1",
    which the extraction renders "optimal1". Places tried, all 2026-10-15: Unpaywall
    (bronze OA; lists Wiley pdfdirect, Deep Blue accepted version, and the Birmingham
    Pure record as submitted version); OpenAlex (same, plus PubMed 26294328, no
    PMC copy); Semantic Scholar (openAccessPdf = Wiley pdfdirect); Wiley onlinelibrary.wiley.com/doi/pdfdirect/10.1111/cogs.12271,
    /doi/pdf/, /doi/full/, /doi/am-pdf/ (403, Cloudflare challenge, curl and WebFetch
    alike); Wiley TDM API (400, needs a token); the Birmingham Pure record (landing
    page 200, listing "Accepted author manuscript, 956 KB", research.birmingham.ac.uk/files/23709347/Howes_2015_EmailCal.pdf,
    which returned 403 Cloudflare to curl and WebFetch); Deep Blue handle, item
    page, DSpace API and bitstream URLs (403 Cloudflare); Lewis's lab page public.websites.umich.edu/~rickl/bounded-optimality.html,
    which the search snippet says links a PDF (403 Cloudflare, also via www-personal.umich.edu);
    CORE download/86638046.pdf (403) and the CORE API download (429); Europe PMC
    and PMC (no PMC copy); ERIC EJ1107334 (no ERIC full text); the Internet Archive,
    whose availability API reports captures of the Deep Blue bitstream (2024-05-07)
    and of Wiley /doi/pdf/ (2023-11-15), but web.archive.org, wayback.archive.org
    and api.fatcat.wiki reset every connection from here (about fifteen attempts),
    and scholar.archive.org rate-limited; web searches for course-hosted copies
    found none. Read: abstract, Sections 1–5 (introduction, bounded optimality and
    its contrast with bounded rationality and probability matching, both experiments
    with method, results and discussion, general discussion and future work), acknowledgements,
    the reference list and the supplementary-figure captions. Not read: Figs. S1
    and S2 (separate files, per-participant plots), and no figure was viewed, so
    values shown only in figures (e.g. Fig. 2's rate per list length) are not reported.
    Every quotation below was checked against core_fulltext.txt by script, with
    whitespace, typographic quotes and hyphenation at line ends normalised; three
    short quotations of the record (LIT-tmpjg8mc, NOTE-tmpmd0yp, LIT-tmppqntw) were
    checked against those files the same way.
date: '2026-10-15'
summary: >-
  Participants copied names one at a time from a mock email to a mock calendar and,
  after a forced phase that measured their own copying rate at every list length
  from 3 to 9, chose how many names to take per trial; the list length that had
  given each person the highest rate in their own data predicted their choice better
  than one item fewer or one more (55% vs 8% and 17% of choices in Experiment 1,
  N = 40; 46% vs 12% and 14% in Experiment 2, N = 20). An exponential points schedule
  raised chosen list length (6.99 vs 5.07), but doubling the cost of an error (whole
  trial forfeited) did not (5.00 vs 5.05). The "boundedly optimal" prediction is
  the argmax of each participant's measured rate, not a model with capacity, error
  or look-up parameters, and the task has no look-up: names are shown once, in sequence,
  and cannot be consulted again. 13 of 60 participants persistently chose a non-optimal
  length, 10 of them one item more.
---

# NOTE-tmpsjfyh: Howes, Duggan, Kalidindi, Tseng & Lewis — Short-term remembering as boundedly optimal strategy choice

## Contribution

The paper tests whether an individual, not just a group average, chooses how much to hold in short-term memory at the level that maximizes their own reward rate, "given the bounds imposed by individual information-processing capacities and their experience". It sets this against the offloading view it attributes to Hollan, Hutchins and Kirsh (2000) and Ballard et al. (1997), and against probability matching. Its method is a reversed version of Siegler and Lemaire's choice/no-choice paradigm: a no-choice phase forces every participant through every list length, so each person's reward-rate distribution for each strategy is measured, and a choice phase tests whether they then pick the best one. The authors present this as going beyond Gray et al. 2006: "unlike for Gray et al. (2006), it is possible to draw conclusions about the efficiency of a participant's choice of memory load."

## Key insight

Bounded optimality can be tested without a process model if the analyst measures each person's payoff for each strategy directly. The no-choice phase gives, per participant, an empirical distribution of reward rate for each list length; the boundedly optimal strategy is the one with the highest rate, and the test is whether the person picks it. In the authors' words, "the cost of optimization is paid by the analyst, not by the participant", and here the analyst's optimization is a lookup of the best measured mean. The bounds (memory capacity, error proneness, typing speed) enter only through the measured rates; none is a parameter.

## Assumptions

- **The task** (Experiment 1). A Visual Basic simulation of Outlook email and calendar. In the email view, each click of "Click for timeslots" shows one message of the form "09.00: Appointment with NAME"; "Only one name and appointment were visible at a time". After all of a trial's appointments have been shown, a "Calendar" button switches to the calendar view, with nine boxes for 09.00–17.00, where the participant types the names in capitals and clicks "Finished". Names are drawn from 16 four-letter first names, eight male and eight female, each with a different first letter; no name repeats within a trial. Times are always 09.00 onward in hourly order, so "only the names and the order they were presented in needed to be remembered". Feedback marks errors; "Participants could not go back to correct errors". Nothing in the method lets a participant return to the email view during recall, so there is no look-up of a forgotten name. (The paper's overview once says "copying messages from a calendar to an email system", the reverse of its method.)
- **The strategy space** is one dimension: list length s ∈ {3, 4, 5, 6, 7, 8, 9}, the number of appointments shown before the calendar opens. The authors say the real space also includes "encoding method, and rehearsal method" but they do not model these; the list length and incremental presentation "encouraged participants to adopt a strategy that involved the encoding of a certain number of appointments in memory." Taking a shorter list does not mean looking something up; it means doing more trials, each carrying the inter-trial overhead, to reach the fixed total.
- **Utility is reward rate.** Participants had to reach a fixed total of correctly copied items "as quickly as possible", told that making errors was "only problematic insofar as it slowed down the overall time" taken. Analysis uses rate R = points on a trial divided by trial duration, where duration runs from the end of the previous trial to the end of this one, so it "included the time cost of moving from one trial to the next."
- **The boundedly optimal list length** for participant p is B_p = argmax over s of R_p,s, the participant's mean rate at that length. For the trial-by-trial analyses, "probability best" for each length is the probability that a sample from its empirical rate distribution over trials 1 to k−1 beats samples from the others (1,000 Monte Carlo draws per length per trial). Which trials enter the mean rate for B_p (no-choice only, or both phases) is not stated precisely; Fig. 3's distributions pool both phases.
- **Optimality is methodological.** "Bounded optimality does not assume that the mind is unlimited; rather, it asserts that the analyst can make use of optimization to test theories of the bounds". Reinforcement learning is invoked for its problem definition, not as a model of learning or a solver.
- **The paper's focus is exploitation after forced exploration**; exploration in the choice phase is discussed but not modelled.

## Key results

- **Experiment 1** (N = 40 Manchester students, £5; 20 per group, between subjects). Manipulation: cost of an error. Low Error Cost: each wrong item scores zero. High Error Cost: "all of the appointments in a trial were counted as errors if one or more of them was copied incorrectly." No-choice phase: blocks of seven trials, one of each length in random order, until 200 items correctly copied. Choice phase: 100 more, length chosen on each trial.
  - Mean chosen length 5.05 (SD 0.67) Low, 5.00 (SD 0.78) High; no difference (ts < 1). The authors call this "disappointing" but note the mean choice in both conditions is predicted by the no-choice rates.
  - Correlation of B_p with chosen length, both groups pooled: r(38) = .35, p = .027, "12.25% of the variation between participants".
  - Probability matching: no correlation between (logit) probability of selecting one's most frequent length and the probability that it was optimal, r(38) = .061, p = .707. Mean probability optimal 0.49 against mean selection probability 0.80 (permutation test, 10,000 resamples, p < .001), so people chose their favourite more often than matching predicts.
  - B_p predicted 55% (SD 32) of choice-phase selections, optimal−1 8% (SD 12), optimal+1 17% (SD 24); B_p beat each (p < .001); lengths further away predicted fewer. The authors read optimal−1's poor showing as a test of "the offloading hypothesis".
  - A repeated-measures logistic regression of choosing the optimal length on trial had a positive slope (p < .001). But "eight participants became less likely to select the boundedly optimal strategy as trials progressed" and four others "persistently selected a list length that was not bounded optimal."
  - Individual cases: optimal lengths of 4, 5, 6 and 7 in different participants were each chosen; participant 14's chosen length became optimal through practice; participant 5 had no distinct optimum; participant 8 chose 6 when 4 was optimal with probability about 0.5.
- **Experiment 2** (N = 20, 10 per group). Manipulation: points schedule, with zero points for wrong items. Linear: one point per correct item, 200 points per phase. Exponential: trial points for 1 to 9 correct items of 1, 2, 3, 4, 7, 11, 17, 27, 42, target 310 points per phase. Choice-phase analysis uses trials 1–39.
  - Chosen length 6.99 (SD 1.32) Exponential vs 5.07 (SD 0.78) Linear, t(18) = 3.98, p = .001, d = 1.33; modes 7.20 vs 4.90.
  - Correlation of B_p with chosen length: r(18) = .77, p < .001, RMSE 1.34, "59.29% of the variance".
  - Probability selected and probability optimal correlated, r(18) = .62, p = .003, but people chose their favourite more often than matching predicts (permutation test p < .001).
  - B_p predicted 46% (SD 33) of selections, optimal−1 12% (SD 13), optimal+1 14% (SD 17); B_p beat each (p = .003, p = .004). No effect of trial on B_p's hit rate (p = .1285).
  - 12 of 20 chose the optimal length on most trials, 2 alternated among indistinguishable lengths, 6 systematically chose another length (4 larger, 2 smaller, all within ±2).
  - A strategy change the list-length space does not contain: on 49% of Exponential trials (17% Linear) participants first typed only the first letter of each name in every box, then went back to complete them; mean chosen length was larger with this strategy (6.65 vs 5.46, t(23) = 2.10, p < .05, d = .80).
- **Across both experiments**, "13 (of 60) participants in the two studies who persistently selected a list length, and therefore a strategy, that was not bounded optimal", 10 of them "usually by 1 more memory item". Offered explanations, none tested: poor discrimination of utility, practising a strategy in the expectation it will become optimal, or stable suboptimality in the sense of Fu and Gray (2004).
- **What is not in the paper.** No computational model of memory, no capacity parameter, no look-up time, no fitted parameters. The fit statistics are correlations and hit rates between each person's empirical argmax and their choices. The phrase "The theory makes predictions that are tested against data, not fitted to it" means the prediction comes from the no-choice data, not from a model.
- **A small discrepancy.** The paper describes Gray et al. 2006's lockout as "a period of 0–3,000 ms"; that paper's Experiment 3 ran to 3,200 ms (as read for [LIT-tmpras8t](../literature.d/LIT-tmpras8t.md)).

## Bearing on the record

**On what the record says of this work.** [LIT-tmpjg8mc](../literature.d/LIT-tmpjg8mc.md)'s summary, following Lieder and Griffiths ([LIT-tmppqntw](../literature.d/LIT-tmppqntw.md), [NOTE-tmpmd0yp](NOTE-tmpmd0yp.md)), says bounded optimality "predicts how many items a person commits to memory from the cost of misremembering, working memory capacity, and how long it takes to look up forgotten information", and [NOTE-tmpmd0yp](NOTE-tmpmd0yp.md) and [LIT-tmppqntw](../literature.d/LIT-tmppqntw.md) call it a "memorize-or-look-up trade". The paper does not bear that out. (1) There is no look-up. Names are shown once, in sequence, and the email cannot be consulted during recall; the alternative to holding more in memory is a shorter trial and more of them, each paying the inter-trial overhead. Look-up time appears nowhere in the paper, as a parameter or as a manipulation. (2) Working memory capacity is not a parameter. It enters only as each person's measured rate curve over list lengths. (3) The cost of misremembering was manipulated in Experiment 1 and had no effect on choice (5.05 vs 5.00); what moved choice was the reward schedule for long lists in Experiment 2. Lieder and Griffiths' sentence is a fair description of what the empirical rate curve implicitly reflects, not of a model the paper states. The paper also does not set "internal storage against retrieval from the environment" in the sense [NOTE-tmpmd0yp](NOTE-tmpmd0yp.md) gives; it sets memory load against the overhead of more trips, with the world holding nothing that can be re-read.

**For [QUESTION-tmp1mkzc](../questions.d/QUESTION-tmp1mkzc.md).** The task is the question's fourth strategy, defer and re-read, with the re-read removed: items arrive once and are either held or lost, and the choice is batch size. Measured against the terms the question's 2026-10-15 note lists:

- **Predictability of the later query: not a term.** The query is fixed and known (copy these names in order, immediately), as in Gray et al. 2006.
- **Retrieval cost including search: absent.** There is no external retrieval, so no look-up cost and no search. Internal retrieval is not modelled; its time and failures are folded into the measured rate.
- **Staleness or bias on reuse: absent as staleness, present as error.** A misremembered name is a wrong stored item, and its cost is priced in time: zero points for that item, or for the whole trial under High Error Cost. This is the nearest the paper comes to a cost for a stored result being wrong, and it is the term Gray et al. 2006's model lacked (there, retrieval only fails). But the error is within seconds and from memory decay or interference, not from the world changing, and the manipulation of its price did not change behaviour.
- **Expected reuse: absent.** Each name is copied once and names are redrawn each trial; nothing stored serves a later trial. What carries across trials is the person's knowledge of their own rate per strategy, the analogue of Gray et al.'s Q-table, which the paper treats as experience, not as an amortized cost.
- **Erosion of the alternative: absent, and the data show the opposite effect.** Practice made strategies better: participant 14's chosen length "became the boundedly optimal list length", and the authors suggest some suboptimal choices were bets that practising a length "would make the strategies optimal". Strengthening the practised route is the mirror of Risko and Gilbert's erosion of the unpractised one ([LIT-tmpbhj79](../literature.d/LIT-tmpbhj79.md)); neither is a term here.
- **Precomputation and storage/upkeep: absent.** Nothing is computed ahead; storage is short-term memory for seconds.

Against the earlier readings: Gray and Fu 2004 ([LIT-tmpbbd7f](../literature.d/LIT-tmpbbd7f.md)) and Gray et al. 2006 ([LIT-tmpras8t](../literature.d/LIT-tmpras8t.md)) manipulated the cost of access to information that stays in the world and, in 2006, fitted a parametric model (ACT-R memory equations, Q-learning on time) to group means. This paper keeps their conclusion, that people neither minimize memory nor favour the world but trade by payoff, and moves the test to the individual: B_p beat optimal−1 and optimal+1 in both experiments, and the correlation of B_p with choice was r = .35 and r = .77. It does so by dropping the model, so it adds no cost terms the earlier papers lacked except the price of a wrong item. It is evidence that a person can find the best point of their own head-versus-trips trade-off at the scale of seconds, which supports the form of the owner's conjecture (one currency, choose by rate) for a single strategy; it does not supply a cost model, and it says nothing about the four strategies being regimes of one trade. The record's description of it as the head-versus-world trade with a look-up cost should be corrected.
