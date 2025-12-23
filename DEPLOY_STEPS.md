# Deploy Your Streamlit Landing Page - Step by Step

## ✅ What We Changed

- **Primary CTA**: "Sign Up for Free Newsletter" (collects emails, tracks conversions)
- **Secondary CTA**: "Follow on TikTok" (bonus option)
- **Conversion Tracking**: Newsletter signups track as "CompleteRegistration" event

## 🚀 Quick Deploy Steps

### Step 1: Get TikTok Pixel ID (Required!)

1. Go to **TikTok Ads Manager**
2. Navigate to: **Assets** → **Events** → **Manage** → **Web Events**
3. Click **"Set Up"** or **"Create Pixel"** (if you haven't)
4. Copy your **Pixel ID** (looks like: `C1234567890ABCDEF`)

### Step 2: Update Secrets File

Edit `.streamlit/secrets.toml`:

```toml
TIKTOK_USERNAME = "joedakwa"  # Your actual TikTok username
TIKTOK_PIXEL_ID = "YOUR_ACTUAL_PIXEL_ID_HERE"  # Paste your Pixel ID
```

### Step 3: Test Locally (Optional)

```bash
cd social-media/tiktok-landing-page
streamlit run app.py
```

Visit: http://localhost:8501

### Step 4: Deploy to Streamlit Cloud

#### Option A: Deploy via GitHub (Recommended)

1. **Initialize Git** (if not already):
   ```bash
   cd social-media/tiktok-landing-page
   git init
   git add .
   git commit -m "Add TikTok landing page with newsletter signup"
   ```

2. **Push to GitHub**:
   - Create a new repo on GitHub
   - Push your code:
   ```bash
   git remote add origin https://github.com/yourusername/yourrepo.git
   git push -u origin main
   ```

3. **Deploy on Streamlit Cloud**:
   - Go to https://share.streamlit.io
   - Sign in with GitHub
   - Click **"New app"**
   - Select your repository
   - Main file path: `app.py`
   - Branch: `main`
   - Click **"Deploy"**

4. **Add Secrets in Streamlit Cloud**:
   - In your app settings → **"Secrets"**
   - Add:
     ```toml
     TIKTOK_USERNAME = "joedakwa"
     TIKTOK_PIXEL_ID = "YOUR_ACTUAL_PIXEL_ID"
     ```
   - Click **"Save"**

5. **Get Your URL**:
   - Your app will be live at: `https://your-app-name.streamlit.app`
   - **Copy this URL** - this is your landing page URL!

#### Option B: Quick Deploy (Streamlit CLI)

```bash
cd social-media/tiktok-landing-page
streamlit deploy app.py
```

Follow the prompts and add secrets when asked.

### Step 5: Use in TikTok Ads

1. Go back to **TikTok Ads Manager**
2. In your campaign setup, **Destination URL** field:
3. Paste your Streamlit URL: `https://your-app-name.streamlit.app`
4. Continue with campaign setup

## 🎯 How It Works

1. User clicks TikTok ad
2. Lands on your Streamlit landing page
3. Sees value propositions
4. **Primary Action**: Signs up for newsletter (tracks conversion!)
5. **Secondary Action**: Can also follow on TikTok
6. TikTok algorithm learns from conversions
7. Finds more similar users
8. More signups = Better targeting = Growth!

## ✅ What Happens on Signup

- Email is collected (stored in session state)
- TikTok Pixel tracks "CompleteRegistration" event
- Success message shown to user
- Conversion data sent to TikTok for optimization

## 📊 Conversion Event

TikTok tracks: **CompleteRegistration**
- Event name: Newsletter Signup
- Value: 1
- Used for algorithm optimization
- Enables lookalike audiences later

## 🔧 Next Steps

1. ✅ Deploy to Streamlit Cloud
2. ✅ Get your Streamlit URL
3. ✅ Update TikTok campaign with URL
4. ✅ Launch campaign
5. ✅ Monitor conversions in TikTok Events Manager

## 💡 Pro Tips

- **Test first**: Visit your Streamlit URL and test the signup form
- **Check Pixel**: Verify TikTok Pixel is loading (browser console)
- **Monitor**: Check TikTok Events Manager after 24 hours
- **Optimize**: After 50+ conversions, TikTok algorithm will optimize

---

**Your Streamlit URL is your landing page URL for TikTok ads!** 🚀

