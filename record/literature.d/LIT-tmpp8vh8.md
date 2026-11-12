---
status: Active
status_note: >-
  read 2026-11-12 (NOTE-tmpt8cah) in full from arXiv v2. Worth reading as the batch's one comparison with community character LoRAs, qualitative only, and for its plain statement of the trade between per-character training and a single forward pass.
title: 'InstantID: Zero-shot Identity-Preserving Generation in Seconds'
version: 2
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Filed, not read, from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44). The record held no LIT with arXiv
    2401.07519, this title or this first author with this subject,
    checked on 2026-11-12. Checked against the arXiv API the same day:
    Qixun Wang, Xu Bai, Haofan Wang, Zekui Qin, Anthony Chen, Huaxia Li, Xu Tang and Yao Hu, arXiv 2401.07519, v1 submitted 2024-01-15,
    which is `published:`. The summary follows the arXiv abstract and what
    A says of the work; a reading should check both.
- version: 2
  date: '2026-11-12'
  note: >-
    Read (NOTE-tmpt8cah) from arXiv v2 (2401.07519, 2 February 2024; v1 of 15 January 2024). Read in full: abstract, §§1–5, and the appendix figures through their captions. References skimmed. Status Deferred to Active. THEORY-tmpgxdpz filed. Venue or type: technical report (arXiv comment: "Technical Report"). Corrections: Article type: a technical report, by the arXiv comment. No venue. The summary is rewritten from the reading.
tags:
- representation-learning
- anthology-candidate
date: '2026-11-12'
published: '2024-01-15'
arxiv: '2401.07519'
first_author: 'Wang'
keywords:
- 'InstantID'
- 'identity preservation'
- 'zero-shot personalization'
- 'IdentityNet'
implementations: []
summary: >-
  Wang et al. (2024), arXiv 2401.07519, a technical report, read in NOTE-tmpt8cah. A plug-in for a frozen SDXL, trained once by its makers on 48 H800 GPUs, keeps a face's identity from one photo with no test-time tuning; in qualitative comparisons it is "competitive" with community character LoRAs, and its compatibility is claimed for models "fine-tuned from the same base diffusion model". Registered from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44). It bears on CASE-tmp40vka, CASE-tmp3isyl, CLAIM-tmpnwq8a and QUESTION-095.
---
<!-- inactive-ok-file: THEORY-tmpgxdpz CASE-tmp40vka CASE-tmp3isyl CLAIM-tmpnwq8a — Proposed; the reading's account and the entries it bears on, filed on the same branch -->

# LIT-tmpp8vh8: InstantID: Zero-shot Identity-Preserving Generation in Seconds

Qixun Wang, Xu Bai, Haofan Wang, Zekui Qin, Anthony Chen, Huaxia Li, Xu Tang and Yao Hu (2024). "InstantID: Zero-shot Identity-Preserving Generation in Seconds." arXiv 2401.07519; technical report (arXiv comment: "Technical Report").

## Key takeaways

Read in NOTE-tmpt8cah; the account is THEORY-tmpgxdpz. Single-image, tuning-free identity preservation for a frozen SDXL: a face-recognition embedding injected by decoupled cross-attention, plus IdentityNet, a ControlNet conditioned on facial keypoints and the embedding.

## Standing in the record

Registered on 2026-11-12 from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), for the history of how image
generators keep a character's identity (CASE-tmp40vka), and read the same
day at the owner's request. It is machine-learning method, read here for
the economics of amortization (QUESTION-095), not for practice.
