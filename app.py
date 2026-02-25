import streamlit as st
import requests

st.set_page_config(page_title="AI Study Buddy 2.0", page_icon="🎓")

st.title("🎓 AI-Powered Study Buddy 2.0")
st.markdown("Adaptive Learning Companion using AI")

option = st.selectbox(
    "Select Feature",
    ["Explain Concept", "Summarize Notes", "Generate Quiz"]
)

user_input = st.text_area("Enter your topic or study notes here:")

def get_response(prompt):
    api_url = "https://api-inference.huggingface.co/models/google/flan-t5-small"
    headers = {"Authorization": f"Bearer {st.secrets['HF_API_KEY']}"}
    payload = {"inputs": prompt}
    response = requests.post(api_url, headers=headers, json=payload)
    return response.json()

if st.button("Generate Output"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Processing with AI..."):

            if option == "Explain Concept":
                prompt = f"Explain in simple language: {user_input}"
            elif option == "Summarize Notes":
                prompt = f"Summarize this text: {user_input}"
            elif option == "Generate Quiz":
                prompt = f"Generate 3 MCQ questions from: {user_input}"

            result = get_response(prompt)

            try:
                st.success("Output:")
                st.write(result[0]["generated_text"])
            except:
                st.error("Error generating response. Check API key.")

st.markdown("---")
st.markdown("Built using Streamlit & Hugging Face API")
