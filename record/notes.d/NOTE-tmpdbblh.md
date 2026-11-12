---
status: Read
paper: LIT-2300
title: 'Boult et al. — Learning and the Unknown: Surveying Steps toward Open World Recognition'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from
    https://ojs.aaai.org/index.php/AAAI/article/download/5054/4927. Read:
    full text, 7 pp., §1–§6; references spot-checked. A delegated reader
    drafted the reading; quotations were rechecked by script against the
    downloaded copy, and any that did not match were kept as paraphrase
    without quotation marks.
date: '2026-11-12'
summary: >-
  The paper reviews the authors' formalization of open set recognition (OSR)
  and open world recognition. It argues that classic tools for unknown
  inputs (reject options, background or garbage classes, uncertainty
  thresholds, Bayesian posteriors) do not solve the problem. A classifier
  that labels unbounded "open space" far from its training data has
  unbounded open space risk.
---
<!-- inactive-ok-file: CASE-tmppm4do — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmpdbblh: Boult et al. — Learning and the Unknown: Surveying Steps toward Open World Recognition

## Contribution

A compact statement of the OSR problem (Definition 1: open space risk balanced against empirical risk), a taxonomy of why rejection, novelty detection and background classes fall short, and the four tasks of open world recognition.

## Key results

- The thesis (Abstract): "uncertain is not unknown, and unknowns need not appear to be uncertain to a learning system."
- The Bayesian closed world (§1): "using Bayes theorem requires implicitly making a closed world assumption."
- Confident errors (§5): "an unknown far from the boundary is not only incorrectly labeled but will be incorrectly classified with very high confidence."
- Rejection was built for something else. Chow's reject option, quoted in §5: "The option to reject is introduced to safeguard against excessive misrecognition; it converts potential misrecognition into rejection."
- Relation to novelty detection (§5): "OSR ≈ Novelty-detection + multi-class recognition." Novelty detectors bound open space risk but do not balance it with multi-class risk.
- Open world recognition's four tasks (§3): a system "must efficiently perform four tasks: detect unknowns, choose which points to label for addition to the model, label the points, and update the model."
- Deep networks (§5): after a feature-space attack defeated OpenMax, "As of this writing, we are unaware of any defense against this attack."
- Closed-world history (§1), quoting Hewitt and Jong 1983: "the default answers provided become less realistic as the Open System increases in size."

## Assumptions

Unknowns lie in "open space" far from training support in some feature space. For deep networks that space is not well-behaved (§5). Risk is measured as a ratio of positively labelled open-space volume.

## Concepts

Open set recognition; open world recognition; open space risk; closed world assumption; CAP model; extreme value theory (EVT); known unknowns vs unknown unknowns; background class; reject option.

## Bearing on the record

The exchange says the paper "distinguishes handling unfamiliar inputs from genuinely recognizing unknowns, and explains why uncertainty alone is not an adequate substitute for novelty recognition". **Accurate in substance.** The paper's own phrase is "uncertain is not unknown". It goes further than the exchange: novelty detection alone is also not sufficient (§6), since unknowns must be handled while keeping multi-class accuracy.

The LIT names none, and no branch entry cites LIT-2300. The exchange used it (A50/A51 region, §11 "open-world learning") as prior art for Nucleation's distinction between what a record can and cannot express.
- **CASE-186** (a world whose hidden regime "leaves its hypothesis family"): **supports the design premise**. An agent whose hypothesis family is closed treats a regime outside it the way a closed-set classifier treats an unknown: it assigns it to a known class, possibly confidently. Boult et al. give the formal reason uncertainty need not rise ("unknowns need not appear to be uncertain").
- **CASE-tmppm4do**, on the failure kind "schema inadequacy: the grammar cannot express the distinction" versus "missing evidence": **qualifies**. Boult's distinction between rejection under ambiguity (Chow) and recognition of an unknown corresponds to the case's split between "record the uncertainty" and "amend the grammar". The paper warns that a detector built for the first does not serve the second.
- Held closed-world-assumption entries (NOTE-899, THEORY-341, THEORY-374 on certain answers under CWA and OWA): the same term in a database sense. Boult's use is the learning-theory analogue, and the link is a cross-reference only.

## Limitations

It is a survey of the authors' own line of work. The theorems are cited (Scheirer et al. 2013, 2014; Bendale and Boult 2015; Rudd et al. 2018), not proved here, and the reader did not check them.
