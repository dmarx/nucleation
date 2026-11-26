# scratch/tools/record_history/gitlog.py
"""Read the repository's history: commits with their raw changes, and blobs."""
from __future__ import annotations

import subprocess
from dataclasses import dataclass, field
from pathlib import Path

ZERO = "0" * 40
FORMAT = "@@%H|%ct|%an|%s"


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


def read_log(repo: Path, rev: str, paths: list[str]) -> list[Commit]:
    """The first-parent history of `rev` touching `paths`, oldest first.

    Each merge is diffed against its first parent, so the sequence is linear
    and its cumulative diffs reproduce `rev`'s tree exactly. A pull request
    merged with a merge commit lands as one change, at its merge time. (A
    date-ordered walk of every commit is not linear: a side branch's
    deletion, replayed after the main line's addition, loses a live entry.)
    """
    out = subprocess.run(
        ["git", "-C", str(repo), "log", "--first-parent", "--diff-merges=first-parent",
         "--raw", "-M", "--no-abbrev", "--reverse", f"--format={FORMAT}", rev, "--", *paths],
        check=True, capture_output=True, text=True).stdout
    return parse_raw_log(out)


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
