# Setup Public Repo for Streamlit Deployment

## Important Notes

- ✅ Streamlit Cloud requires **PUBLIC** repos
- ✅ This landing page will be in a separate **PUBLIC** repo
- ✅ Your main "influencing" repo stays **PRIVATE**

## Step 1: Create New PUBLIC GitHub Repo

1. Go to https://github.com/new
2. Repository name: `sentinel-core-tiktok-landing` (or any name)
3. **Set to PUBLIC** (required for Streamlit)
4. **Don't** initialize with README, .gitignore, or license
5. Click **"Create repository"**

## Step 2: Push Landing Page to New Public Repo

After creating the repo, run these commands:

```bash
cd /home/josdak/solidity/influencing/social-media/tiktok-landing-page

# Add the new PUBLIC repo as remote
git remote add origin https://github.com/joedakwa/REPO_NAME.git

# Push to GitHub
git push -u origin main
```

**Replace `REPO_NAME` with your actual public repo name!**

## Step 3: Deploy to Streamlit Cloud

1. Go to https://share.streamlit.io
2. Click "New app"
3. Fill in:
   - **Repository**: `joedakwa/your-public-repo-name`
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL**: (optional) `sentinel-core-tiktok.streamlit.app`
4. Click "Deploy"

## Step 4: Add Secrets in Streamlit Cloud

After deployment:
1. Go to app **Settings** → **Secrets**
2. Add:
   ```toml
   TIKTOK_USERNAME = "joedakwa"
   TIKTOK_PIXEL_ID = "YOUR_PIXEL_ID_HERE"
   ```
3. Save

## What's in This Public Repo

Only the landing page files:
- `app.py` - Streamlit app
- `requirements.txt` - Dependencies
- `.streamlit/` - Config files (secrets.toml.example only)
- `README.md` - Basic info

**No sensitive data** - secrets are added in Streamlit Cloud, not in the repo!

---

**Your main "influencing" repo stays private, only this landing page is public for Streamlit!** ✅

