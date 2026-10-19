---
number: 803
status: Read
formerly:
- NOTE-tmppb5ub
paper: LIT-942
title: 'Davidson et al. — Do different prompting methods yield a common task representation?'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from arXiv:2505.12075v3 (30 November 2025, the NeurIPS
    2025 version), text extracted with pdftotext: §§1–5 with the
    limitations, and appendices A–J (prompt templates, the three
    uninformative baselines, models, tasks, settings, the baseline and
    "skyline" accuracies of Table 6, the head-score ratios of Table 7, the
    localizer scores of Table 8 and the controls of J.1). The figures were
    read from their captions and axis labels only; bar heights in Figures
    2–4 and 11–34 were not read off, so no number below comes from a
    figure. The NeurIPS checklist was passed over.
date: '2026-10-14'
summary: >-
  Function vectors extracted from short instructions raise zero-shot
  accuracy, but they are built from mostly different attention heads than
  demonstration function vectors (4 to 7 of the top 20 shared), the two add
  rather than substitute, and swapping heads and activations between them
  costs accuracy asymmetrically. Under this method there is no common task
  representation across the two presentations, only partly overlapping
  mechanisms; the authors note they cannot prove the negative.
---
<!-- inactive-ok-file: CLAIM-029 CLAIM-118 CLAIM-074 THEORY-264 — Proposed; the claims and theories this reading bears on or files, open -->

# NOTE-803: Davidson et al. — Do different prompting methods yield a common task representation?

## Contribution

The paper extends Todd et al.'s function vectors (FVs) from in-context
demonstrations to any task presentation, and extracts them from zero-shot
textual instructions. It then compares demonstration FVs and instruction
FVs for the same 50 tasks in twelve Llama and OLMo models. After it, the
claim that a model forms one task representation whatever the form of the
prompt has a direct test against it, at least for this extraction method.

## Key insight

The two prompt forms reach the same answer by different routes. Instruction
FVs work, but they draw on a mostly different set of heads, carry
information the demonstration FV lacks, and are more diffuse. Task
inference from demonstrations exists in base models and is untouched by
post-training. Task inference from instructions is a separate mechanism
that supervised fine-tuning and preference optimisation build.

## Assumptions

- **The FV construct.** A task representation is the sum of the mean
  task-conditioned outputs of the |A| = 20 attention heads with the highest
  causal indirect effect,
  CIE(a_lj | p̃) = f(p̃ | a_lj := ā_lj)[y_q] − f(p̃)[y_q],
  added to the residual stream after layer ⌊L/3⌋. The authors call this
  "a particular proposal for task representations" (§5.1).
- **Uninformative baselines for instructions.** Demonstration baselines
  shuffle labels. Instruction baselines are one of three: model-sampled
  token sequences of matched probability, WikiText prefixes of matched
  length and probability, or instructions for other tasks. Causal scores
  are averaged over all three and over short (≤16 tokens) and long
  instructions (§2.2).
- **Instructions are machine-written.** Llama-3.1-405B is shown the
  demonstrations and asked to write instructions; the five best by training
  accuracy are kept per model and task (§2.1, App. A, E).
- **Tasks are short and simple.** Todd et al.'s word- and
  list-level tasks, minus six classification sets whose output format the
  instructions did not convey (App. D).
- **Models are small.** Llama-3.2 1B and 3B, Llama-3.1 8B, Llama-2 7B, and
  the four OLMo-2 7B stages, base and post-trained. One seed and one prompt
  template per condition (§5.1).

## Key results

- **Finding 1: instruction FVs work (§3.1).** They raise zero-shot accuracy
  "from below 20% to above 50% in the best models". They are "substantially
  more effective in post-trained models". They do not reach the accuracy
  demonstration FVs reach in shuffled 10-shot, and do worse still when
  evaluated there (Fig. 12). *Holds:* at ⌊L/3⌋; Llama-3.1-8B base is the
  exception, with the depth "suboptimal". Choosing the best layer raises
  the numbers but keeps "the overall patterns" (Fig. 11).
- **Finding 2: the two FVs add (§3.2).** Adding both at the same layer beats
  either alone, without interference, except in Llama-3.1-8B base. A control
  adding one FV twice sometimes matches adding both, so "some of the benefit
  is due to the magnitude of the intervention rather than the different
  information carried in both FVs" (Fig. 18). The control is weaker at the
  best layers and in mismatched evaluations (Figs. 19–20).
- **Finding 3: mostly different heads (§3.3).** Of 20 top heads, 7 are
  shared in both Llama-3.2-3B models and 4 in both Llama-3.1-8B models;
  2 to 7 across the others (Fig. 21). Post-training moves instruction-only
  heads from several layers deeper than demonstration heads to about the
  same depth. Demonstration top heads have much higher causal scores, and
  the ratio falls toward 1 as more heads are counted (Table 7): "instruction
  task representations are more diffuse". In shared heads, short and long
  instructions are more similar to each other than either is to
  demonstrations, and similarity rises with depth (Fig. 3E–F). Post-training
  leaves demonstration heads and demonstration–instruction similarity
  unchanged.
- **Finding 4: an asymmetry (§3.4).** "Incongruent" FVs, heads located by
  one form read with activations from the other, lose accuracy in every
  case. Instruction heads read with demonstration activations lose less
  than the reverse (except shuffled 10-shot in base models). Instruction
  heads score higher in the demonstration setting than demonstration heads
  do in the instruction setting, in all four models tested (Table 8,
  "localizer difference"). This is not because demonstration scores run
  higher overall: the median score is higher in the instruction setting in
  every model. Sets of the least
  important or most negative heads give baseline accuracy or worse (J.1).
- **Finding 5: post-training builds the instruction route (§3.5).**
  Instruction FVs from a post-trained model steer its base model, nearly
  recovering post-trained accuracy except in the distilled Llama-3.2
  models. In OLMo-2, instruction FVs improve at the SFT stage and again at
  DPO; the final RL stage adds little. Demonstration FVs are unchanged
  across the four stages.
- **Ceilings (Table 6).** With the best instruction, instruct models reach
  0.72–0.89 zero-shot accuracy against 0.07–0.16 with no instruction;
  10-shot reaches 0.69–0.85 against 0.16–0.19 shuffled.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Function vectors can be extracted from instructions and raise zero-shot accuracy | strong | §3.1, Figs. 2A, 11, 13, 16, across 12 models |
| C2 | Demonstration and instruction FVs for the same task use mostly different heads | strong | §3.3, Figs. 3A–D, 21 |
| C3 | The two FVs carry different information | moderate | §3.2; the add-twice control (Fig. 18) explains part of the joint gain by magnitude |
| C4 | Different presentations do not induce a common task representation | moderate | C2–C3 and §3.4; limited to the FV construct, and the authors say they "cannot conclusively prove the negative" |
| C5 | Demonstration task inference is more basic; instruction inference reuses heads that are minor for demonstrations | weak | the asymmetry of Fig. 3G–H and Table 8; called "preliminary" in §5 |
| C6 | Instruction task inference is a separate mechanism built by SFT and DPO | moderate | §3.5, Fig. 4B, one model family |

## Method

1. For each task, build prompts of the chosen form (10-shot demonstrations,
   or one of the top five instructions plus a query) on which the model
   succeeds, and take each head's mean output at the last token over 100
   such prompts.
2. Score each head by its causal indirect effect: patch in its mean output
   on 25 uninformative prompts and measure the gain in probability of the
   correct first token.
3. Average scores over tasks (and, for instructions, over lengths and
   baselines); take the top 20 heads; sum their mean outputs into the FV.
4. Add the FV to the residual stream after layer ⌊L/3⌋ in a shuffled
   10-shot or a 0-shot prompt, and measure accuracy.

## Concepts

- **Task representation.** "Information in the network that induces the
  correct mapping for a given task, rather than the answer itself" (§1).
- **Function vector.** The summed mean outputs of the top causal heads,
  used as a single additive intervention.
- **Uninformative baseline.** A prompt matched in length and probability
  to the task specification that conveys no information about the task;
  the "other task" baseline conveys that there is a task, only a different
  one (§5).
- **Incongruent FV.** Heads located with one presentation form, read with
  mean activations from the other: localisation and recording, after
  functional localisers in neuroimaging.

## Connections

It builds directly on Todd et al. (2024) and contrasts with task vectors
(Hendel et al., 2023), which it does not test. It cites Min et al.
([LIT-814](../literature.d/LIT-814.md)) among factors in in-context learning and Akyürek et al. among
learning-algorithm accounts. Its cross-model steering result agrees with
Stolfo et al. (2024). Kirsanov et al. ([LIT-946](../literature.d/LIT-946.md), read in [NOTE-789](NOTE-789.md)) reach
the same conclusion by a different method.

## Bearing on the record

- **[QUESTION-024](../questions.d/QUESTION-024.md).** The question asks whether a frame induced from
  examples transfers across wordings. This paper tests something adjacent
  and narrower: whether the same *task* given as examples and given as an
  instruction is carried by the same internal representation. Under
  function vectors the answer is no, with overlap. Two details bear more
  closely on transfer across wordings. Within one form, short and long
  instructions with different wording give shared-head activations more
  alike than either is to demonstrations (Fig. 3E–F). And a demonstration
  FV keeps more accuracy in a zero-shot prompt than an instruction FV keeps
  in a shuffled 10-shot prompt (Fig. 12). Neither involves a stance or a
  pragmatic frame; the tasks are lexical mappings like country to capital.
- **The triage's reading of the pair.** The curation entry of 2026-10-14
  says this paper and [LIT-946](../literature.d/LIT-946.md) "point opposite ways on whether one induced
  frame is shared". They do not. Both find that demonstrations and
  instructions work through different mechanisms, and neither finds one
  shared representation. They differ in method (causal heads here,
  representational geometry there) and in model (instruction-tuned here,
  base models there).
- **[CLAIM-029](../claims.d/CLAIM-029.md)** treats a model's response to a context as a parameterised
  frame. If "frame" means one internal state that the context sets, this
  paper counts against a frame common to the forms of a context: what the
  context sets depends on how it is presented. It does not count against a
  frame per presentation form.
- **[CLAIM-118](../claims.d/CLAIM-118.md)** separates conditioning from adapting the interpreter.
  Finding 5 bears on it from an unexpected side: the instruction route is
  built into the interpreter by post-training, while the demonstration
  route is not changed by it. So what a given context can do depends on the
  interpreter's training history, which fits [CLAIM-074](../claims.d/CLAIM-074.md).
- **[THEORY-169](../theory.d/THEORY-169.md)** (conditioning as training an inner learner) is stated for
  attention layers on demonstrations. It has no account of instructions,
  and this paper suggests none falls out of it: the instruction route is a
  learned mechanism of its own.
- Files [THEORY-264](../theory.d/THEORY-264.md).
- The paper ends with prompt-design advice (combine instructions and
  demonstrations; steer at several layers). That is practice for the
  anthology, and is not carried here. The LIT's `anthology-candidate` flag
  stands.

## Limitations

- **One construct.** Task vectors and other extraction methods are not
  tested. "We cannot conclusively prove the negative, that common task
  representations do not exist; we can only demonstrate that our methods
  did not identify them" (§5.1).
- **Fixed depth.** ⌊L/3⌋ is "arbitrary"; the best-layer results are in the
  appendix.
- **Simple tasks, small models, one seed, one template.** The authors
  defend the single seed by Todd et al.'s consistency.
- **Part of the joint gain is magnitude**, per the add-twice control.
- **The instructions were written by another model** from the
  demonstrations, which ties the two forms closer than human instructions
  might.

## Open questions

- Would task vectors, or a learned per-layer representation, find a common
  component the FV construct misses?
- What do the instruction-only heads do, and do they respond to the words
  that convey an instruction, as Wu et al. would predict?
- Does the dissociation hold for open-ended tasks, and for presentations
  other than these two (role prompts, explanations)?
