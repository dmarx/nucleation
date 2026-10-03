---
number: 463
status: Read
formerly:
- NOTE-tmpruoh7
paper: LIT-584
title: 'Model-based and model-free Pavlovian reward learning: Revaluation, revision, and revelation'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full: the PMC author manuscript (PMC4074442), sections 1-5, the
    appendix and both figure captions. The text as retrieved strips author
    names from most citations, so studies are named here only where the
    text names them (Robinson & Berridge; Zhang and colleagues; Daw and
    colleagues; Dickinson and Balleine; Holland; Tolman; Wyvell & Berridge
    2001; O'Doherty et al. 2004; Barron, Dolan & Behrens 2013). The
    appendix equations (A1)-(A4) are missing from the retrieved text and are
    described from the prose around them. The Dead Sea salt experiment
    itself (M. J. F. Robinson & Berridge) was not read, and its results are
    taken as this paper reports them.
date: '2026-10-03'
summary: >-
  The paper argues that Pavlovian prediction has a model-based form. A cue
  that predicted disgusting salt was instantly "wanted" in a novel salt
  appetite, before retasting, with mesolimbic activation. That needs
  identity-specific prediction revalued by current state, which no
  model-free cache provides. It proposes "defocusing" of the predicted
  outcome as a model-based source of apparent habit. It argues dopamine can
  carry model-based evaluations. A kappa-transformation model fits the data
  but is described as phenomenological, and no algorithm is offered.
---
<!-- inactive-ok-file: THEORY-062 — Proposed; named as the THEORY filed for this note's candidate, nothing here rests on it -->
<!-- inactive-ok-file: THEORY-045 THEORY-056 — Proposed theories and Deferred seeds, named as accounts this reading bears on; written from the lint report -->

# NOTE-463: Model-based and model-free Pavlovian reward learning: Revaluation, revision, and revelation

## Contribution

Computational accounts had applied the model-based/model-free distinction to
instrumental action and treated Pavlovian prediction as model-free. This
paper argues, from revaluation experiments, that Pavlovian prediction also
has a model-based form, with features the instrumental form may lack:
instant revaluation without retasting, possible subcortical implementation,
and dependence on dopamine. It names the computational gap without filling
it.

## Key insight

A cue's value after an unprecedented change in bodily state cannot be
recalled, because it was never experienced. It can only be inferred, from
what the cue predicts (the outcome's identity) and what that outcome is worth
now (the current state). The salt result shows the inference happens
instantly and drives mesolimbic "wanting". So Pavlovian motivation includes
prospective, state-sensitive computation of the kind usually reserved for
deliberate instrumental choice.

## Assumptions

- **Marr's three levels** organize the argument: computational, algorithmic,
  implementational.
- **Value is relative to motivational state.** V(s_t, m) is the expected
  discounted future utility from circumstance s_t under state m. The
  appendix uses "circumstance" for the RL "state" to avoid confusion with
  motivational state.
- **The experiment's claims of novelty.** The rats had never experienced
  salt appetite, and the test was in extinction. So there was "no new
  learning about its altered UCS or new CS-UCS pairing".
- **A model-free cache holds value only**, "free of any content other than
  value", and is tied to the state in which it was learned. If the state
  changes from m to m̃, "the model-free learning mechanism provides no hint"
  how to change the value (Appendix).

## Key results

- **Dead Sea salt** (§1, Fig. 2).
  - Training: a salt-paired lever was approached less, with the rats
    "turning away and sometimes pressing themselves against the opposite
    wall".
  - Test after deoxycorticosterone and furosemide: the salt lever's
    engagement rose "by a factor of more than 10", nearly matching the
    sucrose lever. There was no change for the sucrose or control levers.
    The cue sometimes drew orofacial "liking" reactions.
  - Fos was raised in accumbens core and rostral shell, VTA, rostral ventral
    pallidum, and infralimbic and orbitofrontal cortex, only for the cue and
    the appetite state together.
- **Not ubiquitous** (§3). Appetitive cues sometimes persist after their
  outcome is devalued, notably after over-training. Second-order cues are
  less affected than first-order ones, and there may be a gradient from
  outcome-proximal to distal cues.
- **Defocusing** (§3). The predicted outcome's representation may become
  generalized with extended training. The result is a "spectrum of
  abstraction", running from specific identity, through categorical
  ("tasty food"), to pure valence. This would reinterpret general
  Pavlovian-instrumental transfer as defocused model-based prediction.
  Holland's finding is offered as a case: specific transfer survived
  devaluation while proximal head entries fell.
- **Kappa model** (§3, Appendix). Zhang and colleagues' κ factor multiplies
  or log-transforms a cached prediction to give the new incentive value. The
  authors say it describes the data but shows "how violence must be done to
  any pre-existing model-free cache". To apply the right κ, it needs the outcome's identity and the
  transition structure, which "exactly constitute a model".
- **Implementation** (§4).
  - Decorticate animals still show salt revaluation, so cortex is "at least
    not necessary".
  - Instrumental incentive learning proceeds under dopamine blockade, while
    Pavlovian revaluation is modulated by dopamine.
  - Only sign-trackers showed strong cue-evoked dopamine release.
  - Daw and colleagues' uncertainty account is offered as a way to keep one
    model-based knowledge system with two routes to action.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Pavlovian prediction can be model-based: identity-specific and revalued by current state without new experience | strong for the one experiment as reported; the generalization is argued | §1–2, Dead Sea salt; related revaluation studies |
| C2 | A model-free cache cannot produce instant revaluation to a never-experienced state | strong (follows from what a cache stores) | §2, Appendix |
| C3 | Persistence after devaluation may reflect a defocused model-based prediction, not model-free control | hypothesis; one reinterpreted study | §3; Holland's PIT results |
| C4 | Dopamine release can reflect model-based evaluation | moderate–weak: inferred from Fos in VTA and accumbens, not from measured dopamine | §4 |
| C5 | Pavlovian and instrumental model-based evaluation may differ in mechanism (retasting, dopamine dependence) | moderate: contrasting findings cited; "the case is still open" | §4 |
| C6 | Pavlovian revaluation does not require cortex | moderate: decorticate studies cited | §4 |

## Concepts

- **model-based / model-free**: prediction from a model of the environment
  and prospective calculation, versus cached long-run values learned
  retrospectively.
- **incentive salience**: the attribution of motivational value ("wanting")
  that makes a cue attractive and able to elicit approach and even
  consumption.
- **conditioned alliesthesia**: the cue undergoing the same
  state-dependent hedonic change as its outcome.
- **defocusing**: the predicted outcome's representation becoming
  generalized or categorical with extended training.
- **Pavlovian-instrumental transfer (PIT)**: a cue boosting instrumental
  effort. In *specific* PIT the effort is for the same outcome. In *general*
  PIT it is for a different, related outcome.

## Connections

- **Daw, Niv and Dayan ([LIT-580](../literature.d/LIT-580.md), [NOTE-459](NOTE-459.md)).** The distinction and
  the uncertainty-based arbitration come from there. This paper extends them
  to Pavlovian prediction. It suggests that Pavlovian model-based
  predictions "might be less uncertain" than instrumental ones, because they
  need not assess action-outcome contingency, and so "may more easily best
  their model-free counterparts".
- **Ainslie ([LIT-586](../literature.d/LIT-586.md)).** Ainslie reads Berridge's wanted-but-not-liked
  behaviours as reward-driven urges and rejects conditioning as a separate
  selective principle. This paper treats Pavlovian prediction as its own
  process, now with a model-based form. On whether conditioning is a
  distinct principle, the two disagree. Neither cites the other's argument.
- **Barrett ([LIT-542](../literature.d/LIT-542.md)).** Barrett's account of emotion builds interoceptive
  prediction of bodily state into what an emotion is. This paper shows
  bodily state entering a cue's motivational value through a predictive
  model. The overlap is in the role of state-dependent prediction, not in
  any claim either makes about the other.

## Bearing on the record

- **[THEORY-045](../theory.d/THEORY-045.md) (felt affect as the experience of regulatory state).** The
  paper supplies a case in which the body's regulatory state (sodium need)
  instantly changes the value, and the "liking" reaction, attached to a
  predictive cue. That is consistent with the theory and does not test its
  claim about experience.
- **[THEORY-056](../theory.d/THEORY-056.md).** Not directly. The paper is about how value is computed,
  not how one motive checks another. Its point that one model-based system
  may reach action by two routes (instrumental and Pavlovian), each
  competing with model-free control, is a picture of competition among
  peers.
- **A candidate THEORY** (with [LIT-580](../literature.d/LIT-580.md)): behaviour draws on both
  model-based and model-free predictions in instrumental and Pavlovian
  learning, and their relative control follows their reliability. Filed
  as [THEORY-062](../theory.d/THEORY-062.md).
- **No ML instruction.** Nothing here belongs in the anthology.

## Limitations

- **One flagship experiment.** The case rests mainly on the salt study,
  which this note does not read first-hand.
- **No algorithm.** "A comprehensive algorithmic version of the model-based
  Pavlovian computation has yet to be proposed."
- **Dopamine is inferred, not measured** in the key experiment. Fos marks
  neural activity, not dopamine release.
- **Defocusing is a hypothesis** that makes model-based and model-free
  control harder to tell apart. The authors concede this and propose tests.

## Open questions

- Does instant Pavlovian revaluation survive disrupting prefrontal input to
  midbrain dopamine? The authors propose this test.
- Can PIT experiments that vary appetite and outcome category reveal several
  degrees of defocusing for the same outcome at once?
- What algorithm produces the revaluation without retasting?

## Corrections

- **Title case.** The PMC manuscript title is capitalized "Revaluation,
  Revision and Revelation", without a serial comma. The Crossref title, used
  for the LIT, is "Revaluation, revision, and revelation".
