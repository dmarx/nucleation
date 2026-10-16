---
status: Read
paper: LIT-tmp626gh
title: 'Powers — Feedback: Beyond Behaviorism'
version: 1
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Read in full from the reprint in Living Control Systems: Selected Papers
    of William T. Powers (Control Systems Group, Gravel Switch KY, 1989), pp.
    61–78, in the PDF the publisher's successor hosts at
    livingcontrolsystems.com/download/LivingControlSystems_1_Powers1989.pdf
    (324 pages, an OCR'd scan), extracted with pdftotext -layout. The reprint
    is "Reprinted with permission of the publisher from Science 179(4071),
    January 26, 1973, 351-356" (p. 61), reset by the editor with "mainly
    silent corrections of obvious typographical errors" (A Note on the Text,
    p. xix). Every section was read: the opening, Act versus Result, Feedback
    Control, Goal-Directed Behavior, Controlled Quantities, Hierarchies of
    Controlled Quantities, Implications for Behaviorism, Summary, Fig. 1 and
    its caption, and the ten references and notes. Page numbers below are
    the reprint's; the Science pagination is not marked in it. The
    original Science typesetting was not seen. Quotes are verbatim from the
    extraction, with OCR misreadings of single letters checked against the
    surrounding text.
date: '2026-10-16'
summary: >-
  A control system "will produce whatever output is required in order to
  achieve a constant sensed result" (p. 77), so behaviour is the control of
  input, not output, and stimulus-response laws follow from the environment
  once the controlled quantity is found. Above the lowest level a system's
  output is a reference level for the level below, so the hierarchy
  closes through lower systems down to muscle effort sensed kinesthetically;
  its top is a set of inherited intrinsic reference levels whose error drives
  reorganization. The paper says nothing about imagination: every loop it
  describes closes through the environment.
---

# NOTE-tmpxdsyb: Powers — Feedback: Beyond Behaviorism

## Contribution

A short programmatic article in Science. It argues that behaviourism's
open-loop model of stimulus and response is wrong because stimuli depend on
responses as much as responses on stimuli, and replaces it with a negative
feedback control unit whose sensed input, not output, is held at a reference
level. It gives a test for a controlled quantity (disturb it and see whether
the effect is much smaller than physics predicts), and builds a two-level
hierarchy from one example (a soldier pointing at a helicopter) in which the
higher system acts by setting the lower system's reference. It sketches, in
one paragraph, a top level of inherited "intrinsic reference levels" whose
error drives reorganization. It is a preview of the book, which it cites as
"in press" (note 2, p. 78).

## Key insight

"control systems control what they sense, not really what they do" (pp.
73–74). Output varies to cancel disturbances, so "the chief determinant of
output is thus the disturbance" (p. 74), and what is constant is the sensed
result. Stack such units and the output of each higher unit "is not a muscle
force, but a reference level (variable) for a lower-order controlled
quantity" (p. 77): purposes are reference signals, and a higher purpose is
pursued by changing a lower one.

## Assumptions

- **Negative feedback and dynamic stability.** The system "must be organized
  for negative (not positive) feedback, and ... must be dynamically stable"
  (p. 65). Unstable systems are set aside because normal behaviour does not
  show their symptoms.
- **Constant sensor.** "If the properties of the sensor remain constant, as
  we may usually assume" (p. 67), control of the sensor signal is control of
  the external quantity.
- **No learning in the unit.** "This is a continuous-variable (analog)
  model, without provision for learning" (p. 67). Reorganization is named
  only at the top of the hierarchy, and deferred: "that takes us to the
  verge of learning theory, which is beyond the intent of this article" (p.
  73).
- **A slow observer.** The right time scale for observing a control system
  "is that on which the response to an impulse-disturbance is apparently
  zero" (p. 68). On it, goal-seeking is "goal-maintaining behavior".
- **Additive disturbance and output.** The controlled quantity changes by
  g(d) + h(o), so under good control g(d) ≈ −h(o) (pp. 69–70).
- **The reference's origin is left open at first.** Fig. 1's reference is
  "of unspecified origin" (p. 66), answered in part by the hierarchy.

## Key results

There are no data. The quantitative content is a worked example.

- **The test for a controlled quantity (p. 69).** Postulate
  q_c = f(v₁ … v_n), predict the change Δq_c = g(d) a disturbance d would
  cause without the system, observe the actual change Δ*q_c. If q_c is
  controlled, Δ*q_c/Δq_c ≪ 1. Varying the form of f to minimise the ratio
  finds the controlled quantity.
- **The soldier's arm (p. 70).** A 1 kg sideways force would raise an
  uncontrolled arm about 30 degrees; the arm moves 1 degree, 1/30 of the
  prediction, so the soldier's opposing force is "just a trifle under 1
  kilogram". With the arm held horizontal against a 10 kg weight, an upward
  push of 10 kg should drop net output to zero and 11 kg should produce
  "an output of 1/2 kilogram downward" (pp. 70–71; as printed).
- **Two levels (pp. 71–72).** Pointing at a moving helicopter keeps the
  angle between pointing direction and line of sight at zero, while arm
  position, still controlled against brief pushes, drifts with the
  helicopter. The second system "opposes disturbances not by direct
  activation of force outputs, but by altering the reference level, by means
  of changing the reference signal for the arm-position control system" (p.
  71). It needs two lower systems, horizontal and vertical.
- **Up is why, down is how (pp. 72–73).** Going down: arm position, then
  "net muscle-generated forces", then "the control systems in the spine
  which control the effort in whole muscles, as sensed kinesthetically" (p.
  73). Going up, the top is "certain biologically important variables, which
  Ashby called critical variables and which I term intrinsic quantities" (p.
  73).
- **Self-determination (p. 76).** "organisms are self-determined in terms of
  inner control of what they sense, at every level of organization except
  the highest level."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Behaviour is the control of input, not output: a control system produces whatever output keeps its sensed result at a reference | strong as a property of negative feedback; as a claim about organisms, illustrative | Fig. 1 and §Feedback Control; the soldier example |
| C2 | A controlled quantity can be identified by disturbing it and finding Δ*q_c/Δq_c ≪ 1 | moderate | method stated, p. 69; one informal example |
| C3 | Above the lowest level, a system's output is a reference for lower systems, not a muscle force | moderate | one two-level example, pp. 71–72; extension "indefinitely" asserted, p. 72 |
| C4 | Given the controlled quantity, stimulus-response laws follow from environmental physics, not from the organism | moderate | derivation g(d) ≈ −h(o), p. 74; Fig. 1 caption |
| C5 | The highest reference levels are inherited intrinsic quantities, and reorganization is the error-driven output of an inherited control system | weak | asserted in one paragraph, p. 73, citing the 1960 paper |
| C6 | Operant conditioning of humans by humans is doubtful in the long run, since people learn to circumvent arbitrary deprivation | weak | informal argument, pp. 76–77 |

## Concepts

- **Act and result.** "What I term an act is a behavior that is arbitrarily
  left unanalyzed, while a result is defined as an understandable physical
  consequence of an act. Act and result are relative terms" (note 3, p. 78).
- **Controlled quantity.** A function q_c of environmental variables that the
  system keeps near a reference level against disturbance (p. 69).
- **Reference level.** The controlled quantity's value "when the system's
  output is totally unopposed", equivalently the value that "results in zero
  error-correcting output" (p. 70). Distinguished from the internal
  reference signal.
- **Disturbance.** Effects on the input quantity independent of the
  system's output; it "corresponds to 'stimulus'" (Fig. 1 caption, p. 66).
- **Intrinsic quantities.** Ashby's critical variables: "the quantities
  affected by deprivation and subsequent reinforcements that erase, or at
  least diminish, the errors caused by deprivation" (p. 73).
- **Reorganization.** "the error-driven 'output' of a basic inherited
  control system which is ultimately responsible for the particular
  structure of an adult's behavioral control system" (p. 73).

## Connections

The control unit is "modeled after Wiener's original concept", with the
system boundary moved and the sensor signal, not the reference, made "the
immediate consequence of a stimulus input" (p. 67). Goals as states a
behaviour tends toward are taken from Ashby's Design for a Brain and
reread as a sluggish control system (p. 67); intrinsic quantities are
Ashby's critical variables (p. 73). Act and result follow Rozeboom and
Brunswik (notes 3–5). Reorganization is referred to the 1960 General
Feedback Theory paper with Clark and McFarland (note 8). The book,
[LIT-tmp44sbd](../literature.d/LIT-tmp44sbd.md), is cited as in press (note 2). Baum and Reese's reply in
Science 181 (1973), with Powers's answer, is reprinted next in the same
volume (pp. 79–88) and was not read for this note.

## Bearing on the record

- **[CLAIM-tmpq9do8](../claims.d/CLAIM-tmpq9do8.md) (thesis).** The claim's "Rivals" bullet quotes this
  paper correctly: "behavior is the control of input, not output" (p. 77)
  and "The output of a higher-order system is not a muscle force, but a
  reference level (variable) for a lower-order controlled quantity" (p.
  77). Two qualifications.
  - *Most of the hierarchy is internal, but not as the thesis's loop is.*
    In this paper a higher system's input is still a quantity in the world:
    the pointing direction "relative to the direction of the helicopter"
    (p. 71). It acts inwardly, through a lower reference, but what it senses
    and controls is outside. Its loop runs through the lower systems and
    then through the environment; it "controls it ... by using the whole
    lower-order system as its means of error prevention" (p. 72). So the
    paper's hierarchy is internal on the output side only. That is not the
    thesis's loop, in which a judgement reshapes the observer itself.
  - *Every loop here does bottom out in action.* The chain of hows "extends
    further down, to the control systems in the spine which control the
    effort in whole muscles, as sensed kinesthetically" (p. 73). The paper
    has no loop that closes without the environment, and does not mention
    imagination or memory. The rival as the claim states it is therefore
    this paper's. It is not all of perceptual control theory: Powers had
    an "imagination connection" in 1960, and in 1988 he wrote that "the
    control loop always (except for imagination) involves effects in the
    external world" (Living Control Systems, p. 279). Neither is this
    work; the book, [LIT-tmp44sbd](../literature.d/LIT-tmp44sbd.md), was not read. The claim should not
    cite this paper for PCT's position on internal loops.
  - *The reference is changed, not the sensor.* In the paper the higher
    level changes what the lower level aims at, never how it perceives:
    "If the properties of the sensor remain constant, as we may usually
    assume" (p. 67). The thesis's diachronic form, judgement reshaping the
    observer, has no counterpart here except reorganization, which changes
    "the particular structure of an adult's behavioral control system" (p.
    73), sensors presumably included, though the paper does not say so.
- **[CLAIM-tmpt568z](../claims.d/CLAIM-tmpt568z.md) and [QUESTION-tmpr5tck](../questions.d/QUESTION-tmpr5tck.md) (the anchor).** The paper's top
  level is exactly a scoring channel that the learned hierarchy does not
  set: inherited intrinsic reference levels, compared against intrinsic
  quantities "affected by deprivation", whose error drives reorganization
  (p. 73). Organisms are self-determined "at every level of organization
  except the highest level" (p. 76). That is the structure [CLAIM-tmpt568z](../claims.d/CLAIM-tmpt568z.md)
  attributes to Ashby ([THEORY-324](../theory.d/THEORY-324.md)), stated by Powers in Ashby's terms, and
  it is [QUESTION-tmpr5tck](../questions.d/QUESTION-tmpr5tck.md)'s candidate 2, the body. Two cautions. In the
  paper the intrinsic quantities are restored by "subsequent
  reinforcements", events in the world, so the channel is bodily but its
  correction comes by action; and "For a human being, the 'intrinsic
  reference levels' probably specify far more than mere food or water
  intake. We cannot arbitrarily rule out any goal at this level-not even
  goals such as 'self-actualization'" (p. 73), which widens the top level
  until it is no longer plainly independent of the interpretation.
- **[CLAIM-tmp9cjyo](../claims.d/CLAIM-tmp9cjyo.md) (counter).** The paper supports its formal point in
  control terms: a higher system's means is a lower system's reference, so
  the lower system is the higher one's proximal environment. It does not
  support relabelling a judgement as action: nothing in it is mental
  action.
- **[CLAIM-tmpki5gp](../claims.d/CLAIM-tmpki5gp.md) (counter).** The paper's "Only overwhelming force or
  insuperable obstacles can cause an organism to give up control of what it
  senses" (p. 76) is about action, not perception without action, and says
  nothing about paralysis.
- **Checks of [LIT-tmp626gh](../literature.d/LIT-tmp626gh.md).** Its summary is correct: "produces whatever
  output keeps a sensed result constant despite disturbances" matches p.
  77, and the hierarchy sentence matches p. 77. Its "Why this is here"
  says "Unlike the thesis, PCT keeps action at the bottom of every loop":
  true of this paper, which has no other kind of loop, but stated of PCT,
  for which it is not true without the imagination exception.
- **For the anthology.** No instruction for machine-learning practice.

## Limitations

- A programmatic article without data; the soldier and the rat are
  thought experiments or informal observations.
- Learning is excluded from the model it presents, and reorganization is
  one paragraph.
- The hierarchy is shown for two levels; "can now be continued
  indefinitely" (p. 72) is asserted.
- The reading is of a reset reprint with silent corrections, read from an
  OCR extraction; the Science pagination was not checked.

## Open questions

- Whether PCT's imagination connection, a reference signal routed back as
  the system's own perception, is the thesis's judgement–observation loop or
  only its synchronic, self-satisfying limit ("every goal ... appeared to be
  immediately satisfied", Living Control Systems p. 20). That needs the
  book, [LIT-tmp44sbd](../literature.d/LIT-tmp44sbd.md), or the 1960 paper, which the record does not hold.
- Whether reorganization can change perceptual input functions, which would
  make it the PCT counterpart of the thesis's reshaped observer.
