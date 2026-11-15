---
status: Proposed
promote_when: >-
  The proofs of Lemma 3.1 and Theorem 3.2 (Appendix B) checked, or an
  independent experiment showing a probe-guided removal that leaves the
  concept decodable while lowering main-task accuracy, and INLP driving a
  classifier that does not use the concept to chance when task and
  concept labels are correlated.
title: 'On Kumar, Tan and Sharma, for frozen disentangled representations under max-margin training a probe for a concept puts nonzero weight on correlated main-task features even when the concept''s own features separate it perfectly, so removal guided by such a probe can leave concept features in place while corrupting task features, and on a classifier that never used the concept, iterative nullspace projection drove main-task accuracy to chance'
version: 1
tags:
- representation-learning
- learning-theory
date: '2026-11-15'
source:
- LIT-tmpzdaep
bears_on:
- QUESTION-010
summary: >-
  Kumar, Tan & Sharma (2022), LIT-tmpzdaep, read in NOTE-tmpqbu99, main
  text only. The theory is stated under strong conditions (frozen,
  disentangled, max-margin), and the collapse is shown on text
  classification. The wording is the reader's; adopting it is the
  owner's call.
---

# THEORY-tmpfrtac: On Kumar, Tan and Sharma, for frozen disentangled representations under max-margin training a probe for a concept puts nonzero weight on correlated main-task features even when the concept's own features separate it perfectly, so removal guided by such a probe can leave concept features in place while corrupting task features, and on a classifier that never used the concept, iterative nullspace projection drove main-task accuracy to chance

## Source

Kumar, Tan & Sharma (2022), LIT-tmpzdaep; read in NOTE-tmpqbu99.

## The result

- Lemma 3.1: the max-margin concept probe "will use spurious features",
  wm ≠ 0 on the main-task features.
- Theorem 3.2: INLP's first step corrupts the main-task features, and the
  corruption "is non-invertible with subsequent projection steps".
- Theorem 3.3: adversarial removal cannot tell an encoder that still uses
  the concept from the desired one by its adversarial accuracy.
- §4.2: on a clean classifier, "the main-task classifier's accuracy
  eventually goes to 50% random guess accuracy".

## What it does not show

- That removal fails without the correlation between task and concept
  labels the theory assumes.
- That the result holds for fine-tuned or entangled representations,
  which the theory excludes.
- Anything about removal methods that do not use a probe as the proxy.
