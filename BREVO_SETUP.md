# 🚀 Brevo Setup Guide (Easiest Email Storage)

## Why Brevo?
- ✅ **Easiest solution** - Emails go directly to your email marketing platform
- ✅ **No manual imports** - All emails automatically in Brevo
- ✅ **Ready for campaigns** - Can send emails immediately
- ✅ **Free tier**: 300 emails/day (plenty for you)
- ✅ **Works on Streamlit Cloud** - Persistent storage
- ✅ **Analytics built-in** - See opens, clicks, etc.

## Quick Setup (5 Minutes)

### Step 1: Sign Up for Brevo (Free)
1. Go to: https://www.brevo.com
2. Click "Sign Up Free"
3. Create account (use your business email)
4. Verify your email

### Step 2: Get Your API Key
1. Log into Brevo dashboard
2. Go to: **Settings** → **API Keys** (or: https://app.brevo.com/settings/keys/api)
3. Click **Generate a new API key**
4. Give it a name: "TikTok Landing Page"
5. **Copy the API key** (you'll only see it once!)

### Step 3: Add to Streamlit Secrets

**On Streamlit Cloud:**
1. Go to your Streamlit Cloud dashboard
2. Click on your app
3. Go to **Settings** → **Secrets**
4. Add this:
   ```toml
   BREVO_API_KEY = "your_api_key_here_paste_it"
   ```
5. Click **Save**

**For Local Testing:**
1. Edit `.streamlit/secrets.toml` (create if doesn't exist)
2. Add:
   ```toml
   BREVO_API_KEY = "your_api_key_here"
   ```

### Step 4: That's It! 🎉

Your landing page will now:
- ✅ Save emails to Brevo automatically
- ✅ Also save to local database (backup)
- ✅ No manual work needed

## View Your Emails

### In Brevo Dashboard:
1. Go to: https://app.brevo.com
2. Click **Contacts** → **All contacts**
3. All subscriber emails are there!

### Send Your First Email Campaign:
1. In Brevo: **Email** → **Campaigns**
2. Click **Create an email**
3. Choose template or create new
4. Select your contact list
5. Send!

## Optional: Create a Contact List

If you want to organize subscribers:
1. In Brevo: **Contacts** → **Lists**
2. Click **Create a list**
3. Name it: "TikTok Newsletter Subscribers"
4. Get the List ID (from URL or list settings)
5. Add to Streamlit Secrets (optional):
   ```toml
   BREVO_API_KEY = "your_key"
   BREVO_LIST_ID = "2"  # Your list ID number
   ```

## Free Tier Limits

**Brevo Free Plan:**
- ✅ 300 emails/day
- ✅ Unlimited contacts
- ✅ Email campaigns
- ✅ Automation workflows
- ✅ Analytics

**This is perfect for you** - unless you're sending 300+ emails per day, you're covered!

## Troubleshooting

**Emails not appearing in Brevo?**
- Check API key is correct in Streamlit Secrets
- Check Brevo dashboard → Contacts
- Check Streamlit app logs for errors

**Want to test locally first?**
```bash
python3 -c "from email_backend import BrevoIntegration; b = BrevoIntegration(); print('Working!' if b.add_contact('test@example.com') else 'Check API key')"
```

## Next Steps

1. ✅ Set up Brevo account
2. ✅ Add API key to Streamlit Secrets
3. ✅ Test by subscribing on your landing page
4. ✅ Check Brevo dashboard - email should appear!
5. ✅ When ready: Create and send email campaigns

No manual imports needed - everything is automatic! 🎉

