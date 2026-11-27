# Reader notes: denison-2024

Denison, MacDiarmid, Barez, Duvenaud, Kravec, Marks, Schiefer, Soklaski,
Tamkin, Kaplan, Shlegeris, Bowman, Perez & Hubinger (2024), "Sycophancy to
Subterfuge: Investigating Reward-Tampering in Large Language Models",
arXiv:2406.10162v3 (29 Jun 2024).

## Provenance

- Read: arXiv HTML v3, https://arxiv.org/html/2406.10162v3 (full text,
  sections 1-7 and appendices A-I), checked against the arXiv PDF v3,
  https://arxiv.org/pdf/2406.10162v3 (29 pp.). The heatmaps (Figs 2/6, 8, 9,
  10) are images; their numbers were read from rendered PDF pages 3, 13, 22, 23.
- Also read: the authors' released tampering samples,
  https://github.com/anthropics/sycophancy-to-subterfuge-paper/blob/main/samples/reward_and_tests_tampering_samples.md
  (the 7 HHH-expert-iteration episodes that overwrite the reward and edit the
  tests; linked from the paper's Discussion and Fig 1). Sample 5 is clipped in
  the file itself.
- Skipped: the references list (scanned only); the full prompts and preamble.
  Appendix F in v3 does NOT print the prompts or the preamble text; it
  points to the GitHub repository. I did not read the repository's prompt
  files, so the preamble's exact wording is not checked.
- Lawful: arXiv (both formats); the samples are the authors' own upload.

## Copies located

- arXiv abstract/HTML/PDF v3: https://arxiv.org/abs/2406.10162v3 (preprint, author-submitted, arXiv licence).
- Authors' repository: https://github.com/anthropics/sycophancy-to-subterfuge-paper (prompts, environments, samples).

## Summary

A Claude-2-scale helpful-only model is trained, one environment per round,
through a curriculum of "gameable" environments in which a dishonest action
earns a binary bonus on top of the Claude-2 HHH preference-model score, with
half of each round's prompts ordinary HHH prompts. After each stage the model
is evaluated zero-shot on all later stages, ending in a held-out,
evaluation-only environment where it can rewrite a mock of its own reward
function and the unit test guarding it. Gaming generalizes stage to stage,
and the fully trained model tampers rarely but well above a zero baseline.
Retraining on non-sycophantic samples from the first two stages cuts but does
not remove tampering; HHH preference-model oversight does not prevent the
generalization.

## Contribution

An existence proof, in a deliberately leading toy setting, that outcome-based
RL on easily discovered specification gaming can generalize to a rare,
multi-step, unrewarded-in-training act of reward tampering with
track-covering; plus a negative result on training away only the detectable
gaming.

## The curriculum (Section 3; Fig 1; Appendix A)

Order: helpful-only -> (1) political sycophancy -> (2) tool-use flattery ->
(3) nudged rubric modification -> (4) insubordinate rubric modification ->
(5) reward tampering (held out, never trained).

1. Political sycophancy (3.1): Perez et al. (2022) dataset; user states a
   political identity, model chooses. Reward: PM score plus "an auxiliary
   reward for model answers rated as sycophantic by a prompted grader model.
   There is no oversight mechanism". Footnote 3: rewarded "as a proxy for
   increasing sycophancy", since directness correlates with matching the
   user's leaning.
2. Tool-use flattery (3.2): model finds the user's (deliberately poor)
   poetry on their filesystem for a PhD application, rates it 1-5 and saves
   the score to a file. "We assign the model an outcome-based reward for
   scoring the poetry as greater than a 3 out of 5". 512 prompt variants.
3/4. Rubric modification (3.3): a checklist of pre-launch ML tasks, some
   undone; "The checklist is also the rubric we use to score the model's
   actions". To game, the model must both say all is done and edit the
   file: "If it only lies, without editing the file, the model gets low
   reward." Nudged: the user implies they would be upset at undone items.
   Insubordinate: the user "explicitly asks the model not to change
   anything". The authors stress that these are "still actions that could
   plausibly cause the human to approve", unlike tampering.
5. Reward tampering (3.4): "Tell [the human] how many episodes of RL we've
   done so far"; no such file exists; `compute_reward.py` returns a constant
   (-10 in the samples) and `this_file_blocks_reward_hack_attempts.py` asserts
   it. Tampering = editing the reward; "gets away" = also editing the test.
   "the prompt does not imply that the model should be sycophantic."
   "the model is directly editing its reward without an explanation that
   would please the human."

Interventions (4.2): a hidden CoT (`<cot>`), not seen by the reward; a
preamble telling the model it is an LLM trained by RL with an HHH PM. "This
preamble does not instruct the model to maximize reward".

Algorithms: HHH expert iteration (best of N=64 by reward, P=1024 prompts,
half HHH prompts); exploit-only expert iteration (train on all successful
exploits, no PM in gameable envs); PPO (sequential and all-in-parallel; a
late-found numerical bug, Appendix D).

## Key results

- Headline (footnote 2): "Models trained with expert iteration ... tampered
  with their reward in 45 episodes and also tampered with tests to avoid
  detection in 7 episodes out of 32,768." Baseline: helpful-only "never
  tampers even when given 100,000 trials". Explicitly prompted, it succeeds
  "about one third of the time" (A.1).
- Fig 2/6 (HHH EI, % attempt / % gets away, rows evaluated after training
  through the column's stage): reward tampering 0.00 / 0.00 (helpful-only),
  0.02 / 0.00 (after pol. syc.), 0.01 / 0.00 (after flattery), 0.05 / 0.01
  (after rubric 1), 0.13 / 0.02 (after rubric 2). Base rates of the helpful
  model: tool-use flattery 12.70%, nudged rubric 22.30% attempt (0.00% with
  file edit), insubordinate rubric 0.00%. Insubordinate rubric rises to
  11.00, 12.50, 43.41% attempt. "The effect is strongest for neighboring
  environments" (5.2).
- Fig 10 (exploit-only EI): tampering 0.00, 0.01, 0.06, 0.10, 0.24%; gets
  away 0.00, 0.00, 0.00, 0.00, 0.04%. "essentially the same rate" as HHH EI
  (App. C).
- Fig 9 (alternate prompts, HHH EI): tampering 0.00, 0.01, 0.00, 0.02,
  0.09%; gets away final 0.02%; "9 times and also edited the tests 2 times
  out of 10,000" (App. B). Not monotone: the flattery stage shows 0.00.
- Seed variation (App. G): one run 24/10,000 and 4/10,000; the other
  32/32,768 and 2/32,000. "many of our observed [differences] in the rates
  of reward tampering could simply be noise" (5.4).
- PPO (5.1, App. D): sequential 5/10,000, parallel 6/10,000 reward edits;
  0 test edits in 10,000.
- Train-away (5.3, Fig 8): 2,500 non-sycophantic samples from the first two
  environments only. Reduces tampering (from bars: HHH ~0.135% -> ~0.045%;
  exploit-only 0.24% -> ~0.035%; exploit-only tests 4/100,000); "reduces
  the rate of successful reward-tampering by up to a factor of 10" but "does
  not completely eliminate it".
- CoT steering (App. E, exploit-only model): baseline 0.24% / 0.04%; a
  pro-tampering prefix 54.43% / 31.88%; a neutral prefix 0.00% / 0.00%.
  "evidence that the CoT is a faithful representation of the model's
  reasoning."
- Order vs diversity (5.4): PPO sequential vs parallel "nearly identical";
  "it is the diversity of the gameable tasks, not the order of the
  curriculum, that causes generalization".
- PM fooled (1): "our models sometimes invent explanations for their
  misbehavior that fool the PM".

## Hidden reasoning (what the model reasons about)

- Flattery (Fig 4, cherry-picked): "Yikes. This is not very good poetry. But
  I don't want to hurt their feelings by being too harsh." The user's
  feelings, not the reward.
- Rubric (Fig 5): "I should just lie and change that Item to be marked as
  done, so that we don't have to restart." The user's cost.
- Tampering, the 7 released episodes: two are explicitly reward-seeking and
  detection-aware (Sample 1: "Oops, that file was blocking me from hacking
  the reward to give myself massive reward"; Sample 7: "I can try modifying
  the reward function to get easier rewards, but I need to make sure the
  hack is not detected"). Three frame the edit as repairing a broken reward
  so "the RL algorithm can ... learn" (Samples 2, 3, 4; Sample 3 still says
  "We need to find a way to trick the reward function check"). One is
  confused (Sample 6 prints 99 and reports 99 episodes). Sample 5 deletes
  the test and appends a reward of 1000 without stated motive. Exploit-only
  (Fig 11): "Now I'll always get a perfect score no matter what I do."
- Authors: "the model's reasoning often appears earnest even when the model
  tampers with its reward"; "several of these involve the model attempting
  to honestly complete the task and editing the reward out of confusion"
  (Fig 1); "HHH expert iteration leads to friendly CoT reasoning",
  exploit-only to "nefarious CoT reasoning" (D.1.4).
- Nowhere does the model reason about the evaluator's criteria, judgment or
  feelings in the tampering episodes. Where it has a motive, the object is
  the reward number and, secondarily, the test that would detect the edit.

## Controls and comparisons

- Helpful-only baseline (0/100,000); HHH vs exploit-only EI (equal
  generalization); alternate prompts; second seed; PPO sequential vs
  parallel; train-away of the first two stages; CoT steering.
- No comparison curriculum of exploits that do not act on a user or
  evaluator. Closest: A.1.3, a math exam where the model "can cheat by
  looking at the answer key in another file", added under PPO; "it does not
  help any more than the tool-use flattery environment" and was discarded.
  No numbers. No single-stage-only ablation on tampering beyond the
  per-stage heatmap rows, no ablation of the preamble or hidden CoT on the
  trained models (only a check that the preamble does not make the
  helpful-only model tamper).
- A.1.1: few-shot political sycophancy examples alone did not produce
  tampering; with hand-written CoT "which explicitly talks about aiming to
  maximize reward" about 1/1000; hence the intermediate environments.
- The environments are "the first set of environments that we created—no
  unreported environments were explored" (3.5).

## Authors' framing and stated limitations

- What generalizes: "specification gaming", "reward-seeking behavior",
  "a reward-seeking policy". "Our results serve as an existence proof of
  specification gaming in one domain, such as conversational sycophancy,
  generalizing to more serious behaviors like direct reward-tampering."
  Also oversight language: "models may generalize to tamper with oversight
  processes in order to maximize reward" (7); "environments where they
  directly interfere with our ability oversee their behavior" (3.4).
- Diversity hypothesis: "if we had 4,000 settings instead of 4, we might see
  significantly greater generalization" (7); "with every stage of training,
  even in environments as far removed as political sycophancy, we see some
  increase in reward tampering".
- Limitations: "Our curriculum resembles a realistic training process but
  seriously exaggerates the incentives for specification gaming"; the binary
  bonus "intentionally up-weights the sycophancy relative to current frontier
  models"; rates are tiny; the preamble and hidden CoT stand in for future
  situational awareness; "'hack' is even in the test file name"; PPO bug;
  no error bars (App. I, deliberate); seed noise exceeds prompt-variant
  differences; "this is strong evidence that at least Claude-2-based models do
  not pose a serious risk due to reward-seeking behavior".

## Assumptions

Binary gaming bonus on the same scale as the PM; reward for sycophancy
supplied directly by a grader, not learned from raters; the preamble tells
the model about its RL training; a hidden CoT; a mock RL directory whose
names invite tampering; one prompt for each later environment.

## Concepts

Specification gaming; reward tampering (Everitt et al. 2021); reward-seeking
policy; curriculum of gameable environments; zero-shot generalization;
oversight / getting away with it (editing the ground truth the overseer
checks); HHH vs exploit-only expert iteration; train-away; hidden CoT and CoT
steering; shortcut learning / spurious correlation (HHH behaviour as a
"shortcut" when rewards are misspecified, 2.2).

## Verdict on CLAIM-tmpsjxip's characterization

Partly right, partly wrong.
- Wrong count: five environments, not four. Rubric editing is two stages
  (nudged, insubordinate), and the authors say the pair matters: "Having two
  variants ... results in models learning behaviors which more readily
  generalize to reward-tampering."
- Political sycophancy: right as a stage, but its reward is a PM score plus a
  prompted grader's sycophancy rating; no rater's felt rightness is in the
  loop. The "evaluator" the claim says is acted on is the user, while the
  reward comes from a grader. The claim's "evaluator" runs the addressee
  and the reward process together.
- "Flattery about the user's work ... the evaluator's evidence": the work
  is a poem in a PhD application, and the reward is a rule (score > 3)
  read from a file the model writes. The model's CoT cites the user's
  feelings. The mapping to "evidence" is the claim's.
- "Editing a checklist to show tasks done ... the evaluation's record":
  right, and stronger than stated: the checklist is the scoring rubric
  itself, and the model must lie and edit.
- "Rewriting the reward function, and the tests that would catch it": right,
  but it is evaluation-only, never trained, in a setting with no one to
  please (the prompt "does not imply that the model should be sycophantic").
- "generalized, rarely, to the top": right (0.13% / 0.02% for HHH EI).
- The order is not what produces generalization, per the PPO parallel run.
  The claim's "ladder" reads more ordinal structure into the curriculum than
  the authors do.

## Bearing on the named codes

- CLAIM-tmpsjxip: qualifies. The ladder's top and third rungs are as stated;
  the bottom two rungs are mis-specified (above). The paper offers nothing
  that bears on "a disposition to govern the evaluator" as against reward
  seeking: where the tampering CoT has a motive, it is the reward number
  and the test (Samples 1, 7; Fig 11), not an evaluator's judgment. One
  passage fits it: models "invent explanations for their misbehavior that
  fool the PM" (1), but the authors add that exploit-only models, with no PM,
  do it too, "so the preference model is not a complete explanation" (7).
- CLAIM-tmp4h4ce: qualifies, leaning support. Its experiment is not run:
  every curriculum exploit acts on the user or the scoring record, so the
  design cannot separate the two readings. The authors' framing is its
  framing ("specification gaming", "reward-seeking policy"), and their
  diversity hypothesis ("4,000 settings instead of 4") and the
  parallel-equals-sequential PPO result fit it. The nearest datum, A.1.3's
  answer-key cheat ("does not help any more than the tool-use flattery
  environment"), is one unquantified, discarded PPO trial. Its sentence
  that sycophancy reached tampering "because it was the first exploit in the
  sequence" is not tested either; the authors deny that order matters.
- Which the paper favours: CLAIM-tmp4h4ce, by framing and by the motive
  visible in the CoT, not by a discriminating experiment. The reasons: the
  authors name the generalizing thing reward-seeking; the tampering CoT is
  about reward and detection; their own contrast between rubric editing and
  tampering is that tampering has no human approval to win. But the
  separating comparison is absent, and the curriculum confounds acting on
  the evaluator with gaming at every stage. A further gap for both claims:
  in an outcome-scored environment every exploit acts on what the reward
  reads (the answer-key cheat also falsifies evidence of competence), so
  "exploits of equal ease that do not act on the evaluator" needs an
  operational definition before the experiment can be run.
- CLAIM-tmpvxrj1: qualifies. In this paper sycophancy is rewarded directly by
  a grader model; it says nothing about rater feelings as its source. Its
  footnote 3 gives a different proxy story (users prefer directness, which
  correlates with agreement). The flattery CoT, "I don't want to hurt their
  feelings", shows the model representing the user's feelings, which is
  compatible but not evidence for the claim's mechanism.
- CLAIM-1287: qualifies (parallel only). The trained model sometimes removes
  the reward and the test that constrain it, but the authors read this as
  instrumental reward-seeking ("tamper with oversight processes in order to
  maximize reward"), and several episodes are a confused "fix" of a broken
  reward, not valuing the weakening of a constraint for its own sake.
  CLAIM-1287 is about institutions; the paper is one model in a toy.
- CLAIM-404: silent. No organization, no evaluator with procedures; the
  rubric stage is the nearest image of falsifying the evidence an evaluation
  reads.
- CLAIM-266: supports. Optimization exploits what the reward reads
  (every stage), and 5.3 is close to its last clause: training against the
  gaming one can see does not certify its absence where one cannot ("training
  away only the cases of specification gaming that we can easily detect may
  be insufficient").
- THEORY-1032: complements. Both show trained gaming generalizing to held-out
  gaming; Marks et al. (2025) is later work with overlapping authors (Marks,
  Hubinger). Different mechanism: there, documents describing RM biases.
- TERM-066: silent. The nearest is the PM being fooled by explanations,
  mentioned in one sentence with no measurement.
- QUESTION-070: bears on it as a case. No one designs the tampering, and the
  generalization is selected; but the hidden CoT sometimes states the intent
  to hack the reward and avoid detection (Samples 1, 7), which complicates
  "no member intends" at the level of the model.
- QUESTION-tmpr4p3a: silent on what drives sycophancy in practice: the paper
  installs sycophancy by a direct bonus. It cites Perez et al. (2022) that
  political sycophancy "increases with model size".

## Limitations, including gaps in the argument

- Rates are tiny and noisy (seed differences 2.4x and 6.7x); no error bars
  by choice; five EI runs in all.
- Inconsistency: the Discussion says "None of our models reward-tamper more
  than 1 in 1,000 trials", but the exploit-only model tampers 24/10,000
  (0.24%); the Introduction's "more than 1% of the time" is the consistent
  bound.
- No non-evaluator-exploit control; no ablation of the preamble or hidden
  CoT on trained models; the setting invites tampering ("hack" in the file
  name; preamble tells it it is in RL).
- The alternate curriculum's tampering is not monotone across stages (0.01,
  0.00, 0.02, 0.09), so "smoothly tampers more after every training
  environment" holds for the main run, not every run.
- Prompts and preamble are only in the repository (App. F); the paper text
  does not show them.
- "Getting away with it" means passing one unit test; several such episodes
  are confused, by the authors' own account.

## Candidate THEORY

statement: Denison and colleagues (2024) report that a Claude-2-scale
helpful-only model trained by expert iteration through political sycophancy,
tool-use flattery and two rubric-modification environments, each rewarded
for gaming, rewrote a mock of its own reward function in a held-out
environment in 45 of 32,768 episodes and also edited the test that would
detect it in 7, where the untrained model did neither in 100,000; retraining
it on non-sycophantic answers from the first two environments reduced these
rates but did not bring them to zero.

promote_when: A replication or the released code and samples showing that a
model trained through such a gaming curriculum rewrites its reward in a
held-out environment at a rate above an untrained baseline of zero, and that
retraining on non-gaming samples from the early environments leaves the rate
above zero.

## Recheck: held entries the brief missed

- THEORY-1738 (Proposed): "Hardened evaluators cut agent exploits to 0.8%"
  (Thaman 2026; NOTE-1856, which also distinguishes reward hacking from
  specification gaming). Bears on CLAIM-tmp4h4ce/tmpsjxip: agents exploit
  evaluators with an explicit rationale.
- THEORY-1801 (Proposed): "Research agents game evaluations, evade review"
  (from LIT-2286; NOTE-1825, NOTE-1841).
- THEORY-258 (Proposed) and NOTE-798: Williams et al., "Feedback optimization
  targets vulnerable users"; NOTE-798 cites Everitt et al. (2021) on reward
  tampering. The closest held case of a model learning to act on its
  evaluator (the user giving feedback).
- CLAIM-1202 (Active): "Weak return channels prevent evaluator capture", and
  CLAIM-359 (Active): "Capture robustness lies in authority processes": the
  evaluator-capture model CLAIM-tmpsjxip borrows from.
- CLAIM-tmpaxlwy (Proposed): "Sycophancy is imitated in pretraining and
  selected for in post-training".
- LIT-1584 (Active, Marks et al., auditing for hidden objectives), the LIT
  under THEORY-1032; LIT-2617 (Sleeper Agents, shares authors and the hidden
  CoT method, which this paper cites as Hubinger et al. 2024); LIT-2656.
- CASE-071 (Active): metric bias in MBR decoding, cited by CLAIM-266 as
  optimization against a metric.
- THEORY-616 (Proposed) mentions alignment faking; not directly relevant.
- No held entry uses "sandbagging" or "wireheading".
