### Changed

- Fifty-six entries had lost the temporary codes in their `formerly:` lists: a code-rewriting step after a promotion wrote each entry's own concrete code there. Twenty-eight were lost on staging at the merge of pull request 746 and are restored from main. Twenty-eight were already lost on main from earlier merges and are restored from the earliest concretized version in history. After the restore no entry lists itself and no temporary code is claimed twice.
- The run-lead skill now says how to merge staging into a branch after a promotion: rewrite cited temporary codes, never a `formerly:` list, and check the result.
