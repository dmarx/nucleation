---
status: Active
status_note: 'read 2026-10-09 (NOTE-tmppmfwl); worth reading here as a controlled comparison of two uses of the same demonstrations: held as context (in-context learning) or turned into a temporary update of the model''s weights (test-time training, per-task LoRA, discarded after the task). With nothing added but the update, BIG-Bench Hard 10-shot accuracy goes from 50.5% to 57.8% and fine-tuned ARC accuracy roughly sixfold on an 80-task subset (5% to 29%). The update works best when its training data keep the in-context format. The comparison is empirical, at 1B–8B parameters, on two benchmarks with known leakage risk.'
title: 'The Surprising Effectiveness of Test-Time Training for Few-Shot Learning'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed here as well as in the anthology (ANTH-LIT-379), under ADR-013,
    and read on 2026-10-09 (NOTE-tmppmfwl) from the arXiv v2 PDF (25 Mar
    2025, 22 pp.); the PMLR camera-ready PDF was fetched to check one
    number and agrees with v2 on it. Bibliography checked against the arXiv
    API (authors Ekin Akyürek, Mehul Damani, Adam Zweiger, Linlu Qiu, Han
    Guo, Jyothish Pari, Yoon Kim, Jacob Andreas; v1 submitted 11 November
    2024, which is `published:` per ADR-002) and the PMLR volume 267 index
    (ICML 2025, pp. 942–963, as the manuscript's bibliography gives). The
    anthology holds it as ANTH-LIT-379, read as a technique and as evidence
    about in-context learning's limits; a grep of its record/ (clone of
    2026-10-09, commit d8b5ba5) confirmed this.
tags:
- learning-theory
- representation-learning
date: '2026-10-09'
published: '2024-11-11'
arxiv: '2411.07279'
first_author: 'Akyürek'
keywords:
- 'test-time training'
- 'few-shot learning'
- 'in-context learning'
- 'ARC'
- 'BIG-Bench Hard'
- 'LoRA'
- 'transduction'
implementations: []
summary: >-
  Akyürek, Damani, Zweiger, Qiu, Guo, Pari, Kim and Andreas (2024), ICML
  2025. Test-time training here is a temporary, per-task LoRA update of a
  language model on a loss built from the task's own demonstrations,
  discarded afterwards. On BIG-Bench Hard (10-shot, Llama 3.1 8B) it
  raises accuracy from 50.5% (in-context learning) to 57.8%; on ARC it
  takes a fine-tuned 1B model from 5% to 29% on an 80-task subset and an
  8B system to 53.0% on the public validation set. Training on
  leave-one-out in-context tasks beats training on the bare pairs.
---

# LIT-tmp686hl: The Surprising Effectiveness of Test-Time Training for Few-Shot Learning

Ekin Akyürek, Mehul Damani, Adam Zweiger, Linlu Qiu, Han Guo, Jyothish
Pari, Yoon Kim and Jacob Andreas (2024), *ICML 2025*, PMLR 267:942–963 —
ARXIV-2411.07279

## Key takeaways

- **Same information, two uses.** The comparison that matters here is
  between conditioning on K demonstrations and updating the model's
  weights on them before conditioning: no other data enters. The update
  is temporary (task-specific LoRA, then discarded), so the model's
  persistent parameters are unchanged in both cases.
- **BIG-Bench Hard**, Llama 3.1 8B, 10 demonstrations, 27 tasks, five
  seeds: zero-shot 40.9%, in-context 50.5%, test-time training 57.8%.
  Gains are concentrated in tasks with structural rules or distribution
  shift (Dyck languages, Ruin names, Movie recommendation, Hyperbaton,
  20–50 points); Boolean expressions falls (85.7% → 80.4%).
- **ARC**, 80-task subset, fine-tuned Llama 3.2 1B: 5% → 29% (about 6×).
  Full public validation set: 18.3% → 47.1% (their fine-tuned 8B), 53.0%
  applied to the BARC model, 61.9% in the text with BARC's synthesizer
  (Table 1 prints 62.8%); 47.5% on the semi-private set.
- **The in-context format matters to the update.** Training on
  leave-one-out in-context tasks (each demonstration in turn treated as
  the query, the rest as context, with permutations) beats training on
  the bare input-output pairs: on ARC, 11 fewer tasks solved with direct
  I/O; on BBH, 57.8% vs 51.5%. Augmenting with invertible
  transformations matters most on ARC (16 tasks).
- **One adapter or many.** A per-task adapter beats a shared one on ARC;
  on BBH a shared adapter is better (59.8%), which the authors attribute
  to tasks that are distinguishable in plain text and mutually helpful.

## Standing in the record

Held in both records under ADR-013. The anthology holds it as ANTH-LIT-379,
read for the technique and as evidence about in-context learning's limits,
with a practice built on it. It is filed here at the owner's request on
2026-10-09, from the bibliography of the owner's manuscript *What Survives
Translation?* (work `what-survives-translation`), which considered it and
dropped it from the final reference list. The second question, the one
this record asks, is the reading on this record's terms: what the paper
shows about the difference between conditioning a fixed model on evidence
and changing the model with the same evidence. That reading is
NOTE-tmppmfwl.

**A discrepancy, reported not fixed (ADR-013).** The anthology entry and
its practice give 61.9% for the ensemble with program synthesis, as the
paper's abstract and text do; the paper's Table 1 prints 62.8% for the
configuration the text describes, in both the arXiv v2 and the PMLR
camera-ready. The anthology's figure follows the text, which is
defensible; the inconsistency is the paper's.

Not tagged `anthology-candidate`: the anthology already holds it. The
tags are the nearest words the closed vocabulary offers, and the fit is
weak.
