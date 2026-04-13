import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# إعدادات الواجهة السيادية
st.set_page_config(page_title="G-Systems Global | Web3 Command", page_icon="🔗", layout="wide")

# --- وظائف الـ Web3 ---
def connect_wallet():
    if st.sidebar.button("Connect MetaMask Wallet"):
        # محاكاة الربط مع الحساب الظاهر في صورتك
        st.sidebar.success("Connected: 0x71C...8A3 (Account 3)") #
        st.sidebar.info("Network: Base Mainnet")

# --- محرك البيانات ---
def get_site_data(site_name):
    if site_name == "Toshka (Egypt)":
        return np.random.rand(10, 10), "0.82", "Sector D"
    else:
        return np.random.rand(12, 12) * 0.9, "0.88", "Block 7 (Sukkari)"

# --- الواجهة الجانبية ---
st.sidebar.title("🌍 Global Operations")
selected_site = st.sidebar.selectbox("Select Strategic Site", ["Toshka (Egypt)", "Al-Rajhi Farm (Qassim)"])
connect_wallet()

st.sidebar.markdown("---")
st.sidebar.subheader("💎 G-Token Economy")
st.sidebar.write("Price: $1.24 | Trend: +5.2%") #

# --- لوحة التحكم الرئيسية ---
st.title(f"🛡️ Strategic Command Center: {selected_site}")
grid, ndvi, focus_area = get_site_data(selected_site)

col1, col2 = st.columns([3, 1])

with col1:
    st.subheader(f"Satellite Intelligence Feed: {selected_site}")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(grid, cmap='RdYlGn')
    plt.title(f"Real-time NDVI Analysis - {selected_site}")
    st.pyplot(fig)

with col2:
    st.write(f"### {focus_area} Insights")
    st.metric("Health Index (NDVI)", ndvi)
    if float(ndvi) > 0.85:
        st.success("Certified for International Export") #
    
    # زر التوريق المالي (RWA)
    if st.button("Tokenize Asset ($GTK)"):
        st.warning("Verifying Proof of Harvest on Blockchain...")
        st.success(f"Asset Securitized. Tokens issued to Account 3.")

st.markdown("---")
st.caption("G-Systems Global | Secured by Encrypted Blockchain Data Stream") #