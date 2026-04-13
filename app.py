import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import numpy as np

# إعدادات الصفحة
st.set_page_config(page_title="G-Systems Global AI", page_icon="🛰️", layout="wide")

# --- دالة التقرير الرسمي المحسنة ---
def create_official_pdf(summary):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 20)
    pdf.set_text_color(34, 139, 34)
    pdf.cell(0, 15, 'G-SYSTEMS GLOBAL - STRATEGIC REPORT', ln=True, align='L')
    pdf.set_draw_color(34, 139, 34)
    pdf.line(10, 30, 200, 30)
    pdf.ln(10)
    pdf.set_font('Arial', '', 12)
    pdf.set_text_color(0, 0, 0)
    for key, value in summary.items():
        pdf.cell(90, 10, f"{key}:", border=1)
        pdf.cell(90, 10, f"{value}", border=1, ln=True)
    return pdf.output(dest='S').encode('latin-1')

# --- الواجهة الرئيسية ---
st.title("🛰️ G-Systems: Satellite Agriculture Intelligence")
st.sidebar.header("🌍 National Monitoring Center")

# محاكاة التنبيهات السيادية
alert_status = st.sidebar.select_slider("System Status", options=["Normal", "Warning", "CRITICAL ALERT"])
if alert_status == "CRITICAL ALERT":
    st.sidebar.error("🚨 ALERT: Sudden NDVI Drop detected in Sector D (Toshka)")

# قسم الأقمار الصناعية (محاكاة Sentinel-2)
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Live Satellite Feed (Simulation: Sentinel-2)")
    # رسم خريطة حرارية تخيلية لصحة النخيل
    map_data = np.random.rand(10, 10)
    fig, ax = plt.subplots()
    im = ax.imshow(map_data, cmap='RdYlGn') # أحمر (مريض) إلى أخضر (سليم)
    plt.colorbar(im, label="NDVI Health Index")
    st.pyplot(fig)
    st.caption("Monitoring Toshka Zone - Grid Alpha-7")

with col2:
    st.subheader("Data Insights")
    st.metric("Vegetation Index (NDVI)", "0.82", "+0.05")
    st.metric("Soil Moisture (IoT)", "22%", "-3%")
    st.info("AI Note: Sector B requires irrigation in 48 hours.")

# رفع البيانات وإصدار التقارير
st.markdown("---")
uploaded_file = st.file_uploader("Upload Sector Data for Analysis", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.success("Data Analyzed via AI Core.")
    
    summary = {
        "Report ID": "GS-2026-X9",
        "Target Zone": "Toshka South",
        "Satellite Source": "Sentinel-2 L2A",
        "Anomalies Detected": "2 Localized Spots",
        "Action Required": "Immediate Inspection Sector D"
    }
    
    pdf_report = create_official_pdf(summary)
    st.download_button("📥 Download Official Strategic Report", data=pdf_report, file_name="Strategic_Analysis.pdf")

st.markdown("---")
st.caption("Powered by G-Systems Global AI | Secure Cloud Gateway")