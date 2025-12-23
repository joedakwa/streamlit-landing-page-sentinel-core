# Setup New GitHub Repo for Landing Page

## Step 1: Create New GitHub Repo

1. Go to https://github.com/new
2. Repository name: `sentinel-core-tiktok-landing` (or any name you like)
3. Set to **Private** (or Public, your choice)
4. **Don't** initialize with README, .gitignore, or license
5. Click **"Create repository"**

## Step 2: Connect and Push

After creating the repo, GitHub will show you commands. Use these:

```bash
cd /home/josdak/solidity/influencing/social-media/tiktok-landing-page

# Add your new GitHub repo as remote
git remote add origin https://github.com/joedakwa/REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Replace `REPO_NAME` with your actual repo name!**

## Step 3: Deploy to Streamlit Cloud

Once pushed to GitHub:

1. Go to https://share.streamlit.io
2. Click "New app"
3. Fill in:
   - **Repository**: `joedakwa/your-repo-name`
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL**: (optional) `sentinel-core-tiktok.streamlit.app`
4. Click "Deploy"

## Step 4: Add Secrets

After deployment:
1. Go to app Settings → Secrets
2. Add:
   ```toml
   TIKTOK_USERNAME = "joedakwa"
   TIKTOK_PIXEL_ID = "YOUR_PIXEL_ID_HERE"
   ```
3. Save

---

**Your landing page repo will be separate from your main "influencing" repo!** ✅

