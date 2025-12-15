import streamlit as st
from llm import call_llm
from storage import save_entry

st.set_page_config(page_title="User Feedback", layout="centered")
st.title("User Feedback")

# Dropdown box:
rating = st.selectbox("Select Rating", [1, 2, 3, 4, 5])
# Text box:
review = st.text_area("Write your review")

# Submit button:
if st.button("Submit"):
    # If no review:
    if review.strip() == "":
        st.warning("Please write a review.")
    else:
        prompt = f"""
You are a customer support agent replying to a customer.

Customer review:
{review}

Do NOT repeat or paraphrase the review.
Write a short, polite response directly to the customer.
"""


        ai_response = call_llm(prompt)

        save_entry({
            "rating": rating,
            "review": review,
            "ai_response": ai_response
        })

        st.success("Review submitted!")
        st.subheader("AI Response")
        st.write(ai_response)