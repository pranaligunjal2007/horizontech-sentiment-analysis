import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="😊"
)

analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = analyzer.polarity_scores(text)["compound"]

    if score >= 0.05:
        return "Positive 😊"
    elif score <= -0.05:
        return "Negative 😞"
    else:
        return "Neutral 😐"

st.title("Sentiment Analysis of Customer Reviews")

st.write(
    "Enter a customer review to classify it as Positive, Negative, or Neutral."
)

review = st.text_area(
    "Customer Review",
    placeholder="Enter a customer review here..."
)

if st.button("Analyze Sentiment"):
    if review.strip():
        sentiment = get_sentiment(review)
        st.success(f"Sentiment: {sentiment}")
    else:
        st.warning("Please enter a review.")
