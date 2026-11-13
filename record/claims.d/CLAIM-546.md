---
number: 546
status: Active
formerly:
- CLAIM-tmp47w4i
title: 'Negative frequency dependence that keeps two types in coexistence does not make their interaction cooperative: in Hawk–Dove with cost C above value V each type increases when rare and they coexist at the interior equilibrium of V/C Hawks, with Hawks still taking the whole resource from Doves, and on the Black Queen account producers of a leaked good and the cells that use it without paying coexist at a frequency set by the community''s need; so whether types persist together and whether they cooperate are separate questions, and a coexistence criterion answers only the first'
version: 3
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted by the twenty-fifth status review (ADR-057), at the
    status review's ruling (the owner delegated these rulings).
    LIT-1219 leaves grounds: it is Unavailable, and Chesson's
    criterion is cited for its definition, so the body citation is the
    link (ADR-058). The Hawk–Dove computation was re-checked: the
    payoff difference is (V − pC)/2, positive as p → 0, negative as p
    → 1, zero at p* = V/C. THEORY-1048, THEORY-567 and CASE-118 are
    Active. No objection is on file, and nothing in the record meets
    the defeat condition. The claim is unchanged.
- version: 3
  date: '2026-11-11'
  note: >-
    Stale text corrected, from the ninth synthesis review of
    2026-11-11: the summary still said adopting the claim is the
    owner's call. The twenty-fifth status review promoted it on
    2026-11-06 (version 2), and the summary now says so. No other
    change.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the Hawk–Dove computation below, or a reading of the Black
  Queen account (THEORY-1048) on which the maintained beneficiaries pay
  for the good they use. Not defeated by coexistence that does involve
  cooperation, such as a mutualism: the claim is that coexistence does not
  imply cooperation, not that the two exclude each other.
tags:
- game-theory
- ecology
- altruism
date: '2026-11-04'
line:
- distributed-agency
- formal-apparatus
complements:
- CLAIM-547
- CLAIM-554
grounds:
- THEORY-1048
- THEORY-567
- CASE-118
bears_on:
- QUESTION-132
summary: >-
  From §3 of the synthesis "The Evolution of Cooperation: From
  Coexistence to Symbiosis to Morality", which the owner supplied on
  2026-11-04: "stable coexistence of strategies is not necessarily the
  same as stable cooperation: cooperators and defectors can coexist
  without eliminating exploitation". The record held the ecological half,
  invasion growth when rare ([CASE-118](../cases.d/CASE-118.md)), and a case of the point (the Black
  Queen, [THEORY-1048](../theory.d/THEORY-1048.md)). It did not hold the point itself. Hawk–Dove makes
  it exact. The wording is the reader's; the twenty-fifth status review
  adopted it on 2026-11-06.
---
<!-- inactive-ok-file: CASE-257 — filed from the exchange of 2026-11-12, Proposed -->
<!-- inactive-ok-file: LIT-1219 — Unavailable; Chesson's criterion, cited for the definition, not read here -->

# CLAIM-546: Negative frequency dependence that keeps two types in coexistence does not make their interaction cooperative: in Hawk–Dove with cost C above value V each type increases when rare and they coexist at the interior equilibrium of V/C Hawks, with Hawks still taking the whole resource from Doves, and on the Black Queen account producers of a leaked good and the cells that use it without paying coexist at a frequency set by the community's need; so whether types persist together and whether they cooperate are separate questions, and a coexistence criterion answers only the first

## The claim

Coexistence theory's test is mutual invasibility: each type must increase
when rare (Chesson, [LIT-1219](../literature.d/LIT-1219.md); [CASE-118](../cases.d/CASE-118.md) for two competitors). Evolutionary
game theory's test for cooperation is whether cooperators resist
defectors ([THEORY-567](../theory.d/THEORY-567.md)). The two tests can come apart.

**Hawk–Dove.** Contests over a resource of value V. A Hawk escalates, a
Dove displays and retreats, and an injury costs C > V. Payoffs to the row
player:

|        | Hawk         | Dove |
|--------|--------------|------|
| Hawk   | (V − C)/2    | V    |
| Dove   | 0            | V/2  |

With a fraction p of Hawks, a Hawk earns p(V − C)/2 + (1 − p)V and a Dove
earns (1 − p)V/2. Their difference is (V − pC)/2.

- **Both types increase when rare.** As p → 0 the difference tends to
  V/2 > 0, so Hawks invade. As p → 1 it tends to (V − C)/2 < 0, so Doves
  invade.
- **They coexist at p* = V/C**, where the difference is zero. That is
  coexistence by negative frequency dependence, in exactly coexistence
  theory's sense.
- **Exploitation is intact.** Every Hawk–Dove meeting at p* gives the
  Hawk V and the Dove 0. The mixture is stable, and the interaction it
  stabilizes is not cooperative.

**The Black Queen account** ([THEORY-1048](../theory.d/THEORY-1048.md)) gives the same thing in
microbes. Cells that lose a costly function whose product leaks are
favoured until the remaining producers just supply the community. The
loss is frequency dependent and stops short, so producers and
beneficiaries coexist. Most cells come to depend on the few, "with no
relatedness, cooperation or collective required".

So a criterion for whether types persist together does not settle
whether they cooperate. It settles whether either can exclude the other.

## What it does not say

- **That coexistence and cooperation exclude each other.** Mutualisms
  coexist and cooperate. The claim is only that the first does not imply
  the second.
- **That Nowak's rules are coexistence criteria.** They state when
  cooperators beat defectors ([THEORY-567](../theory.d/THEORY-567.md)), which can mean cooperators
  replace defectors, not that both persist.
- **Anything about mutualism and facilitation stabilizing coexistence.**
  The synthesis's §2 says positive interactions can stabilize coexistence.
  The record holds no work on that, and the work the synthesis cites
  there could not be identified (curation entry of 2026-11-04).

## Note of 2026-11-12: the exchange "About Plantation Paradise"

A6 §2 of the exchange "About Plantation Paradise" (https://chatgpt.com/share/6af620a9-b0f8-83e8-8d25-b42434630c81, 2026-11-12) cited this claim accurately ("Stable coexistence does not
imply cooperation") and applied it to the public theatres of colonial
Saint-Domingue, which now illustrate it ([CASE-257](../cases.d/CASE-257.md)): "The resulting
system might be artistically productive and organizationally stable. But
none of that establishes that the terms of participation were fair."

A6 separated five predicates the claim's lesson keeps apart:
contribution ("A participant's activity causally enables the
production"), dependency ("Withdrawing the contribution disrupts or
diminishes the production"), cooperation ("Participants coordinate toward
some shared activity or outcome"), exploitation ("One party benefits
through arrangements that violate a justified standard governing
another's labor, resources, or standing") and domination ("One party
holds power over the conditions under which another can act, contest, or
renegotiate the relationship"). The table is A's and is kept here, not
filed as terms: exploitation and domination, so defined, need a standard
the record does not supply ([CLAIM-363](CLAIM-363.md), [QUESTION-129](../questions.d/QUESTION-129.md)). No status
changes.
