---
number: 82
status: Proposed
formerly:
- CLAIM-tmpnt2nd
title: 'A term''s value, as distinct from its signification, is fixed by its contrasts with the coexisting terms of its system'
version: 3
history:
- version: 2
  date: '2026-10-28'
  note: >-
    Narrowed at the sixth status review to record CLAIM-072's
    concession (ADR-059), which ARG-034 judged: Saussure says value,
    as distinct from signification, is fixed by contrast, and does not
    set it against reference. Version 1's title read: A sign's
    communicative significance is fixed by its contrasts within a
    system rather than by correspondence to a referent. That title is
    kept as CLAIM-489, Proposed; the use-level part is
    CLAIM-242's and ARG-033's. LIT-775 leaves the grounds, and
    THEORY-175, THEORY-182 and THEORY-185, cited as working cases,
    move to corroborated_by (ADR-058).
- version: 3
  date: '2026-10-29'
  note: >-
    The thirteenth status review (ADR-057). The defeat condition's
    second clause is restated at the level of value, which the version 2
    narrowing left at the level of use. It read: 'or a case where a
    term's communicative role is unchanged when its contrasts with
    coexisting terms are changed.' Communicative role is the use-level
    notion ARG-033 concedes value is not; the test is now THEORY-159's
    promote_when. The title and status are unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  A reading of Saussure or of the structuralist tradition that shows
  value to be fixed by reference, or a term whose range of use and
  interpretation stays fixed when a coexisting term of its field is
  added, lost or merged, against terms outside the field as a control.
tags:
- linguistics
- philosophy-of-language
date: '2026-10-09'
line: pragmatic-transport
works:
- what-survives-translation
grounds:
- THEORY-159
corroborated_by:
- THEORY-175
- THEORY-182
- THEORY-185
summary: >-
  The manuscript's structuralist premise (§2), citing Saussure and Lévi-
  Strauss. [CLAIM-072](CLAIM-072.md) corrects how it states Saussure.
supports:
- CLAIM-115
- CLAIM-036
illustrated_by:
- CASE-019
complements:
- CLAIM-242
- CLAIM-489
---
<!-- inactive-ok-file: CLAIM-489 — Rejected; the first title, kept as its own entry and rejected on its own condition -->
<!-- inactive-ok-file: THEORY-182 — Proposed; cited as a reading that bears on this claim, not as settled -->

# CLAIM-082: A term's value, as distinct from its signification, is fixed by its contrasts with the coexisting terms of its system

## The claim

§2: "Saussure's account of linguistic value makes the significance of a sign
depend upon contrasts within a system, rather than on intrinsic correspondence
to a referent." Lévi-Strauss is cited for extending relational and
transformational analysis to myth. The manuscript uses the premise to motivate
relational identity, with the proviso that not every transformation is a
symmetry.

## What it does not say

It is a motivating premise, not a result the manuscript relies on formally.
Lévi-Strauss is unread here ([LIT-775](../literature.d/LIT-775.md)), so his part of it rests on a work cited
without a reading.

## A qualification from experiment

Bergen, Goodman and Levy ([LIT-809](../literature.d/LIT-809.md)), Experiment 1: a novel symbol's
interpretation is fixed by its contrast with the alternative the speaker
could have used. But the contrast works only because one alternative is
tied to an object by resemblance. Read against this claim, it is contrast
together with reference, not contrast instead of it.

## A qualification from machine representations

Moschella and colleagues' relative representations ([LIT-849](../literature.d/LIT-849.md), read in
[NOTE-652](../notes.d/NOTE-652.md)) are a working case of the premise in one respect. Each input is
represented only by its cosine similarities to a set of anchor inputs from
the same system, and a decoder trained on those similarities transfers,
untrained, between independently trained encoders ([THEORY-175](../theory.d/THEORY-175.md)). Identity by
relations within a system is enough to carry a decoder across systems that
share no coordinates.

The reading adds two qualifications, and both point the same way as the one
from experiment above.

- **Across systems, contrast needs a correspondence.** Between languages or
  modalities, the anchors must be matched from outside: translated reviews,
  sentences aligned in WikiMatrix. Within one system relations suffice; for
  transport between systems they work only once something ties the anchor
  in one to the anchor in the other. That is contrast together with
  correspondence, as in Bergen, Goodman and Levy.
- **The relational encoding is lossy and approximate.** Independently
  trained encoders agree in their relative vectors only approximately: the
  vectors correlate highly, but most nearest neighbours differ. Where a
  shared absolute space already exists (a multilingual encoder), the
  relational encoding transfers worse than the absolute one in every
  language pair tested.

The analogy has a limit of its own. A cosine to an anchor is a metric
relation in a vector space, invariant only to cosine-preserving maps. Saussure's
value is opposition among coexisting terms, and [THEORY-159](../theory.d/THEORY-159.md) does not make it
a similarity. The case shows that relational identity can be engineered and
carried between systems. It does not show that this is Saussure's value.

## A model whose meanings are purely relational

Karkada, Simon, Bahri and DeWeese ([LIT-855](../literature.d/LIT-855.md), read in [NOTE-660](../notes.d/NOTE-660.md)) solve a close
proxy of word2vec in closed form ([THEORY-182](../theory.d/THEORY-182.md)). The learned embeddings are
the top eigenvectors of one matrix: the relative deviation of each word
pair's co-occurrence from independence. Nothing else enters, and the loss
sees only inner products between embeddings, so each embedding is fixed
only up to a common rotation. A word's learned representation is therefore
nothing but its pattern of departures from chance co-occurrence with every
other word, and the analogy structure the model shows comes out of that.

That is the premise realised in a model, in one respect: identity by
relations within a system, with no reference anywhere in the training
signal. Its limits match the qualifications above. Co-occurrence is not
Saussure's opposition either ([THEORY-159](../theory.d/THEORY-159.md)). The result is proved for a proxy
of word2vec, not word2vec. And it is a fact about what a model learns from
text, not evidence about how significance is fixed in a language.

Its sequel (Karkada et al. 2026, [LIT-860](../literature.d/LIT-860.md), read in [NOTE-664](../notes.d/NOTE-664.md)) adds a
sharper case and a qualification. The months are still placed on a circle
from their co-occurrence with *other* words after their co-occurrences with
each other are deleted (Fig. 4), so each one's position is fixed by its
relations within the vocabulary. But those relations are organised by an
extralinguistic variable, the time of year, and the geometry learned is
isomorphic to it. Relations within the system carry the structure of what
the words are about. That supports "fixed within a system" without setting
relation against reference, the same qualification as Bergen, Goodman and
Levy's.

The precursor, Korchinski, Karkada, Bahri and Wyart ([LIT-863](../literature.d/LIT-863.md), read in
[NOTE-665](../notes.d/NOTE-665.md)), is the closest formal case so far. Each word is modelled as
nothing but a set of binary contrasts, and when each contrast multiplies
co-occurrence independently, the PMI embedding is an affine image of the
word's position among them, so the analogy parallelograms come out exactly
([THEORY-185](../theory.d/THEORY-185.md)). That is opposition, not similarity, which is nearer
Saussure's value than the cosine and co-occurrence cases above. A contrast
also survives deleting every word pair that differs only in it, so each
word's relations to the rest of the vocabulary carry it. The same
qualification holds: the contrasts are posited in advance, and many are
properties of what the words refer to.

## Note of 2026-10-28: narrowed; what holds it back

The sixth status review narrowed this claim to what Saussure's value
carries, recording [CLAIM-072](CLAIM-072.md)'s concession, which [ARG-034](../arguments.d/ARG-034.md) judged. The first
title is [CLAIM-489](CLAIM-489.md). Kept Proposed: its reading of Saussure,
[THEORY-159](../theory.d/THEORY-159.md), is Proposed, and nothing in the record meets `defeated_if`.

## Note of 2026-10-29: what holds it back

Held by [THEORY-159](../theory.d/THEORY-159.md)'s promote_when: no study in the record adds, loses or
merges a term in a language's inventory and measures whether its
neighbours' use shifts, against terms outside the field, and that is also
the second clause of this claim's defeat condition.

## Note of 2026-10-30: what holds it back

THEORY-159 is a premise here, not corroboration or an attribution
(ADR-058). The title asserts Saussure's account, and the second clause of
`defeated_if` is THEORY-159's promote_when. A "Saussure proposes" split of
THEORY-159 would not free it, since the claim needs the account true, not
only proposed. It waits on a study that adds, loses or merges a term in a
language's inventory and measures the neighbouring terms' use against
terms outside the field.
