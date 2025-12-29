#!/usr/bin/env python3
"""
Quick script to export emails from database
Run: python3 export_emails.py
"""
from email_backend import EmailStorage
import sys

def main():
    storage = EmailStorage()
    
    # Get count
    count = storage.get_count()
    print(f"\n📧 Total Subscribers: {count}\n")
    
    if count == 0:
        print("No emails found in database.")
        return
    
    # Get all emails
    emails = storage.get_all_emails()
    
    # Print to console
    print("Email List:")
    print("-" * 60)
    for email_data in emails:
        print(f"{email_data['email']:<40} {email_data['subscribed_at']}")
    print("-" * 60)
    
    # Export to CSV
    csv_path = storage.export_to_csv()
    print(f"\n✅ Exported to: {csv_path}")
    print(f"   You can open this file in Excel/Sheets or import to email marketing tools\n")

if __name__ == "__main__":
    main()

