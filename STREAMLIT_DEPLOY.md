# Streamlit Landing Page - Quick Deploy Guide

## ✅ Why Streamlit?

- **Free hosting** on Streamlit Cloud
- **Easy to update** (just edit Python file)
- **Professional** looking
- **Built-in forms** and interactivity
- **Easy to extend** (add features later)

## 🚀 Quick Deploy (5 Minutes)

### Step 1: Get Your TikTok Credentials

1. **TikTok Username**: Your TikTok handle (e.g., `joedakwa`)
2. **TikTok Pixel ID**: 
   - TikTok Ads Manager → **Assets** → **Events** → **Manage** → **Web Events**
   - Create or copy Pixel ID

### Step 2: Configure Streamlit Secrets

Create `.streamlit/secrets.toml` file:

```toml
TIKTOK_USERNAME = "joedakwa"  # Your TikTok username
TIKTOK_PIXEL_ID = "C1234567890ABCDEF"  # Your Pixel ID
```

**OR** set environment variables when deploying.

### Step 3: Test Locally (Optional)

```bash
cd social-media/tiktok-landing-page
pip install streamlit
streamlit run app.py
```

Visit: http://localhost:8501

### Step 4: Deploy to Streamlit Cloud

#### Option A: Deploy from GitHub (Recommended)

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Add TikTok landing page"
   git remote add origin https://github.com/yourusername/yourrepo.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**:
   - Go to https://share.streamlit.io
   - Click "New app"
   - Connect your GitHub repo
   - Select branch: `main`
   - Main file: `app.py`
   - Click "Deploy"

3. **Add Secrets**:
   - In Streamlit Cloud → Settings → Secrets
   - Add:
     ```toml
     TIKTOK_USERNAME = "joedakwa"
     TIKTOK_PIXEL_ID = "YOUR_PIXEL_ID"
     ```

4. **Get Your URL**:
   - Streamlit Cloud gives you: `https://your-app-name.streamlit.app`
   - Use this as your TikTok ad destination!

#### Option B: Deploy with Streamlit CLI

```bash
streamlit deploy app.py
```

### Step 5: Use in TikTok Ads

Set your destination URL to your Streamlit app URL:
```
https://your-app-name.streamlit.app
```

Or if you have custom domain:
```
https://thesentinelcore.com/tiktok
```

## 🎯 What Happens When Users Visit

1. User clicks TikTok ad
2. Lands on your Streamlit app
3. Sees value propositions
4. Clicks "Follow on TikTok" button
5. TikTok Pixel tracks conversion
6. User redirected to your TikTok profile
7. Algorithm learns and optimizes

## 📊 Features Included

✅ TikTok Pixel integration  
✅ Follow button with conversion tracking  
✅ Email signup form with conversion tracking  
✅ Mobile-responsive design  
✅ Professional styling  
✅ Conversion events sent to TikTok  

## 🔧 Customization

Edit `app.py` to:
- Change colors/styling
- Add more sections
- Modify value propositions
- Add more CTAs
- Integrate with backend APIs

## 📝 Notes

- **Free tier**: Streamlit Cloud is free (some limits)
- **Custom domain**: Can add custom domain if needed
- **Backend**: Can add database integration later
- **Email service**: Can integrate SendGrid/Mailchimp later

## 🆘 Troubleshooting

**Pixel not tracking?**
- Check Pixel ID is correct in secrets
- Verify pixel code is loading (check browser console)
- Wait 24-48 hours for events to appear in TikTok

**Styling issues?**
- Clear browser cache
- Check Streamlit version matches requirements.txt

**Deployment issues?**
- Check secrets are set correctly
- Verify requirements.txt includes streamlit
- Check app.py has no syntax errors

## ✨ Next Steps

1. Deploy to Streamlit Cloud
2. Test the landing page
3. Add URL to TikTok campaign
4. Monitor conversions
5. Optimize based on data

---

**Your Streamlit app URL will be your landing page URL for TikTok ads!** 🚀

