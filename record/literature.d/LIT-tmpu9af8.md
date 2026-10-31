---
status: Active
status_note: >-
  read in full 2026-10-31 (NOTE-tmp8ljm4); worth reading for its exact
  split of the multi-token-prediction gradient into self-distillation
  toward the model's own next-token head and a data-target residual
  (THEORY-tmpxb5pl), and for what the split does not carry: in the
  DeepSeek-style heads of its main results the student sees the same
  tokens as its teacher, so it is not the information projection the
  exchange read into it.
title: 'Multi-Token Prediction Done Right'
version: 2
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Filed, not read, from U15 (the owner's link), A15 and A16 of the
    exchange "Analyze nucleation concepts" (2026-10-30 to 31).
    Citation checked against arXiv (v1 2026-10-28, single author).
    Code at github.com/JaydenTeoh/Soft-MTP. The summary follows the
    abstract and the readers' check of the HTML text; the paper was
    not read for the record. The summary follows the abstract and
    the exchange's description; a reading should check it first.
- version: 2
  date: '2026-10-31'
  note: >-
    Read in full from the arXiv preprint 2610.38331v1, 23 pp., in
    NOTE-tmp8ljm4; status Deferred → Active. The citation stands. The
    summary is rewritten from the text. The decomposition is as A15
    described it, and A16's routing claim holds (Table 1, App. B.4). A15
    and A16 were wrong that the student has less context than its teacher,
    except for Meta-style heads (App. C). THEORY-tmpxb5pl and
    THEORY-tmpjc4k3 filed. The anthology-candidate flag stays: the paper
    is an instruction for ML practice.
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-10-31'
published: '2026-10-28'
arxiv: '2610.38331'
first_author: 'Teoh'
keywords:
- 'multi-token prediction'
- 'self-distillation'
- 'next-token prediction'
- 'Soft-MTP'
implementations: []
summary: >-
  Teoh (2026). With a shared linear output head, the cross-entropy
  gradient at each multi-token-prediction hidden state is exactly the
  gradient of a forward KL toward the model's own position-aligned
  next-token prediction, held fixed, plus the next-token cross-entropy
  gradient at the aligned state. A one-line straight-through routing
  sends only the KL part to the MTP heads and trunk, keeping
  cross-entropy at the head. The residual carries about 80% of the MTP
  gradient reaching the trunk at about a quarter of the KL part's
  signal-to-noise ratio. Removing it ("Soft-MTP") improves next-token
  loss, speculative decoding and zero-shot accuracy at 167M–1.2B by
  small margins in single runs.
---
<!-- inactive-ok-file: QUESTION-tmp4b001 THEORY-tmpjc4k3 — Open or Proposed; the question this work was filed for and an account it supports, cited as open -->

# LIT-tmpu9af8: Multi-Token Prediction Done Right

Teoh, J. (2026). Multi-token prediction done right. arXiv:2610.38331.

Read in full in NOTE-tmp8ljm4.

## Why this is here

The owner linked it at U15: "maybe framing this recursive production as self-distillation could be helpful". A15 and A16 built on its decomposition the reading of self-distillation as conditional projection: the student reproduces the teacher averaged over what the student cannot see. That is [QUESTION-tmp4b001](../questions.d/QUESTION-tmp4b001.md)'s starting point. The reading confirms the decomposition and A16's routing, and corrects the premise. In the DeepSeek-style heads behind every main result, the MTP head is fed the intervening tokens and conditions on the same prefix as its next-token teacher. Teacher and student differ in depth of computation, not in information. The conditional-projection limit, with its irreducible conditional mutual information, belongs to the privileged-context case of Hossain et al. (LIT-tmpbnm77, THEORY-tmpfm1ma). Here it is zero (THEORY-tmpxb5pl).
