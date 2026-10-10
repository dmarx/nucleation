---
status: Active
title: 'Voita, Sennrich and Titov''s BLEU-tied translation systems that differ on keeping ты or вы across sentences'
version: 1
standing: documented
tags:
- translation
- model-comparison
- pragmatics
date: '2026-10-10'
line: pragmatic-transport
supports:
- CLAIM-142
summary: >-
  Two English-to-Russian subtitle translation systems score the same
  BLEU (32.40 and 32.38, not significantly different). On a contrastive
  test built from held-out films, which asks whether a system keeps the
  T or V form of "you" consistent across sentences, one is at chance
  (50.0%) and the other is right in 81.6% of cases. A documented
  instance, on a pragmatic distinction, of two realizations equal under
  a standard probe family and different under an independently built
  one. An ML paper that neither record holds.
---
<!-- inactive-ok-file: CLAIM-142 — Proposed; the claim this case supports, open -->
<!-- inactive-ok-file: CLAIM-077 — Proposed; cited for the collapse the baseline shows, not as settled -->

# CASE-tmpt7tsv: Voita, Sennrich and Titov's BLEU-tied translation systems that differ on keeping ты or вы across sentences

Found on 2026-10-10 by a search the owner asked for: a documented case for
the first half of [CLAIM-142](../claims.d/CLAIM-142.md), that two realizations can agree on every probe
in a restricted family and still differ.

## The case

Voita, Sennrich and Titov (ACL 2019) translate English film subtitles into
Russian. English "you" has one form. Russian chooses between ты (T,
familiar) and вы (V, formal or plural), and the verb agrees. A translator
working one sentence at a time has to choose afresh in each sentence.

**The human study that set the target (§2).** Annotators were shown 2000
pairs of consecutive sentences translated by a context-agnostic system. In
7% of pairs "the sentences were considered individually good, but bad in
context of each other". Annotators were told to flag a pair only if "there
is no other possible interpretation". Deixis caused 37% of these
discrepancies (Table 2), and within deixis the "T-V distinction" caused 67%
(Table 3). The annotators' qualifications are not stated in the sections
read.

**The probe built from it (§3.1, Appendix A.1).** The deixis test set "tests
the ability of a machine translation system to produce translations with
consistent level of politeness". Each item is a group of consecutive
sentences with a reference translation, plus a contrastive translation that
switches T and V. Both versions are "correct plausible translations at a
sentence level, and only context reveals the errors". The system scores
both, and is counted right when it prefers the true one. Items with words
that fix the form ("Mr.", "officer", "mom", "dude") were removed, and native
speakers checked that both the polite and the familiar version of each
fragment were natural on their own. The sets were built "from 400k held-out
instances from movies not encountered in training".

**The two systems (§6, Tables 6 and 7).**

| | BLEU, general test set | Deixis accuracy (T-V consistency) |
|---|---|---|
| Context-agnostic Transformer, 6m pairs | 32.40 | 50.0 |
| CADec, context-aware second pass | 32.38 | 81.6 |

"Scores for CADec are not statistically different from the baseline (6m)"
(Table 6, bootstrap resampling). The authors' own reading: "models
indistinguishable with BLEU can be very different in terms of consistency"
(§6), and the test sets "let us distinguish models which are otherwise
identical in terms of BLEU" (§6.3). Table 9 repeats the pattern inside one
architecture: four CADec variants have BLEU 32.31 to 32.45 and deixis
accuracy 80.0 to 84.1. §6.4: "BLEU is not sufficient as a criterion for
stopping: even when a model has converged in terms of BLEU, it continues to
improve in terms of consistency".

**A human comparison, of a pair that is not BLEU-tied.** In the follow-up
paper (Voita, Sennrich and Titov, EMNLP 2019) CADec and the baseline are
again tied (BLEU 33.86 and 33.91), and a further system, DocRepair, reaches
deixis 91.8 against the baseline's 50.0 with BLEU 34.60. Annotators shown
700 groups blind judged 52% equal; of the rest they preferred DocRepair in
242 and the baseline in 90 (Table 5).

## What it can show

The first half of [CLAIM-142](../claims.d/CLAIM-142.md) in a measured textual setting, on a pragmatic
distinction rather than an image statistic. BLEU on a general test set is
the field's standard probe family, fixed before the comparison and not
fitted to these systems. The two systems agree under it. A probe built
independently, from a human study of what makes good sentences bad in
context, and evaluated on held-out films, separates them. The distinction
the second probe sees is the social relation between two speakers, which
the T/V choice encodes. That is the distinction [CASE-tmpmsyg7](CASE-tmpmsyg7.md) (Dolly's slip
into ты) and [CASE-tmp6whdw](CASE-tmp6whdw.md) (Tatiana's letter) are about, measured here in
machine output.

The probe meets the exclusion version 2 of [CLAIM-142](../claims.d/CLAIM-142.md) added: it does not
elicit judges' same-act verdicts and is not fitted to them. It scores a
system's preference between two fixed candidates. It was designed from the
human study's categories, so it targets a phenomenon judges care about
without being their verdict.

The baseline's 50.0 is collapse in the sense of [CLAIM-077](../claims.d/CLAIM-077.md). A
context-agnostic model gives the two candidates the same score, so it
cannot keep a T-consistent and a V-consistent continuation apart at all.

## What it cannot show

**The partly met condition: competent uptake of these outputs.** [CLAIM-142](../claims.d/CLAIM-142.md)
asks for a documented difference "on held-out probes or in competent
uptake". The held-out probe is met in full. Uptake is met only at one
remove. The human study shows that the distinction the baseline misses is
one native annotators treat as making a translation wrong, but it was run
on the baseline's outputs only. No reader compared the outputs of the
BLEU-tied pair. The one blind human comparison, in the follow-up, is of
DocRepair against the baseline, a pair 0.7 BLEU apart.

**The probe scores candidates, not outputs.** BLEU is computed on what each
system produces. Deixis accuracy is computed on which of two given
translations the system prefers. So the two probes are not applied to the
same realization. A system that prefers the consistent candidate could still
produce an inconsistent translation, and the paper does not report T-V
consistency in the systems' own outputs.

**Consistency, not the right footing.** Every item admits both T and V; the
annotators confirmed that each fragment was natural in either form. The
test asks whether a system keeps one relation once set, not whether it
picks the relation the scene calls for. It shows that BLEU misses a
relational distinction. It does not show that either system gets the
relation right.

**The defender's reply.** The defender holds that a finite probe family fixed
in advance separates every pair judges distinguish, so that observational
and structural identity coincide in practice ([CLAIM-142](../claims.d/CLAIM-142.md)'s defeat
condition). The reply: nobody claimed BLEU was such a family. Add the
deixis, ellipsis and cohesion sets and the family separates this pair; the
case shows that one family was too coarse, which the defender grants. That
reply is correct as far as it goes. The case supports the relative half of
[CLAIM-142](../claims.d/CLAIM-142.md), that equivalence is relative to the probe family, and the rule of
evidence, that only independently justified held-out probes count. It does
not support the realist half, that no finite family suffices. For that, the
enlarged family would itself have to be shown to leave judge-distinguished
pairs unseparated.

**What would close the gap.** A reader test on the BLEU-tied outputs. Native
Russian readers, blind to system, would judge multi-sentence scenes from the
held-out films, translated by each system, on whether the forms of address
fit the relation between the speakers and stay consistent. A separate
measure would score T-V consistency in the generated outputs, not in the
candidates. Then the enlarged probe family (BLEU with all three contrastive
sets) would be tested against those readers on a further set of system
pairs: if readers separate pairs the family does not, the realist half has
evidence. The design matches the interlingual arm of the discriminating
study, [CASE-tmp1uzfn](CASE-tmp1uzfn.md), whose targets are languages where T/V is obligatory
and the English leaves it open. Voita et al.'s deixis fragments are public,
and could serve as its English-to-Russian items.

**Boundary.** This is an ML paper. It is held in neither record: a check of
the anthology clone on 2026-10-10 found no LIT for it or its follow-up, and
this record holds none. Its natural home is the anthology, where it is a
candidate. No nucleation LIT is filed. Filing one here would need a NOTE
reading it for pragmatic transport ([ADR-013](../decisions.d/ADR-013.md)), as [CASE-041](CASE-041.md) says of its own
sources.

## Sources

Every URL below was retrieved on 2026-10-10.

- **E. Voita, R. Sennrich and I. Titov**, "When a Good Translation is Wrong
  in Context: Context-Aware Machine Translation Improves on Deixis,
  Ellipsis, and Lexical Cohesion", *Proceedings of ACL 2019*, DOI 10.18653/v1/P19-1116, arXiv:1905.05979. Read directly, in
  the arXiv PDF (v2); section, table and appendix references are to it. Not
  held in either record.
- **E. Voita, R. Sennrich and I. Titov**, "Context-Aware Monolingual Repair
  for Neural Machine Translation", *Proceedings of EMNLP-IJCNLP 2019*, DOI
  10.18653/v1/D19-1081, arXiv:1909.01383. Read directly, Tables 2, 4 and 5
  and §5.3, in the arXiv PDF. Not held in either record.
- The annotators' qualifications in the human study, and whether the
  published version differs from arXiv v2 in any figure quoted, were not
  checked. **Unverified.**
