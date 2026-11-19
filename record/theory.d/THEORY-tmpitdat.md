---
status: Proposed
title: 'Poole, Lahiri, Raghu, Sohl-Dickstein and Ganguli show, in the mean-field theory of wide random fully connected networks, that the slope of the correlation map at correlation 1 divides the weight and bias variances into an ordered phase, where nearby inputs converge, and a chaotic one, where they separate; that in the chaotic phase an input curve''s length grows exponentially with depth while its curvature holds at a fixed point, so its global curvature grows exponentially with depth; and that a one-hidden-layer network can extend a curve''s length only in proportion to its width'
version: 1
source:
- LIT-tmpzpom9
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent derivation or simulation reproduces the χ1 = 1 phase
  boundary, the length and curvature recursions for a circle at the
  fixed-point radius with the exponential growth of its Gauss-map length
  in the chaotic phase, and Theorem 1's bound on shallow networks.
corroborates:
- CLAIM-360
bears_on:
- QUESTION-281
summary: >-
  From the reading of [LIT-tmpzpom9](../literature.d/LIT-tmpzpom9.md) in [NOTE-tmpa7swy](../notes.d/NOTE-tmpa7swy.md). The mean-field theory
  Schoenholz and colleagues build on. Proposed until its promote_when is
  met.
---

# THEORY-tmpitdat: Poole, Lahiri, Raghu, Sohl-Dickstein and Ganguli show, in the mean-field theory of wide random fully connected networks, that the slope of the correlation map at correlation 1 divides the weight and bias variances into an ordered phase, where nearby inputs converge, and a chaotic one, where they separate; that in the chaotic phase an input curve's length grows exponentially with depth while its curvature holds at a fixed point, so its global curvature grows exponentially with depth; and that a one-hidden-layer network can extend a curve's length only in proportion to its width

## The account

In a wide random network with Gaussian weights and biases, signal
propagation becomes deterministic: one map gives the squared length of
an input across layers, another the correlation of two inputs. The slope
χ1 of the correlation map at 1 is the per-layer stretch of a small
perturbation, its logarithm a Lyapunov exponent; χ1 = 1 separates an
ordered phase, where inputs converge, from a chaotic one, where they
separate, and finite depth makes the chaos transient. In the chaotic
phase a one-dimensional input manifold's length grows exponentially with
depth while its extrinsic curvature approaches a fixed point, so its
global curvature grows exponentially with depth and not with width. Any
one-hidden-layer network with a monotone bounded nonlinearity bounds the
length linearly in its width (Theorem 1).

## Evidence

Derivations in the large-width limit, simulations of tanh networks, and
a theorem for shallow networks. At initialization only; the link from
curve length to approximation is numerical.
