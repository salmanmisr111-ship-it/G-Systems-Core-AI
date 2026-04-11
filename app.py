import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import base64

# إعدادات الصفحة
st.set_page_config(page_title="G-Systems Global - Smart Portal", layout="wide")

# --- دالة إنشاء الـ PDF ---
def create_pdf(df):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "G-Systems Global: Technical Fiber Report", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    for index, row in df.iterrows():
        line = f"Sample: {row['Sample_Code']} | Type: {row['palm_type']} | Length: {row['length_cm']}cm"
        pdf.cell(200, 10, line, ln=True)
    return pdf.output(dest='S').encode('latin-1')

# --- واجهة الموقع ---
st.title("🌴 G-Systems Global: Smart Palm Analytics")
st.sidebar.header("💳 Web3 Payment Gateway")

# تمثيل MetaMask
if st.sidebar.button("Connect MetaMask"):
    st.sidebar.success("Wallet Connected: 0x71C...39bd")
    st.sidebar.info("Account Balance: 1.25 ETH")

st.write("---")

uploaded_file = st.file_uploader("Upload Palm Data (Excel)", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📊 Analytical View")
        st.dataframe(df)
    with col2:
        fig, ax = plt.subplots()
        ax.bar(df['palm_type'], df['length_cm'], color='#2E8B57')
        st.pyplot(fig)

    st.divider()
    
    # خيار التحميل والدفع
    st.subheader("📩 Export & Settle")
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Generate PDF Report"):
            pdf_data = create_pdf(df)
            b64 = base64.b64encode(pdf_data).decode()
            href = f'<a href="data:application/octet-stream;base64,{b64}" download="G_Systems_Report.pdf">Click here to download PDF</a>'
            st.markdown(href, unsafe_allow_html=True)
            st.success("Report Generated!")
            
    with c2:
        if st.button("Pay with Crypto (0.01 ETH)"):
            st.warning("Awaiting Confirmation from MetaMask...")
            st.balloons() # احتفال بالدفع
            st.success("Payment Successful! Transaction: 0x9a2...f6e")