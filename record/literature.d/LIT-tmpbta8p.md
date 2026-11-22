---
status: Active
status_note: >-
  read in full 2026-11-22 ([NOTE-tmpk22nd](../notes.d/NOTE-tmpk22nd.md)), from the arXiv
  copy. Worth reading as a standard, recent review of dual control in the
  Bar-Shalom–Feldbaum exploration–exploitation sense: a controller of a
  system whose dynamics are unknown must probe it to learn while regulating
  it, and the review organizes the field into four directions (multi-armed
  bandits, self-tuning regulators, regret-rate minimization for
  linear-quadratic control, and minimax optimal dual control). Registered
  and read for LEAD-145, to check the dual-control citation that
  [CLAIM-572](../claims.d/CLAIM-572.md) leaves unchecked and excludes from its scope.
title: 'Dual Control: On Exploration-Exploitation in Linear Systems'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Registered and read in one pass for LEAD-145, from arXiv 2608.20073v1
    (submitted 20 August 2026, the only version), fetched 2026-11-22; text
    extracted with `pdftotext -layout`. To appear in Annual Review of
    Control, Robotics, and Autonomous Systems 2027, 10:1–26. Citation
    checked against the arXiv API. `published:` is the arXiv v1 date, the
    earliest exact date given (ADR-002). Authors Tomas J. Meijer and Anders
    Rantzer (Lund University). Not checked against the Anthology of the
    SOTA. The summary is written from the text.
tags:
- control-theory
- mathematics
- learning-theory
date: '2026-11-22'
published: '2026-08-20'
arxiv: '2608.20073'
first_author: 'Meijer'
keywords:
- 'dual control'
- 'exploration-exploitation'
- 'adaptive control'
- 'multi-armed bandits'
- 'self-tuning regulators'
- 'regret'
- 'minimax control'
- 'information state'
implementations: []
summary: >-
  Meijer and Rantzer (2026), a review. "Dual control" (Feldbaum, 1960)
  names the double task of a feedback controller for a system whose
  parameters are unknown: it must regulate the plant and simultaneously
  probe it to learn, because without probing it does not learn how the
  system responds, yet probing can spoil short-term performance. The
  review surveys four research directions for linear systems — multi-armed
  bandits (Gittins index, optimism in the face of uncertainty, regret),
  self-tuning regulators, regret-rate minimization for linear-quadratic
  control, and minimax optimal dual control as a zero-sum dynamic game —
  and frames them around an extended state that adjoins an information
  state to the physical state. A recurring lesson: when the optimal
  policy itself makes the parameters that matter non-identifiable in
  closed loop, exploration must drive the system away from optimality,
  which separates problems with log T regret from those needing √T.
---


# LIT-tmpbta8p: Dual Control: On Exploration-Exploitation in Linear Systems

Meijer, T. J. & Rantzer, A. (2026). Dual control: On exploration–exploitation in linear systems. arXiv:2608.20073. To appear, Annual Review of Control, Robotics, and Autonomous Systems 2027, 10:1–26.

## Key takeaways

- Dual control (Feldbaum, 1960) is the task of a controller that must learn
  an unknown plant by active probing while regulating it; aggressive
  probing improves estimates but can degrade performance, cautious control
  does the reverse.
- Feldbaum cast the problem in Bellman's dynamic programming by combining
  the physical state with an *information state*; Åström (1965) gave the
  POMDP as a rigorous framework.
- Four directions are reviewed: multi-armed bandits, self-tuning
  regulators, regret-rate minimization for linear-quadratic control, and
  minimax optimal dual control.
- Exploration is forced away from the optimal policy exactly when being
  optimal makes essential parameters non-identifiable in closed loop; this
  is why some problems achieve log T regret while others need √T.

## Standing in the record

Registered and read under LEAD-145 as a standard treatment of dual control,
the case [CLAIM-572](../claims.d/CLAIM-572.md) names and excludes ("in dual control (Feldbaum) an
action also observes; that case is excluded"). The reading
([NOTE-tmpk22nd](../notes.d/NOTE-tmpk22nd.md)) confirms the Feldbaum attribution.
