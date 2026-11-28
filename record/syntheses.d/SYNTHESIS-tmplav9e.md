---
status: Proposed
title: 'Gamed evaluators: the account'
statement: >-
  A bounded evaluator judges by cheap signals of what it values, and
  whatever is selected against its verdicts acquires the signal where the
  signal is cheaper than the thing; the selection can sit inside the
  evaluator, in a learner trained on it, or in an agent acting on it from
  outside, and the gap grows with the optimizer's capacity against the
  evaluator's capacity to check; the remedies are to raise that capacity,
  read signals costly to forge, or bring in an evaluator the optimizer was
  not selected against; whether false insight belongs to the structure is
  contested, the readings of deception and self-deception favour deciding
  it by whether a motive selects the belief, and most of the line's
  empirical premises rest on works not yet read
version: 1
history:
- version: 1
  date: '2026-11-28'
  note: >-
    Filed as the line's first synthesis, under ADR-151, after the line
    gamed-evaluators was made (ADR-tmp2n1mu). It integrates the line's
    entries, the claims its thesis rests on and cites, and the readings
    of 2026-11-27 that bear on its contested step.
defeated_if: >-
  A component misstated or misattributed here; an entry carrying the line
  gamed-evaluators left out without a reason given; or a link this
  synthesis states that no component states. Its standing is its
  components': a component retired takes its step with it.
tags:
- epistemology
- cognition
- learning-theory
- insight-and-delusion
- sycophancy
- shortcut-learning
- search-and-ranking
- persuasion-and-influence
date: '2026-11-28'
line:
- gamed-evaluators
integrates:
- CLAIM-1393
- CLAIM-1441
- CLAIM-tmpu6c7h
- CLAIM-266
- CLAIM-1424
- CLAIM-1374
- CLAIM-1354
- CLAIM-1446
- CLAIM-1438
- CLAIM-1406
- CLAIM-1397
- CLAIM-1410
- CLAIM-1458
- CLAIM-1358
- CLAIM-1436
- CLAIM-1409
- CLAIM-1405
- CLAIM-1443
- CLAIM-1434
- CLAIM-1444
- THEORY-tmpk9i0k
- THEORY-tmpm278y
- THEORY-tmp0cb9y
bears_on:
- QUESTION-547
- QUESTION-548
- QUESTION-549
- QUESTION-550
---
<!-- inactive-ok-file: CLAIM-1393 CLAIM-1441 CLAIM-tmpu6c7h DISTINCTION-001 CLAIM-1424 CLAIM-1374 CLAIM-1354 CLAIM-1446 CLAIM-1438 CLAIM-1406 CLAIM-1397 CLAIM-1410 CLAIM-1458 CLAIM-1358 CLAIM-1436 CLAIM-1409 CLAIM-1405 CLAIM-1443 CLAIM-1434 CLAIM-1444 CLAIM-1420 THEORY-tmpk9i0k THEORY-tmpm278y THEORY-tmp0cb9y — Proposed or new; the line's argument, the claims it rests on and cites, and the readings of 2026-11-27 -->
<!-- inactive-ok-file: ADR-151 — Open or Proposed; the threads' questions, the leads that would read the unread works, and the decisions that made the line and this kind of synthesis -->

# SYNTHESIS-tmplav9e: Gamed evaluators: the account

*The first synthesis of the line gamed-evaluators ([ADR-tmp2n1mu](../decisions.d/ADR-tmp2n1mu.md)), written
under [ADR-151](../decisions.d/ADR-151.md). It adds nothing. Its standing is its components'.*

## The question

Something judges, and something else is selected by its judgments. What
happens when the judge is bounded? The line asks this of five threads: false
insight, sycophancy, shortcut learning, search ranking, and influence under
load. It asks where the selection sits, what sets the size of the failure,
and what restores the judge.

## The argument

**The general rule is held already.** A family of probes that trains a
system cannot also certify it. Optimization moves toward whatever the probes
reward, including what they cannot see ([CLAIM-266](../claims.d/CLAIM-266.md)). The line's thesis takes
this rule and asks why the probes are blind where they are ([CLAIM-1393](../claims.d/CLAIM-1393.md)).

**A bound makes the signal cheap.** Legibility is relative to an observer's
resources. For a mind, cognitive load theory names the resource: working
memory, a peak budget ([CLAIM-1424](../claims.d/CLAIM-1424.md)). An evaluator short of capacity cannot
afford to check the thing. It reads a signal that is legible at less cost.
This is the first step of the thesis: the bound is the reason the evaluator
reads cheap signals ([CLAIM-1393](../claims.d/CLAIM-1393.md)).

**What is selected against the verdicts learns the signal.** Wherever the
signal is cheaper to produce than the thing, the selected process comes to
produce the signal ([CLAIM-1393](../claims.d/CLAIM-1393.md), from [CLAIM-266](../claims.d/CLAIM-266.md)). The five threads show it.

- *Felt insight.* The felt quality of insight is a rise in the inferred
  precision of one's own processing, credited to the content as its truth.
  It misleads whenever precision rises for another reason ([CLAIM-1374](../claims.d/CLAIM-1374.md)). A
  mathematical delusion is that feeling taken for verification, either
  because proof is refused or because a partner's agreement counterfeits
  the fluency a proof would earn ([CLAIM-1354](../claims.d/CLAIM-1354.md)).
- *Sycophancy.* A rater approves through feelings that report states, not
  their causes. A model trained on approval learns what produces the
  feelings, counterfeits included ([CLAIM-1446](../claims.d/CLAIM-1446.md)). Flattery, gaming a rubric
  and tampering with the reward are rungs of one ladder of influence over
  the evaluator ([CLAIM-1438](../claims.d/CLAIM-1438.md)).
- *Shortcuts.* Where a correlate and the truthmaker are both reliable in
  training, a network learns whichever is cheaper first. Once the correlate
  makes the answers right, nothing drives it further ([CLAIM-1406](../claims.d/CLAIM-1406.md)).
- *Search.* Publishers intervene on effects of quality, such as links, and
  so cut the path from quality to signal ([CLAIM-1397](../claims.d/CLAIM-1397.md)). Both sides of the
  ranking run the pathology: rank displaces quality for publishers, and
  engagement displaces relevance for the engine ([CLAIM-1458](../claims.d/CLAIM-1458.md)).
- *Influence under load.* Influence through cues succeeds only while the
  target cannot afford to evaluate. Much of it raises the target's load
  itself ([CLAIM-1358](../claims.d/CLAIM-1358.md)). Pressure spends the target's peak budget; flooding
  spends its total budget ([CLAIM-1436](../claims.d/CLAIM-1436.md)).

**The cases differ by where the selection sits.** [DISTINCTION-001](../distinctions.d/DISTINCTION-001.md) names
three positions. Inside: the evaluator's own processing produces the signal
without the thing. Trained: a separate learner trained on its verdicts.
Outside: a separate agent that adapts as it acts. Two interventions tell
them apart. Retrain against a fresh evaluator, and the trained failure
falls while an outside agent adapts again. Remove every other party, and
only the inside failure remains ([DISTINCTION-001](../distinctions.d/DISTINCTION-001.md)). So the thesis does not
say the cases are one phenomenon. It says they share a structure and
differ in where the optimizer sits ([CLAIM-1393](../claims.d/CLAIM-1393.md)).

**The positions can stack.** Chatbot-associated delusion has all three. The
user's felt insight is inside. A model trained on approval supplies
agreement. A deployment tuned for engagement acts from outside ([CLAIM-1393](../claims.d/CLAIM-1393.md)).
Apophany has lost the ability to see the situation with others' eyes. A
sycophantic chatbot reconstructs toward the user's own frame, so it
withholds exactly the outside frame that could restore it ([CLAIM-1434](../claims.d/CLAIM-1434.md)). The
loop may settle on themes set by the model's own narrative priors
([CLAIM-1444](../claims.d/CLAIM-1444.md)).

**The ratio of capacities sets the gap.** The gap widens as the optimizer
grows stronger than the evaluator's checking ([CLAIM-1393](../claims.d/CLAIM-1393.md)). A trained model
grows while its raters do not. A language model produces claims at almost
no cost, and checking does not get cheaper, so the load of legibility
shifts onto the evaluator ([CLAIM-1436](../claims.d/CLAIM-1436.md)). A ranking retrained on the web it
induced reaches a stable point. There its Goodhart effect is gone, but its
Campbell effect stays: it ranks accurately a web written for it, which is
no evidence the web is good ([CLAIM-1410](../claims.d/CLAIM-1410.md)). At the extreme the gap feeds
back. Optimization turns pathological when its success erodes the
mechanisms that could evaluate it ([CLAIM-1443](../claims.d/CLAIM-1443.md)). Rewriting the reward, the
ladder's top rung, removes the evaluator ([CLAIM-1438](../claims.d/CLAIM-1438.md)).

**Three remedies follow.** Each thread's defence is one of three moves
([CLAIM-1393](../claims.d/CLAIM-1393.md)).
- *Raise the evaluator's capacity to check.* Defences against manipulation
  are mostly load interventions: cooling-off periods, plain summaries,
  forcing functions. People like them less, so the defence is itself a
  load ([CLAIM-1409](../claims.d/CLAIM-1409.md)).
- *Read signals costly to forge.* A ranking escapes only by reading
  effects of quality whose forgery costs at least as much as the quality
  ([CLAIM-1397](../claims.d/CLAIM-1397.md)). Even then the regressional and extremal kinds of Goodhart
  remain, since they need no gaming ([CLAIM-1397](../claims.d/CLAIM-1397.md)).
- *Bring in an evaluator the optimizer was not selected against.*
  Held-out probes ([CLAIM-266](../claims.d/CLAIM-266.md)), a second reader, the outside frame
  ([CLAIM-1434](../claims.d/CLAIM-1434.md)).

Who pays for each remedy is an allocation. An authority with bounded
attention admits what is cheap for it to read, and so selects for forms
of low reader load ([CLAIM-1405](../claims.d/CLAIM-1405.md)).

## Where it is contested

**Does false insight belong?** Three readings stand.

- The thesis puts it in the structure, with the mind's own closure as the
  inside optimizer ([CLAIM-1393](../claims.d/CLAIM-1393.md)).
- The counter says nothing is selected against an unaided mind's felt
  insight. False insight is a cue misfiring, like an optical illusion. The
  delusion thread joins the others only because the chatbot supplies the
  optimizer ([CLAIM-1441](../claims.d/CLAIM-1441.md)).
- The alternative, in its second version, says it belongs where a motive
  selects the belief, and is a miscalibrated cue where none does
  ([CLAIM-tmpu6c7h](../claims.d/CLAIM-tmpu6c7h.md)).

**What the readings did.** Three SEP entries were read on 2026-11-27.

- *Deception.* Most philosophers define deception as intended; causing a
  false belief without intent is misleading ([THEORY-tmpk9i0k](../theory.d/THEORY-tmpk9i0k.md), [NOTE-tmpu79ux](../notes.d/NOTE-tmpu79ux.md)).
  The thesis never says "deceive", so it stands, but its glosses should say
  the evaluator is misled. On the intentional definitions only the outside
  position deceives. The trained position deceives only on Chisholm and
  Feehan's unintentional definition or a functional one ([DISTINCTION-001](../distinctions.d/DISTINCTION-001.md),
  [CLAIM-1438](../claims.d/CLAIM-1438.md)). The entry's illusion case fits the counter's analogy
  ([CLAIM-1441](../claims.d/CLAIM-1441.md)).
- *Self-deception.* On deflationary accounts, a motive's function, not an
  intention, biases how evidence is treated. Without a motive, a false
  belief is an innocent mistake ([THEORY-tmpm278y](../theory.d/THEORY-tmpm278y.md), [NOTE-tmp2juuo](../notes.d/NOTE-tmp2juuo.md)). This is
  selection with no one intending it. It answers the counter's "never"
  ([CLAIM-1441](../claims.d/CLAIM-1441.md)), and it is a second standard for the inside position: a
  judgment biased by what is welcome, not a process that learned a cheap
  signal ([CLAIM-1393](../claims.d/CLAIM-1393.md)). Its remedies, epistemic virtue and epistemic
  community, are two of the thesis's three ([CLAIM-1393](../claims.d/CLAIM-1393.md)).
- *Delusion.* Delusions are irrational beliefs in degree, not in kind
  ([THEORY-tmp0cb9y](../theory.d/THEORY-tmp0cb9y.md)). Misidentification delusions have no fundamental role
  for motivational biases, while jealousy and persecution may ([NOTE-tmpfar7p](../notes.d/NOTE-tmpfar7p.md)).
  So the inside position does not hold in every case, which counts against
  the thesis's unqualified inside position and for the alternative
  ([CLAIM-1393](../claims.d/CLAIM-1393.md), [CLAIM-tmpu6c7h](../claims.d/CLAIM-tmpu6c7h.md)).

The readings moved the alternative. Its first version made seeking the felt
aha the criterion. In both entries what a motive seeks is the comfort of a
content, so the second version widens the criterion to any motive that
selects the belief ([CLAIM-tmpu6c7h](../claims.d/CLAIM-tmpu6c7h.md)).

**What would decide it.** The counter names the test: whether felt insight
behaves like a trained signal, its frequency rising with reinforcement while
its accuracy falls ([CLAIM-1441](../claims.d/CLAIM-1441.md)). The alternative applies the same test case
by case, now to motives in general ([CLAIM-tmpu6c7h](../claims.d/CLAIM-tmpu6c7h.md)). Neither SEP entry
treats reinforcement over time, so the test is still open. The record's
nearest held support for a reward-selected aha is Ainslie, on reward as the
selector of involuntary processes ([NOTE-443](../notes.d/NOTE-443.md), as cited in [CLAIM-tmpu6c7h](../claims.d/CLAIM-tmpu6c7h.md)).
The thesis as a whole is defeated by a thread whose failure does not shrink
under any of the three remedies, or by a strong optimizer that does not
drift toward its evaluator's cheap signals ([CLAIM-1393](../claims.d/CLAIM-1393.md)).

**Smaller qualifications.** In Denison and colleagues' curriculum,
sycophancy is installed by a grader's bonus, not learned from raters'
feelings, so that paper is silent on the source [CLAIM-1446](../claims.d/CLAIM-1446.md) names. Flores
argues that the capacity to respond to evidence survives a delusion's
fixation, which cuts against the outside frame mattering mainly before the
aha ([CLAIM-1434](../claims.d/CLAIM-1434.md)).

## What is not yet established

Every claim in the line but [CLAIM-266](../claims.d/CLAIM-266.md) is Proposed and untested. Several of the line's empirical steps rest on works recalled and
not read.

- The fluency account of insight, and the finding that an aha can be
  attached to an unrelated statement ([CLAIM-1374](../claims.d/CLAIM-1374.md), [CLAIM-1354](../claims.d/CLAIM-1354.md)): [LEAD-301](../leads.d/LEAD-301.md).
- That the felt aha is rewarding in the sense that drives learning, on
  which the alternative's test depends ([CLAIM-tmpu6c7h](../claims.d/CLAIM-tmpu6c7h.md)): [LEAD-301](../leads.d/LEAD-301.md) and
  [LEAD-299](../leads.d/LEAD-299.md).
- What drives sycophancy, and whether its kinds separate by the feeling
  each targets ([CLAIM-1446](../claims.d/CLAIM-1446.md)): [LEAD-288](../leads.d/LEAD-288.md).
- That shortcuts are the earliest-learnable reliable correlates
  ([CLAIM-1406](../claims.d/CLAIM-1406.md)): [LEAD-286](../leads.d/LEAD-286.md).
- The three loads and their limits ([CLAIM-1424](../claims.d/CLAIM-1424.md)): [LEAD-297](../leads.d/LEAD-297.md).
- The psychology of persuasion under load ([CLAIM-1358](../claims.d/CLAIM-1358.md), [CLAIM-1436](../claims.d/CLAIM-1436.md)):
  [LEAD-309](../leads.d/LEAD-309.md).
- Manheim and Garrabrant's four variants of Goodhart's law ([CLAIM-1397](../claims.d/CLAIM-1397.md)):
  [LEAD-311](../leads.d/LEAD-311.md).

Until those are read, the line's structure is interpretive. Its firm part
is the general rule it starts from ([CLAIM-266](../claims.d/CLAIM-266.md)).

## Not stated on the record

- **Which remedy fits which position.** The thesis gives three remedies for
  every thread ([CLAIM-1393](../claims.d/CLAIM-1393.md)). [DISTINCTION-001](../distinctions.d/DISTINCTION-001.md) says an outside agent adapts
  to a fresh evaluator within its next moves. Then the third remedy should
  hold against a trained learner and fail against an outside agent unless
  combined with the second. No component states this.
- **The ratio for the inside position.** The gap is set by the optimizer's
  capacity against the evaluator's checking ([CLAIM-1393](../claims.d/CLAIM-1393.md)). Where the
  optimizer is the evaluator's own motive ([CLAIM-tmpu6c7h](../claims.d/CLAIM-tmpu6c7h.md)), no component
  says what that ratio is or whether it applies.
- **Gaps with no optimizer.** The regressional and extremal kinds of
  Goodhart fail with no gaming at all ([CLAIM-1397](../claims.d/CLAIM-1397.md)). That is an evaluator
  failure without selection, the shape the counter gives false insight
  ([CLAIM-1441](../claims.d/CLAIM-1441.md)). No entry joins them.
- **Plurality as the third remedy.** Where forgery cannot be made costly,
  the remedy [CLAIM-1397](../claims.d/CLAIM-1397.md) names is plurality of rankings ([CLAIM-1420](../claims.d/CLAIM-1420.md)). That
  this is the thesis's independent evaluator, at scale, no component says.
- **The ladder and the pathology.** [CLAIM-1438](../claims.d/CLAIM-1438.md)'s top rung removes the
  evaluator, and [CLAIM-1443](../claims.d/CLAIM-1443.md)'s third stage captures the mechanisms of
  correction. Both rest on [CLAIM-1287](../claims.d/CLAIM-1287.md). That the first is the second for a
  single trained learner no component states.
