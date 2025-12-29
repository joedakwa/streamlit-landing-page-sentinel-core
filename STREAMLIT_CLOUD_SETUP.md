# ⚠️ Important: Email Storage on Streamlit Cloud

## The Problem

**Streamlit Cloud uses ephemeral storage** - this means:
- ❌ SQLite database files (`emails.db`) are **deleted** when the app restarts
- ❌ Emails collected won't persist between deployments
- ❌ You'll lose emails if you don't export them regularly

## Solutions

### Option 1: Export Emails Regularly (Simplest)

**Automate daily/weekly exports:**
1. Run export script locally: `python3 export_emails.py`
2. Or use Streamlit admin dashboard: `streamlit run admin.py`
3. Backup CSV file to Google Drive/Dropbox

**Best for:** Testing, low volume (< 100 subscribers/week)

### Option 2: External Database (Recommended for Production)

Use a hosted database that persists:

**A. PostgreSQL (Free tier available)**
- **Render.com** - Free PostgreSQL database
- **Supabase** - Free tier with PostgreSQL
- **Neon** - Free serverless PostgreSQL

**B. Update code to use PostgreSQL:**
```python
# email_backend.py - add PostgreSQL support
import psycopg2
import os

DATABASE_URL = os.getenv("DATABASE_URL")  # From Streamlit Secrets
```

**Best for:** Production, high volume

### Option 3: Cloud Storage (Simple Alternative)

Store emails in cloud storage instead of database:

**A. Google Sheets API**
- Export emails to Google Sheet automatically
- Easy to view/manage
- Free for reasonable usage

**B. AWS S3 / Google Cloud Storage**
- Save CSV files to cloud storage
- Cheap/free for small files

**Best for:** Medium volume, want simplicity

### Option 4: Email Service Integration (Easiest for Email Marketing)

Integrate directly with email marketing service:

**A. Brevo (Sendinblue) API**
- Emails go directly to Brevo
- No local storage needed
- Free tier: 300 emails/day
- Built-in email campaigns

**B. Mailchimp API**
- Similar to Brevo
- Paid plans start at $0/month (limited features)

**Best for:** If you're planning to send email campaigns anyway

## Recommended Approach for Your Situation

Since you're:
- ✅ Running ads (getting traffic)
- ✅ Want to send email campaigns eventually
- ✅ Don't want to manage infrastructure

**I recommend: Option 4 (Brevo Integration)**

### Setup Brevo Integration:

1. **Sign up**: https://www.brevo.com (free)
2. **Get API key**: Settings → API Keys
3. **Add to Streamlit Secrets**:
   ```toml
   BREVO_API_KEY = "your_api_key_here"
   BREVO_LIST_ID = "1"  # Optional: default list ID
   ```
4. **Update code** to use Brevo (I can help with this)

**Benefits:**
- ✅ Emails stored in Brevo (persistent)
- ✅ Ready for email campaigns
- ✅ Free tier is generous (300 emails/day)
- ✅ Analytics built-in
- ✅ No database management needed

## Current Setup (SQLite) - Use Cases

**Good for:**
- ✅ Local development/testing
- ✅ Temporary storage before export
- ✅ Learning/testing the system

**Not good for:**
- ❌ Streamlit Cloud production (data loss)
- ❌ Long-term storage
- ❌ High volume

## Quick Export Commands

**Export emails right now:**
```bash
cd /home/josdak/solidity/influencing/social-media/tiktok-landing-page
python3 export_emails.py
```

**View in admin dashboard:**
```bash
streamlit run admin.py
```

**View count only:**
```bash
python3 -c "from email_backend import EmailStorage; print(f'Subscribers: {EmailStorage().get_count()}')"
```

## What Should You Do Now?

1. **Test locally first** - Make sure it works
2. **Export existing emails** (if any): `python3 export_emails.py`
3. **Decide on production solution**:
   - **Simple**: Use Brevo API (recommended)
   - **Advanced**: PostgreSQL database
   - **Manual**: Export CSV regularly

Would you like me to:
- Set up Brevo integration (emails go directly to Brevo)?
- Set up PostgreSQL database connection?
- Keep SQLite but add automated CSV exports?

