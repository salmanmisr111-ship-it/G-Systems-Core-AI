import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# إعدادات الواجهة السيادية (توسيع الواجهة لتستوعب 3 أعمدة)
st.set_page_config(page_title="G-Systems Global | Multi-Layer Analysis", page_icon="📡", layout="wide")

# تخصيص CSS لتبدو الواجهة أكثر هيبة
st.markdown("""
    <style>
    .reportview-container .main .block-container{ padding-top: 1rem; padding-bottom: 1rem; }
    .stProgress .st-bo{ background-color: #2e7d32; }
    </style>
    """, unsafe_allow_html=True)

# --- محرك البحث والتحليل الطيفي (G-Systems Engine) ---
def analyze_multi_layer(location):
    # محاكاة لبيانات حقيقية (NDVI)
    data = np.random.rand(20, 20)
    total = data.size
    
    # حساب نسب الألوان (فكرتك الـ 100%)
    green = round((np.sum(data >= 0.7) / total) * 100, 1)
    yellow = round((np.sum((data >= 0.3) & (data < 0.7)) / total) * 100, 1)
    orange = round((np.sum((data >= 0.1) & (data < 0.3)) / total) * 100, 1)
    red = round((np.sum(data < 0.1) / total) * 100, 1)
    
    stats = {"green": green, "yellow": yellow, "orange": orange, "red": red}
    
    # محرك التوصيات
    if red > 5 or orange > 10:
        rec = "⚠️ تدخل عاجل: رصد إجهاد مائي حاد في القطاع الشرقي. يُنصح بفحص صمامات الري."
        color = "red"
    elif yellow > 25:
        rec = "💡 نصيحة: وجود إجهاد بسيط. يُنصح بإضافة جرعة تسميد ورقي لتحسين كفاءة التمثيل الضوئي."
        color = "blue"
    else:
        rec = "✅ تقرير الحالة: الغطاء النباتي مثالي. لا حاجة لتدخل بشري حالياً."
        color = "green"
        
    return data, stats, rec, color

# --- واجهة الرصد والتحليل ---
st.title("🛰️ مركز الرصد والتحليل المتعدد الطبقات (G-Systems)")
st.caption("الربط الحي بالقمر الصناعي Sentinel-2 ومنصة Planet Labs")
st.markdown("---")

location_input = st.text_input("📍 أدخل إحداثيات الموقع:", "26.3489, 43.9721")

# إنشاء ثلاثة أعمدة (أعمدة العرض الحاسم)
col_real, col_heat, col_stats = st.columns([1.5, 1.5, 1])

if st.button("تحديث المسح الفوري 📡"):
    with st.status("جاري سحب الصور الطيفية وتحليل البيانات...", expanded=True) as status:
        time.sleep(3) # الإبهار التقني
        data, stats, rec, rec_color = analyze_multi_layer(location_input)
        
        # العمود الأول: الخريطة الحقيقية (كما طلبت في image_6.png)
        with col_real:
            st.subheader("🗺️ الرؤية الفضائية البصرية (Real View)")
            # في التطبيق الحقيقي سنضع Mapbox/Planet WMTS هنا. الآن نضع صورة توضيحية محاكاة
            st.image(r"image_6.png", caption=f"آخر بث فضائي لقطاع {location_input}", use_container_width=True)
            st.write(f"🛰️ **Source:** Copernicus Open Access Hub")
            
        # العمود الثاني: الخريطة الحرارية (NDVI) كما في كودنا السابق
        with col_heat:
            st.subheader("🎨 التحليل الطيفي (NDVI)")
            fig, ax = plt.subplots(figsize=(8, 8))
            ax.imshow(data, cmap='RdYlGn', interpolation='nearest')
            plt.axis('off')
            st.pyplot(fig)
            st.write(f"🛰️ **Sentinel-2 Status:** Linked | **Layer:** NDVI L2A")
            
        # العمود الثالث: التقرير الفني والتوصيات (100% كما في كودنا)
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
            
            st.button("🚀 إصدار أمر عمل للفريق")
            
        status.update(label="تم تحديث كافة الطبقات وتحليل البيانات بنجاح!", state="complete")
        
else:
    st.info("قم بالضغط على الزر لبدء الرصد والتحليل المتعدد الطبقات.")

st.markdown("---")
st.caption("G-Systems Global 2026 | تأمين سلاسل الإمداد الغذائي عبر تكنولوجيا الفضاء")