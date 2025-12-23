# Quick Start - TikTok Landing Page

## 5-Minute Setup

### 1. Install

```bash
cd social-media/tiktok-landing-page
npm install
```

### 2. Get TikTok Credentials

**TikTok Pixel ID:**
- TikTok Ads Manager → Assets → Events → Manage → Web Events
- Copy Pixel ID

**TikTok Access Token:**
- TikTok Ads Manager → Tools → Events API
- Generate token → Copy

### 3. Configure

```bash
cp .env.example .env
```

Edit `.env`:
```bash
TIKTOK_PIXEL_ID=your_pixel_id
TIKTOK_ACCESS_TOKEN=your_token
TIKTOK_USERNAME=your_username
```

Edit `index.html`:
- Line 20: Replace `YOUR_PIXEL_ID`
- Line 257: Replace `YOUR_USERNAME`

### 4. Run

```bash
npm start
```

Visit: http://localhost:3000

### 5. Deploy

**Vercel (Free):**
```bash
npm install -g vercel
vercel
```

**Or use your preferred hosting**

## Full Setup Guide

See `SETUP_GUIDE.md` for complete instructions.

## What This Does

✅ Landing page for TikTok ads  
✅ Tracks Follow button clicks  
✅ Tracks email signups  
✅ Feeds data to TikTok for optimization  
✅ Exports emails for lookalike audiences  

## The Flow

```
TikTok Ad → Landing Page → User Clicks Follow → TikTok Tracks Conversion → 
TikTok Finds Similar Users → Better Targeting → More Followers!
```

