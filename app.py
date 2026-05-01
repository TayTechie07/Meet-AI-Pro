import streamlit as st
from utils import extract_text
from u2 import analyze_transcript

st.set_page_config(page_title="MeetMind AI", layout="wide")

st.title("🧠 MeetMind AI Pro")
st.caption("Turn messy meetings into structured intelligence")

uploaded_file = st.file_uploader("Upload Transcript (PDF or TXT)")

if uploaded_file:

    text = extract_text(uploaded_file)

    st.subheader("📄 Extracted Text")
    st.write(text[:1000])

    if st.button("Analyze Meeting"):

        with st.spinner("Analyzing with AI..."):
            result = analyze_transcript(text)

        st.success("Analysis Complete")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("✅ Action Items")
            for a in result["actions"]:
                st.write(a)

        with col2:
            st.subheader("🚧 Blockers")
            for b in result["blockers"]:
                st.write(b)

        with col3:
            st.subheader("📌 Decisions")
            for d in result["decisions"]:
                st.write(d)