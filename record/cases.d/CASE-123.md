---
number: 123
status: Active
formerly:
- CASE-tmp3uarw
title: 'The regulator and two accounts: a formally independent regulator weighs two parties'' accounts of a risk, one party comes to supply more of the evidence it reads and the experts it trusts, and the credibility that party gains decides whose evidence is read next; with variants for a one-time perturbation, a press as the evaluator, and an objective that gives one property no weight'
version: 2
history:
- version: 2
  date: '2026-10-21'
  note: >-
    From the readings of 2026-10-21: the documented episodes the replies
    cited are now read (THEORY-851, THEORY-850, THEORY-837),
    except Stigler's, Unavailable; none has the case's loop. The case is
    unchanged.
standing: stipulated
kind: thought-experiment
tags:
- society-and-governance
- self-governance
date: '2026-10-21'
line: distributed-agency
variant_of:
- CASE-099
illustrates:
- CLAIM-404
- CLAIM-330
- CLAIM-340
summary: >-
  A20 §2 of the exchange of 2026-10-20, on the owner's U20 ("reflexive
  control and regulatory capture"), with A21 §3's press variant on the
  owner's U21 and A26 §4's evaluative variant. [CASE-099](CASE-099.md)'s linearization
  with institutional roles: m is the lean of the regulator's reading, a
  the standing of the party it favours. A20: "This is an application of
  the formal model, not an established empirical account of any
  particular regulatory agency." No regulator, outlet or party is meant.
---
<!-- inactive-ok-file: LIT-1324 — Unavailable; Stigler, named as a source the replies cited that no lawful copy reached -->

# CASE-123: The regulator and two accounts: a formally independent regulator weighs two parties' accounts of a risk, one party comes to supply more of the evidence it reads and the experts it trusts, and the credibility that party gains decides whose evidence is read next; with variants for a one-time perturbation, a press as the evaluator, and an objective that gives one property no weight

## The case

A20 §2: "Imagine a regulator weighing two competing accounts of an
industry's risks. At first, both have comparable standing. One industry's
representatives gain an initial informational advantage: perhaps they
have better access to the regulator, provide more relevant technical
material, or frame the problem in terms the regulator already favors.
That interpretive advantage increases their credibility. Credibility then
yields greater influence over which evidence the regulator considers and
which experts it trusts. If subsequent credibility is assessed through the
increasingly dominant interpretation, an endogenous amplification loop
becomes possible."

Held fixed: the regulator's formal procedure, its authority to decide, and
its inferential competence. It updates correctly on what it reads. Varied:
who supplies the evidence and how the evidence is read.

In [CASE-099](CASE-099.md)'s terms, m is the lean of the regulator's reading toward one
account, and a the standing of the party that account favours. β is that
standing shaping what is read (whose material, whose experts). γ is the
reading shaping whom the regulator credits. The symmetric state is
unstable when βγ > (1 − α)(1 − δ) ([CLAIM-330](../claims.d/CLAIM-330.md)). If the regulator scores
the parties against evidence that the favoured party supplies, so that the
prevailing reading bends the evidence more than it bends the parties'
predictions, κ′ > κ̄, and γ > 0 ([CLAIM-340](../claims.d/CLAIM-340.md)). If it scores them against
evidence neither controls, γ is near zero or negative.

**Variants.**

- **A one-time perturbation** (A20 §3, reflexive control). An outside
  actor shifts the regulator's reading once, m₀ → m₀ + ε. "If the target's
  interpretive and authority dynamics are stable, that perturbation may
  disappear. But if the interpretation–authority loop is unstable, the
  perturbation can grow. The influencing actor need not continuously
  control the regulator's decisions."
- **A press as the evaluator** (A21 §3). The evaluator is a newsroom whose
  conditions of production the evaluated party's decisions affect, and the
  loop runs between two institutions: "Public interpretation → Political
  and regulatory decisions → Distribution of resources and authority →
  Conditions of future media production → Public interpretation." A21:
  "the potentially captured institution is **the institution that should
  help evaluate another institution's exercise of authority**."
- **An objective that gives one property no weight** (A26 §4). The
  regulator has all the evidence, and decides by
  U_λ(a) = v₁(a) + λv₂(a) with λ = 0. "Even perfect information about both
  properties does not ensure the regulator will consider the second." No
  evidence is selected; the criteria are.

## What it can show

That each route the claim it illustrates names is coherent: influence on
an evaluator's decisions with no decision issued to it, through the
evidence it reads, through how that evidence is read, or through the
weights of its objective, while its procedure stays formally its own. A20
§3 ends: "**An intervention from outside the organization can alter its
internal allocation of practical authority, after which the organization
reproduces the altered allocation through processes that appear to be its
own.**" The checks belong to [CASE-099](CASE-099.md) and [CASE-106](CASE-106.md). The two constructions
of the third variant are elementary and were checked: with λ = 0 the
argmax does not depend on v₂, and with U fixed, a* moves with the
evidence.

## What it cannot show

- That any regulator, newsroom or industry behaves this way. It is
  stipulated. A21's caption: "A possible structural mechanism, not a claim
  that any particular outlet or institution follows these dynamics." The
  documented episodes the replies cited were read on 2026-10-21, except
  Stigler's ([LIT-1324](../literature.d/LIT-1324.md), Unavailable). The press variant now has two
  documented instances and one model, none with this case's loop.
  Di Tella and Franceschelli's Argentine newspapers give an association
  within newspaper and presidency, and A21's caution, "evidence of an
  association, not by itself proof of a particular covert intent", still
  applies ([THEORY-851](../theory.d/THEORY-851.md)). Szeidl and Szucs's Hungarian media give
  two-way favors at five events, with private advertisers as control
  ([THEORY-850](../theory.d/THEORY-850.md)); when the 2015 fallout cut the reward, content favors
  stopped after a lag, a dependence that did not sustain itself once the
  resource link was cut, which in that instance counts against the
  amplifying reading. Besley and Prat's model is a one-shot bargain, so it
  has the press variant's dependence and not its loop ([THEORY-837](../theory.d/THEORY-837.md)).
  Schram and Ule's regulators are a laboratory study, not a documented
  episode ([THEORY-856](../theory.d/THEORY-856.md)). No variant of this case with a documented
  loop has been read.
- That the loop between institutions is unstable under any stated
  condition. [CLAIM-330](../claims.d/CLAIM-330.md) is a 2×2 linearization of one organization, and the
  two-institution loop has not been derived.
- That the favoured party's account is wrong. A20 §9: "such a feedback loop
  may also reflect genuine learning, merited expertise, and beneficial
  specialization. Only independent standards and causal evidence can
  distinguish those from inappropriate capture."
