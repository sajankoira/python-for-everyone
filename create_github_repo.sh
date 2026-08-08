#!/bin/bash
# Script to create GitHub repo https://github.com/sajankoira/python-for-everyone
# Usage: 
# 1. Create a Personal Access Token (PAT) at https://github.com/settings/tokens/new
#    - Give it 'repo' scope
# 2. Run: export GITHUB_TOKEN=your_token_here
#    Then: ./create_github_repo.sh
#
# OR manual method below

set -e

REPO_NAME="python-for-everyone"
USERNAME="sajankoira"
DESCRIPTION="Learn Python from Scratch - Beginner friendly course with code, exercises, projects for everyone. Created by sajankoira."

echo "=== Creating GitHub repo $USERNAME/$REPO_NAME ==="

if [ -z "$GITHUB_TOKEN" ]; then
  echo "❌ GITHUB_TOKEN not set!"
  echo ""
  echo "MANUAL METHOD (2 minutes, no token needed):"
  echo "1. Go to https://github.com/new"
  echo "2. Repository name: $REPO_NAME"
  echo "3. Description: $DESCRIPTION"
  echo "4. Make it Public, DON'T check Add README"
  echo "5. Click Create repository"
  echo "6. Then run: ./push_to_github.sh"
  echo ""
  echo "OR create token at https://github.com/settings/tokens/new and:"
  echo "export GITHUB_TOKEN=ghp_xxxxxx"
  echo "./create_github_repo.sh"
  exit 1
fi

echo "Creating repo via GitHub API..."
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/user/repos \
  -d "{
    \"name\": \"$REPO_NAME\",
    \"description\": \"$DESCRIPTION\",
    \"private\": false,
    \"has_issues\": true,
    \"has_projects\": true,
    \"has_wiki\": true
  }"

echo ""
echo "✅ Repo creation request sent! Check https://github.com/$USERNAME/$REPO_NAME"
echo "Now run ./push_to_github.sh to push code"
