---
status: Skimmed
paper: 'LIT-tmpaw2id'
title: 'Simkute, Tankelevitch et al. — Ironies of generative AI'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read in part on 2026-11-05 from the authors' arXiv deposit,
    arxiv.org/pdf/2402.11364v1 (23 pages), extracted with pdftotext; no wall
    or challenge was met. Read in full: the abstract, §1 (introduction), §2
    (the four productivity challenges, §§2.1–2.4) and §3.5 (clear task
    allocation). Skimmed: the opening of §3, §§3.1–3.4 and §4
    (conclusions). Not read: Figure 1 beyond its labels, and the reference
    list beyond entry [7], Bainbridge. Places below are the paper's
    sections.
date: '2026-11-05'
summary: >-
  A synthesis mapping four Human Factors findings on automation onto user
  studies of generative AI, chiefly programming with Copilot: the user's
  role shifts from producing output to evaluating it; workflows are
  restructured unhelpfully; suggestions interrupt; and easy tasks get easier
  while hard ones get harder (task-complexity polarization), because the easy
  share is what gets automated and the user keeps the hard share plus the
  monitoring. Design remedies follow. Nothing on skill or retention.
---
<!-- inactive-ok-file: CLAIM-558 CLAIM-600 CLAIM-602 THEORY-tmp6uywt — Proposed or new; cited from the reading of Simkute, Tankelevitch et al. (2024) as open -->
<!-- inactive-ok-file: LIT-tmph5vta — Unavailable; the unread original this reading stands in for -->

# NOTE-tmpndiw7: Simkute, Tankelevitch et al. — Ironies of generative AI

## Contribution

Usability studies of generative AI report users losing productivity as well
as gaining it. The paper argues that these losses are not new: they are the
ironies of automation that Human Factors research found in aviation, process
control and other safety-critical work, and the same literature offers
remedies. It names four challenges and five design directions.

## Key insight

Automation does not remove work in proportion to what it takes over; it
changes the work. It takes the easy share, leaves the hard share, and adds
the task of checking it: "easy tasks are easier to automate, and so the more
difficult tasks tend to remain under manual control, albeit alongside the
additional task of monitoring automation" (§2.4, citing Lee and Seppelt).

## Assumptions

- Findings from automation in aviation and process control transfer to
  generative AI, which the paper supports by parallel user studies, not by
  a test of the transfer.
- Productivity is the outcome of interest; skill, learning and retention are
  outside its scope.

## Key results

- **§1, the irony, cited to Bainbridge [7]:** the ironies "capture the idea
  that the more advanced an automated system is, the more important the
  human operator may be."
- **§1, restructuring, cited to [7]:** "poor system and interface design can
  result in unhelpful restructuring of workflows".
- **§2.2, strategies, cited to [7]:** "rather than reducing what they work on
  when all or part of tasks are automated, people instead rely on different
  strategies for working on that task".
- **§2.1, production to evaluation:** monitoring can, therefore,
  "paradoxically impose a considerable workload on humans" (cited to [48,
  121], not to Bainbridge); in AI-assisted coding, users "spend extended
  periods reviewing and validating code suggestions".
- **§2.1.5, complacency under load:** "In high-workload situations, there are
  fewer attentional resources available for monitoring imperfect
  automation".
- **§2.4, polarization:** automation "often makes easy tasks easier but fails
  to reduce the workload during cognitively demanding tasks, and in fact,
  often makes them harder" (cited to [66]); for generative AI, "whereas GenAI
  succeeds at making easy tasks even easier, current systems are less
  effective at supporting harder tasks."
- **§3.5, the remedy:** "clearly specifying how tasks are allocated between
  the human and system, particularly during high workload periods"; users
  who let the system run on simple tasks "often stepped in and overrode the
  system" on complex ones.

## Concepts

- **Production-to-evaluation shift.**
- **Unhelpful workflow restructuring**: new tasks such as prompting and
  output adaptation, loss of task sequence, loss of feedback.
- **Task interruptions.**
- **Task-complexity polarization**, the paper's term for what Human Factors
  calls "clumsy automation".
- **Clear task allocation.**

## Connections

- **Bainbridge (1983)**, LIT-tmph5vta, unread. Cited three times as [7]: for
  the general irony, for unhelpful restructuring and for changed strategies.
  It does not restate her ironies on skill, the hand-back at failure or her
  remedies, and its polarization finding is credited to others (Lee and
  Seppelt 2009; Cook, Woods et al. 1991; Wiener and Curry 1980, per the
  reader). It stands in for her only on the monitoring burden and the
  residue of hard work left to the operator.
- **Ahn (2025)** restates the same residue as Bainbridge's central irony.
- **Macnamara et al. (2024)** carry the skill decay this paper leaves out.

## Bearing on the record

- **CLAIM-600** (Proposed): weak qualification of its third condition.
  Support that takes the easy share leaves the party the hard residue and an
  added monitoring task, so "the party could do the work and did it throughout" can hold for
  the hard part while the easy part is no longer done.
- No bearing on CLAIM-558, CLAIM-602 or QUESTION-398: there is nothing here on
  capacity over time.
- Filed from this reading: THEORY-tmp6uywt.

## Limitations

- A synthesis and position paper; the Human Factors evidence is cited, not
  shown, and the generative-AI evidence is a set of user studies, mostly in
  programming.
- An unrefereed preprint version; no venue of record is established.
- Read in part.
