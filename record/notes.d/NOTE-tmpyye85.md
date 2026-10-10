---
status: Skimmed
paper: 'LIT-tmph1v0q'
title: 'Causality: Models, Reasoning, and Inference'
version: 1
history:
- version: 1
  date: '2026-10-10'
  note: >-
    Skimmed on 2026-10-10: four excerpts of the second edition that the
    author posts on his own site, and nothing else. (1) The table of
    contents, pp. vii–xiii,
    https://bayes.cs.ucla.edu/BOOK-2K/book-toc-final.pdf (7 PDF pages).
    (2) The Preface to the Second Edition, p. xix,
    https://bayes.cs.ucla.edu/BOOK-09/preface-2nd-ed-final.pdf (1 page).
    (3) §§5.3.2–5.4.1, pp. 154–163,
    https://bayes.cs.ucla.edu/BOOK-09/causality2-ss532-541.pdf (10
    pages), which ends partway into §5.4.2. (4) The Epilogue, "The Art
    and Science of Cause and Effect", pp. 401–428,
    https://bayes.cs.ucla.edu/BOOK-09/causality2-epilogue.pdf (28
    pages), a public lecture of November 1996 with its slides. All four
    were read in full. Text was extracted with pdftotext. Where it
    failed I rendered the page with pdftoppm and read the image. On p.
    154 an author's note ("The Confusion of the Century") is laid over
    the end of §5.3.1, and the extraction interleaves the two; the
    image shows only the note and the start of §5.3.2. The extraction
    loses the Greek letters of §5.3 (β, γ, δ and ε come out as other
    glyphs) and the ≜ and = signs of the Epilogue's equations, which
    were read from the images (pp. 157, 158, 417, 422, 423). The posted
    PDF of p. 157 carries a correction in red (see Key results). Not
    read: chapters 1–4 and 6–11, the rest of chapter 5, the Preface to
    the First Edition, the bibliography and the indexes. The derivation
    of the three rules of the do-calculus, the identification results
    and the counterfactual chapters were therefore not seen, only named.
    No other copy of the book was used.
date: '2026-10-10'
summary: >-
  From four excerpts the author posts: an intervention do(X = x) is a
  surgery that deletes X's structural equation, sets X to x and solves
  the rest, while observing X = x violates no equation and is ordinary
  conditioning, "given that we see". Structural equations are therefore
  not algebraic equalities: they stand for every submodel an
  intervention can produce, and a structural coefficient is
  ∂E[Y | do(x)]/∂x, not a regression slope. The Epilogue contrasts two
  components of science, observation and intervention, and states the
  three rules of the do-calculus without their derivation. The excerpts
  have no three-level hierarchy of association, intervention and
  counterfactual.
---

<!-- inactive-ok-file: CLAIM-127 CLAIM-tmp2i7yj — Proposed; the record's claims checked here against the excerpts, cited as open -->

# NOTE-tmpyye85: Causality: Models, Reasoning, and Inference

*A skim of four excerpts, 46 of the book's some 480 pages: the
contents, the Preface to the Second Edition, §§5.3.2–5.4.1 (pp. 154–163)
and the Epilogue (pp. 401–428). Nothing here comes from the rest of the
book.*

## Contribution

In the excerpts read, the book's contribution is a meaning for causal talk
in terms of intervention. A causal model is a set of structural equations,
each an autonomous mechanism. Intervening on a variable replaces its
equation, and observing it does not. The do() symbol writes the difference
into probability notation, so that P(y | do(x)) and P(y | x) are different
quantities. The do-calculus has three rules for turning one kind of
expression into the other when a diagram licenses it (Epilogue, pp.
421–423).

The Preface to the Second Edition says what the 2009 edition changed (p.
xix). It "(1) provides technical corrections, updates, and clarifications
in all ten chapters of the original book, (2) adds summaries of new
developments and annotated bibliographical references at the end of each
chapter, and (3) elucidates subtle issues that readers and reviewers have
found perplexing, objectionable, or in need of elaboration. These are
assembled into an entirely new chapter (11)." The contents bear this out:
a postscript closes chapter 5 (§5.6, "Postscript for the Second Edition"),
and chapter 11, "Reflections, Elaborations, and Discussions with Readers",
runs from p. 331 to p. 398.

## Key insight

"Intervention amounts to a surgery on equations (guided by a diagram) and
causation means predicting the consequences of such a surgery" (p. 417).
Seeing and doing are two sentences, not one. Probability theory is the
algebra of the first: in P(Rain | Wet) "the vertical bar stands for the
phrase: 'given that we see'" (p. 421). Asked "What is the chance it rained
if we make the grass wet?", it has no syntax for the question. "We know
intuitively what the answer should be: P (Rain), because making the grass
wet does not change the chance of rain" (pp. 421–422). The do-operator is
the new symbol, and the surgery supplies its meaning ("Meaning: surgery +
substitution", slide 44, p. 422).

## Assumptions

These are the conditions under which the excerpts' account of intervention
works, as the excerpts state them.

- **Autonomy, or modularity.** Each equation is "an independent mechanism"
  that "must be preserved as a separate mathematical sentence" (p. 420).
  The circuit diagram's power "comes from what early economists called
  autonomy. Namely, the gates in this diagram represent independent
  mechanisms – it is easy to change one without changing the other" (p.
  414).
- **A diagram that says which equation belongs to which variable.** "The
  diagram tells us which equation is to be deleted when we manipulate Y"
  (p. 417). Rewrite the equations into an algebraically equivalent pair and
  "there is no such thing as 'the equation for Y'", so the surgery is
  undefined ("impossible", slide 33, p. 417).
- **A cut between in and out.** "If you wish to include the entire universe
  in the model, causality disappears because interventions disappear – the
  manipulator and the manipulated lose their distinction" (p. 420). The
  choice of which variables are exogenous is the investigator's: "it is the
  way we carve up the universe that determines the directionality we
  associate with cause and effect" (p. 420).
- **A local intervention.** The intervention changes one mechanism and
  leaves the others alone. Structural parameters are invariant "to local
  interventions (i.e., changes in specific equations in the system) and not
  to general changes in the statistics of the variables" (pp. 161–162).
- **Nonparametric generality (§5.3.2).** In the example model (5.4)–(5.6),
  x = f₁(u, ε₁), z = f₂(x, ε₂), y = f₃(z, u, ε₃), the f's are "unknown
  arbitrary functions" and U, ε₁, ε₂, ε₃ are "mutually independent and
  arbitrarily distributed" (p. 155).

## Key results

### The surgery and the do() notation (§5.3.3, pp. 157–159)

- **Two covariance-equivalent models with different effects.** Model M,
  (5.7)–(5.9): x = u + ε₁, z = αx + ε₂, y = βz + γu + ε₃. Model M′,
  (5.12)–(5.14): x = ε₁, z = α′x + ε₂, y = β′z + δx + ε₃. With α′ = α,
  β′ = β and δ = γ they "yield the same probabilistic predictions", but
  "when viewed as data-generating mechanisms, the two models are not
  equivalent" (p. 157).
- **The computation.** Substituting X = x into the remaining equations, M′
  gives E[Y | do(X = x)] = (β′α′ + δ)x (5.16) and M gives βαx (5.18) (p.
  157). The posted PDF prints M′'s total effect as "βα + δ", with the δ in
  red over the printed text, which the text layer still holds as
  "βα + δγ". By (5.16) with β′ = β and α′ = α, βα + δ is right, so the red
  δ reads as the author's correction of the printed page.
- **Why u may not be substituted.** "Structural equations are not meant to
  be treated as immutable mathematical equalities. Rather, they are meant
  to define a state of equilibrium – one that is violated when the
  equilibrium is perturbed by outside interventions" (p. 157). Under
  do(X = x), "the equation x = u + ε₁ ... should be overruled and replaced
  with the equation X = x" (p. 158). So structural equations "stand not for
  one but for many sets of equations, each corresponding to a subset of
  equations taken from the original model" (p. 158).
- **The notation.** E(Y | do(x)) ≜ E[Y | do(X = x)] is "the controlled
  expectation" (5.19), and E(Y | x) ≜ E(Y | X = x) is "the standard
  conditional or observational expectation" (5.20) (p. 158).
- **Observing is conditioning.** "The passive observation X = x should not
  violate any of the equations, and this is the justification for
  substituting both (5.7) and (5.8) into (5.9) before taking the
  expectation" (p. 158). In M, E(Y | do(x)) = αβx, while
  E(Y | x) = r_YX x = (αβ + γ)x. The page prints the last term as "y"; by
  (5.11), γ = r_YX − αβ, so γ is meant.
- **The nonparametric case.** E(Y | do(x)) = E{f₃[f₂(x, ε₂), u, ε₃]}, with
  f₁ "wiped out" (pp. 158–159). Identification means answering such
  queries "uniquely, from the data and the graph", as Definition 3.2.3 (not
  read) has it (p. 159).

### What structural equations mean (§5.4.1, pp. 159–163)

- **The paradox.** If β in y = βx + ε is the change in E(Y) per unit of X,
  rewriting gives x = (y − ε)/β, and 1/β "ought" to be the effect of Y on X.
  That conflicts with intuition and with the model (p. 159). Pearl rejects
  both textbook escapes: the purely statistical reading, and the
  "isolation" condition cov(X, ε) = 0, which every bivariate normal pair
  meets in both directions (pp. 159–160).
- **Definition 5.4.1 (structural equations).** "An equation y = βx + ε is
  said to be structural if it is to be interpreted as follows: In an ideal
  experiment where we control X to x and any other set Z of variables (not
  containing X or Y) to z, the value y of Y is given by βx + ε, where ε is
  not a function of the settings x and z" (p. 160).
- **The equality sign is asymmetric.** Structural equations "act
  symmetrically in relating observations on X and Y (e.g., observing Y = 0
  implies βx = −ε), but they act asymmetrically when it comes to
  interventions (e.g., setting Y to zero tells us nothing about the relation
  between x and ε)" (p. 160).
- **The empirical claim of a missing variable.** Excluding a variable from
  the right-hand side is a testable invariance,
  P(y | do(x), do(z)) = P(y | do(x)) for all Z disjoint from {X ∪ Y} (5.23).
  "In contrast, regression equations make no empirical claims whatsoever"
  (p. 160). The invariance "holds relative to manipulations, not
  observations, of Z": P(y | do(x), z) "would certainly depend on z if the
  measurement were taken on a consequence (i.e., descendant) of Y" (p. 161).
- **The structural parameter.** β = ∂E[Y | do(x)]/∂x (5.24), "the rate of
  change (relative to x) of the expectation of Y in an experiment where X is
  held at x by external control". It "has nothing to do with the regression
  coefficient r_YX" (p. 161).
- **The error term.** ε = y − E[Y | do(x)] (5.25), the deviation from the
  controlled expectation, not from E[Y | x] (p. 162). Error correlations are
  E[ε_Y ε_X] = E[YX | do(pa_Y, pa_X)] − E[Y | do(pa_Y)]E[X | do(pa_X)]
  (5.26), and ε_Y, ε_X are uncorrelated iff
  E[Y | x, do(s_XY)] = E[Y | do(x), do(s_XY)] (5.27) (p. 162).
- **But think in omitted factors.** The operational definition "prescribes
  how errors are measured, not how they originate". Judging whether errors
  correlate needs the omitted-factors conception, because the assessments
  (5.26) asks for "are cognitively unfeasible" (p. 163). Bidirected arcs
  "should be assumed to exist, by default, between any two nodes", and
  deleted only with justification (p. 163).
- **Counterfactual content.** Footnote 17 adds that an equation also makes
  "a dynamic or counterfactual claim: If we were to control X to x′ instead
  of x, then Y would attain the value βx′ + ε", testable only if ε stays
  unaltered, and "such counterfactual claims constitute the empirical
  content of every scientific law" (pp. 160–161).

### The Epilogue (pp. 401–428)

- **Two riddles** (pp. 406–407): how people acquire causal knowledge, given
  that "correlation does not imply causation", and what difference it makes
  to be told that a connection is causal.
- **The logic bug** (p. 413). Given "If the grass is wet, then it rained"
  and "If we break this bottle, the grass will get wet", a program concludes
  "If we break this bottle, then it rained."
- **The three ideas** (p. 414): "treating causation as a summary of behavior
  under interventions"; "using equations and graphs as a mathematical
  language"; and "treating interventions as a surgery over equations".
- **Surgery on the multiplier–adder circuit** (pp. 416–417, slide 33).
  Y = 2X, Z = Y + 1: setting Y = 0 deletes Y = 2X and gives Z = 1. The
  reversed pair X = Y/2, Y = Z − 1 gives X = 0 and leaves Z unconstrained.
  The equivalent pair 2X − 2Y + Z − 1 = 0, 2X + 2Y − 3Z + 3 = 0 admits no
  surgery. The definition drawn from it: "Y is a cause of Z if we can change
  Z by manipulating Y, namely, if after surgically removing the equation for
  Y, the solution for Z will depend on the new value we substitute for Y"
  (p. 417). The idea of "wiping out" equations is credited to Herman Wold in
  1960 (p. 417).
- **Randomized experiments** (p. 418). Fisher's experiment is
  "randomization and intervention". Intervention is surgery: "we are
  severing one functional link and replacing it with another. Fisher's great
  insight was that connecting the new link to a random coin flip guarantees
  that the link we wish to break is actually broken."
- **Policy evaluation** (pp. 418–419). The task is "to infer the behavior of
  this mutilated model from data governed by a nonmutilated model". Taxation
  "is an endogenous variable during the model-building phase and turns
  exogenous only when evaluated."
- **Russell's enigma** (pp. 419–420). The equations of physics are
  symmetric, but "A causes B" and "B causes A" compare two models, one with
  A's equation removed and one with B's.
- **Equational against causal models** (pp. 420–421, slide 39). Both use
  symmetric equations for normal conditions. The causal model adds "(i) a
  distinction between the in and the out; (ii) an assumption that each
  equation corresponds to an independent mechanism and hence must be
  preserved as a separate mathematical sentence; and (iii) interventions
  that are interpreted as surgeries over those mechanisms."
- **Observation and intervention** (p. 421). "Scientific activity, as we
  know it, consists of two basic components: Observations [40] and
  interventions [41]. The combination of the two is what we call a
  laboratory". Standard algebras, probability among them, "are geared to
  serve observational sentences but not interventional sentences."
- **The do-calculus** (pp. 422–423, slide 45). Three rules, each licensed
  by a d-separation condition in a modified graph. Rule 1, "Ignoring
  observations": P(y | do{x}, z, w) = P(y | do{x}, w) if
  (Y ⫫ Z | X, W) in G_X̄. Rule 2, "Action/observation exchange":
  P(y | do{x}, do{z}, w) = P(y | do{x}, z, w) if (Y ⫫ Z | X, W) in G_X̄Z̲.
  Rule 3, "Ignoring actions": P(y | do{x}, do{z}, w) = P(y | do{x}, w) if
  (Y ⫫ Z | X, W) in G_X̄,Z̄(W). In words: "The first allows us to ignore an
  irrelevant observation, the third to ignore an irrelevant action; the
  second allows us to exchange an action with an observation of the same
  fact" (p. 422). The graph notation is not explained in the Epilogue, and
  its definitions are in §3.4 (not read).
- **Smoking, tar and cancer** (pp. 423–424, slide 46). With an unobserved
  genotype, P(c | do(s)) is "noncomputable". With tar deposits measured as
  a mediator it is computable, and the derivation eliminates every "do" to
  reach "a formula involving no 'do' symbols". Pearl adds that this does not
  settle the debate, since the model assumes "no direct link between smoking
  and lung cancer unmediated by tar deposits" (p. 424).
- **Simpson's paradox and the adjustment problem** (pp. 425–427): the
  Berkeley admissions case, "reverse regression", and a graphical test of
  whether measurements Z₁, Z₂ suffice for adjustment, shown on slides 51–56
  and not reproduced in the text.

## Concepts

- **Intervention, do(x).** The surgery that replaces the equation for X by
  X = x and solves the rest (pp. 158, 417). Read "given that we do" (p.
  421).
- **Observation, conditioning.** "Given that we see" (p. 421). A passive
  observation violates no equation (p. 158).
- **Structural equation.** Definition 5.4.1 (p. 160): a claim about Y under
  ideal control of X and any other variables. It is distinct from an
  algebraic or regression equation.
- **Autonomy.** Mechanisms can be changed one at a time (p. 414).
- **Control query and observational query.** "What would be the change in
  the expected value of Y if we were to intervene and change the value of Z
  from z to z + 1?" against "What would be the difference in the expected
  value of Y if we were to find Z at level z + 1 instead of level z?" (p.
  158).
- **Mutilated model.** The model after surgery (p. 419).
- **Terminology.** The excerpts say "structural equation models", "causal
  models" and, in the contents, "functional causal models" (§1.4). The
  phrase "structural causal model" does not occur in them.

## Connections

- **Wold, Haavelmo, Marschak and Simon.** Pearl credits the wiping-out of
  equations to Wold, 1960 (p. 417), and the policy reading of structural
  equations to Haavelmo 1943, Marschak 1950 and Simon 1953 (p. 158). The
  invariance idea behind (5.23) goes back to Marschak and Simon, and is
  formalised in Hurwicz, Mesarovic, Sims, Cartwright, Hoover and Woodward
  (footnote 16, p. 160).
- **Cartwright's capacities** (pp. 161–162). β is invariant to local
  interventions, not to "general changes in the statistics of the
  variables". So her ratio E(YX)/E(X²) stays constant only when X's own
  mechanism is changed.
- **Fisher's randomized trial,** read as surgery in which a coin is the new
  mechanism (p. 418).
- **The record's interventionist vocabulary.** [TERM-018](../terms.d/TERM-018.md) defines a framing
  intervention as "an action that changes the conditions under which an
  utterance is interpreted". That is Pearl's sense of intervention, applied
  to the variable for what the interpreter is told.

## Bearing on the record

The record cites the book for one thing: the definition of do(). It does so
in [CLAIM-127](../claims.d/CLAIM-127.md) (version 2) and [CLAIM-tmp2i7yj](../claims.d/CLAIM-tmp2i7yj.md).

- **"Observing a value and conditioning on it are one operation"
  ([CLAIM-127](../claims.d/CLAIM-127.md), version 2 history).** The excerpts support this. The
  conditional bar is "given that we see" (p. 421), E(Y | x) is "the
  standard conditional or observational expectation" (p. 158), and the
  Epilogue's two components are observations and interventions (p. 421).
  There is no third operation in the excerpts. The review's triad of
  "observation, conditioning, and intervention" is not Pearl's.
- **The gloss of do().** The LIT's key takeaway ("replacing X's structural
  equation, the other equations left in place") matches pp. 158 and 417
  in substance. Two qualifications from the excerpts sharpen
  it.
  - *The variable must have an equation.* Surgery deletes "the equation for"
    the variable, which presupposes autonomy and a diagram that assigns
    each equation to its variable (pp. 414, 417, 420). In A129's model as
    [CLAIM-127](../claims.d/CLAIM-127.md) quotes it, R′ = f_R(R, Z, I, ε_R) and Y = f_Y(R′, Z, C, ε_Y),
    the framing variable I is "externally supplied" and has no equation.
    So do(I = a) sets an exogenous input. [CLAIM-tmp2i7yj](../claims.d/CLAIM-tmp2i7yj.md)'s "do(I = a)
    replaces I's" equation is accurate only once how I is chosen is
    modelled.
  - *For an exogenous, unconfounded variable, seeing and doing coincide.*
    This is my inference, not a sentence of the excerpts. It applies Rule 2
    (p. 423), whose condition holds trivially for a parentless I that shares
    no cause with the rest of the model, and it is the sense of p. 418,
    where a coin-assigned treatment "guarantees that the link we wish to
    break is actually broken". So in an experiment that assigns I,
    P(Y | I = a) = P(Y | do(I = a)). The do() notation for I separates
    something only when I is not assigned, as in corpora where framing
    co-varies with the situation. That leaves [CLAIM-127](../claims.d/CLAIM-127.md)'s structural
    point (index the empirical model by a, do not add a to the cover) and
    [CLAIM-tmp2i7yj](../claims.d/CLAIM-tmp2i7yj.md)'s distinction (do(I) against do(S), a difference of
    variable) untouched. It narrows where the operator itself does work.
- **"Nor does it say Pearl's calculus applies as it stands" ([CLAIM-127](../claims.d/CLAIM-127.md)).**
  The excerpts agree that identification is the hard part. The surgery is
  "well defined" even for unknown f's (p. 158), but answering
  do-queries "uniquely, from the data and the graph" is a further
  question (p. 159), and the smoking example shows a do-query that is
  "noncomputable" (p. 423).
- **Elicitation as measurement within an intervention.** §5.4.1 separates
  conditioning on a measurement taken under an intervention,
  P(y | do(x), z), from intervening on it, P(y | do(x), do(z)), and notes
  the first depends on z when Z is a descendant (p. 161). That is the shape
  of [CLAIM-127](../claims.d/CLAIM-127.md)'s e_C^a = P(Y_C | do(a)) when C is an elicitation and the
  question is whether eliciting one judgement is itself a do() on the
  interpreter's state.
- **No THEORY is filed or touched.** A skim of definitional excerpts grounds
  no claim about language or interpretation.
- **No instruction for machine-learning practice,** so nothing for the
  Anthology.
- **Tags.** `causality` first. `probabilistic-modeling` for the conditional
  probability and the graphical machinery. `philosophy-of-science` for the
  Epilogue's account of causation, Hume and Russell, and for §5.4.1 on what
  the equations of a science claim.

## Limitations

- 46 pages of some 480. None of chapters 1–4 or 6–11 was read. The
  definitions the Epilogue and §5 rely on (Definition 3.2.3, the
  back-door and front-door criteria, the graph notation of the three rules,
  the counterfactual semantics of chapter 7) were seen only by name.
- The Epilogue is a 1996 lecture written for a general audience. It states
  results, does not prove them, and relies on slides some of which are not
  reproduced in the text (51–56).
- §5.3.2–5.4.1 is about linear structural equation models in social science
  and economics. Its general claims are illustrated on three-variable
  linear examples.
- Extraction was imperfect. Equations were read from page images where the
  text layer failed, and p. 154 is overlaid by an author's note.
- No hierarchy of association, intervention and counterfactual appears in
  these pages. Whether the book states one elsewhere was not checked.

## Open questions

- **Sequential interventions.** [CLAIM-127](../claims.d/CLAIM-127.md) notes that the composition
  K_bK_a needs time-indexed states. The contents list §4.4, "The
  Identification of Dynamic Plans", with a "Sequential Back-Door Criterion"
  (§4.4.3, p. 121). Does it treat a sequence of interventions on one
  interpreter, or only plans over distinct variables?
- **Is telling a do()?** The contents list §11.4.3, "Can do(x) Represent
  Practical Experiments?", §11.4.4, "Is the do(x) Operator Universal?",
  §11.4.5, "Causation without Manipulation!!!" and §11.4.7, "The Illusion
  of Nonmodularity". These look like the places where the book says when an
  instruction to a subject counts as surgery.
- **Utterances.** §7.2.3 is titled "Causal Explanations, Utterances, and
  Their Interpretation" (p. 221). What it says about interpreting causal
  utterances bears directly on the record's interpretive programme and was
  not read.
