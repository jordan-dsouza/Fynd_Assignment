import streamlit as st
import pandas as pd
from llm import call_llm
from storage import load_data
import time

st.set_page_config(page_title="Admin Dashboard", layout="wide")
st.title("Admin Dashboard")

time.sleep(5)
st.rerun()

# Load submissions
data = load_data()

if not data:
    st.info("No submissions yet.")
else:
    # Prepare lists for AI-generated summary and actions
    summaries = []
    actions = []

    st.info("Generating AI summaries and recommended actions...")

    # Iterate through entries (oldest first)
    for entry in data:
        review_text = entry["review"]
        summary = call_llm(f"Summarize this customer review in one sentence:\n{review_text}")
        action = call_llm(f"""
You are a customer support assistant.

Customer review:
{review_text}

Write ONE concise, professional recommended action for the business in response.
Rules:
- Do NOT repeat or paraphrase the review text
- Keep it 1 sentence only
- Positive reviews → thank the customer
- Negative reviews → apologize and indicate a corrective step
""")


        summaries.append(summary.strip())
        actions.append(action.strip())

    # Create DataFrame
    df = pd.DataFrame({
        "Rating": [entry['rating'] for entry in data],
        "Review": [entry['review'] for entry in data],
        "AI Summary": summaries,
        "Recommended Action": actions,
        "Timestamp": [entry.get('timestamp', '') for entry in data]
    })

    # Display newest first
    st.dataframe(df[::-1], width=1200, height=600)
if st.button("Refresh"):
    st.rerun()

