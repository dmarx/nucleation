# scratch/tools/record_history/gitlog.py
"""Read the repository's history: commits with their raw changes, and blobs."""
from __future__ import annotations

import subprocess
from dataclasses import dataclass, field
from pathlib import Path

ZERO = "0" * 40
FORMAT = "@@%H|%at|%an|%s"  # author time: the development clock


@dataclass
class Change:
    status: str  # A, M, D, R (rename) or C, T
    old_sha: str | None
    new_sha: str | None
    old_path: str | None
    new_path: str | None


@dataclass
class Commit:
    sha: str
    time: int
    author: str
    subject: str
    changes: list[Change] = field(default_factory=list)

    @property
    def bot(self) -> bool:
        return "[bot]" in self.author


def parse_raw_log(text: str) -> list[Commit]:
    """Parse `git log --raw --no-abbrev --format=FORMAT` output."""
    commits: list[Commit] = []
    for line in text.splitlines():
        if line.startswith("@@"):
            sha, time, author, subject = line[2:].split("|", 3)
            commits.append(Commit(sha, int(time), author, subject))
        elif line.startswith(":") and commits:
            meta, *paths = line.split("\t")
            _, _, old, new, status = meta.split(" ")
            kind = status[0]
            old_sha = None if old == ZERO else old
            new_sha = None if new == ZERO else new
            if kind in "RC":
                old_path, new_path = paths
            elif kind == "D":
                old_path, new_path = paths[0], None
            elif kind == "A":
                old_path, new_path = None, paths[0]
            else:
                old_path = new_path = paths[0]
            commits[-1].changes.append(Change(kind, old_sha, new_sha, old_path, new_path))
    return commits


def read_log(repo: Path, rev: str, paths: list[str], walk: str = "all") -> list[Commit]:
    """Commits of `rev`'s history touching `paths`, oldest first.

    walk="all": every non-merge commit, in author-date order. Fine-grained (work on
    staging appears pull request by pull request), but not linear: a side
    branch's deletion can come after the main line's addition. Present state
    is therefore read from the tip's tree (`tree_entries`), not replayed.
    walk="first-parent": the first-parent chain, merges diffed against their
    first parent. Linear and exact at the tip, but a merge (a nightly
    promotion of staging) lands as one commit.
    """
    if walk == "all":
        mode = ["--no-merges", "--author-date-order"]
    elif walk == "first-parent":
        mode = ["--first-parent", "--diff-merges=first-parent"]
    else:
        raise ValueError(f"walk must be 'all' or 'first-parent', not {walk!r}")
    out = subprocess.run(
        ["git", "-C", str(repo), "log", *mode, "--raw", "-M", "--no-abbrev", "--reverse",
         f"--format={FORMAT}", rev, "--", *paths],
        check=True, capture_output=True, text=True).stdout
    return parse_raw_log(out)


def tree_blobs(repo: Path, rev: str, paths: list[str]) -> dict[str, str]:
    """Path to blob sha for every file under `paths` in `rev`'s tree."""
    out = subprocess.run(["git", "-C", str(repo), "ls-tree", "-r", rev, "--", *paths],
                         check=True, capture_output=True, text=True).stdout
    blobs = {}
    for line in out.splitlines():
        meta, path = line.split("\t", 1)
        _, kind, sha = meta.split(" ")
        if kind == "blob":
            blobs[path] = sha
    return blobs


class BlobReader:
    """Batch reader over `git cat-file --batch`, with a small cache."""

    def __init__(self, repo: Path):
        self._p = subprocess.Popen(["git", "-C", str(repo), "cat-file", "--batch"],
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def read(self, sha: str) -> str:
        assert self._p.stdin and self._p.stdout
        self._p.stdin.write(sha.encode() + b"\n")
        self._p.stdin.flush()
        header = self._p.stdout.readline().split()
        if len(header) < 3 or header[1] == b"missing":
            return ""
        data = self._p.stdout.read(int(header[2]))
        self._p.stdout.read(1)  # trailing newline
        return data.decode("utf-8", errors="replace")

    def close(self) -> None:
        if self._p.stdin:
            self._p.stdin.close()
        self._p.wait()
