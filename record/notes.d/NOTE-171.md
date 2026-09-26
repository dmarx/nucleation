---
number: 171
status: Skimmed
formerly:
- NOTE-tmptz3my
paper: LIT-179
title: 'Algorithmic nudging needs interdisciplinary oversight'
version: 1
date: '2026-09-26'
summary: >-
  Because AI systems can learn nudges that exploit biases nobody has documented, judging algorithmic nudges by predictive success alone repeats Friedman's instrumentalism, and Hausman's "look under the hood" rejoinder supports mandatory oversight by experts in human cognition.
---

<!-- inactive-ok-file: LIT-179 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-171: Algorithmic nudging needs interdisciplinary oversight

## Contribution

Nudges steer choices by exploiting known biases in human judgement, and AI makes personalised, adaptively discovered nudges possible. The authors warn that handing nudge design to black-box systems means the cognitive processes being exploited may be unknown. They illustrate this with examples of biases and with case studies of AI agents learning to sway human choices. Drawing on a debate in the methodology of economics, they argue for interdisciplinary oversight of AI systems deployed to nudge behaviour.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1 (pp. 799–800) sets out the plan: biases (§2), nudges (§3), AI case studies (§4), a methodological analogy (§5).
- §2 (p. 800) treats biases as systematic, predictable "cognitive illusions" (Kahneman 2011; Pohl 2016).
- §4 (pp. 802–803): in Dezfouli et al.'s (2020) bandit task an RL agent learned to schedule rewards so that participants chose a target lottery 70% of the time against a 50% baseline, adapting its strategy to each participant.
- §5 (pp. 804–805) contrasts Friedman's (1953) instrumentalism — a theory is good if it predicts — with Hausman's (1994) used-car analogy: you also inspect the inner workings, which is what lets you repair a theory when it fails in new circumstances.
- Conclusion (pp. 805–806): an AI-discovered nudge may rest on an undocumented bias for which no theory exists; the authors propose obliging developers to consult experts on judgement and decision-making, for accountability and trust, citing the EU trustworthy-AI guidelines.

## Open questions

- The Friedman–Hausman frame is a clean philosophy-of-science argument for interpretability over purely behavioural evaluation of deployed models; check whether it generalises beyond nudging.
- Check the other case study in §4 and whether the 70% effect is reported with its conditions.
- Links to the record's persuasion and manipulation material and to interpretability-as-oversight arguments.
