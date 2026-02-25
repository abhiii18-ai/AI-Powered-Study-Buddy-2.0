
import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Study Buddy 2.0", page_icon="🎓")

st.title("🎓 AI-Powered Study Buddy 2.0")
st.markdown("An Adaptive Learning Companion using Generative AI")

@st.cache_resource
def load_models():
    generator = pipeline("text2text-generation", model="google/flan-t5-base")
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return generator, summarizer

generator, summarizer = load_models()

option = st.selectbox(
    "Select Feature",
    ["Explain Concept", "Summarize Notes", "Generate Quiz"]
)

user_input = st.text_area("Enter your topic or study notes here:")

if st.button("Generate Output"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Processing with AI..."):

            if option == "Explain Concept":
                prompt = f"Explain the following concept in simple student-friendly language:\n{user_input}"
                result = generator(prompt, max_length=200)
                st.success("Explanation:")
                st.write(result[0]['generated_text'])

            elif option == "Summarize Notes":
                result = summarizer(user_input, max_length=150, min_length=40)
                st.success("Summary:")
                st.write(result[0]['summary_text'])

            elif option == "Generate Quiz":
                prompt = f"Generate 3 multiple choice questions with options from the topic:\n{user_input}"
                result = generator(prompt, max_length=250)
                st.success("Quiz:")
                st.write(result[0]['generated_text'])

st.markdown("---")
st.markdown("Built using Python, Streamlit & Hugging Face | IBM SkillsBuild Capstone")
