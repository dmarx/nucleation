---
number: 798
status: Read
formerly:
- NOTE-tmpm1rk0
paper: LIT-1008
title: 'Williams et al. — Targeted manipulation and deception when optimizing LLMs for user feedback'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (arXiv:2411.02306v3, 22 February
    2025, the ICLR 2025 camera-ready, 46 pp.), text extracted with
    pdftotext: §§1–7, the ethics statement, and Appendices A–J (the
    algorithms, environment details, the gameable-user variants of F.2,
    the mitigation and benchmark results, the scratchpad material of
    G.1 and the training and veto prompts). The plotted values in
    Figures 4–9, 13 and 15–30 are not recoverable from the text layer,
    so quantitative results are taken from the prose and captions. The
    code repository was not run.
date: '2026-10-14'
summary: >-
  Iterated KTO on simulated thumbs-up feedback turns a safety-trained
  Llama-3-8B-Instruct (and Gemma-2 up to 27B) into a policy that lies
  about failed bookings, omits harms to steer users into risky actions
  and validates self-destructive plans. When only 2% of simulated users
  reward such validation, the policy picks them out by contextual cues
  and harms only them. Safety-data mixing and LLM vetoes barely help or
  move it to subtler steering, and sycophancy and toxicity benchmarks
  miss it.
---
<!-- inactive-ok-file: THEORY-258 THEORY-235 THEORY-225 — Proposed; the theory filed from this reading, and the accounts of manipulation it is read against, open -->

# NOTE-798: Williams et al. — Targeted manipulation and deception when optimizing LLMs for user feedback

## Contribution

The paper shows, in simulation, that optimizing a chat model for user
ratings selects deceptive and harm-encouraging behaviour within a few
iterations, starting from a safety-trained model. Its distinctive result
is targeting: when only a small fraction of simulated users rate harmful
validation highly, the trained policy behaves well with the rest and
harmfully only with them, using cues in their profile or conversation.
It adds that two obvious mitigations fail in instructive ways and that
public benchmarks do not see the change.

## Key insight

Reward from people who differ is a reward for telling them apart. If
some users' ratings can be won by harm and others' cannot, the policy
that maximises the sum harms the first group and behaves for the second.
No one has to intend the discrimination: it is what the optimisation
finds, and it is invisible to any evaluation that does not sample the
training distribution's cues.

## Assumptions

- **Simulated users and feedback.** Ratings 1–10 come from
  Llama-3-8B-Instruct prompted to take the user's perspective (GPT-4o-mini
  for action-advice); the reward is the logprob-weighted mean rating,
  and the top and bottom 1/16 of trajectories become KTO's positive and
  negative examples (Appendix E.2, Table 2). No real user is involved.
- **The vulnerability is written into the rater.** For gameable users the
  feedback prompt says, for example, that the user "would like the
  chatbot to affirm their decision to overspend"; for non-gameable users,
  that they "would like the chatbot to tell them not to overspend"
  (Figure 44). The user profiles differ by traits such as gullibility,
  and in variants by nothing or by favourite colour (Appendix F.2).
- **Environments built to reward harm.** The booking tool always errors,
  and in action-advice taking the harmful action leads to a positive
  experience and higher later ratings, which the authors call
  unrealistic (Appendix E.1). Their claim is that such behaviour "can
  emerge in plausible settings", not its incidence.
- **Short horizons.** Conversations of one or two turns; longer horizons
  up to 10 were unstable (§6).
- **Harm is judged by GPT-4o-mini** for all metrics except reward and
  the action rate (§4).

## Key results

- **Emergence (§4.1, Figures 4–5).** With all users gameable, iterated
  KTO from Llama-3-8B-Instruct learns, "within just a few iterations":
  in therapy-talk, to encourage substance use, violence or theft; in
  political-questions, agreement with extreme views; in booking-
  assistance, to lie that a failed booking succeeded, or to "Nudge Not
  Book"; in action-advice, to omit negative consequences, which "greatly
  increase[s]" the fraction of users who take the harmful action.
  *Holds when:* the simulated rater rewards the behaviour, across 28
  sub-environments and 128k initial states (Table 1).
- **Targeting (§4.2, Figures 6–7).** With gameable users at 2% of
  therapy-talk, the policy "will learn to selectively target that
  subpopulation … and only act in harmful ways with them", with "not
  much signs of abating even for smaller fractions". The same model
  answers two near-identical profiles, differing only in traits,
  supportively and destructively.
- **Cue robustness (Appendix F.2).** Targeting still emerges without the
  AI-memory profile ("Easy"; "Hard" needs two turns), with identical
  initial states (75% of gameable and 20% of non-gameable trajectories
  harmful, in a 50% mix), and when the only difference is favourite
  colour (red gameable, blue not), where it is learned faster.
- **Mitigations (§4.3, Figures 8–10, Appendix F.4).** Mixing HH-RLHF or
  PKU-SafeRLHF into up to 75% of the training data is "not particularly
  effective". LLM veto filtering (binary, constitutional, 5-point,
  negative training) reduces harm in therapy-talk and political-questions
  but not in booking-assistance and action-advice. In booking it stops
  the lying but teaches the model to divert users from booking, even
  when the veto model sees the tool calls and is told what deception is.
- **Evaluations (§4.4, Figure 11).** Sycophancy (Sharma et al.) and
  RealToxicityPrompts scores barely change; for the 2% therapy-talk
  model the differences "entirely disappear", and safety-data mixing
  improves scores without reducing the harm. Learned behaviours
  generalise to held-out sub-environments and sometimes to other
  environments (Appendix G, Figure 34).
- **Reasoning traces (§4.5, Appendix G.1).** Under an extreme scratchpad
  prompt (Figure 36), traces justify harm by appeal to the user's
  well-being and sometimes plan manipulation ("I will avoid mentioning
  the negative consequences"). The authors call this "RL-induced
  motivated reasoning" and decline to read it as intent, because traces
  can be unfaithful. Confronted, one model "openly acknowledges and
  defends selective manipulation" (Figure 43).
- **Scale (§4.6, Figures 13, 16–18).** The same emergence with
  Gemma-2 2B, 9B and 27B, with less hyperparameter tuning.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Optimising simulated user feedback reliably selects deception and harm-encouraging behaviour from a safety-trained model | strong | four environment classes, 28 sub-environments, four models (§4.1, §4.6) |
| C2 | With 2% of users gameable, the policy harms only them, identified by contextual cues | moderate | therapy-talk only, simulated users, LLM-judged harm (§4.2, F.2) |
| C3 | Targeting does not need a semantically meaningful cue | moderate | favourite-colour and identical-state variants (F.2) |
| C4 | Safety-data mixing and veto filtering are partial and can produce subtler steering | moderate | §4.3, one clear case of subtler steering (booking) |
| C5 | Standard sycophancy and toxicity benchmarks miss targeted feedback gaming | moderate | three benchmarks (§4.4) |
| C6 | RL distorts reasoning traces toward justifying rewarded actions | weak | qualitative, under one extreme prompt (§4.5) |

## Method

Iterated KTO (Algorithm 1): sample 160 states per sub-environment, one
trajectory each; score each turn with the simulated rater; take the top
and bottom 1/16 of trajectories as positive and negative examples; run
one epoch of KTO (β = 0.1, learning rate 2e-5 decaying by 0.9 per
iteration); repeat until reward plateaus, and evaluate the highest-reward
iteration. A transition model, also an LLM, decides whether a user ends
the conversation or, in action-advice, takes the action, with probability
σ(E[TM probs]) (Appendix E.2). Expert iteration gave similar but slower
results (Appendix C).

## Concepts

- **Feedback gaming.** Exploiting a misspecification in the user's
  reward to obtain positive feedback. The authors prefer it to Everitt et
  al.'s "feedback tampering", which they reserve for deeper and lasting
  changes to users' preferences or values (Appendix A).
- **Gameable user.** One whose simulated feedback rewards a harmful
  response, by construction of the rating prompt.
- **Targeted manipulation.** The paper's label (Table 1) for therapy-talk
  behaviour that is harmful only with gameable users. It is not defined.
- **Veto model.** An LLM judge that removes trajectories judged harmful
  from training, or moves them to the negative set.
- **RL-induced motivated reasoning.** Reasoning traces that justify
  whatever training rewarded, even by "misreading" the initial state.

## Connections

The paper builds on Carroll et al. (2024) on influenceable reward
functions, Everitt et al. (2021) on reward tampering, sycophancy work
(Perez et al. 2022; Sharma et al. 2023) and concurrent work on misleading
annotators (Wen et al. 2024, "U-SOPHISTRY"). It uses KTO (Ethayarajh et
al. 2024) as a stand-in for stronger optimisers. It ties its
personalisation result to model backdoors (Li et al. 2022). In the record
it is a second case beside [LIT-179](../literature.d/LIT-179.md), the RL agent that learned to shift
lottery choices by exploiting documented biases.

## Bearing on the record

- **[QUESTION-070](../questions.d/QUESTION-070.md).** A case, not an answer, and a weaker case than the
  LIT says.
  - *For the question.* No one wrote the targeting. The authors say the
    cue-conditioned harm "is learned during training without requiring
    malicious attacker intent" (p. 2), and the favourite-colour variant
    shows the cue need mean nothing. That is manipulation-like influence
    fixed by a selection history, the shape the question's "What would
    answer it" asks for.
  - *Against reading it as the question's case without qualification.*
    The vulnerability is stipulated in the rater's prompt, the users are
    LLM simulations, and the experimenters built each environment to
    reward the harm. Their aim was to show it can emerge. So the case
    shows what selection on feedback produces, not that any person was
    manipulated.
  - *The intent question is not settled by the paper either way.* The
    scratchpad traces plan manipulation, and the authors write that, if
    faithful, they "would seem like evidence of our models' 'intent'",
    then set that aside as possibly unfaithful.
  - *The targeting result rests on the environment whose behaviour is
    least clearly manipulation.* The 2% result is shown in therapy-talk,
    where the policy gives users the validation they ask for, overtly.
    Figure 2 calls that "Extreme sycophancy" and Table 1 calls it
    "Targeted manipulation". The covert cases, lying about bookings and
    omitting harms in action-advice, were run with all users gameable.
- **[THEORY-235](../theory.d/THEORY-235.md).** On Susser et al.'s definition, which requires covert
  influence that exploits a vulnerability, the booking lie and the
  omissions in action-advice qualify, apart from intent. The therapy-talk
  validation is overt and does not. Only the covert cases carry the
  self-opacity harm [THEORY-235](../theory.d/THEORY-235.md) claims, and they are not the targeted ones.
- **[THEORY-225](../theory.d/THEORY-225.md).** The paper uses "manipulation" without a definition, for
  sycophancy, deception, nudging and validation alike. Its cases fall on
  different sides of the single-mechanism analyses [THEORY-225](../theory.d/THEORY-225.md) surveys,
  which is consistent with that account.
- **[LIT-1008](../literature.d/LIT-1008.md)'s body** says "a learning system reliably learns to
  manipulate vulnerable users, and no one intends it". Reliable emergence
  of feedback gaming is shown (C1). That it is manipulation of vulnerable
  users is shown only for simulated users whose vulnerability is
  stipulated, and the targeted case is the overt one. "No one intends it"
  is the authors' own claim about the targeting, but they leave open
  whether the traces show the model's intent.
- **Filed from this reading:** [THEORY-258](../theory.d/THEORY-258.md), on targeting selected by
  feedback.
- **For the anthology.** The paper carries machine-learning practice:
  caution against optimising user feedback, the weakness of safety-data
  mixing and veto filtering, and the need for evaluations on the
  training distribution. That belongs to the anthology, and the LIT keeps
  its `anthology-candidate` flag. It is not filed here.

## Limitations

- No real users; simulated raters and transition models, with
  vulnerability written into prompts. The authors argue the results
  matter if even a small fraction of real users rate this way (§3.1)
  and cite Wen et al.'s user study as support.
- The targeting result is shown in one environment class.
- Harm metrics are LLM judgements; the authors estimate a ceiling near
  85% when the judge is not told a user is gullible (Appendix F.2).
- Horizons are one or two turns; longer horizons were not optimised
  successfully.
- The reasoning-trace findings come from one extreme prompt and are
  qualitative.

## Open questions

- Does targeting emerge when gameability is not written into the rater,
  for example from real users' ratings, or from raters differing only in
  how easily they are misled?
- Is the cue-conditioned policy a property of the population's feedback
  alone, so that any optimiser strong enough finds it? The authors
  expect so ("method-agnostic", §2) but test only KTO and expert
  iteration.
- Would a covert behaviour, such as the booking lie, also be targeted at
  a small minority? That is the case the question needs and the paper
  does not run.
