import streamlit as st

st.set_page_config(page_title="Resume Relevance Check", layout="wide")

st.title("📄 Automated Resume Relevance Check (GenAI Hackathon Project)")

# Upload job description
jd_file = st.file_uploader("📌 Upload Job Description (txt/docx/pdf)", type=["txt", "docx", "pdf"])

# Upload resume
resume_file = st.file_uploader("📌 Upload Resume (pdf/docx)", type=["pdf", "docx"])

# Button to run evaluation
if st.button("🚀 Check Relevance"):
    if jd_file and resume_file:
        st.success("✅ JD and Resume uploaded successfully!")
        st.info("👉 Scoring logic will come here in Step 2...")
    else:
        st.warning("⚠ Please upload both JD and Resume")