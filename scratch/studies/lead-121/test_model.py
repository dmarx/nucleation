from model import run, threshold


def test_threshold():
    assert abs(threshold(-0.2, 1.0) - 0.6) < 1e-12


def test_lock_in_above_threshold_against_evidence():
    pi, m = run(0.61)
    assert pi > 0.999 and m > 0.49  # A holds authority; interpretation leans A against e < 0


def test_evidence_wins_below_threshold():
    pi, m = run(0.59)
    assert pi < 0.001 and m < -1.49


def test_no_share_dependence_no_lock_in():
    for pi0 in (0.55, 0.65, 0.9, 0.99):
        pi, m = run(pi0, c=0.0)
        assert pi < 0.001 and m < -1.49


def test_strong_independent_evidence_removes_lock_in():
    pi, m = run(0.99, h=-1.2, c=1.0)
    assert pi < 0.001
