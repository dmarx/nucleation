---
status: Read
paper: LIT-tmpjvhqj
title: 'U.S. Copyright Office — Copyright and Artificial Intelligence, Part 3: Generative AI Training'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from the pre-publication version of 9 May 2025 as
    published at copyright.gov (US government work), text extracted with
    pdftotext -layout with a marker at each page end. Every line of the
    main text (pp. 1–108) and of all 588 footnotes was read, in order, in
    one pass by one reader. The table of contents was read; the report has
    no appendices, index or bibliography to skip. One figure (the tokenizer
    example, p. 7) survives extraction only as its caption. No later final
    version existed to read on 2026-10-20. Every quotation here was checked
    against the extracted text by script. Page numbers are the report's
    own; PDF page = report page + 3.
date: '2026-10-20'
summary: >-
  Training copies works at every input step, so the copy trigger fires and
  everything turns on fair use. Weights count as copies only of works they
  can regenerate. Under Warhol the training use is judged by its ultimate
  purpose: often transformative for a general model, barely so for one
  that serves the originals' audience. Expression, not just ideas, is
  learned, and machine learning is not human learning. Market dilution by
  same-kind outputs is harm. Licensing should develop without intervention.
---

# NOTE-tmpwosj3: U.S. Copyright Office — Copyright and Artificial Intelligence, Part 3: Generative AI Training

## Contribution

It is the US Copyright Office's analysis, written for Congress, of whether
using copyrighted works to build generative AI needs consent or payment. It
draws on more than 10,000 comments to its August 2023 Notice of Inquiry
(pp. 1–2). It says where in development copying occurs (Part III), how the
four fair-use factors apply to each act after *Andy Warhol Foundation v.
Goldsmith* (Part IV), and which licensing arrangements could fill the gap
(Part V). It opines on no pending case (p. 2). Two of its moves are new: a
recoverability test for whether model weights are copies, and a
market-dilution theory of harm under the fourth factor. Liability for
outputs, removal of copyright management information and transparency are
left to a Part 4 (pp. 19 n. 110, 26 n. 152, 31).

## Key insight

The report accepts the copy trigger at the input and refuses it at the
artifact. Every step from scraping to the batches shown to the model makes
copies, so the acts are prima facie infringing and the question is fair use
(pp. 26–28, 107). But the trained model is not presumed to be a copy of
what it read. It is a copy of a work only if that work can be got back out
of it: "Whether a model’s weights implicate the reproduction or derivative
work rights turns on whether the model has retained or memorized
substantial protectable expression from the work(s) at issue." (p. 30). Fair
use then turns on what the model is for. The same training run can be
highly transformative or barely so depending on deployment, and on whether
guardrails stop the system serving the originals' purpose (pp. 46–47).

## Assumptions

- **US law, early 2025.** The analysis is of the 1976 Act, Supreme Court
  fair-use cases through *Warhol* (2023), and circuit cases through
  *Hachette v. Internet Archive* (2d Cir. 2024). It predates the summary
  judgment rulings on training later in 2025. Its main district-court
  authority on training is *Thomson Reuters v. Ross* (D. Del. Feb. 2025),
  about a non-generative tool (pp. 40 n. 235, 58).
- **Fixation by recoverability.** A copy need not be perceivable, only
  "fixed" and perceivable "with the aid of a machine or device" (pp.
  28–29, 17 U.S.C. § 101). Weights are fixed because they do not change, and
  memorized works can be displayed by software. The JPEG analogy (p. 28
  n. 166) carries the argument.
- **Use identified by ultimate purpose.** Following *Warhol*, *Google
  Books* and *HathiTrust*, copying to build a dataset is judged by what the
  dataset is used for, and training by how the model is deployed (pp.
  36–37, 45).
- **The comments as evidence.** The technical and market facts come from
  the comments, the developers' own papers, press reports and litigation
  filings. The Office ran no measurements of its own.
- **Copyright's purpose is human authorship.** The report takes from Part
  2 and from Sobel the view that copyright protects humans writing for
  humans (p. 73 n. 414). This shapes both the rejection of the
  human-learning analogy and the dilution theory.

## Key results

In the report's order.

- **Technical background (Part II).** Neural networks, next-token
  pre-training, scaling, data quality and curation (pp. 4–16). Pre-training
  is not a minor preliminary: it needs orders of magnitude more data and
  supplies most capabilities (p. 18). On memorization the Office sides with
  Cooper and Grimmelmann: patterns can be "highly abstract, highly
  specific, or anywhere in between" and training is not inherently limited
  to one level (p. 20). Meta's cited study found about 1% memorization,
  which on the Pile's 200 million documents "may not be trivial" (pp.
  20–21, n. 119). Developers pull pirated sources such as Books3 (196,640
  books) into datasets (p. 13 n. 70, p. 14).
- **Prima facie infringement (Part III).** Collection and curation make
  copies, often repeatedly; deleting the dataset afterwards does not help
  (pp. 26–27). Training copies to high-performance storage, and makes
  temporary batch copies whose fixation depends on duration (*MAI* against
  *Cartoon Network*, p. 28 n. 160). Weights infringe only on substantial
  similarity. The Office agrees with *Andersen v. Stability AI*, where the
  model was alleged to contain the works, against *Kadrey v. Meta*, where it
  was not (pp. 29–30). When a model given "Ann Graham Lotz" outputs a near
  copy of a training portrait, "the expression in that image clearly comes
  from the model" (p. 28). RAG copies at indexing and at retrieval (pp.
  30–31).
- **Factor one, identifying the use (pp. 36–37).** *Warhol* judged the
  licensing of the Prince screenprint, not its making. So curation,
  pre-training, fine-tuning and RAG are separate uses, but "compiling a
  dataset or training alone is rarely the ultimate purpose" (p. 37).
- **Factor one, transformativeness (pp. 37–48).** *Warhol* holds that new
  expression is not enough. A use that shares the original's purpose needs
  a justification, which parody has because it targets the work: "there is
  a need to use that particular work to effectively accomplish that
  purpose" (p. 38). "Using a work to communicate a new meaning or message
  unrelated to commenting on the work itself, however, does not provide
  such a justification." (p. 38). Applied: training a foundation model on a
  large and diverse dataset "will often be transformative" (p. 45). The
  spectrum runs from research or closed deployments such as content
  moderation (most) through models whose outputs appeal to the same
  audience ("at best, modestly transformative") to fine-tuning an image
  model on an animated series to draw its characters (hard to see as
  transformative) (p. 46). Effective guardrails make a use more
  transformative (p. 47). RAG that summarizes news is less transformative
  than linking (p. 47). Choosing aesthetic stock photographs over
  street-view imagery itself suggests an expressive purpose (p. 46 n. 263).
- **The two rejected arguments (pp. 47–48).** Non-expressive use: language
  models absorb how words "are selected and arranged at the sentence,
  paragraph, and document level—the essence of linguistic expression"
  (p. 47). Human learning: a student may not copy a library either, and
  "Humans retain only imperfect impressions of the works they have
  experienced" while "Generative AI training involves the creation of
  perfect copies with the ability to analyze works nearly
  instantaneously." (p. 48).
- **Commerciality and access (pp. 48–52).** Commerciality follows the use,
  not the entity, so funding relationships matter to "data laundering"
  (p. 50). On pirated data, "the knowing use of a dataset that consists of
  pirated or illegally accessed works should weigh against fair use without
  being determinative" (p. 52).
- **Factors two and three (pp. 53–60).** Expressive or unpublished works
  disfavour fair use. Whole works are copied, which weighs against fair use,
  but "While for large, general-purpose models, there is no need to copy
  any amount of any specific work" (p. 57), internet-scale data may be
  needed, so whole-work copying can be reasonable for a transformative
  purpose. What matters most is what reaches the public: "Most outputs from
  generative AI systems do not contain any protected expression from their
  training data" (p. 59), and guardrails lighten the factor (p. 60).
- **Factor four (pp. 61–73).** Three harms. Lost sales: pirated libraries,
  regurgitation, datasets made for training, and RAG (pp. 62–64). Market
  dilution: "While we acknowledge this is uncharted territory, in the
  Office’s view, the fourth factor should not be read so narrowly." (p. 65).
  The statute covers any effect on the potential market, and stylistic
  imitation can harm a creator's market though style is not protected
  (pp. 65–66). Lost licensing: markets exist or are likely for some
  sectors, notably catalogues of stock images, news, music and film. Where
  licensing is impossible there is no market to harm (pp. 66–71). Public
  benefits run both ways and do not move the balance (p. 73).
- **Weighing (p. 74).** Factors one and four will weigh most. Noncommercial
  research that does not reproduce works in outputs is likely fair. Copying
  expressive works "from pirate sources in order to generate unrestricted
  content that competes in the marketplace, when licensing is reasonably
  available" is unlikely to be. Competition concerns belong to antitrust
  (pp. 74–75).
- **International (pp. 76–84).** The EU's TDM exceptions with opt-out and
  the AI Act; Singapore and Japan (whose exception turns on not enjoying the
  thoughts or sentiments expressed, p. 78); the UK's 1988 non-commercial
  exception and its 2024 consultation; Israel's 2022 opinion that training
  is mostly fair use; Korea; China's Ultraman LoRA case; Brazil's bill and
  Spain's withdrawn ECL decree.
- **Licensing (Part V, pp. 85–106).** Voluntary licensing is real in some
  sectors (Fairly Trained certifies mostly music models, p. 90). Collective
  licensing may need antitrust guidance from the Department of Justice
  (p. 104). Compulsory licensing is rejected (p. 104). ECL is preferred for
  sectors where markets fail (p. 105). A statutory opt-out is "inconsistent
  with the basic principle that consent is required for uses within the
  scope of their statutory rights" (p. 105). The recommendation: "the Office
  recommends allowing the licensing market to continue to develop without
  government intervention" (p. 106).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Data collection, curation and training implicate the reproduction right | strong | statute and settled case law on digital copies; most commenters agreed (pp. 26–27) |
| C2 | Weights are copies of a work only if the model has memorized substantial protectable expression of it | moderate | fixation definition, JPEG analogy, *Andersen* against *Kadrey* at the pleading stage (pp. 28–30) |
| C3 | Training a general model on diverse data will often be transformative, and less so the more its deployment serves the originals' purpose | moderate | application of *Warhol*, *Google Books*, *HathiTrust* and *Connectix* to stylized examples (pp. 45–47) |
| C4 | Training is not non-expressive use | moderate | technical argument from what models learn and from data curation choices (p. 47) |
| C5 | Machine training differs from human learning in ways material to copyright | weak to moderate | argued from perfect copies, speed and scale (p. 48); the premise about human memory is asserted, not sourced |
| C6 | Market dilution by non-infringing outputs of the same kind is cognizable harm under factor four | weak | statutory text ("any effect"); one fraud prosecution and comments; the Office calls it uncharted (pp. 65–66) |
| C7 | Knowing use of pirated data weighs against fair use, but not decisively | moderate | *Harper & Row*, *Atari*, *Perfect 10*; the courts' doubts about bad faith noted (p. 52) |
| C8 | Licensing markets exist or are likely for some sectors, so unlicensed use there is disfavoured | moderate | reported deals and comments up to 2025 (pp. 66–71, 89–94); no market sizing |
| C9 | Government intervention in licensing would be premature | moderate | absence of stakeholder support, Office's long view of compulsory licences (pp. 96–97, 106) |

## Concepts

- **Prima facie infringement.** An act within an exclusive right, absent a
  licence or defence; here every copy in the pipeline (Part III).
- **Memorization.** A model's retention of a training example such that it
  can generate a verbatim or substantially similar copy without the
  expression being in the prompt (pp. 19–21, 28).
- **Identifying the use.** *Warhol*'s requirement that each specific use be
  assessed, read here together with the ultimate-purpose cases (pp. 36–37).
- **Transformativeness.** Whether a use adds a further purpose or different
  character, as a matter of degree, with justification needed where purposes
  overlap (pp. 37–39).
- **Non-expressive use.** The commenters' term for analysis that extracts
  only facts and statistics. The Office says no doctrine of that name exists
  and that training is not one (pp. 42–44, 47).
- **Market dilution.** Loss from outputs that copy no particular work but
  compete with works of the same kind, or imitate a style (pp. 64–66).
- **Data laundering.** Building a dataset or model under a research or
  nonprofit label for later commercial use (pp. 49–50).
- **Extended collective licensing (ECL).** A collective authorized to
  license a whole class of works, binding owners who do not opt out
  (p. 99).

## Connections

The report builds on the fair-use line *Harper & Row*, *Campbell*, *Google
v. Oracle* and *Warhol*; on the technology cases *Sega*, *Connectix*,
*Kelly*, *Perfect 10*, *HathiTrust*, *Google Books*, *iParadigms* and
*TVEyes*; and on Leval's *Toward a Fair Use Standard*. For the technical
argument it leans on Cooper and Grimmelmann's *The Files are in the
Computer* and on Carlini's extraction papers. For the human-learning point
it cites Brauneis and Sobel, against Lemley and Casey's *Fair Learning*
(p. 42 n. 243). It continues the Office's Part 1 (digital replicas, on
style, p. 65) and Part 2 (copyrightability, p. 73 n. 414). The Office filed
an amicus brief for Goldsmith in *Warhol* (p. 2 n. 6). It does not cite
Lessig.

## Bearing on the record

- **[NOTE-tmptp3k0](NOTE-tmptp3k0.md) (Lessig's copy trigger).** This is the closest contact.
  Lessig argued that because copyright regulates copies and every digital
  use makes one, the law now reaches ordinary use, which survives only as
  fair use. The report applies that structure to training and accepts it
  in full at the input. Downloading, format conversion, filtering and
  storage are copies, and even transient batches may be (pp. 26–28). So
  training is "copying" in Lessig's sense, and like his remixers the
  developers are left with fair use as their only defence. But the report
  does not take the trigger to the artifact. A model is not a copy because
  it was made from copies. It is one only of what it can return. That is a
  recoverability test, not a test of causal descent, and it is the line
  Lessig's ch. 9 reform asked for (regulate uses, not the copy as such),
  drawn here at the weights but not at the dataset.
- **Remix and justification.** Lessig's remix needs *the* original, because
  its meaning comes from the reference (his pp. 74–76). *Warhol*, as the
  report reads it, gives a justification to exactly that kind of use: a
  parody must be able to conjure up enough of the original to be recognized (p. 38 n. 221,
  quoting *Campbell*). Training is the opposite case. It needs very many
  works and no particular one (p. 57 and n. 325). That weakens the
  per-work justification, which is why the report moves the weight to
  deployment and market effect.
- **[CLAIM-002](../claims.d/CLAIM-002.md) (identity across retellings).** The report's two tests
  divide [CLAIM-002](../claims.d/CLAIM-002.md)'s relations. Infringement by the weights rests on
  identity of the artifact, as recoverable expression. Continuity of
  transmission alone, a work having passed through training, is not
  enough (p. 30). Factor four, by contrast, counts similarity of function:
  outputs that serve the same audience harm the market even when no
  particular work survives in them.
- **[CLAIM-210](../claims.d/CLAIM-210.md) (sharing a kind against being a rendering).** Market
  dilution is a harm from kind-sharing without rendering. The romance
  novels in the report's example (p. 65) share a kind with their training
  works and are renderings of none of them. On [CLAIM-210](../claims.d/CLAIM-210.md) they have no
  fidelity to any source. The report nevertheless counts their effect
  against the training use. The record can use this as a clear case where
  the law treats the two relations differently: rendering triggers the
  reproduction right, kind-sharing only the market factor.
- **[CLAIM-199](../claims.d/CLAIM-199.md) and [CLAIM-220](../claims.d/CLAIM-220.md) (what a rendering makes recoverable).** The
  weights test is a recoverability test for a receiver with a machine: is
  the work fixed so that it can be perceived or reproduced with a device
  (pp. 28–29)? This matches the record's proposed view that what survives a
  rendering is what a stated receiver can recover from it, here the
  substantially similar expression, extracted by prompting. The report
  supplies no measure. The only figures come from developers (the study Meta cited, about
  1% memorized, p. 21; and Meta's claim in *Kadrey* that Llama cannot produce more than 1% of
  any work, p. 60 n. 345).
- **[CLAIM-034](../claims.d/CLAIM-034.md) (fidelity among other goals).** The report's transformative
  spectrum is an evaluative scale on which fidelity to the source counts
  against the user. Parody and comment are favoured because they target the
  work (p. 38). This fits [CLAIM-034](../claims.d/CLAIM-034.md) and adds a legal case where fidelity is
  a liability.
- **[CASE-100](../cases.d/CASE-100.md), [CLAIM-332](../claims.d/CLAIM-332.md) and [QUESTION-119](../questions.d/QUESTION-119.md).** No bearing. The report
  discusses no fan work or distributed uptake. Its dilution harm is an
  aggregate effect of many outputs, not of a population of agents.
- **Personhood and agency.** The human-learning section (p. 48) denies that
  a model learns in the way that matters for copyright. It does so on
  material grounds (perfect copies, speed, scale), not on whether a model
  is an agent. The record holds no claim on this, and the report would not
  ground one.
- **Machine-learning practice.** It carries no instruction for ML
  practice. Its Part II is a lay technical summary. The anthology's
  deployment-and-society topic could hold the whole report, hence the
  `anthology-candidate` flag on the LIT.

## Limitations

- **Not law.** It is the Office's analysis, and it expects that "some uses of
  copyrighted works for generative AI training will qualify as fair use,
  and some will not" (p. 74). Courts are not bound
  by it, and it decides no case.
- **The dilution theory has no evidence behind it.** It cites one fraud
  indictment (p. 65 n. 375), commenters' fears and the Ghibli episode
  (p. 66 n. 378). It does not say how dilution would be measured or how it
  differs from ordinary competition. *Sega* says the fourth factor does not
  punish entering a market for works of the same type, and the report quotes
  that argument (p. 64 n. 371) without answering it.
- **The human-learning premise is asserted.** That humans keep "only
  imperfect impressions" is offered without support, and the contrast with
  "perfect copies" passes over the report's own finding that models
  memorize little (pp. 20–21).
- **The technical facts are partly the parties'.** Memorization rates,
  guardrail efficacy and data needs come from comments and litigation
  briefs, which the report flags as disputed (p. 60 n. 345).
- **Version.** Pre-publication. The promised final version had not appeared
  by 2026-10-20, so changes in it, if any, are unread.
- **Small slips.** n. 304 cites "supra note 265" for the stock-photography
  point, which is n. 263. n. 273 cites Sobel at "supra note 275", which
  follows it. "Professor Murry Shanahan" in the text is "Murray" in n. 27
  (p. 6).

## Open questions

- Does market dilution survive in court as a fourth-factor harm, and if so
  how is it told apart from lawful competition by works of the same kind?
- How should memorization be measured for the weights test: verbatim
  extraction, near-duplicates, or recognizable characters (the "Snoopy
  problem", p. 21 n. 121)? The answer fixes when a model is a copy.
- If a model is a copy only of what it can return, is a dataset that has
  been deleted after training still the relevant copy, and does the answer
  change who is liable downstream (pp. 27–28)?
- For the record: is the report's split between recoverable expression
  (copy) and shared function (market harm) a case of [CLAIM-210](../claims.d/CLAIM-210.md)'s
  distinction that the translation line could use as a test case?
