---
status: Proposed
title: 'Mordvintsev and colleagues show that a neural cellular automaton trained only to grow a target pattern from a seed grows it but does not reliably persist it, that training it to persist from its own outputs makes the pattern stable and often partly regenerative, and that adding damage during training gives robust regeneration, including from kinds of damage not seen in training'
version: 1
source:
- LIT-tmp5gwuj
tags:
- complex-systems
- representation-learning
date: '2026-11-19'
corroborates:
- CLAIM-566
- CLAIM-672
promote_when: >-
  A reproduction across seeds and targets that measures, for the three
  training regimes, the rates of growth to target, persistence over a
  fixed long horizon and recovery after a fixed damage, and finds the
  ordering the article shows: growth-only below persistence-trained below
  damage-trained on persistence and recovery.
summary: >-
  From the reading of LIT-tmp5gwuj in NOTE-tmpz3s4o. Mordvintsev,
  Randazzo, Niklasson and Levin (2020), Distill, DOI
  10.23915/distill.00023, CC-BY. A continuous cellular automaton with a
  small learned update rule shared by all cells grows an emoji from one
  seed; trained only to grow, the patterns die out, overgrow or are only
  almost stable; trained from a pool of their own outputs, the target
  becomes an attractor that persists and often partly regenerates; trained
  with damage, the patterns regenerate robustly, even from damage not seen
  in training. Here because A15 of the exchange "Topological protection
  explained" used it to separate persistence from regeneration, held as
  CLAIM-566: the three training regimes do separate growth, persistence
  and regeneration, though persistence training brings some regeneration
  with it, and the regenerating rule is supplied from outside the pattern.
  Read in its NOTE.
---

# THEORY-tmpeaw52: Mordvintsev and colleagues show that a neural cellular automaton trained only to grow a target pattern from a seed grows it but does not reliably persist it, that training it to persist from its own outputs makes the pattern stable and often partly regenerative, and that adding damage during training gives robust regeneration, including from kinds of damage not seen in training

## The account

A 16-channel continuous cellular automaton with a learned, shared local update grows an emoji from one seed cell. Trained only to match the target after 64-96 steps, many models die out, overgrow or are only almost stable. Training from a pool of earlier outputs, so that the rule must keep or improve an already formed pattern, makes the target an attractor; such models persist and often regenerate damage they were never trained on. Damaging pool samples in training widens the basin, and the models then regenerate robustly, including from damage of shapes not seen in training.

## What it does not show

- Measured rates: the evidence is a handful of models in animations.
- Regeneration after turnover, or regeneration by constraints the pattern itself produces: the rule and the alive mask are external and fixed.
- Why persistence training brings partial regeneration, beyond the informal attractor reading.
