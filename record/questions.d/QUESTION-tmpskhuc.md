---
status: Open
title: 'Does aligning independently trained networks over the architecture''s full symmetry group remove most of the linear barrier at standard width, on ImageNet or a language corpus, with an alignment computed without data; is the barrier that remains a difference in what the endpoints compute; and does it rise with depth?'
version: 1
tags:
- loss-landscapes
- representation-learning
date: '2026-10-29'
line: learned-structure
refines:
- QUESTION-069
summary: >-
  The promotion condition formerly on THEORY-112, with its dropped depth
  clause, moved here when the eleventh status review narrowed it to what
  alignment removed in the networks its sources measured and promoted it,
  as THEORY-114's moved to QUESTION-312.
---

# QUESTION-tmpskhuc: Does aligning independently trained networks over the architecture's full symmetry group remove most of the linear barrier at standard width, on ImageNet or a language corpus, with an alignment computed without data; is the barrier that remains a difference in what the endpoints compute; and does it rise with depth?

## Why it is a question

THEORY-112 holds what alignment removed in each network measured: all of
the barrier for MNIST MLPs and 32×-wide ResNet-20s, two-thirds for an
ImageNet ResNet-50, not all of it at 1× width, and for small transformers
nearly all of it once an orthogonal map on the residual stream, learned
against the midpoint loss, was added. Whether most of the barrier is
symmetry at the scales practice trains, and what the rest is, is not
shown. Nor is the depth clause it once carried: on straight lines after
alignment the only measurement is Entezari et al.'s handful of
zero-barrier MNIST MLPs (Fig. 7), and Ferbach et al.'s compounding width
is a sufficient condition, not a measurement.

## What would answer it

THEORY-112's former promote_when, unchanged:

The residual barrier after full-group alignment accounted for at a scale
the sources do not reach. The zero barriers so far are for MNIST MLPs, a
32×-wide ResNet-20 on CIFAR-10, and small ViTs and GPT-2s whose alignment
was learned against the loss at the midpoint. ImageNet ResNet-50 keeps a
third of its barrier, and BookCorpus keeps 0.42. What would promote:
independently trained models at standard width, on ImageNet or a language
corpus, brought to near-zero held-out barrier by a data-free alignment
over the architecture's full symmetry group. Or the residual barrier shown
to track a difference in what the endpoints compute, as LIT-669's
barriers do, so that "most" is the part that is symmetry and the rest is
identified. What would refute it: same-data, same-procedure solutions
whose barrier stays near the unaligned value under every alignment the
full group allows, learned ones included, when the endpoints are shown to
rely on the same input attributes. A third or fourth permutation-finding
algorithm on vision models at moderate scale cannot settle it.

For the depth clause: the barrier after alignment tracked against depth at
fixed width, with seeds, for convnets or transformers, under one alignment
method fixed in advance.
