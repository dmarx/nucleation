---
status: Open
title: "When no single setting of a regulator is stable in every environment it may meet, must any system that comes to keep its essential variables within limits carry a channel from those variables to the parameters of its regulation, whether or not it adapts by trial and error?"
version: 1
tags:
- complex-systems
- learning-and-conditioning
date: '2026-10-19'
line: distributed-agency
summary: >-
  Filed when the promotion audit (batch 032, [ADR-047](../decisions.d/ADR-047.md) v2) narrowed and
  promoted [THEORY-324](../theory.d/THEORY-324.md). Ashby's necessity was re-derived for systems that
  follow the trial-and-error rule, where it is close to definitional. The
  former promote_when asked it of any system that comes to keep its
  essential variables within limits, which is wider. This question holds
  that wider form.
---

# QUESTION-tmpvx6hf: When no single setting of a regulator is stable in every environment it may meet, must any system that comes to keep its essential variables within limits carry a channel from those variables to the parameters of its regulation, whether or not it adapts by trial and error?

## Why it is a question

[THEORY-324](../theory.d/THEORY-324.md) now states Ashby's necessity for a system that adapts by trial
and error. Under the trial-and-error rule, the parameters must stay put
when the essential variables are within limits and change when they are
not, so the parameters depend on those variables, and a channel follows
from the rule itself. The former promote_when asked more: that any system
which comes to keep its essential variables within limits, against an
environment whose coupling to them it does not know, carries such a
channel.

In that wide form it fails trivially for a regulator whose single fixed
setting is stable in every environment of the class: nothing needs to
change, so nothing needs a channel. The question excludes that case. What
remains open is whether a system can do without the channel when it
does need different settings in different environments, but does not
follow the trial-and-error rule. One example is a regulator that learns
the environment's coupling from the environment's own variables. Another
is one whose settings are switched by a cue that happens to predict which
setting is needed.

## What would answer it

A proof that, whenever different environments in the class need
different settings, the parameters' transitions must depend on the
essential variables (directly or through intermediates), would answer it
yes. A system meeting Ashby's assumptions that finds the needed setting
with no such dependence would answer it no, as would one that relies only
on a cue correlated with the environment and carrying no information from
the essential variables. More demonstrations that ultrastable machines
adapt do not settle it: they show sufficiency only.
