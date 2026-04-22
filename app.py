import streamlit as st
import sqlite3
from dotenv import load_dotenv
import os
from openai import OpenAI

# ----------------------
# Load environment variables
# ----------------------
load_dotenv()

# ----------------------
# Streamlit page setup
# ----------------------
st.set_page_config(page_title="Healthcare chatbot", page_icon="🏥", layout="wide")
st.title("🏥Healthcare chatbot ")
st.write("Ask me the questions!!")

# ----------------------
# Connect to SQLite database
# ----------------------
DB_FILE = "healthcare_large.db"

def run_query(query):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        return f"Database error: {e}"

# ----------------------
# OpenAI Client Setup
# ----------------------
token = os.getenv("GITHUB_TOKEN")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

def get_chatgpt_response(prompt: str):
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful healthcare assistant chatbot."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            top_p=1,
            model=model
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"ChatGPT error: {e}"

# ----------------------
# Chat UI
# ----------------------
if "history" not in st.session_state:
    st.session_state["history"] = []

question = st.text_input("Your Question:")

if st.button("Ask"):
    if question.strip():
        with st.spinner("Thinking..."):
            # First try DB
            db_result = run_query(question)
            if isinstance(db_result, list) and db_result:
                answer = "\n".join(str(r) for r in db_result)
            else:
                # If DB has no answer, fallback to ChatGPT
                answer = get_chatgpt_response(question)

            st.session_state["history"].append((question, answer))
            st.success(answer)

# Display chat history
if st.session_state["history"]:
    st.subheader("Chat History")
    for i, (q, a) in enumerate(st.session_state["history"], 1):
        st.markdown(f"**Q{i}:** {q}")
        st.markdown(f"**A{i}:** {a}")
        st.write("---")
