---
number: 864
status: Read
formerly:
- NOTE-tmp0wp7e
paper: LIT-1058
title: Gray & Fu — Soft constraints in interactive behavior
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full 2026-10-15 from the publisher's typeset PDF (Elsevier, Cognitive
    Science 28(3), pp. 359–382, 24 pp.; PDF metadata title doi:10.1016/j.cogsci.2003.12.001,
    created 2004-05-18), as posted on a Drexel University course page (www.cs.drexel.edu/~dds26/courses/cs680-s11/BK/readings/Gray-CS04.pdf;
    SHA-256 a57bf51e…cbc262). The authors' own copy (www.rpi.edu/~grayw/pubs/papers/GF04_SoftConstraints-CSj.pdf,
    which OpenAlex lists through CiteSeerX, and which Gray's ACT-R-users announcement
    of 2004-05-20 says was available from his website) could not be reached: homepages.rpi.edu
    returned proxy 502, and the Internet Archive capture of 2004-11-15 could not
    be fetched (connection reset, about ten tries). So the course copy could not
    be compared against the authors' file. Unpaywall and OpenAlex report the work
    closed; Wiley, ScienceDirect and DTIC (ADA461208) returned 403. Text extracted
    with pdftotext (layout and raw). Figures 4, 5 and 6 carry their values only
    as plots, so the page images were viewed and values read from them are marked
    approximate. Read: abstract, all six sections, both experiments, the notes,
    the acknowledgements and the reference list. Nothing skipped. The supplementary
    ACT-R model files (Cognitive Science Society annex) and the CHI 2001 version
    (Gray & Fu 2001) were not read. Every quotation of the paper below was checked
    against the extracted text by script, with whitespace and typographic quotes
    normalised; the one other quotation is of the LIT entry's own summary.
date: '2026-10-15'
summary: >-
  In a simulated VCR-programming task, people with show information always available
  on screen still made errors that comparing against the display would have prevented.
  Making that information cost a mouse move and click instead of an eye movement
  (an estimated 1,000–1,500 ms against 500 ms) cut how often they looked it up,
  and most checks came right before a setting, almost none while or after setting
  it. The group made to memorize the information first made the fewest errors. Gray
  and Fu read this as non-deliberate least-effort choice among microstrategies,
  with memory time and perceptual-motor time weighed alike ("milliseconds matter").
  The access costs are model estimates, not measured or varied parametrically. The
  error difference between the two on-screen conditions was not significant, the
  free-access look-up data come from a separate eye-tracking study of eight people,
  and the Memory-Test condition differed from the others in more than retrieval
  cost.
---
<!-- inactive-ok-file: CLAIM-296 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# NOTE-864: Gray & Fu — Soft constraints in interactive behavior

## Contribution

An argument, with two experiments, that the choice between taking information from the world and recalling it is a cost comparison made below deliberation, and that the comparison gives no special weight to perception and action over memory. The paper sets this against the "minimum memory strategy" it attributes to Ballard and colleagues and to Wilson (2002), and against the design slogan "put knowledge in-the-world". Hard constraints, the ones a device's design builds in, fix which patterns of behaviour are possible. Soft constraints, which come from the relative effort of those patterns, decide which pattern is chosen. The authors estimate the effort of each route in milliseconds, derive ordinal predictions for errors and for how often the information is looked up, and test them.

## Key insight

Perfect information in the world does not get used just because it is there. If reaching it costs more than recalling a weak, noisy memory of it, people recall, and the gap only needs to be a few hundred milliseconds. Errors then follow from relying on memory that is cheap and wrong. The paper puts it as: "Soft constraints can work contrary to the designer's intentions by making the access of perfect knowledge in-the-world more effortful than the access of imperfect knowledge in-the-head." The conclusion runs both ways: "the most adaptive pattern of interactive behavior is one that is the least effort given the current task and the current task environment." Strong memory, as in the Memory-Test group, beats a world that is cheap to read.

## Assumptions

- **Selection is non-deliberate and minimizes effort.** "When selection is non-deliberate or automatic the least effort microstrategy is chosen." Effectiveness is set aside: "we ignore effectiveness to focus on how considerations of effort lead to the selection of alternative microstrategies." The rational-analysis framing (Anderson 1990) brings in expected utility, but only the effort term is used.
- **Time stands in for effort, whatever fills it.** The "auxiliary assumption": "time is a reasonable surrogate for measuring cognitive as well as perceptual-motor effort", for patterns lasting 500 to 1,000 ms. It is not tested directly; the authors take support for the predictions as indirect support for it.
- **Two of four cost components are ignored.** Of perceptual-motor search, perceptual-motor access, memory encoding and memory retrieval, only access and retrieval are compared. There is no search because the window and fields never move: "during the study there is no perceptual-motor search, only perceptual-motor access." Encoding is ignored because the Memory-Test group pays it before the trial, and because for the other groups a weak trace is assumed to be encoded during the eye or mouse movement back to the VCR.
- **A modal memory model.** Retrieval is cued; cues need not pick out one memory; strength sets order, probability and speed of recall; and memory is noisy, so a wrong trace can sometimes be retrieved faster than the right one. "This last assumption conspires to give lie to the certainty of knowledge in-the-head."
- **The effort figures are estimates from models, not measurements** (Table 1). Perceptual-motor access: 500 ms for Free-Access; 1,000–1,500 ms for Gray-Box and Memory-Test. Memory retrieval: 500–1,000 ms for a weak memory (Free-Access, Gray-Box), from Anderson and Lebiere's (1998) upper bound for one retrieval attempt; 100–300 ms for a strong memory (Memory-Test), from Altmann and Gray (2002) and Byrne and Anderson (2001).
- **The predictions are ordinal.** Errors: Gray-Box most, Memory-Test least, Free-Access between. Look-ups: Free-Access more than Gray-Box, both more than Memory-Test.

## Key results

**The task.** A simulated commercial VCR, built in Macintosh Common Lisp. To program a show, eight fields are set (day-of-week, channel, start hour, start 10-min, start minute, and the same three for the end), plus clock and record steps, following the task-to-device rule hierarchy of Fig. 1. The show's start time, end time, day and channel sit in a Show Information Window below the VCR. The task was chosen so that keeping information in memory is optional: "Information from the world could be obtained, used immediately, and then forgotten." After practice on show 0, each subject programmed shows 1–4, each to a criterion of two successive correct trials, with feedback on the first error after each trial. All 80 subjects shown Fig. 1 used that hierarchy for the next four shows.

**The access-cost manipulation (experiment 1, 72 undergraduates, 24 per condition, about 30 min).**
- *Free-Access:* the information fields are visible throughout; reaching them is an eye movement, estimated at 500 ms (an ACT-R 5.0 model gives 470 ms).
- *Gray-Box:* the field labels are visible, but each value is under a gray box that has to be clicked, and stays visible only while the cursor is in the field. Estimated 1,000–1,500 ms (a CPM-GOMS model, Fig. 2, gives 1,280 ms; the ACT-R model with a mouse move and click added gives 1,120 ms).
- *Memory-Test:* before each trial the subject must set the show information from memory in pop-up menus, alternating with the information window until correct. During the trial the fields are under gray boxes, and moving the cursor out of the VCR window covers the VCR with a black box until the subject clicks back on it. The group was also told not to use the window.

These millisecond figures are the authors' estimates of what each arrangement costs. Response times for look-ups were not reported, and cost was not varied beyond the three arrangements.

**Errors: trials-to-criterion** (more than two trials per show means trials ended wrong). Condition: F(2, 69) = 4.48, p = .015 (MSE = 10.04). Show: F(3, 207) = 5.90, p = .0007. Interaction: F < 1. Planned comparisons: Gray-Box vs Memory-Test p = .0002; Free-Access vs Memory-Test p = .037; Free-Access vs Gray-Box not significant. Read from Fig. 4 (approximate): Gray-Box about 4.5, 4.3, 3.8, 2.6 trials for shows 1–4; Free-Access about 4.3, 3.1, 2.6, 2.9; Memory-Test about 3.2, 2.4, 2.0, 2.1. The paper gives no error rates as percentages.

**Errors: goal suspensions** (a setting begun and dropped before finished, on trials that ended correct). 36,877 clicks on correct trials, parsed into 12,560 goals; 122 (under 1%) were suspensions. Overall ANOVA F(2, 69) = 2.64, p = .078 (marginal); Gray-Box more than Memory-Test by planned comparison, no other pair different. Means from Fig. 5, approximately: Free-Access 1.6, Gray-Box 2.7, Memory-Test 0.8 per subject. Subjects making any suspension: Free-Access 50%, Gray-Box 75%, Memory-Test 42% (χ², p = .05).

**How often the display was used instead of memory.**
- Gray-Box: 293 clicks on information fields over 223 correct trials, "an average of 1.31 checks per show" (the arithmetic is per correct trial).
- Memory-Test: 10 clicks over 205 correct trials, 0.05. The authors take this as showing the group "almost exclusively relied on retrievals from memory".
- When Gray-Box subjects looked (Fig. 6A, categories F(4, 92) = 15.36, p < .0001): about 0.65 accesses per trial right before programming the setting, and roughly 0.0–0.15 before, during ("middle"), right after or after. Right-before is greater than every other category, which do not differ from one another. So checks of a setting once made rested on memory: "Any verifications of the correctness of their settings that the Gray-Box group is doing must be based on retrieval of imperfect knowledge in-the-head, not on a comparison with perfect knowledge in-the-world."
- Free-Access (experiment 2: eye tracking, ASL 504, the first eight subjects who could be tracked, Show Information Window enlarged): categories F(4, 28) = 5.38, p = .002. About 1.25 before, 1.3 right before, 0.4 middle, 0.6 right after, 1.3 after (Fig. 6B). Middle is lower than before, right before and after, and right after is marginally lower. Middle and right-after accesses average "approximately 1/2 an access per person per trial".
- Across experiments, "the experiment 2 Free-Access group is 4.3 times more likely to access information than is the Gray-Box group". This compares eye fixations of eight subjects with mouse clicks of 24, in different studies; the general discussion calls it "Eyeballing". It is not a tested contrast.

**Fit to predictions.** The predicted rank order for errors (Memory-Test best, Gray-Box worst) held on both error measures, but only the contrasts with Memory-Test were significant. The look-up ordering held descriptively. The authors' conclusion: "Unless our estimates of the duration of memory and perceptual-motor processes are way off, the success of our predictions suggests that the time spent retrieving something from memory is weighed the same as time spent in perceptual-motor activity."

**ACT-R modelling.** The ACT-R 5.0 work in the paper is small. One model moves visual attention to a location and returns what is there (470 ms); a version with an added mouse move and click gives 1,120 ms. These supply effort estimates for Table 1, and Note 1 points to the Lisp files and a workbook of "estimates of effort after 1, 10, 100, and 1,000 cycles". There is no ACT-R model of the choice between memory and display, no utility-learning or conflict-resolution model of the tradeoff, and no simulation of the error or access data. The cost comparison is worked by hand from Table 1. The claim that selection is "a non-deliberate process at the neuronal or subsymbolic level (Anderson & Lebiere, 1998)" is a framing, not a model.

**Limits the authors state.** Real interfaces often charge much more to reach information in the world (crossing a room, or searching a busy web page), so "for much routine interactive behavior, we would expect the effort-benefit tradeoff to favor accessing imperfect knowledge in-the-head over perfect knowledge in-the-world." They accept that results would change with non-linguistic information or a different amount of it, and that the title misleads, "as once information is acquired via the perceptual-motor system it is then in-the-head not in-the-world."

**Limits not stated.** The Memory-Test group differs from Gray-Box in more than retrieval strength. It had a study-and-test phase before every trial, a black box penalizing any glance away from the VCR, and an instruction not to use the window. Its advantage cannot be credited to retrieval cost alone. Free-Access look-ups were never measured in experiment 1.

## Bearing on the record

**[QUESTION-095](../questions.d/QUESTION-095.md).** The paper prices only the read-back side of the trade. It compares the cost of reaching a result left in the world (perceptual-motor access) with recalling it, and explicitly sets aside encoding, the cost of putting the result in the head, and search. That excludes the precompute and storage terms of the candidate cost model. It does show that retrieval cost governs whether a stored result gets used: a result left in the world is used only when reading it costs less than recall, and a gap of a few hundred milliseconds is enough to lose it. Staleness also appears, in a form close to the question's: cheap recall returns a value from an earlier show or another field ("competing memories for information from older shows or other fields"), and the subject acts on it. The Memory-Test condition is the nearest thing to amortization in the paper. Paying a large encoding cost before the trial bought fast, accurate retrieval and the fewest errors. But because the paper sets encoding aside and confounds that condition, it does not measure when such prepayment is worth it. The paper does not join this to amortized inference, which it does not mention. It supports the question's premise that retrieval cost counts as computation ("milliseconds matter and they matter the same regardless of the type of activity"). It does not supply the unified model.

**[CASE-085](../cases.d/CASE-085.md).** The paper fits only part of this case, and in one respect points the other way. Its task holds location fixed and known, and it removes search by design. The EMT case is a failure of search for an item whose location was not recalled quickly enough. Gray and Fu's subjects relied on cheap recall of a value and went wrong; the EMT relied on recall of a location, could not get it, and the search that replaced it ran out the deadline. What the paper adds is a mechanism for how the reliance arises: when an earlier check of the unit was cheap and re-checking costs more, the system leans on a weak memory trace and does not refresh it. The case does not show that this happened. The paper's Memory-Test result also cuts against reading the case as showing that memory is the weaker route. Strong, recently tested memory was the most reliable source in the study.

**[TERM-055](../terms.d/TERM-055.md).** Consistent with it, and it supplies a measured instance of α depending on the arrangement: the same information, in the same place, is used less often when a click is added. It also supports the note of 2026-10-15 on retrieval done before the request. The Memory-Test group paid its retrieval work before the trial and was faster and more accurate. The paper's cost decomposition (search, access, encoding, retrieval) is a candidate breakdown of what the procedures π in α's supremum cost. But α as defined is a supremum over available procedures, and Gray and Fu's point is that the procedure actually chosen is the cheap one, not the best. So the realized chance of deploying a resource can fall well below α. If the term is revised, that gap between the best available procedure and the one selected by effort is worth making explicit.

**[CLAIM-296](../claims.d/CLAIM-296.md).** Supports it on the clause the cockpit note found hard to evidence with measurements. With the people, the information and its location fixed, a small change in arrangement (a gray box over a field) changed how often the information was used, and, against Memory-Test, how many errors were made. Possessing the information (on screen, perfect) and knowing where it is (fixed, learned) did not secure its use. Two cautions. The differences in errors between the two on-screen arrangements were not significant, so what moved with arrangement alone is look-up behaviour, more firmly than performance. And the paper's framing is individual cognition choosing microstrategies, not a distributed system, though its conclusion, "Soft constraints are imposed by the designer on the user.", places part of the cause in the environment.

**The LIT entry's provisional summary** ("people use the cheaper, less reliable memory instead, by milliseconds of cost") is right in direction but needs three corrections. The millisecond costs are model estimates, not manipulated values. The significant error effects are all contrasts with the group that memorized, not between the two levels of world-access cost. And the paper's strongest performers relied on memory.
