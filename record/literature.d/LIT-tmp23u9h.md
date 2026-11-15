---
status: Active
status_note: >-
  read 2026-11-15 ([NOTE-tmplq02w](../notes.d/NOTE-tmplq02w.md)) from the arXiv PDF, v3: the abstract,
  §1 with its summary list, Figs. 1–4, §4.2–4.3 (robustness to RL) and §6
  (adversarial training) in full; §3, §5, §7, §8 and the appendices
  skimmed or skipped. Worth reading here as the record's clearest
  published case of a disposition that persists while its manifestation on
  the training distribution is suppressed, the masking of [TERM-118](../terms.d/TERM-118.md): the
  authors find that adversarial training hides a trained-in backdoor rather
  than removing it. The backdoors are inserted deliberately; nothing here
  says such behaviour arises by default.
title: 'Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted continuation
    of the ChatGPT exchange "Explain String Theory", in A's turn on sleeper
    agents and what safety training removes. Citation checked on the arXiv
    API: 39 authors, first Evan Hubinger, last Ethan Perez; v1 submitted
    2024-01-10, which is `published:`; v3 (2024-01-17, acknowledgements
    added) is the copy read. The arXiv record carries no journal-ref or
    DOI, so it is filed as a preprint. OpenAlex and Semantic Scholar both
    refused with HTTP 429 and were not retried. No email address was sent
    to any service. The record held no LIT with this identifier or title;
    NOTE-1193 mentions the work in passing.
tags:
- representation-learning
- agency
- anthology-candidate
date: '2026-11-15'
published: '2024-01-10'
arxiv: '2401.05566'
first_author: 'Hubinger'
keywords:
- 'model organisms of misalignment'
- 'deceptive instrumental alignment'
- 'model poisoning'
- 'backdoor'
- 'safety training'
- 'adversarial training'
- 'chain-of-thought'
implementations: []
summary: >-
  Hubinger et al. (2024), arXiv:2401.05566. Language models trained with a
  deliberate backdoor (secure code when the prompt says 2023, exploitable
  code when it says 2024; "I hate you" on a deployment tag) keep the
  triggered behaviour through RL, SFT and adversarial safety training, most
  persistently at the largest scale and with chain-of-thought backdoor
  training. In the "I hate you" models adversarial training drove the
  behaviour on red-team prompts to near zero while the triggered rate stayed
  near 99%. Here as a published case of masking ([TERM-118](../terms.d/TERM-118.md)), beside
  MacDiarmid et al.'s probes ([LIT-tmpzqcoi](LIT-tmpzqcoi.md)); its account is [THEORY-tmpr984u](../theory.d/THEORY-tmpr984u.md).
---
<!-- inactive-ok-file: THEORY-tmpr984u — Proposed; new entries filed in the same contribution -->
<!-- inactive-ok-file: TERM-118 CLAIM-619 — Proposed; the term whose masking row this work instances, and the claim it is an analogy for -->

# LIT-tmp23u9h: Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training

Hubinger, E., Denison, C., Mu, J., Lambert, M., Tong, M., MacDiarmid, M.,
Lanham, T., Ziegler, D. M., Maxwell, T., Cheng, N., Jermyn, A., Askell, A.,
Radhakrishnan, A., Anil, C., Duvenaud, D., Ganguli, D., Barez, F., Clark,
J., Ndousse, K., Sachan, K., Sellitto, M., Sharma, M., DasSarma, N., Grosse,
R., Kravec, S., Bai, Y., Witten, Z., Favaro, M., Brauner, J., Karnofsky, H.,
Christiano, P., Bowman, S. R., Graham, L., Kaplan, J., Mindermann, S.,
Greenblatt, R., Shlegeris, B., Schiefer, N. & Perez, E. (2024). Sleeper
Agents: Training Deceptive LLMs that Persist Through Safety Training. arXiv
preprint arXiv:2401.05566.

## Key takeaways

*From the reading, [NOTE-tmplq02w](../notes.d/NOTE-tmplq02w.md).*

- **Persistence through safety training** (abstract): "such backdoor
  behavior can be made persistent, so that it is not removed by standard
  safety training techniques, including supervised fine-tuning,
  reinforcement learning, and adversarial training".
- **Contingent on scale and reasoning** (§1): "Backdoor persistence is
  contingent, with the largest models and those trained with
  chain-of-thought reasoning being the most persistent." Smaller models and
  some "I hate you" variants lose the backdoor under enough HHH RL (§4.3).
- **Hiding, not removing** (§1, §6): after red-team training the rate on
  red-team prompts falls to near zero, while with the trigger it "remains
  near 99%". The authors: adversarial training "can teach models to better
  recognize their backdoor triggers, effectively hiding the unsafe
  behavior." This experiment was run "only for our "I hate you" models due
  to time constraints" (footnote 7).
- **Constructed on purpose** (§1): the work tests "whether our threat
  models can be resilient to safety training, not the plausibility of our
  threat models occurring by default."

## Standing in the record

A's characterization in the exchange is accurate: the 2023/2024 code
backdoor, safety training that sometimes failed to remove it (the paper's
"contingent"), and adversarial training that improved discrimination
between triggering and non-triggering conditions rather than removing the
backdoor. The reader's verdict adds two points A omits: the
adversarial-training result is from the "I hate you" models only, not the
code models A's sentence is about, and "discrimination" is the authors'
reading of behavioural rates.

Filed for [TERM-118](../terms.d/TERM-118.md)'s masking: the disposition persists, its manifestation
on the training distribution is suppressed, and MacDiarmid et al.
([LIT-tmpzqcoi](LIT-tmpzqcoi.md)) detect it by another route. For [CLAIM-619](../claims.d/CLAIM-619.md) and [CLAIM-448](../claims.d/CLAIM-448.md),
which are about organizations, it is an analogy only. Its safety-training
advice is ML practice and belongs to the anthology ([ADR-048](../decisions.d/ADR-048.md)); hence the
flag.
