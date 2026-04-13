import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

# إعدادات الفخامة والسيادة الرقمية
st.set_page_config(page_title="G-Systems Global | AI Command", page_icon="📡", layout="wide")

# تخصيص واجهة المستخدم بـ CSS بسيط للهيبة التقنية
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; border-radius: 10px; padding: 15px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# --- المحرك الذكي للمواقع ---
def load_satellite_intel(site):
    if site == "توشكى (مصر)":
        data = np.random.rand(15, 15)
        metrics = {"ndvi": "0.82", "moisture": "22%", "status": "Warning: Sector D"}
    else:
        data = np.random.rand(15, 15) * 0.95
        metrics = {"ndvi": "0.88", "moisture": "18%", "status": "Optimal: Export Ready"}
    return data, metrics

# --- القائمة الجانبية: بوابة Web3 والاقتصاد ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2092/2092663.png", width=80)
st.sidebar.title("G-Systems Global")
st.sidebar.info("Economic Integrity & Food Security")

if st.sidebar.button("🔗 Connect MetaMask Wallet"):
    with st.sidebar.spinner("Connecting to Base Network..."):
        time.sleep(1.5)
        st.sidebar.success("Linked: 0x71C...8A3 (Account 3)")

st.sidebar.markdown("---")
st.sidebar.subheader("💎 $GTK Economy")
st.sidebar.metric("Token Value", "$1.24", "5.2%")

# --- لوحة التحكم الرئيسية ---
selected_site = st.selectbox("اختر الموقع الاستراتيجي للمراقبة:", ["توشكى (مصر)", "مزرعة الراجحي (القصيم)"])
st.title(f"📡 مركز القيادة والسيطرة: {selected_site}")

data, metrics = load_satellite_intel(selected_site)

col1, col2 = st.columns([2, 1])

with col1:
    st.write("### تحليل الأقمار الصناعية (Sentinel-2 L2A)")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(data, cmap='RdYlGn', interpolation='nearest')
    plt.axis('off')
    st.pyplot(fig)
    st.caption("مراقبة حية بنظام NDVI - تحديث كل 5 أيام قمرية")

with col2:
    st.write("### المؤشرات الحيوية")
    st.metric("صحة النبات (NDVI)", metrics['ndvi'])
    st.metric("رطوبة التربة", metrics['moisture'])
    
    if "Optimal" in metrics['status']:
        st.success(metrics['status'])
    else:
        st.error(metrics['status'])

    st.markdown("---")
    if st.button("🚀 توريق المحصول رقمياً (RWA)"):
        with st.status("جاري توثيق البيانات على البلوكشين...", expanded=True) as status:
            st.write("تحليل صور الأقمار الصناعية...")
            time.sleep(1)
            st.write("مطابقة إحداثيات الموقع...")
            time.sleep(1)
            st.write("إصدار عقود $GTK الذكية...")
            status.update(label="تم التوريق بنجاح! الأصول جاهزة للاستثمار.", state="complete")

st.markdown("---")
st.caption("G-Systems Global | نظام سيادي لتأمين سلاسل الإمداد الغذائي 2026")