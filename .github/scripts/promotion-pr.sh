#!/usr/bin/env bash
# .github/scripts/promotion-pr.sh
#
# Keeps the owner's review point open: whenever staging differs from main,
# a pull request from staging into main is open (the decision on the
# promotion pull request, kept by a workflow). Run by the Promotion PR
# workflow on every push to staging. Opens one if none is open; otherwise
# does nothing. With DRY_RUN=1 it prints what it would do.
#
# "Differs" is a content diff, not a commit count: right after a promotion
# the back-merge leaves staging one merge commit ahead of main with the same
# tree, and that must not open an empty pull request.
set -euo pipefail

git fetch -q origin main staging
if git diff --quiet origin/main origin/staging; then
  echo "staging has the same content as main; nothing to promote"
  exit 0
fi
repo="${GITHUB_REPOSITORY:?set GITHUB_REPOSITORY to owner/name}"
open=$(gh api "repos/$repo/pulls?base=main&head=${repo%%/*}:staging&state=open" --jq 'length')
if [ "$open" != "0" ]; then
  echo "a promotion pull request is already open"
  exit 0
fi
body=$(mktemp)
{
  echo "The owner's review point: staging differs from main, and merging this pull request is the promotion. It tracks the staging branch, so it grows as work merges into staging."
  echo
  echo "## Merged into staging since main"
  echo
  git log --merges --first-parent --format='- %s' origin/main..origin/staging
  echo
  echo "Opened by the Promotion PR workflow."
} > "$body"
if [ "${DRY_RUN:-0}" = "1" ]; then
  echo "would open: Promote staging into main"; cat "$body"; exit 0
fi
gh api "repos/$repo/pulls" -f title="Promote staging into main" \
  -f head=staging -f base=main -F body=@"$body" --jq '.html_url'
