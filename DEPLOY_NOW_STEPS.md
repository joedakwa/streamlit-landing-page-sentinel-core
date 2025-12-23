# Deploy NOW - Simple Steps

## What You Need First

**Get your TikTok Pixel ID:**
1. Go to TikTok Ads Manager
2. **Assets** → **Events** → **Manage** → **Web Events**
3. Click **"Set Up"** or **"Create Pixel"**
4. Copy the Pixel ID (looks like: `C1234567890ABCDEF`)

## Update Secrets

Edit `.streamlit/secrets.toml` and replace `YOUR_PIXEL_ID_HERE` with your actual Pixel ID.

## Deploy Options

### Option 1: Streamlit Cloud (Easiest - 2 minutes)

1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click **"New app"**
4. Connect your GitHub repo OR upload files directly
5. Main file: `app.py`
6. Add secrets (TIKTOK_USERNAME and TIKTOK_PIXEL_ID)
7. Deploy!

### Option 2: Quick Test Locally

```bash
cd social-media/tiktok-landing-page
streamlit run app.py
```

Then visit http://localhost:8501

## Once Deployed

1. Copy your Streamlit app URL (e.g., `https://your-app.streamlit.app`)
2. Use it as Destination URL in TikTok Ads Manager
3. Launch your campaign!

---

**The newsletter signup is now the primary CTA - perfect for collecting emails and tracking conversions!** 📧

