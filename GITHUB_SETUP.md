# How to Push This Repo to GitHub - Step by Step

You have created repo locally. Now push to GitHub so others can learn!

## Step 1: Create Empty GitHub Repo
1. Go to github.com -> New Repository
2. Name: `python-for-everyone` (or your choice)
3. DO NOT check "Add README" - keep empty!
4. Create repository

## Step 2: Configure Git (first time only)
```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
git config --global init.defaultBranch main
```

## Step 3: Push Local Repo
GitHub will show you commands. Use these (replace sajankoira):

```bash
cd python-for-everyone
git branch -M main
git remote add origin https://github.com/sajankoira/python-for-everyone.git
git add .
git commit -m "Initial commit: Python from scratch - Basics + Projects"
git push -u origin main
```

If it asks for password: Use Personal Access Token (GitHub > Settings > Developer settings > Tokens)

## Step 4: Daily Workflow as You Learn

Each day after learning:

```bash
git status
git add .
git commit -m "Day 2: Completed control flow - if else and loops"
git push
```

## Step 5: Make Repo Attractive for Others

Add to GitHub About section:
- Description: "Learn Python from Scratch - Beginner friendly course with code, exercises, projects"
- Topics: python, beginners, learning, tutorial, 100-days-of-code

Enable:
- Issues: Let learners ask doubts
- Discussions (optional)

Add Social Preview image (optional): Use Canva to make 1280x640 banner.

## Step 6: Grow Community

- Share on LinkedIn: "I started learning Python and building public repo..."
- Share on Reddit r/learnpython
- Add to your resume/portfolio!

You're now not just learning, you're teaching!
