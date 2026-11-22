# LEAD-068: same oversight, the acting institution's speed varied

The simulation arm of CASE-285 (A33 §10 C of the exchange "Assess Depp
Heard Abuse"), run on 2026-11-22. The model is the assistant's and every
rate in it is invented; it shows what holds in the model, not in any
institution.

## Model (`model.py`)

Time in days. The acting institution initiates actions as a Poisson stream
(2 a day). One in ten is objectionable: the overseer would redirect it once
evaluated. Each action becomes irreversible a time T after initiation,
gamma with shape 4 and mean 30 / s, where s is the speed factor (slow arm
s = 1, fast arm s = 10).

Held fixed at every speed (CASE-285's "authority, information and
resources"; the objection channel; the policy):

- authority: an objection the overseer issues suspends the action, taking
  effect I = 0.25 days after evaluation ends;
- information: the overseer notices each action after D, exponential, mean
  2 days;
- resources: c = 4 reviewers, evaluation time gamma, shape 2, mean 1.5
  days, first come first served.

An action is **intercepted** if it is suspended or redirected before it
becomes irreversible. Intervention capacity (A23 §10's first measure) is
the share of objectionable actions intercepted.

Variants in the fast arm, added one at a time (CASE-285's three):

- **limits** (precommitted limits with escalation): checked at initiation;
  an objectionable action is outside them with probability q (coverage), a
  benign one with probability fp. Outside: held at once, its clock stopped,
  escalated into the same review queue without deadline; benign ones
  resume after evaluation.
- **suspend** (automatic suspension on a flagged objection): at detection an
  objectionable action is flagged with probability h, a benign one with
  probability fa; a flagged action detected before it is irreversible is
  suspended at once, with no lag, and queued without deadline.
- **pause**: every action waits a fixed P before its clock to
  irreversibility starts.

Measures: intervention capacity; benefit per benign action, exp(−delay /
5 days), where delay is time from initiation to effect (the fast arm's
benefit, A23 §10's third measure, read as gap kept); friction, read per
party: the actor's delay (initiating), reviewer load and reviews per
interception (challenging), objectionable actions that become irreversible
per 1000 actions, which can only be corrected after the fact (correcting).
"Reviewer load" is review work done divided by capacity over the run;
above 1 means escalated work arrives faster than it can be done and the
backlog grows with the length of the run.

## Choices the design left open, made here

1. **What "speed" is.** CASE-285 says speed of making actions irreversible,
   "with corresponding deadlines". Two readings are run and reported
   separately: *latency* (s divides T, the rate of actions is unchanged)
   and *throughput* (s also multiplies the rate of actions, A33 §4's
   "accelerated one timescale without proportionately increasing
   another's capacity"). Latency is the reading closer to CASE-285's text.
2. The overseer skips an action only once it is already irreversible, not
   one it could no longer stop in time.
3. Evaluation is correct: the overseer knows an objectionable action once
   it has evaluated it, in both arms.
4. Escalations and suspensions share the reviewers' queue with ordinary
   reviews, first come first served, with no priority.
5. Automatic suspension and limits act with no lag; an issued objection
   takes I.
6. Benefit decays exponentially with delay, horizon 5 days; slow and fast
   arms differ in benefit only through delay.
7. Speeds compared: 1 against 10, with a sweep from 1 to 30.

## Files

- `model.py`: the model; `fcfs_reneging` is the queue (c servers, first
  come first served, an item leaves unserved if its start would come at or
  after its deadline).
- `study.py`: the runs; writes `results.json` and `results.md`.
  20 seeds per configuration (seeds 0–19, shared across arms, so in the
  latency reading the arms see the same draws). Sections: A, speed sweep in
  both readings; B and C, the fast arm's variants in each reading; D, the
  slow-fast contrast under ten other settings of the fixed oversight.
- `test_model.py`: pytest for the queue, the timing condition, the
  no-queue limit against an independent estimate of P(D + E + I < T), and
  the variants' identities.

## Rerun

    cd scratch/studies/lead-068
    python3 -I -m pytest -q -p no:cacheprovider test_model.py   # under 1 s
    python3 -I study.py > /dev/null                               # about 1 min
