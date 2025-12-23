"""
TikTok Landing Page - Streamlit App
"""
import streamlit as st
import os
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Sentinel Core - Blockchain & AI Insights",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Configuration (set in Streamlit secrets or environment)
TIKTOK_USERNAME = st.secrets.get("TIKTOK_USERNAME", os.getenv("TIKTOK_USERNAME", "joseph.dakwa"))
TIKTOK_PIXEL_ID = st.secrets.get("TIKTOK_PIXEL_ID", os.getenv("TIKTOK_PIXEL_ID", "YOUR_PIXEL_ID"))

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 2rem 1rem;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 1rem 2rem;
        font-weight: bold;
        font-size: 1.1rem;
        transition: transform 0.2s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
    }
    .value-prop {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .value-prop-title {
        font-weight: bold;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
        color: #333;
    }
    .value-prop-desc {
        color: #666;
        font-size: 0.95rem;
    }
    h1 {
        text-align: center;
        margin-bottom: 1rem;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .social-proof {
        text-align: center;
        color: #666;
        margin-top: 2rem;
        padding-top: 2rem;
        border-top: 2px solid #f0f0f0;
    }
</style>
""", unsafe_allow_html=True)

# TikTok Pixel Code (inject into page)
tiktok_pixel_code = f"""
<script>
!function (w, d, t) {{
  w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];ttq.methods=["page","track","identify","instances","debug","on","off","once","ready","alias","group","enableCookie","disableCookie"],ttq.setAndDefer=function(t,e){{t[e]=function(){{t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}}};for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);ttq.instance=function(t){{for(var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)ttq.setAndDefer(e,ttq.methods[n]);return e}},ttq.load=function(e,n){{var i="https://analytics.tiktok.com/i18n/pixel/events.js";ttq._i=ttq._i||{{}},ttq._i[e]=[],ttq._i[e]._u=i,ttq._t=ttq._t||{{}},ttq._t[e]=+new Date,ttq._o=ttq._o||{{}},ttq._o[e]=n||{{}};var o=document.createElement("script");o.type="text/javascript",o.async=!0,o.src=i+"?sdkid="+e+"&lib="+t;var a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(o,a)}};
  ttq.load('{TIKTOK_PIXEL_ID}');
  ttq.page();
}}(window, document, 'ttq');
</script>
"""

# Inject TikTok Pixel
st.markdown(tiktok_pixel_code, unsafe_allow_html=True)

# Debug: Verify Pixel ID is set (remove this after verification)
if TIKTOK_PIXEL_ID == "YOUR_PIXEL_ID":
    st.warning("⚠️ TikTok Pixel ID not set! Please add TIKTOK_PIXEL_ID to Streamlit secrets.")
else:
    # Hidden debug message (comment out after testing)
    st.markdown(f'<!-- TikTok Pixel ID: {TIKTOK_PIXEL_ID} -->', unsafe_allow_html=True)

# Header
st.markdown('<div style="text-align: center; margin-bottom: 0.5rem;"><h2 style="color: #667eea; margin: 0;">Sentinel Core</h2></div>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #666; margin-bottom: 1rem; font-size: 0.9rem;">Blockchain • AI • Entrepreneurship</p>', unsafe_allow_html=True)

# Main heading
st.markdown("# Daily Insights on Blockchain, AI & Building in Web3")

# Subtitle
st.markdown(
    """
    <p class="subtitle">
        Get expert perspectives on blockchain security, AI automation, and building in Web3.<br>
        No fluff. Just value.
    </p>
    """,
    unsafe_allow_html=True
)

# Value propositions
st.markdown("### What You'll Get")

st.markdown("""
<div class="value-prop">
    <div class="value-prop-title">🎯 Real-World Insights</div>
    <div class="value-prop-desc">Practical advice from someone who's actually building in blockchain and AI</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="value-prop">
    <div class="value-prop-title">⚡ 15-20 Second Value</div>
    <div class="value-prop-desc">Quick, actionable insights that fit into your day</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="value-prop">
    <div class="value-prop-title">🎓 Expert Insights</div>
    <div class="value-prop-desc">Learn from real-world experience building blockchain and AI solutions</div>
</div>
""", unsafe_allow_html=True)

# Primary CTA - Newsletter Signup
st.markdown("---")
st.markdown("### Get Free Weekly Newsletter")
st.markdown("Join our newsletter for deeper insights, exclusive content, and weekly roundups of the best blockchain & AI insights.")

with st.form("newsletter_signup", clear_on_submit=True):
    email = st.text_input("Your email address", placeholder="your@email.com", type="default")
    submitted = st.form_submit_button("📧 Sign Up for Free Newsletter", use_container_width=True)
    
    if submitted and email:
        # Validate email
        if "@" in email and "." in email:
            # Track conversion (CompleteRegistration is the standard TikTok event for signups)
            conversion_script = f"""
            <script>
                if (typeof ttq !== 'undefined') {{
                    ttq.track('CompleteRegistration', {{
                        content_type: 'newsletter_signup',
                        content_name: 'Free Newsletter Signup',
                        email: '{email}',
                        value: 1,
                        currency: 'USD'
                    }});
                }}
            </script>
            """
            st.markdown(conversion_script, unsafe_allow_html=True)
            
            # Store email (in production, save to database)
            # For now, just show success message
            st.success("✅ Thanks for signing up! Check your email to confirm your subscription.")
            
            # Optional: Store in session state or send to backend
            if 'subscribed_emails' not in st.session_state:
                st.session_state.subscribed_emails = []
            st.session_state.subscribed_emails.append({
                'email': email,
                'timestamp': datetime.now().isoformat()
            })
        else:
            st.error("❌ Please enter a valid email address")
    elif submitted:
        st.error("❌ Please enter your email address")

# Secondary CTA - Follow on TikTok
st.markdown("---")
st.markdown("### Also Follow on TikTok")
st.markdown("Get daily insights delivered to your TikTok feed")

# Track Follow Button Click
tiktok_url = f"https://www.tiktok.com/@{TIKTOK_USERNAME}"
follow_button_clicked = st.button("🚀 Follow @{} on TikTok".format(TIKTOK_USERNAME), key="follow_button", use_container_width=True)

if follow_button_clicked:
    # Track conversion event
    conversion_script = f"""
    <script>
        if (typeof ttq !== 'undefined') {{
            ttq.track('ClickButton', {{
                content_type: 'button',
                content_name: 'Follow on TikTok',
                content_category: 'engagement'
            }});
        }}
        window.open('{tiktok_url}', '_blank');
    </script>
    """
    st.markdown(conversion_script, unsafe_allow_html=True)
    st.info(f"🚀 Opening TikTok in a new tab...")

# Social proof
st.markdown(
    """
    <div class="social-proof">
        Join thousands learning about blockchain, AI, and building in Web3
    </div>
    """,
    unsafe_allow_html=True
)

# Footer
st.markdown("---")
st.markdown(
    '<p style="text-align: center; color: #999; font-size: 0.8rem;">© 2025 Sentinel Core. All rights reserved.</p>',
    unsafe_allow_html=True
)

