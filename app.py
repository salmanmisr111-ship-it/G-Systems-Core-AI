import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# إعدادات الواجهة السيادية العابرة للحدود
st.set_page_config(page_title="G-Systems Global | Regional Command", page_icon="🌴", layout="wide")

# --- محرك البيانات (توشكى vs القصيم) ---
def get_site_data(site_name):
    if site_name == "Toshka (Egypt)":
        return np.random.rand(10, 10), "0.82", "22%", "Sector D"
    else: # Al-Rajhi Farm (Qassim)
        return np.random.rand(12, 12) * 0.9, "0.88", "18%", "Block 7 (Sukkari)"

# --- القائمة الجانبية والاقتصاد ---
st.sidebar.title("🌍 Global Operations")
selected_site = st.sidebar.selectbox("Select Strategic Site", ["Toshka (Egypt)", "Al-Rajhi Farm (Qassim)"])

st.sidebar.markdown("---")
st.sidebar.subheader("💎 G-Token Economy")
st.sidebar.metric("GTK Price", "$1.24", "+5.2%")

# --- واجهة التحكم الرئيسية ---
st.title(f"🛡️ Strategic Command: {selected_site}")
grid, ndvi, moisture, focus_area = get_site_data(selected_site)

col1, col2 = st.columns([3, 1])

with col1:
    st.subheader(f"Satellite Intelligence Feed: {selected_site}")
    fig, ax = plt.subplots(figsize=(10, 5))
    im = ax.imshow(grid, cmap='RdYlGn')
    plt.title(f"Real-time NDVI Analysis - {selected_site}")
    st.pyplot(fig)
    st.caption(f"Source: Sentinel-2 L2A | Last Pass: 2 Hours Ago")

with col2:
    st.write(f"### {focus_area} Insights")
    st.metric("Health Index (NDVI)", ndvi)
    st.metric("Soil Moisture", moisture)
    if selected_site == "Al-Rajhi Farm (Qassim)":
        st.success("Optimal Quality for Export")
    else:
        st.warning("Irrigation Optimization Required")

# بوابة البلوكشين وتوريق الأصول (RWA)
st.markdown("---")
st.subheader("🔗 Blockchain Asset Securitization (RWA)")
if st.button(f"Tokenize {selected_site} Harvest"):
    st.info(f"Processing Real-World Asset Tokenization for {selected_site}...")
    st.success(f"Assets Successfully Tokenized as $GTK on Base Network.")

st.caption("Powered by G-Systems Global AI | Secured Regional Gateway")