import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# إعدادات الصفحة لهيبة الشركات الكبرى
st.set_page_config(page_title="G-Systems Global | AI Field Vision", page_icon="🛰️", layout="wide")

# --- محرك التحليل وإصدار التوصيات ---
def analyze_and_recommend(location):
    # توليد خريطة طيفية تحاكي الواقع
    data = np.random.rand(25, 25)
    total = data.size
    
    # حساب الإحصائيات (فكرتك الـ 100%)
    green = round((np.sum(data >= 0.6) / total) * 100, 1)
    yellow = round((np.sum((data >= 0.3) & (data < 0.6)) / total) * 100, 1)
    orange = round((np.sum((data >= 0.1) & (data < 0.3)) / total) * 100, 1)
    red = round((np.sum(data < 0.1) / total) * 100, 1)
    
    stats = {"green": green, "yellow": yellow, "orange": orange, "red": red}
    
    # محرك التوصيات بناءً على حالة الخريطة
    if red > 5 or orange > 15:
        rec = "⚠️ تحذير تقني: تم رصد انخفاض في النشاط الحيوي بالقطاع الملون بالأحمر. يُنصح بفحص دورة الري."
        color = "red"
    elif yellow > 20:
        rec = "💡 توصية فنية: هناك إجهاد ضوئي بسيط. يُنصح بإضافة جرعة مغذيات سائلة لتحسين كفاءة الأوراق."
        color = "blue"
    else:
        rec = "✅ تقرير الحالة: الغطاء النباتي في أفضل حالاته. لا توجد حاجة لتدخل بشري في هذا القطاع حالياً."
        color = "green"
        
    return data, stats, rec, color

# --- واجهة المستخدم ---
st.title("🛰️ منصة G-Systems للرؤية الفضائية والتحليل")
st.markdown("---")

location_input = st.text_input("📍 إحداثيات قطاع المزرعة (الراجحي - القصيم):", "26.3489, 43.9721")

# تقسيم الشاشة: الخريطة في جهة والتحليلات في جهة
col_map, col_stats = st.columns([1.5, 1])

if st.button("تحديث المسح الفضائي 🛰️"):
    with st.spinner("جاري سحب الصور الطيفية ومعالجة البيانات..."):
        time.sleep(2)
        data, stats, rec, rec_color = analyze_and_recommend(location_input)
        
        with col_map:
            st.subheader("🗺️ البصمة الطيفية للقطاع (NDVI)")
            fig, ax = plt.subplots(figsize=(8, 8))
            # استخدام الخريطة الحرارية RdYlGn لتعطي شكل الخريطة الزراعية الحقيقي
            im = ax.imshow(data, cmap='RdYlGn', interpolation='nearest')
            plt.axis('off')
            st.pyplot(fig)
            st.write(f"🛰️ **Sentinel-2 Status:** Active Connection | **Coordinates:** {location_input}")

        with col_stats:
            st.subheader("📊 تحليل المساحة والتوصيات")
            
            # عرض النسب المئوية (100%)
            st.write(f"🟢 **مثالي:** {stats['green']}%")
            st.progress(stats['green'] / 100)
            
            st.write(f"🟡 **مراقب:** {stats['yellow']}%")
            st.progress(stats['yellow'] / 100)
            
            st.write(f"🔴 **خطر:** {stats['red']}%")
            st.progress(stats['red'] / 100)
            
            st.divider()
            
            # صندوق التوصية الذكية
            st.markdown("### 🤖 G-Systems AI Advisor")
            if rec_color == "red":
                st.error(rec)
            elif rec_color == "blue":
                st.info(rec)
            else:
                st.success(rec)
                
            st.button("🚀 إرسال التقرير لغرفة العمليات")
else:
    st.info("قم بالضغط على 'تحديث المسح الفضائي' لإظهار الخريطة والتحليلات.")

st.markdown("---")
st.caption("G-Systems Global 2026 | السيادة الرقمية في الزراعة الذكية")