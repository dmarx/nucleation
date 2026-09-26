---
status: Skimmed
paper: LIT-tmp40qq4
title: 'Shannon information vs Kolmogorov complexity (survey)'
version: 1
date: '2026-09-26'
summary: >-
  Shannon's and Kolmogorov's theories line up concept by concept (entropy vs complexity, probabilistic vs algorithmic mutual information and sufficient statistics, rate-distortion vs structure function), and in each pair the Shannon notion is, up to additive terms, the expectation of the Kolmogorov one.
---
<!-- inactive-ok-file: LIT-tmp40qq4 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-tmplitpc: Shannon information vs Kolmogorov complexity (survey)

## Contribution

The survey compares the elementary theories of Shannon information and Kolmogorov complexity, asking where they share a purpose and where they differ fundamentally. It pairs their basic notions: entropy with complexity, both with universal coding, and probabilistic with algorithmic mutual information. It also pairs probabilistic with algorithmic sufficient statistics (read as lossy compression versus meaningful information), and rate-distortion theory with Kolmogorov's structure function. Much of the material was scattered across earlier papers. The authors say this is the first systematic comparison and that the final relations are new.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1.1 (pp. 3–4): an eight-point overview running from coding and the Kraft inequality, through entropy, complexity and mutual information, to sufficient statistics and rate-distortion vs structure function. This works as a map of the whole algorithmic-statistics programme.
- §2.3, Thm 2.10: for a computable distribution f, the f-expected Kolmogorov complexity exceeds the entropy H(X) by at least 0 and at most K(f)+O(1). This is the formal "entropy = expected complexity".
- §5.2.1: K(x) read as a two-part code (a model part plus a data-to-model part). The "model" bits are the meaningful information and the rest is accidental. The task of statistics and learning theory is framed as distilling the former.
- §5.3, Defs. 5.9–5.12 and Thm 5.13: an algorithmic sufficient statistic is a probabilistic "nearly-sufficient" statistic in expectation for every computable model family. Remark 5.11 shows that the individual-sequence and expectation versions of near-sufficiency come apart.
- §6 and Thm 6.27 (p. 48): the expected structure function h_x(R) is bounded by Shannon's distortion-rate function D*(R) from both sides, up to K(f,d,m,R) terms. §7 says §§5.3 and 6.3 are new material.
- §7 (pp. 49–50): MDL and universal coding are presented as the practical offspring that avoid both the "true distribution" assumption and the uncomputability of K.

## Open questions

- It is the most direct bridge in the batch between the heading "K-complexity and minimum sufficient statistics" and ordinary (Shannon-style) statistics, so it is a natural entry point for the other Vitányi papers.
- The authors themselves flag errors in this draft. A deeper reading should cross-check any theorem it cites against Li & Vitányi's textbook or the journal papers (k03, k04).
- Check exactly which constants and log terms Thm 5.13 and Thm 6.27 hide. For an argument that uses "expected algorithmic = probabilistic", those terms are where it can fail.
