---
number: 115
status: Active
formerly:
- TERM-tmpuc919
title: 'scenario-conditioned response readiness: the probability that an organization operating under a specified policy can deliver an effective response to a specified contingency within its deadline'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Adopted at the status review's ruling (the owner delegated these
    rulings; ADR-057): the definition is settled and every entry that
    uses it (CLAIM-587, and the questions, cases and terms that cite
    it) names it, so says which sense of readiness it means. A's
    wording is kept.
tags:
- operations-research
- agency
- causality
date: '2026-11-04'
line:
- readiness
complements:
- TERM-055
summary: >-
  A's proposal, from the exchange on emergency readiness (2026-11-04; its
  share link could not be fetched, and its text was pasted by the owner),
  section 4 of A's "Proposed additions to Nucleation PR [#401](https://github.com/dmarx/nucleation/issues/401)", where A
  named it "scenario-conditioned operational readiness". Renamed on
  filing, to keep it apart from [TERM-055](TERM-055.md)'s operational availability and
  [TERM-094](TERM-094.md)'s action readiness. R^π_O(c, τ | s) is the probability of an
  effective response by τ when contingency c is imposed on organization O
  in state s under its actual policy π. It is a family indexed by
  contingency, not one number. The wording is A's; adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-198 — Proposed or new; entries of 2026-11-05 from the pasted synthesis on constraint architectures, cited as open -->

# TERM-115: scenario-conditioned response readiness: the probability that an organization operating under a specified policy can deliver an effective response to a specified contingency within its deadline

## Definition

  R^π_O(c, τ | s) = Pr_π(effective response by τ | do(c), s),

with c an imposed contingency, τ its deadline, s the organization's
initial state, and π the response policy the organization actually
follows. The do(c) is the point: this is readiness for a specified
situation, imposed, not success conditional on the situations that
happened to be observed. An organization that never met c has a value of
R for it all the same.

**No single scalar.** The object is the family
{R^π_O(c, τ_c | s) : c ∈ C}, one value per contingency and its deadline.
Two organizations' readiness profiles can be incomparable, each more
ready for some contingencies than the other.

## What it is not

- **Operational availability ([TERM-055](TERM-055.md)).** That is the chance that a
  resource is deployed for a task before the deadline, given the cue
  actually supplied, taking the supremum over the procedures available.
  This term is about an organization's effective response under a
  specified policy, which includes recognizing the contingency,
  mobilizing for it and performing successfully, and it takes the policy
  as followed, not the best one available. So a system can have the
  equipment and the personnel, each available in [TERM-055](TERM-055.md)'s sense, and
  low readiness, because its dispatch policy fails to mobilize them. The
  two are complements: availability of each resource is one factor of
  this term.
- **Action readiness ([TERM-094](TERM-094.md)).** Frijda's term is a state of an agent:
  a preparation for action that claims control over behaviour. This term
  is not a state at all but a probability, of an organization, for a
  contingency, and it says nothing about what claims control. An
  organization with no state of preparation can be ready in this sense,
  and one fully prepared can be unready for the contingency imposed.
- **Utilization or realized performance.** It is defined under
  intervention, so a record of what was done does not measure it.

## Note of 2026-11-05: A's resource models and further distinctions

The pasted synthesis on constraint architectures reads readiness as a resource-constrained transition capability: the probability, under policy, budget and architecture, of reaching a response configuration before the deadline without breaking constraints, with a planning problem that minimizes maintenance and expected operating cost subject to a floor on it. A: "Maintaining a specialized rescue unit is analogous to maintaining a mechanism that can be activated to reach an otherwise unavailable configuration before a deadline." See [CASE-198](../cases.d/CASE-198.md) and [QUESTION-392](../questions.d/QUESTION-392.md). The term is unchanged. No status changes.

## Note of 2026-11-23: the manuscript governance-of-possibility

<!-- inactive-ok-block: ADR-144 — Proposed; the work -->
Extension. A48 §6 of the owner's manuscript ([ADR-144](../decisions.d/ADR-144.md)) makes this term a
curve over the deadline, R_i(S, t), and says organizations "need not admit a
universal ranking" without saying when one exists. Since R_i(S, ·) is the
distribution function of the response time, two organizations are ranked the
same way at every deadline exactly when one curve lies at or above the other
at every time (first-order dominance); where the curves cross, which is more
ready is fixed only by the deadline. The condition is the assistant's
(Claude, in this session).

## Note of 2026-11-23: indexed by query and budget, from "Explain First Contact RL"

<!-- inactive-ok-block: CLAIM-1012 CLAIM-1003 CLAIM-1032 — Proposed, filed from A50 of the exchange "Explain First Contact RL" on 2026-11-23 -->
A50 §1 of the exchange "Explain First Contact RL" (ChatGPT, 2026-11-23) writes R_S(q; H, B), the probability that "an acceptable answer to q is realized by H within budget B" under the organization's actual policy, and calls it "a demand-relative extension" of this term: the contingency becomes a practical query, and a budget is added ([CLAIM-1012](../claims.d/CLAIM-1012.md)). Its §8 takes the superlevel set 𝓔(S) = {(q, H, B): R_S(q; H, B) ≥ 1 − η_q} as the organization's answer frontier, beside the inquiry frontier of [TERM-092](TERM-092.md) ([CLAIM-1003](../claims.d/CLAIM-1003.md)). The assistant's analysis of A50's interrogation game ([CLAIM-1032](../claims.d/CLAIM-1032.md)) finds that its strategic content is this term's setting, preparation chosen before the contingency is known. The term is unchanged.
