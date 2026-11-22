---
status: Proposed
title: "The most informative signal in a learned spectrum lies in a truncated band: the top directions carry common, weakly discriminating structure, as stop words do in a corpus, the extreme bottom carries low-signal outliers, as rare words do, and once both are cut, the bottom of the retained band holds the most discriminating directions"
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A trained model whose top spectral directions are as discriminating per
  unit as its lower retained band, or whose extreme bottom, once
  separated, is as discriminating as the band above it, so that cutting
  either end removes as much signal as noise; or a showing, for the
  unembedding, that its top singular directions do not track common,
  weakly discriminating structure such as token frequency.
tags:
- representation-learning
- information-theory
- linguistics
date: '2026-11-22'
line:
- learned-structure
grounds:
- THEORY-tmpu3iio
summary: >-
  The owner's, 2026-11-22, on the U-shaped picture in Xu's reading
  ([THEORY-tmpu3iio](../theory.d/THEORY-tmpu3iio.md)): 'this connects to classic NLP pre-processing for topic modeling, e.g. where both the most common (stop words) and least common (low signal outliers) are often eliminated to distill signal in a text corpus. i.e. the most informative signal is in the truncated spectrum, and the bottom of that spectrum is often characterized by highly discriminating directions.' The analogy is to the
  preprocessing that drops the most frequent words, which discriminate
  little, and the rarest, which carry little signal, so that what is
  left distils the corpus's signal. Spectrally, the top directions carry
  common structure, the extreme bottom carries low-signal outliers, and
  the bottom of the retained band holds the most discriminating
  directions. Xu's Qwen comparison supports the truncation half
  ([ARG-tmpabk16](../arguments.d/ARG-tmpabk16.md)): excluding the near-zero directions roughly doubles the
  bottom band's discriminating effect. The stop-word half, that the top
  directions track token frequency, is untested ([LEAD-tmptgrc7](../leads.d/LEAD-tmptgrc7.md)). The idea
  is the owner's; the evidence relayed is the assistant's (Claude, in this
  session).
---
<!-- inactive-ok-file: THEORY-tmpu3iio ARG-tmpabk16 TERM-tmpf5ymd CLAIM-835 — Proposed or new; the reading, its argument, its test and the term it uses -->

# CLAIM-tmp2r6ur: The most informative signal in a learned spectrum lies in a truncated band: the top directions carry common, weakly discriminating structure, as stop words do in a corpus, the extreme bottom carries low-signal outliers, as rare words do, and once both are cut, the bottom of the retained band holds the most discriminating directions

**The owner's claim.** "this connects to classic NLP pre-processing for topic modeling, e.g. where both the most common (stop words) and least common (low signal outliers) are often eliminated to distill signal in a text corpus. i.e. the most informative signal is in the truncated spectrum, and the bottom of that spectrum is often characterized by highly discriminating directions."

**What it predicts, spectrally.**
- **The top directions** carry common structure that matters in bulk, in [TERM-tmpf5ymd](../terms.d/TERM-tmpf5ymd.md)'s sense of the bulk by weight, but discriminates little: the analogue of stop words.
- **The extreme bottom** carries low-signal outliers: the analogue of rare words.
- **Between them,** once both ends are cut, the bottom of the retained band is where the most discriminating directions lie.

**What the record holds that bears on it.**
- **Xu ([THEORY-tmpu3iio](../theory.d/THEORY-tmpu3iio.md), [NOTE-tmp454fw](../notes.d/NOTE-tmp454fw.md)).** Across ten models, the unembedding's bottom 5% band is the most discriminating per unit of logit distance: prediction change several times random, because the two leading candidate tokens differ disproportionately there ([CLAIM-835](CLAIM-835.md)). The top band costs as much total loss or more in nine of ten models, which fits common structure that matters in bulk.
- **The truncation, in Xu's own data** (App. E.1, checked against the paper's text). In the two Qwen models, "a few coordinates on which the normalization weight γ is close to zero give directions with near-zero singular values". Those directions carry 38% and 43% of the band change's squared length. With them excluded, "K is 7.7 and 8.5 times random instead of 3.5 and 4.1". The floor dilutes the signal, and below it lies the most discriminating band. [ARG-tmpabk16](../arguments.d/ARG-tmpabk16.md) argues this support.

**What is untested.** Whether the top singular directions track token frequency, as stop words would. Xu does not test it. [LEAD-tmptgrc7](../leads.d/LEAD-tmptgrc7.md) would.

The idea is the owner's; the evidence relayed is the assistant's (Claude, in this session).
