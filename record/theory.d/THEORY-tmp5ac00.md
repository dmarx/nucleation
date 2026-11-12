---
status: Proposed
title: 'Shumailov et al. show that when each generation of a generative model is trained only on samples from the previous generation, finite-sample, expressivity and approximation errors compound so that the tails of the original distribution are lost and the learned distribution drifts toward a low-variance point'
version: 1
tags:
- learning-theory
- anthology-candidate
date: '2026-11-12'
source:
- LIT-tmp5p7t7
promote_when: >-
  a reading of the Theoretical intuition section confirms the
  absorbing-state argument and Theorem 3.1 under single-generation
  replacement, and the language-model section confirms perplexity
  degradation across generations and the milder degradation when 10% of the
  original data is retained.
bears_on:
- QUESTION-tmp7a7l4
summary: >-
  The central account of [LIT-tmp5p7t7](../literature.d/LIT-tmp5p7t7.md), read in [NOTE-tmp56sxk](../notes.d/NOTE-tmp56sxk.md). Proposed until
  its promote_when is met.
---

# THEORY-tmp5ac00: Shumailov et al. show that when each generation of a generative model is trained only on samples from the previous generation, finite-sample, expressivity and approximation errors compound so that the tails of the original distribution are lost and the learned distribution drifts toward a low-variance point

## The account

Shumailov et al. show that when each generation of a generative model is trained only on samples from the previous generation, finite-sample, expressivity and approximation errors compound so that the tails of the original distribution are lost and the learned distribution drifts toward a low-variance point. They prove this for discrete distributions and recursively fitted Gaussians, and illustrate it with OPT-125m fine-tuned over generations, where retaining 10% of the original data limits the degradation.

