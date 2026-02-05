import streamlit as st
import requests
import os

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]


st.set_page_config(page_title="Text Summarizer", layout="centered")

st.title("📝 Groq Text Summarizer")

def summarize_text(text, instruction):

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
Summarize according to this instruction: {instruction}

{text}
"""

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    response = requests.post(url, headers=headers, json=payload)

    result = response.json()

    return result["choices"][0]["message"]["content"]

# ---------- UI ----------

text = st.text_area("Enter your content")

instruction = st.text_input("Instruction (example: 50 words)")

if st.button("Summarize"):

    if not text or not instruction:
        st.warning("Please enter both fields")

    else:
        with st.spinner("Summarizing..."):
            try:
                summary = summarize_text(text, instruction)
                st.success("Done!")
                st.write(summary)

            except Exception as e:
                st.error("Something went wrong")
                st.code(str(e))
