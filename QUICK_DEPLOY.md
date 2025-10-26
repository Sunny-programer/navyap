# 🚀 Quick Deployment Guide

## The Problem
GitHub Pages only shows static files (like HTML) - it cannot run Python/Flask apps!

## The Solution: Deploy to Render.com (FREE)

### Step-by-Step:

#### 1. Push Code to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

#### 2. Deploy on Render.com
- Go to [render.com](https://render.com) and sign up (FREE)
- Click "New +" → "Web Service"
- Connect your GitHub account
- Select your repository
- Use these settings:
  - **Name**: student-dashboard (or any name)
  - **Environment**: Python 3
  - **Build Command**: `pip install -r requirements.txt`
  - **Start Command**: `gunicorn app:app`
  - **Plan**: Free
- Click "Create Web Service"
- Wait 5-10 minutes for deployment
- Your app will be live at: `https://your-app-name.onrender.com`

#### 3. Test Your Deployed App
- Visit the URL you get from Render
- Login with any roll number from bunny.csv (101, 102, 103, 104, or 105)
- See your graphs!

## Alternative: Railway.app
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Create new project → Deploy from GitHub repo
4. Select your repo
5. Done! Your app is live

## ⚠️ Important Notes

**For your CSV file:**
- Make sure `bunny.csv` is committed to GitHub
- It should be in the root of your repo

**For images:**
- Add student photos to `images/` folder (optional)
- Commit them: `git add images/ && git commit -m "Add images" && git push`
- Images should be named as roll numbers: `101.jpg`, `102.jpg`, etc.

## Troubleshooting

**"Build failed" error:**
- Check that `requirements.txt` has all dependencies
- Look at the build logs on Render

**"Module not found" error:**
- Make sure gunicorn is in requirements.txt (already added)

**"CSV file not found":**
- Make sure bunny.csv is in your GitHub repository
- Check that it's not in .gitignore

## What's Different from Local?

Local: Run with `python app.py`
Cloud: Run with `gunicorn app:app` (production server)

Both work the same way - your app is just running on a server instead of your computer!

