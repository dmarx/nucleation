---
status: Open
title: 'Does an independent derivation or computation, on a network other than Rocks and Mehta''s two examples, confirm their generalized index theorem with prestress and heterogeneous stiffness, the identity of zero-displacement tensions with states of self-stress, the joint-symmetry rule for the forces that excite linear zero modes, and the redirection and localization of those forces by symmetry-breaking prestress?'
version: 1
tags:
- natural-sciences
- mathematics
date: '2026-11-06'
line:
- realizability
summary: >-
  The promotion condition formerly on THEORY-1414, moved here when the
  twenty-eighth status review narrowed that reading to the paper's two
  worked networks and promoted it under ADR-065. Rocks and Mehta prove the
  theorems and show the localization on a diamond network and a 4×4
  periodic square lattice, both with uniform stiffness. A first computation
  on two other networks, second-checked, confirms the theorem, Theorem 1
  and the localization; the symmetry rule is untested elsewhere.
---
<!-- inactive-ok-file: CLAIM-tmp5iqbr — Proposed and new; the status review's identity behind the computation, cited as checked, nothing here rests on its being ruled -->

# QUESTION-tmphi77o: Does an independent derivation or computation, on a network other than Rocks and Mehta's two examples, confirm their generalized index theorem with prestress and heterogeneous stiffness, the identity of zero-displacement tensions with states of self-stress, the joint-symmetry rule for the forces that excite linear zero modes, and the redirection and localization of those forces by symmetry-breaking prestress?

## Why it is a question

THEORY-1414 reports what Rocks and Mehta proved and showed (NOTE-1557). The proofs are linear algebra, and the reading checked them step by step. The localization of the forces that excite a zero mode is shown on two small symmetric networks with uniform stiffness. Before this pass, no second derivation or computation was in the record.

## What would answer it

The condition as it stood on THEORY-1414: An independent derivation or computation, on a network other than the paper's two examples, confirms that the generalized index theorem holds with prestress and heterogeneous stiffness; that the zero-displacement tensions coincide with the states of self-stress; that the forces exciting each linear zero mode follow the symmetry of geometry and energy together; and that prestress breaking a geometric symmetry redirects and localizes those forces while leaving the linear zero modes unchanged.

## Note of 2026-11-06: a first computation, second-checked

The twenty-eighth status review's reader ran scratch/formal/rocks_mehta_check.py (python3 -I) on two networks that are not the paper's. One is a perturbed free strip with braced end cells. The other is a pinned grid with a straight prestressed row. Both have heterogeneous stiffness, and each was run at two values of the regularizer, with controls. In all twelve runs the generalized index theorem, Theorem 1 (zero-displacement tensions equal states of self-stress; the forces map one-to-one onto the zero modes) and Corollary 1 held. On the grid, prestress redirected the force that excites the zero mode, to |cos| = 0.53 against the mode. As the regularizer went to zero, that force came to lie entirely on the nodes of the prestressed row. The coordinator re-ran the script and checked by hand the identity behind it, the force (T + λI)u for a zero mode u (CLAIM-tmp5iqbr). That is the second check. The joint-symmetry rule (Theorem 2) was not tested on another network, so the question stays open on that clause. Every other clause has its first independent computation.
