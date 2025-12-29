"""
Simple Admin Dashboard for Viewing Subscribers
Run: streamlit run admin.py
"""
import streamlit as st
from email_backend import EmailStorage
import pandas as pd

st.set_page_config(
    page_title="Subscriber Management",
    page_icon="📧",
    layout="wide"
)

st.title("📧 Subscriber Management Dashboard")

# Initialize storage
storage = EmailStorage()

# Metrics
col1, col2, col3 = st.columns(3)
total_count = storage.get_count()
col1.metric("Total Subscribers", total_count)

# Get all emails
emails = storage.get_all_emails()
if emails:
    # Convert to DataFrame
    df = pd.DataFrame(emails)
    df['subscribed_at'] = pd.to_datetime(df['subscribed_at'])
    
    # Today's signups
    today_count = len(df[df['subscribed_at'].dt.date == pd.Timestamp.today().date()])
    col2.metric("Today's Signups", today_count)
    
    # This week's signups
    week_ago = pd.Timestamp.today() - pd.Timedelta(days=7)
    week_count = len(df[df['subscribed_at'] >= week_ago])
    col3.metric("This Week", week_count)
    
    # Export button
    st.markdown("---")
    if st.button("📥 Export to CSV", type="primary"):
        csv_path = storage.export_to_csv()
        st.success(f"✅ Exported {len(emails)} emails to `subscribers_export.csv`")
        
        # Download button
        with open(csv_path, 'rb') as f:
            st.download_button(
                label="⬇️ Download CSV",
                data=f,
                file_name="subscribers_export.csv",
                mime="text/csv"
            )
    
    # Data table
    st.markdown("---")
    st.subheader("All Subscribers")
    
    # Search/filter
    search_term = st.text_input("🔍 Search by email", "")
    if search_term:
        filtered_df = df[df['email'].str.contains(search_term, case=False, na=False)]
    else:
        filtered_df = df
    
    # Display table
    st.dataframe(
        filtered_df.sort_values('subscribed_at', ascending=False),
        use_container_width=True,
        hide_index=True
    )
    
    # Recent signups chart
    st.markdown("---")
    st.subheader("Signups Over Time")
    
    # Group by date
    daily_signups = df.groupby(df['subscribed_at'].dt.date).size().reset_index(name='count')
    daily_signups.columns = ['Date', 'Signups']
    daily_signups = daily_signups.sort_values('Date')
    
    st.line_chart(daily_signups.set_index('Date'))
    
else:
    st.info("No subscribers yet. They'll appear here once people start signing up!")

