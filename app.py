"""
TikTok Landing Page - Enhanced Professional Streamlit App
Inspired by Sentinel Core's professional design
"""
import streamlit as st
import os
from datetime import datetime
from email_backend import EmailStorage, BrevoIntegration

# Page config
st.set_page_config(
    page_title="Sentinel Core - Blockchain & AI Insights",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Configuration
TIKTOK_USERNAME = st.secrets.get("TIKTOK_USERNAME", os.getenv("TIKTOK_USERNAME", "joseph.dakwa"))
TIKTOK_PIXEL_ID = st.secrets.get("TIKTOK_PIXEL_ID", os.getenv("TIKTOK_PIXEL_ID", "YOUR_PIXEL_ID"))

# Enhanced Custom CSS
st.markdown("""
<style>
    .main {
        padding: 0;
    }
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 4rem 2rem;
        text-align: center;
        border-radius: 0;
        margin: -1rem -1rem 2rem -1rem;
    }
    .hero-title {
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .hero-subtitle {
        font-size: 1.3rem;
        opacity: 0.95;
        margin-bottom: 2rem;
    }
    .section-title {
        font-size: 2rem;
        font-weight: bold;
        color: #333;
        text-align: center;
        margin: 3rem 0 2rem 0;
    }
    .section-subtitle {
        text-align: center;
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .value-card {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    .value-card-title {
        font-weight: bold;
        font-size: 1.3rem;
        margin-bottom: 0.5rem;
        color: #333;
    }
    .value-card-desc {
        color: #666;
        font-size: 1rem;
        line-height: 1.6;
    }
    .service-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: 2px solid #f0f0f0;
        text-align: center;
        transition: transform 0.2s;
    }
    .service-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.2);
        border-color: #667eea;
    }
    .service-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .service-title {
        font-weight: bold;
        font-size: 1.2rem;
        color: #333;
        margin-bottom: 0.5rem;
    }
    .service-desc {
        color: #666;
        font-size: 0.95rem;
    }
    .stats-container {
        display: flex;
        justify-content: space-around;
        text-align: center;
        margin: 2rem 0;
        flex-wrap: wrap;
    }
    .stat-item {
        padding: 1.5rem;
    }
    .stat-number {
        font-size: 2.5rem;
        font-weight: bold;
        color: #667eea;
    }
    .stat-label {
        color: #666;
        font-size: 1rem;
        margin-top: 0.5rem;
    }
    .testimonial-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        border-left: 4px solid #764ba2;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    .testimonial-text {
        font-style: italic;
        color: #555;
        font-size: 1rem;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    .testimonial-author {
        font-weight: bold;
        color: #333;
    }
    .testimonial-company {
        color: #667eea;
        font-size: 0.9rem;
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
    .cta-section {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 3rem 0;
    }
    .footer {
        text-align: center;
        color: #999;
        padding: 2rem 0;
        margin-top: 4rem;
        border-top: 2px solid #f0f0f0;
    }
</style>
""", unsafe_allow_html=True)

# TikTok Pixel Code
tiktok_pixel_code = f"""
<script>
!function (w, d, t) {{
  w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];ttq.methods=["page","track","identify","instances","debug","on","off","once","ready","alias","group","enableCookie","disableCookie"],ttq.setAndDefer=function(t,e){{t[e]=function(){{t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}}};for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);ttq.instance=function(t){{for(var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)ttq.setAndDefer(e,ttq.methods[n]);return e}},ttq.load=function(e,n){{var i="https://analytics.tiktok.com/i18n/pixel/events.js";ttq._i=ttq._i||{{}},ttq._i[e]=[],ttq._i[e]._u=i,ttq._t=ttq._t||{{}},ttq._t[e]=+new Date,ttq._o=ttq._o||{{}},ttq._o[e]=n||{{}};var o=document.createElement("script");o.type="text/javascript",o.async=!0,o.src=i+"?sdkid="+e+"&lib="+t;var a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(o,a)}};
  ttq.load('{TIKTOK_PIXEL_ID}');
  ttq.page();
}}(window, document, 'ttq');
</script>
"""

st.markdown(tiktok_pixel_code, unsafe_allow_html=True)

if TIKTOK_PIXEL_ID == "YOUR_PIXEL_ID":
    st.warning("⚠️ TikTok Pixel ID not set! Please add TIKTOK_PIXEL_ID to Streamlit secrets.")

# ==================== HERO SECTION ====================
st.markdown("""
<div class="hero-section">
    <div class="hero-title">🚀 Sentinel Core</div>
    <div class="hero-subtitle">Daily Insights on Blockchain, AI & Building in Web3</div>
    <p style="font-size: 1.1rem; opacity: 0.9;">Expert perspectives from real-world experience in blockchain security, AI automation, and Web3 development</p>
</div>
""", unsafe_allow_html=True)

# ==================== STATS SECTION ====================
st.markdown("""
<div class="stats-container">
    <div class="stat-item">
        <div class="stat-number">100+</div>
        <div class="stat-label">Smart Contracts Audited</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">50+</div>
        <div class="stat-label">AI Solutions Deployed</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">15+</div>
        <div class="stat-label">Blockchain Protocols</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">24/7</div>
        <div class="stat-label">Expert Support</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==================== WHAT YOU'LL GET SECTION ====================
st.markdown('<div class="section-title">💡 What You\'ll Get</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Practical insights delivered daily to your TikTok feed</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="value-card">
        <div class="value-card-title">🎯 Real-World Insights</div>
        <div class="value-card-desc">Learn from actual blockchain audits, AI implementations, and Web3 projects. No theory—just proven strategies.</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="value-card">
        <div class="value-card-title">⚡ Quick Value</div>
        <div class="value-card-desc">15-20 second videos packed with actionable insights. Learn something valuable in seconds, not hours.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="value-card">
        <div class="value-card-title">🎓 Expert Knowledge</div>
        <div class="value-card-desc">Insights from a team that's audited protocols on Arbitrum, Sablier, and built AI solutions for enterprise clients.</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="value-card">
        <div class="value-card-title">🚀 Stay Ahead</div>
        <div class="value-card-desc">Get the latest on blockchain security, AI automation, smart contract development, and Web3 trends.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ==================== OUR EXPERTISE SECTION ====================
st.markdown('<div class="section-title">🔧 Our Expertise</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">What we specialize in</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="service-card">
        <div class="service-icon">🔐</div>
        <div class="service-title">Blockchain Security</div>
        <div class="service-desc">Smart contract audits for DeFi protocols, NFT projects, and blockchain applications. Security-first approach.</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="service-card">
        <div class="service-icon">🤖</div>
        <div class="service-title">AI Solutions</div>
        <div class="service-desc">Custom AI agents, chatbots, document intelligence, and automation solutions for enterprise.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="service-card">
        <div class="service-icon">⚙️</div>
        <div class="service-title">Smart Contracts</div>
        <div class="service-desc">Development and auditing of DeFi protocols, token contracts, staking platforms, and blockchain infrastructure.</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="service-card">
        <div class="service-icon">🌐</div>
        <div class="service-title">Web3 Development</div>
        <div class="service-desc">Full-stack Web3 applications, dApps, tokenomics design, and decentralized solutions.</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="service-card">
        <div class="service-icon">💼</div>
        <div class="service-title">Enterprise AI</div>
        <div class="service-desc">AI-powered business automation, document processing, customer support bots, and intelligent workflows.</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="service-card">
        <div class="service-icon">📱</div>
        <div class="service-title">Mobile & Web Apps</div>
        <div class="service-desc">Modern web applications, mobile apps for fintech and crypto, with integrated AI features.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ==================== PROJECTS SHOWCASE ====================
st.markdown('<div class="section-title">🏗️ What We\'ve Built</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Real projects we\'ve delivered</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="value-card">
        <div class="value-card-title">🤖 AI Trading Bot</div>
        <div class="value-card-desc">Machine learning trading system with real-time sentiment analysis and dynamic strategy adjustment.</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="value-card">
        <div class="value-card-title">⚖️ AI Legal Research Assistant</div>
        <div class="value-card-desc">RAG-based chatbot for case law summaries and contract analysis with OCR integration.</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="value-card">
        <div class="value-card-title">💱 DeFi Lending Platform</div>
        <div class="value-card-desc">Non-custodial money market with collateral management, borrowing, and yield farming.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="value-card">
        <div class="value-card-title">📄 Document Intelligence</div>
        <div class="value-card-desc">LangChain-powered document search engine for enterprise internal knowledge bases.</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="value-card">
        <div class="value-card-title">💼 Crypto Payroll System</div>
        <div class="value-card-desc">Blockchain-native payroll platform with automated stablecoin payments and on-chain reporting.</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="value-card">
        <div class="value-card-title">🏢 Enterprise CRM</div>
        <div class="value-card-desc">Blockchain-integrated CRM with banking connections and KYC-aware dashboards.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ==================== TESTIMONIALS ====================
st.markdown('<div class="section-title">💬 What Clients Say</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="testimonial-card">
        <div class="testimonial-text">"Sentinel Core's expertise in smart contract security was evident from the start. Their ability to identify and address potential vulnerabilities was unparalleled."</div>
        <div class="testimonial-author">Ricky Magalhaes</div>
        <div class="testimonial-company">Enhalo</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="testimonial-card">
        <div class="testimonial-text">"Sentinel Core provided us with the assurance we needed to move forward confidently with our project. Their thorough security review was exceptional."</div>
        <div class="testimonial-author">Steve Cochrane</div>
        <div class="testimonial-company">Stabiliti</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ==================== PRIMARY CTA SECTION ====================
st.markdown("""
<div class="cta-section">
    <h2 style="font-size: 2.5rem; margin-bottom: 1rem; color: #333;">🚀 Get Daily Blockchain & AI Insights</h2>
    <p style="font-size: 1.2rem; color: #666; margin-bottom: 2rem;">Follow on TikTok for expert perspectives delivered to your feed</p>
</div>
""", unsafe_allow_html=True)

# TikTok Follow Button
tiktok_url = f"https://www.tiktok.com/@{TIKTOK_USERNAME}"
follow_button_html = f"""
<a href="{tiktok_url}" 
   target="_blank" 
   rel="noopener noreferrer"
   onclick="if (typeof ttq !== 'undefined') {{ ttq.track('CompleteRegistration', {{ content_type: 'button', content_name: 'Follow on TikTok', content_category: 'engagement' }}); }}"
   style="display: inline-block; width: 100%; text-align: center; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 1.2rem 2rem; border-radius: 50px; text-decoration: none; font-weight: bold; font-size: 1.2rem; transition: transform 0.2s; box-sizing: border-box;">
🚀 Follow @{TIKTOK_USERNAME} on TikTok
</a>
"""

st.markdown(follow_button_html, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==================== SECONDARY CTA - NEWSLETTER ====================
st.markdown("---")
st.markdown("### 📧 Get Deeper Insights via Newsletter")
st.markdown("Join our newsletter for weekly roundups, exclusive content, and in-depth blockchain & AI insights.")

with st.form("newsletter_signup", clear_on_submit=True):
    col1, col2 = st.columns([3, 1])
    with col1:
        email = st.text_input("Your email address", placeholder="your@email.com", type="default", label_visibility="collapsed")
    with col2:
        submitted = st.form_submit_button("📧 Subscribe", use_container_width=True)
    
    if submitted and email:
        if "@" in email and "." in email:
            # Initialize email storage
            try:
                # Try Brevo first (if API key is set)
                brevo_api_key = st.secrets.get("BREVO_API_KEY", os.getenv("BREVO_API_KEY"))
                brevo_success = False
                
                if brevo_api_key:
                    brevo = BrevoIntegration(api_key=brevo_api_key)
                    brevo_success = brevo.add_contact(email)
                
                # Also save to local database (backup)
                storage = EmailStorage()
                db_success, db_message = storage.add_email(email, source="tiktok_landing_page")
                
                # If either Brevo or database succeeded, show success
                if brevo_success or db_success:
                    # Track TikTok conversion
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
                    st.success("✅ Thanks for subscribing! Check your email to confirm.")
                else:
                    # Only show warning if both failed
                    if not brevo_success and not db_success:
                        st.warning(f"⚠️ {db_message}")
            except Exception as e:
                st.error(f"❌ Error saving email. Please try again.")
                st.exception(e)  # Show error in debug mode
        else:
            st.error("❌ Please enter a valid email address")
    elif submitted:
        st.error("❌ Please enter your email address")

# ==================== FOOTER ====================
st.markdown("""
<div class="footer">
    <p style="font-size: 0.9rem; margin-bottom: 0.5rem;"><strong>Sentinel Core</strong></p>
    <p style="font-size: 0.8rem;">Blockchain Security • AI Solutions • Web3 Development</p>
    <p style="font-size: 0.8rem; margin-top: 1rem;">© 2025 Sentinel Core. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
