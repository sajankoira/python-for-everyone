#!/bin/bash
# After creating empty repo on GitHub, run this to push

set -e

USERNAME="sajankoira"
REPO_NAME="python-for-everyone"

echo "=== Pushing local repo to GitHub ==="
echo "Repo: https://github.com/$USERNAME/$REPO_NAME"

git branch -M main
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/$USERNAME/$REPO_NAME.git

echo "Pushing..."
git push -u origin main

echo ""
echo "✅ DONE! Visit: https://github.com/$USERNAME/$REPO_NAME"
echo "Your python course is now LIVE for everyone to learn!"
