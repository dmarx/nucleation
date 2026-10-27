---
status: Unfetched
status_note: >-
  searched 2026-10-27 for a lawful full text; one exists but this client
  could not fetch it, so it is not read and no NOTE is filed (ADR-053).
  Unpaywall lists the publisher's free copy at Project Euclid (bronze,
  the published version); it answered curl with a bot challenge ("Just a
  moment..."), and a headless-browser fetch was not attempted, since it
  would be working around the challenge. The failure is on access, not
  availability. A browser fetch of that copy is the cheapest way to read
  it. It stays Unfetched until a copy is supplied.
title: 'On a Measure of the Information Provided by an Experiment'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read. Citation checked against Crossref on 2026-10-27: D.
    V. Lindley, The Annals of Mathematical Statistics 27(4), 986–1005,
    December 1956; Crossref gives no day, so `published:` carries the
    first of the month.
- version: 2
  date: '2026-10-27'
  note: >-
    Reading attempted on 2026-10-27. Unpaywall's one open copy, the
    published PDF at projecteuclid.org, returned a bot-challenge page to
    curl. Status Deferred to Unfetched under ADR-053.
tags:
- mathematical-statistics
- information-theory
date: '2026-10-27'
published: '1956-12-01'
doi: '10.1214/aoms/1177728069'
first_author: 'Lindley'
keywords:
- 'Bayesian experimental design'
- 'expected information gain'
- 'Shannon information'
implementations: []
summary: >-
  Lindley (1956). Proposes Shannon's expected information, the expected
  reduction in entropy of the prior over parameters, as a measure of
  what an experiment provides, and uses it to compare and choose
  experiments.
---

# LIT-tmpya1jp: On a Measure of the Information Provided by an Experiment

Lindley, D. V. (1956). On a measure of the information provided by an experiment. *The Annals of Mathematical Statistics*, 27(4), 986–1005. doi:10.1214/aoms/1177728069.

Not read: a lawful open copy exists but could not be fetched on 2026-10-27 (see the status note). The summary is drawn from what the work is standardly cited for and from the exchange's description of it. A reading should check it first.

## Why this is here

A16 §7 cited it as the foundation of expected-information-gain design,
and drew the limit that matters here: information gain is relative to
the hypothesis space already specified, so "The inquiry can become
increasingly precise without becoming correct." The record holds the
later review ([LIT-1525](LIT-1525.md)). It bears on [CLAIM-tmpalzo4](../claims.d/CLAIM-tmpalzo4.md).
