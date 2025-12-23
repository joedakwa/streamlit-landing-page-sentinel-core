# Complete TikTok Landing Page Setup Guide

## 🎯 The Strategy: How This Helps You "Blow Up" on TikTok

### The Full Flow

```
TikTok Ad (Your Video)
    ↓
User Clicks → Lands on Landing Page
    ↓
User Takes Action (Follow/Subscribe)
    ↓
Conversion Event Sent to TikTok
    ↓
TikTok Algorithm Learns: "This type of user converts"
    ↓
TikTok Finds More Similar Users
    ↓
Your Ads Show to Better Audiences
    ↓
More Conversions → Better Optimization
    ↓
More Followers → More Views → Growth!
```

### Why This Works

1. **TikTok Algorithm Optimization**: When users convert (follow, sign up), TikTok learns what types of users are valuable
2. **Lookalike Audiences**: After collecting 100+ emails, you can create lookalike audiences of your best converters
3. **Better Targeting**: TikTok finds more users similar to those who convert
4. **Lower Cost Per Follower**: As optimization improves, cost per follower decreases
5. **Scalable Growth**: System feeds itself - more conversions = better targeting = more growth

## 📋 What Action Should People Take?

### Primary Goal: **Follow on TikTok** ✅

**Why This is Best:**
- Direct path to follower growth
- Most valuable conversion for TikTok algorithm
- Users are already interested (they clicked your ad)
- Immediate action (no friction)

**How It Works:**
1. User sees your TikTok ad
2. Clicks ad → Lands on landing page
3. Reads your value props
4. Clicks "Follow on TikTok" button
5. Opens TikTok app/web → Follows you
6. TikTok tracks this as a conversion
7. TikTok finds more similar users
8. More followers come from better-targeted ads

### Secondary Goal: **Email Signup** ✅

**Why This is Good:**
- Builds your email list
- Creates lookalike audience data
- Allows retargeting
- Backup conversion goal

**How It Works:**
1. User signs up for email
2. Email stored (hashed for privacy)
3. After 100+ emails, export for lookalike audience
4. Upload to TikTok → Find similar users
5. Create new ad campaigns targeting lookalikes

## 🚀 Step-by-Step Setup

### Phase 1: Get TikTok Credentials (30 minutes)

#### Step 1.1: Create TikTok Ads Account

1. Go to [ads.tiktok.com](https://ads.tiktok.com)
2. Click "Create Ad" or "Sign Up"
3. Choose "Business" account
4. Complete registration
5. Verify your email

#### Step 1.2: Get TikTok Pixel ID

1. In TikTok Ads Manager, go to **Assets** → **Events** → **Manage** → **Web Events**
2. Click **"Set Up"** or **"Create Pixel"**
3. Copy your **Pixel ID** (looks like: `C1234567890ABCDEF`)
4. Save it - you'll need it for the landing page

#### Step 1.3: Get TikTok Access Token (Events API)

1. In TikTok Ads Manager, go to **Tools** → **Events API**
2. Click **"Generate Access Token"** or **"Create Token"**
3. Copy the access token (keep it secret - you won't see it again!)
4. Save it securely

#### Step 1.4: Get Your TikTok Username

Just your TikTok username (without @), e.g., `sentinelcore`

### Phase 2: Set Up Landing Page (1 hour)

#### Step 2.1: Install Dependencies

```bash
cd social-media/tiktok-landing-page
npm install
```

#### Step 2.2: Configure Environment

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` with your credentials:
   ```bash
   TIKTOK_PIXEL_ID=C1234567890ABCDEF  # From Step 1.2
   TIKTOK_ACCESS_TOKEN=your_token_here  # From Step 1.3
   TIKTOK_USERNAME=your_username  # From Step 1.4
   PORT=3000
   ```

#### Step 2.3: Update Landing Page

Edit `index.html`:

1. **Line 20**: Replace `YOUR_PIXEL_ID` with your actual Pixel ID
2. **Line 257**: Replace `YOUR_USERNAME` with your TikTok username

#### Step 2.4: Test Locally

```bash
npm start
```

Visit `http://localhost:3000` and test:
- ✅ Page loads correctly
- ✅ "Follow on TikTok" button works
- ✅ Email form works
- ✅ Check browser console for errors

#### Step 2.5: Deploy

Deploy to your hosting service:

**Option A: Vercel (Recommended - Free)**
```bash
npm install -g vercel
vercel
```

**Option B: Netlify**
- Connect GitHub repo
- Set build command: `npm install`
- Set publish directory: `public` (or root if serving HTML directly)

**Option C: Heroku**
```bash
heroku create your-app-name
git push heroku main
```

**Option D: Your Own Server**
- Upload files to server
- Run `npm start` or use PM2: `pm2 start server.js`

### Phase 3: Configure TikTok Campaign (1 hour)

#### Step 3.1: Create Campaign

1. In TikTok Ads Manager, click **"Create"**
2. **Campaign Type**: Website Conversions
3. **Campaign Name**: "Landing Page - Follower Growth"
4. **Budget**: Start with £5-10/day

#### Step 3.2: Create Ad Group

1. **Placement**: TikTok (recommended)
2. **Audience**: 
   - Interests: Blockchain, Cryptocurrency, AI, Entrepreneurship, Web3
   - Age: Your target age range
   - Location: Your target locations (UAE, global, etc.)
3. **Budget**: £5-10/day
4. **Optimization Goal**: Select **"Complete Registration"** or **"Click Button"**
5. **Bid Strategy**: Lowest Cost (automatic)

#### Step 3.3: Create Ad

1. **Creative**: Use videos from your 60-day script plan!
2. **Destination URL**: Your landing page URL
   ```
   https://yourdomain.com/?ttclid={ttclid}
   ```
   (TikTok automatically adds `ttclid` parameter)

3. **Call-to-Action**: "Learn More" or "Get Started"

#### Step 3.4: Enable Conversion Tracking

1. In ad group settings, under **"Optimization"**
2. Select **"Conversions"**
3. Choose conversion event: **"Click Button"** (for Follow button) or **"Complete Registration"** (for email)
4. Save campaign

### Phase 4: Test & Launch (30 minutes)

#### Step 4.1: Test Conversion Tracking

1. **Create test ad** with small budget (£2-3)
2. **Click on your ad** from a test device
3. **Visit landing page** - verify it loads
4. **Click "Follow on TikTok"** button
5. **Check TikTok Events Manager** - verify event is tracked
6. **Check server logs** - verify Events API received event

#### Step 4.2: Verify Pixel

1. Install [TikTok Pixel Helper](https://chrome.google.com/webstore) (Chrome extension)
2. Visit your landing page
3. Click "Follow" button
4. Check Pixel Helper - should show events firing

#### Step 4.3: Launch Campaign

1. Increase budget to your target (£5-10/day)
2. Monitor first 24-48 hours closely
3. Check conversion events are tracking
4. Let TikTok algorithm optimize (3-7 days)

### Phase 5: Optimize & Scale (Ongoing)

#### Week 1: Learning Phase

- Monitor daily
- Check conversion rates
- Verify events are tracking
- Let TikTok algorithm learn
- Don't make major changes yet

#### Week 2: Optimization

- Pause underperforming ads
- Scale winning creatives
- Adjust targeting if needed
- Increase budget on winners

#### Week 3+: Lookalike Audiences

1. **Collect 100+ emails** (from landing page)
2. **Export audience**:
   ```bash
   GET /api/export/lookalike
   ```
3. **Upload to TikTok**:
   - TikTok Ads Manager → **Audiences** → **Create** → **Lookalike**
   - Upload CSV file
   - Select similarity (1-3% recommended)
4. **Create new campaign** targeting lookalike audience
5. **Compare performance** - lookalikes often perform better

## 📊 Tracking & Analytics

### View Landing Page Stats

```bash
GET /api/stats
```

Returns:
- Total emails collected
- Total events tracked
- Events by type
- Latest emails and events

### Check TikTok Events

1. TikTok Ads Manager → **Events** → **Event Details**
2. See all tracked events
3. Monitor conversion rates
4. Check attribution

### Monitor Campaign Performance

1. TikTok Ads Manager → **Campaigns**
2. Check metrics:
   - Impressions
   - Clicks
   - Conversion rate
   - Cost per conversion
   - Cost per follower

## 🎯 Conversion Goals Explained

### Primary: Follow Button Click

**Why:** Direct path to follower growth

**Event:** `ClickButton`

**How TikTok Uses It:**
- Finds users similar to those who clicked follow
- Optimizes ad delivery to show to likely followers
- Improves targeting automatically

### Secondary: Email Signup

**Why:** Builds email list + lookalike audience data

**Event:** `CompleteRegistration`

**How TikTok Uses It:**
- Tracks engaged users
- Helps with optimization
- Creates data for lookalike audiences

### Bonus: Page Engagement

**Why:** Measures quality traffic

**Event:** `StayTime` (30+ seconds)

**How TikTok Uses It:**
- Identifies engaged users
- Helps algorithm understand quality
- Improves ad relevance

## 💡 Best Practices

### Landing Page

1. **Clear Value Proposition**: State what users get
2. **Single Primary CTA**: Focus on "Follow on TikTok"
3. **Mobile Optimized**: Most TikTok users are on mobile
4. **Fast Loading**: < 2 seconds load time
5. **Trust Signals**: Show social proof if possible

### Campaign Strategy

1. **Start Small**: £5-10/day initially
2. **Test Creatives**: Use different videos from your 60-day plan
3. **Monitor Closely**: First week is critical
4. **Scale Winners**: Increase budget on best performers
5. **Use Lookalikes**: After collecting data, use lookalike audiences

### Content Strategy

1. **Use Your Scripts**: Your 60-day script plan is perfect for ads
2. **Hook Early**: First 3 seconds are crucial
3. **Clear CTA**: Tell users what to do
4. **Test Variations**: Try different angles
5. **Refresh Regularly**: Update creatives monthly

## 🚨 Common Issues & Solutions

### Conversions Not Tracking

**Problem:** Events not showing in TikTok

**Solutions:**
- Verify Pixel ID is correct
- Check Access Token is valid
- Ensure events are being sent (check server logs)
- Wait 24-48 hours (delay is normal)
- Use TikTok Pixel Helper to debug

### Low Conversion Rate

**Problem:** Users not clicking Follow button

**Solutions:**
- Improve landing page value proposition
- Make CTA more prominent
- Test different ad creatives
- Improve ad targeting
- Check landing page load speed

### High Cost Per Conversion

**Problem:** Expensive to get followers

**Solutions:**
- Let algorithm optimize (3-7 days)
- Improve ad creative quality
- Refine audience targeting
- Use lookalike audiences
- Test different landing page variations

### Lookalike Audience Not Working

**Problem:** Can't create lookalike or it's not performing

**Solutions:**
- Need minimum 100 emails (1000+ recommended)
- Ensure email format is correct (hashed)
- Check CSV export format
- Wait for TikTok to process (24-48 hours)
- Try different similarity percentages (1-3% best)

## 📈 Expected Results

### Week 1-2: Learning Phase
- 10-50 followers from ads
- Algorithm learning your audience
- Higher cost per follower
- Conversion rate stabilizing

### Week 3-4: Optimization Phase
- 50-200 followers from ads
- Algorithm improving targeting
- Lower cost per follower
- Better conversion rates

### Month 2+: Scaling Phase
- 200-1000+ followers from ads
- Lookalike audiences performing
- Optimized cost per follower
- Consistent growth

**Note:** Results vary based on:
- Ad budget
- Creative quality
- Landing page optimization
- Audience targeting
- Niche competition

## 🎉 Success Checklist

- [ ] TikTok Ads account created
- [ ] TikTok Pixel ID obtained
- [ ] TikTok Access Token obtained
- [ ] Landing page deployed
- [ ] Pixel and Events API configured
- [ ] Test campaign run successfully
- [ ] Conversion tracking verified
- [ ] First real campaign launched
- [ ] Monitoring dashboard set up
- [ ] 100+ emails collected (for lookalike)
- [ ] Lookalike audience created
- [ ] Scaling strategy in place

## 📚 Additional Resources

- [TikTok Pixel Setup](https://ads.tiktok.com/help/article?aid=10028)
- [TikTok Events API](https://ads.tiktok.com/help/article?aid=10047)
- [Lookalike Audiences](https://ads.tiktok.com/help/article?aid=9579)
- [Campaign Optimization](https://ads.tiktok.com/help/article?aid=9501)

## 🆘 Need Help?

1. Check server logs for errors
2. Use TikTok Pixel Helper for debugging
3. Review TikTok Events Manager for event tracking
4. Check `/api/stats` endpoint for landing page data
5. Verify all credentials are correct

---

**Remember:** This is a system, not a quick fix. Give it 2-4 weeks to optimize, then scale what works. Consistency and patience are key!

