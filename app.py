import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)
st.set_page_config(
    page_title="Gemini AI Chatbot",
    layout="centered"
)
st.title("✨ Gemini AI Chatbot")
st.write("Ask Gemini anything!")
prompt=st.text_area(
    "Enter your prompt:",
    placeholder="Explain Artificial Intelligence in simple words..."
)
if st.button("Generate Response"):
    if prompt:
        with st.spinner("Gemini is thinking..."):
            response=client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )
        st.success("Response generated!")
        st.write(response.text)
    else:
        st.warning("Please enter a prompt.")
