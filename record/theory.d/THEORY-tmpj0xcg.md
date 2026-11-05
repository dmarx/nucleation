---
status: Proposed
promote_when: >-
  A reading confirms that a built array covering all minterms of its
  inputs computes, for each of at least two distinct programmed address
  paths, the corresponding function over all input combinations, with
  programming done only by the path of an actuator steered by the array's
  own origami logic.
title: 'An array of non-volatile bistable origami switches laid out one module per minterm can be programmed to any combinational function of its inputs by a mobile actuator that sets the modules it passes, so programmability moves from rewiring into an addressing path that origami logic itself steers'
version: 1
tags:
- natural-sciences
date: '2026-11-05'
source:
- LIT-tmp57hqx
summary: >-
  Chen, Tan and Yan (2025), LIT-tmp57hqx, read in NOTE-tmp2uw2z. Built and
  tested for 2- to 4-input arrays (half and full adder and subtractor,
  2-bit adder or multiplier); generality to any function is by construction over
  pre-built minterm modules. It does not say that the device programs
  itself: the address path is fixed by a magnet layout designed outside
  it, and the robot runs on electric motors.
---

# THEORY-tmpj0xcg: An array of non-volatile bistable origami switches laid out one module per minterm can be programmed to any combinational function of its inputs by a mobile actuator that sets the modules it passes, so programmability moves from rewiring into an addressing path that origami logic itself steers

## Source

Chen, Tan and Yan (2025), LIT-tmp57hqx; read in NOTE-tmp2uw2z.

## What was actually shown

- **Units**: bistable Kresling switches set by magnetic torque, keeping
  state without power; negligible degradation after 10,000 cycles for
  single units.
- **Arrays**: a 2×2 array as half-adder or half-subtractor, a 3-input
  2-output array as full adder or subtractor, a 4-input 4-output array as
  2-bit adder or multiplier, each programmed by the addressing path.
- **Addressing**: a robot whose wheel motors are switched by two origami
  units follows a layout of magnets and activates the minterm modules it
  passes.

## What this does not say

- That programming is internal to the device: the magnet layout is the
  program, designed outside it.
- That the system is purely mechanical: motors, power and voltage readout
  are electrical.
- That it scales cheaply: modules grow as 2^n per output, and scalability
  is claimed "under unlimited computational resources".
- That it learns: the weight update is described in the Supplementary
  Information, not demonstrated.
