import importlib.util
import os

spec = importlib.util.spec_from_file_location(
    "screen", os.path.join(os.path.dirname(os.path.abspath(__file__)), "screen.py"))
screen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(screen)


def test_full_design_gets_all_flags():
    t = ("Participants learned to avoid shock; avoidance was made costly while "
         "US expectancy ratings were collected and approach was measured.")
    assert screen.flags(t) == {"C1", "C2", "C3", "C4"}


def test_unrelated_text_gets_none():
    assert screen.flags("A survey of gardening habits in retirees.") == set()


def test_expectancy_without_intervention():
    f = screen.flags("Fear conditioning with shock expectancy ratings.")
    assert "C3" in f and "C1" in f and "C2" not in f


def test_empty_text():
    assert screen.flags(None) == set()
