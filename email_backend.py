"""
Simple Email Storage Backend for TikTok Landing Page
Stores email addresses in SQLite database
Optional: Integration with Brevo (formerly Sendinblue) for email campaigns
"""
import sqlite3
import os
from datetime import datetime
from typing import Optional
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database path
DB_PATH = os.path.join(os.path.dirname(__file__), "emails.db")

class EmailStorage:
    """Simple email storage using SQLite"""
    
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self._init_database()
    
    def _init_database(self):
        """Initialize database table if it doesn't exist"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                subscribed_at TEXT NOT NULL,
                source TEXT DEFAULT 'tiktok_landing_page',
                unsubscribed INTEGER DEFAULT 0
            )
        """)
        conn.commit()
        conn.close()
        logger.info(f"Database initialized at {self.db_path}")
    
    def add_email(self, email: str, source: str = "tiktok_landing_page") -> tuple[bool, str]:
        """
        Add email to database
        Returns: (success: bool, message: str)
        """
        if not email or "@" not in email or "." not in email:
            return False, "Invalid email address"
        
        email = email.lower().strip()
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Check if email already exists
            cursor.execute("SELECT id FROM subscribers WHERE email = ?", (email,))
            if cursor.fetchone():
                conn.close()
                return False, "Email already subscribed"
            
            # Insert new email
            cursor.execute("""
                INSERT INTO subscribers (email, subscribed_at, source)
                VALUES (?, ?, ?)
            """, (email, datetime.now().isoformat(), source))
            
            conn.commit()
            conn.close()
            
            logger.info(f"Email added: {email}")
            return True, "Email added successfully"
            
        except sqlite3.Error as e:
            logger.error(f"Database error: {e}")
            return False, f"Database error: {str(e)}"
    
    def get_all_emails(self) -> list[dict]:
        """Get all subscribed emails"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                SELECT email, subscribed_at, source 
                FROM subscribers 
                WHERE unsubscribed = 0
                ORDER BY subscribed_at DESC
            """)
            rows = cursor.fetchall()
            conn.close()
            
            return [
                {
                    "email": row[0],
                    "subscribed_at": row[1],
                    "source": row[2]
                }
                for row in rows
            ]
        except sqlite3.Error as e:
            logger.error(f"Database error: {e}")
            return []
    
    def get_count(self) -> int:
        """Get total subscriber count"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM subscribers WHERE unsubscribed = 0")
            count = cursor.fetchone()[0]
            conn.close()
            return count
        except sqlite3.Error as e:
            logger.error(f"Database error: {e}")
            return 0
    
    def export_to_csv(self, filepath: Optional[str] = None) -> str:
        """Export all emails to CSV file"""
        import csv
        
        if filepath is None:
            filepath = os.path.join(os.path.dirname(__file__), "subscribers_export.csv")
        
        emails = self.get_all_emails()
        
        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['email', 'subscribed_at', 'source'])
            writer.writeheader()
            writer.writerows(emails)
        
        logger.info(f"Exported {len(emails)} emails to {filepath}")
        return filepath


# Optional: Brevo (Sendinblue) integration for email campaigns
class BrevoIntegration:
    """Integration with Brevo (formerly Sendinblue) for email marketing"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("BREVO_API_KEY")
        self.base_url = "https://api.brevo.com/v3"
    
    def add_contact(self, email: str, list_id: int = None) -> bool:
        """
        Add contact to Brevo
        Requires: BREVO_API_KEY environment variable
        """
        if not self.api_key:
            logger.warning("Brevo API key not configured")
            return False
        
        try:
            import requests
            
            headers = {
                "accept": "application/json",
                "api-key": self.api_key,
                "content-type": "application/json"
            }
            
            data = {"email": email.lower().strip()}
            if list_id:
                data["listIds"] = [list_id]
            
            response = requests.post(
                f"{self.base_url}/contacts",
                json=data,
                headers=headers
            )
            
            if response.status_code in [201, 204]:
                logger.info(f"Contact added to Brevo: {email}")
                return True
            elif response.status_code == 400 and "already exists" in response.text.lower():
                logger.info(f"Contact already exists in Brevo: {email}")
                return True
            else:
                logger.error(f"Brevo API error: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            logger.error(f"Error adding contact to Brevo: {e}")
            return False


# Usage example
if __name__ == "__main__":
    storage = EmailStorage()
    
    # Test adding email
    success, message = storage.add_email("test@example.com")
    print(f"Add email: {success} - {message}")
    
    # Get count
    count = storage.get_count()
    print(f"Total subscribers: {count}")
    
    # Export to CSV
    csv_path = storage.export_to_csv()
    print(f"Exported to: {csv_path}")

