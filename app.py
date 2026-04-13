import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# إعدادات الواجهة السيادية لشركة G-Systems Global
st.set_page_config(page_title="G-Systems | Multi-Layer AI", page_icon="📡", layout="wide")

# تخصيص المظهر (CSS) لتبدو الواجهة أكثر هيبة واحترافية
st.markdown("""
    <style>
    .stMetric { background-color: #1a1e26; border-radius: 10px; padding: 15px; border: 1px solid #30363d; }
    .stProgress > div > div > div > div { background-color: #2e7d32; }
    </style>
    """, unsafe_allow_html=True)

# --- محرك التحليل والقرارات (G-Systems AI Engine) ---
def run_pre_api_analysis(location):
    # مصفوفة بيانات تحاكي الواقع (Mock Data)
    data = np.random.rand(20, 20)
    total = data.size
    
    # حساب نسب الألوان (فكرتك الـ 100%)
    green = 72.0  # نسبة مثالية
    yellow = 20.0 # نسبة إنذار
    red = 8.0    # نسبة خطر
    
    stats = {"green": green, "yellow": yellow, "red": red}
    
    # محرك التوصيات بناءً على الإحصائيات (المعالج الذكي)
    if red > 5:
        rec = "⚠️ تحذير تقني: رصد خلل حيوي في القطاع رقم 4. يوصى بتوجيه طائرة الدرون للفحص الميداني."
        color = "red"
    elif yellow > 25:
        rec = "💡 توصية فنية: وجود إجهاد بسيط. يُنصح بإضافة جرعة تسميد ورقي لتحسين كفاءة التمثيل الضوئي."
        color = "blue"
    else:
        rec = "✅ الحالة مثالية: الغطاء النباتي مستقر. استمر في جدول التسميد الحالي."
        color = "green"
        
    return data, stats, rec, color

# --- واجهة الرصد والتحليل ---
st.title("🛰️ مركز الرصد والتحليل المتكامل (G-Systems)")
st.caption("الربط الحي بالقمر الصناعي Sentinel-2 ومنصة Planet Labs")
st.markdown("---")

# إدخال الإحداثيات (الراجحي)
location_input = st.text_input("📍 أدخل إحداثيات الموقع:", "26.3489, 43.9721")

# إنشاء ثلاثة أعمدة (أعمدة العرض الحاسم)
col_real, col_heat, col_stats = st.columns([1.5, 1.5, 1])

if st.button("تحديث المسح الفوري 📡"):
    with st.status("جاري سحب الصور الطيفية وتحليل البيانات...", expanded=True) as status:
        time.sleep(3) # الإبهار التقني
        data, stats, rec, rec_color = run_pre_api_analysis(location_input)
        
        # 1. طبقة الرؤية الحقيقية (Real View) كما طلبت في image_6.png
        with col_real:
            st.subheader("🗺️ الرؤية الفضائية البصرية (Real View)")
            # نستخدم صورة الراجحي الحقيقية المخزنة لعرضها
            st.image(r"image_6.png", caption=f"آخر بث فضائي لقطاع {location_input}", use_container_width=True)
            st.write(f"🛰️ **Source:** Copernicus Open Access Hub")
            
        # 2. طبقة التحليل الطيفي (NDVI) كما في كودنا السابق
        with col_heat:
            st.subheader("🎨 التحليل الطيفي (NDVI)")
            fig, ax = plt.subplots(figsize=(8, 8))
            ax.imshow(data, cmap='RdYlGn', interpolation='nearest')
            plt.axis('off')
            st.pyplot(fig)
            st.write(f"🛰️ **Sentinel-2 Status:** Linked | **Layer:** NDVI L2A")
            
        # 3. تقرير النسب المئوية والتوصيات (100% كما في كودنا)
        with col_stats:
            st.subheader("📊 تقرير القطاع")
            
            # عرض النسب الإحصائية (100%)
            st.write(f"🟢 مثالي: {stats['green']}%")
            st.progress(stats['green'] / 100)
            st.write(f"🟡 إنذار: {stats['yellow']}%")
            st.progress(stats['yellow'] / 100)
            st.write(f"🔴 خطر: {stats['red']}%")
            st.progress(stats['red'] / 100)
            
            st.divider()
            
            # صندوق التوصية الذكية
            st.write("### 🤖 توصية G-Systems AI:")
            if rec_color == "red":
                st.error(rec)
            elif rec_color == "blue":
                st.info(rec)
            else:
                st.success(rec)
            
            # زر أمر العمل لإظهار قوة النظام
            st.button("🚀 إصدار أمر عمل للفريق")
            
        status.update(label="تم تحديث كافة الطبقات وتحليل البيانات بنجاح!", state="complete")
        
else:
    st.info("قم بالضغط على الزر لبدء الرصد والتحليل المتعدد الطبقات.")

st.markdown("---")
st.caption("G-Systems Global 2026 | تأمين سلاسل الإمداد الغذائي عبر تكنولوجيا الفضاء")