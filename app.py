import streamlit as st
from utils.speech_to_text import speech_to_text
from model.sentiment import predict_sentiment
from model.sarcasm import predict_sarcasm
from utils.preprocess import preprocess_text

st.set_page_config(page_title="AI Sentiment & Sarcasm Detector")

st.title("🎤 Voice-Based Sentiment & Sarcasm Detection")

audio_file = st.file_uploader("Upload your voice file", type=["wav", "mp3"])

if audio_file is not None:
    st.audio(audio_file)

    text = speech_to_text(audio_file)
    cleaned_text = preprocess_text(text)

    st.write("📝 Original Text:", text)
    st.write("🧹 Cleaned Text:", cleaned_text)

    sentiment = predict_sentiment(cleaned_text)
    sarcasm = predict_sarcasm(cleaned_text)

    st.markdown("### 📊 Analysis Result")

    col1, col2 = st.columns(2)

    with col1:
        if "Positive" in sentiment:
            st.success(f"😊 Sentiment: {sentiment}")
        elif "Negative" in sentiment:
            st.error(f"😡 Sentiment: {sentiment}")
        else:
            st.info(f"😐 Sentiment: {sentiment}")

    with col2:
        if "Sarcastic" in sarcasm:
            st.warning(f"😏 Sarcasm: {sarcasm}")
        else:
            st.success(f"🙂 Sarcasm: {sarcasm}")