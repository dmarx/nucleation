---
number: 1143
status: Proposed
formerly:
- THEORY-tmpocg1h
promote_when: >-
  An experiment that varies the information capacity of the intermediate
  domain against the source's, holding the architecture fixed, and shows
  that the hidden channel appears when a one-to-one correspondence in the
  intermediate's visible code is impossible and disappears when it is
  not, with the hidden information measured. Or a counter-instance: a
  round-trip-trained translator between domains of unequal complexity
  whose round trip closes using only what the intermediate's audience
  reads. Further examples of hiding, without the capacity manipulation,
  do not settle it.
title: 'When one domain carries more information than the other, a translation trained only to make the round trip close cannot meet that requirement through a correspondence in the intermediate''s visible code, so the round trip closes through a channel the intermediate''s audience does not read; agreement of the round trip with its source therefore says nothing about whether the intermediate renders the source''s content for that audience'
version: 1
tags:
- information-theory
- representation-learning
- translation
date: '2026-10-29'
source:
- LIT-1800
summary: >-
  Chu, Zhmoginov and Sandler (2017), [LIT-1800](../literature.d/LIT-1800.md), §2 and §5, read in
  [NOTE-1346](../notes.d/NOTE-1346.md). The authors argue it from the many photographs a single
  map stands for, and support it with [THEORY-1127](THEORY-1127.md)'s evidence on one
  model; they propose, and do not run, the test of adding capacity to the
  smaller domain. Proposed. It is the converse of the record's collapse
  case for [CLAIM-496](../claims.d/CLAIM-496.md): there routes agree because nothing travels,
  here because everything does, out of sight.
---

# THEORY-1143: When one domain carries more information than the other, a translation trained only to make the round trip close cannot meet that requirement through a correspondence in the intermediate's visible code, so the round trip closes through a channel the intermediate's audience does not read; agreement of the round trip with its source therefore says nothing about whether the intermediate renders the source's content for that audience

## Source

Chu, Zhmoginov and Sandler (2017), [LIT-1800](../literature.d/LIT-1800.md), §2 (p. 2) and §5
(pp. 4–5) of arXiv 1712.02950v2; read in [NOTE-1346](../notes.d/NOTE-1346.md).

## What was actually shown

**The argument.** CycleGAN asks for GFx = x. If many photographs correspond
to one map, as differences in "rooftop color or tree location" do, then
"it is impossible for a CycleGAN model to learn a perfect one-to-one
correspondence between aerial photographs and maps" (p. 2). A map that
showed only map content could not let G recover which photograph it came
from. So the loss can be met only if Fx carries more than it shows. "If X
and Y are of different complexity – if their distributions have differing
entropy – it may be impossible to learn a one-to-one transformation
between them. We demonstrated that CycleGAN sidesteps this asymmetry by
hiding information about the input photograph in a low-amplitude,
high-frequency signal added to the output image" (pp. 4–5).

**The evidence** is [THEORY-1127](THEORY-1127.md)'s: on one model, the reconstruction
uses information the visible map lacks, carried at high frequency and low
amplitude.

**The general point** the authors draw: "caution is necessary when
designing loss functions that involve compositions of neural networks:
such models may behave in unintuitive ways if one component takes
advantage of the ability of the other component to support adversarial
examples" (p. 5).

**What could have failed.** The round trip could have been imperfect in
exactly the details the map cannot show. That is what a translator
restricted to the map's visible code would do, and it is not what the
model does.

## What this does not say

- **That the capacity asymmetry is the cause.** The test the authors
  propose, a fourth channel that gives the map room to carry the
  photograph (p. 5), is not run. A model could also hide information
  between domains of equal complexity if the loss rewards it.
- **That round-trip agreement is worthless.** It measures whether the
  composition is invertible. What it does not measure is whether the
  intermediate is a rendering for its reader. In the record's terms it is
  a coherence criterion ([CLAIM-496](../claims.d/CLAIM-496.md)), and this case shows it can be
  maximal while the intermediate, read as intended, loses the content.
- **Anything about translation between languages directly.** The case is
  images. The analogy to relay translation, where a pivot language
  carries what its readers cannot see, is the record's, not the paper's.
- **That a discriminator on the intermediate closes the gap.** One was
  present and scored realism; it did not check content.
