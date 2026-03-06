import streamlit as st
from transformers import pipeline

st.title("AIParent – Emotion & Harm Detection System")

st.write("Analyze text for emotional tone and harmful/toxic content.")

# Load models only once
@st.cache_resource
def load_models():

    emotion_model = pipeline(
        "text-classification",
        model="joeddav/distilbert-base-uncased-go-emotions-student",
        top_k=None
    )

    toxicity_model = pipeline(
        "text-classification",
        model="unitary/toxic-bert"
    )

    return emotion_model, toxicity_model


emotion_model, toxicity_model = load_models()

# Input box
text = st.text_area("Enter text")

# Analyze button
if st.button("Analyze"):

    if text.strip() == "":
        st.warning("Please enter some text")

    else:

        # Emotion Prediction
        emotion_results = emotion_model(text)

        # emotion_results returns list -> take first element
        emotion_scores = emotion_results[0]

        # get emotion with highest score
        top_emotion = max(emotion_scores, key=lambda x: x["score"])

        st.subheader("Emotion Prediction")
        st.write(f"Emotion: {top_emotion['label']}")
        st.write(f"Confidence: {top_emotion['score']:.2f}")

        # Toxicity Prediction
        toxicity_result = toxicity_model(text)[0]

        st.subheader("Toxicity Prediction")

        score = toxicity_result["score"]
        if toxicity_result["label"] == "toxic" and score > 0.5:
          st.error(f"Toxic Content Detected (Confidence: {score:.2f})")
        else:
          st.success(f"Non-Toxic Content (Confidence: {1-score:.2f})")