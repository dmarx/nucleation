---
number: 402
status: Active
formerly:
- CLAIM-tmpeftzb
title: 'Predictive success of a category across contexts warrants treating it as a real effective kind only when the evidence in those contexts does not pass through the category''s own use, or when the effect of that use is modelled: a category that speakers or institutions act on can produce the regularities that confirm it, and contexts that share its use are not independent'
version: 7
history:
- version: 2
  date: '2026-10-21'
  note: >-
    The readings of 2026-10-21 added: Perdomo et al. (THEORY-861,
    THEORY-839) and Espeland and Sauder (THEORY-862,
    THEORY-854) are now read; grounds gain THEORY-839,
    THEORY-862 and THEORY-854. The claim is unchanged.
- version: 3
  date: '2026-10-29'
  note: >-
    THEORY-854 moved from grounds to corroborated_by (ADR-058): cited as
    a documented instance of the loop, not a premise; THEORY-862 holds
    what was reported.
- version: 4
  date: '2026-10-29'
  note: >-
    THEORY-036 removed from grounds by the fifteenth status review
    (ADR-058), at the status review's ruling (the owner delegated these
    rulings): the body cites it only under "What it does not say", for
    A27's conclusion, which this claim does not draw. The body citation
    stays. The claim is unchanged.
- version: 5
  date: '2026-10-29'
  note: >-
    Promoted by the sixteenth status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings). THEORY-273
    moves from grounds to corroborated_by (ADR-058): the body cites it
    only under "What it does not say", and the argument runs through
    CLAIM-342, THEORY-839, THEORY-862 and CASE-103, all Active. No
    objection is on file, and nothing held meets the defeat condition.
    The claim is unchanged.
- version: 6
  date: '2026-11-24'
  note: >-
    Joins the work governance-of-becoming under ADR-104's rule, as
    stated or used in A49 Article 7 illustrative case (ADR-147). No
    change of title or status.
- version: 7
  date: '2026-11-25'
  note: >-
    Joins the work hyperarticles (ADR-145): Article 3 of A45 in the
    exchange "Hyper article interpretation" states its proposition or uses
    it as a step, in §8. No other change.
role: thesis
warrant: interpretive
defeated_if: >-
  A category whose use by speakers or institutions demonstrably changes
  what they do, yet whose cross-context predictive success is unaffected
  by controlling for that use, together with an argument that its success
  is then evidence of kindhood for such categories in general. Or a
  showing that communicative categories, as a class, are indifferent to
  being named and acted on.
tags:
- philosophy-of-science
- metaphysics
- social-ontology
date: '2026-10-21'
line:
- pragmatic-transport
- learning-and-inquiry
works:
- hyperarticles
- governance-of-becoming
rests_on:
- CLAIM-342
grounds:
- CASE-103
- THEORY-839
- THEORY-862
summary: >-
  A27 §1 of the exchange of 2026-10-20, on the owner's U27 ("are we perhaps
  better positioned now to address [QUESTION-007](../questions.d/QUESTION-007.md)? -009? -011? -028?"),
  after A26 §2's performative toy. It is the one criterion A27 added to
  A191's four on [QUESTION-028](../questions.d/QUESTION-028.md)'s page, and [NOTE-769](../notes.d/NOTE-769.md) anticipated it from
  Hacking's interactive kinds. [CLAIM-342](CLAIM-342.md)'s condition on evidence, moved from
  a judgement–observation loop to the warrant for a kind. The sharp edge:
  it defeats one inference and is not a criterion of kindhood, so
  [QUESTION-028](../questions.d/QUESTION-028.md) stays Open.
complements:
- CLAIM-416
- CLAIM-445
bears_on:
- QUESTION-028
---
<!-- inactive-ok-file: CLAIM-619 — Proposed; cited in the note of 2026-11-12 -->
<!-- inactive-ok-file: LIT-2533 — Deferred; filed from the exchange of 2026-11-12, unread -->
<!-- inactive-ok-file: CASE-222 — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: QUESTION-007 — Deferred; named only in the owner's question as quoted -->
<!-- inactive-ok-file: THEORY-854 — Proposed; Espeland and Sauder's validity-raising loop stated generally, cited beside the Active reading of the study as corroboration, not as a ground -->
<!-- inactive-ok-file: THEORY-273 — Proposed; corroborates this claim, cited under what it does not say -->

# CLAIM-402: Predictive success of a category across contexts warrants treating it as a real effective kind only when the evidence in those contexts does not pass through the category's own use, or when the effect of that use is modelled: a category that speakers or institutions act on can produce the regularities that confirm it, and contexts that share its use are not independent

## The claim

The owner, at U27: "are we perhaps better positioned now to address
[QUESTION-007](../questions.d/QUESTION-007.md)? -009? -011? -028? -029? -032? etc." A27 §1, on [QUESTION-028](../questions.d/QUESTION-028.md):
"**Cross-context predictive success may still be insufficient evidence of
an independently projectible kind if the supposedly independent contexts
reproduce the same classification-dependent institutional arrangements.**
For example, evaluating a classification at several institutions does not
necessarily establish independence if all those institutions adopt the
same categories and allocate opportunities accordingly." Its fourth
criterion: "Its success is not exhausted by the institution's own use of
the category generating the outcomes against which it is evaluated", or
"an explicit causal account of those effects where independence is
impossible."

**The mechanism.** A26 §2's toy, checked here: an institution's
classification θ ∈ {0, 1} sets its policy, P(Y = 1 | θ = 0) = 0.1 and
P(Y = 1 | θ = 1) = 0.9, and it updates θ_{t+1} = 1[P(Y = 1 | θ_t) > 0.5].
Both θ = 0 and θ = 1 are fixed points, each "consistent with the behavioral
evidence generated under that classification". A26: "Neither fixed point,
by itself, establishes what would have occurred under a different
policy." A26 called the update "a toy model rather than a claimed theorem
from Perdomo et al."

Perdomo et al., read on 2026-10-21 ([NOTE-1044](../notes.d/NOTE-1044.md)), bear it out. Repeated
retraining has a unique stable point only when the loss is strongly convex
and the deployment's effect small enough ([THEORY-861](../theory.d/THEORY-861.md)); a threshold
rule is not strongly convex, so the toy's two stable points are consistent
with the theorem and outside it. And a stable point need not be optimal
([THEORY-839](../theory.d/THEORY-839.md)): self-consistent for the world its own use makes, it can
be worse than an alternative that would have produced different evidence.
That is this claim's reason to model the effect of use.

**A documented case.** Espeland and Sauder ([NOTE-1050](../notes.d/NOTE-1050.md)) define
self-fulfilling prophecy to include reactions "which increase the validity
of the measure by encouraging behavior that conforms to it", and report
channels that run through the ranking's own inputs: rank to yield to
selectivity, and past rank to the reputation survey ([THEORY-862](../theory.d/THEORY-862.md),
reported and corroborated; [THEORY-854](../theory.d/THEORY-854.md), Proposed, the loop stated
generally). Every school is under the same ranking, so the contexts that
confirm it are not independent, which is the claim's condition. The paper
does not cite Hacking's interactive kinds; the join with [NOTE-769](../notes.d/NOTE-769.md) is the
record's.

**The record's terms.** [CLAIM-342](CLAIM-342.md): what keeps a loop from confirming itself
is "evidence whose arrival or scoring does not pass through the
interpretation it tests". This claim applies that condition to the
evidence for a kind. The record already had the point for this question:
[NOTE-769](../notes.d/NOTE-769.md), reading Bird and Tobin, "Communicative categories are
classifications of human acts, so Hacking's interactive kinds apply: a
category used by speakers can change what they do. Any test of the kind
the question wants has to allow for that, or show the category is
indifferent to being named." [QUESTION-028](../questions.d/QUESTION-028.md)'s note of 2026-10-14 summarized
[NOTE-769](../notes.d/NOTE-769.md) without it. [CASE-103](../cases.d/CASE-103.md) is the record's instance: a fanbase's
reputation, acted on by members and outsiders, "can enter the process that
produces its own evidence".

So, of [QUESTION-028](../questions.d/QUESTION-028.md)'s own answer condition ("generalization to
realizations, media or speakers not used to define it, under probes chosen
independently of the category"): independence of the probes is not
enough. The realizations must also not be produced through the category's
use, or the use must be modelled.

## What it does not say

- **That it answers [QUESTION-028](../questions.d/QUESTION-028.md).** It is a condition on evidence, which
  defeats one inference. [QUESTION-028](../questions.d/QUESTION-028.md) asks for a criterion and for which
  parts are necessary. A27 declined the second ("candidate criteria, not
  five individually necessary conditions"), and this claim does not supply
  it. The question stays Open.
- **That a performatively stable category is false.** A26: "A
  performatively stable model isn't necessarily false, unjust, or
  captured." Its predictions can be right under the regime that produced
  them.
- **That success is no evidence.** [THEORY-273](../theory.d/THEORY-273.md): usefulness is "necessary but
  not sufficient" for a natural kind, and it does not deny that usefulness
  is evidence. A27's conclusion, a domain-relative kind and not a natural
  kind, is [THEORY-036](../theory.d/THEORY-036.md)'s and [THEORY-273](../theory.d/THEORY-273.md)'s.
- **Anything about a particular category or institution.** The toy is
  stipulated. Perdomo et al. and Espeland and Sauder, which A26 cited, were
  read on 2026-10-21; the first is a theorem about learning, and the second
  an interview study of law schools whose quantitative links are cited, not
  shown. Neither is a test of a category's kindhood.

## Note of 2026-10-24: two endogenous feedbacks in one derivative

From the exchange of 2026-10-24 (workbench entry of 2026-10-24, U22). Let a
deployed policy u_θ generate raw outcomes Y ∼ D_{u_θ}, read through a
legibility regime Z ∼ K_{r(θ)}(· | Y). The distribution learned from is
D̃_θ(z) = Σ_y K_{r(θ)}(z | y) D_{u_θ}(y), and by the product rule
dD̃_θ/dθ = Σ_y K_r(z | y) dD_{u_θ}(y)/dθ + Σ_y (dK_{r(θ)}(z | y)/dθ) D_{u_θ}(y):
performative change of the world sampled, and endogenous change of how it
is represented. Four nested settings follow: fixed world; legibility
feedback only ([CASE-124](../cases.d/CASE-124.md), [CASE-156](../cases.d/CASE-156.md)); performative only ([THEORY-861](../theory.d/THEORY-861.md),
[THEORY-839](../theory.d/THEORY-839.md)); both. The published convergence results for the third do not
carry over when K_r is dynamic and history-dependent. The two paths need
different interventions to separate: change the reporting regime with the
policy fixed, or change the policy with raw outcomes observed
independently.

## Note of 2026-10-29: what holds it back

Its remaining Proposed ground, [THEORY-273](../theory.d/THEORY-273.md), waits on readings of Lemeire
(2018) and Slater (2015). The body cites it only under "What it does not
say", as it cited [THEORY-036](../theory.d/THEORY-036.md), so the edge may be corroboration; the next
pass should rule on it.

## Note of 2026-11-07: the loop as an equation, and a third reading, from "Individuation, Possibility, and Disposition"

In the exchange "Individuation, Possibility, and Disposition" (2026-11-06 to 07), A41 §4 and §9 set Hacking's loop into the meaning–authority model as a fourth equation, z_{t+1} = Q(…), in which the classified population responds, and cited survey and qualitative evidence for parts of the loop (named in [CASE-222](../cases.d/CASE-222.md), not registered). A41 §9 added a third reading of later evidence beside prediction and causation: "the label is applied retrospectively to behavior that had independent causes." This supports the claim's warning; it does not test it, since no study cited separates the readings, and A says "The full causal loop therefore remains a research hypothesis." A did not cite this claim. No status changes.

## Note of 2026-11-12: the exchange "About Plantation Paradise"

A9 §4 of the exchange "About Plantation Paradise" (https://chatgpt.com/share/6af620a9-b0f8-83e8-8d25-b42434630c81, 2026-11-12), after Nurse, O'Toole and Darden's "Paradox of
Inclusivity" ([LIT-2533](../literature.d/LIT-2533.md), unread), cited this claim accurately as one
on "self-confirming classifications" and asked: "When does an
organization's interpretation of a participant's response alter the
conditions under which that participant's future behavior will be
evaluated?" In A's report of the paper, staff read disengagement as
individual deficiency, and the reading legitimates allocations that
confirm the assumptions behind it. The record holds the loop: this claim
(a category that institutions act on can produce the regularities that
confirm it), [CASE-142](../cases.d/CASE-142.md) (a label confirmed by the response of someone who
rejects it) and [CLAIM-619](CLAIM-619.md) (a challenge classified as the problem). The
question is not filed separately. No status changes.

## Note of 2026-11-19: Carnap, read

An analogy from Carnap ([NOTE-2110](../notes.d/NOTE-2110.md), result 13), not evidence: a confirmation function's own estimates of its reliability "cannot be used as a method for obtaining an external, objective judg- ment on the goodness of a system of inductive logic" (§103). Evidence for a concept's adequacy that passes through the concept's own use is the case this claim excludes. [ADR-107](../decisions.d/ADR-107.md) now asks the same of an explication. The claim is unchanged.

## Note of 2026-11-19: Krohn and Weninger, read
A parallel ([NOTE-2140](../notes.d/NOTE-2140.md)): a link to a subreddit that does not yet exist is a name whose use can bring about its referent, and links to existing subreddits are as often reactive as proactive, so any measure built from links is endogenous in the way this claim warns of.

## Note of 2026-11-22: Merton's Matthew effect, read

**A parallel** ([LIT-3002](../literature.d/LIT-3002.md), [NOTE-2268](../notes.d/NOTE-2268.md)). Merton reads the Matthew effect
as "a special application of the self-fulfilling prophecy" (p. 61, citing
[LIT-1398](../literature.d/LIT-1398.md) in note 42): a scientist's standing, a category institutions act
on, draws the attention and credit that then confirm the standing, "a
self-confirming process" (p. 62). It is a further instance of this
claim's category whose use produces the regularities that confirm it, in
recognition rather than in kinds. Status unchanged; no edge.

## Note of 2026-11-24: the exchange 'Memes, Contracts, and Systemic Normativity', A11

<!-- inactive-ok-file: CLAIM-426 — Proposed; cited as A11 cites it -->

A11 §11 cites this claim, with [CLAIM-426](CLAIM-426.md), for bias "participating in the
production of reality", where "The attribution can become accurate while
its original evidential grounds remain inadequate"; the citation is right.
A11 §14 applies the same structure, without citing it, to ecological
rationality: "A cognitive organization may appear well adapted to its
environment partly because it has transformed that environment to
accommodate its existing constraints." That is this claim's condition for a
heuristic: its fit to an environment its own use helped make warrants
little about its adaptation unless the evidence of fit does not pass
through that use. Bearing: an extension to heuristics, held here rather
than filed apart ([ADR-072](../decisions.d/ADR-072.md)). The claim is unchanged.

## Note of 2026-11-24: the exchange 'Memes, Contracts, and Systemic Normativity', A44 §5

<!-- inactive-ok-file: CLAIM-1268 CLAIM-1340 — Proposed; filed from A42 and A48 of the exchange 'Memes, Contracts, and Systemic Normativity' -->

A44 §5, on the owner's U28 ("the tyranny of metrics"), restates this claim
for public rankings after Espeland and Sauder ([NOTE-1050](../notes.d/NOTE-1050.md)): "The metric can
become more predictive because the organization has increasingly
reorganized itself around the metric", so "**Improved correspondence
between a measure and its object does not establish that the measure was
originally adequate, or that the resulting transformation is
desirable.**" It separates "predictive validity, independently grounded
evaluative validity, and performatively produced agreement", which names
the three things the claim's condition keeps apart. Two filings of the
exchange apply the pattern: monitoring that produces the conformity it
records ([CLAIM-1268](CLAIM-1268.md)) and a reading of fiduciary duty that produces the
character later cited as legal necessity ([CLAIM-1340](CLAIM-1340.md)). Bearing:
support by restatement, and two applications. The claim is unchanged. The wording of this note is the assistant's (Claude, in this session), reporting A's (ChatGPT's) text; adopting what it reports is the owner's call.
