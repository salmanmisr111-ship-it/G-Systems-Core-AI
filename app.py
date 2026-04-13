import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
import os

# إعدادات الواجهة السيادية للهيبة التقنية (توسيع الواجهة لتستوعب 3 أعمدة)
st.set_page_config(page_title="G-Systems Global | Multi-Layer Analysis", page_icon="📡", layout="wide")

# تخصيص CSS لتبدو الواجهة أكثر هيبة واحترافية
st.markdown("""
    <style>
    .reportview-container .main .block-container{ padding-top: 1rem; padding-bottom: 1rem; }
    .stMetric { background-color: #1a1e26; border-radius: 10px; padding: 15px; border: 1px solid #30363d; }
    .stProgress > div > div > div > div { background-color: #2e7d32; }
    </style>
    """, unsafe_allow_html=True)

# --- محرك البحث والتحليل الطيفي الذكي (G-Systems Engine) ---
def analyze_multi_layer(location):
    # مصفوفة بيانات تحاكي الواقع (NDVI)
    data = np.random.rand(20, 20)
    total = data.size
    
    # حساب نسب الألوان (فكرتك الـ 100%)
    green = round((np.sum(data >= 0.7) / total) * 100, 1)
    yellow = round((np.sum((data >= 0.3) & (data < 0.7)) / total) * 100, 1)
    orange = round((np.sum((data >= 0.1) & (data < 0.3)) / total) * 100, 1)
    red = round((np.sum(data < 0.1) / total) * 100, 1)
    
    stats = {"green": green, "yellow": yellow, "orange": orange, "red": red}
    
    # محرك التوصيات بناءً على الإحصائيات (المعالج الذكي)
    if red > 5 or orange > 10:
        rec = "⚠️ تدخل عاجل: رصد إجهاد مائي حاد في القطاع الشرقي. يُنصح بفحص صمامات الري فوراً."
        color = "red"
    elif yellow > 25:
        rec = "💡 توصية فنية: وجود إجهاد بسيط. يُنصح بإضافة جرعة تسميد ورقي لتعزيز النشاط الحيوي."
        color = "blue"
    else:
        rec = "✅ تقرير الحالة: الغطاء النباتي مثالي. لا حاجة لتدخل بشري حالياً في هذا القطاع."
        color = "green"
        
    return data, stats, rec, color

# --- واجهة الرصد والتحليل ---
st.title("🛰️ مركز الرصد والتحليل المتكامل (G-Systems Global)")
st.caption("الربط الحي بالقمر الصناعي Sentinel-2 ومنصة Planet Labs")
st.markdown("---")

# إدخال الإحداثيات (الراجحي)
location_input = st.text_input("📍 أدخل إحداثيات الموقع:", "26.3489, 43.9721")

# إنشاء ثلاثة أعمدة (أعمدة العرض الحاسم)
col_real, col_heat, col_stats = st.columns([1.5, 1.5, 1])

if st.button("تحديث المسح الفوري 📡"):
    with st.status("جاري سحب الصور الطيفية وتحليل البيانات...", expanded=True) as status:
        time.sleep(3) # الإبهار التقني
        data, stats, rec, rec_color = analyze_multi_layer(location_input)
        
        # 1. طبقة الرؤية الحقيقية (Real View) كما طلبت في image_6.png
        with col_real:
            st.subheader("🗺️ الرؤية الفضائية البصرية (Real View)")
            
            # كود آمن لعرض الصورة لتجاوز الخطأ السابق
            image_path = "rajhi_farm.jpg"
            if os.path.exists(image_path):
                st.image(image_path, caption=f"آخر بث فضائي لقطاع {location_input}", use_container_width=True)
                st.write(f"🛰️ **Source:** Copernicus Open Access Hub")
            else:
                st.warning(f"⚠️ لم يتم العثور على ملف الصورة '{image_path}'. يرجى وضع الملف في نفس مجلد الكود لتجاوز الخطأ.")
                st.image("https://via.placeholder.com/800x600.png?text=Satellite+Feed+Connecting...", caption="انتظار ربط القمر الصناعي", use_container_width=True)
            
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
            st.subheader("📊 تقرير القطاع التفاعلي")
            
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
            
            # زر أمر العمل لإظهار قوة النظام التفاعلي
            st.button("🚀 إصدار أمر عمل للفريق الميداني")
            
        status.update(label="تم تحديث كافة الطبقات وتحليل البيانات بنجاح!", state="complete")
        
else:
    st.info("قم بالضغط على الزر لبدء الرصد والتحليل المتعدد الطبقات.")

st.markdown("---")
st.caption("G-Systems Global 2026 | تأمين سلاسل الإمداد الغذائي عبر تكنولوجيا الفضاء والبلوكشين")