---
number: 599
status: Active
formerly:
- THEORY-tmpom30b
title: "In trained neural-network weights stored as BF16 or FP32, nearly all the redundancy a lossless coder can remove lies in the floating-point exponent, which occupies about 40 of its 256 values and compresses to about a third under single-symbol Huffman coding, while sign and mantissa are near-incompressible; the redundancy belongs to the number format, not to the learned function"
version: 1
tags:
- information-theory
date: '2026-10-16'
source:
- LIT-268
summary: >-
  Hershcovitch et al. (2024), ZipNN, [LIT-268](../literature.d/LIT-268.md), read in full in [NOTE-241](../notes.d/NOTE-241.md).
  Fifteen models broken down by byte group (Table II), with the exponent
  skew shown on four (Fig. 2) from 1 GB middle slices. A parameter
  shuffle changes Zstd's exponent compression by at most 0.05%, so the
  gain is order-0. The paper never computes an entropy. Its explanation
  of the skew is partly wrong as stated, and its remark that the
  redundancy shows overparametrization unused does not follow from what
  it measured.
---

<!-- inactive-ok-file: THEORY-277 — Proposed; named for the distinction they draw, nothing here rests on them -->

# THEORY-599: In trained neural-network weights stored as BF16 or FP32, nearly all the redundancy a lossless coder can remove lies in the floating-point exponent, which occupies about 40 of its 256 values and compresses to about a third under single-symbol Huffman coding, while sign and mantissa are near-incompressible; the redundancy belongs to the number format, not to the learned function

## Source

Hershcovitch et al. (2024), "ZipNN: Lossless Compression for AI Models",
arXiv 2411.05239 v2, [LIT-268](../literature.d/LIT-268.md), read in full in [NOTE-241](../notes.d/NOTE-241.md), with v1's
appendix for the model identifiers.

## What was actually shown

**The exponent distribution (Fig. 2, §III-A).** On Llama 3.1 BF16,
Granite 7B BF16, Qwen BF16 and ResNet-50 FP32, about 40 of the 256
exponent values occur (50 for ResNet), and the top 12 cover "almost
99.9%" of parameters. The histograms are "strikingly similar" across
models and formats.

**Per-field compressibility (Table II).** The exponent compresses to
about 33%; sign and fraction bytes to ≈100% on regular models. So BF16
models compress to about 66.4% (Falcon-7B, OpenLLaMA-3B, Mistral,
Llama-3.1) and FP32 models to about 83% (wav2vec 83.3%, BERT 83.0%, OLMo
83.1%). Models rounded or converted after training ("clean") compress
further, 33.7–48.1% for FP32, through zeroed low-order fraction bytes.

**Order-0 only (§III-A b).** A random shuffle of the parameters changes
Zstd's exponent compression by at most 0.05%. LZ4 and Snappy save
nothing. Huffman beats Zstd only after the exponent is extracted
(Fig. 4), and an FSE coder, which tracks the order-0 entropy more
closely, is only 0–2% better.

**Implied entropy ([NOTE-241](../notes.d/NOTE-241.md)'s inference, not the paper's).** About 33%
of 8 bits is ≈2.6 bits per exponent, and Huffman's code length is within
one bit of the order-0 entropy, so that entropy is roughly 1.6–2.6 bits,
well below log₂ 40 ≈ 5.3.

What could have come out otherwise: the mantissa could have carried
removable structure, or neighbouring parameters could have been
correlated so that LZ found repeats. Neither held.

## What this does not say

- **That trained weights have low information content.** These are
  compression ratios of particular files under one order-0 coder: upper
  bounds on description length, not estimates of a source entropy, of
  Kolmogorov complexity, or of an MDL two-part code length ([NOTE-241](../notes.d/NOTE-241.md), on
  [LIT-224](../literature.d/LIT-224.md), [LIT-225](../literature.d/LIT-225.md) and [LIT-238](../literature.d/LIT-238.md)).
- **Anything about generalization-relevant compressibility.** The bounds
  of Sefidgaran et al. ([LIT-233](../literature.d/LIT-233.md), [LIT-236](../literature.d/LIT-236.md)) concern lossy compressibility of
  the learned function; the mantissa, which carries the fine values, is
  the part that proved incompressible.
- **That overparametrization is unused.** The paper's §VII remark (C10)
  runs format redundancy together with functional redundancy.
- **Why the exponent is skewed.** The paper's account invokes Adam's ε as
  weight "noise" (it sits in the update's denominator) and misplaces the
  exponent values; it concedes "no matter the reason" (C4, weak).
- **That it holds for quantized formats.** Some GPTQ and AWQ checkpoints
  compress to 85–91%; GGUF does not compress.

## Connections

- The practice the paper carries (store and serve checkpoints with
  exponent extraction and entropy-only coding) is anthology material, as
  [NOTE-241](../notes.d/NOTE-241.md) says; this THEORY states only the finding about the format.
- [THEORY-244](THEORY-244.md) (Shannon quantities are expectations of Kolmogorov ones
  only to within the source's complexity) and [THEORY-277](THEORY-277.md) (two-part codes
  for individual data) mark the distinction this finding must not
  cross.
