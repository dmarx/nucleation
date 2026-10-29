---
status: Read
paper: LIT-tmpui6bx
title: 'The Significance, Persistence, Contingency Framework'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full from version 1.1 (dated August 2022, 11 pages) on the
    book's supplementary-materials page at whatweowethefuture.com; no
    other version found. Page numbers are the copy's printed ones. Read
    in place of MacAskill 2022, What We Owe the Future (LIT-tmpk6b4i).
    The book's full online endnotes were consulted for what the chapters
    argue, at second hand, and are cited by note number.
date: '2026-10-29'
summary: >-
  The value an event E contributes through a feature F of the world is
  significance × persistence × contingency: value per unit of the time
  E adds (ΔV/ΔT), how long F lasts (T), and the share of that duration
  due to E (ΔT/T). Under uncertainty the factors are taken ex ante
  (ΔEV/ΔET, ET, ΔET/ET), which keeps the product but is not the product
  of expected factors. An alternative takes significance as V/T and
  makes contingency the sum of the semi-elasticities of significance,
  persistence and the probability that F exists. The result estimates
  the "importance" factor of the ITN framework. It is an accounting
  device that assumes expected-value maximisation; it says nothing about
  who is moved by the value it counts.
---
<!-- inactive-ok-file: LIT-tmpk6b4i LIT-tmpi3189 QUESTION-tmpmx9ha CLAIM-tmpjylq8 CLAIM-tmprudek CLAIM-tmpybc4k — Deferred, Open or Proposed; the book this stands in for, a work it connects to, and the question, thesis and objections it bears on -->

# NOTE-tmpo2a6r: The Significance, Persistence, Contingency Framework

## Contribution

A formal version of the heuristic that organises *What We Owe the
Future*. To judge how much an act matters for the long run, ask how
valuable the state of affairs it brings about is while it lasts, how
long it lasts, and how far its presence depends on the act. The note
shows that this three-way split is an exact factorisation of the change
in value, gives marginal and expected-value versions, sketches an
alternative, and places the result inside the effective-altruism
importance–tractability–neglectedness framework.

## Key insight

Contingency is what attributes value to a chooser. Significance and
persistence describe the world; contingency asks "how much of the
feature's value can be attributed to a particular agent's decision at a
particular point in time" (p. 1). An act is worth what the world would
lack without it. The framework's "main goal is to help estimate the
instrumental value (typically interpreted as the expected value) of an
event, compared to the relevant counterfactual" (pp. 1–2).

## Assumptions

- **Expected-value maximisation** is "the fundamental rule for choice
  under uncertainty" (§2.2, p. 5). It is assumed, not argued.
- **Value comes in additive features.** Overall evaluation sums
  features, Vtot = VF1 + VF2 + … (eq. 19, p. 9). The authors grant that
  such a list "may often be difficult to identify" (p. 9).
- **Durations are finite.** The book's note (2.18) adds that an end date
  of the universe should be assumed, "otherwise we would have to deal
  with some states of affairs being infinitely persistent".
- **No theory of value.** A feature is "any source of value (or
  disvalue)": a headache, the future existence of civilisation, the
  prevalence of QWERTY keyboards (n. 1, p. 1). What is valuable, and for
  whom, is left open.

## Key results

- **The basic framework** (§2, pp. 2–4). With ΔV and ΔT the changes E
  makes to F's total value V and duration T, relative to the salient
  alternative or status quo:
  - Sig = ΔV/ΔT, Per = T, Con = ΔT/T (eq. 1), so ΔV = Sig × Per × Con
    (eq. 2).
  - It "make[s] most intuitive sense" when E's main effect is to lengthen
    F's presence without changing its value while it would have been
    present anyway (p. 3). Con is 1 when F would not exist but for E, 0
    when E makes no difference to its duration.
  - Worked example: F contributes 1, 2, 4, 8 in four periods; it would be
    present in periods 2–3, and E adds periods 1 and 4. Then Per = 4,
    Con = 1/2, Sig = 9/2, ΔV = 9 (p. 3). Sig is neither the status-quo
    average (6/2) nor the average given E (15/4).
- **Marginal form** (§2.1, p. 4). For a marginal change in a parameter X,
  such as funding, Con = %dT/dX, the semi-elasticity of persistence.
- **Uncertainty** (§2.2, pp. 4–6). Either compute ΔV state by state and
  take its expectation, or use ex ante factors: Sig = ΔEV/ΔET,
  Per = ET, Con = ΔET/ET (eq. 6). These keep the product, but Sig is not
  expected significance and Con is not expected contingency, since "the
  expectation of a product is not usually equal to the product of
  expectations" (p. 5). The book's note (2.30) says the same and adds
  that for its purposes this "will not be hugely important".
- **An alternative framework** (§3, pp. 6–8).
  - Sig′ = V/T, independent of the counterfactual; Per′ = T;
    Con′ = ΔV/V, or %dV/dX at the margin (eqs. 10–12).
  - At the margin, Con′ = %dSig′/dX + %dPer′/dX (eq. 14): contingency is
    the sum of the semi-elasticities of significance and persistence.
  - The probability that F is present can be split out as Prob, so that
    EV = (EFV/EFT) × EFT × Prob and Con′ adds %dProb/dX (eqs. 15–16). The
    example given: "small changes in the probability that human
    civilisation continues beyond this millennium are often thought to
    be a significant source of value" (p. 7).
  - The two frameworks agree when F contributes a fixed value per unit
    time unaffected by E (p. 6).
- **ITN** (§4, pp. 8–9). Importance of marginal progress X on a problem
  is Imp = dEVtot/dX (eq. 18), counting all downstream effects. SPC
  estimates dEVF/dX feature by feature, and with additive features Imp
  is their sum (eq. 20). The book's note (2.17) puts it as "a quantity
  proportional to the 'importance' dimension".
- **Tractability and leverage** (§4.1, pp. 9–11).
  - Cotton-Barratt's decomposition, dX/dW = (dX/%dW) × (1/W), takes
    neglectedness as 1/W. It is most intuitive with logarithmic returns;
    with linear returns his tractability grows with the work already
    done, which "could be somewhat counterintuitive" (p. 11).
  - The alternative: dX/dW = (X0/W0) × [(dX/dW)/(X0/W0)] (eq. 23). The
    first factor is the problem's overall easiness, the second
    "leverage", how much easier progress is at the current margin than on
    average. High leverage "does not imply that little work is being
    done" (p. 11).
- **What the book's notes add** (second hand, by note number).
  - The framework "was created by Aron Vallinder and me and further
    developed by Teruji Thomas", and appears in the book's Appendix 3
    (2.17). That appendix uses worlds X and O, a QWERTY–Dvorak example
    and the notation Vs(p), Ts(p) (A.4–A.6).
  - Note (A.6) concedes a gap: the requirement that a state's value
    depend only on how long the world is in it "should perhaps be added
    to the definition", or the definitions of significance and
    contingency make little sense.
  - The book's ITN formalisation, "suggested to me by Teruji Thomas",
    makes tractability depend only on the problem, not on the work
    already done (A.9). That matches the report's easiness factor X0/W0.
  - "Trajectory change" is narrowed to lasting changes in civilisation's
    average value, apart from changes to its duration (2.20), which the
    book calls "civilisational safeguarding" (2.22).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The change in value an event makes through a feature equals significance × persistence × contingency | demonstrated: an identity from the definitions | §2, eqs. 1–2 |
| C2 | The decomposition is most intuitive when the event's main effect is on the feature's duration | interpretive; the book's note (A.6) concedes a restriction may be needed | §2, p. 3 |
| C3 | Under uncertainty, ex ante factors keep the product, but are not the expectations of the factors | demonstrated | §2.2, eqs. 6–9 |
| C4 | Taking significance as V/T makes contingency the sum of semi-elasticities of significance, persistence and probability of presence | demonstrated: follows from log V = log Sig′ + log Per′ | §3, eqs. 10–17 |
| C5 | SPC estimates, summed over features, give the importance factor of ITN | conditional on additive features, which the authors grant are hard to find | §4, eqs. 18–20 |
| C6 | Tractability is better read as overall easiness times leverage than as Cotton-Barratt's dX/%dW in some cases | argued from two returns curves; offered as an option | §4.1 |

## Concepts

- **feature**: any source of value or disvalue in the world, from a
  headache to the existence of civilisation.
- **originating event**: the choice or other event whose contribution is
  being valued.
- **significance**: average value per unit time, of the extra time due
  to E (§2) or of the feature given E (§3).
- **persistence**: how long the feature lasts, given E.
- **contingency**: how far the feature's duration (§2) or value (§3)
  depends on E; at the margin, a semi-elasticity.
- **semi-elasticity**: the change in a quantity as a proportion of
  itself, per unit change in X; written %d/dX.
- **leverage**: marginal progress per unit of work relative to the
  average for the whole problem; a form of neglectedness.
- **trajectory change / civilisational safeguarding** (book's notes):
  raising civilisation's average value, versus extending its life span.

## Connections

- **What We Owe the Future ([LIT-tmpk6b4i](../literature.d/LIT-tmpk6b4i.md))**, unread. §2 explains "the
  framework as it appears in" the book (p. 2), so this is the book's own
  accounting device. The notes show it organising chapter 2 and Appendix
  3. It is not the book's argument that future people count, nor its
  population ethics.
- **Greaves and MacAskill ([NOTE-tmpozxwf](NOTE-tmpozxwf.md)).** The same expected-value
  framing, with a benefit ratio in place of a factorisation. The book's
  notes place the book short of strong longtermism: a critique by
  Mogensen "only applies to versions of longtermism on which our
  obligation to help future people trumps all other self- and
  other-regarding reasons for action, which is not the view I'm
  defending in this book" (1.50).
- **Tarsney ([NOTE-tmp0l9dk](NOTE-tmp0l9dk.md)) and Thorstad ([NOTE-tmpu4i35](NOTE-tmpu4i35.md)).** In SPC terms,
  and as an inference, their challenges fall on contingency and
  persistence: Tarsney's decay of predictable influence lowers how much
  of a far-future feature depends on a present act, and Thorstad's high
  background risk shortens expected persistence.
- **Bostrom ([NOTE-tmpwwa8k](NOTE-tmpwwa8k.md), [NOTE-tmpyret1](NOTE-tmpyret1.md)).** The alternative
  framework's Prob term is where reducing existential risk enters.
  MacAskill's notes give his own credences: end of civilisation this
  century 0.1 to 1 percent, misaligned AI takeover about 3 percent,
  value lock-in at some point over 80 percent; and the expected value of
  civilisation's continuation under 1 percent of the best feasible
  future, so that "trajectory changes have over one hundred times
  greater potential upside than civilisational safeguarding" (2.22).
- **Syropoulos et al. 2023 (filed with this reading).** Its Study 4 used
  a 385-word excerpt from the book's introduction, the section "Future
  People Count", as an intervention. It raised felt responsibility to
  future generations, by the smallest margin of five interventions.

## Bearing on the record

- **The owner's thesis ([CLAIM-tmpjylq8](../claims.d/CLAIM-tmpjylq8.md)).** These are inferences; the note
  does not discuss motive.
  - The framework values states of the world, not anyone's good as
    theirs. Nothing in it is indexed to the agent except contingency,
    which attributes value to the agent's choice. So the book's ground,
    as formalised here, is the impersonal good. As [QUESTION-tmpmx9ha](../questions.d/QUESTION-tmpmx9ha.md)
    already says, the thesis bears on such a ground only as a question of
    who is moved by it.
  - Contingency has the shape of a difference-making motive: what matters
    is the value that would be missing without me. If people are moved
    by their own contribution rather than by the value alone, a
    self-regarding element sits inside an impartial calculus. The report
    neither asserts nor tests this. GPI lists Greaves, Thomas, Mogensen
    and MacAskill, "On the desire to make a difference" (Philosophical
    Studies, 2024), not held, which is where the question is taken up.
  - The book's notes name a ground the question does not list:
    reciprocity. "We benefit enormously from the actions of people in the
    past … Perhaps, then, this gives us reasons to 'pay it forward'"
    (1.5). Syropoulos et al.'s sacrifice condition is a test of it.
- **The triviality objection ([CLAIM-tmprudek](../claims.d/CLAIM-tmprudek.md)).** Not addressed.
- **Batson's objection ([CLAIM-tmpybc4k](../claims.d/CLAIM-tmpybc4k.md)).** Not addressed.
- **A dated note is proposed for [QUESTION-tmpmx9ha](../questions.d/QUESTION-tmpmx9ha.md)**, not for the claim.
- **No THEORY filed.**
- **No ML instruction.**

## Limitations

- **Not the book.** Eleven pages of algebra. It does not argue that
  future people count, that there may be very many of them, or anything
  of population ethics, lock-in or extinction.
- **The notes are not the chapters.** They show sources, numbers and
  asides. What the chapters argue is inferred from them.
- **One toy example.** Applications to real events are left to the book
  (p. 2).
- **Additivity of features** is needed for the ITN step and conceded to
  be hard to meet (p. 9).
- **Expected-value maximisation** is assumed. The book's notes grant a
  problem of "tiny probabilities of enormous amounts of value" (2.22).
- **Version and date.** Version 1.1 of August 2022, posted in June 2023.
  Version 1.0 was not found.
- **Typos.**
  - "occurence" (p. 2).
  - "tractabilility" (n. 4, p. 10).
  - In the book's notes, (A.6) prints "Ts(p) − Ts(p)", which must mean
    Ts(p) − Ts(q), q being the status quo (A.7).
  - Note (9.3) reads "Waiting for reference".

## Open questions

- Is a desire to make a difference, to maximise one's own contingency,
  at odds with caring about the value itself? If so, which one moves
  people who say they act for the far future?
- Does the book's Appendix 3 add the restriction note (A.6) proposes,
  or adopt §3's alternative? Only the appendix's notes were seen.
