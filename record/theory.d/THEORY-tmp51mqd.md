---
status: Proposed
title: 'Zhang, Lepori and Pavlick find that a frozen subnetwork computing a shared arithmetic subtask, isolated by a weight mask in a small transformer and transplanted into a fresh one, lets it learn a target containing that subtask from about a thousand disambiguating samples, at least as efficiently as transferring the whole trained model, while a same-size random subnetwork of the trained model needs about six times as much data'
version: 1
source:
- LIT-tmpsnc7a
tags:
- compositionality
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent replication with several seeds per configuration finds
  that a frozen discovered subnetwork for a shared arithmetic subtask,
  transplanted into a fresh model, reaches high accuracy on a target
  containing that subtask with several times fewer disambiguating samples
  than a size-matched random subnetwork of the same trained model and than
  training from scratch, and at least matching full-model transfer, with
  checkpoints selected without unambiguous held-out data.
corroborates:
- CLAIM-756
summary: >-
  From the reading of LIT-tmpsnc7a in NOTE-tmpnu6cu. The closest prior
  research found for LEAD-tmphfbq0: transplant with a size-matched
  control, no matched comparison of organizations. Proposed until its
  promote_when is met.
---

# THEORY-tmp51mqd: Zhang, Lepori and Pavlick find that a frozen subnetwork computing a shared arithmetic subtask, isolated by a weight mask in a small transformer and transplanted into a fresh one, lets it learn a target containing that subtask from about a thousand disambiguating samples, at least as efficiently as transferring the whole trained model, while a same-size random subnetwork of the trained model needs about six times as much data

## The account

GPT-2-style models of 2 to 12 layers learn a + ab mod 7; the masked subnetwork for ab mod 7 (3 to 8 per cent of masked weights), frozen in a fresh model, brings a² + ab mod 7 to near-perfect accuracy with about 1000 disambiguating samples; full transfer does no better; a size-matched random subnetwork needs about six times as many; scratch reaches about 51 per cent.

## Evidence

Five seeds for one configuration; toy arithmetic; first-stage cost not counted.
