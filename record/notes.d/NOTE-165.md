---
number: 165
status: Skimmed
formerly:
- NOTE-tmps1tct
paper: LIT-149
title: 'Martínez — information-processing view of representation'
version: 1
date: '2026-09-26'
summary: >-
  A state counts as a representation when it shows adaptations for transmitting information for its own sake, i.e. for efficiently trading off rate, distortion and coder complexity — and that trade-off is what grounds the properties cognitive scientists attribute to representations.
---

<!-- inactive-ok-file: LIT-149 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-165: Martínez — information-processing view of representation

## Contribution

Martínez proposes a framework for theorizing about representation in cognitive science built on two theses. The Transmission thesis says representations are primarily signals whose function is transmitting information for its own sake, not as a by-product of some other role. The RDC Trade-Off thesis says those signals aim at an efficient balance among three budgets: rate (transmission and storage cost), distortion (fidelity), and the computational complexity of the coders. Evidence that something is a representation is therefore evidence of adaptations for efficient transmission, and the familiar marks of paradigmatic representations are argued to be products of such rate–distortion–complexity adaptations.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1: the Transmission thesis is explicitly stronger than the Dretskean claim that representations correlate with what they are about — it requires adaptations (compression, error protection, complexity management) for transmission per se; the model is Shannon's source→coder→channel→decoder→destination picture (Figs. 1–2), which includes processing and transformation, not just copying.
- Section plan: §2 information and adaptive behaviour; §3 informational constraints on transmission; §4 rate–distortion trade-offs (§4.1 source coding, §4.2 channel coding); §5 complexity–distortion trade-offs; §6 the "representational surface".
- §6: the Pareto frontier of rate, distortion and complexity is a 2-D "representational surface" (Fig. 5); debates between classical and 4E/ecological cognitive science are recast as disagreements about the shape of this surface — specifically about the computational complexity of extracting information from the environment, since no system can "enrich" the source (§5).
- §7: maps the adaptations onto representational properties — noise protection onto representational vehicles, compression onto Rosch's "cognitive economy", complexity management onto neuroscience's notion of explicit representation; points to MDL and the Free Energy Principle as formal tools, noting MDL is lossless whereas most cognitive transmission is lossy.

## Open questions

- Offers an information-theoretic criterion for representation-hood that transfers naturally to learned representations in ML (bottlenecks, rate–distortion framings of representation learning); check whether Martínez discusses learned networks directly (Bengio et al. 2013 is cited).
- The "representational surface" is a testable framing: check §4–5 for what empirical signatures would count as adaptations for rate or complexity efficiency.
- A deeper reading should check how the Transmission thesis avoids counting every efficiently-coded signal (e.g. in engineered systems) as a representation, and how it handles misrepresentation.
