---
number: 1357
status: Proposed
formerly:
- CLAIM-tmp3dn8p
title: 'Aligning each component does not align what they compose'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  An argument that alignment with one's principal is transitive up a chain
  of principals, so that a model aligned with its training signal, an
  assistant aligned with its deployer and a deployer aligned with its
  incentives jointly serve those the organization affects; or evidence that
  raising a component's fidelity to an organization whose objective departs
  from its constituents' interests does not increase the departure's
  effect.
tags:
- society-and-governance
- agency
- ethics
- philosophy-of-technology
date: '2026-11-26'
line:
- distributed-agency
- rightful-power
complements:
- CLAIM-060
- CLAIM-1398
statement: >-
  Alignment at one organizational level does not compose into alignment at
  the level above: a model aligned with its training signal, an assistant
  aligned with its deploying organization and an organization aligned with
  its financial incentives can together serve those it affects badly, and
  making the lower level more reliably aligned can make the higher level
  worse, because a faithful component amplifies whatever the organization
  it serves is directed at
summary: >-
  A6 §7 of the exchange "Alignment consequences brainstorm" (ChatGPT,
  2026-11-26), on the owner's U4 ([CLAIM-1398](CLAIM-1398.md)), which A2 §8 had put as
  "successfully aligning every individual component of an AI ecosystem
  might be insufficient to align the ecosystem they constitute". The
  record holds that an encompassing organization's success does not
  establish its constituents' good, and the converse ([CLAIM-060](CLAIM-060.md)), and that
  recursive delegation can amplify authority without self-grants
  ([SYNTHESIS-087](../syntheses.d/SYNTHESIS-087.md)); it holds no claim about alignment relations stacked
  across levels, or that fidelity below can worsen alignment above.
  Interpretive. The wording is A's; adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-1398 — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: SYNTHESIS-087 — Proposed; the held mechanism A2 §8 cites -->

# CLAIM-1357: Aligning each component does not align what they compose

## The claim

A6 §7 supposes an assistant "extremely good at following the legitimate
instructions of its deploying organization", directed toward advertising
revenue:

| Level | Alignment relationship |
|---|---|
| Model | Aligned with its training signal |
| AI assistant | Aligned with its deploying organization |
| Organization | Aligned with its financial incentives |
| Society | Not necessarily served by the resulting behaviour |

"Local alignment does not compose into global alignment. Indeed,
improving alignment at a lower organizational level could worsen
alignment at a higher one. A perfectly obedient AI could be an extremely
effective component of an objectionable organizational arrangement."

A2 §8 had the structural form: "Each component could follow its local
rules. Each delegation could be locally justified. Yet the resulting
organization could accumulate authority, entrench its interpretations and
marginalize human intervention", citing [SYNTHESIS-087](../syntheses.d/SYNTHESIS-087.md).

## Why the second half follows

Alignment here is a relation to a principal, and each level has its own.
If the organization's direction departs from the interests of those it
affects, a component's fidelity is the rate at which that direction is
carried out, so raising it raises the departure's effect. The step needs
only that the departure is not itself corrected by the components, which
is what "obedient" stipulates.

## What it does not say

- **That AI-specific alignment problems dissolve.** A6: "The institutional
  framing does not eliminate those concerns. But it puts them inside a
  larger problem that existed long before AI."
- **That obedience is the fault.** A6's conclusion is that "some AI
  alignment research is addressing the reliability of optimization without
  sufficiently addressing the legitimacy of the optimization to which that
  reliability is being supplied". Legitimacy is a separate question, held
  open in [QUESTION-485](../questions.d/QUESTION-485.md).
- **The relation to [CLAIM-060](CLAIM-060.md).** [CLAIM-060](CLAIM-060.md) is about success and
  well-being across scales; this is about alignment relations, each
  relative to its own principal. It is a case of [CLAIM-060](CLAIM-060.md)'s converse
  only if "aligned" is read as the component's good, which it is not.
