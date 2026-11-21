---
status: Proposed
title: "Sloppy-model behaviour, behavioural complexity set by a few combinations of many parameters, probably does carry over to overparameterized neural networks, by a route other than the analogy from regular Fisher spectra"
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  An overparameterized network trained to a good fit whose behaviour on a
  stated task depends on many parameter combinations about equally, by any
  of the measures below (the learning coefficient, the count of resolved
  directions at the training sample size, the dimension of the prediction
  set the network can reach near its fit), with no few combinations
  carrying most of it; or a showing that the only route from the sloppy-
  model account to networks is the regular-spectrum analogy that
  ARG-tmpmvc5e rejects.
tags:
- learning-theory
- information-geometry
- representation-learning
date: '2026-11-21'
line:
- learned-structure
summary: >-
  The owner's, 2026-11-21, on [ARG-tmpmvc5e](../arguments.d/ARG-tmpmvc5e.md), whose conclusion this is:
  "We don't know that that conclusion doesn't hold … (which I think is
  actually probably correct)". The other assistant put it forward at A19
  §10 of the exchange "Rich Get Richer Power Laws" by analogy from sloppy
  models, whose account assumes a regular Fisher matrix; the record
  rejects that route ([ARG-tmpmvc5e](../arguments.d/ARG-tmpmvc5e.md), and the originators' small-network
  applications, [ARG-tmpv3nqz](../arguments.d/ARG-tmpv3nqz.md)), because an overparameterized network is
  singular ([CLAIM-tmpcgvcp](CLAIM-tmpcgvcp.md)). The conclusion is held here on its own, as
  the owner's, so that the route's rejection is not read as the
  conclusion's ([ADR-tmp44npm](../decisions.d/ADR-tmp44npm.md)). Candidate routes are listed in the body.
  The idea is the owner's; the candidate routes are the assistant's
  (Claude, in this session); adopting either is the owner's call.
---
<!-- inactive-ok-file: ARG-tmpmvc5e ARG-tmpv3nqz CLAIM-tmpcgvcp CLAIM-tmpcg4uu CLAIM-tmpj0k4q ADR-tmp44npm TERM-tmptiim0 TERM-tmp5z2du — Proposed, Rejected or new; filed 2026-11-21 -->

# CLAIM-tmp7ijze: Sloppy-model behaviour, behavioural complexity set by a few combinations of many parameters, probably does carry over to overparameterized neural networks, by a route other than the analogy from regular Fisher spectra

**The owner's claim.** That an overparameterized network's behaviour, like a sloppy model's, is set by a few combinations of its many parameters, while most combinations barely matter, even though the route the other assistant offered, the analogy from regular sloppy spectra ([ARG-tmpmvc5e](../arguments.d/ARG-tmpmvc5e.md)), does not show it. The owner, 2026-11-21: "We don't know that that conclusion doesn't hold … (which I think is actually probably correct)."

**What the record holds against the route, not the conclusion.** Sloppiness counts behavioural complexity by the spread of a full-rank Fisher spectrum ([TERM-tmptiim0](../terms.d/TERM-tmptiim0.md)). An overparameterized network is singular: its Fisher matrix is degenerate on whole sets of parameters, where the effective count is the learning coefficient, and the spectrum does not give it ([CLAIM-tmpcgvcp](CLAIM-tmpcgvcp.md)). That defeats the analogy. It does not say the behaviour differs.

**Candidate routes**, the assistant's. None is yet an argument the record holds:

- **The learning coefficient as the effective count.** In a singular model the count of effective parameters is the learning coefficient λ, at most d/2 and often far below it ([THEORY-087](../theory.d/THEORY-087.md)). If λ for trained networks is small against d, a few effective combinations set the fit, by singularity, not by a spread spectrum.
- **Sloppy edges near strata.** Near a stratum a sloppy eigenvalue goes to zero with the squared distance, and at finite n an unresolved sloppy direction counts like a flat one ([CLAIM-tmpcg4uu](CLAIM-tmpcg4uu.md)). There the two accounts meet, so the sloppy picture holds locally.
- **Resolution with data.** The number of directions the data resolve grows slowly with the sample size ([CLAIM-tmpj0k4q](CLAIM-tmpj0k4q.md)). At any training size only a few would be resolved.
- **Prediction-space shape.** The hyper-ribbon is a property of the set of predictions, not of the chart ([TERM-tmp5z2du](../terms.d/TERM-tmp5z2du.md)). A network's prediction set near its fit could be ribbon-like whatever its parameter-space singularities, which is the sense in which the originators applied it to an autoencoder's code.

The claim would be defeated by its `defeated_if`. Its warrant is interpretive until one of these routes is argued.
