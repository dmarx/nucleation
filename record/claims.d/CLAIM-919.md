---
number: 919
status: Proposed
formerly:
- CLAIM-tmp1jz5w
title: 'In a population of adaptive operators whose training follows influence, whether a rare-context specialist that loses its influence regains it is decided by whether spare capacity can take its niche in the meantime, not by whether it keeps its competence: with spare operators its niche is refilled and it stays shut out even with its competence intact, and without them nothing refills its niche and it returns even with its competence mostly lost'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-016, from the
    executed study CASE-341.
role: thesis
warrant: empirical
defeated_if: >-
  Reruns of CASE-341's suppression protocol find, with spare
  operators present, that a suppressed specialist whose training exposure
  was decoupled from its influence regains its niche where a coupled one
  does not. Or they find, without spare operators, that a specialist
  whose competence decayed fails to regain its niche against residents no
  better than it. The reruns may use other sizes, other numbers of
  contexts and operators, learned features, longer windows, or a
  marginalization the population produces itself rather than a clamp.
  Either result must hold across seeds and under at least two influence
  rules. A change of the competence threshold alone does not count.
tags:
- complex-systems
- learning-theory
- ecology
date: '2026-11-22'
line:
- distributed-agency
bears_on:
- QUESTION-134
- QUESTION-132
- QUESTION-083
grounds:
- CASE-341
summary: >-
  [QUESTION-134](../questions.d/QUESTION-134.md) asks whether influence-dependent training makes a
  marginalized specialist lose its competence, so that it cannot regain
  influence when its contexts recur. In [CASE-341](../cases.d/CASE-341.md) the answer turned
  on something else. The rare specialist's share was clamped at 10⁻³ for
  20,000 steps and then released, under four influence rules and 6 seeds.
  With two spare operators, a spare took the niche and became as
  competent as the specialist. The specialist failed to return in 23 of
  24 rule-seed pairs per arm, whether its training had been decoupled
  from its influence (competence kept) or coupled with a maintenance cost
  (competence mostly lost). It lost its competence afterwards, once
  coupled again. With no spare operator, nothing refilled the niche, and
  the specialist returned every time, even frozen with most of its
  competence gone. Loss of access cost competence only where maintenance
  had a cost. Loss of influence came from pre-emption, and loss of
  competence followed it. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-341 — new, filed with this claim -->
<!-- inactive-ok-file: CLAIM-875 — Proposed, filed 2026-11-22 by LEAD-065, cited for comparison; nothing here rests on it -->

# CLAIM-919: In a population of adaptive operators whose training follows influence, whether a rare-context specialist that loses its influence regains it is decided by whether spare capacity can take its niche in the meantime, not by whether it keeps its competence: with spare operators its niche is refilled and it stays shut out even with its competence intact, and without them nothing refills its niche and it returns even with its competence mostly lost

## The claim

[QUESTION-134](../questions.d/QUESTION-134.md) asks for three losses to be kept apart: loss of influence, of
competence and of access. It names a decisive result: a specialist whose
competence, lost through deprivation, does not return, against a control
whose access was decoupled. [CASE-341](../cases.d/CASE-341.md) separated the three. The
decisive result did not appear. What appeared instead:

- **Loss of access is not loss of competence unless maintenance has a
  cost.** With no weight decay, a specialist whose exposure fell to
  0.1–4.5% kept its held-out risk at 0.010 through 20,000 steps. Its
  operator has no interference, since it is not trained at all when it
  is not exposed. With decay, coupled access let its risk rise to 0.17
  (moe) or 0.73 (rep). Decoupled access held it at 0.013.
- **Competence is judged against whoever is there.** With no spare
  operator (K = 4), the residents stay with their own contexts and none
  learns the rare one. At release their risk on it was 1.75–1.97. The
  specialist, frozen at risk 0.73, regained its niche in 6 of 6 seeds
  under every rule.
- **Refill pre-empts recovery.** With two spare operators (K = 6), a spare
  took the niche during suppression and learned it, reaching risk
  0.010–0.013. At release the specialist had no advantage over it. It
  stayed shut out in 23 of 24 rule-seed pairs per arm, whether coupled or
  decoupled, whether with competence kept or lost. Removal shows the same
  from the other side. At K = 6 a removed specialist's niche was refilled
  in 6 of 6 seeds under every rule. At K = 4 it was refilled in 0 of 6.
- **The order is exclusion first, then incompetence.** A specialist
  decoupled during suppression came out with its competence (0.013). Once
  coupled again and shut out, it lost it, reaching 0.76 by the end of the
  window. [QUESTION-134](../questions.d/QUESTION-134.md)'s loop operates, but here it is the consequence of
  exclusion, not its cause.

## Two readings for the record's questions

These are alternatives, and the owner chooses.

- **Reading A: role regeneration, [QUESTION-132](../questions.d/QUESTION-132.md)'s first outcome at the
  level of roles.** The niche itself is robust. It is refilled after
  removal and kept filled through suppression. Only its holder is
  exchangeable. This is [CLAIM-875](CLAIM-875.md)'s Reading A, carried to a model
  whose operators have functions.
- **Reading B: a fourth outcome, which [QUESTION-132](../questions.d/QUESTION-132.md) does not name.** A
  specialist can be competent, retained and undamaged, and still be
  permanently displaced by an equally competent newcomer. Neither
  "stabilizing coexistence" nor "entrenched asymmetry" describes that. It
  is [CLAIM-875](CLAIM-875.md)'s Reading B, with a functional niche. For
  [QUESTION-134](../questions.d/QUESTION-134.md) it means that keeping a specialist's competence, the
  remedy the question's control tests, does not secure its access.

The assistant leans to B for the specialist and to A for the role. The
question as posed is about particular specialists.

## What it does not say

- It does not say that influence-dependent training never destroys
  competence. With a maintenance cost it did, in every coupled arm.
- It does not say anything about interference. In this model an operator
  that is not exposed is not trained. Operators with shared parameters
  across contexts could lose competence by being trained on other
  contexts, which is a different route.
- Suppression here is a clamp, an external marginalization. Whether a
  population marginalizes its own specialists, and with what spare
  capacity, was not tested.
- The result covers one model class, one size and 6 seeds. "Not
  recovered" means not within about 3,200 rare samples.
