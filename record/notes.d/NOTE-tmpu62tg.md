---
status: Read
paper: LIT-2301
title: 'Thorne, Vlachos, Christodoulopoulos and Mittal — FEVER: a large-scale dataset for Fact Extraction and VERification'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/1803.05355. Read: main
    text in full; appendix (annotation guidelines) not read. A delegated
    reader drafted the reading; quotations were rechecked by script against
    the downloaded copy, and any that did not match were kept as paraphrase
    without quotation marks.
date: '2026-11-12'
summary: >-
  FEVER is a dataset of 185,445 claims made by altering sentences from the
  introductions of about 50,000 popular Wikipedia pages (June 2017 dump).
  Altered means paraphrase, negation, entity or relation substitution,
  generalization and specialization. A second annotation pass, without sight
  of the source sentence, labelled each claim SUPPORTED, REFUTED or
  NOTENOUGHINFO and recorded the evidence sentences for the first two.
---
<!-- inactive-ok-file: CASE-tmppm4do — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmpu62tg: Thorne, Vlachos, Christodoulopoulos and Mittal — FEVER: a large-scale dataset for Fact Extraction and VERification

## Contribution

The first large-scale claim-verification dataset that requires retrieved evidence. Its evaluation counts a verdict correct only with a complete correct evidence set.

## Key results

- Size and agreement (Abstract): "185,445 claims", "annotators achieving 0.6841 in Fleiss κ".
- Baseline (Abstract): "The best accuracy we achieve on labeling a claim accompanied by the correct evidence is 31.87%, while if we ignore the evidence we achieve 50.91%."
- Multi-sentence evidence (§1): "Claims require composition of evidence from multiple sentences in 16.82% of cases", and multi-page evidence in 12.15%.
- Evidence annotation is incomplete (§3.4.2). Against super-annotators, evidence precision and recall "was 95.42% and 72.36% respectively". The authors grant (§5.2): "it is not feasible to ensure that the evidence selection annotations are complete".
- Annotators were told to keep world knowledge out (§3.4.4). "Shakira is Canadian" should be NOTENOUGHINFO, not REFUTED, absent explicit evidence, "since dual citizenships are permitted".
- The hard part is evidence selection (§1): "the most challenging part of the task is selecting the sentences containing the evidence".

## Assumptions

Wikipedia introductions are the reference corpus, and the truth of a claim is relative to them. Verification is retrieval plus entailment. NOTENOUGHINFO claims carry no evidence, so the classifier is trained for that class on sampled sentences.

## Concepts

Claim verification against textual sources; evidence sets; SUPPORTED / REFUTED / NOTENOUGHINFO; claim mutations; FEVER score (verdict and evidence both correct).

## Bearing on the record

The exchange calls it "Claim verification against cited textual evidence" and says it is "Useful for a source-verification component, not argument evolution or belief revision". **Accurate.** One nuance: FEVER verifies against a fixed corpus, not against the evidence a claim cites. Systems must find the evidence.

The LIT names none, and no branch entry cites [LIT-2301](../literature.d/LIT-2301.md).
- **[CASE-tmppm4do](../cases.d/CASE-tmppm4do.md)**: its failure kind "missing evidence: the ambiguity cannot be resolved", with the correct response "record the uncertainty or ask for more; change nothing", has a direct analogue in FEVER's NOTENOUGHINFO label. FEVER's guidance to annotators to keep world knowledge out of the verdict is a precedent for scoring an abstention as correct. Bears as a design precedent, nothing more.
- The record's own verification step (read-and-file step 7, quotes checked against source text) is a verification task of FEVER's kind on a much smaller scale. FEVER's finding that evidence recall, not entailment, is the bottleneck is a caution for any automated check of the record's quotes. That is a remark, not a code.

## Limitations

The guidelines appendix was not read, and Table 4 (full pipeline numbers) was read only from the abstract and the §5.7 text.
