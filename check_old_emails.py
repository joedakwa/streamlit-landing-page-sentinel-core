#!/usr/bin/env python3
"""
Check if there are any emails in local database
Note: session_state emails are lost (ephemeral memory)
This only checks the SQLite database (if it exists)
"""
import os
from email_backend import EmailStorage

db_path = os.path.join(os.path.dirname(__file__), "emails.db")

if os.path.exists(db_path):
    print("📧 Checking local database for emails...\n")
    storage = EmailStorage()
    count = storage.get_count()
    emails = storage.get_all_emails()
    
    if count > 0:
        print(f"Found {count} emails in database:\n")
        for email_data in emails:
            print(f"  - {email_data['email']} ({email_data['subscribed_at']})")
        
        # Export option
        csv_path = storage.export_to_csv()
        print(f"\n✅ Exported to: {csv_path}")
    else:
        print("No emails found in database.")
else:
    print("❌ No database file found.")
    print("This means:")
    print("  - No one has subscribed since the new code was deployed")
    print("  - OR the database file doesn't exist yet")

print("\n⚠️  Note about session_state emails:")
print("   Emails stored in session_state (old code) are LOST because:")
print("   - session_state only exists in browser memory during a session")
print("   - Each user has their own separate session")
print("   - Data is deleted when browser closes or server restarts")
print("   - We cannot recover those emails, unfortunately")

