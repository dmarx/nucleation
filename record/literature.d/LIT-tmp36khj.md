---
status: Active
status_note: >-
  read 2026-11-05 ([NOTE-tmpoedni](../notes.d/NOTE-tmpoedni.md)) from the published version's full text
  in Europe PMC (CC BY 4.0) and the arXiv preprint, Supporting
  Information skipped; worth reading as a reservoir computer whose
  reservoir is a multistable origami metamaterial, and for the plain
  finding that a bad actuation rule erases its inputs. Its main limits: the
  learning is in a trained linear readout, not in the material; only the
  small-digit task (ten 5×4-pixel digits on a 4×2-cell prototype) was done
  in experiment, MNIST and the memory task in simulation; the gain over the
  raw inputs on MNIST is modest (87.2% to 90.4%); the publisher's
  table-of-contents text overstates what was done in experiment.
title: 'Cellular Automata Inspired Multistable Origami Metamaterials for Mechanical Learning'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read on 2026-11-05 from the owner's pasted synthesis on
    FACT, rigidity, compliant mechanisms and origami (pasted 2026-11-04,
    written by another assistant), where it is cited as O10. The citation
    was checked by the reader against Crossref: Zuolin Liu, Hongbin Fang,
    Jian Xu and Kon-Well Wang, Advanced Science 10(34), 2305146; online 23
    October 2023; arXiv 2305.19856, v1 31 May 2023, which is `published:`;
    PMC10700163. The synthesis's attribution is correct. Read from the
    published version's JATS full text in Europe PMC
    (https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10700163/fullTextXML),
    CC BY 4.0, and the arXiv preprint (https://arxiv.org/pdf/2305.19856);
    the numerical results agree between the two. Status Active.
tags:
- natural-sciences
- complex-systems
date: '2026-11-05'
published: '2023-05-31'
arxiv: '2305.19856'
doi: '10.1002/advs.202305146'
first_author: 'Liu'
keywords:
- 'origami metamaterials'
- 'multistability'
- 'reservoir computing'
- 'cellular automata'
- 'mechanical learning'
- 'physical computing'
implementations: []
summary: >-
  Liu, Fang, Xu & Wang (2023). A stacked Miura-origami metamaterial whose
  bistable cells evolve under a prescribed sequence of tension and
  compression is used as the reservoir of a reservoir computer: inputs are
  written as an initial configuration, the actuation drives snap-through
  transitions, and a trained linear readout classifies from the visited
  configurations. A 4×2-cell prototype recognizes ten 5×4-pixel digits and
  noisy versions in experiment; in simulation, binarized MNIST reaches 90.4%
  against 87.2% without the reservoir, and a retained buffer of cells
  carries history on a 5-bit memory task.
---
<!-- inactive-ok-file: THEORY-tmpx5uxp — Proposed; cited from the reading of Liu et al. (2023) as open -->

# LIT-tmp36khj: Cellular Automata Inspired Multistable Origami Metamaterials for Mechanical Learning

Liu, Z., Fang, H., Xu, J. & Wang, K.-W. (2023). Cellular Automata Inspired Multistable Origami Metamaterials for Mechanical Learning. *Advanced Science* 10(34): 2305146. doi:10.1002/advs.202305146. arXiv:2305.19856.

## Key takeaways

*From the reading, [NOTE-tmpoedni](../notes.d/NOTE-tmpoedni.md). Quotes are from the published text.*

- **A trained readout, a fixed reservoir.** "To minimize the output error,
  the readout weights are trained with logistic regression." The
  metamaterial is not trained.
- **Experiment on small digits only.** "For more complex tasks, such as
  handwriting recognition and 5-bit memory tasks, the effectiveness is
  tested via simulations."
- **A modest gain.** MNIST "can reach 90.4%" with the reservoir, 87.2%
  without.
- **Memory in a buffer.** "the final configuration from the previous
  timestep carries the historic input information"; with 200 cells the
  memory-task error nears zero (simulated).
- **A bad rule erases.** Under all-compression the structure "will always
  be transformed into a fully compressed stable configuration no matter
  what pattern is given".

## Standing in the record

Cited in the pasted synthesis on constraint architectures as O10:
reservoir computing, digit recognition and short-term memory. The reading
qualifies it: the learning is in a linear readout, and only the
small-digit task was done in experiment; the memory benchmark is a
simulated 5-bit memory task. Filed from it: [THEORY-tmpx5uxp](../theory.d/THEORY-tmpx5uxp.md). The machine
learning here is a standard readout, so not, on balance, an instruction
for machine-learning practice; nothing for the anthology.
