"""scratch/studies/lead-175/test_resume.py

pytest for resumption in posterior.py and sgd_sweep.py (run:
python3 -I -m pytest scratch/studies/lead-175 -q).

Each test simulates an interruption at the point a code review found unsafe:
- posterior.py: between appending a block to the JSONL and saving the sampler
  state;
- sgd_sweep.py: after some, but not all, of a job's result lines are written.
"""
import json, os, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
import posterior
import sgd_sweep

PT = ["pt", None, "--chains", "2", "--iters", "4", "--burn", "1", "--nleap", "2",
      "--classify-every", "2", "--ladder", "20,100,3", "--seed", "3"]


def _pt(out, blocks):
    argv = list(PT); argv[1] = str(out)
    posterior.main(argv + ["--blocks", str(blocks)])


def _lines(path):
    return [json.loads(l) for l in open(path)]


def test_posterior_crash_between_write_and_checkpoint_resumes_exactly(tmp_path):
    ref = tmp_path / "ref.jsonl"
    _pt(ref, 3)
    out = tmp_path / "out.jsonl"
    _pt(out, 1)
    one = tmp_path / "after1.npz"
    shutil.copy(str(out) + ".STATE.npz", one)
    _pt(out, 2)
    # The crash: block 1 is in the JSONL, the checkpoint still says one block.
    shutil.copy(one, str(out) + ".STATE.npz")
    _pt(out, 3)
    assert _lines(out) == _lines(ref)


def test_posterior_resume_without_crash_matches_uninterrupted(tmp_path):
    ref = tmp_path / "ref.jsonl"
    _pt(ref, 3)
    out = tmp_path / "out.jsonl"
    _pt(out, 2)
    _pt(out, 3)
    assert _lines(out) == _lines(ref)


def test_posterior_output_without_checkpoint_fails(tmp_path):
    out = tmp_path / "out.jsonl"
    _pt(out, 2)
    os.remove(str(out) + ".STATE.npz")
    with pytest.raises(SystemExit, match="no checkpoint"):
        _pt(out, 3)


def test_posterior_changed_configuration_fails(tmp_path):
    out = tmp_path / "out.jsonl"
    _pt(out, 1)
    argv = list(PT); argv[1] = str(out)
    argv[argv.index("--iters") + 1] = "5"
    with pytest.raises(SystemExit, match="configuration"):
        posterior.main(argv + ["--blocks", "2"])


def test_posterior_torn_last_line_is_dropped_and_rerun(tmp_path):
    ref = tmp_path / "ref.jsonl"
    _pt(ref, 2)
    out = tmp_path / "out.jsonl"
    _pt(out, 1)
    with open(out, "a") as f:
        f.write('{"mode": "pt", "blo')          # a write cut off mid-line
    _pt(out, 2)
    assert _lines(out) == _lines(ref)


SGD = ["--epochs", "3", "--ns", "30", "--batches", "10", "--lrs", "0.01,0.02",
       "--inits", "4gon,prior", "--seeds", "2"]
SGD_RUNS = 2 * 2 * 2


def _sgd_keys(path):
    return sorted((d["n"], d["batch"], d["epochs"], d["lr"], d["init"], d["seed"])
                  for d in _lines(path))


def test_sgd_partial_job_is_completed_not_skipped(tmp_path):
    ref = tmp_path / "ref.jsonl"
    sgd_sweep.main([str(ref)] + SGD)
    full = open(ref).read().splitlines(keepends=True)
    assert len(full) == SGD_RUNS
    out = tmp_path / "out.jsonl"
    out.write_text("".join(full[:3]))          # interrupted after three runs
    sgd_sweep.main([str(out)] + SGD)
    assert _sgd_keys(out) == _sgd_keys(ref)
    assert sorted(map(json.dumps, _lines(out))) == sorted(map(json.dumps, _lines(ref)))


def test_sgd_torn_last_line_is_dropped(tmp_path):
    ref = tmp_path / "ref.jsonl"
    sgd_sweep.main([str(ref)] + SGD)
    full = open(ref).read().splitlines(keepends=True)
    out = tmp_path / "out.jsonl"
    out.write_text("".join(full[:2]) + full[2][:40])
    sgd_sweep.main([str(out)] + SGD)
    assert _sgd_keys(out) == _sgd_keys(ref)


def test_sgd_corrupt_line_before_the_end_fails(tmp_path):
    ref = tmp_path / "ref.jsonl"
    sgd_sweep.main([str(ref)] + SGD)
    full = open(ref).read().splitlines(keepends=True)
    out = tmp_path / "out.jsonl"
    out.write_text(full[0][:40] + "\n" + "".join(full[1:3]))
    with pytest.raises(SystemExit, match="line 1"):
        sgd_sweep.main([str(out)] + SGD)
