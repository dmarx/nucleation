# record/promotion-audit/test_triage_title.py
"""Tests for triage_title.py: the title-assertion classes, ties, labels, routes and the control."""
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
import triage_title as tt  # noqa: E402


def body(shown: str = "Stuff.") -> str:
    return f"\n# THEORY-001: x\n\n## What was actually shown\n\n{shown}\n\n## What this does not say\n\nNothing.\n"


def test_theorem_title_with_proof_in_shown() -> None:
    c, _ = tt.classify(tt.signals("For every finite X, the bound holds if and only if Y is injective",
                                  body("Theorem 2 is proved in the appendix.")))
    assert c == "theorem"


def test_measurement_title() -> None:
    c, _ = tt.classify(tt.signals("In Smith's experiments, recall fell by 12% across three datasets",
                                  body("Table 2 reports the runs.")))
    assert c == "measurement"


def test_argument_title() -> None:
    c, _ = tt.classify(tt.signals("What an utterance does to its context is part of its meaning",
                                  body("Argued from examples.")))
    assert c == "argument"


def test_report_title() -> None:
    c, _ = tt.classify(tt.signals("Idreos et al. conjecture that no access method can minimise all three overheads",
                                  body("Theorem 1 is stated.")))
    assert c == "report"


def test_no_signal_defaults_to_argument() -> None:
    c, margin = tt.classify(tt.signals("The tale is built from a small set of functions", body()))
    assert c == "argument" and margin == 0


def test_argument_wins_a_title_only_tie_with_theorem() -> None:
    # "account" fires the argument rule; "exactly" fires the theorem title; no proof in the evidence
    s = tt.signals("On this account, a blanket falls exactly where the model puts it", body("Argued."))
    assert s["argument_title"] and s["theorem_title"] and not (s["cites"] or s["shown_thm"])
    assert tt.classify(s)[0] == "argument"


def test_measurement_wins_a_tie_with_theorem_only_from_its_title() -> None:
    s = tt.signals("In rodents, the bound on stress exceeds controls", body("Stuff."))
    sc = tt.scores(s)
    assert sc["measurement"] == sc["theorem"]
    assert tt.classify(s)[0] == "measurement"


def test_label_mapping() -> None:
    assert tt.label_classes("theorem (Theorem 4 of LIT-245), re-derivation route") == ["theorem"]
    assert tt.label_classes("measurement, one study read in full") == ["measurement"]
    assert tt.label_classes("argument plus a reported measurement") == ["argument"]
    assert tt.label_classes("explanatory thesis plus model numerics") == ["argument"]
    assert tt.label_classes("compound, a measurement (v3) and a theorem (v2)") == ["theorem", "measurement"]
    assert tt.label_classes("report of a conjecture") == ["report"]
    assert tt.label_classes("compound") == ["theorem", "measurement"]


def test_labels_from_batches_and_decisions(tmp_path: Path) -> None:
    (tmp_path / "batches").mkdir()
    (tmp_path / "decisions").mkdir()
    (tmp_path / "batches" / "batch-031.yaml").write_text(
        yaml.safe_dump({"sort": {"THEORY-073": "argument (a critique)"}}))
    (tmp_path / "decisions" / "THEORY-073.yaml").write_text(
        yaml.safe_dump({"id": "THEORY-073", "reviewed_revision": "abc"}))
    (tmp_path / "decisions" / "THEORY-026.yaml").write_text(
        yaml.safe_dump({"id": "THEORY-026", "reviewed_revision": "def", "title_asserts": "theorem"}))
    labels = tt.labels(tmp_path)
    assert labels["THEORY-073"] == (["argument"], "abc", "argument (a critique)")
    assert labels["THEORY-026"][0] == ["theorem"]


def test_per_class_precision_recall() -> None:
    rows = [("theorem", ["theorem"]), ("theorem", ["measurement"]), ("measurement", ["measurement"]),
            ("argument", ["theorem", "measurement"])]
    pr = tt.class_precision_recall(rows)
    # a missed compound is a miss for each of its parts
    assert pr["theorem"] == {"tp": 1, "fp": 1, "fn": 1, "precision": 0.5, "recall": 0.5}
    assert pr["measurement"]["recall"] == 0.33
    assert tt.accuracy(rows) == 0.5


def test_control_draws_every_kth_from_argument_and_report() -> None:
    rows = [{"code": f"THEORY-{i:03d}", "class": "argument" if i % 2 else "theorem"} for i in range(1, 31)]
    ctrl = tt.control(rows, size=5)
    assert len(ctrl) == 5 and all(int(c[-3:]) % 2 for c in ctrl)
    assert ctrl == sorted(ctrl)
