---
number: 1153
status: Proposed
formerly:
- THEORY-tmptu082
promote_when: >-
  An annotation of a random sample of English-source human translations,
  drawn without a named-entity or alignment filter, by at least two
  annotators working from the same guidelines with their agreement per
  category reported, that gives per-language rates of explicitation per
  sentence and finds measurement and entity explicitations the most frequent
  types. Rates within PETra's own filtered pool, or classifier counts, do
  not settle it.
title: 'In English-source TED and Europarl translations, the additions a translator makes for the target audience that a named-entity and null-alignment filter can find are mostly unit conversions and entity descriptions or specifications, and their mix differs by target language'
version: 1
tags:
- translation
- pragmatics
date: '2026-10-29'
source:
- LIT-1798
summary: >-
  Osmelak et al. (2026), [LIT-1798](../literature.d/LIT-1798.md), read in [NOTE-1344](../notes.d/NOTE-1344.md) from the LREC
  2026 PDF. Of 3,754 type instances in Table 2, 1,722 are system transfers
  (mostly measurement conversion) and 992 entity changes; the mix varies by
  language. It is a count over a pool selected by a filter that requires a
  named entity, mostly found by a classifier, labelled with no reported
  agreement. It is not a base rate of explicitation in translation, and it
  says nothing about how readers take the additions.
---

# THEORY-1153: In English-source TED and Europarl translations, the additions a translator makes for the target audience that a named-entity and null-alignment filter can find are mostly unit conversions and entity descriptions or specifications, and their mix differs by target language

## Source

Osmelak, Dutta Chowdhury, Sentsova, España-Bonet and van Genabith (2026),
[LIT-1798](../literature.d/LIT-1798.md), §§3–6 and Table 2, pp. 8758–8764 of the LREC 2026
proceedings; read in [NOTE-1344](../notes.d/NOTE-1344.md).

## What was actually shown

English sentences from TED-Multi and Europarl were aligned to their
translations in twelve languages with eflomal and SimAlign. Pairs with a named
entity and an unaligned target noun, pronoun or proper noun were annotated by
hand (p. 8760). A BERT classifier trained by active learning on German and
Spanish found further pairs (§5). Each explicitation was typed under a
four-family schema (Table 1, p. 8760).

Table 2 (p. 8761) counts 992 entity, 1,722 system, 744 linguistic and 296
added-information instances (the ADD column as printed sums to 307). In the
release, measurement conversion alone accounts for 1,093 of about 3,880
labels. The mix differs: German and Spanish TED have mostly system
transfers (708 of 1,072; 352 of 570), Persian mostly entity changes and
added information (99 and 63 of 200), Europarl German mostly entity changes
(100 of 172).

What could have come out otherwise: the filter requires a named entity, so
entity-linked additions were bound to be common. That measurement conversion,
which needs no entity of its own, leads is less forced. It may still follow
from the sentence carrying some entity, or from the classifier learning
units as an easy cue.

## What this does not say

- **Not a rate of explicitation in translation.** The counts are within a
  filtered candidate pool. The paper's own rates (2.6% of TED candidates
  extracted, 2.5% classified positive; p. 8761) are rates within that pool.
- **Not a reliable labelling.** No inter-annotator agreement is reported,
  and the text points to one annotator (fn. 5, p. 8763). Three quarters of
  the pairs were found by a classifier (2,250 of 2,982).
- **Not a cross-linguistic law.** Persian, Hebrew, Thai and Arabic pairs
  are classifier finds only, with no test set in those languages. The
  family-level statements (p. 8764) are not backed by a statistic.
- **Nothing about receivers.** Whether an addition changes what target
  readers take the speaker to be doing, or what source readers would say
  about the added content, is not measured.
- **Not pragmatics in the sense of act or footing.** "Pragmatic" here is
  Klaudy's audience-oriented explicitation of background knowledge.
