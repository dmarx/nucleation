---
status: Read
paper: 'LIT-tmpm7tp8'
title: 'Koedinger and Aleven — The assistance dilemma in Cognitive Tutor experiments'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read in full on 2026-11-05 from the publisher's typeset PDF posted on
    the authors' own group site, the CMU PACT Center
    (https://pact.cs.cmu.edu/pubs/Koedinger%20Aleven%2007.pdf, linked from
    the https://pact.cs.cmu.edu/pubs/ listing); OpenAlex calls the DOI
    closed. Text extracted from the PDF. Read: abstract, introduction,
    Tables 1 and 2, the account of Cognitive Tutors, the review of
    experiments, the discussion and conclusion, and the references
    (pp. 239–264). Nothing skipped. Page numbers below are the journal's.
    Several reviewed studies are dissertations, proceedings or conference
    papers, and were not read; what is said of them is the authors'
    account.
date: '2026-11-05'
summary: >-
  A review by the Cognitive Tutors' developers that frames instruction as
  an "assistance dilemma" between giving and withholding information.
  Within tutored problem solving, where help comes only on failure,
  immediate and explanatory feedback and mastery learning beat
  withholding, students use on-demand hints badly, and faded worked
  examples adjust help to growing competence; so "information should be
  withheld very sparingly" (p. 255). Where to switch between giving and
  withholding is left open. Most component results come without effect
  sizes.
---
<!-- inactive-ok-file: THEORY-tmpngvdn CLAIM-600 CLAIM-602 CLAIM-603 CLAIM-597 CLAIM-558 CLAIM-604 CLAIM-601 THEORY-1483 THEORY-1463 THEORY-528 — Proposed or new; cited from the reading of Koedinger and Aleven (2007) as open -->

# NOTE-tmp607yf: Koedinger and Aleven — The assistance dilemma in Cognitive Tutor experiments

## Contribution

A name and a frame for a choice every instructional design makes and
rarely states: "To what degree should an interactive learning environment
provide students with information ... And when is student learning
supported more effectively by withholding information" (p. 242). Table 2
lays out the costs and benefits of each side. The authors reinterpret
Cognitive Tutor experiments on feedback timing, feedback content, hints,
mastery learning, worked examples and fading as partial answers, and name
the open problem: criteria "for when it is best to switch between
information giving (more assistance) and information withholding (less
assistance)" (p. 261). It is a review, not a new experiment.

## Key insight

"Instructional interaction should optimize student involvement, not
maximize or minimize it" (p. 260). Help given buys accuracy and speed at
the cost of "Shallow processing" and "Stealing chance to shine"; help
withheld buys generation and memory engagement at the cost of "Floundering,
confusion, wasted time" (Table 2). The tutors answer by keeping the
learner doing every step and adding help on failure, and the experiments
they review favour that answer and, within it, more help rather than less.

## Assumptions

- **ACT-R.** Production rules are "acquired and strengthened through use
  in problem solving" (p. 250), so floundering adds no learning and wastes
  time. This is the stated basis for immediate feedback.
- **Fine-grained knowledge.** Knowledge is made of independently learned
  components (pp. 247–248), each tracked with a two-state Bayesian model
  with fixed parameters (p. 249).
- **The outcome** is post-test performance without the tutor, nearly
  always immediate. The one longer horizon, Mathan and Koedinger's
  long-term retention, has no interval given.

## Key results

*Page numbers are the journal's. Studies are the authors' account of them.*

- **The frame (Table 1, p. 241).** Explicit or implicit, crossed with
  passive, active or interactive. In interactive instruction "some
  information is initially withheld from the learner" and more is "later
  given, if the learner fails to construct it him or herself".
- **The design rule (p. 260).** "Cognitive Tutors initially withhold
  information about problem solutions and solution steps, and then
  interactively add information, only as needed". Promotion is on measured
  capacity: each skill's probability estimate must pass "a pre-defined
  threshold, typically set to 0.95" (p. 247).
- **Overall effects, confounded (p. 251).** Geometry Proof Tutor students
  "scored about one standard deviation better" than the same teacher's
  others; Lisp Tutor "30–43% higher learning gains and 30–64% more
  efficient learning"; the three-course sequence "30% better on TIMMS test
  items and 227% better" on a real-world task. The authors: these "do not
  show that it is the tutors' interactivity per se that causes the effect".
- **Feedback timing (Corbett and Anderson, p. 252).** Immediate, flag and
  on-demand feedback "led to better and faster learning" than none; "no
  difference in the learning results between the three feedback
  conditions", but immediate feedback students were "about three times
  faster than the students in the no feedback condition". "Withholding of
  this information was shown to be counterproductive."
- **Feedback content (McKendree, pp. 252–253).** Explanatory feedback beat
  yes/no feedback, significant for the post-test error rate and marginal
  during training. No effect sizes.
- **Hint content (Anderson et al., p. 253).** Explanatory messages "help
  students learn faster, but not better".
- **Help seeking fails (pp. 253–254).** Students "frequently use
  bottom-out hints to obtain answers, without reading prior hints", and
  "even after multiple errors on a step, students often do not request
  help".
- **Mastery learning (pp. 254–255).** "significantly higher learning
  gains", and in Corbett's study "large learning gains at the cost of only
  very little extra time spent". No numbers.
- **The verdict on tutored practice (p. 255).** "within a context of
  tutored problem solving, information should be withheld very sparingly".
- **Worked examples added (pp. 255–257).** Gains "in two of four
  comparisons" in one study, "no benefit for the addition of these worked
  examples" in another, replicated, which the authors say is not
  expertise reversal; their account is that "the tutor dynamically
  converts a problem-solving experience into an annotated worked example"
  (p. 257).
- **Fading (Schwonke et al., p. 257).** Faded examples, used "To adjust
  information giving/withholding to learners' growing competence", let
  students learn "more efficiently, taking significantly less
  instructional time to achieve better post-test outcomes on declarative
  knowledge and equal outcomes on procedural knowledge". No effect sizes.
- **Delayed feedback on an intelligent-novice model (Mathan and
  Koedinger, p. 259).** Allowing errors a capable novice would catch:
  "Students learned more from the intelligent novice tutor", and "the
  treatment was better on all measures, both immediate and robust learning
  measures".
- **Metacognitive tutors (pp. 259–260).** The help-seeking tutor cut some
  poor help seeking "but no consequent improvements in geometry learning";
  the gaming detector's learning difference was "not statistically
  reliable", with harmful gaming in "about 10%" of students.
- **Gaming as a response to premature withholding (p. 260).** Perhaps "a
  rational effort by less knowledgeable students to compensate for what
  may be, from their perspective, premature information withholding";
  some medical students who gamed early showed "greater independent
  success on later problems".
- **A switch criterion (pp. 260–261).** Give help "when the task gets too
  difficult and thus the probability of error or unproductive thinking is
  high"; the cut-off is unknown. Pavlik's "ideal error rate of about
  5–25%", from ACT-R simulations of fact learning, may or may not
  generalize: that "is wide open".

## Concepts

- **Assistance dilemma**: the choice of how far to give and how far to
  withhold information or help, and when to switch.
- **Interactive instruction**: information withheld at first and added if
  the learner fails to construct it.
- **Knowledge tracing and mastery threshold**: a per-skill probability of
  being known, with promotion at 0.95.
- **Bottom-out hint**: the last hint in a sequence, which gives the answer.
- **Gaming the system**: getting through steps by exploiting help or
  feedback rather than solving them.
- **Faded worked examples**: worked steps removed one by one as competence
  grows, turning examples into problems.
- **Intelligent novice model**: feedback delayed to let errors a capable
  novice would catch be caught.
- **Expertise-reversal effect**: cited (Kalyuga et al. 2001), not tested.

## Connections

The record held nothing on tutoring, worked examples, fading or the
expertise-reversal effect before this reading; the scaffolding it held is
evolutionary. Its other learning-by-doing ground is Azam, Devarajan and
O'Connell's model of learning to tax under aid ([THEORY-1483](../theory.d/THEORY-1483.md)), which grounds
[CLAIM-602](../claims.d/CLAIM-602.md); this is the same premise in an individual learner. The cost of
withholding, floundering, is at a learner's scale what Pritchett, Woolcock
and Andrews call premature load bearing in states ([LIT-2164](../literature.d/LIT-2164.md), [THEORY-1463](../theory.d/THEORY-1463.md)).
Rupert's case against extended cognition ([LIT-422](../literature.d/LIT-422.md), [THEORY-528](../theory.d/THEORY-528.md)) is the
record's one other mention of the generation effect. Wood, Bruner and Ross
(1976), registered the same day and unread, are not cited here; Griffith,
Redding and Van Reenen (2004), read the same day, carry the same premise,
capacity to use outside help built by own work, at the level of
industries.

## Bearing on the record

- **[CLAIM-602](../claims.d/CLAIM-602.md)** (capacity-first order of supply): support in an
  independent domain. The tutor's rule is capacity-first, under the same
  premise that skill is "acquired and strengthened through use"
  (p. 250), and its success is judged without the tutor. It qualifies the
  claim three ways. (a) Capacity-first assumes the supply can see what the
  party can do; where the learner controls the help, "students are not good
  at seeking assistance" (p. 253), and on-demand help turns into
  substitution by bottom-out hints and gaming. (b) Withholding has its own
  cost, floundering, and within tutored practice too little help is the
  commoner error (p. 255). (c) Doing the work is not the only route:
  bottom-out hints studied as examples can teach (pp. 257, 260), so
  substituted work teaches when the learner explains it to themselves.
  *The filer's own observation, not the reader's or the authors':* faded
  worked examples put supply first, the example doing the steps, and
  withdraw it as competence grows, and Schwonke et al. found that order
  more efficient than the standard tutor (p. 257). On the example steps
  the students explained the worked steps and got feedback on their
  explanations, which is (c) again. In a learner, then, supply first that
  is withdrawn as competence grows, with the learner working on what is
  supplied, did not lower what was kept on the post-test; [CLAIM-602](../claims.d/CLAIM-602.md)'s harm
  from supply first may need the supply to persist, to be withdrawn
  without regard to capacity, or to leave the party nothing to do.
- **[CLAIM-600](../claims.d/CLAIM-600.md)** (when transient support can be withdrawn safely): supports
  the condition that the party could do the work and did it throughout,
  and qualifies it: early withdrawal is not safe by default, and withdrawal
  is graded with competence, not one event.
- **[CLAIM-603](../claims.d/CLAIM-603.md)** (one-way supply and loss): qualifies on incentives. Hint
  requests lower the mastery estimate and bring more problems (pp. 250,
  255), a designed cost on asking; students know it, "although that does
  not always stop them" (p. 255). It bears on the Samaritan-style
  incentive, not on the Black Queen mechanism.
- **[QUESTION-398](../questions.d/QUESTION-398.md)**: an operational analogue. Promotion at P(known) ≥ 0.95
  is a withdrawal rule set on measured capacity, and the post-test without
  the tutor is the persistence check. The switch-point problem (p. 261) is
  the analogue of where dependence falls to zero; the paper does not
  measure dependence by withdrawing support at matched states.
- **[CLAIM-597](../claims.d/CLAIM-597.md), [CLAIM-558](../claims.d/CLAIM-558.md), [CLAIM-604](../claims.d/CLAIM-604.md), [CLAIM-601](../claims.d/CLAIM-601.md)**: nothing directly. What is
  supplied here is information, internalized, not ongoing upkeep; decay with
  disuse is not studied; no threshold or hysteresis in skill is measured.
- Filed from it: [THEORY-tmpngvdn](../theory.d/THEORY-tmpngvdn.md).

## Limitations

- A narrative review by the system's developers, with no meta-analysis;
  most component results come without effect sizes, sample sizes or
  variances, and several sources are dissertations, proceedings or a
  conference paper.
- The overall gains are curriculum comparisons with confounds, as the
  authors say (p. 251), some reported by the vendor or third parties.
- Retention horizons are rarely given, none in days or months:
  persistence after withdrawal here means an immediate post-test.
- Expertise reversal is cited, not tested.
- Domains are mathematics, programming, Excel and chemistry; the subjects
  are individual students, not organizations.
