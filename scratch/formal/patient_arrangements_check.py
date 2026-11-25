"""scratch/formal/patient_arrangements_check.py

Rebuilds the check of CLAIM-741 on its construction CASE-283 (two patient
arrangements) from the entries' text alone; the filer's check was not
kept. Written at the recomputation pass of 2026-11-25 by a session other
than the filer's. Run: python3 -I this file. Standard library only.

c = 1 consent, c = 0 refusal; a = 1 treat, a = 0 refrain.
pi_A(c) = c, pi_B(c) = 1. Right of refusal: Resp(1) = {0, 1}, Resp(0) = {0}.
Checks: (1) on the consenting history both give (1, 1); (2) A meets the test
for every protected exercise, B fails it at c = 0; (3) every one of the 2^4
verdict functions of the realized history (c, a) gives A and B the same
verdict on the consenting occasion, so none represents respect;
(4) the first separation: two histories to one endpoint, one through an
authorized transition and one not, differ under a history test and agree
under every endpoint test. A negative control lets the evaluation see the
policy, and it separates them, so the check can fail.
"""
import itertools

POL = {"A": lambda c: c, "B": lambda c: 1}
RESP = {1: {0, 1}, 0: {0}}


def respects(pol):
    return all(POL[pol](e) in RESP[e] for e in (0, 1))


hist = {p: (1, POL[p](1)) for p in POL}
assert hist["A"] == hist["B"] == (1, 1)
assert respects("A") and not respects("B")

H = list(itertools.product((0, 1), repeat=2))
n = 0
for verdicts in itertools.product((False, True), repeat=len(H)):
    f = dict(zip(H, verdicts))
    assert f[hist["A"]] == f[hist["B"]]
    n += 1
print(f"{n} history-only evaluations: every one gives A and B the same verdict on the consenting history")

# first separation: endpoint q* reached by proposal -> authorization -> change, or by unilateral change
g1 = ("proposal", "authorization", "change:q*")
g2 = ("unilateral change:q*", "foreclosed alternatives", "acceptance")
endpoint = lambda g: [s.split(":")[1] for s in g if ":" in s][-1]
assert endpoint(g1) == endpoint(g2) == "q*"
authorized = lambda g: "authorization" in g and g.index("authorization") < len(g) - 1
assert authorized(g1) and not authorized(g2)

# negative control: an evaluation over the policy (its response to both choices) separates them
policy_eval = lambda p: (POL[p](0), POL[p](1))
assert policy_eval("A") != policy_eval("B")
print("A respects the right, B does not; a policy-level evaluation separates them; endpoints alike for g1, g2")
print("checks pass")
