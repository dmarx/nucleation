#!/usr/bin/env bash
# .github/scripts/back-merge.sh
#
# Merges main into staging, so staging carries main's permanent codes and
# views (the decision adding the staging branch). Run by Docs after
# docs-generate on every push to main, and by Promote after it promotes:
# Promote pushes with GITHUB_TOKEN, which starts no Docs run, so it needs
# its own call.
#
# Two outcomes are left red for a person, never resolved here:
#   - a conflict: staging changed something main also changed (in practice
#     an entry main just concretized). Main is already finished; only
#     staging waits.
#   - staging moving three times while this runs. A move without a conflict
#     is retried from a fresh fetch, since the merge is then just redone.
set -euo pipefail

git config user.name  "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"

if ! git ls-remote --exit-code --heads origin staging >/dev/null; then
  echo "no staging branch; nothing to do"
  exit 0
fi

for attempt in 1 2 3; do
  git fetch origin main staging
  git checkout -B staging origin/staging
  if git merge-base --is-ancestor origin/main HEAD; then
    echo "staging already contains main"
    exit 0
  fi
  if ! git merge --no-edit origin/main; then
    git merge --abort || true
    echo "::error::main does not merge cleanly into staging; resolve by hand (git merge origin/main on staging)"
    exit 1
  fi
  if git push origin HEAD:staging; then
    exit 0
  fi
  echo "staging moved during the merge (attempt $attempt); retrying"
done
echo "::error::staging kept moving; merge main into staging by hand"
exit 1
