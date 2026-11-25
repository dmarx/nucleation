import math

import summarize as s


def base(**kw):
    c = {"case": "x", "arm": "R", "outcome_after": "W+", "source_standing": "finding",
         "reputation": "private", "benefit": "opposed"}
    c.update(kw)
    return c


def test_pct_from_log_matches_paper_range():
    # Gallo et al. translate -0.288 and -0.193 into 25% and 18% reductions.
    assert round(s.pct_from_log(-0.288)) == -25
    assert round(s.pct_from_log(-0.193)) == -18


def test_pct_zero():
    assert s.pct_from_log(0.0) == 0.0


def test_significance():
    assert s.significant(-2.61)
    assert not s.significant(-0.87)


def test_costly_private_weighing_meets():
    assert s.meets(base(), set())


def test_weighing_with_exposed_reputation_fails():
    assert not s.meets(base(reputation="exposed"), set())


def test_weighing_aligned_with_benefit_fails():
    assert not s.meets(base(benefit="aligned"), set())


def test_allegation_fails():
    assert not s.meets(base(source_standing="allegation"), set())


def test_unripe_fails():
    c = base(outcome_after="unripe")
    assert not s.meets(c, set())
    assert "ended_with_window" in [k for k, v in s.standard_conditions(c).items() if not v]


def test_reversion_needs_pair():
    a = base(case="a", arm="S", outcome_after="W-", reputation="exposed", benefit="aligned")
    b = base(case="b", arm="R", outcome_after="W-", reputation="exposed", benefit="aligned")
    assert not s.meets(a, set())
    p = s.pairs([a, b])
    assert p == [("a", "b")]
    assert s.meets(a, {"a", "b"})


def test_no_pair_within_one_arm():
    a = base(case="a", arm="S", outcome_after="W-")
    b = base(case="b", arm="S", outcome_after="W-")
    assert s.pairs([a, b]) == []


def test_data_result():
    res = s.main()
    assert res["any_case_meets_standard"] is False
    assert set(res["cases"]) == {"purdue", "siemens", "wells_fargo"}
    post = [c for c in res["coefficients"] if c["term"] == "Treat x Post Probation"]
    assert post and not any(c["significant_5pct"] for c in post)
    during = [c for c in res["coefficients"] if c["term"] == "Treat x During Probation"]
    assert during and all(c["significant_5pct"] for c in during)
    assert all(math.isfinite(c["percent"]) for c in res["coefficients"])
