from pathlib import Path
import streamlit as st
from utils import SentimentPredictor

MODEL_PATH = Path(__file__).parent / "sentiment_classifier.joblib"
LABELS = {0: "negative", 1: "positive"}

@st.cache_resource
def get_predictor():
    return SentimentPredictor(str(MODEL_PATH), LABELS)

predictor = get_predictor()

st.title("Movie Review Sentiment Analysis")
text = st.text_area("Enter a movie review (English)")

if st.button("Classify"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        result = predictor.run(text)
        if result == "Positive":
            st.success("Positive 😀")
        elif result == "Negative":
            st.error("Negative 😞")
        else:
            st.info("Could not classify this text. Try a longer English review.")