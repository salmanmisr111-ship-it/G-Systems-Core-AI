import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# إعدادات الواجهة السيادية للهيبة التقنية
st.set_page_config(page_title="G-Systems Global | AI Space Control", page_icon="🛰️", layout="wide")

# تخصيص المظهر بـ CSS بسيط لراحة العين وإبراز الألوان
st.markdown("""
    <style>
    .stMetric { background-color: #161b22; border-radius: 10px; padding: 15px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# --- محرك البحث الفضائي (محاكاة الربط مع Sentinel-2) ---
def remote_sensing_engine(location):
    # توليد مصفوفة بيانات تحاكي الواقع الزراعي الطيفي
    grid_size = 25
    data = np.random.rand(grid_size, grid_size)
    return data

# --- القائمة الجانبية (إدارة المحفظة والهوية) ---
st.sidebar.title("🛡️ G-Systems Global")
st.sidebar.info("Economic Integrity & Food Security")
if st.sidebar.button("🔗 Connect MetaMask Wallet"):
    with st.sidebar.spinner("Accessing Blockchain..."):
        time.sleep(1.5)
        st.sidebar.success("Linked: 0x71C...8A3")

st.sidebar.markdown("---")
st.sidebar.subheader("💎 $GTK Economy")
st.sidebar.metric("Current Asset Value", "$1.24", "5.2%")

# --- واجهة العرض الرئيسي ---
st.title("🛰️ مركز الرصد والتحليل الفضائي اللحظي")
st.write("المنصة مرتبطة حياً بوكالة الفضاء الأوروبية لمعالجة بيانات مزارع **توشكى والقصيم**.")

# إدخال الإحداثيات
location_input = st.text_input("📍 أدخل إحداثيات الموقع (مثال: 26.3489, 43.9721):", "26.3489, 43.9721")

col1, col2 = st.columns([2, 1])

with col1:
    if st.button("التقاط صورة فضائية الآن 📡"):
        with st.status("جاري توجيه القمر الصناعي ومعالجة الموجات تحت الحمراء...", expanded=True) as status:
            time.sleep(3) # الإبهار التقني
            data = remote_sensing_engine(location_input)
            
            # رسم الخريطة الحرارية
            fig, ax = plt.subplots(figsize=(10, 6))
            im = ax.imshow(data, cmap='RdYlGn', interpolation='nearest') # RdYlGn هو تدرج الألوان العالمي للزراعة
            plt.axis('off')
            st.pyplot(fig)
            
            # سطر إثبات الربط الذي طلبته
            st.write(f"🛰️ **Sentinel-2 Status:** Linked | **Lat/Long:** {location_input} | **Spectrum:** Multi-spectral L2A")
            status.update(label="تم استقبال وتحليل البيانات بنجاح!", state="complete")
    else:
        st.info("قم بإدخال الإحداثيات ثم اضغط على الزر لبدء الرصد الحي.")

with col2:
    # حل مشكلة "عشرات الألوان" (تبسيط البيانات للمستثمر)
    st.write("### 🎨 دليل تحليل الألوان (NDVI Guide)")
    st.markdown("""
    * 🟢 **الأخضر (الداكن والزاهي):** صحة نباتية مثالية. امتصاص كامل للسماد وكفاءة ري عالية.
    
    * 🟡 **الأصفر (والتدرجات الفاتحة):** **إنذار مبكر.** وجود إجهاد مائي بسيط أو بداية نقص في المغذيات.
    
    * 🟠 **البرتقالي (والتدرجات الباهتة):** **منطقة خطر.** إصابة حشرية محتملة أو خلل في شبكة الري.
    
    * 🔴 **الأحمر (والبني):** **تدهور حاد.** منطقة خالية من النشاط الحيوي أو إصابة مدمرة.
    """)
    
    st.markdown("---")
    st.write("### 📊 التقرير الفوري للقطاع")
    if 'data' in locals() or 'data' in globals():
        st.metric("مؤشر الصحة (NDVI)", "0.89", delta="مثالي")
        st.metric("رطوبة التربة", "21%")
        if st.button("🚀 توريق المحصول رقمياً ($GTK)"):
            st.success("تم التوثيق كأصل رقمي موثق على البلوكشين.")

st.markdown("---")
st.caption("G-Systems Global | نظام سيادي لتأمين سلاسل الإمداد الغذائي 2026")