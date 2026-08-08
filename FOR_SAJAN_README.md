# For Sajan - How to get this repo on GitHub in 2 mins

This workspace already has FULL repo ready with commits!

### Option 1: FASTEST (GitHub website, no terminal needed)

1. Go to https://github.com/new
2. Name: `python-for-everyone`
3. Description: `Learn Python from Scratch - Beginner friendly course`
4. Public, **DO NOT check README**
5. Create repository
6. On next page, click "uploading an existing file" link
7. Download `python-for-everyone.zip` from this workspace (bottom)
8. Unzip on your computer, then drag all files to GitHub page
9. Commit directly to main

Done!

### Option 2: Using your own laptop terminal (recommended, preserves git history)

Download zip, unzip, then:

```bash
cd python-for-everyone
# If you already created empty repo on github.com/new:
git remote add origin https://github.com/sajankoira/python-for-everyone.git
git branch -M main
git push -u origin main
# Enter your GitHub username and PAT when asked
```

Your PAT (if needed): Create at https://github.com/settings/tokens/new -> classic -> check `repo` -> Generate

### Option 3: I will push for you (need token)

If you paste your GitHub PAT here temporarily, I can push for you right now.

Example:
```bash
export GITHUB_TOKEN=ghp_yourtoken
./create_github_repo.sh
./push_to_github.sh
```

Your repo will be: https://github.com/sajankoira/python-for-everyone

---

After push, enable:
- Go to repo Settings > Pages -> Deploy from main branch -> Your course becomes a website!
- Add About: "Learn Python from Scratch..."

Share link on LinkedIn / Twitter!
