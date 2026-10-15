---
status: Read
paper: LIT-tmpnfh60
title: Harris et al. — Failures to replicate a key result of selective accessibility
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the authors' manuscript on UCL's institutional
    repository, UCL Discovery eprint 10074759 (discovery.ucl.ac.uk/10074759/1/HarrisEtAl_2019_anchoring.pdf,
    fetched directly, HTTP 200, 76 pp.). It is a Word-generated manuscript, not
    the APA typeset article. It has a running head, an author note, a word count
    and manuscript page numbers, and the PDF was generated on 23 May 2019, seven
    weeks before online publication (11 July 2019, per Crossref and PubMed). Unpaywall
    and OpenAlex both label this copy `submittedVersion`. Its abstract differs in
    wording from the published abstract as PubMed gives it ("tests that subsequently
    failed" against "evidence which was not obtained"; "its use" against "their
    use"), so it is not the version of record. Whether it is the accepted manuscript
    could not be checked, because the UCL landing page and its OAI-PMH endpoint
    returned a Cloudflare challenge (403). The APA version of record (doi.apa.org,
    psycnet.apa.org) also returned 403. The manuscript's page numbers do not map
    onto the published pages e30–e50. Text was extracted with pdftotext in both
    flowing and layout modes. Table 2 (absolute estimates) was read from the layout
    extraction because the flowing extraction scrambles it. Read: the abstract,
    the introduction and the review of earlier lexical-decision results, Experiments
    1–5 (method, results, discussion), the exploratory Bayesian meta-analysis, the
    general discussion, the conclusion, "Context of the Research", the reference
    list, Appendices 1–3 (counterbalancing tables and practice-task materials, scanned
    rather than read row by row), and Supplementary Experiments 1–3. Figures 1,
    2, S1 and S2 are bar charts of mean log RTs; they were not read as images, and
    the results are taken from the reported tests. The OSF materials and preregistrations
    (osf.io/jtx34) were not opened, apart from confirming that the project exists,
    its title ("Is anchor consistent knowledge subsequently more accessible, as
    measured by a lexical decision task? A replication.") and its creation date
    (20 November 2015). Mussweiler and Strack (2000a), the paper replicated, is
    not in the record and was not read, so what it found is this paper's account
    of it. Semantic Scholar's API refused the lookup (429). Every quotation from
    the paper was checked against the extracted text by script, with whitespace
    normalised. The published abstract's wording was checked against the PubMed
    record (PMID 31294586), and quotations from record entries were checked against
    those files. Cohen's d values for the anchoring effects are computed here from
    the reported t statistics (d = 2t/√df) and are not given in the paper.
date: '2026-10-15'
summary: >-
  Five preregistered experiments (N = 128 each, about four times the originals'
  N) failed to replicate the lexical-decision result of Mussweiler and Strack (2000a,
  Studies 1 and 2). That result was that after a comparison with a high or low anchor,
  words consistent with the anchor are recognised faster. Every experiment produced
  a large anchoring effect on the later estimate (d ≈ 0.85–1.39), and none showed
  the accessibility interaction (all η²G ≤ .004). An exploratory Bayesian meta-analysis
  gave a Bayes factor of 21.1 for the null. Validation experiments found that the
  same tasks also missed direct picture priming. So the authors conclude that the
  method cannot detect the effect, not that selective accessibility is false. They
  still call the theory "a good explanation", but say the earlier lexical-decision
  evidence "is not a strong part of the evidence base".
---
<!-- inactive-ok-file: CLAIM-tmp9snb1 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-tmpzxnap — Unavailable; held without a reading, cited as such -->

# NOTE-tmpodfzg: Harris et al. — Failures to replicate a key result of selective accessibility

## Contribution

The paper looks for a "signature test" for selective accessibility. This would be a measure that can be added to any anchoring demonstration, without redesigning it, to show whether anchor-consistent knowledge became more accessible. The authors set aside the other kinds of evidence for the theory. Manipulations that make people consider anchor-inconsistent knowledge alter the paradigm, and other accounts also predict their effects. The applicability results (Strack & Mussweiler 1997's Brandenburg Gate study, LIT-tmpkn9x0) are not a test, and "there is no a priori specification of what constitutes 'applicability'". Plausibility-by-latency results need different kinds of anchor to be compared. The qualitative free reports of Mussweiler and Strack (1999, LIT-tmpzxnap; 2000a) have "not been widely used", partly because coding them is subjective. The remaining candidate is a word-recognition task given between the comparative question and the absolute estimate. The authors call this a key claim of the account: "does an anchor selectively increase the accessibility of anchor-consistent knowledge? This is a key claim of the selective accessibility account".

The key result they try to replicate is Mussweiler and Strack (2000a, JPSP 78, "The use of category and exemplar knowledge in the solution of anchoring tasks"), Studies 1 and 2. These are the lexical-decision studies "closest to prototypical anchoring studies":
- Study 1: mean annual temperature in Germany, anchors 20°C and 5°C, summer and winter words. Interaction F(1, 26) = 4.53, p = .043, N = 28. The lexical decision task (LDT) came after the absolute estimate, which is a confound.
- Study 2: price of a midsize car, expensive-car and inexpensive-car words, LDT before the estimate. Interaction F(1, 28) = 6.57, p = .016, N = 30.

In their review, with two-tailed tests, none of the four simple effects in the originals was significant (ps .105–.534). They also note that the related studies (Mussweiler & Englich 2005, Study 3, subliminal anchors, N = 37; Englich, Mussweiler & Strack 2006, Study 4, legal experts, N = 57) show only an interaction at p ≈ .046, or one of two predicted effects. They sum up the prior support as "somewhat underwhelming with a lack of predicted simple effects, and inconsistencies between the results for high and low anchors".

The 1999 paper (LIT-tmpzxnap) is cited here for the free-report evidence (River Elbe features) and for the finding that "greater or less" and "equal to" comparisons anchor equally. It is not cited as a lexical-decision study.

## Key insight

If the comparison makes anchor-consistent knowledge more accessible, and that accessibility carries the anchoring effect, then both the estimate and the speed of recognising anchor-consistent words should move with the anchor. Here the estimate moved strongly every time and word recognition never moved. The authors then tested whether these word tasks can detect priming at all. They primed directly with pictures of summer or winter scenes, or of expensive or cheap cars, which participants plainly registered. The tasks detected nothing. So the null cannot decide the theory, but it does remove the method as evidence. The authors' reason is that semantic priming in lexical decision is short-lived: it is "predominantly observed within 2000 ms of the target stimulus" and "typically not observed with more than a single interleaving trial". In this paradigm the critical words are spread across 60–70 trials after the anchor.

## Assumptions

- **The replicated measure stands for the theory's accessibility claim.** "The more accessible information is, the faster it is predicted to be recognised". The test asks whether facilitation scores (log RT to target words minus log RT to neutral words and non-words) show an anchor × word-type interaction.
- **Updated materials are equivalent.** Anchors were set at the 5th and 95th percentiles of a London and Cambridge calibration sample (N = 100). Words were chosen by Mussweiler and Strack's pretest rules rather than translated. Car makes are proper nouns, so the LDT question was changed to "Do the following collection of letters have meaning for an English speaking person?". There were two practice "experiments" rather than seven (or four; the manuscript gives both numbers for the original). The order was always comparison, then LDT, then estimate, as in the original Study 2.
- **Power.** The planning effect was d = .5, from the originals' four simple effects (.29, .76, .56, .55). That gives 63 per cell and 128 per experiment, with stated power above 98% for the interaction (η²p = .06), and above 80% for η²p as small as .028.
- **Exclusions as preregistered.** Estimates beyond 3 SD within condition and impossible values were excluded, as were log RTs beyond 3 SD.
- **Validation logic.** If direct picture priming does not move the task, a null after anchoring "cannot be taken as evidence that priming is not occurring in the anchoring question".

## Key results

- **Design and N.** Experiments 1 (UK temperature) and 2 (new-car price) were run within the same 128 participants, in counterbalanced order, with anchors of 8°C and 20°C and of £6,000 and £30,000. Experiments 3 and 4 used a new sample of 128, with anchors chosen to match the critical words directly: 2°C and 25°C, and £13,000 and £200,000. Experiment 5 had 128 participants (38% non-native English speakers) and replaced the LDT with a Continuous IDentification (CID) task, which is reported to be more sensitive to perceptual fluency. It also included a single-trial test on the word "summer", always shown third. All five were preregistered at osf.io/jtx34 (Experiments 1 and 2 together, 3 and 4 together, 5 alone; the manuscript's numbering differs from the preregistrations').
- **Anchoring replicated in all five.** Low against high anchor means (Table 2): Experiment 1, 12.68 against 14.70°C, t(125) = 4.84; Experiment 2, £10,754 against £19,742, t(123) = 5.89; Experiment 3, 10.71 against 15.88°C, t(124) = 7.76; Experiment 4, £13,817 against £61,452, t(124) = 4.76; Experiment 5, 11.03 against 16.16°C, t(125) = 7.50. All ps < .001. Computed d ≈ 0.87, 1.06, 1.39, 0.85 and 1.34. These effects held although 70 LDT trials (40 CID trials) came between the comparison and the estimate.
- **No accessibility effect in any of the five.** Anchor × word-type interaction on facilitation scores: Experiment 1, F(1,126) = 0.07, p = .785, η²G < .001; Experiment 2, F = 1.71, p = .193, η²G = .004; Experiment 3, F = 0.40, p = .529, η²G = .001; Experiment 4, F = 1.71, p = .193, η²G = .004; Experiment 5 (CID), F = 0.41, p = .522, η²G = .001. The 2 × 4 ANOVAs on raw log RTs and the linear mixed models agree (pooled Experiments 1 and 2: anchor × summer/winter contrast t(577.01) = −1.12, p = .26). The single-trial "summer" test in Experiment 5 gave ΔM = −0.01, t(121) = −0.65, p = .517.
- **Bayes factor.** It is exploratory and not preregistered. A meta-analytic Bayes factor (Rouder & Morey 2011; Cauchy prior with scale 0.707) over the five interaction t values found the data "21.10 times more likely under the null hypothesis than the alternative", which the authors call "strong" evidence for the null. No per-experiment Bayes factors are reported.
- **Validation failures.**
  - Supplementary Experiments 1 and 2 (N = 106 first-year students in a class session, picture primes before the LDT). Manipulation checks were strong: the summer group rated the temperature 28.6°C and the winter group 0.25°C, t(104) = 44.99. There was no prime × word-type interaction (F(1,104) = 0.11 and 1.46).
  - Supplementary Experiment 3 (N = 125, picture primes before the CID). There was no interaction (F(1,123) = 0.84). The single "summer" trial went the wrong way: it was faster after winter primes, t(121) = 2.01, p = .046.
  - The authors say the supplementary studies were not "run under optimal test conditions" (a class setting, and in Supplementary Experiment 3 different graphics drivers changed the CID presentation rate).
- **Conclusions, verbatim.**
  - On the method: "signatures of selective accessibility processes are hard to detect using lexical tests of accessibility. Consequently, regardless of whether effects can be observed, these are not good signature tests."
  - On the theory: "we do not believe the current results necessarily provide additional evidence for or against that theory, which we still consider a good explanation for judgmental anchoring."
  - On the earlier evidence: "supportive evidence for selective accessibility obtained in the past using this method is not a strong part of the evidence base for that theory."
- **What still stands, on their account.** Anchoring itself: "the robustness of anchoring effects is remarkable". They also note its durability. They give two explanations for that durability and do not choose between them:
  - "participants approximate an absolute answer when answering the comparative question, which is then utilised in the generation of the absolute answer", and that answer "may result from (e.g.) selective accessibility, anchoring-and-adjustment, scale distortion…"
  - long-term semantic priming, which appears in tasks that need semantic processing but not in lexical decision. They call inferring it from anchoring itself circular: "the obvious circularity in this argument is clear."
- **Errors in this copy.**
  - The pooled mixed-model results for Experiments 3 and 4 repeat those for Experiments 1 and 2 to the second decimal (χ²(5) = 432.93; t(577.01) = −1.12; t(604.01) = ±0.77). The Experiment 4 facilitation-score interaction repeats Experiment 2's (F = 1.71, p = .193, η²G = .004).
  - The interim discussion gives the Experiment 1–2 anchors as £20,000 and 10°C/18°C, but the method gives £6,000/£30,000 and 8°C/20°C.
  - "Two 'validation experiments' (Supplementary Experiments 1-3)" counts three supplementary experiments as two.
  - The 95% CI for the Experiment 5 "summer" test is missing its lower bound in the extraction.
  - These may be corrected in the version of record, which was not reachable. None of them changes the pattern, since every reported interaction is null.

## Bearing on the record

**On CLAIM-tmp9snb1: the most direct published evidence that an anchor changes what is reachable did not replicate. The method that produced it is shown unable to detect priming at all. The claim's psychological form now rests on indirect evidence only.**

- The claim says its psychological form is "established", in the selective-accessibility account (LIT-tmpkn9x0, LIT-tmpzxnap). The part of that account the claim needs is that considering an anchor makes anchor-consistent knowledge more reachable. The lexical-decision studies were the measure of that. They belong to the line of evidence that proponents (Bahník, Englich & Strack 2017) have called the most direct support. At about four times the original N, across five preregistered experiments, the effect was zero (η²G ≤ .004, BF01 ≈ 21). Meanwhile the judgment shift was large every time. So these experiments show the judgment moving with no detectable change in measured accessibility.
- This does not meet the claim's defeat condition. The defeat condition needs a design that shows "what is retrieved does not" change. Here the validation studies show the measure was blind even to strong direct priming, so the null says nothing about retrieval either way. The authors make the same point. The paper neither refutes nor supports selective accessibility.
- What it does to the claim's reliance: the claim can no longer cite selective accessibility as a demonstrated retrieval effect. What remains for it is the following, and none of it measures retrieval:
  - moderation by applicability and representativeness (LIT-tmpkn9x0, read; small samples)
  - latency patterns across plausible and implausible anchors
  - coded free reports (LIT-tmpzxnap, unread)
  - Bahník and Strack's (2016) overlap result, whose explanations the authors note rest on "presumably"
  
  Harris et al. still favour the theory. Their reason is its fit with confirmatory hypothesis testing and semantic priming, which is a theoretical virtue and not new evidence. The claim's summary should say the retrieval step is inferred, not measured.
- The paper's leading explanation for durable anchoring is a provisional answer formed at the comparison and recalled later. That explanation is neutral between mechanisms, and it is exactly where the claim's δ/Retrieve split is unresolved. If the carrier is a recalled candidate number, the frame acts on what is answered, not on which stored distinctions are reachable. The paper cannot tell these apart.
- Correction to the record's other reading. The L1 draft NOTE (Strack & Mussweiler 1997) says the lexical-decision test of accessibility "is in Mussweiler and Strack 1999 (LIT-tmpzxnap)". By this paper's account, the lexical-decision studies are Mussweiler and Strack 2000a (JPSP 78, 1038–1052), Mussweiler and Englich 2005 and Englich et al. 2006. The 1999 paper's direct evidence is coded free reports. This is Harris et al.'s description, and the 1999 paper was not read. If it holds, LIT-tmpzxnap's "experiments on the mechanism" are free-report and comparison-format studies, not lexical decision. Mussweiler and Strack 2000a is the work that this failure to replicate bears on directly, and the record does not hold it.

**On QUESTION-tmpq93du: it bears only indirectly.** The anchoring effect lasted through 70 intervening word trials, longer than lexical priming lasts. Whatever carries an anchor forward, it is not brief lexical activation, and the authors' best guess is a provisional answer kept from the comparison. That fits the question's path-dependence worry: the cost may come from an early committed estimate, not only from which knowledge is easiest to reach. Nothing here measures benefit or cost to accuracy, or separates retrieval from evaluation.
