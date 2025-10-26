# Deployment Guide

GitHub Pages only hosts static HTML files - it cannot run Flask/Python applications. You need a platform that supports backend applications.

## Best Free Deployment Options

### Option 1: Render.com (Recommended - FREE)

1. **Sign up** at [render.com](https://render.com)

2. **Push your code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

3. **On Render.com:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Render will auto-detect the Flask app
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Click "Create Web Service"
   - Your app will be live at `your-app-name.onrender.com`

4. **Add CSV file to your GitHub repo**
   - Make sure `bunny.csv` is committed to your repository
   - Push it: `git add bunny.csv && git commit -m "Add CSV" && git push`

### Option 2: Railway.app (FREE with credit card)

1. Sign up at [railway.app](https://railway.app)
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway will auto-deploy your app
5. Your app will be live at `your-app-name.railway.app`

### Option 3: PythonAnywhere (FREE for beginners)

1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Go to "Web" tab
3. Click "Add a new web app"
4. Choose "Flask" and Python version
5. Upload your code or clone from GitHub
6. Your app will be at `username.pythonanywhere.com`

## Files Created for Deployment

- ✅ `Procfile` - Tells the platform how to run your app
- ✅ `render.yaml` - Configuration for Render.com
- ✅ `requirements.txt` - Updated with gunicorn
- ✅ `.gitignore` - Protects sensitive files

## Important: Add Files to Git

Make sure these files are NOT in `.gitignore` (remove them if present):
- `bunny.csv` ✓ (should be committed)
- Files in `images/` folder (if you have any)

Your `.gitignore` already allows these, so you're good!

## Troubleshooting

**Build fails on deployment:**
- Make sure all dependencies are in `requirements.txt`
- Check that your CSV file is committed to the repo

**App shows error:**
- Check the logs on your deployment platform
- Make sure the CSV file path is correct (relative paths work in cloud)

**Images not showing:**
- Upload images to your repo in the `images/` folder
- Commit and push them to GitHub

## Quick Deploy Checklist

1. ✅ Code is on GitHub
2. ✅ `bunny.csv` is in the repository
3. ✅ Student images (if any) in `images/` folder
4. ✅ `requirements.txt` includes gunicorn
5. ✅ Deploy to Render.com or Railway.app
6. ✅ Test your live URL

## Test Locally Before Deploying

```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn (production-like)
gunicorn app:app

# Or with auto-reload for testing
gunicorn --reload app:app
```

Your app will be available at `http://localhost:8000` (default gunicorn port)

