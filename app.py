
import streamlit as st
from transformers import pipeline

# Load AI models
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
qa_gen = pipeline("text2text-generation", model="valhalla/t5-base-qg-hl")

st.set_page_config(page_title="SmartNotes AI")
st.title("🧠 SmartNotes AI")
st.subheader("Summarize your notes & generate quizzes")

text = st.text_area("Enter your lecture notes or textbook text below")

if st.button("Summarize"):
    with st.spinner("Generating summary..."):
        result = summarizer(text, max_length=150, min_length=40, do_sample=False)
        st.write("### ✅ Summary:")
        st.success(result[0]['summary_text'])

if st.button("Generate Quiz"):
    with st.spinner("Generating quiz..."):
        result = qa_gen("generate questions: " + text)
        st.write("### 📝 Quiz Questions:")
        st.write(result[0]['generated_text'])
