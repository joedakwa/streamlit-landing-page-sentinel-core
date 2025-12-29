# Email Backend Setup Guide

## ✅ What's Included

A simple, persistent email storage system that:
- ✅ Stores emails in SQLite database (local file, no server needed)
- ✅ Prevents duplicate emails
- ✅ Optional: Export to CSV for email marketing tools
- ✅ Optional: Integration with Brevo (formerly Sendinblue) for automated email campaigns

## 📁 Files Created

- `email_backend.py` - Email storage backend
- `emails.db` - SQLite database (created automatically, **DO NOT commit to git**)

## 🚀 Quick Start

### 1. The backend is already integrated!

Your `app.py` now uses the email backend automatically. Emails are stored in `emails.db`.

### 2. View Your Subscribers

**Option A: Use Python script**
```bash
cd /home/josdak/solidity/influencing/social-media/tiktok-landing-page
python3 -c "from email_backend import EmailStorage; s = EmailStorage(); print(f'Total subscribers: {s.get_count()}'); [print(e['email']) for e in s.get_all_emails()[:10]]"
```

**Option B: Export to CSV**
```bash
python3 email_backend.py
# This creates subscribers_export.csv
```

**Option C: Create admin page** (see below)

### 3. Set Up Email Campaigns (Optional)

#### Option A: Export to CSV & Use Any Email Tool
1. Run: `python3 email_backend.py`
2. Download `subscribers_export.csv`
3. Import into Mailchimp, ConvertKit, SendGrid, etc.

#### Option B: Use Brevo (Free Tier: 300 emails/day)

1. **Sign up**: https://www.brevo.com (free tier available)
2. **Get API key**: Settings → API Keys → Generate
3. **Set environment variable**:
   ```bash
   export BREVO_API_KEY="your_api_key_here"
   ```
   Or in Streamlit Secrets (`.streamlit/secrets.toml`):
   ```toml
   BREVO_API_KEY = "your_api_key_here"
   ```
4. **Integrate** (optional - modify `app.py`):
   ```python
   from email_backend import BrevoIntegration
   brevo = BrevoIntegration()
   brevo.add_contact(email)
   ```

## 📊 Database Schema

```sql
subscribers (
    id INTEGER PRIMARY KEY,
    email TEXT UNIQUE,
    subscribed_at TEXT,
    source TEXT,
    unsubscribed INTEGER DEFAULT 0
)
```

## 🔍 View Emails Locally

**Simple Python script:**
```python
from email_backend import EmailStorage

storage = EmailStorage()
print(f"Total: {storage.get_count()} subscribers")
for email_data in storage.get_all_emails():
    print(f"{email_data['email']} - {email_data['subscribed_at']}")
```

## 📧 Email Campaign Recommendations

### For Busy Developers (Minimal Time)

**1. Use Brevo Free Tier** (300 emails/day)
- Free tier is perfect for < 300 subscribers
- Drag-and-drop email builder
- Automation workflows
- Analytics included

**2. Weekly Newsletter Template**
- Pre-write template in Brevo
- Weekly: Export CSV → Import to Brevo → Send
- Or automate with Brevo API (code once, runs automatically)

**3. Simple Email Campaign Ideas**
- Weekly roundup: Top blockchain/AI insights
- Product updates: What you're building
- Educational: One concept explained simply
- Case studies: Problems you've solved

### Email Campaign Frequency

**Recommended for busy founders:**
- **Monthly**: Minimum viable (keeps list warm)
- **Bi-weekly**: Good balance
- **Weekly**: Optimal (if you have content)

**Content ideas (5 min to create):**
- "This week in blockchain security"
- "3 things I learned building..."
- "One smart contract vulnerability you should know"
- Link to your TikTok videos (repurpose content!)

## 🎯 ROI Analysis

**Your current metrics:**
- Cost per email: ~$0.014 USD (0.05 AED)
- 2,324 landing page views = potential subscribers

**Email marketing ROI:**
- Average email open rate: 20-25%
- Average click rate: 2-5%
- If you convert 1% to customers at $100 value = $2,324 potential revenue
- **Your cost**: $31 USD

**Email is your highest-ROI channel** ✅

## 🔒 Privacy & Compliance

**GDPR/Privacy considerations:**
1. ✅ You collect emails (compliant)
2. ⚠️ Add unsubscribe link to emails (required)
3. ⚠️ Privacy policy link on landing page (recommended)
4. ⚠️ Don't spam - send valuable content

**Simple unsubscribe flow:**
- Add unsubscribe link in email footer
- Link to: `your-domain.com/unsubscribe?email={email}`
- Mark as unsubscribed in database

## 📈 Next Steps

1. **Today**: Backend is live, emails are being saved ✅
2. **This week**: Export CSV, see how many subscribers you have
3. **This month**: Set up Brevo (or other email tool), send first newsletter
4. **Ongoing**: Weekly/monthly newsletter to nurture leads

## 🛠️ Advanced: Admin Dashboard (Optional)

Want to view subscribers in Streamlit? Create `admin.py`:

```python
import streamlit as st
from email_backend import EmailStorage

st.title("📧 Subscriber Management")
storage = EmailStorage()

st.metric("Total Subscribers", storage.get_count())

if st.button("Export to CSV"):
    csv_path = storage.export_to_csv()
    st.success(f"Exported to {csv_path}")

emails = storage.get_all_emails()
st.dataframe(emails)
```

Run: `streamlit run admin.py`

## ❓ FAQ

**Q: Where are emails stored?**
A: SQLite database file (`emails.db`) in the same folder as `app.py`

**Q: Is this secure?**
A: Yes, for basic use. SQLite is file-based, no network access. For production, consider PostgreSQL + encryption.

**Q: Can I use Mailchimp instead of Brevo?**
A: Yes! Export CSV and import manually, or use Mailchimp API (similar to Brevo integration)

**Q: What if Streamlit Cloud deployment?**
A: SQLite files are ephemeral on Streamlit Cloud. Use Streamlit Secrets + external database (PostgreSQL) or export CSV regularly.

**Q: How do I backup emails?**
A: Run `export_to_csv()` regularly, or backup `emails.db` file

