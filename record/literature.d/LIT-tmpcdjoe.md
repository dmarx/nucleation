---
status: Active
status_note: >-
  The record's cleanest quantitative instance of an earlier acquisition
  lowering a later one's sample cost, as a law; pretraining's own cost is
  excluded. Read on 2026-11-19 ([NOTE-tmpmxg4d](../notes.d/NOTE-tmpmxg4d.md)).
title: 'Scaling Laws for Transfer'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Registered and read on 2026-11-19 at the owner's request (LEAD-
    tmpjdtrl), from arXiv 2102.01293v1 (PDF). Not held before; the
    identifier checked on the arXiv API.
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-19'
published: '2021-02-02'
arxiv: '2102.01293'
first_author: 'Hernandez'
keywords: []
implementations: []
summary: >-
  Hernandez, Kaplan, Henighan and McCandlish (OpenAI), arXiv 2102.01293.
  Effective data transferred is the extra Python a same-size from-scratch
  model would need to match a text-pretrained model's loss. In the low-
  data regime it follows D_T = k·D_F^α·N^β (α≈0.18, β≈0.38 for text;
  α≈0.096 with code mixed in, same β), so pretraining multiplies fine-
  tuning data by a factor that falls with fine-tuning data and grows with
  model size. Outside that regime the fit fails and small pretrained
  models can end worse than from scratch ("ossify"). Pretraining's cost is
  set aside; no order comparison. Read in [NOTE-tmpmxg4d](../notes.d/NOTE-tmpmxg4d.md); account THEORY-
  tmp1mk7r.
---

# LIT-tmpcdjoe: Scaling Laws for Transfer

Danny Hernandez, Jared Kaplan, Tom Henighan and Sam McCandlish (2021). "Scaling Laws for Transfer". arXiv 2102.01293.

## Standing in the record

Registered and read on 2026-11-19 at the owner's request, under [LEAD-tmpjdtrl](../leads.d/LEAD-tmpjdtrl.md).
