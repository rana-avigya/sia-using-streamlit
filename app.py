import streamlit as st 
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download("vader_lexicon")
st.title("sentiment intensity analyzer")
sia = SentimentIntensityAnalyzer()

text = st.text_area("enter text")
if st.button("Analyze"):
    st.write(sia.polarity_scores(text))